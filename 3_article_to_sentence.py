#_*_coding:utf-8 _*_
import re
import os

def text_to_sentence(input_file,output_path):
    file_string = input_file.split("/")
    out_name = file_string[-1].split(".")[0]
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        list1 = []
        p0 = re.compile("\?|\!")  # 匹配句末标点，可以增删
        p2 = re.compile("([.](?!([\d]+)))|((?<=[^\d+])[.])")   # 用于断句的regrex，可以修改
        pattern_list = {"et al.":"et al",
                        "i.e.":"i-e",
                        "vs.":"vs",
                        "e.g.":"eg",
                        "Fig.":"Fig"}                            #需要替换的模式对,可以增删
        for line in lines:
            if line.replace("\n", "").replace("\n", "").strip():
                s = re.sub(p0,'.',line)        # 将句末标点"?" 和 " !"替换成 ".",起到换行作用
                for key,value in pattern_list.items():
                    s = s.replace(key,value)
                c = re.sub(p2,".\n",s)
                sentences = c.split("\n")
                for h in sentences:
                    if h:
                        list1.append(h.replace("\n","").replace("\n", "").strip())

        with open(output_path+"%s_sentence.txt"%(out_name) ,"a",encoding = "utf-8") as f1:
            for i in list1:
                f1.write(i+"\n")

if __name__ == "__main__":
    input_file_path = "/media/_Extend2017/Fuyibao/text_mining_NCBI/NCBI/Fulltext/TXT/need_1990_2015/"
    output_path = "/media/_Extend2017/Fuyibao/text_mining_NCBI/Fulltext_sentence/"

    first_level_file_list = os.listdir(input_file_path)
    for first_level_file in first_level_file_list:   #对于每个文件夹
        print(first_level_file)
        folder_name = first_level_file + "_sentence"
        os.mkdir(output_path + folder_name)
        second_level_file_list = os.listdir(input_file_path + first_level_file + "/")
        for file in second_level_file_list:
            print(file)
            text_to_sentence(input_file_path +first_level_file +"/"+ file, output_path + folder_name+"/")
    print("done")
