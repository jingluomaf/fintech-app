import scrapy
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from sqlalchemy import create_engine
import os


class QuotesSpider(scrapy.Spider):

    def dataToSQL(tickers, datatype):
        if datatype in os.environ['POSTGRESQL_DATABASE']:
            engine = create_engine('postgresql://'+os.environ['POSTGRESQL_USER']+':'+os.environ['POSTGRESQL_PASSWORD']+'@' +
                                   os.environ['POSTGRESQL_HOST_IP']+':'+os.environ['POSTGRESQL_PORT']+'/' + datatype, echo=False)
            result_by_method = getattr(yf.Ticker(tickers), datatype)
            result_by_method.to_sql(name=tickers, con=engine,
                                    if_exists='replace', index=False)
        else:
            return print("Database not avaliable!")

    dataToSQL('AAPL', 'cashflow')
