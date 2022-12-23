import os
path='/home/yangjiaqi/Desk/Cervical/Medical_Datasets/Images'

#获取该目录下所有文件，存入列表中
f=os.listdir(path)

n=0
for i in f:

    #设置旧文件名（就是路径+文件名）
    oldname=path+f[n]
    print(f[n].split('.')[0].replace('','_'))
    #设置新文件名
    # newname=path+f[n].split('.')[0].replace('','_')+'.jpg'

    #用os模块中的rename方法对文件改名
    # os.rename(oldname,newname)
    # print(oldname,'======>',newname)

    n+=1