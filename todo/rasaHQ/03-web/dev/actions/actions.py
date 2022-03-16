import datetime
from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.dt import ass_dt
from actions.finance.tool import Tool
from actions.finance.world_index import WorldIndex, WorldIndexHistory


class SearchWorldIndex(Action):
    def name(self) -> Text:
        return "action_search_index"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        market_date = next(tracker.get_latest_entity_values("market_date"), None)

        if market_date:
            dispatcher.utter_message(text=ass_dt.get_date_by_entity(market_date))
        else:
            # DucklingEntityExtractor
            value_date = next(tracker.get_latest_entity_values("time"), None)
            dispatcher.utter_message(text=ass_dt.get_date_by_value(value_date))

        return []


class QueryWorldIndex(Action):
    """query world index"""
    def name(self) -> Text:
        return "action_query_index"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # date
        market_date_tmp = next(tracker.get_latest_entity_values("market_date"), None)
        if market_date_tmp:
            market_date = ass_dt.get_date_by_entity(market_date_tmp)
        else:
            # DucklingEntityExtractor
            duck_date = next(tracker.get_latest_entity_values("time"), None)
            market_date = ass_dt.get_date_by_value(duck_date)

        # market
        market_name = next(tracker.get_latest_entity_values("market"), None)
        # 市场处理，如果找不到市场，则直接返回提示（可以查下列市场），不用再查询接口
        market_id = Tool.convert_market_id(market_name)
        if market_id is None:
            text = "可以查看如下全球指数情况\n"
            text += Tool.get_world_index_name()
            dispatcher.utter_message(text=text)
            return []
        # 时间处理
        is_today = False
        market_strftime = None
        try:
            market_strftime = market_date.strftime("%Y%m%d")
        except Exception:
            is_today = True
        else:
            if market_strftime == datetime.date.today().strftime("%Y%m%d"):
                is_today = True
        # 如果是当天，则调用index api, 否则调用index history api
        if is_today:
            response_text = WorldIndex().fetch_index(market_id)
        else:
            response_text = WorldIndexHistory().fetch_index(market_strftime, market_id)
        dispatcher.utter_message(text=response_text)
        return []
