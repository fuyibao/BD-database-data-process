#-*- coding: utf-8 -*-
import os
file_path = "concurrence-information/"
file_path2 = "Disease_pattern_Manifestation_Sentence/"
files = os.listdir(file_path)

# pattern
X = [" and ", " with ", ", ", " (", " associated with ", " ", " or ", ", and ", "-associated ", " in "]
Y = [" and ", " in ", ", ", " associated with ", " (", " in patients with ", " in a patient with ", " due to ", " or ", " of "]

for file in files:
    print(file)
    file_name = file.split(".")[0]
    with open(file_path + file, "r",encoding = 'utf-8') as f:
        D_M_Sentence = [line.strip() for line in f.readlines()]
    print(len(D_M_Sentence))

    P =[]

    for i in D_M_Sentence:
        record = i.strip().split("|")
        print(record)
        for j in X:     # j为X中的元素，D_pattern_M
            print(j)
            if record[1].lower() + j + record[2].lower() in record[4].lower() and record[1] != record[2]:
                P.append(i)
                break

        for k in Y:    # k为Y中的元素，M_pattern_D
            print(k)
            if record[2].lower() + k + record[1].lower() in record[4].lower() and record[1] != record[2]:
                P.append(i)
                break

    print("未去重之前：",len(P))
    P_result = list(set(P))  # 去重
    print("去重之后：",len(P_result))


    with open(file_path2 + file_name + '_pattern.txt', 'a', encoding = 'utf-8') as file:
        for itr in P_result:
            file.write(itr + "\n")


    print("Done")
