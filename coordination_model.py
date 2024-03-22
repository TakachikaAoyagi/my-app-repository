import pandas as pd

df = pd.read_csv('C:/Users/ryuji/GeekSalon/my_app/color_com.csv')

def find_sub_color(main_color, impression):
    result = df[(df['main_color'] == main_color) & (df['impression'] == impression)]['sub_color'].values
    if len(result) > 0:
        return result[0]
    else:
        return None

def main_color_eng(main_color):
    result_m_eng = df[df['main_color'] == main_color]['main_color_eng'].values
    if len(result_m_eng) > 0:
        return result_m_eng[0]
    else:
        return None

def find_sub_color_eng(main_color, impression):
    result_eng = df[(df['main_color'] == main_color) & (df['impression'] == impression)]['sub_color_eng'].values
    if len(result_eng) > 0:
        return result_eng[0]
    else:
        return None
