import pandas as pd
import requests 
from bs4 import BeautifulSoup as bs
import numpy as np
import math

class ScraperError(Exception):
    "Error handling class for all thing related to webscraping"
    pass

class Webscraping:

    def __init__(self) -> None:
        self.dataframe = None
        self.keyword = None

    def extract(self,num_items:int, keyword:str):
        """
        A basic web-scraper on scraping Ebay data based on specific category ie dress, bicycle.

        Parameters:
        num_items (int): The number of samples (observations) of data to be scraped.
        The minimum samples for scraping is 50, as that is minimum per page

        keyword (str): The name of the category of which the data is to be scraped.
        Currently only accepts single word as keyword.

        Returns:
        pd.DataFrame: A DataFrame object that has title,price of the category,
        item URL,image URL and category for the keyword entered.
        """
        self.keyword = keyword

        titles = []
        page_numbers =[]
        year = []
        downloads = []
        is_new = []


        num_pages = math.ceil(num_items/20)
        pages = np.arange(1, num_pages + 1, 1)
        for page in pages:
            url = f"https://www.pdfdrive.com/search?q={self.keyword}&pagecount=&pubyear=&searchin=&page="+str(page)
            source = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"}).text
            soup = bs(source, "lxml")
            #print(page)


     
            for book in soup.find_all('div', class_="file-right"):
                title = book.h2.text
                titles.append(title)
                page_no = book.find('span',class_='fi-pagecount').text
                page_numbers.append(page_no)
                yr = book.find('span', class_='fi-year').text
                year.append(yr)
                download = book.find('span', class_='fi-hit').text
                downloads.append(download)
                new = book.find('span', class_='new').text if book.find("span", class_='new') else " "
                is_new.append(new)
        self.dataframe = pd.DataFrame(
           {
            "title": titles, "page_number": page_numbers, "published_year": year, "downloads": downloads,"is_new":is_new,
           }
        )
        return self.dataframe

scrape = Webscraping()
#output = scrape.extract(50,"children")
#output.to_csv("romance.csv")


  