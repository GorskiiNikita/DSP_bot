import json

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

from core.telegram_api import invoke_telegram, download_file
from core.utils import write_audio_file, convert_audio_file, found_faces_on_image, save_image


@csrf_exempt
def telegram_hook(request):
    update = json.loads(request.body)
    message = update.get('message')
    text = None

    if message is None:
        return HttpResponse('OK')

    user_id = message['from']['id']

    if 'voice' in message.keys():
        file_id = message['voice']['file_id']
        file_path = get_telegram_file_path(file_id)
        voice_message = download_file(file_path)
        file_src = write_audio_file(voice_message, user_id)
        convert_audio_file(file_src, user_id)
        text = 'Your voice message saved'

    elif 'photo' in message.keys():
        file_id = message['photo'][-1]['file_id']
        file_path = get_telegram_file_path(file_id)
        img = download_file(file_path)
        count_faces = found_faces_on_image(img)
        if count_faces > 0:
            save_image(img, user_id)
            text = f'Found {count_faces} faces' if count_faces > 1 else f'Found {count_faces} face'
        else:
            text = 'Face not found '

    invoke_telegram('sendMessage', chat_id=update['message']['chat']['id'], text=text)

    return HttpResponse('OK')


def get_telegram_file_path(file_id):
    return json.loads(invoke_telegram('getFile', file_id=file_id).content)['result']['file_path']
