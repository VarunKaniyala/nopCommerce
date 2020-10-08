import logging

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler('logfile.log')
logger.addHandler(fileHandler)
logger.debug("A debug statement is executed")
logger.info("information statement")
logger.warning("Something is in warning mode")
logger.error("A major error has happened")
logger.critial("Critical issue")

