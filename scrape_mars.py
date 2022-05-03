from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit redplanetscience.com
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)

    time.sleep(1)

    scraped_data = []

    # BROWSER ONE #
    # Scrape page into Soup
    news_html = browser.html
    news_soup = BeautifulSoup(news_html, 'html.parser')

    article = news_soup.find("div", class_='list_text')
    news_title = article.find("div", class_="content_title").text
    # print(f'Lastest News Title: {news_title}')
    news_p = article.find("div", class_='article_teaser_body').text
    # print(f'Article Preview: {news_p}')
    browser.quit()

    # Store data in a dictionary
    scraped_data.append({'Title': news_title, 'Preview': news_p})

    # Close the browser after scraping
    browser.quit()

    # BROWSER TWO #
    # img_url = 'https://spaceimages-mars.com/'
    # browser.visit(img_url)
    # img_html = browser.html
    # img_soup = BeautifulSoup(img_html, 'html.parser')

    # featured_image = img_soup.find('a', class_='showimg fancybox-thumbs')
    # featured_link = img_url + featured_image["href"]
    # scraped_data.append({'featured_image': featured_link})

    # browser.quit()

    # #BROWSER THREE #
    # mars_url = 'https://galaxyfacts-mars.com/'
    # tables = pd.read_html(mars_url)
    # df_1 = tables[0]
    # df_2 = tables[1]
    # mars_df = pd.concat([df_1, df_2])
    # mars_df.columns = ['Description', 'Mars', 'Earth']
    # mars_df = mars_df.iloc[1:]
    # mars_df.set_index('Description', inplace=True)
    # scraped_data.append({'mars_df': mars_df.head(20)})


    # # BROWSER FIVE #
    # mars_hemp_url = 'https://marshemispheres.com/'
    # browser.visit(mars_hemp_url)
    # mars_hemp_html = browser.html
    # marsh_soup = BeautifulSoup(mars_hemp_html, 'html.parser')

    # results= marsh_soup.find_all('div',class_='description')

    # # hemisphere_image_urls = []
    # for i in range(len(results)):
    #     hemisphere_img_url = mars_hemp_url + results[i].a['href']
    #     browser.visit(hemisphere_img_url)
    #     time.sleep(1)

    #     html = browser.html
    #     soup = BeautifulSoup(html, 'html.parser')    
    #     hemisphere_title = soup.find('h2', class_='title').text
    #     hemisphere_img_url = mars_hemp_url + soup.find_all('img')[4]['src']
            
    #     scraped_data.append({'title': hemisphere_title.replace(" Enhanced", ''), 'img_url': hemisphere_img_url})   
    # hemisphere_image_urls

    # Return results
    return scraped_data
