import os
import subprocess


def get_number_file(path):
    return len(os.listdir(path))


def make_dirs(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def write_audio_file(file, user_id):
    path = f'media/audio/{user_id}/oga'

    make_dirs(path)

    number = get_number_file(path)
    filename = f'audio_message_{number}'

    with open(f'{path}/{filename}', 'wb') as f:
        f.write(file)

    return f'{path}/{filename}'


def convert_from_opus(file_src, dest, filename):
    subprocess.run(['ffmpeg', '-i', file_src, f'{dest}/{filename}.wav'])


def convert_audio_file(file_src, user_id):
    dest = f'media/audio/{user_id}/wav'
    filename = file_src.split('/')[-1]

    make_dirs(dest)

    convert_from_opus(file_src, dest, filename)






