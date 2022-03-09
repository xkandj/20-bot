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
            print(1)
            dispatcher.utter_message(text=ass_dt.get_date_by_entity(market_date))
        else:
            # DucklingEntityExtractor
            print(2)
            value_date = next(tracker.get_latest_entity_values("time"), None)
            dispatcher.utter_message(text=ass_dt.get_date_by_value(value_date))

        return []
