import cv2
import os
import random
import textwrap
import requests
import re

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

height = int(1920)
width = int(1080)

length = 10  # length of the video in seconds

number_of_videos = 10  # how many videos (maximum 10 at a time)============================================================


def simplify_text(text):
    def replace_unicode_escape(match):
        return chr(int(match.group(1), 16))
    
    # Use regular expression to find Unicode escape sequences and replace them
    simplified_text = re.sub(r'\\u([0-9a-fA-F]{4})', replace_unicode_escape, text)
    return simplified_text


def API_Call(limit):

    api_url = "https://api.api-ninjas.com/v1/dadjokes?limit={}".format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR API KEY'})

    if response.status_code == requests.codes.ok:
        final = []
        text = response.text
        list = text.split('}')
        for text_list in list:
            final.append(text_list[11:-2])
        return final
    else:
        print("Error:", response.status_code, response.text)

Jokes = API_Call(number_of_videos)

def textFormater(text=str):
    text_ = simplify_text(text)
    wrapper = textwrap.TextWrapper(width=10)
    string = ''
    wrapped = wrapper.wrap(text_)
    return wrapped

def imagePathGenerator():

    imgPaths = []
    
    for root,dirs,files in os.walk('C:/Users/Pahul/python/API Project/images'):  # paths of the background images
        for file in files:
            print(root)
            imgPath = root+'/'+ file  # path of a single image
            imgPaths.append(imgPath)

    return imgPaths 

def image_to_video(seconds,number_of_vids=1):
    frames = int(seconds)
    paths = imagePathGenerator()
    
    for num in range(number_of_vids):
        print(f'initializing video {num+1}...')
        image_path = random.choice(paths)
        frame = cv2.imread(image_path)

        text = textFormater(Jokes[num])
        for i,t in enumerate(text):
            cv2.putText(frame, f'{t}',(int(0/5),(int((i+1)*140))),cv2.FONT_HERSHEY_SIMPLEX,5,(240,245,245),9)

        out = cv2.VideoWriter(f'C:/Users/Pahul/python/API Project/images/Videos/{num+1}.mp4',fourcc,1,(width,height))
        for i in range(frames):
            out.write(frame)
        print('Video',num+1,'Completed')


image_to_video(length,number_of_videos)