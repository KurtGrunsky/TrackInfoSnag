#TrackInfoSnag v.5
#by Kurt Grunsky
#Feb. 24th, 2019

import re
import sys
import requests
import os
import mutagen
import mutagen.id3
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from tkinter import *

global g_container
global g_entry
global g_query

#var = ""

"""def get_queryab(): #Function that opens an input box and saves the contents to a temporary file for use in the main program
    g_container = Tk()
    label = Label(g_container, text="Are you using Spotify or Discogs as a source?")
    label.pack()
    def ok_button_clicka():
        file = open("temp_response.txt", "w")
        file.write("a")
        file.close()
        g_container.destroy()
    def ok_button_clickb():
        file = open("temp_response.txt", "w")
        file.write("b")
        file.close()
        g_container.destroy()
    a_button = Button(g_container, text="Spotify", command=ok_button_clicka)
    a_button.pack()
    b_button = Button(g_container, text="Discogs", command=ok_button_clickb)
    b_button.pack()
    mainloop()"""

def get_query(): #Function that opens an input box and saves the contents to a temporary file for use in the main program
    g_container = Tk()
    label = Label(g_container, text="Enter the URL of the album:")
    label.pack()
    g_entry = Entry(g_container)
    g_entry.pack()
    def ok_button_click():
        content = g_entry.get()
        temp_file = open("temp_url.txt", "w")
        temp_file.write(content)
        temp_file.close()
        g_container.destroy()
    goodbye_button = Button(g_container, text="OK", command=ok_button_click)
    goodbye_button.pack()
    mainloop()

def get_querya(): #Function that opens an input box and saves the contents to a temporary file for use in the main program
    g_container = Tk()
    label = Label(g_container, text="Directory name:")
    label.pack()
    g_entry = Entry(g_container)
    g_entry.pack()
    def aok_button_click():
        content = g_entry.get()
        temp_file = open("temp_dir.txt", "w")
        temp_file.write(content)
        temp_file.close()
        g_container.destroy()
    goodbye_button = Button(g_container, text="OK", command=aok_button_click)
    goodbye_button.pack()
    mainloop()

"""def specialCharReplace(LLL):
    for x in LLL:
        if "&#038;" in x:
            LLL[LLL.index(x)] = x.replace("&#038;", "&")
        if "&#039;" in x:
            LLL[LLL.index(x)] = x.replace("&#039;", "'")
        if '&#034;' in x:
            LLL[LLL.index(x)] = x.replace('&#034;', '"')"""

def specialCharReplaceB(LLL):
    for x in LLL:
        if "&#38;" in x:
            LLL[LLL.index(x)] = x.replace("&#38;", "&")
        if "&#39;" in x:
            LLL[LLL.index(x)] = x.replace("&#39;", "'")
        if '&#34;' in x:
            LLL[LLL.index(x)] = x.replace('&#34;', '"')


#filename = input("Enter the URL of the album: ")
#source_dir = input("Directory name: ")

"""get_queryab()

file = open("temp_response.txt", "r")
var = file.read()
file.close()"""

get_query()
get_querya()

count = 0
county = 0

file = open("temp_url.txt", "r")
url = file.read()

http_object = requests.get(url) #this imports the html from the URL
raw_html = http_object.content
s_content = raw_html.decode('utf-8') #this decodes the raw html
li = s_content

"""if var == "a":
    li = re.split('"><', li)
    for x in li:
        if "tracklist-col__track-number position middle-align" in x:
            li = li[li.index(x):]
            break
    for x in li:
        if "{" in x:
            li = li[:li.index(x)]
            break
    lu = []
    print(li)
    for x in li:
        if 'tracklist-name ellipsis-one-line" dir="auto"' or 'span class="track-name"' in x:
            lu.append(x)
    la = []
    print(lu)
    for x in lu:
        la.append(re.split(">*<", x))
    le = []
    print(la)
    for x in la:
        le.append(x[0][35:])
    specialCharReplace(le)
    print(le)
elif var == "b":"""
li = re.split('"><', li)
for x in li:
    if 'table class="playlist"' in x:
        li = li[li.index(x):]
        break
for x in li:
    if 'class="artist' in x:
        li = li[:li.index(x)]
        break
la = []
for x in li:
    la.append(re.split(">*<", x))
lu = []
for x in la:
    for y in x:
        if 'span class="tracklist_track_title"' in y:
            lu.append(y)
le = []
for x in lu:
    le.append(x[35:])
specialCharReplaceB(le)


file.close()
file = open("temp_dir.txt", "r")
source_dir = file.read()

for name in os.listdir(source_dir):
    if name[-4:].lower() != ".mp3":
            continue
    if count >= len(le):
    	break
    path = os.path.join(source_dir, name)
    try:
            tag = EasyID3(path)
    except:
            tag = mutagen.File(path, easy=True)
            tag.add_tags()
    tag['title'] = le[count]
    tag.save(v2_version=3)
    count = count + 1

for name in os.listdir(source_dir):
    if name[-4:].lower() != ".mp3":
            continue
    path = os.path.join(source_dir, name)
    try:
            tag = EasyID3(path)
    except:
            tag = mutagen.File(path, easy=True)
            tag.add_tags()
    tag['tracknumber'] = str(county + 1)
    tag.save(v2_version=3)
    county = county + 1

file.close()
#exit = input(" ")

