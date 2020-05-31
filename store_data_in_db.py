from stock_data import *
import time 
from datetime import datetime
import threading
import pandas as pd 



username 	= "Your_Screener_Username"
password 	= "Your_Screener_Password"
db_name  	= "fundamentals"
db_usename 	= "postgres"
db_password = "1234"
host = "localhost"



obj1 = Stock_Data(username,password,db_usename,db_password,host,db_name)
obj2 = Stock_Data(username,password,db_usename,db_password,host,db_name)
obj3 = Stock_Data(username,password,db_usename,db_password,host,db_name)
obj4 = Stock_Data(username,password,db_usename,db_password,host,db_name)


TICKER_SET1 = ['AARTIIND', 'AAVAS', 'ABBOTINDIA', 'ABCAPITAL', 'ABFRL', 'ACC', 'ADANIGAS', 'ADANIGREEN', 'ADANIPORTS', 'ADANIPOWER',
			 'ADANITRANS', 'ADVENZYMES', 'AEGISCHEM', 'AFFLE', 'AIAENG', 'AJANTPHARM', 'AKZOINDIA', 'ALKEM', 'ALLCARGO', 'AMARAJABAT', 
			 'AMBER', 'AMBUJACEM', 'APLAPOLLO', 'APLLTD', 'APOLLOHOSP', 'APOLLOTYRE', 'ARVINDFASN', 'ASAHIINDIA', 'ASHOKA', 'ASHOKLEY', 
			 'ASIANPAINT', 'ASTERDM', 'ASTRAL', 'ASTRAZEN', 'ATUL', 'AUBANK', 'AUROPHARMA', 'AVANTIFEED', 'AXISBANK', 'BAJAJ-AUTO', 
			 'BAJAJCON', 'BAJAJELEC', 'BAJAJFINSV', 'BAJAJHLDNG', 'BAJFINANCE', 'BALKRISIND', 'BALMLAWRIE', 'BALRAMCHIN', 'BANDHANBNK', 
			 'BANKBARODA', 'BANKINDIA', 'BASF', 'BATAINDIA', 'BAYERCROP', 'BBTC', 'BDL', 'BEL', 'BEML', 'BERGEPAINT', 'BHARATFORG', 
			 'BHARTIARTL', 'BHEL', 'BIOCON', 'BIRLACORPN', 'BLISSGVS', 'BLUEDART', 'BLUESTARCO', 'BOMDYEING', 'BOSCHLTD', 'BPCL', 
			 'BRIGADE', 'BRITANNIA', 'BSE', 'BSOFT', 'CADILAHC', 'CANBK', 'CANFINHOME', 'CAPLIPOINT', 'CARBORUNIV', 'CARERATING', 
			 'CASTROLIND', 'CCL', 'CDSL', 'CEATLTD', 'CENTRALBK', 'CENTURYPLY', 'CERA', 'CESC', 'CGCL', 'CHALET', 'CHAMBLFERT', 
			 'CHENNPETRO', 'CHOLAFIN', 'CHOLAHLDNG', 'CIPLA', 'COALINDIA', 'COCHINSHIP', 'COLPAL', 'CONCOR', 'COROMANDEL', 
			 'CREDITACC', 'CRISIL', 'CROMPTON', 'CUB', 'CUMMINSIND', 'CYIENT', 'DABUR', 'DALBHARAT', 'DBCORP', 'DBL', 'DCAL', 
			 'DCBBANK', 'DCMSHRIRAM', 'DEEPAKNTR', 'DELTACORP', 'DHFL', 'DISHTV', 'DIVISLAB', 'DIXON', 'DLF', 'DMART', 'DRREDDY', 'ECLERX', 'EDELWEISS', 'EICHERMOT']

