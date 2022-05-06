from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit https://redplanetscience.com/
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    article = soup.find("div", class_='list_text')
    news_title = article.find("div", class_="content_title").text

    news_p = article.find("div", class_='article_teaser_body').text

    # Exit Browser
    browser.quit()


    # BROWSER TWO #
    # Scrape page into Soup
    browser = Browser('chrome', **executable_path, headless=False)
    img_url = 'https://spaceimages-mars.com/'
    browser.visit(img_url)

    img_html = browser.html
    img_soup = bs(img_html, 'html.parser')
    time.sleep(1)

    featured_image = img_soup.find('a', class_='showimg fancybox-thumbs')
    featured_link = img_url + featured_image["href"]

    browser.quit()

    #BROWSER THREE #
    mars_url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(mars_url)
    df_1 = tables[0]
    df_2 = tables[1]
    # mars_df = pd.concat([df_1, df_2])
    mars_df = tables[0]
    mars_df.columns = ['Description', 'Mars', 'Earth']
    mars_df = mars_df.iloc[1:]
    mars_df= mars_df.reset_index(drop=True)
    
    # mars_dict = mars_df.to_dict('split')
    # mars_dict = mars_df.to_dict('list')
    import numpy as np
    len(mars_df)
    mars_table = []
    for i in np.arange(len(mars_df)):
        mars_desc = mars_df['Description'][i]
        mars_val = mars_df['Mars'][i]
        earth_val = mars_df['Earth'][i]
        mars_table.append({'Description': mars_desc, 'Mars': mars_val, 'Earth': earth_val})
    mars_table



    # # BROWSER FOUR #
    browser = Browser('chrome', **executable_path, headless=False)    
    mars_hemp_url = 'https://marshemispheres.com/'
    browser.visit(mars_hemp_url)
    mars_hemp_html = browser.html
    marsh_soup = bs(mars_hemp_html, 'html.parser')

    results= marsh_soup.find_all('div',class_='description')

    hemisphere_list = []

    for i in range(len(results)):
        hemisphere_img_url = mars_hemp_url + results[i].a['href']
        browser.visit(hemisphere_img_url)
        time.sleep(1)

        html = browser.html
        soup = bs(html, 'html.parser')    
        hemisphere_title = soup.find('h2', class_='title').text
        hemisphere_img_url = mars_hemp_url + soup.find_all('img')[4]['src']

        # Store data in a dictionary   
        hemisphere_list.append({'title': hemisphere_title.replace(" Enhanced", ''), 'url': hemisphere_img_url})


    browser.quit()

    # Store data in a dictionary
    missions_to_mars = {
        "title": news_title,
        "preview": news_p,
        "img_url": featured_link,
        "hemisphere": hemisphere_list,
        "mars_table": mars_table
    }

    # Return results
    return missions_to_mars
