# Books_Scraper

 A basic web-scraper on scraping pdf drive website for information about books uploaded.

        Args:
        num_items (int): The number of samples (observations) of data to be scraped.
        The minimum samples for scraping is 20, as that is minimum per page

        keyword (str): The name of the category of which the data is to be scraped.
        Currently only accepts single word as keyword.

        Returns:
        pd.DataFrame: A DataFrame object that has title, number of pages, year published,
        number of downloads and if it is recently uploaded on pdfdrive.
       
