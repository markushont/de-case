import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y%m%d %I:%M:%S'
)

class LoggerFactory:
    @staticmethod
    def create_logger(name='main', level=logging.INFO):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        return logger
