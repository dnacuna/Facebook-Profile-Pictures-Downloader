import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('facebook-deep-learning')
handler = logging.FileHandler('facebook-profile-picture-grabber.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(thread)d - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logging.getLogger("requests").setLevel(logging.WARNING)


def log(string):
    logger.log(logging.INFO, string)
