import random
from random import *
import random as random
import os
import threading
import requests
import win32console as wc
import colorama
from colorama import Fore

webhook_url = "N/A"
save = open("webhook.txt", "w+")
webhook = input(f"{Fore.BLUE}Please Paste Here The Discord Webhook{Fore.WHITE} --> ")
webhook_url = webhook
    

username = input(f"{Fore.BLUE}Enter The Bot's Name To Continue{Fore.WHITE} --> ")
appname = username


while True:
    content = input(f"{Fore.GREEN}Message or Command here{Fore.WHITE} --> ")
    if content == "!break app":
        print(f"{Fore.RED}Ok Breaking The App{Fore.WHITE}")
        break
    elif content == "!randnum":
        num = randint(1, 1000)
        requests.post(webhook_url, json={"content": num, "username": appname})
        print(f"{Fore.MAGENTA}You Used Command: Random Number Generator")
    elif content == "!basicpy":
        requests.post(webhook_url, json={"content": "Easteregg: app Maded By Kókai Balázs", "username": "Basic py"})
        print(f"{Fore.MAGENTA}You Founded An Easteregg!")
    elif content == "!changename":
        newname = input(f"{Fore.BLUE}Enter The New Name Of The App{Fore.WHITE} --> ")
        appname = newname
    elif content == "!changewebhook":
        new = input(f"{Fore.BLUE}Paste Here The New Webhook{Fore.WHITE} --> ")
        webhook_url = new
    else:
        requests.post(webhook_url, json={"content": content, "username": appname})
