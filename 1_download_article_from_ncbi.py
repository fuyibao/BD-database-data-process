#-*- coding: UTF-8 -*-
from Bio import Entrez
from math import ceil
import sys,os
path="./NCBI/Fulltext2018/"
if not os.path.exists(path):
    os.mkdir(path)
Entrez.email = "jiajmeurida@163.com"
handle = Entrez.esearch(db="pmc",retmax=100,retstart=0,term = "2018[pdat]")  #日期可以修改
records = Entrez.read(handle)
number = records["Count"]
#b=records["IdList"]    #获取具体的UID
number = int(number)
number_circle = int(ceil(number/100))       #循环次数
retmax_circle = 100
retstart_circle = 0
print("total number:")
print(number)
i= 0  #文件名的序号
fileList_xml = [path+'2018_fulltext_'+str(x) + '.xml' for x in range(1,number_circle+2) ]       #创建文件的名字xml
while (retstart_circle < number):
    handle = Entrez.esearch(db = "pmc",retmax = 100,retstart = retstart_circle,term = "2018[pdat]")
    records = Entrez.read(handle)
    handle.close()
    b = records["IdList"]     #获取具体的UID
    handle = Entrez.efetch("pmc",id = b,rettype = 'medline',retmode = "xml")       #下载UID为b的文章
    records = handle.read()    #把handle句柄读入records中
    with open (fileList_xml[i],"a") as f:
        f.write(records)
    handle.close()
    i += 1
    print('txt:',i)
    retstart_circle += 100 #迭代
print("done")
