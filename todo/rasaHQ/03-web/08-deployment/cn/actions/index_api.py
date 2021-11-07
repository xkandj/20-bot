# datetime： 2021/10/17 20:33
# author： xiazhou
# email： xiazhou@fudata.cn
# file： index_api.py
# ide： PyCharm
import json
import os
import requests
import pandas as pd

# from actions.constants import DEFAULT_TIMEOUT


class GlobalIndex():
    def __init__(self):
        self.http_url = "http://api.k780.com"
        self.https_url = "https://sapi.k780.com"
        self.app = "finance.globalindex"
        self.sh_id = "1010"
        self.xz_id = "1011"
        self.inxnos = 1010, 1011
        self.appkey = "10003"
        self.sign = "b59bc3ef6191eb9f747dd4e83c99f2a4"
        self.format = "json"

    @staticmethod
    def read_index_txt() -> pd.DataFrame:
        """[summary]

        Returns:
            pd.DataFrame: [description]
        """
        file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "actions/global_index.txt")
        df = pd.read_csv(file, sep=" ", header=None)
        df.columns = ["id", "name"]

        return df

    def fetch_global_index(self, inx_id: str = None) -> str:
        """[summary]

        Args:
            inx_id (str, optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        params = {
            "app": self.app,
            "inxids": inx_id,
            # "inxnos": self.inxnos,
            "appkey": self.appkey,
            "sign": self.sign,
            "format": self.format
        }
        try:
            response = requests.get(self.http_url, params=params, timeout=2)
            # print(response.json())
        except requests.ConnectionError:
            return "查询失败，请稍后再试"
        else:
            # return response.content
            return response
        return None  # response.json()

    def get_index(self, inx_id: str) -> str:
        """[summary]

        Args:
            inx_id (str): [description]

        Returns:
            str: [description]
        """
        result = self.fetch_global_index(inx_id)
        # re = str(result, "utf-8")
        # return (json.loads(re))["result"]
        # return result

        return result.text

    def get_index_info(self, index_name: str) -> str:
        """
        获取具体指数信息

        Args:
            index_name (str): 指数名称

        Returns:
            str: 指数信息字符串
        """
        result = 1
        index_df = self.read_index_txt()
        print(index_df)
        id_df = index_df[index_df.name.astype(str).str.contains(index_name)]
        print(id_df.id.values)
        #
        #
        # print("美元" in index_df.name.values)

    def get_indexs(self):
        df = self.read_index_txt()
        names = sorted(df.name.values, reverse=True)
        return '\n'.join(names)

# gi = GlobalIndex()
# a = gi.fetch_global_index()
# print(a)
# gi.get_index_info('')
# gi.get_index_names()


# a = os.path.dirname(__file__)
# print(a)
# aa = os.path.realpath(__file__)
# print(aa)
# {
#     success: "1",
#     result: {
#         totline: "1",
#         inxid_s: "1010",
#         lists: {
#             1010: {
#                 inxid: "1010", /*编号*/
#                 typeid: "asia", /*版块*/
#                 inxno: "000001", /*指数编号*/
#                 inxnm: "上证指数", /*指数名称*/
#                 yesy_price: "2602.78", /*昨日收盘价*/
#                 open_price: "2617.03", /*今日开盘价*/
#                 last_price: "2606.24",/*当前价*/
#                 rise_fall: "3.46", /*涨跌额*/
#                 rise_fall_per: "0.13%", /*涨跌幅*/
#                 high_price: "2636.80",/*最高价*/
#                 low_price: "2603.65",/*最低*/
#                 amplitude_price_per: "1.27%", /*振幅amp*/
#                 volume: "361059804", /*成交量 (部分股指为0，以实际数据为准)*/
#                 turnover: "484990205754",/*成交额 (部分股指为0，以实际数据为准)*/
#                 uptime: "2018-11-01 15:35:30" /*数据更新时间*/
#             }
#         }
#     }
# }
# ........
#
# 2.系统错误
# {
#     "success":"0",
#     "msgid":"...",
#     "msg":"..."
# }
