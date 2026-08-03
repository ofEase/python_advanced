import pandas as pd
import numpy as np
from pathlib import Path

root_file = Path(r"D:\CODE\datas\员工数据表.xlsx")

def nan_handle_01():
    df = pd.read_excel(root_file)
    df.loc[df["部门"] == "技术部","薪资"] = np.nan

    df.loc[df["部门"]=="运营部", "性别"] = np.nan
    # print(df.info())
    print(df.isna().sum())
    print(df.no)



if __name__ == "__main__":
    nan_handle_01()