TICKER_SET2 = ['EIDPARRY', 'EIHOTEL', 'ELGIEQUIP', 'EMAMILTD', 'ENDURANCE', 'ENGINERSIN', 'EQUITAS', 'ERIS', 'ESCORTS', 'ESSELPACK', 'EXIDEIND', 'FCONSUMER', 
				'FDC', 'FEDERALBNK', 'FINCABLES', 'FINEORG', 'FINPIPE', 'FLFL', 'FMGOETZE', 'FORTIS', 'FRETAIL', 'FSL', 'GAIL', 'GALAXYSURF', 'GARFIBRES', 'GAYAPROJ', 
				'GEPIL', 'GESHIP', 'GET&D', 'GHCL', 'GICRE', 'GILLETTE', 'GLAXO', 'GLENMARK', 'GMDCLTD', 'GMRINFRA', 'GNFC', 'GODFRYPHLP', 'GODREJAGRO', 'GODREJCP', 
				'GODREJIND', 'GODREJPROP', 'GPPL', 'GRANULES', 'GRAPHITE', 'GRASIM', 'GREAVESCOT', 'GRINDWELL', 'GSFC', 'GSPL', 'GUJALKALI', 'GUJGASLTD', 'GULFOILLUB', 
				'HAL', 'HATSUN', 'HAVELLS', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HEG', 'HEIDELBERG', 'HERITGFOOD', 'HEROMOTOCO', 'HEXAWARE', 'HFCL', 
				'HIMATSEIDE', 'HINDALCO', 'HINDCOPPER', 'HINDPETRO', 'HINDUNILVR', 'HINDZINC', 'HONAUT', 'HSCL', 'HUDCO', 'IBREALEST', 'IBULHSGFIN', 'IBULISL', 'IBVENTURES', 
				'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'ICRA', 'IDBI', 'IDEA', 'IDFC', 'IDFCFIRSTB', 'IEX', 'IFBIND', 'IFCI', 'IGL', 'IIFL', 'INDHOTEL', 'INDIACEM', 
				'INDIAMART', 'INDIANB', 'INDIGO', 'INDOSTAR', 'INDUSINDBK', 'INFIBEAM', 'INFRATEL', 'INFY', 'INOXLEISUR', 'INTELLECT', 'IOB', 'IOC', 'IPCALAB', 'IRB', 
				'IRCON', 'ISEC', 'ITC', 'ITDC', 'ITDCEM', 'ITI', 'J&KBANK', 'JAGRAN', 'JAICORPLTD', 'JAMNAAUTO', 'JBCHEPHARM', 'JCHAC', 'JINDALSAW', 'JINDALSTEL', 'JISLJALEQS', 'JKCEMENT']

TICKER_SET3 = ['JKLAKSHMI', 'JKPAPER', 'JKTYRE', 'JMFINANCIL', 'JSL', 'JSLHISAR', 'JSWENERGY', 'JSWSTEEL', 'JUBILANT', 'JUBLFOOD', 'JUSTDIAL', 'JYOTHYLAB', 'KAJARIACER', 
				'KALPATPOWR', 'KANSAINER', 'KARURVYSYA', 'KEC', 'KEI', 'KENNAMET', 'KIRLOSENG', 'KNRCON', 'KOLTEPATIL', 'KOTAKBANK', 'KPITTECH', 'KPRMILL', 'KRBL', 'KSCL', 
				'KTKBANK', 'L&TFH', 'LAKSHVILAS', 'LALPATHLAB', 'LAURUSLABS', 'LAXMIMACH', 'LEMONTREE', 'LICHSGFIN', 'LINDEINDIA', 'LT', 'LTI', 'LTTS', 'LUPIN', 'LUXIND', 
				'M&M', 'M&MFIN', 'MAGMA', 'MAHABANK', 'MAHINDCIE', 'MAHLOG', 'MAHSCOOTER', 'MAHSEAMLES', 'MANAPPURAM', 'MARICO', 'MARUTI', 'MASFIN', 'MCDOWELL-N', 'MCX', 
				'METROPOLIS', 'MFSL', 'MGL', 'MHRIL', 'MIDHANI', 'MINDACORP', 'MINDAIND', 'MINDTREE', 'MMTC', 'MOIL', 'MOTHERSUMI', 'MOTILALOFS', 'MPHASIS', 'MRF', 'MRPL', 
				'MUTHOOTFIN', 'NAM-INDIA', 'NATCOPHARM', 'NATIONALUM', 'NAUKRI', 'NAVINFLUOR', 'NBCC', 'NBVENTURES', 'NCC', 'NESCO', 'NESTLEIND', 'NETWORK18', 'NFL', 'NH', 
				'NHPC', 'NIACL', 'NIITTECH', 'NILKAMAL', 'NLCINDIA', 'NMDC', 'NTPC', 'OBEROIRLTY', 'OFSS', 'OIL', 'OMAXE', 'ONGC', 'ORIENTCEM', 'ORIENTELEC', 'ORIENTREF', 
				'PAGEIND', 'PARAGMILK', 'PCJEWELLER', 'PEL', 'PERSISTENT', 'PETRONET', 'PFC', 'PFIZER', 'PGHH', 'PGHL', 'PHILIPCARB', 'PHOENIXLTD', 'PIDILITIND', 'PIIND', 'PNB', 
				'PNBHOUSING', 'PNCINFRA', 'POLYCAB', 'POWERGRID', 'PRAJIND', 'PRESTIGE', 'PRSMJOHNSN', 'PTC', 'PVR', 'QUESS', 'RADICO']

