from selenium import webdriver
import threading
import requests
import random
import time
import os
import ctypes
import sys
import webbrowser
import subprocess
from time import sleep
from os import system
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from colorama import Fore, Back, Style


aimmail = input('What is the email i will message: ')
message = input('What message should it send: ')
length = 10
lengthd = 13
symbols = ascii_letters
secure_random = random.SystemRandom()

opts = webdriver.ChromeOptions()
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
opts.add_argument('--disable-extensions')
opts.add_argument('--profile-directory=Default')
opts.add_argument("--incognito")
opts.add_argument("--disable-plugins-discovery")
#opts.add_argument("--headless")
opts.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"')
opts.add_argument("--mute-audio")
while True:
    driver = webdriver.Chrome('chromedriver.exe', options=opts)

    username = "".join(secure_random.choice(symbols)
        for i in range(length))
    password = "".join(secure_random.choice(symbols)
        for i in range(length))
    email = "".join(secure_random.choice(symbols)
         for i in range(lengthd))
    with open(r"emails.txt", "a") as f:
        f.write(email + "@sharklasers.com" + " <--- was the email used to message " + aimmail + "\n")
    driver.get('https://www.guerrillamail.com/compose')

    driver.find_element_by_xpath('//*[@id="forget_button"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="inbox-id"]/input').send_keys(email + Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="nav-item-compose"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="send-form"]/div[2]/div/input[1]').send_keys(aimmail)
    driver.find_element_by_xpath('//*[@id="send-form"]/div[2]/div/input[2]').send_keys('email')
    driver.find_element_by_xpath('//*[@id="send-form"]/div[4]/textarea').send_keys(message + " Tool by Node#9999")
    driver.find_element_by_xpath('//*[@id="send-button"]').click()
    pageurl = 'https://www.guerrillamail.com/compose'

    site_key = "6LcIHdESAAAAALVQtprzwjt2Rq722tkxk-RDQ0aN"

    with open(r"api_key.txt", "r") as f:
        api_key = f.read()

    form = {"method": "userrecaptcha",
            "googlekey": site_key,
            "key": api_key, 
            "pageurl": pageurl, 
            "json": 1}

    response = requests.post('http://2captcha.com/in.php', data=form)
    request_id = response.json()['request']

    url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"
    status = 0
    while not status:
        res = requests.get(url)
        if res.json()['status']==0:
            time.sleep(3)
        else:
            requ = res.json()['request']
            status = 1
    driver.execute_script(f'document.getElementById("g-recaptcha-response").value = "{requ}"')
    time.sleep(2)
    driver.close()
