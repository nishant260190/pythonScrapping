from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r'/Users/nishantgoel/desktop/geckodriver.exe')
driver.get("https://www.facebook.com/");
login_email = driver.find_element_by_id('email').send_keys('nishant260190@gmail.com');
login_pass = driver.find_element_by_id('pass').send_keys('hjj');
login = driver.find_element_by_id('u_0_2').click()
