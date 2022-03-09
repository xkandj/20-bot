import pandas as pd
df = pd.read_table("global_index.txt", header=None, sep=" ")
df.columns = ["id", "name"]
print(df.head())
df.to_csv("global_index.csv", index=None)
exit()
# import os
# 
# from pandas import DataFrame
# 
# 
# file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/1.txt")
# with open(file, encoding="utf-8") as f:
#     s = """
#     <table>
#     <tr>
#     <th>左对齐</th>
#     <th>右对齐</th>
#   </tr>
#     """
#     for l in f.readlines():
#         a = l[:4]
#         b = l[4:]
# 
#         s +=f"""
#         <tr>
#         <td align="left">{a}</td>
#         <td align="left">{b.strip()}</td>
#         </tr>
#         """
#     s+="""
# </table>
#     """
# 
# print(s)
# 
#
import json
import os

import pandas as pd
import requests

def query_global_index2() -> str:
    """[summary]
    Args:
        inx_id (str, optional): [description]. Defaults to None.
    Returns:
        str: [description]
    """
    http_url = "http://api.k780.com"

    app = "finance.globalindex"
    sh_id = "1010"
    xz_id = "1011"
    inxnos = 1010, 1011
    appkey = "10003"
    sign = "b59bc3ef6191eb9f747dd4e83c99f2a4"
    format = "json"
    
    params = {
        "app":   app,
        "inxids": "1010",
        "appkey":   appkey,
        "sign":   sign,
        "format":   format
    }
    ret = "指数查询结果如下\n"
    try:
        response = requests.get(  http_url, params=params, timeout=2)
        result = json.loads(response.text)
        if result:
            if result.get("success") != "0":
                lst = result.get("result").get("lists")
                if lst is not None:
                    for k, v in lst.items():
                        print(k)
                        ret += f"版块：{v.get('typeid')}\n"
                        ret += f"指数名称：{v.get('inxnm')}\n"
                        ret += f"昨日收盘价：{v.get('yesy_price')}\n"
                        ret += f"今日开盘价：{v.get('open_price')}\n"
                        ret += f"当前价：{v.get('last_price')}\n"
                        ret += f"涨跌额：{v.get('rise_fall')}\n"
                        ret += f"涨跌幅：{v.get('rise_fall_per')}\n"
                        ret += f"最高价：{v.get('high_price')}\n"
                        ret += f"最低：{v.get('low_price')}\n"
                        ret += f"成交量：{v.get('volume')}(部分股指为0，以实际数据为准)\n"
                        ret += f"成交额：{v.get('turnover')}(部分股指为0，以实际数据为准)\n"
                        ret += f"数据更新时间：{v.get('uptime')}\n"
            else:
                error_msg = result.get("msg")
                ret += error_msg
        else:
            # log
            ret += "查询失败"
        print(ret)

    except requests.ConnectionError:
        return "查询失败，请稍后再试"
    else:
        ...
    return ret


# query_global_index2()
# exit()
a = "123q"
print(a.isdigit())
exit()
name = "指数"
file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/global_index.txt")
df = pd.read_table(file, header=None, sep="  ")
# print(df)
df.columns = ["id","name"]
id_df = df[df.name.str.contains(name)]
print(id_df.id)
a  = df.name.filter(like="台湾加权")
print(a)


df2 = df[df.name.isin(["台湾加权a"])]
# df2 = df["指数".str.contains(df.name)]
print(df2)
