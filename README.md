# project-amazon-webscraping

Python Scrapy spiders that scrape product data and reviews from [Amazon.com](https://www.amazon.com/). 

- In this project amazon product are scraped using amazon spider

# Highlights of project
- amazon products are scarped using scrapy
- amazon website stops user from webscraping using its antibots. In this project we use scrapeops api to handle proxies which allow us to scrape the website.
- an pipeline is established using which we can clean the data and then load in to mysql database or amazon s3.

# proesss
- install scrapy
  ```
  pip install scrapy
  ```
- enter in the terminal to start the project
  ```
  scrapy startproject <project_name>
  ```
- crawl the website
  ```
  scrapy crawl <spider_name> -O path
  scrapy crawl <spider_name> -o path
  ```
  - 'O' will rewrite evry time spider is run
  - 'o' will append the data to existing file every time spider when run.
