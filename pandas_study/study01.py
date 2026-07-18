import pandas as pd
import pathlib
import numpy as np

ROOT_FILE_EMPLOYEE = r"D:\CODE\first_p\datas\员工数据表.xlsx"
df_original = pd.read_excel(ROOT_FILE_EMPLOYEE)

def costomize_title(column_name):
    # 首字母变大写
    return str(column_name).title()

def review_colum():
    """
        列的操作
    """
    # columns = ["编号", "性别", "姓名", "年龄", "生日", "部门", "薪资", "爱好"]
    # reorder = df_original.reindex(columns=columns)
    

    sex_index = df_original.columns.get_loc('性别')
    birthday = df_original.pop('生日')
    
    df_original.insert(sex_index - 1, '生日', value=birthday)

    series_name = df_original[df_original["姓名"].str.contains("刚")]

    # 对薪资低于5千的加0.6倍
    salary = df_original.columns.get_loc("薪资")
    df_original["薪资"]
    df_original.insert(salary + 1, '加薪', 
                       value=np.where(df_original["薪资"] < 10000, df_original["薪资"] * 1.5, df_original["薪资"]))
    
    df_original.rename(columns=costomize_title, inplace=True)

    
    print(df_original.head(10))
    # print(series_name.sample(11))

    df_original.rename()
if __name__ == "__main__":
    review_colum()
