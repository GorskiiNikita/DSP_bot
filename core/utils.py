import os


def get_number_file(path):
    return len(os.listdir(f'{path}/oga'))


def make_dirs(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def write_audio_file(file, user_id):
    path = f'media/audio/{user_id}'

    make_dirs(f'{path}/oga')
    make_dirs(f'{path}/wav')

    number = get_number_file(path)

    with open(f'media/audio/{user_id}/oga/audio_message_{number}', 'wb') as f:
        f.write(file)
