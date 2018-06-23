from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import cv2.cv as cv
import tesseract
#import os
#print(os.path.isfile('/Users/nishantgoel/desktop/geckodriver.exe'))
'''
driver = webdriver.Firefox(executable_path='/Users/nishantgoel/desktop/geckodriver.exe')
#driver = webdriver.Firefox()
driver.get("http://mylpg.in/index.aspx")
value = driver.find_element_by_id('cons_id').send_keys('1')
value1 = driver.find_element_by_id('cons_id1').send_keys('0000')
value2 = driver.find_element_by_id('cons_id2').send_keys('0000')
value3 = driver.find_element_by_id('cons_id3').send_keys('3866')
value4 = driver.find_element_by_id('cons_id4').send_keys('3900')

print(driver.find_elements_by_class_name("btn"));
submitButton = driver.find_elements_by_class_name("btn")
submitButton[0].click()

print(submitButton);

'''

def getCaptcha():
    grayScale = cv.LoadImage('https://my.ebharatgas.com/bharatgas/MyCaptcha.png', cv.CV_LOAD_IMAGE_GRAYSCALE)
    cv.Threshold(gray, gray, 231, 255, cv.CV_THRESH_BINARY)
    api = tesseract.TessBaseAPI()
    api.Init(".","eng",tesseract.OEM_DEFAULT)
    api.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijklmnopqrstuvwxyz")
    api.SetPageSegMode(tesseract.PSM_SINGLE_WORD)
    tesseract.SetCvImage(gray,api)
    print(api.GetUTF8Text())

getCaptcha()