TICKER_SET4 = ['RAIN', 'RAJESHEXPO', 'RALLIS', 'RAMCOCEM', 'RATNAMANI', 'RAYMOND', 'RBLBANK', 'RCF', 'RECLTD', 'REDINGTON', 'RELAXO', 'RELCAPITAL', 'RELIANCE', 'RELINFRA', 
				'RENUKA', 'REPCOHOME', 'RESPONIND', 'RITES', 'RPOWER', 'RVNL', 'SADBHAV', 'SAIL', 'SANOFI', 'SBILIFE', 'SBIN', 'SCHAEFFLER', 'SFL', 'SHILPAMED', 'SHK', 'SHOPERSTOP', 
				'SHREECEM', 'SHRIRAMCIT', 'SIEMENS', 'SIS', 'SJVN', 'SKFINDIA', 'SOBHA', 'SOLARINDS', 'SONATSOFTW', 'SOUTHBANK', 'SPANDANA', 'SPARC', 'SPICEJET', 'SRF', 'SRTRANSFIN', 
				'STAR', 'STARCEMENT', 'STRTECH', 'SUDARSCHEM', 'SUNCLAYLTD', 'SUNDARMFIN', 'SUNDRMFAST', 'SUNPHARMA', 'SUNTECK', 'SUNTV', 'SUPRAJIT', 'SUPREMEIND', 'SUZLON', 'SWANENERGY', 
				'SWSOLAR', 'SYMPHONY', 'SYNGENE', 'TAKE', 'TASTYBITE', 'TATACONSUM', 'TATAELXSI', 'TATAINVEST', 'TATAMOTORS', 'TATAMTRDVR', 'TATAPOWER', 'TATASTEEL', 'TATASTLBSL', 'TCIEXP', 
				'TCNSBRANDS', 'TCS', 'TEAMLEASE', 'TECHM', 'TECHNOE', 'THERMAX', 'THYROCARE', 'TIINDIA', 'TIMETECHNO', 'TIMKEN', 'TITAN', 'TORNTPHARM', 'TORNTPOWER', 'TRENT', 'TRIDENT', 
				'TRITURBINE', 'TTKPRESTIG', 'TV18BRDCST', 'TVSMOTOR', 'TVTODAY', 'UBL', 'UCOBANK', 'UFLEX', 'UJJIVAN', 'ULTRACEMCO', 'UNIONBANK', 'UPL', 'VAIBHAVGBL', 'VAKRANGEE', 'VARROC', 
				'VBL', 'VEDL', 'VENKEYS', 'VGUARD', 'VINATIORGA', 'VIPIND', 'VMART', 'VOLTAS', 'VRLLOG', 'VSTIND', 'VTL', 'WABAG', 'WABCOINDIA', 'WELCORP', 'WELSPUNIND', 'WESTLIFE', 'WHIRLPOOL', 
				'WIPRO', 'WOCKPHARMA', 'ZEEL', 'ZENSARTECH', 'ZYDUSWELL']


final_df = pd.DataFrame()

def get_data_and_load1():
	for i in TICKER_SET1:
		obj1.get_fundamental_data(i)
		time.sleep(1)
		obj1.create_df()
	df = obj1.dataframe
	global final_df
	final_df =  final_df.append(df)



def get_data_and_load2():
	for i in TICKER_SET2:
		obj2.get_fundamental_data(i)
		time.sleep(1)
		obj2.create_df()
	df = obj2.dataframe	
	global final_df 
	final_df =  final_df.append(df)
	

def get_data_and_load3():
	for i in TICKER_SET3:
		obj3.get_fundamental_data(i)
		time.sleep(1)
		obj3.create_df()
	df = obj3.dataframe	
	global final_df
	final_df =  final_df.append(df)

def get_data_and_load4():
	for i in TICKER_SET4:
		obj4.get_fundamental_data(i)
		time.sleep(1)
		obj4.create_df()
	df = obj4.dataframe	
	global final_df
	final_df =  final_df.append(df)

t1 = threading.Thread(target = get_data_and_load1)
t2 = threading.Thread(target = get_data_and_load2)
t3 = threading.Thread(target = get_data_and_load3)
t4 = threading.Thread(target = get_data_and_load4)



t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

obj1.send_to_db(final_df)

	

