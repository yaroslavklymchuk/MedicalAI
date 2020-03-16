import logging
from logging import FileHandler


logger = logging.getLogger('Medical AI')
# writes to pathToLog
# creates a new file every day because when="d" and interval=1
# automatically deletes logs more than 3 days old because backupCount=3
#
handler = FileHandler('./logs/medical_ai.log')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s:%(filename)s:%(lineno)d %(message)s', "%Y-%m-%d %H:%M:%S")
ch.setFormatter(formatter)
logger.addHandler(ch)
handler.setFormatter(formatter)
logger.addHandler(handler)
