from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='bookscraper',
    version='0.0.1',
    description='scrape books information from pdfdrive',
    py_modules=["bookscraper"],
    package_dir={'':'src'},

       classifiers=[
        "programming Language :: python :: 3",
        "programming Language :: python :: 3.6",
        "programming Language :: python :: 3.7",
        "License :: OSI Approved :: GNU General Pubic License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    
    extras_require = {"dev":["pytest>=3.7",],},

)
