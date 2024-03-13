import pandas as pd

df = pd.read_csv('C:/Users/ryuji/GeekSalon/my_app/color_com.csv')

def find_sub_color(df, main_color, impression):
    result = df[(df['main_color'] == main_color) & (df['impression'] == impression)]['sub_color'].values
    if len(result) > 0:
        return result[0]
    else:
        return None

#結果を取得
result = find_sub_color(df, 'サーモンピンク', '上品')
if result:
    print(result)
else:
    print("No matching result found.")
