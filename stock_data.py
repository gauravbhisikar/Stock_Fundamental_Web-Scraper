import selenium
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import request
from bs4 import BeautifulSoup
import pandas as pd 
import sqlalchemy
from urllib.request import urlopen 
from datetime import date
import time


 

def run_safely_coma(index):
	try:
		output = float((meta_data[index].text).replace(',',''))
	except Exception as e:
		output = 0		
	
	return output

def run_safely(index):
	try:
		output = float((meta_data[index].text))
	except Exception as e:
		output = 0
		

	return output

def run_safely_pros(index):
	try:
		output = (Pros[index].text).replace("\n"," ").replace(":","").replace("Pros","").replace("  "," ")
	except Exception as e:
		output = ""
		

	return output

def run_safely_cons(index):
	try:
		output = (Cons[index].text).replace("\n"," ").replace(":","").replace("Cons","").replace("  "," ")
	except Exception as e:
		output = ""	
		
	return output

def run_safely_standaloan(index):
	try:
		output = float((meta_data[index].text))
	except Exception as e:
		output = 0	
		
	return output
  

class Stock_Data():

	def __init__(self,login_username,login_password,username,password,host,database_name,port = '5432'):
		self.login_username = login_username
		self.login_password = login_password
		self.username = username
		self.password = password
		self.database_name = database_name
		self.port = port
		self.index = -1
		self.dataframe = pd.DataFrame()
		try:
			self.engine = sqlalchemy.create_engine(f'postgresql://{self.username}:{self.password}@{host}:{self.port}/{self.database_name}')
			print("Engine Created")
		except Exception as e:
			print("Engine was not Created")
			print(e)
		try:
			test_url = "https://www.screener.in/login/"
			urlopen(test_url)
			print("Internet Connected")
			self.Internet_status = 'Working'
		except Exception as e:
			print("Internet Disconnected")
			self.Internet_status = 'Not Working'		


		


	def get_fundamental_data(self,Ticker):
		if self.Internet_status == 'Working':
					self.Ticker = Ticker
					options = Options()
					options.add_argument("--headless")
					options.add_argument("--incognito")
					driver = webdriver.Chrome(options = options)
					#driver = webdriver.Chrome()	
					driver.get("https://www.screener.in/login/")
					#print(driver.title)
					username = driver.find_element_by_id("id_username")
					username.send_keys(self.login_username)
					password = driver.find_element_by_id("id_password")
					password.send_keys(self.login_password)
					password.send_keys(Keys.RETURN)
					driver.get(f'https://www.screener.in/company/{Ticker}/consolidated/')
					time.sleep(1)
					soup = BeautifulSoup(driver.page_source,'html.parser')
					global meta_data
					meta_data =  soup.find_all('b')
					global Pros
					Pros = soup.find_all('div', class_ = 'six columns callout success' )
					global Cons
					Cons = soup.find_all('div', class_ = 'six columns callout warning')
					
					




					try:
			
						consolidated ={
					'Ticker'					: Ticker,
					'Market_Cap'				: run_safely_coma(0),
					'Current_Price'				: run_safely_coma(1),
					'52week_High'				: run_safely(2),
					'52week_Low' 				: run_safely(3),
					"Book_Value"				: run_safely(4),
					"Stock_P/E"  				: run_safely(5),
					"Dividend_Yield"			: run_safely(6),
					"ROCE"						: run_safely(7),
					"ROE"						: run_safely(8),
					"Sales_Growth(3Yrs)"		: run_safely(9),
					"Face_Value"				: run_safely(13),
					"Return_on_assets"			: run_safely(14),
					"Asset_Turnover_Ratio"  	: run_safely(15),
					"PB_value"					: run_safely(16),
					"Debt"						: run_safely_coma(17),
					"Promoter_holding" 			: run_safely(18),
					"Pledged_percentage" 		: run_safely(19),
					"Profit_growth"				: run_safely(20),
					"Profit_after_tax"			: run_safely_coma(21),
					"Price_to_Sales"			: run_safely(22),
					"Enterprise_Value" 			: run_safely_coma(23),
					"PEG_Ratio" 				: run_safely(24),
					"Current_ratio"				: run_safely(25),
					"Debt_to_equity"			: run_safely(26),
					"Interest_Coverage_Ratio"	: run_safely(27),
					"Inventory_turnover_ratio"	: run_safely_coma(29),
					"Dividend_Payout_Ratio" 	: run_safely(29),
					"Quick_ratio"				: run_safely(30),
					"Pros"						: run_safely_pros(0),
					"Cons" 						: run_safely_cons(0),
					}

						driver.get(f'https://www.screener.in/company/{Ticker}/#quarters')
						time.sleep(1)
						soup = BeautifulSoup(driver.page_source,'html.parser')
						meta_data =  soup.find_all('b')
						Standalone  = {	

					"Standalone_Book_Value"					: run_safely(4),
					"Standalone_Stock_P/E"  				: run_safely(5),
					"Standalone_ROCE"						: run_safely(7),
					"Standalone_ROE"						: run_safely(8),
					"Standalone_Sales_Growth(3Yrs)"			: run_safely(9),
					"Standalone_Return_on_assets"			: run_safely(14),
					"Standalone_Asset_Turnover_Ratio"  		: run_safely(15),
					"Standalone_PB_value"					: run_safely(16),
					"Standalone_Debt"						: run_safely_coma(17),
					"Standalone_Profit_growth"				: run_safely(20),
					"Standalone_Profit_after_tax"			: run_safely_coma(21),
					"Standalone_Price_to_Sales"				: run_safely(22),
					"Standalone_Enterprise_Value" 			: run_safely_coma(23),
					"Standalone_PEG_Ratio" 					: run_safely(24),
					"Standalone_Current_ratio"				: run_safely(25),
					"Standalone_Debt_to_equity"				: run_safely(26),
					"Standalone_Interest_Coverage_Ratio"	: run_safely(27),
					"Standalone_Inventory_turnover_ratio"	: run_safely_coma(29),
					"Standalone_Dividend_Payout_Ratio" 		: run_safely(29),
					"Standalone_Quick_ratio"				: run_safely(30),	
					"Date"									: date.today(),
					}

						Data = {**consolidated, **Standalone}
						driver.close()
						self.Data = Data
						self.Status = 'Working'
						print(f"Data of Ticker {self.Ticker} was extracted")
						return Data

					except Exception as e:
						print(f"Data of Ticker {self.Ticker} was not extracted")
						self.Status = 'Not Working'
						print(e)
		else:
			print("Internet Disconnected")



	def create_df(self,index = 0):
		if self.Status == 'Working':
				try:
					df  = pd.DataFrame(self.Data, index=[index])
					df.rename(columns = {'Ticker':'ticker','Market_Cap':'c_mc','Current_Price':'c_cp','52week_High':'c_52h',
								'52week_Low':'c_52l','Book_Value':'c_bv','Stock_P/E':'c_pe','Dividend_Yield':'c_dy',
								'ROCE':'c_roce','ROE':'c_roe','Sales_Growth(3Yrs)':'c_sg3','Face_Value':'c_fv',
								'Return_on_assets':'c_roa','Asset_Turnover_Ratio':'c_atr', 'PB_value':'c_pbv', 
								'Debt':'c_debt','Promoter_holding':'c_ph','Pledged_percentage':'c_pleg', 'Profit_growth':'c_pg',
								'Profit_after_tax':'c_pat','Price_to_Sales':'c_pts','Enterprise_Value':'c_enpv', 
								'PEG_Ratio':'c_peg_r','Current_ratio':'c_cr','Debt_to_equity':'c_dte','Interest_Coverage_Ratio':'c_icr',
								'Inventory_turnover_ratio':'c_itr',
								'Dividend_Payout_Ratio':'c_dpr','Quick_ratio':'c_qr','Pros':'pros','Cons':'cons',
								'Standalone_Book_Value':'s_bv','Standalone_Stock_P/E':'s_pe','Standalone_ROCE':'s_roce',
								'Standalone_ROE':'s_roe','Standalone_Sales_Growth(3Yrs)':'s_sg3','Standalone_Return_on_assets':'s_roa',
								'Standalone_Asset_Turnover_Ratio':'s_atr','Standalone_PB_value':'s_pbv','Standalone_Debt':'s_debt',
								'Standalone_Profit_growth':'s_pg','Standalone_Profit_after_tax':'s_pat','Standalone_Price_to_Sales':'s_pts',
								'Standalone_Enterprise_Value':'s_enpv','Standalone_PEG_Ratio':'s_peg_r','Standalone_Current_ratio':'s_cr',
								'Standalone_Debt_to_equity':'s_dte','Standalone_Interest_Coverage_Ratio':'s_icr',
								'Standalone_Inventory_turnover_ratio':'s_itr','Standalone_Dividend_Payout_Ratio':'s_dpr',
								'Standalone_Quick_ratio':'s_qr','Date':'date'
							},inplace = True)
					self.dataframe = self.dataframe.append(df,ignore_index=True)

				except Exception as e:
					print(f"DataFrame of Ticker {self.Ticker} was not Created")
					print(e)			
		else:
			print("Error in function get_fundamental_data")		

		return self.dataframe	

	def send_to_db(self,DataFrame):
		try:
			index = [j for j in range(0,500)]
			DataFrame = DataFrame.sort_values(by = ['ticker'])
			DataFrame['index'] = index
			print(DataFrame)
			DataFrame.to_sql(name = 'fundamental_data',con = self.engine,if_exists ='append',index = False)
			print(f"Data was Successfuly commited")
			
		except Exception as e:
				print(f"Data was not sent to Database")
				print(e)	

	
						


    			



