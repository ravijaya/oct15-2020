import logging

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
fmt = logging.Formatter(fmt_str)   # what to log?


sh = logging.StreamHandler()   # to log at console
fh = logging.FileHandler(filename='access.log')

sh.setFormatter(fmt)
fh.setFormatter(fmt)

logger = logging.getLogger('abb')
logger.setLevel(level=logging.DEBUG)

logger.addHandler(sh)
logger.addHandler(fh)

