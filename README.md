# Books_Scraper

 A basic web-scraper package on scraping pdf drive website for information about books uploaded.

        Args:
        num_items (int): The number of samples (observations) of data to be scraped.
        The minimum samples for scraping is 20, as that is minimum per page

        keyword (str): The name of the category of which the data is to be scraped.
        Currently only accepts single word as keyword.

        Returns:
        pd.DataFrame: A DataFrame object that has title, number of pages, year published,
        number of downloads and if it is recently uploaded on pdfdrive(is_new).
  
# Installation
Run the following to install the book scraper: pip install git+https://github.com/rukayah/Books_scraper

# Usage
from bookscraper import Webscraping

## Use the extract method to extract the number of listings you want to extract, by entering the keyword

instance = Webscraping() creates an instance of the class
dataframe = instance.extract(50, "children") calls the extract method and output a dataframe
 
 
