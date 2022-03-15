import json
import os
import requests
import pandas as pd



class Indexes():
    def __init__(self):
        self.http_url = "http://api.k780.com"
        self.https_url = "https://sapi.k780.com"
        self.app = "finance.globalindex"
        self.sh_id = "1010"
        self.xz_id = "1011"
        self.appkey = "10003"
        self.sign = "b59bc3ef6191eb9f747dd4e83c99f2a4"
        self.format = "json"

    @staticmethod
    def read_global_index_txt() -> list:
        file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/world_index.txt")
        with open(file, encoding="utf-8") as f:
            content = f.readlines()

        return content

    def query_global_index(self):
        content = self.read_global_index_txt()
        content = "".join(content)

        return "指数编号 指数名称\n\n" + content

    def fetch_index(self):
        ...

    def query_global_index2(self, inx_id: str = None) -> str:
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
            a = json.loads( response.text)
            # print(response.json())
            """
            a_result = json.loads(nowapi_call)
            if a_result:
              if a_result['success'] != '0':
                print a_result['result'];
              else:
                print a_result['msgid']+' '+a_result['msg']
            else:
              print 'Request nowapi fail.';
            """

        except requests.ConnectionError:
            return "查询失败，请稍后再试"
        else:
            # return response.content
            return a
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


gi = Indexes()
a = gi.query_global_index2("1244")
# print(a)
# print(231)
# gi.get_index_info('')
# gi.get_index_names()


# a = os.path.dirname(__file__)
# print(a)
# aa = os.path.realpath(__file__)
# print(aa)
# {
#     success: "1.txt",
#     result: {
#         totline: "1.txt",
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
#                 amplitude_price_per: "1.txt.27%", /*振幅amp*/
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

class FinanceStock():
    def __init__(self):
        self.http_url = "http://api.k780.com"
        self.https_url = "https://sapi.k780.com"
        self.app = "finance.stock_realtime"
        self.stosym = None
        self.appkey = "10003"
        self.sign = "b59bc3ef6191eb9f747dd4e83c99f2a4"
        self.format = "json"


    def query_global_index2(self, inx_id: str = None) -> str:
        """[summary]
        Args:
            inx_id (str, optional): [description]. Defaults to None.
        Returns:
            str: [description]
        """
        params = {
            "app": self.app,
            "stoSym": inx_id,
            "appkey": self.appkey,
            "sign": self.sign,
            "format": self.format
        }
        try:
            response = requests.get(self.http_url, params=params, timeout=2)
            a = json.loads( response.text)
            # print(response.json())
            """
            a_result = json.loads(nowapi_call)
            if a_result:
              if a_result['success'] != '0':
                print a_result['result'];
              else:
                print a_result['msgid']+' '+a_result['msg']
            else:
              print 'Request nowapi fail.';
            """

        except requests.ConnectionError:
            return "查询失败，请稍后再试"
        else:
            # return response.content
            return a
        return None  # response.json()


gi = FinanceStock()
a = gi.query_global_index2("sh513050")
# print(a)


class FinanceStockHis():
    def __init__(self):
        self.http_url = "http://api.k780.com"
        self.https_url = "https://sapi.k780.com"
        self.app = "finance.stock_history"
        self.stosym = None
        self.ht_type = "HT1D"
        self.date_ymd = "20211101"
        self.appkey = "10003"
        self.sign = "b59bc3ef6191eb9f747dd4e83c99f2a4"
        self.format = "json"


    def query_global_index2(self, inx_id: str = None) -> str:
        """[summary]
        Args:
            inx_id (str, optional): [description]. Defaults to None.
        Returns:
            str: [description]
        """
        params = {
            "app": self.app,
            "stoSym": inx_id,
            "htType": self.ht_type,
            "dateYmd": self.date_ymd,
            "appkey": self.appkey,
            "sign": self.sign,
            "format": self.format
        }
        try:
            response = requests.get(self.http_url, params=params, timeout=2)
            a = json.loads( response.text)
            # print(response.json())
            """
            a_result = json.loads(nowapi_call)
            if a_result:
              if a_result['success'] != '0':
                print a_result['result'];
              else:
                print a_result['msgid']+' '+a_result['msg']
            else:
              print 'Request nowapi fail.';
            """

        except requests.ConnectionError:
            return "查询失败，请稍后再试"
        else:
            # return response.content
            return a
        return None  # response.json()
