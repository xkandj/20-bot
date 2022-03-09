import json
import os
from typing import Any

import pandas as pd
from actions.api.nowapi import NowApi
from actions.constants import ACTIONS_PATH
from actions.utils.create_log import logger


class Stock:
    def __init__(self):
        # api定义
        self.api = NowApi()
        self.api_params = self.api.params
        self.api_params["app"] = "finance.stock_realtime"


    def get_da(self):
        stosym

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

class StockHistory:
    def __init__(self):
        # api定义
        self.api = NowApi()
        self.api_params = self.api.params
        self.api_params["app"] = "finance.stock_history"


    def get_da(self):
        stosym

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
