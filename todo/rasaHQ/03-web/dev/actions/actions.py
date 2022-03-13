from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.dt import ass_dt


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
    def name(self) -> Text:
        return "action_query_index"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        market_date = next(tracker.get_latest_entity_values("market_date"), None)

        if market_date:
            date = ass_dt.get_date_by_entity(market_date)
        else:
            # DucklingEntityExtractor
            duck_date = next(tracker.get_latest_entity_values("time"), None)
            date = ass_dt.get_date_by_value(duck_date)

        # market
        market = next(tracker.get_latest_entity_values("market"), None)
        print(market)


        # 不正常逻辑处理
        # 不正常的逻辑有，1. 没时间（如果获取不到日期怎么办？）， 2. 没市场， 3. 都没，
        # 4. 没有结果的话启动utter，其他信息， 5. 有结果是否启动utter, 应该不启动

        # 正常逻辑处理
        # 调用api，获取结果
        response_text = WorldIndex().fetch_index()

        dispatcher.utter_message(text=market)

        return []
