import logging

logging.basicConfig(
    filename='quizwiz.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger()
