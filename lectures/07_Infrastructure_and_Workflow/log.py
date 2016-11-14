import logging


logger = logging.getLogger('park')
logger.setLevel(logging.DEBUG)  # А если поменять на WARNING?

lite_handler = logging.StreamHandler()
lite_handler.setLevel(logging.DEBUG)  # А если тут?

formatter = logging.Formatter('lite [%(name)s] %(levelname)s: %(asctime)s - %(message)s')
lite_handler.setFormatter(formatter)

logger.addHandler(lite_handler)

# heavy_handler = logging.StreamHandler()
# heavy_handler.setLevel(logging.ERROR)
#
# formatter = logging.Formatter('heavy [%(name)s] %(levelname)s: %(asctime)s - %(message)s')
# heavy_handler.setFormatter(formatter)
#
# logger.addHandler(heavy_handler)


logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')


# try:
#     1 / 0
# except ZeroDivisionError:
#     logger.exception('What could go wrong?')
