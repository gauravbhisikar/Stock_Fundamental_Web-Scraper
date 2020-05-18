
import selenium
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import request
from bs4 import BeautifulSoup
import time
import json
import pandas as pd 
import psycopg2
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:1234@localhost:5432/fundamentals')
#connection  = psycopg2.connect(database = "fundamentals",user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
print("Database Opened Successfuly")
Ticker = "JUSTDIAL"
ID  = 1
#cur = connection.cursor()
print("curr success")

path = "C:\\Users\\Asus\\Desktop\\chromedriver.exe"
data = []
meta_data = []
compitior = []
Growth = []
new_growth = []
options = Options()
options.add_argument("--headless")
options.add_argument("--incognito")
driver = webdriver.Chrome(options = options)
#driver = webdriver.Chrome()

url = "https://www.screener.in/login/"
driver.get(url)
print(driver.title)
username = driver.find_element_by_id("id_username")
username.send_keys("joncorner1000@gmail.com")
password = driver.find_element_by_id("id_password")
password.send_keys("7p.ReT8-WKh.ULm")
password.send_keys(Keys.RETURN)
driver.get(f'https://www.screener.in/company/{Ticker}/consolidated/')
time.sleep(1)
soup = BeautifulSoup(driver.page_source,'html.parser')
meta_data =  soup.find_all('b')
Pros = soup.find_all('div', class_ = 'six columns callout success' )
Cons = soup.find_all('div', class_ = 'six columns callout warning')
Growth = soup.find_all('td')
#for i in Growth:
#	print(i.text)


try:
	Inventory_turnover_ratio = float((meta_data[29].text).replace(',',''))
except Exception as e:
	Inventory_turnover_ratio = 0	

	
consolidated ={
		'Ticker'					: Ticker,
		'Market_Cap'				: float((meta_data[0].text).replace(',','')),
		'Current_Price'				: float((meta_data[1].text).replace(',','')),
		'52week_High'				: float(meta_data[2].text),
		'52week_Low' 				: float(meta_data[3].text),
		"Book_Value"				: float(meta_data[4].text),
		"Stock_P/E"  				: float(meta_data[5].text),
		"Dividend_Yield"			: float(meta_data[6].text),
		"ROCE"						: float(meta_data[7].text),
		"ROE"						: float(meta_data[8].text),
		"Sales_Growth(3Yrs)"		: float(meta_data[9].text),
		"Face_Value"				: float(meta_data[13].text),
		"Return_on_assets"			: float(meta_data[14].text),
		"Asset_Turnover_Ratio"  	: float(meta_data[15].text),
		"PB_value"					: float(meta_data[16].text),
		"Debt"						: float((meta_data[17].text).replace(',','')),
		"Promoter_holding" 			: float(meta_data[18].text),
		"Pledged_percentage" 		: float(meta_data[19].text),
		"Profit_growth"				: float(meta_data[20].text),
		"Profit_after_tax"			: float((meta_data[21].text).replace(',','')),
		"Price_to_Sales"			: float(meta_data[22].text),
		"Enterprise_Value" 			: float((meta_data[23].text).replace(',','')),
		"PEG_Ratio" 				: float(meta_data[24].text),
		"Current_ratio"				: float(meta_data[25].text),
		"Debt_to_equity"			: float(meta_data[26].text),
		"Interest_Coverage_Ratio"	: float(meta_data[27].text),
		"Inventory_turnover_ratio"	: Inventory_turnover_ratio,
		"Dividend_Payout_Ratio" 	: float(meta_data[29].text),
		"Quick_ratio"				: float(meta_data[30].text),
		"Pros"						: (Pros[0].text).replace("\n"," ").replace(":","").replace("Pros","").replace("  "," "),
		"Cons" 						: (Cons[0].text).replace("\n"," ").replace(":","").replace("Cons","").replace("  "," "),



	}

driver.get(f'https://www.screener.in/company/{Ticker}/#quarters')
time.sleep(1)
soup = BeautifulSoup(driver.page_source,'html.parser')
meta_data =  soup.find_all('b')
try:
	Standalone_Inventory_turnover_ratio = float((meta_data[29].text).replace(',',''))
except Exception as e:
	Standalone_Inventory_turnover_ratio = 0	

