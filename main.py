from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import uniform
from keyboard import is_pressed
from os import _exit
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from math import ceil


NAME = ""  # your typewriter-name
PASSWORT = ""  # your typewriter-name
DRIVER = webdriver.Chrome()
DRIVER.get("https://at4.typewriter.at/index.php?r=site/login")
EXIT_KEY = "strg"
DELAY = uniform(0.15, 0.17)
MISTAKE_PERCENT = 0.02
TOTAL_MISTAKE_AMOUNT = None
TOTAL_LETTER_AMOUNT = None


def getItemIfExists(strategy, selector):
    try:
        return WebDriverWait(DRIVER, timeout=10).until(
            EC.visibility_of_element_located((strategy, selector)))
    except TimeoutException:
        return None


def acceptCookies():
    cookies = getItemIfExists(By.CSS_SELECTOR, ".fc-cta-consent")
    if cookies:
        cookies.click()


def writeUsername():
    usernameInterface = getItemIfExists(By.NAME, "LoginForm[username]")
    if usernameInterface:
        usernameInterface.send_keys(NAME)


def writePasswort():
    passwortInterface = getItemIfExists(By.NAME, "LoginForm[pw]")
    if passwortInterface:
        passwortInterface.send_keys(PASSWORT)


def submitLogin():
    loginButton = getItemIfExists(By.ID, "login-submit-btn")
    if loginButton:
        loginButton.click()


def openLesson():
    lessonButton = getItemIfExists(By.CLASS_NAME, "image")
    if (lessonButton):
        lessonButton.click()


def startLesson():
    startLessonButton = getItemIfExists(By.XPATH, "//button[text()='Start']")
    if startLessonButton:
        startLessonButton.click()


def getMistakes():
    global TOTAL_LETTER_AMOUNT
    global TOTAL_MISTAKE_AMOUNT
    letter = DRIVER.find_element(
        By.CSS_SELECTOR, "#text_todo_1 > span").text
    typeLetter(letter)
    TOTAL_LETTER_AMOUNT = int(getItemIfExists(
        By.CSS_SELECTOR, "#amountRemaining").text) + 1
    TOTAL_MISTAKE_AMOUNT = TOTAL_LETTER_AMOUNT * MISTAKE_PERCENT


def typeLetter(letter):
    DRIVER.find_element(By.CSS_SELECTOR, "#input_area").send_keys(letter)
    sleep(DELAY)


def typeText():
    MISTAKE_INTERVAL = ceil(TOTAL_LETTER_AMOUNT / TOTAL_MISTAKE_AMOUNT)
    i = 0
    while True:
        i += 1
        if (is_pressed(EXIT_KEY)):
            DRIVER.close()
            _exit(0)
        try:
            if i % MISTAKE_INTERVAL == 0:
                typeLetter("{")
            letter = DRIVER.find_element(
                By.CSS_SELECTOR, "#text_todo_1 > span").text
        except:
            return
        typeLetter(letter)


def goBackToHome():
    writeButton = getItemIfExists(By.CSS_SELECTOR, ".navButtonText")
    if writeButton:
        writeButton.click()


def main():
    acceptCookies()
    writeUsername()
    writePasswort()
    submitLogin()
    while True:
        openLesson()
        startLesson()
        getMistakes()
        typeText()
        goBackToHome()


main()
