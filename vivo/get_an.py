import logging

from vivo.config import settings


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(settings.LOG_LEVEL)


def get_an(num_list):
    try:
        record = {}
        for expected_num in range(16):
            record[expected_num] = 0
        for num in num_list:
            if num < 0 or num > 15:
                raise Exception('Number should be between 0 and 15')
            record[num] += 1
        return str(record)
    except Exception as e:
        logger.error(e, exc_info=True)
