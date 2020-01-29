import os
import subprocess
import soundfile as sf
import scipy.signal
import numpy as np
import cv2


def get_number_file(path):
    return len(os.listdir(path))


def make_dirs(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def convert_from_opus(file_src, dest, filename):
    subprocess.run(['ffmpeg', '-i', file_src, f'{dest}/{filename}.wav'])


def write_audio_file(file, user_id):
    path = f'media/audio/{user_id}/oga'
    make_dirs(path)
    number = get_number_file(path)
    filename = f'audio_message_{number}'
    with open(f'{path}/{filename}', 'wb') as f:
        f.write(file)
    return f'{path}/{filename}'


def convert_audio_file(file_src, user_id):
    dest = f'media/audio/{user_id}/wav'
    filename = file_src.split('/')[-1]
    make_dirs(dest)
    convert_from_opus(file_src, dest, filename)
    audio_data, samplerate = sf.read(f'{dest}/{filename}.wav')
    new_audio_data = scipy.signal.decimate(audio_data, samplerate//16000)
    sf.write(f'{dest}/{filename}.wav', new_audio_data, 16000)


def found_faces_on_image(img):
    nparr = np.fromstring(img, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.3,
                                         minNeighbors=3,
                                         minSize=(30, 30))
    return len(faces)


def save_image(img, user_id):
    path = f'media/photo/{user_id}'
    make_dirs(path)
    number = get_number_file(path)
    filename = f'photo_{number}.jpg'
    with open(f'{path}/{filename}', 'wb') as f:
        f.write(img)