Standalone  = {	

		"Standalone_Book_Value"					: float(meta_data[4].text),
		"Standalone_Stock_P/E"  				: float(meta_data[5].text),
		"Standalone_ROCE"						: float(meta_data[7].text),
		"Standalone_ROE"						: float(meta_data[8].text),
		"Standalone_Sales_Growth(3Yrs)"			: float(meta_data[9].text),
		"Standalone_Return_on_assets"			: float(meta_data[14].text),
		"Standalone_Asset_Turnover_Ratio"  		: float(meta_data[15].text),
		"Standalone_PB_value"					: float(meta_data[16].text),
		"Standalone_Debt"						: float((meta_data[17].text).replace(',','')),
		"Standalone_Profit_growth"				: float(meta_data[20].text),
		"Standalone_Profit_after_tax"			: float((meta_data[21].text).replace(',','')),
		"Standalone_Price_to_Sales"				: float(meta_data[22].text),
		"Standalone_Enterprise_Value" 			: float((meta_data[23].text).replace(',','')),
		"Standalone_PEG_Ratio" 					: float(meta_data[24].text),
		"Standalone_Current_ratio"				: float(meta_data[25].text),
		"Standalone_Debt_to_equity"				: float(meta_data[26].text),
		"Standalone_Interest_Coverage_Ratio"	: float(meta_data[27].text),
		"Standalone_Inventory_turnover_ratio"	: Standalone_Inventory_turnover_ratio,
		"Standalone_Dividend_Payout_Ratio" 		: float(meta_data[29].text),
		"Standalone_Quick_ratio"				: float(meta_data[30].text),


}

	

def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 

data = Merge(consolidated,Standalone)
print(json.dumps(data, indent = 1))

df  = pd.DataFrame(data, index=[0])
df.rename(columns = {'Ticker':'TICKER','Market_Cap':'c_mc','Current_Price':'c_cp','52week_High':'c_52h','52week_Low':'c_52l',
					'Book_Value':'c_bv','Stock_P/E':'c_pe','Dividend_Yield':'c_dy','ROCE':'c_roce','ROE':'c_roe',
					'Sales_Growth(3Yrs)':'c_sg3','Face_Value':'c_fv','Return_on_assets':'c_roa','Asset_Turnover_Ratio':'c_atr', 
					'PB_value':'c_pbv', 'Debt':'c_debt','Promoter_holding':'c_ph','Pledged_percentage':'c_pleg', 'Profit_growth':'c_pg',
					'Profit_after_tax':'c_pat','Price_to_Sales':'c_pts','Enterprise_Value':'c_enpv', 'PEG_Ratio':'c_peg_r',
					'Current_ratio':'c_cr','Debt_to_equity':'c_dte','Interest_Coverage_Ratio':'c_icr','Inventory_turnover_ratio':'c_itr',
					'Dividend_Payout_Ratio':'c_dpr','Quick_ratio':'c_qr','Pros':'pros','Cons':'cons',
					'Standalone_Book_Value':'s_bv','Standalone_Stock_P/E':'s_pe','Standalone_ROCE':'s_roce','Standalone_ROE':'s_roe',
					'Standalone_Sales_Growth(3Yrs)':'s_sg3','Standalone_Return_on_assets':'s_roa','Standalone_Asset_Turnover_Ratio':'s_atr',
					'Standalone_PB_value':'s_pbv','Standalone_Debt':'s_debt','Standalone_Profit_growth':'s_pg','Standalone_Profit_after_tax':'s_pat',
					'Standalone_Price_to_Sales':'s_pts','Standalone_Enterprise_Value':'s_enpv','Standalone_PEG_Ratio':'s_peg_r','Standalone_Current_ratio':'s_cr',
					'Standalone_Debt_to_equity':'s_dte','Standalone_Interest_Coverage_Ratio':'s_icr','Standalone_Inventory_turnover_ratio':'s_itr',
					'Standalone_Dividend_Payout_Ratio':'s_dpr','Standalone_Quick_ratio':'s_qr'
					},inplace = True)

print(df.head())
df.to_sql(
	name = 'fundamental_data',
	con = engine,
	if_exists = 'append' )

print("Successfuly commited")




