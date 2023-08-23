import pytube
from pytube import YouTube

url = input("enter video url: ")

path = ""

stream = pytube.YouTube(url).streams.get_by_resolution('720p').download(path)
