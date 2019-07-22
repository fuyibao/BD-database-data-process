# -*- coding:utf-8 -*-
import  re
import os

def filter_out_special_characters(inputfile,outputpath):
    name_list = inputfile.split("_")
    id = "PMC_" + name_list[-3]
    if(name_list[-1] == 'utf8.txt'):
        print(file)
        with open(inputfile, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            with open(outputpath + "PMC_"+ name_list[-3]+"_metamap.txt", "a", encoding="utf-8") as f1:
                i = 1
                for line in lines:
                    s1 = re.sub(r'[^\x00-\x7f]', ' ', line)  # 去掉non_ASCII码
                    s1.replace("\n"," ").replace("\n"," ").strip()
                    f1.write(id+"_"+str(i)+"|"+s1 + "\n")
                    i+=1

if __name__ == "__main__":
    xml_file_path = "/media/EXTend2018/Fuyibao2018/Process_NCBI_article/2018Fulltext_sentence/"
    output_path = "/media/EXTend2018/Fuyibao2018/Process_NCBI_article/Final_2018Fulltext/"
    file_list = os.listdir(xml_file_path)
    for file in file_list:
        filter_out_special_characters(xml_file_path + file, output_path)
    print("done")
