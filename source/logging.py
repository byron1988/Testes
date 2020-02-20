import logging


format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename="hello.log", level=logging.DEBUG, filemode="w", format=format)
logger = logging.getLogger(__file__)

logger.info("Mensagem informativa")
logger.debug("Mensagem de debug")
logger.error("Um erro aconteceu.")