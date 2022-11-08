"""
time:   2022.11.8
func:   将datasets数据中的Cervical_data中的负样本进行更新
        遍历文件，该jpg/bmp若不存在json，则根据他的文件大小生成一个png格式的mask
"""

import os
import cv2
import shutil
import numpy as np

# global
source = "datasets/Cervical_data"
JPEGImages = "datasets/JPEGImages"
SegmentationClass = "datasets/SegmentationClass"

if __name__ == '__main__':
    for cur in os.listdir(source):

        # 仅处理jpg或者bmp文件
        if cur.endswith(".jpg") or cur.endswith(".bmp"):
            image = cv2.imread(os.path.join(source, cur), -1)
            # 替换成json进行检测
            cur_json = ""
            if cur.endswith(".jpg"):
                cur_json = cur.replace(".jpg", ".json")
            elif cur.endswith(".bmp"):
                cur_json = cur.replace(".bmp", ".json")
            cur_json_dir = os.path.join(source, cur_json)
            cur_dir = os.path.join(source, cur)

            # 如果没有该json文件，转化成jpg到JPEGImages中，并且生成一个空白的mask到SegmentationClass中
            if not os.path.isfile(cur_json_dir):
                if cur.endswith(".jpg"):
                    shutil.copy(cur_dir, os.path.join(JPEGImages, cur))
                else:
                    cv2.imwrite(os.path.join(JPEGImages, cur.replace(".bmp", ".jpg")), image)
                # 添加mask
                cv2.imwrite(os.path.join(SegmentationClass, cur[:-4] + ".png"), np.zeros(image.shape[:2]))
