import pyKey as pk
import time as t
from pynput.mouse import Button, Controller
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import codecs
import re
from webdriver_manager.firefox import DriverManager


mouse = Controller()
driver = webdriver.Firefox()
url = "https://theonlinemetronome.com/instrument-tuner"
driver.get(url)
button = driver.find_element(By.CLASS_NAME, "Tuner_StartTuningBtn__22Y_i")
button.click()
page_source = driver.page_source


while True:
    soup = BeautifulSoup(page_source,features='html.parser')
    matches = driver.find_element(By.CLASS_NAME, "Tuner_Frequency__Dm1Lk")
    freq = matches.text
    freq = freq.strip("Hz")
    freq = freq.strip(" ")
    if freq == "":
        freq = 0.00
    else:
        freq = float(freq)

        match freq:
        
            case freq if freq > 145.00 and freq < 150.00:
                pk.press(key='.', sec=0.5)
            case freq if freq > 155.00 and freq < 160.00:
                pk.pressKey("W")
                pk.pressKey("R")
                t.sleep(0.2)
                pk.releaseKey("R")
                pk.releaseKey("W")
            case freq if freq > 161.00 and freq < 170.00:
                pk.pressKey("A")
                t.sleep(0.2)
                pk.releaseKey("A")
            case freq if freq > 172.00 and freq < 178.00:
                pk.pressKey("S")
                t.sleep(0.2)
                pk.releaseKey("S")
            case freq if freq > 184.00 and freq < 187.00:
                pk.pressKey("D")
                t.sleep(0.2)
                pk.releaseKey("D")
            case freq if freq > 192.00 and freq < 196.00:
                pk.pressKey("P")
                t.sleep(0.2)
                pk.releaseKey("P")
            case freq if freq > 205.00 and freq < 209.00:
                pk.pressKey("O")
                t.sleep(0.2)
                pk.releaseKey("O")
            case freq if freq > 218.00 and freq < 223.00:
                pk.pressKey("L")
                t.sleep(0.2)
                pk.releaseKey("L")
            case freq if freq > 230.00 and freq < 239.00:
                pk.pressKey("K")
                t.sleep(0.2)
                pk.releaseKey("K")
            case freq if freq > 247.00 and freq < 252.00:
                pk.press(key='X', sec=0.3)
            case freq if freq > 260.00 and freq < 265.00:
                pk.press(key='H', sec=0.2)
            case freq if freq > 278.00 and freq < 283.00:
                pk.press(key='Q', sec=1)
            case freq if freq > 294.00 and freq < 300.00:
                mouse.move(20,0)
                t.sleep(0.3)
            case freq if freq > 310.00 and freq < 318.00:
                mouse.move(0,20)
                t.sleep(0.3)
            case freq if freq > 325.00 and freq < 335.00:
                mouse.move(-20,0)
                t.sleep(0.3)
            case freq if freq > 345.00 and freq < 355.00:
                mouse.move(0,-20)
                t.sleep(0.3)
            case freq if freq > 367.00 and freq < 380.00:
                mouse.scroll(1,0)
                t.sleep(0.5)
            case freq if freq > 410.00 and freq < 420.00:
                mouse.scroll(0,1)
                t.sleep(0.5)
            case freq if freq > 435.00 and freq < 450.00:
                pk.press(key='C',sec=1)
            case freq if freq > 465.00 and freq < 480.00:
                mouse.click(Button.left, 1)
                t.sleep(0.3)
            case freq if freq > 490.00 and freq < 500.00:
                mouse.click(Button.right, 1)
                t.sleep(0.3)
