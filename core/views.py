import json

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

from core.telegram_api import invoke_telegram, download_file
from core.utils import write_audio_file, convert_audio_file


@csrf_exempt
def telegram_hook(request):
    update = json.loads(request.body)
    message = update.get('message')

    if message is not None and 'voice' in message.keys():
        user_id = message['from']['id']
        file_id = message['voice']['file_id']
        file_path = get_telegram_file_path(file_id)
        voice_message = download_file(file_path)
        file_src = write_audio_file(voice_message, user_id)
        convert_audio_file(file_src, user_id)

    invoke_telegram('sendMessage', chat_id=update['message']['chat']['id'], text='OK')

    return HttpResponse('OK')


def get_telegram_file_path(file_id):
    return json.loads(invoke_telegram('getFile', file_id=file_id).content)['result']['file_path']
