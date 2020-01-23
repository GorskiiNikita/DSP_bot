import json

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

from core.telegram_api import invoke_telegram


@csrf_exempt
def telegram_hook(request):
    update = json.loads(request.body)
    invoke_telegram('sendMessage', chat_id=update['message']['chat']['id'], text='OK')

    return HttpResponse('OK')