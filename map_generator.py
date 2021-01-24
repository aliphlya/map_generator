#隨機地圖生成器 V1.0
#作者 春雨宮可
#更新時間 V1.0 2020.08.17


#import 隨機、陣列、圖片生成、時間
import random
import numpy as np
from PIL import Image
import time
import datetime

#開始計算時間
start = datetime.datetime.now()

#可以改的兩個參數
x = 100
count = 1000000

#隨機生成x*x的亂數陣列
map1 = np.zeros((x,x),dtype = int)
for i in range(x):
    for j in range(x):
            map1[i][j] = random.randint(0,3)
#0 海洋 藍色
#1 草地 淺綠
#2 沙漠 黃色
#3 樹林 深綠

#隨機挑選一個點 使那個點周圍與那個點數字相同 直到count=0結束
#      2                          0
#    1 0 1      =====>          0 0 0
#      3                          0

while count != 0:
    rd_x = random.randint(1,x-2)
    rd_y = random.randint(1,x-2)
    map1[rd_x-1][rd_y],map1[rd_x][rd_y-1], map1[rd_x+1][rd_y] , map1[rd_x][rd_y+1] = map1[rd_x][rd_y] , map1[rd_x][rd_y] , map1[rd_x][rd_y], map1[rd_x][rd_y]    
    count = count - 1


#尋找一個點 如果那個點周圍數字與那個點不同 把周圍數字變成那個點
#        1                          1
#      1 0 1        ======>       1 1 1
#        1                          1

for i in range(1,x-1):
    for j in range(1,x-1):
        if map1[i-1][j] != map1[i][j] and map1[i][j-1] != map1[i][j] and map1[i+1][j] != map1[i][j] and map1[i][j+1] != map1[i][j]:
            map1[i][j] = map1[i-1][j]

#邊邊狀況
#     1                         1
#     0 1         ======>       1 1
#     1                         1

for i in range(1,x-1):
    if map1[0][i] != map1[1][i] and map1[0][i] != map1[0][i-1] and map1[0][i] != map1[0][i+1]:
        map1[0][i] = map1[1][i] 
    if map1[x-1][i] != map1[x-2][i] and map1[x-1][i] != map1[x-1][i-1] and map1[x-1][i] != map1[x-1][i+1]:
        map1[x-1][i] = map1[x-2][i]
    if map1[i][0] != map1[i][1] and map1[i][0] != map1[i+1][0] and map1[i][0] != map1[i-1][0]:
        map1[i][0] = map1[i][1] 
    if map1[i][x-1] != map1[i][x-2] and map1[i][x-1] != map1[i+1][x-1] and map1[i][x-1] != map1[i-1][x-1]:
        map1[i][x-1] = map1[i][x-2]

#角角狀況
#     0 1                     1 1
#     1         ======>       1 

if map1[0][0] != map1[0][1] and map1[0][0] != map1[1][0]:
    map1[0][0] = map1[0][1]
if map1[0][x-1] != map1[0][x-2] and map1[0][x-1] != map1[1][x-1]:
    map1[0][x-1] = map1[0][x-2]
if map1[x-1][0] != map1[x-1][1] and map1[x-1][0] != map1[x-2][0]:
    map1[x-1][0] = map1[x-1][1]
if map1[x-1][x-1] != map1[x-1][x-2] and map1[x-1][x-1] != map1[x-2][x-1]:
    map1[x-1][x-1] = map1[x-2][x-1]

#圖片套入

map2 = Image.new( "RGB", (16 * x,16 * x) )
tree = Image.open( "tree.png" )
ocean = Image.open( "ocean.png" )
desert = Image.open( "desert.png" )
grass = Image.open( "grass.png" )

for i in range(x):
    for j in range(x):
        if map1[i][j] == 0:
            map2.paste( ocean, (16 * j, 16 * i) )   
        if map1[i][j] == 1:
            map2.paste( grass, (16 * j, 16 * i) )
        if map1[i][j] == 2:
            map2.paste( desert, (16 * j, 16 * i) )
        if map1[i][j] == 3:
            map2.paste( tree, (16 * j, 16 * i) )

#圖片匯出
t = time.localtime()
time_ = time.strftime("%Y-%m-%d %H-%M-%S", t)
map2.save("map {0} .png".format(time_))

#print 執行時間
end = datetime.datetime.now()
print("執行時間：", end - start)
