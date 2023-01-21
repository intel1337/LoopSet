from pytube import YouTube
import os
import time
import sys
import colorama
from colorama import Fore

def menu():
    global onstart
    print(f"""
    
    
{Fore.WHITE}██╗      ██████╗  ██████╗ {Fore.RED}██████╗ ███████╗███████╗████████╗
{Fore.WHITE}██║     ██╔═══██╗██╔═══██╗{Fore.RED}██╔══██╗██╔════╝██╔════╝╚══██╔══╝
{Fore.WHITE}██║     ██║   ██║██║   ██║{Fore.RED}██████╔╝███████╗█████╗     ██║   
{Fore.WHITE}██║     ██║   ██║██║   ██║{Fore.RED}██╔═══╝ ╚════██║██╔══╝     ██║   
{Fore.WHITE}███████╗╚██████╔╝╚██████╔╝{Fore.RED}██║     ███████║███████╗   ██║   
{Fore.WHITE}╚══════╝ ╚═════╝  ╚═════╝ {Fore.RED}╚═╝     ╚══════╝╚══════╝   ╚═╝ 


                        [download]                       
    
    """)
    cmd = input("LoopSet@$> ")
    if cmd == "download":
        mp = input("mp4 or mp3 >")
        qu = input("4320p / 2160p / 1440p / 1080p / 720p / 480p / 360p / 240p / 144p >")
        url = input("Enter the URL of the YouTube video >")
        yt = YouTube(url)
        streams = yt.streams.filter(file_extension=mp, resolution=qu)
        stream = streams.first()
        stream.download()
        onstart()


def onstart():
    os.system("cls && title LoopSet - Python")
    menu()

onstart()