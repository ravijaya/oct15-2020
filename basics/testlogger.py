from customlogconfig import logger
from time import sleep


for item in range(1, 11):
    logger.debug(f'dummy log content : {item}')
    sleep(.5)