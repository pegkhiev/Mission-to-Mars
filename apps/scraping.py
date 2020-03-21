#!/usr/bin/env python
# coding: utf-8

from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

def scrape_all():
    #initiate headless driver for deployment
    executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
    browser = Browser('chrome', executable_path = 'chromedriver', headless = True)
    news_title, news_paragraph = mars_news(browser)
    img_url1, image_title1 = gethemi1()
    img_url2, image_title2 = gethemi2()
    img_url3, image_title3 = gethemi3()
    img_url4, image_title4 = gethemi4()

    data = {'news_title': news_title,
    'news_paragraph': news_paragraph,
    'featured_image': featured_image(browser),
    'facts': mars_facts(),
    'last_modified':dt.datetime.now(),
    'hemisphere_url1':img_url1,
    'hemisphere_title1':image_title1,
    'hemisphere_url2':img_url2,
    'hemisphere_title2':image_title2,
    'hemisphere_url3':img_url3,
    'hemisphere_title3':image_title3,
    'hemisphere_url4':img_url4,
    'hemisphere_title4':image_title4}

    browser.quit()
    return data
#create function for repeated use. 
def mars_news(browser):
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    #add try/except for error handling
    try: 
        slide_elem = news_soup.select_one('ul.item_list li.slide')

        news_title = slide_elem.find("div", class_='content_title').get_text()
  
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None
    return news_title, news_p


# news_date = slide_elem.find('div',class_='list_date').get_text()
# news_date

def featured_image(browser):
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    browser.is_element_present_by_text('more info', wait_time = 1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()

    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')

    try:
        image_url_rel = img_soup.select_one('figure.lede a img').get('src')
    except AttributeError:
        return None


    img_url = f"https://jpl.nasa.gov{image_url_rel}"
    return img_url

def mars_facts(classes=["table-bordered", "table-striped"]):
    # Add try/except for error handling
    # try:
        # Use 'read_html' to scrape the facts table into a dataframe
    df = pd.read_html('http://space-facts.com/mars/')[0]

    # except BaseException:
    #     return None
    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()


def gethemi1():
    executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
    browser = Browser('chrome', executable_path = 'chromedriver', headless = True)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    hemispheres = browser.find_by_css('h3')[0]
    hemispheres.click()
    hemi_html = browser.html
    hemi = BeautifulSoup(hemi_html, 'html.parser')
    hemi_url_rel = hemi.find('img', class_= 'wide-image').get('src')
    hemi_title= hemi.find('h2',class_='title').text
    hemi_url = f"https://astrogeology.usgs.gov{hemi_url_rel}"
    return hemi_url, hemi_title
def gethemi2():
    executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
    browser = Browser('chrome', executable_path = 'chromedriver', headless = True)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    hemispheres = browser.find_by_css('h3')[1]
    hemispheres.click()
    hemi_html = browser.html
    hemi = BeautifulSoup(hemi_html, 'html.parser')
    hemi_url_rel = hemi.find('img', class_= 'wide-image').get('src')
    hemi_title= hemi.find('h2',class_='title').text
    hemi_url = f"https://astrogeology.usgs.gov{hemi_url_rel}"
    return hemi_url, hemi_title
def gethemi3():
    executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
    browser = Browser('chrome', executable_path = 'chromedriver', headless = True)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    hemispheres = browser.find_by_css('h3')[2]
    hemispheres.click()
    hemi_html = browser.html
    hemi = BeautifulSoup(hemi_html, 'html.parser')
    hemi_url_rel = hemi.find('img', class_= 'wide-image').get('src')
    hemi_title= hemi.find('h2',class_='title').text
    hemi_url = f"https://astrogeology.usgs.gov{hemi_url_rel}"
    return hemi_url, hemi_title
def gethemi4():
    executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
    browser = Browser('chrome', executable_path = 'chromedriver', headless = True)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    hemispheres = browser.find_by_css('h3')[3]
    hemispheres.click()
    hemi_html = browser.html
    hemi = BeautifulSoup(hemi_html, 'html.parser')
    hemi_url_rel = hemi.find('img', class_= 'wide-image').get('src')
    hemi_title= hemi.find('h2',class_='title').text
    hemi_url = f"https://astrogeology.usgs.gov{hemi_url_rel}"
    return hemi_url, hemi_title


if __name__ == '__main__':
    print(scrape_all())







