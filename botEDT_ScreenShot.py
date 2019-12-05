# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:28:04 2019

@author: marc-
"""
import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


username = '20130179'
password = '9912Battesti'
pageEDT = "https://reverse-proxy-edt.univ-corse.fr/g781295.html"

js = "ShowEventsList('Grid');"
browser = webdriver.Chrome('chromedriver')
action = ActionChains(browser)

""" On va sur la page et on se connecte"""
browser.get((pageEDT))
box_username = browser.find_element_by_name('username')
box_username.send_keys(username)
box_pwd = browser.find_element_by_name('password')
box_pwd.send_keys(password)
bt_connect = browser.find_element_by_name('submit')
bt_connect.click()

"""On affiche la page en fullscreen"""
browser.fullscreen_window()
browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))


browser.execute_script(js)

browser.execute_script("window.scrollTo(0, 500);") 
browser.save_screenshot('/screen/screenie.jpg')
browser.quit()