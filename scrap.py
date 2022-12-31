from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
START_URL ="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
find_all.get(START_URL)
scrapped_data=[]
time.sleep(10)

def scrape():
    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )
        bright_star_table = soup.find("table", attrs={"class", "wikitable"})
        table_body = bright_star_table. find('tbody' )
        table_rows = table_body. find_all( 'tr')
    for row in table_rows:
        table_cols = row. find_all('td' )
        temp_list = []
        print(table_cols)
    for col_data in table_cols:
        print (col_data. text)
        data = col_data. text. strip()
        print (data)
        temp_list. append(data)
        scarped_data . append (temp_list)



stars_data = []
for i in range(0, len(scarped_data) ) :
    star_names = scarped_data[i] [1]
    Distance = scarped_data[i] [3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i ] [6]
    Lum = scarped_data[i] [7]

    required_data = [star_names, Distance, Mass, Radius, Lum]
    stars_data . append(required_data)

headers = ['Star_name' , 'Distance' , 'Mass', 'Radius' , ' Luminosity' ]

new_planet_df_1=pd.DataFrame(scrapped_data,columns=headers)
new_planet_df_1.to_csv("newscrapData.csv",index=True,index_label="id")
