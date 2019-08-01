from merge_information import *
from not_mapping_merge import *
file_path = "data_resource/"
result_path  ="result/"
df = pd.read_excel(result_path + "plus_BPA_comment.xlsx",converters={"OMIM_ID":str,"Orphat_ID":str,"UMLS":str,"ICD9_ID":str,"ICD10_ID":str,
                                                          "ICD10CM_ID":str,"ICD11_ID":str,"BPA_ID":str,"eRAM_ID":str})   # 基准
Basic_information_dict = {}
row = df.shape[0]
for i in range(0,row):
    Basic_information_dict[i] = {}
    # DOID
    if not pd.isnull(df["DOID"][i]):
        Basic_information_dict[i]["DOID"] = [d.strip() for d in str(df["DOID"][i]).lower().strip().split(";")]
    else:
        Basic_information_dict[i]["DOID"] = []

    # UMLS
    if not pd.isnull(df["UMLS"][i]):
        Basic_information_dict[i]["UMLS"] = [d.strip() for d in str(df["UMLS"][i]).lower().strip().split(";")]
    else:
        Basic_information_dict[i]["UMLS"] = []
    # Orphanet
    if not pd.isnull(df["Orphat_ID"][i]):
        Basic_information_dict[i]["Orphat_ID"] = [d.strip() for d in str(df["Orphat_ID"][i]).lower().strip().split(";")]
    else:
        Basic_information_dict[i]["Orphat_ID"] = []
    # OMIM
    if not pd.isnull(df["OMIM_ID"][i]):
        Basic_information_dict[i]["OMIM_ID"] = [d.strip() for d in str(df["OMIM_ID"][i]).lower().strip().split(";")]
    else:
        Basic_information_dict[i]["OMIM_ID"] = []
    # eRAM
    if not pd.isnull(df["eRAM_ID"][i]):
        Basic_information_dict[i]["eRAM_ID"] = [d.strip() for d in str(df["eRAM_ID"][i]).lower().strip().split(";")]
    else:
        Basic_information_dict[i]["eRAM_ID"] = []
########################################################################################################################
# files = ['MRCONSO.xlsx', 'MRDEF.xlsx', 'OMIM.xlsx', 'Orphanet.xlsx', 'eRAM.xlsx', 'ICD10.xlsx', 'ICD10CM.xlsx',
#          'ICD11.xlsx', 'ICD9.xlsx', 'Texas.xlsx''BPA.xlsx', 'BPA_comment.xlsx']
file_name = "Texas"
df[file_name + "_Name"] = None          # 增加Name列
#df[file_name + "_Synonyms"] = None      # 增加Synonyms列
#df[file_name + "_Definition"] = None    # 增加Definition列
df1 = pd.read_excel(file_path + file_name +".xlsx",converters={"OMIM_ID":str,"Orphat_ID":str,"UMLS":str,"ICD9_ID":str,"ICD10_ID":str,
                                                          "ICD10CM_ID":str,"ICD11_ID":str,"BPA_ID":str,"eRAM_ID":str})
row1 = df1.shape[0]
for j in range(0, row1):
    print(j)

    # 读取DOID
    DOID = []
    if not pd.isnull(df1["DOID"][j]):
        DOID = [d.strip() for d in str(df1["DOID"][j]).lower().strip().split(";")]

    # 读取UMLS
    UMLS = []
    if not pd.isnull(df1["UMLS"][j]):
        UMLS = [u.strip() for u in str(df1["UMLS"][j]).lower().strip().split(";")]

    # 读取Orphanet
    Orphat_ID = []
    if not pd.isnull(df1["Orphat_ID"][j]):
        Orphat_ID = [o.strip() for o in str(df1["Orphat_ID"][j]).lower().strip().split(";")]

    # 读取OMIM
    OMIM_ID = []
    if not pd.isnull(df1["OMIM_ID"][j]):
        OMIM_ID = [om.strip() for om in str(df1["OMIM_ID"][j]).lower().strip().split(";")]

    # 读取eRAM
    eRAM_ID = []
    if not pd.isnull(df1["eRAM_ID"][j]):
        eRAM_ID = [e.strip() for e in str(df1["eRAM_ID"][j]).lower().strip().split(";")]

    #print(DOID, UMLS, Orphat_ID, OMIM_ID, eRAM_ID)
    ###################################################################################################################
    # 开始匹配
    DOID_count = 0
    for key, val in Basic_information_dict.items():
        for per_DOID in  DOID:
            if per_DOID in val["DOID"]:
                DOID_count += 1
                print("DOID:",DOID_count)
                merge_inforamiton_fun(df,df1,key,val,j,file_name)
                break
        if DOID_count:
            break
    if DOID_count:
        continue
    else:
        # 用UMLS 匹配
        UMLS_count = 0
        for key,val in Basic_information_dict.items():
            for per_UMLS in UMLS:
                if per_UMLS in val["UMLS"]:
                    UMLS_count += 1
                    print("UMLS:", UMLS_count)
                    merge_inforamiton_fun(df, df1, key, val, j, file_name)
                    break
            if UMLS_count:
                break
        if UMLS_count:
            continue
        else:
            # 比较 Orphanet
            Orphat_count = 0
            for key,val in Basic_information_dict.items():
                for per_Orphat in Orphat_ID:
                    if per_Orphat in val["Orphat_ID"]:
                        Orphat_count +=1
                        print("Orphanet:", Orphat_count)
                        merge_inforamiton_fun(df, df1, key, val, j, file_name)
                        break
                if Orphat_count:
                    break
            if Orphat_count:
                continue
            else:
                # 比较OMIM
                OMIM_count = 0
                for key,val in Basic_information_dict.items():
                    for per_OMIM in OMIM_ID:
                        if per_OMIM in val["OMIM_ID"]:
                            OMIM_count += 1
                            print("OMIM:", OMIM_count)
                            merge_inforamiton_fun(df, df1, key, val, j, file_name)
                            break
                    if OMIM_count:
                        break
                if OMIM_count:
                    continue
                else:
                    eRAM_count = 0
                    for key, val in Basic_information_dict.items():
                        for per_eRAM in eRAM_ID:
                            if per_eRAM in val["eRAM_ID"]:
                                eRAM_count +=1
                                print("eRAM:",eRAM_count)
                                merge_inforamiton_fun(df, df1, key, val, j, file_name)
                                break
                        if eRAM_count:
                            break
                    if eRAM_count:
                        continue
                    else:
                        not_mapping_merge(df,df1,j,file_name)
                        continue
df.to_excel(result_path +"plus_Texas.xlsx",index = False)
