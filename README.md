# Stock_Fundamental_Web-Scraper
### I created a simple web scraper which scrapes latest fundamental data for NIFTY-500 Stocks and store them into PSQL database 
## Prerequisites
### Python>3.6
### [screener.in ](https://www.screener.in/)account
### 2.You need set all the ratios in your account exactly as given below:
![screener](https://user-images.githubusercontent.com/32850887/83355606-23336900-a37e-11ea-81d5-af063408b518.png)
#  Quickstart
### Dependencies
* Selenium
* bs4
* pandas
* sqlalchemy
* urllib

### Install dependencies for python>3.6
* pip install -r requirements.txt
* Setup PSQL Database schema as given in backup.sql
* Change Your_screener_Username and Your_Screener_Password in store_data_in_db.py with your original Screener.in username and password
### Start Using with
* python store_data_in_db.py
