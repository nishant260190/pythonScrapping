#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:24:56 2018

@author: nishantgoel
"""

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("/Applications/chromedriver")
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)
 
username_box = driver.find_element_by_id('email')
username_box.send_keys('nishant260190@gmail.com')
print ("Email Id entered")
sleep(1)
 
password_box = driver.find_element_by_id('pass')
password_box.send_keys('inspiron5010')
print ("Password entered")
 
login_box = driver.find_element_by_id('loginbutton')
login_box.click()
 
print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")