gi2 = FinanceStockHis()
a = gi2.query_global_index2("sh513050")
# print(a)

if __name__ == "__main__":
    file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/world_index.txt")
    # df = pd.read_csv(file, sep=" ", header=None)
    # df.columns = ["编号", "名称"]
    # df = df.set_index("编号")
    # pd.set_option('display.unicode.ambiguous_as_wide', True)
    # pd.set_option('display.unicode.east_asian_width', True)
    # df = df.sort_values(by="编号", ascending=True)
    # a = df.to_string(justify= 'left')
    # df.style.set_properties(**{'text-align': 'left'})
    # print(a)
    pd.set_option("display.colheader_justify", "left")
    # dfStyler = df.style.set_properties(**{'text-align': 'left'})
    # dfStyler.set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
    # print(df)

    # print(df)
    # file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/world_index.txt")
    # with open(file, encoding="utf-8") as f:
    #     content = f.readlines()
    #
    # print()


"""
1. 沪深股市
{
    success: "1",
    result: {
        totline: "1",
        disline: "1",
        page: "1",
        lists: {
            sh600000: {
                stoid: "1", /*自定义编号*/
                symbol: "sh600000", /*股票代号*/
                scode: "600000", /*股票编号*/
                sname: "浦发银行", /*股票名称*/
                sname_eng: "", /*股票名称英文*/
                open_price: "16.390", /*开盘价*/
                yesy_price: "16.400", /*昨收价*/
                last_price: "16.430", /*当前价*/
                high_price: "16.450", /*最高价*/
                low_price: "16.380", /*最低价*/
                rise_fall: "0.030", /*涨跌额*/
                rise_fall_per: "0.18", /*涨跌幅*/
                volume: "21269924", /*成交量*/
                turn_volume: "349039232.000", /*成交量额*/
                buy1_n: "6300", /*买1*/
                buy1_m: "16.420", /*买1报价*/
                buy2_n: "6980", /*买2*/
                buy2_m: "16.410", /*买2报价*/
                buy3_n: "343800", /*买3*/
                buy3_m: "16.400", /*买3报价*/
                buy4_n: "473321", /*买4*/
                buy4_m: "16.390", /*买4报价*/
                buy5_n: "292400", /*买5*/
                buy5_m: "16.380", /*买5报价*/
                sell1_n: "254", /*卖1*/
                sell1_m: "16.430", /*卖1报价*/
                sell2_n: "223459", /*卖2*/
                sell2_m: "16.440", /*卖2报价*/
                sell3_n: "368981", /*卖3*/
                sell3_m: "16.450", /*卖3报价*/
                sell4_n: "226339", /*卖4*/
                sell4_m: "16.460", /*卖4报价*/
                sell5_n: "237610", /*卖5*/
                sell5_m: "16.470", /*卖5报价*/
                uptime: "2016-11-07 14:58:50" /*更新时间*/
            }
        }
    }
}

备注： 涨停价/跌停价计算方式，涨停=昨日收盘价+(昨日收盘价*0.1)   跌停=昨日收盘价-(昨日收盘价*0.1)

------------------------------------------------------------------

2.香港股市
{
    success: "1",
    result: {
        totline: "1",
        disline: "1",
        page: "1",
        lists: {
            hk00001: {
                stoid: "2906", /*自定义编号*/
                symbol: "hk00001", /*股票代码*/
                scode: "00001",  /*股票代号*/
                sname: "长和", /*股票名称*/
                sname_eng: "CHEUNG KONG", /*股票名称英文*/
                open_price: "95.250", /*开盘价*/
                yesy_price: "95.500", /*昨收价*/
                last_price: "96.000", /*当前价*/
                high_price: "96.250", /*最高价*/
                low_price: "94.800", /*最低价*/
                rise_fall: "0.500", /*涨跌额*/
                rise_fall_per: "0.52", /*涨跌幅*/
                volume: "2341664", /*成交量*/
                turn_volume: "224225024.000", /*成交额*/
                peratio: "11.713", /*市盈率*/
                week52_high: "105.400", /*52周最高*/
                week52_low: "80.600", /*52周最低*/
                uptime: "2016-11-07 15:36:00" /*更新时间*/
            }
        }
    }
}

------------------------------------------------------------------

3.美国股市
{
    success: "1",
    result: {
        totline: "1",
        disline: "1",
        page: "1",
        lists: {
            gb_aapl: {
                stoid: "4803",/*自定义编号*/
                symbol: "gb_aapl", /*股票代码*/
                scode: "AAPL", /*股票代号*/
                sname: "苹果公司", /*股票名称*/
                sname_eng: "Apple Inc.", /*股票名称英文*/
                open_price: "108.530", /*开盘价*/
                yesy_price: "109.830", /*昨收价*/
                last_price: "108.840", /*当前价*/
                high_price: "110.250", /*最高价*/
                low_price: "108.110", /*最低价*/
                rise_fall: "-0.990", /*涨跌额*/
                rise_fall_per: "-0.90", /*涨跌幅*/
                volume: "29939342", /*成交量*/
                turn_volume: "0.000", /*成交额 美股暂无法提供提交额*/
                peratio: "13.100", /*市盈率*/
                week52_high: "121.810", /*52周最高*/
                week52_low: "89.470", /*52周最低*/
                day10_volume: "34542335", /*10日均量*/
                mvalue: "2147483647", /*市值*/
                ep_share: "8.310", /*每股收益*/
                beta_coefficient: "13.100", /*贝塔系数*/
                dividend: "2.180", /*股息*/
                yield: "1.100", /*收益率*/
                equity: "2147483647", /*股本*/
                db_price: "108.950", /*盘后价*/
                db_volume: "779446", /*盘后成交量*/
                uptime: "2016-11-05 04:57:56" /*更新时间*/
            }
        }
    }
}

------------------------------------------------------------------

4. 错误
{
    "success":"0",
    "msgid":"...",
    "msg":"..."
}
"""

