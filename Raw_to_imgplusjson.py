"""
time:   2022.11.4
func:   将原始的数据变为单一文件夹下的数据。
        命名方法：原始子文件夹+_+照片+.jpeg/.json
"""

import os
import shutil

datasets = r"D:\learning\UNNC 科研\Cervical\datasets"
if not os.path.exists(datasets):
    os.mkdir(datasets)
    123
# global
raw_data_dir = r"D:\learning\UNNC 科研\202210_CSD超声标注_图片及视频\CSD图片及标注_170例_507张"
target = r"D:\learning\UNNC 科研\Cervical\datasets\Cervical_data"
if not os.path.exists(target):
    os.mkdir(target)

def main():
    for root, dirs, files in os.walk(raw_data_dir):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        # for f in files:
        #     print(os.path.join(root, f))
        # 遍历所有的文件夹
        for d in dirs:
            cur_dir=os.path.join(root, d)
            for cur_file in os.listdir(cur_dir):
                cur_source=os.path.join(cur_dir,cur_file)
                cur_target=os.path.join(target,d+'_'+cur_file)
                shutil.copy(cur_source,cur_target)


if __name__ == '__main__':
    main()
