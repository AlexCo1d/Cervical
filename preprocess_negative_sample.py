"""
time:   2022.11.8
func:   将datasets数据中的Cervical_data中的负样本进行更新
        遍历文件，该jpg/bmp若不存在json，则根据他的文件大小生成一个png格式的mask
"""

import os
import shutil
from labelme import utils

# global
source = "datasets/Cervical_data"
JPEGImages = "datasets/JPEGImages"
SegmentationClass = "datasets/SegmentationClass"

if __name__ == '__main__':
    for cur in os.listdir(source):
        cur= cur.replace(".jpg",".json") if cur.endswith(".jpg") else( cur.replace(".bmp",".json") if cur.endswith(".bmp") else())
        cur_dir=os.path.join(source,cur)
        if not os.path.isfile(cur_dir):
            shutil.copy(cur_dir, os.path.join(JPEGImages,cur))
