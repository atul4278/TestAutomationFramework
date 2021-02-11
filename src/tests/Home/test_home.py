from src.utilities.framework_logger import get_logger
from src.pages.product.actions import ProductPageLocators, ProductsPageActions

class TestHome:
    def test_home1(self):
        page = ProductsPageActions(self.driver)
        page.log.info(f'Logging Test 1')

    def test_home2(self):
        page = ProductsPageActions(self.driver)
        page.log.info(f'Logging Test 2')

    # def test_home3(self):
    #     logging.info(f'Logging Test 3')

    # def test_home4(self):
    #     logging.info(f'Logging Test 4')

    # def test_home5(self):
    #     logging.info(f'Logging Test 5')

    # def test_home6(self):
    #     logging.info(f'Logging Test 6')
