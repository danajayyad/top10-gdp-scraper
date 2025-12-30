import pandas as pd
import numpy as np

def get_top10_gdp(df):

    df.columns =range(df.shape[1])
    df = df[[0,2]]
    df = df.iloc[1:11 , :]
    df.columns  = ['Country' , 'GDP (Millions USD)']
    '''Modify the GDP column of the DataFrame, converting the value available in Million USD to Billion USD. Use the `round()` method of Numpy library to round the value to 2
    decimal places. Modify the header of the DataFrame to `GDP (Billion USD)`.'''
    df['GDP (Millions USD)'] = df['GDP (Millions USD)'].astype(int)
    df[['GDP (Millions USD)']] = df[['GDP (Millions USD)']] / 1000
    df[['GDP (Millions USD)']]  = np.round(df[['GDP (Millions USD)']]  , 2)
    df.rename(columns = {'GDP (Millions USD)' : 'GDP (Billion USD)'} , inplace=True)
    return df



def get_table_df(url):
    tables = pd.read_html(URL)
    df = tables[3]
    return df
    

if __name__ == "__main__":
    URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
    df = get_table_df(URL)
    df = get_top10_gdp(df)
    df.to_csv('Largest_economies.csv', index=False)
