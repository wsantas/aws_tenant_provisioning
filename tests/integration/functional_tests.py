from selenium import webdriver
import os

browser = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))
browser.get('http://localhost:8000')

assert 'Django' in browser.title