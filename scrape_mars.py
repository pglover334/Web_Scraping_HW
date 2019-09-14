from bs4 import BeautifulSoup
import os
import requests
from splinter import Browser
from selenium import webdriver
import pandas as pd
import time
from flask import Flask

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    
    browser = init_browser()
    mars_collection = {}
    url1 = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url1)
    html = browser.html
    response = requests.get(url1)
    soup1 = BeautifulSoup(response.text, 'html.parser')
    
    mars_collection["news_title"] = soup1.find('div', class_='content_title').text.strip()
    mars_collection["news_p"] = soup1.find('div', class_='rollover_description_inner').text.strip()
    
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    browser.click_link_by_id('full_image')
    time.sleep(2)
    html = browser.html
    img_soup = BeautifulSoup(html, "html.parser")
    img_url = img_soup.find('img', class_='fancybox-image')['src']
    mars_collection["featured_img_url"] = "https://www.jpl.nasa.gov" + img_url
    
    url3 = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url3)
    soup2 = BeautifulSoup(response.text, 'html.parser')
    mars_collection["mars_weather"] = soup2.find('div', class_='js-tweet-text-container')
    
    url4 = 'https://space-facts.com/mars/'
    tables = pd.read_html(url4)
    df = tables[0]
    df.columns = ['Mars-Earth_Comparison', 'Mars', 'Earth']
    html_table1 = df.to_html()
    html_table2 = html_table1.replace('\n', '')
    mars_collection["fact_table"] = html_table2
    
    hemisphere_img_urls = []
    
    url4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    response = requests.get(url4)
    soup3 = BeautifulSoup(response.text, 'html.parser')
    mars_collection['cerebrus_img'] = soup3.find('img', class_='wide-image')['src']
    mars_collection['cerebrus_title'] = soup3.find('h2', class_='title')

    
    url5 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    response = requests.get(url5)
    soup4 = BeautifulSoup(response.text, 'html.parser')
    mars_collection['schiaparelli_img'] = soup4.find('img', class_='wide-image')['src']
    mars_collection['schiaparelli_title'] = soup4.find('h2', class_='title')
    
    url6 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    response = requests.get(url6)    
    soup5 = BeautifulSoup(response.text, 'html.parser')
    mars_collection['syrtis_major_img'] = soup5.find('img', class_='wide-image')['src']
    mars_collection['syrtis_major_title'] = soup5.find('h2', class_='title')

    
    url7 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    response = requests.get(url7)
    soup6 = BeautifulSoup(response.text, 'html.parser')
    mars_collection['valles_marineris_img'] = soup6.find('img', class_='wide-image')['src']
    mars_collection['valles_marineris_title'] = soup6.find('h2', class_='title')


    return mars_collection    