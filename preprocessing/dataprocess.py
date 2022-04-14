import cv2
import pandas as pd
import numpy as np
import glob

img_x_size = 3264
img_y_size = 2448
patch_x_size = 408
patch_y_size = 306
x_stride = 204
y_stride = 153
input_dir_image = '/mnt/d/Git/Capstone/data/result_detection/'
output_dir = '/mnt/d/Git/Capstone/preprocessing/label/'

img_list = glob.glob(input_dir_image+'*.csv')

for imname in img_list:
    df = pd.read_csv(imname)
    df = df.iloc[:, :-1]
    imname=imname.split('/')[-1]

    for i in range(0,(img_x_size-patch_x_size)//x_stride+1,1):
        for k in range(0,(img_y_size-patch_y_size)//y_stride+1,1):
            x = i*x_stride
            y = k*y_stride
            x_center = df['right']-20
            y_center = df['bottom']-20

            result = df[(x_center >= x) & (x_center < (x+patch_x_size)) & (y_center >=y) & (y_center < (y+patch_y_size))]

            result.iloc[:,2] = result['left'] - x
            result.iloc[:,4] = result['right'] - x
            result.iloc[:,3] = result['top'] - y
            result.iloc[:,5] = result['bottom'] - y

            print('save '+output_dir+'{}_{}_{}.csv'.format(imname[:-4],x, y))
            result.to_csv(output_dir+'{}_{}_{}.csv'.format(imname[:-4],x, y), sep=',')
