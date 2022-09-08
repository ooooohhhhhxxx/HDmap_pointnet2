import os
import pandas as pd

path = 'D:/pointnet/all/Area_1/part_1/Annotations/'
files = os.listdir(path)
txts = []
for file in files:  #遍历⽂件夹
    position = path+file  #构造绝对路径，"\\"，其中⼀个'\'为转义符
    txts.append(position)
    df = pd.read_csv(position,header= None, sep= ' ',dtype=float)
    try:
        a = df[7]
        df = df.drop(df.columns[6,7],axis=1)
        print(file)
    except:
        df = df.drop(df.columns[6],axis=1)
    #df = df.drop(df.columns[6])
    df.to_csv('D:/pointnet/data/s3dis/Stanford3dDataset_v1.2_Aligned_Version/Area_1/part_1/Annotations/%s'%file,sep = ' ',header=0,index=0)
    print(file,' saved')