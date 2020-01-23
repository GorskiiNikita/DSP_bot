import requests
import logging

from DSP_bot import settings


logger = logging.getLogger(__name__)

def invoke_telegram(method, **kwargs):
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/{method}"
    resp = requests.post(url, data=kwargs, timeout=(3.05, 27), proxies=settings.PROXY)
    logger.info("Response %s %s" % (resp, resp.content))
    return resp