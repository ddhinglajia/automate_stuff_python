#! /usr/bin/python3 
# command line emailer
# use seleneium, login email, send email

import re, sys, os, time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


user = "email_enter@gmail.com"
password = "enter_password"

def sendEmail():
    emailAdr = sys.argv[1]
    mail = " ".join(sys.argv[2:])

    #Logging into gamil
    url = "https://accounts.google.com/ServiceLogin"
    browser = webdriver.Firefox()
    browser.get(url)

    emailElem = browser.find_element_by_id("Email")
    emailElem.send_keys(user)
    browser.find_element_by_id("next").click()

    time.sleep(1)
    passwordElem = browser.find_element_by_id("password")
    passwordElem.send_keys(password)
    browser.find_element_by_id("signIn").click()

    #Send an email of the string to the provided address
    browser.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    time.sleep(2)
    browser.find_element_by_xpath("//textarea[@aria-label='To']").send_keys(emailAdr)
    time.sleep(2)
    browser.find_element_by_xpath("//input[@aria-label='Subject']").send_keys("Hello World!")
    time.sleep(10)
    browser.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys(mail)
    time.sleep(5)
    browser.find_element_by_xpath("//div[contains(mail(), 'Send')]").click()

sendEmail()