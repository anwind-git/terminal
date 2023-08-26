import logging
import sys

logging.basicConfig(level=logging.INFO, filename='loger.log', filemode='a',
                    format='%(asctime)s, %(levelname)s, %(message)s')


logger = logging.getLogger()

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s, %(levelname)s, %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)