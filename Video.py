#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import bs4 as bs
from bs4 import BeautifulSoup
import numpy as np
import urllib.request
import random



def sleepTime(): 
	t = random.randint(1,3)
	time.sleep(t)
	
def execute_times(times): 
    for i in range(times + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def video_scrap(arr):
	video =[]

	for i in arr:
		driver.get('http:'+i)
		execute_times(2) 

		product_html = driver.page_source

		soup = bs.BeautifulSoup(product_html,'lxml')


		products_video = soup.find("video", {"class": "lib-video"})

		if products_video is None:
			video.append('')
		else:
			video.append(products_video.attrs['src'])


	return video

	
# ---- URL starts ----
link = 'https://midea.world.tmall.com/p/rd385623.htm?spm=a312a.7700824.w15914064-14899974279.16.6eaa4e96Wl6NAI&scene=taobao_shop'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

driver.get(link)

execute_times(2) 

html = driver.page_source
soup = bs.BeautifulSoup(html,'lxml')
# ---- URL ends ----


contents = soup.findAll("a", {"class": "item-name"})


products = [] # 存 item-name
links = []
product_url = []
ids = []


for i in contents:
	if i.text not in products:
		products.append(i.text)
		links.append(i)


for i in links:
	product_url.append(i.attrs['href'])


for i in soup.findAll("dl", {"class": "item"}):
	if i.attrs['data-id'] not in ids:
		ids.append(i.attrs['data-id'])



# video_scrap(product_url)

print(ids)
print(len(ids))
# generate_video(ids,video_scrap(product_url))


