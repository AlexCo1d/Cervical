import json
import commentjson
import tarfile
import os
import glob

"""
1.解压存储的标签文件 untar
2.去除一个series的标注信息，包括层号、类别、坐标等等
3.存储到json文件
4.labelme打开确认下
"""

def untar(fname, output_dirs):
    t = tarfile.open(fname)
    t.extractall(path = output_dirs)

def Polyspoints3D2points2D(E_Points):
    tmp_points2d = []
    for e in E_Points:
        e_p = e["Pos"]
        tmp_points2d.append([e_p[0], e_p[1]])
    return tmp_points2d

def save2jsonFile(list_coors, save_dir, filename):
    A = dict()
    listbigoption = []

    for coor in list_coors:
        # print('coor:', coor)
        listobject = dict()
        listxy = coor[:-1]
        label_cls = coor[-1]

        listobject['points'] = listxy
        listobject['line_color'] = 'null'
        listobject['label'] = str(label_cls)
        listobject['fill_color'] = 'null'
        listbigoption.append(listobject)

    A['lineColor'] = [0, 255, 0, 128]
    A['imageData'] = 'imageData'
    A['fillColor'] = [255, 0, 0, 128]
    A['imagePath'] = filename.replace('.json', '.png')
    A['shapes'] = listbigoption
    A['flags'] = {}
    with open(os.path.join(save_dir, filename), 'w') as f:
        json.dump(A, f, indent=2, ensure_ascii=False)


def Polys_json(json_path=None, with_comment=False):
    label_list = []
    with open(json_path, encoding='utf-8') as f:
        if with_comment:  # 若*.json中添加了注释，则使用commentjson。若无注释则使用json库也可。
            Anno_Dict = commentjson.load(f)
        else:
            Anno_Dict = json.load(f)

    Depth, Name = str(Anno_Dict["FileInfo"]["Depth"]), Anno_Dict["FileInfo"]["Name"].split('_')[0]
    Polygon_list = Anno_Dict["Polys"]

    dict_sliceNum_coor = {}
    for E_idx, E_item in enumerate(Polygon_list):
        Shapes_info = E_item["Shapes"]
        for j_idx, j_item in enumerate(Shapes_info):
            E_Label = str(j_item["labelType"])
            E_SliceIndex = str(j_item["ImageFrame"])
            E_Points = j_item["Points"]

            # 由于存储标签中坐标是xyz的，labelme打开一张图时候，不需要高度信息，就去除掉
            E_Points = Polyspoints3D2points2D(E_Points)
            E_Points.append(E_Label)

            # print('slicenum: {}\n类别id：{}\n坐标：{}\n'.format(E_SliceIndex, E_Label, E_Points))
            label_list.append(E_Label)

            if E_SliceIndex not in dict_sliceNum_coor.keys():
                dict_sliceNum_coor[E_SliceIndex] = [E_Points]
            else:
                cur_coor = dict_sliceNum_coor[E_SliceIndex]
                cur_coor.append(E_Points)
                dict_sliceNum_coor[E_SliceIndex] = cur_coor

    for key, value in dict_sliceNum_coor.items():
        save_dir = os.path.join(os.path.dirname(json_path), 'json')
        filename = Name + '_' + (6-len(key))*'0'+key+'_'+Depth+'.json'
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        save2jsonFile(value, save_dir, filename)
        print(save_dir, filename)

    return label_list


if __name__ == '__main__':
    data_dir = r'Z:\cancer1-100'
    patient_list = os.listdir(data_dir)
    label_list_all = []
    TB_PatientNum = 0

    for patient in patient_list:
        file_dir = os.path.join(data_dir, patient)
        print(file_dir)
        if os.path.exists(os.path.join(data_dir, patient, 'json')):
            continue

        tar_list = glob.glob(file_dir + r'/*.tar')
        json_list = glob.glob(file_dir + r'/*.json')
        if len(tar_list) > len(json_list):
            if len(tar_list) > 0:
                for file_path in tar_list:
                    print('start untar ---', file_path)
                    untar(file_path, file_dir)
		json_list = glob.glob(file_dir + r'/*.json')
        if len(json_list) > 0:
            for file_path in json_list:
                # Polys
                label_list = Polys_json(json_path=file_path, with_comment=True)
