import requests
import logging

from DSP_bot import settings


URL = 'https://api.telegram.org'
logger = logging.getLogger(__name__)


# Для Российских серверов нужно добавить параметр proxies в requests.post()
def invoke_telegram(method, **kwargs):
    #
    resp = requests.post(f'{URL}/bot{settings.TELEGRAM_BOT_TOKEN}/{method}', data=kwargs)
    logger.info('Response %s %s' % (resp, resp.content))
    return resp


def download_file(file_path):
    resp = requests.get(f'{URL}/file/bot{settings.TELEGRAM_BOT_TOKEN}/{file_path}')
    return resp.content
