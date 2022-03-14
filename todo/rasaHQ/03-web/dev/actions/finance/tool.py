import os
import pandas as pd

from actions.constants import ACTIONS_PATH


class Tool:
    def __init__(self):
        # 文件路径
        self.index_path = os.path.join(ACTIONS_PATH, "world_index.txt")

    def convert_market_id(self, market_name: str) -> str:
        """convert market name to market id

        Args:
            market_name (str): market name

        Returns:
            str: market id
        """
        df = pd.read_table(self.index_path, sep="  ", header=None)
        df.columns = ["id", "name"]
        df_tmp = df[df.name.str.contains(market_name)]

        if df_tmp.empty:
            # todo 应该支持筛选 输入大于指数名称（被包含），如输入“上证指数数”，文件中的“上证指数”也应符合要求
            return None
        else:
            return str(df_tmp.id.values[0])

    def get_world_index_name(self):
        """ get world index id and name content"""
        with open(self.index_path, encoding="utf-8") as f:
            content = f.readlines()

        return "".join(content)
