import json

import pytest

from core.driver_manager import DriverManager
from utilities import framework_logger as logger


def pytest_addoption(parser):
    parser.addoption("--browser", action='store',default="chrome", help="browser used for execution")
    parser.addoption("--remote", action='store', default=False, help="Run on local or remote. Default is local.")


@pytest.fixture(scope='session', autouse=True)
def data():
    with open('./config/framework.settings.json') as f:
        dataObj = json.load(f)

    return dataObj


@pytest.fixture(scope='function', autouse=True)
def driver(request, data, pytestconfig):
    brwsr = request.config.option.browser
    remote = request.config.option.remote
    driver = DriverManager.get_driver(brwsr, remote)
    request.cls.driver = driver
    request.cls.data = data
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def launch_sausedemo(driver, data):
    print('Launching App....')
    driver.get(data['appUrl'])

def pytest_html_report_title(report):
    report.title = "Regression Results"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extra = extra