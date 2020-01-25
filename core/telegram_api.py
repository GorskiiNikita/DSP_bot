import requests
import logging

from DSP_bot import settings


URL = 'https://api.telegram.org'
logger = logging.getLogger(__name__)


def invoke_telegram(method, **kwargs):
    url = f"{URL}/bot{settings.TELEGRAM_BOT_TOKEN}/{method}"
    resp = requests.post(url, data=kwargs, timeout=(3.05, 27), proxies=settings.PROXY)
    logger.info("Response %s %s" % (resp, resp.content))
    return resp


def download_file(file_path):
    resp = requests.get(f'{URL}/file/bot{settings.TELEGRAM_BOT_TOKEN}/{file_path}', proxies=settings.PROXY)
    return resp.content
