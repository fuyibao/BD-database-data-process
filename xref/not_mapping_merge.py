
def not_mapping_merge(df,df1,j,file_name):

    current_row = df.shape[0]
    df.loc[current_row] = None
    # 添加Name
    df["Name"][current_row]= df1[file_name+"_Name"][j]
    # 添加Synonyms
    #df["Synonyms"][current_row] = df1[file_name + "_Synonyms"][j]
    # 添加Definition
    #df["Definition"][current_row] = df1[file_name + "_Definition"][j]
    # 置空file_name对应的Name列
    df[file_name + "_Name"][current_row] = "-"
    # 置空file_name对应的Synonyms列
    #df[file_name + "_Synonyms"][current_row] = "-"
    # 置空file_name对应的Definition列
    #df[file_name + "_Definition"][current_row] = "-"
    # 添加 DOID
    df["DOID"][current_row] = df1["DOID"][j]
    # 添加 UMLS
    df["UMLS"][current_row] = df1["UMLS"][j]
    # 添加 Orphanet
    df["Orphat_ID"][current_row] = df1["Orphat_ID"][j]
    # 添加 OMIM
    df["OMIM_ID"][current_row] = df1["OMIM_ID"][j]
    # 添加 eRAM
    df["eRAM_ID"][current_row] = df1["eRAM_ID"][j]
    # 添加 ICD9
    df["ICD9_ID"][current_row] = df1["ICD9_ID"][j]
    # 添加 ICD10
    df["ICD10_ID"][current_row] = df1["ICD10_ID"][j]
    # 添加 ICD10CM
    df["ICD10CM_ID"][current_row] = df1["ICD10CM_ID"][j]
    # 添加 ICD11
    df["ICD11_ID"][current_row] = df1["ICD11_ID"][j]
    # 添加 BPA
    df["BPA_ID"][current_row] = df1["BPA_ID"][j]

