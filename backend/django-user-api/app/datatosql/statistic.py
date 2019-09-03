import pandas as pd

tgt_website = r'https://sg.finance.yahoo.com/quote/WDC/key-statistics?p=WDC'


def get_key_stats(tgt_website):

    # The web page is make up of several html table. By calling read_html function.
    # all the tables are retrieved in dataframe format.
    # Next is to append all the table and transpose it to give a nice one row data.
    df_list = pd.read_html(tgt_website, )
    result_df = df_list[0]
    for df in df_list[1:]:
        result_df = result_df.append(df)
    print(result_df)
    # The data is in column format.
    # Transpose the result to make all data in single row
    return result_df.set_index(0).T


# Save the result to csv
result_df = get_key_stats(tgt_website)
print(result_df)

# # Get tickers
# weblink = 'https://www.nasdaq.com/screening/companies-by-name.aspx?letter=A&render=download'
# sym_df = pd.read_csv(weblink)
# stock_symbol_list = sym_df.Symbol.tolist()

# # The last step will be to iterate all the symbols and get the corresponding key statistcis
# all_result_df = pd.DataFrame()
# url_prefix = 'https://sg.finance.yahoo.com/quote/{0}/key-statistics?p={0}'
# for sym in stock_symbol_list:
#     stock_url = url_prefix.format(sym)
#     result_df = get_key_stats(stock_url)
#     if len(all_result_df) == 0:
#         all_result_df = result_df
#     else:
#         all_result_df = all_result_df.append(result_df)

# # Save all results
# all_result_df.to_csv('results.csv', index=False)