# class FinanceStockList():
#     def __init__(self):
#         self.http_url = "http://api.k780.com"
#         self.https_url = "https://sapi.k780.com"
#         self.app = "finance.stock_list"
#         self.category = "hs"
#         self.appkey = "10003"
#         self.sign = "b59bc3ef6191eb9f747dd4e83c99f2a4"
#         self.format = "json"
#
#
#     def query_global_index2(self, inx_id: str = None) -> str:
#         """[summary]
#         Args:
#             inx_id (str, optional): [description]. Defaults to None.
#         Returns:
#             str: [description]
#         """
#         params = {
#             "app": self.app,
#             # "stoSym": inx_id,
#             "category": inx_id,
#             "appkey": self.appkey,
#             "sign": self.sign,
#             "format": self.format
#         }
#         try:
#             response = requests.get(self.http_url, params=params, timeout=2)
#             a = json.loads( response.text)
#             # print(response.json())
#             """
#             a_result = json.loads(nowapi_call)
#             if a_result:
#               if a_result['success'] != '0':
#                 print a_result['result'];
#               else:
#                 print a_result['msgid']+' '+a_result['msg']
#             else:
#               print 'Request nowapi fail.';
#             """
#
#         except requests.ConnectionError:
#             return "查询失败，请稍后再试"
#         else:
#             # return response.content
#             return a
#         return None  # response.json()
# gi2 = FinanceStockList()
# lst = ["hs","hk","us"]
# d = {}
# ids = []
# names = []
# sids = []
# for l in lst:
#     a = gi2.query_global_index2(l)
#     b = a["result"]["lists"]
#
#     for b1 in b:
#         sym = b1["symbol"]
#         sname = b1["sname"]
#         if l == "us":
#             ids.append(sym)
#             names.append(sname)
#             sids.append(sym)
#         else:
#             ids.append(sym[2:])
#             names.append(sname)
#             sids.append(sym)
#
# d["id"] = ids
# d["name"] = names
# d["sid"] = sids
# df = pd.DataFrame(d)
# # df.to_csv("stock.csv", index=False)



if __name__ == "__main__":
    ...
