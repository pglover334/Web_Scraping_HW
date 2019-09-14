{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import os\n",
    "import requests\n",
    "from splinter import Browser\n",
    "from selenium import webdriver\n",
    "import pandas as pd\n",
    "import time\n",
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "def init_browser():\n",
    "    executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "    return Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "\n",
    "def scrape():\n",
    "    \n",
    "    browser = init_browser()\n",
    "    mars_collection = {}\n",
    "    url1 = \"https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest\"\n",
    "    browser.visit(url1)\n",
    "    html = browser.html\n",
    "    response = requests.get(url1)\n",
    "    soup1 = BeautifulSoup(response.text, 'html.parser')\n",
    "    \n",
    "    mars_collection[\"news_title\"] = soup1.find('div', class_='content_title').text.strip()\n",
    "    mars_collection[\"news_p\"] = soup1.find('div', class_='rollover_description_inner').text.strip()\n",
    "    \n",
    "    url2 = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "    browser.visit(url2)\n",
    "    browser.click_link_by_id('full_image')\n",
    "    time.sleep(2)\n",
    "    html = browser.html\n",
    "    img_soup = BeautifulSoup(html, \"html.parser\")\n",
    "    img_url = img_soup.find('img', class_='fancybox-image')['src']\n",
    "    mars_collection[\"featured_img_url\"] = \"https://www.jpl.nasa.gov\" + img_url\n",
    "    \n",
    "    url3 = 'https://twitter.com/marswxreport?lang=en'\n",
    "    response = requests.get(url3)\n",
    "    soup2 = BeautifulSoup(response.text, 'html.parser')\n",
    "    mars_collection[\"mars_weather\"] = soup2.find('div', class_='js-tweet-text-container')\n",
    "    \n",
    "    url4 = 'https://space-facts.com/mars/'\n",
    "    tables = pd.read_html(url4)\n",
    "    df = tables[0]\n",
    "    df.columns = ['Mars-Earth_Comparison', 'Mars', 'Earth']\n",
    "    html_table1 = df.to_html()\n",
    "    html_table2 = html_table1.replace('\\n', '')\n",
    "    mars_collection[\"fact_table\"] = html_table2\n",
    "    \n",
    "    hemisphere_img_urls = []\n",
    "    \n",
    "    url4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'\n",
    "    response = requests.get(url4)\n",
    "    soup3 = BeautifulSoup(response.text, 'html.parser')\n",
    "    mars_collection['cerebrus_img'] = soup3.find('img', class_='wide-image')['src']\n",
    "    mars_collection['cerebrus_title'] = soup3.find('h2', class_='title')\n",
    "\n",
    "    \n",
    "    url5 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'\n",
    "    response = requests.get(url5)\n",
    "    soup4 = BeautifulSoup(response.text, 'html.parser')\n",
    "    mars_collection['schiaparelli_img'] = soup4.find('img', class_='wide-image')['src']\n",
    "    mars_collection['schiaparelli_title'] = soup4.find('h2', class_='title')\n",
    "    \n",
    "    url6 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'\n",
    "    response = requests.get(url6)    \n",
    "    soup5 = BeautifulSoup(response.text, 'html.parser')\n",
    "    mars_collection['syrtis_major_img'] = soup5.find('img', class_='wide-image')['src']\n",
    "    mars_collection['syrtis_major_title'] = soup5.find('h2', class_='title')\n",
    "\n",
    "    \n",
    "    url7 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'\n",
    "    response = requests.get(url7)\n",
    "    soup6 = BeautifulSoup(response.text, 'html.parser')\n",
    "    mars_collection['valles_marineris_img'] = soup6.find('img', class_='wide-image')['src']\n",
    "    mars_collection['valles_marineris_title'] = soup6.find('h2', class_='title')\n",
    "\n",
    "\n",
    "    return mars_collection    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'news_title': 'NASA Invites Students to Name Mars 2020 Rover',\n",
       " 'news_p': \"Through Nov. 1, K-12 students in the U.S. are encouraged to enter an essay contest to name NASA's next Mars rover.\",\n",
       " 'featured_img_url': 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA16021_ip.jpg',\n",
       " 'mars_weather': <div class=\"js-tweet-text-container\">\n",
       " <p class=\"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\" data-aria-label-part=\"0\" lang=\"und\">Weeeeee!  <a class=\"twitter-timeline-link\" data-expanded-url=\"https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA23461\" dir=\"ltr\" href=\"https://t.co/terPoTqKM6\" rel=\"nofollow noopener\" target=\"_blank\" title=\"https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA23461\"><span class=\"tco-ellipsis\"></span><span class=\"invisible\">https://www.</span><span class=\"js-display-url\">jpl.nasa.gov/spaceimages/de</span><span class=\"invisible\">tails.php?id=PIA23461</span><span class=\"tco-ellipsis\"><span class=\"invisible\"> </span>…</span></a><a class=\"twitter-timeline-link u-hidden\" data-pre-embedded=\"true\" dir=\"ltr\" href=\"https://t.co/iuEqJjsQ4G\">pic.twitter.com/iuEqJjsQ4G</a></p>\n",
       " </div>,\n",
       " 'fact_table': '<table border=\"1\" class=\"dataframe\">  <thead>    <tr style=\"text-align: right;\">      <th></th>      <th>Mars-Earth_Comparison</th>      <th>Mars</th>      <th>Earth</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Diameter:</td>      <td>6,779 km</td>      <td>12,742 km</td>    </tr>    <tr>      <th>1</th>      <td>Mass:</td>      <td>6.39 × 10^23 kg</td>      <td>5.97 × 10^24 kg</td>    </tr>    <tr>      <th>2</th>      <td>Moons:</td>      <td>2</td>      <td>1</td>    </tr>    <tr>      <th>3</th>      <td>Distance from Sun:</td>      <td>227,943,824 km</td>      <td>149,598,262 km</td>    </tr>    <tr>      <th>4</th>      <td>Length of Year:</td>      <td>687 Earth days</td>      <td>365.24 days</td>    </tr>    <tr>      <th>5</th>      <td>Temperature:</td>      <td>-153 to 20 °C</td>      <td>-88 to 58°C</td>    </tr>  </tbody></table>',\n",
       " 'cerebrus_img': '/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg',\n",
       " 'cerebrus_title': <h2 class=\"title\">Cerberus Hemisphere Enhanced</h2>,\n",
       " 'schiaparelli_img': '/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg',\n",
       " 'schiaparelli_title': <h2 class=\"title\">Schiaparelli Hemisphere Enhanced</h2>,\n",
       " 'syrtis_major_img': '/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg',\n",
       " 'syrtis_major_title': <h2 class=\"title\">Syrtis Major Hemisphere Enhanced</h2>,\n",
       " 'valles_marineris_img': '/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg',\n",
       " 'valles_marineris_title': <h2 class=\"title\">Valles Marineris Hemisphere Enhanced</h2>}"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scrape()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
