import cv2
import numpy as np
import webcolors
from sklearn.cluster import KMeans

def find_closest_color(rgb_tuple):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb_tuple[0]) ** 2
        gd = (g_c - rgb_tuple[1]) ** 2
        bd = (b_c - rgb_tuple[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

def extract_dominant_color(image_path, clusters=5):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    clt = KMeans(n_clusters=clusters)
    clt.fit(image)

    hist = np.bincount(clt.labels_)
    dominant_color = clt.cluster_centers_[hist.argmax()]

    return dominant_color

# 画像パスを指定
image_path = input('服の画像を入れてね') #服の画像を入れてね static/images/clothes_black.jpg

# 画像から支配的な色を抽出
dominant_color_rgb = extract_dominant_color(image_path)
print(dominant_color_rgb)


"""
３つの値を色と対応した近い値に変換（差分を計算して最小値をもとめる）
"""


salmon = [250,114,128]
red = [255,0,0]
darkred = [139,0,0]
pink = [255,192,203]
hotpink = [255,105,180]
coral = [255,1127,80]
orange = [255,165,0]
gold = [255,125,0]
yellow = [255,255,0]
khaki = [240,230,140]
limegreen = [50,205,50]
green = [0,128,0]
darkgreen = [0,100,0]
yellowgreen = [154,205,50]
olive = [128,128,0]
turquoise = [64,224,208]
skyblue = [135,206,135]
royalblue = [65,105,225]
blue = [0,0,255]
navy = [0,0,128]
lavender = [230,230,250]
purple = [128,0,128]
indigo = [75,0,130]
brown = [165,42,42]
white = [255,255,255]
beige = [245,245,220]
ivory = [255,255,240]
silver = [192,192,192]
gray = [128,128,128]
black = [0,0,0]

#色ごとの差の計算
salmon_diff = sum(abs(x - y) for x, y in zip(salmon, dominant_color_rgb))
red_diff = sum(abs(x - y) for x, y in zip(red, dominant_color_rgb))
darkred_diff = sum(abs(x - y) for x, y in zip(darkred, dominant_color_rgb))
pink_diff = sum(abs(x - y) for x, y in zip(pink, dominant_color_rgb))
hotpink_diff = sum(abs(x - y) for x, y in zip(hotpink, dominant_color_rgb))
coral_diff = sum(abs(x - y) for x, y in zip(coral, dominant_color_rgb))
orange_diff = sum(abs(x - y) for x, y in zip(orange, dominant_color_rgb))
gold_diff = sum(abs(x - y) for x, y in zip(gold, dominant_color_rgb))
yellow_diff = sum(abs(x - y) for x, y in zip(yellow, dominant_color_rgb))
khaki_diff = sum(abs(x - y) for x, y in zip(khaki, dominant_color_rgb))
limegreen_diff = sum(abs(x - y) for x, y in zip(limegreen, dominant_color_rgb))
green_diff = sum(abs(x - y) for x, y in zip(green, dominant_color_rgb))
darkgreen_diff = sum(abs(x - y) for x, y in zip(darkgreen, dominant_color_rgb))
yellowgreen_diff = sum(abs(x - y) for x, y in zip(yellowgreen, dominant_color_rgb))
olive_diff = sum(abs(x - y) for x, y in zip(olive, dominant_color_rgb))
turquoise_diff = sum(abs(x - y) for x, y in zip(turquoise, dominant_color_rgb))
skyblue_diff = sum(abs(x - y) for x, y in zip(skyblue, dominant_color_rgb))
royalblue_diff = sum(abs(x - y) for x, y in zip(royalblue, dominant_color_rgb))
blue_diff = sum(abs(x - y) for x, y in zip(blue, dominant_color_rgb))
navy_diff = sum(abs(x - y) for x, y in zip(navy, dominant_color_rgb))
lavender_diff = sum(abs(x - y) for x, y in zip(lavender, dominant_color_rgb))
purple_diff = sum(abs(x - y) for x, y in zip(purple, dominant_color_rgb))
indigo_diff = sum(abs(x - y) for x, y in zip(indigo, dominant_color_rgb))
brown_diff = sum(abs(x - y) for x, y in zip(brown, dominant_color_rgb))
white_diff = sum(abs(x - y) for x, y in zip(white, dominant_color_rgb))
beige_diff = sum(abs(x - y) for x, y in zip(beige, dominant_color_rgb))
ivory_diff = sum(abs(x - y) for x, y in zip(ivory, dominant_color_rgb))
silver_diff = sum(abs(x - y) for x, y in zip(silver, dominant_color_rgb))
gray_diff = sum(abs(x - y) for x, y in zip(gray, dominant_color_rgb))
black_diff = sum(abs(x - y) for x, y in zip(black, dominant_color_rgb))


# 最小の差を持つ色の特定
min_diff_color = min((salmon, salmon_diff),
                     (red, red_diff),
                     (darkred, darkred_diff),
                     (pink, pink_diff),
                     (hotpink, hotpink_diff),
                     (coral, coral_diff),
                     (orange, orange_diff),
                     (gold, gold_diff),
                     (yellow, yellow_diff),
                     (khaki, khaki_diff),
                     (limegreen, limegreen_diff),
                     (green, green_diff),
                     (darkgreen, darkgreen_diff),
                     (yellowgreen, yellowgreen_diff),
                     (olive, olive_diff),
                     (turquoise, turquoise_diff),
                     (skyblue, skyblue_diff),
                     (royalblue, royalblue_diff),
                     (blue, blue_diff),
                     (navy, navy_diff),
                     (lavender, lavender_diff),
                     (purple, purple_diff),
                     (indigo, indigo_diff),
                     (brown, brown_diff),
                     (white, white_diff),
                     (beige, beige_diff),
                     (ivory, ivory_diff),
                     (silver, silver_diff),
                     (gray, gray_diff),
                     (black, black_diff),
                     key=lambda x: x[1])

#最小の差を持つ色
rgb_triplet = min_diff_color[0]

color_name = webcolors.rgb_to_name(rgb_triplet, spec='css3') #整数RGB値からカラー名へ変換
print(color_name)