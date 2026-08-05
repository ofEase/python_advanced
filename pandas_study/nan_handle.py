import pandas as pd
import numpy as np
from pathlib import Path

root_file = Path(r"D:\CODE\datas\员工数据表.xlsx")


def nan_handle_01():
    df = pd.read_excel(root_file)
    df.loc[df["部门"] == "技术部", "薪资"] = np.nan

    df.loc[df["部门"] == "运维部", "性别"] = np.nan
    # 统计查看空置
    # print(df.info())
    # 是nan
    # print(df.isna().sum())
    # 不是nan
    # print(df.notna())

    # 删除空值行(默认),
    # df = df.dropna()
    # 所有字段为空值才会被删除
    # df.dropna(how="all")
    # 当指定的字段为空值的时候删除
    # df.dropna(subset="性别")

    # 填充缺失值
    # 给空值的列填充固有值
    df = df.fillna(value={"性别": "女", "薪资": 1})
    print(df[df["部门"] == "运维部"].head(10))


if __name__ == "__main__":
    nan_handle_01()
