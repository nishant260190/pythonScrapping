#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:15:40 2018

@author: nishantgoel
"""

'''import mechanize
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

url = 'http://www.facebook.com/login.php'
browser.open(url)
browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
browser.form['email'] = 'nishant260190'
browser.form['pass'] = 'dasdas'
response = browser.submit()
print(response.read())'''

import robobrowser

class Facebook(robobrowser.RoboBrowser):

    url = 'https://facebook.com'

    def __init__(self, email, password):
        self.email = email
        self.password = password
        super().__init__()
        self.login()

    def login(self):
        self.open(self.url)    
        login_form = self.get_form(id='login_form')
        login_form['email'] = self.email
        login_form['pass'] = self.password
        self.submit_form(login_form)
        
fb = Facebook('nishant260190@gmail.com', 'dsadsa')
fb.login()