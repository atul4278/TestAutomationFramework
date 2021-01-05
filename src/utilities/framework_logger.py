"""
This file is not required as pytest has internal logging feaure which can be modified using pytest.ini file.
"""

import logging
import inspect

def get_logger(name):
    # create logger
    # x = inspect.stack()
    # name = x[2].filename
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create a stream handler
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    fh = logging.FileHandler(filename=f'src/reports/logs/{name}.log', mode='a')
    fh.setLevel(logging.DEBUG)

    # create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to stream handler
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add sh to logger
    logger.addHandler(sh)
    logger.addHandler(fh)
    return logger