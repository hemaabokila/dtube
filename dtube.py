#!/usr/bin/python3
from pytube import YouTube
from optparse import OptionParser
from tkinter import filedialog

def dowin(urll):
    try:
        all_stream = YouTube(urll).streams.get_highest_resolution()
        folder = filedialog.askdirectory()
        all_stream.download(folder)
        print("complite")
    except EnvironmentError as e:
            print(e)
pars= OptionParser("""
 _____  _______  _     _  _____   ______ 
(_____)(__ _ __)(_)   (_)(_____) (______)
(_)  (_)  (_)   (_)   (_)(_)__(_)(_)__   
(_)  (_)  (_)   (_)   (_)(_____) (____)  
(_)__(_)  (_)   (_)___(_)(_)__(_)(_)____ 
(_____)   (_)    (_____) (_____) (______)
---------------------------
dtube -u or --url + url
Developed by: Ibrahem abo kila
""")
pars.add_option("-u","--url",dest="s_url",type="string",help="enter url")
(options ,args) = pars.parse_args()
if options.s_url == None:
    print(pars.usage)
else:
    dowin(options.s_url)
