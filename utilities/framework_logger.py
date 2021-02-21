"""
This file may not be required as pytest has internal logging feature which can be modified using pytest.ini file.
"""
import os
import logging
from conftest import ROOT_DIR


def get_logger(name):
    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create a stream handler
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    log_file = os.path.join(ROOT_DIR, f'reports/logs/{name}.log')
    fh = logging.FileHandler(filename=log_file, mode='w')
    fh.setLevel(logging.DEBUG)

    # create a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

    # add formatter to stream handler
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add sh to logger
    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.info('='*50)
    logger.info(f'TEST NAME: {name}')
    logger.info(f"ROOT_DIR: {ROOT_DIR}")
    logger.info('='*50)
    return logger