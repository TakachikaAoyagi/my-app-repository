#color_com.csvのimpression列から該当色のimpressionを抽出

import pandas as pd

df = pd.read_csv('C:/Users/ryuji/GeekSalon/my_app/color_com.csv')

def impression(main_color):
    a = df[(df['main_color'] == main_color)]['impression']
    for i in range(len(a)):
        b = a.values[i]
        print(b)
impression('ネイビー')

