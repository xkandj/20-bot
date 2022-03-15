import json

from actions.api.nowapi import NowApi


class WorldIndex:
    def __init__(self):
        # api定义
        self.api = NowApi()
        self.api_params = self.api.params
        self.api_params["app"] = "finance.globalindex"

    def fetch_index(self, id: str) -> str:
        """根据输入或者槽值查询指数信息"""
        return self.get_content(id)

    def get_content(self, ids: str) -> str:
        """根据指数id查询指数信息，调用api接口

        Args:
            ids (str): 指数id，接口支持接收类型int和str, 统一为str

        Returns:
            str: 查询结果，映射为中文格式
        """
        self.api_params["inxids"] = ids
        data = json.loads(self.api.get_data(self.api_params))
        success = data.get("success")
        text = data.get("text")

        if success is None or success == 0:
            ret = text
        else:
            ret = ""
            lst = text.get("result").get("lists")
            if lst is not None:
                for _, v in lst.items():
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
        return ret


class WorldIndexHistory:
    def __init__(self):
        # api定义
        self.api = NowApi()
        self.api_params = self.api.params
        self.api_params["app"] = "finance.globalindex_history"
        # HT1D: 历史1天级别, HT1M 历史1分钟级别
        self.api_params["htType"] = "HT1D"

    def fetch_index(self, ymd: str, id: str) -> str:
        """根据输入或者槽值查询指数信息

        Args:
            ymd (str): 时间yyyymmdd
            id (str): market id

        Returns:
            str: 查询结果
        """
        return  self.get_content(ymd, id)

    def get_content(self, ymd: str, id: str) -> str:
        """
        根据指数id查询指数信息，调用api接口
        查询结果，映射为中文格式
        """
        self.api_params["inxId"] = id
        self.api_params["dateYmd"] = ymd
        data = json.loads(self.api.get_data(self.api_params))
        success = data.get("success")
        text = data.get("text")

        if success is None or success == 0:
            ret = text
        else:
            ret = ""
            dt = text.get("result").get("dtAppend")
            if dt is not None:
                ret += f"指数编号是{dt.get('inxId')}，名称是{dt.get('inxNm')}"

            lst = text.get("result").get("dtList")
            if lst is not None:
                for _, v in lst.items():
                    ret += f"数据日期：{v.get('dateYmd')}\n"
                    ret += f"今日开盘价：{v.get('openPrice')}\n"
                    ret += f"今日收盘价：{v.get('closePrice')}\n"
                    ret += f"指数名称：{v.get('inxnm')}\n"
                    ret += f"昨日收盘价：{v.get('yesy_price')}\n"
                    ret += f"当前价：{v.get('last_price')}\n"
                    ret += f"涨跌额：{v.get('rise_fall')}\n"
                    ret += f"涨跌幅：{v.get('rise_fall_per')}\n"
                    ret += f"最高价：{v.get('high_price')}\n"
                    ret += f"最低：{v.get('low_price')}\n"
                    ret += f"成交量：{v.get('volume')}(部分股指为0，以实际数据为准)\n"
                    ret += f"成交额：{v.get('turnover')}(部分股指为0，以实际数据为准)\n"
                    ret += f"数据更新时间：{v.get('uptime')}\n"
        return ret

"""
dateYmd: "20201230",/*数据日期*/
            openPrice: "3375.01",/*今日开盘价*/
            closePrice: "3414.45",/*今日收盘价*/
            yesyPrice: "3379.04",/*昨日收盘价*/
            highPrice: "3414.45",/*今日最高价*/
            lowPrice: "3374.42",/*今日最低价*/
            changePrice: "35.41",/*涨跌额*/
            changeMargin: "1.05",/*涨跌幅%*/
            volume: "291023544",/*成交量*/
            turnover: "377542352896"/*成交额 美股港股指无成交额*/
"""

if __name__ == "__main__":
    wih = WorldIndexHistory()
    wih.fetch_index("20220310", "1010")