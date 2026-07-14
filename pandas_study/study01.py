import pandas as pd
import pathlib

ROOT_FILE_EMPLOYEE = r"D:\CODE\first_p\datas\员工数据表.xlsx"
df_original = pd.read_excel(ROOT_FILE_EMPLOYEE)


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
    
    print(series_name.sample(11))

if __name__ == "__main__":
    review_colum()
