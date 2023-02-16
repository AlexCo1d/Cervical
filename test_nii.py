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

