# -*- coding:utf-8 -*-
"""
Caution: 本程序的基因只有一个单词，对于两个单词的基因不适合
"""
import os
path1 = "/media/EXTend2018/Fuyibao2018/BD_conoccurrence_sentence/material/"
output_path = "/media/EXTend2018/Fuyibao2018/BD_conoccurrence_sentence/2016/disease_gene/"

import string

with open(path1+"BD_name/"+"bd_longer_part_1.txt","r",encoding="utf-8") as file1:
    # D 为所有出生缺陷疾病的列表
    Diseases = [line.strip().lower().split("\t") for line in file1.readlines()]

with open(path1 + "human_coding_gene.txt","r",encoding="utf-8") as file2:
    # M 为所有症状名称的列表
    Genes = [line.strip().lower() for line in file2.readlines()]

def removePunctuation_string(text):
    for c in text:
        if c in string.punctuation:
            text = text.replace(c, " ")
    temp = text.split()
    output = " ".join(temp)
    return output        # 输出字符串

def removePunctuation_list(text):
    for c in text:
        if c in string.punctuation:
            text = text.replace(c, " ")
    temp = text.split()
    return temp   # 输出列表

def ifInText(item, D, G):
    """
    :param       item: 某篇文章中的内容
    :param       D:  包含各个疾病名称的列表
    :param       Drugs: 包含各个药物名称的列表
    :return:     判断文章中是否包含疾病列表和表型列表里的疾病和表型,返回出现的疾病和表型,
                 加快程序执行效率。
    """
    appear_diseases =[]   # 包含列表的列表，[ [number,disease1],[number,disease2],....]
    appear_genes = []     # 列表 ，[manifestation1, manifestarion2 ,....]  ,可能重复包含同一个表型
    status = False
    list_item = removePunctuation_list(item)   # 文章中的所有单词的列表（去掉标点）
    for per_disease in D:
        if per_disease[1] in item:
            appear_diseases.append(per_disease)
            for per_g in G:
                if per_g in list_item:
                    appear_genes.append(per_g)
    if(len(appear_diseases)!=0 and len(appear_genes)!=0):
        status = True
    return status, appear_diseases , list(set(appear_genes))



file_path = "/media/EXTend2018/Fuyibao2018/Process_NCBI_article/2016_sentence_after_utf8/"   # 包含所有文章句子的路径
files = os.listdir(file_path)

with open( output_path + "D1_G_ID_Sentence_2016.txt","a",encoding="utf-8") as output:
    for file in files:
        print(file)
        fnameID = file.split(".txt")[0].split("_")[1]
        fname = "PMC_" + fnameID
        with open(file_path + file, encoding="utf-8") as f:
            item = f.read().lower()  # 把文章转换成小写字母
            status, appear_D, appear_G = ifInText(item, Diseases, Genes)
            if status:
                f.seek(0)
                lines = f.readlines()
                for line in lines:  # 对于文章中的每一句话
                    line_lower = line.strip().lower()  # 转换成小写
                    list_line_lower  = removePunctuation_list(line_lower)
                    for disease in appear_D:  # 判断D - M 是否在这句话中共现
                        if disease[1] in line_lower:
                            for gene in appear_G:
                                if gene in list_line_lower:
                                    print(line_lower)
                                    output.write(disease[0] +"|" + disease[1] +'|' + gene + '|' + fname + '|' + line.strip() + '\n')

print("done")
