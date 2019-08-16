import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from sqlalchemy import create_engine, types
import os


def histricalDataToSQL(tickers):

    engine = create_engine('postgresql://'+os.environ['POSTGRESQL_USER']+':'+os.environ['POSTGRESQL_PASSWORD']+'@' +
                           os.environ['POSTGRESQL_HOST_IP']+':'+os.environ['POSTGRESQL_PORT']+'/stock', echo=False)
    result_by_method = getattr(yf.Ticker(tickers), 'history')(period="max")
    result_by_method.index.names = ['date']
    result_by_method.columns = result_by_method.columns.str.lower()
    result_by_method.to_sql(name=tickers.lower(), con=engine, schema='historical_data',
                            if_exists='replace', index=True, dtype={'date': types.Date})
# def histricalDataToJson(tickers):
#     result_by_method = getattr(yf.Ticker(tickers), 'history')
#     result_by_method(period="max").to_json(
#         r'C:\Users\Jing\Desktop\investment\backend\restapi\datatosql\1.json')


# def histricalDataToSQL(tickers, datatype):
#     print(os.environ['POSTGRESQL_DATABASE'])
#     if datatype in os.environ['POSTGRESQL_DATABASE']:
#         engine = create_engine('postgresql://'+os.environ['POSTGRESQL_USER']+':'+os.environ['POSTGRESQL_PASSWORD']+'@' +
#                                os.environ['POSTGRESQL_HOST_IP']+':'+os.environ['POSTGRESQL_PORT']+'/' + datatype, echo=False)
#         result_by_method = getattr(yf.Ticker(tickers), datatype)
#         result_by_method().to_sql(name=tickers, con=engine,
#                                   if_exists='replace', index=True, dtype={'Date': types.Date})
#         print(result_by_method())
#     else:
#         return print("Database not avaliable!")


# download dataframe
# data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
# print(yf.Ticker("AAPL").cashflow)
# save data to PostgreSQL
# data.to_sql(name='SPY', con=engine, if_exists='replace', index=True)

# # parse header
# response.xpath('//table//thead//tr//th//span/text()').getall()
# # parse data
# response.xpath('//table//tbody//tr//td//span/text()').get()
