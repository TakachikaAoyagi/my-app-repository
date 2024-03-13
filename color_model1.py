import cv2
import numpy as np
import webcolors
from sklearn.cluster import KMeans

#与えられた画像から支配的な色を抽出。RGB形式に変換。
def extract_dominant_color(image_path, clusters=5):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    clt = KMeans(n_clusters=clusters)
    clt.fit(image)

    hist = np.bincount(clt.labels_)
    dominant_color = clt.cluster_centers_[hist.argmax()]

    return dominant_color

dict = {'サーモンピンク':[250,114,128],'赤':[255,0,0],'darkred':[139,0,0],'pink':[255,192,203],
        'hotpink':[255,105,180],'coral':[255,1127,80],'オレンジ':[255,165,0],'ゴールド':[255,125,0],
        '黄色':[255,255,0],'カーキ':[240,230,140],'ライム':[50,205,50],'緑':[0,128,0],
        '深緑':[0,100,0],'黄緑':[154,205,50],'olive':[128,128,0],'turquoise':[64,224,208],
        'skyblue':[135,206,135],'royalblue':[65,105,225],'青':[0,0,255],'ネイビー':[0,0,128],
        'lavende': [230,230,250],'パープル':[128,0,128],'indigo':[75,0,130],'ブラウン':[165,42,42],
        '白':[255,255,255],'ベージュ':[245,245,220],'ivory':[255,255,240],'シルバー':[192,192,192],
        'グレー':[128,128,128],'黒':[0,0,0]}

#与えられたRGBのタプルに最も近いCSS3色名を見つける。
def find_closest_color(rgb_tuple):
    min_colors = {}
    for key,value in dict.items():
        r_c = value[0]
        g_c = value[1]
        b_c = value[2]
        rd = (r_c - rgb_tuple[0]) ** 2
        gd = (g_c - rgb_tuple[1]) ** 2
        bd = (b_c - rgb_tuple[2]) ** 2
        min_colors[(rd + gd + bd)] = key
    return min_colors[min(min_colors.keys())]


def get_dominant_color_name(image_path):
    dominant_color_rgb = extract_dominant_color(image_path)
    closest_color_name = find_closest_color(dominant_color_rgb)
    return closest_color_name

if __name__ == "__main__":
    image_path = input('服の画像を入れてね')
    color_name = get_dominant_color_name(image_path)
    print(color_name)
#服の画像を入れてね static/images/clothes_black.jpg 
