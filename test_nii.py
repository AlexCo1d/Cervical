
import nibabel as nib
from matplotlib import pyplot as plt

filename='/home/user/Download/20220913_国妇婴_正常子宫超声视频及标注_2例/ZC1_0001_AVI_Label.nii'
img=nib.load(filename)
print(img.shape)
data=img.get_data()
epi_img_data=data

def show_slices(slices):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")
###################
#这里的数值可以调整
###################
slice_0 = epi_img_data[350, :, :]
slice_1 = epi_img_data[:, 360, :]
slice_2 = epi_img_data[:, :, 105]
show_slices([slice_0, slice_1, slice_2])

# print(data.shape,type(data))
# plt.figure(figsize=(8,5))
# plt.imshow(data[:,:,10],cmap='gray')

plt.show()
# pixdim=img.header['pixdim']
# print(f'z轴分辨率：{pixdim[3]}')
# print(f'in plane 分辨率:{pixdim[1]}*{pixdim[2]}')
'''
import matplotlib
from matplotlib import pylab as plt
import nibabel as nib
from nibabel.viewers import OrthoSlicer3D

file = '/home/user/Download/20220913_国妇婴_正常子宫超声视频及标注_2例/ZC1_0001_AVI_Label.nii'  # 你的nii或者nii.gz文件路径
img = nib.load(file)

print(img.header['db_name'])  # 输出nii的头文件
width, height, queue = img.dataobj.shape
OrthoSlicer3D(img.dataobj).show()

num = 1
for i in range(0, queue, 10):
    img_arr = img.dataobj[:, :, i]
    plt.subplot(5, 4, num)
    plt.imshow(img_arr, cmap='gray')
    num += 1

plt.show()
'''
