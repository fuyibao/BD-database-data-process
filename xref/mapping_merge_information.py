import pandas as pd

def merge_inforamiton_fun(df,df1,key,val,j,file_name):
    """
    :param df:  基准
    :param df1: 待比较
    :param key: 基准的键，代表哪一行
    :param val: 基准的值，存储各种ID
    :param j:   待比较文件每一行
    :param file_name: 文件名称
    :return:
    """
    # 更新DOID
    if val["DOID"]:  # 基准的DOID不为空
        if not pd.isnull(df1["DOID"][j]):  # 待比较的DOID不为空
            df1_DOID = [d.strip() for d in str(df1["DOID"][j]).lower().strip().split(";")]
            df["DOID"][key] = ";".join(list(set(val["DOID"] + df1_DOID)))
    else:
        if not pd.isnull(df1["DOID"][j]):  # 待比较的DOID不为空
            df["DOID"][key] = df1["DOID"][j]

    # 更新UMLS
    if val["UMLS"]:
        if not pd.isnull(df1["UMLS"][j]):
            df1_UMLS = [u.strip() for u in str(df1["UMLS"][j]).lower().strip().split(";")]
            df["UMLS"][key] = ";".join(list(val["UMLS"]+df1_UMLS))
    else:
        if not pd.isnull(df1["UMLS"][j]):
            df["UMLS"][key] = df1["UMLS"][j]

    # 更新Orphanet
    if val["Orphat_ID"]:
        if not pd.isnull(df1["Orphat_ID"][j]):
            df1_orphat_ID = [o.strip() for o in str(df1["Orphat_ID"][j]).lower().strip().split(";")]
            df["Orphat_ID"][key] = ";".join(list(set(val["Orphat_ID"] + df1_orphat_ID)))
    else:
        if not pd.isnull(df1["Orphat_ID"][j]):
            df["Orphat_ID"][key] = df1["Orphat_ID"][j]

    # 更新OMIM
    if val["OMIM_ID"]:
        if not pd.isnull(df1["OMIM_ID"][j]):
            df1_OMIM_ID = [o.strip() for o in str(df1["OMIM_ID"][j]).lower().strip().split(";")]
            df["OMIM_ID"][key] = ";".join(list(set(val["OMIM_ID"] + df1_OMIM_ID)))
    else:
        if not pd.isnull(df1["OMIM_ID"][j]):
            df["OMIM_ID"][key] = df1["OMIM_ID"][j]

    # 更新eRAM
    if val["eRAM_ID"]:
        if not pd.isnull(df1["eRAM_ID"][j]):
            df1_eRAM_ID = [o.strip() for o in str(df1["eRAM_ID"][j]).lower().strip().split(";")]
            df["eRAM_ID"][key] = ";".join(list(set(val["eRAM_ID"] + df1_eRAM_ID)))
    else:
        if not pd.isnull(df1["eRAM_ID"][j]):
            df["eRAM_ID"][key] = df1["eRAM_ID"][j]

    # 更新ICD9
    if not pd.isnull(df["ICD9_ID"][key]):
        df_ICD9_ID = [i_9.strip() for i_9 in str(df["ICD9_ID"][key]).lower().strip().split(";")]
        if not pd.isnull(df1["ICD9_ID"][j]):
            df1_ICD9_ID = [i_9_1.strip() for i_9_1 in str(df1["ICD9_ID"][j]).lower().strip().split(";")]
            df["ICD9_ID"][key] = ";".join(list(set(df_ICD9_ID + df1_ICD9_ID)))
    else:
        df["ICD9_ID"][key] = df1["ICD9_ID"][j]

    # 更新ICD10
    if not pd.isnull(df["ICD10_ID"][key]):
        df_ICD10_ID = [i_10.strip() for i_10 in str(df["ICD10_ID"][key]).lower().strip().split(";")]
        if not pd.isnull(df1["ICD10_ID"][j]):
            df1_ICD10_ID = [i_10_1.strip() for i_10_1 in str(df1["ICD10_ID"][j]).lower().strip().split(";")]
            df["ICD10_ID"][key] = ";".join(list(set(df_ICD10_ID + df1_ICD10_ID)))
    else:
        df["ICD10_ID"][key] = df1["ICD10_ID"][j]

    # 更新ICD10CM
    if not pd.isnull(df["ICD10CM_ID"][key]):
        df_ICD10CM_ID = [i_10.strip() for i_10 in str(df["ICD10CM_ID"][key]).lower().strip().split(";")]
        if not pd.isnull(df1["ICD10CM_ID"][j]):
            df1_ICD10CM_ID = [i_10_1.strip() for i_10_1 in str(df1["ICD10CM_ID"][j]).lower().strip().split(";")]
            df["ICD10CM_ID"][key] = ";".join(list(set(df_ICD10CM_ID + df1_ICD10CM_ID)))
    else:
        df["ICD10CM_ID"][key] = df1["ICD10CM_ID"][j]

    # 更新ICD11
    if not pd.isnull(df["ICD11_ID"][key]):
        df_ICD11_ID = [i_10.strip() for i_10 in str(df["ICD11_ID"][key]).lower().strip().split(";")]
        if not pd.isnull(df1["ICD11_ID"][j]):
            df1_ICD11_ID = [i_10_1.strip() for i_10_1 in str(df1["ICD11_ID"][j]).lower().strip().split(";")]
            df["ICD11_ID"][key] = ";".join(list(set(df_ICD11_ID + df1_ICD11_ID)))
    else:
        df["ICD11_ID"][key] = df1["ICD11_ID"][j]

    # 更新BPA
    if not pd.isnull(df["BPA_ID"][key]):
        df_BPA_ID = [i_10.strip() for i_10 in str(df["BPA_ID"][key]).lower().strip().split(";")]
        if not pd.isnull(df1["BPA_ID"][j]):
            df1_BPA_ID = [i_10_1.strip() for i_10_1 in str(df1["BPA_ID"][j]).lower().strip().split(";")]
            df["BPA_ID"][key] = ";".join(list(set(df_BPA_ID + df1_BPA_ID)))
    else:
        df["BPA_ID"][key] = df1["BPA_ID"][j]

    # 添加Name
    df[file_name+"_Name"][key] = df1[file_name+"_Name"][j]
    # 添加Synonyms
    #df[file_name+"_Synonyms"][key] = df1[file_name+"_Synonyms"][j]
    # 添加Definition
    #df[file_name + "_Definition"][key] = df1[file_name + "_Definition"][j]
