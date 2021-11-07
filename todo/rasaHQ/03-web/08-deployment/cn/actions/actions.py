# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.index_api import GlobalIndex


# class ActionIndexSearch(Action):
#
#     def name(self) -> Text:
#         return "action_index_search"
#
#     async def run(self, dispatcher: CollectingDispatcher,
#                   tracker: Tracker,
#                   domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         for blob in tracker.latest_message["entities"]:
#             if blob['entity'] == 'market_index':
#                 price = 3000
#                 index_info = 11
#                 response = """{}的价格是{}.""".format(blob['value'], price)
#
#                 response = GlobalIndex().get_index_names()
#                 dispatcher.utter_message(text=response)
#
#         return []


class ActionGlobalIndexs(Action):
    def name(self) -> Text:
        return "action_global_indexs"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        for blob in tracker.latest_message["entities"]:
            if blob["entity"] != "global_indexs":

                response = GlobalIndex().get_index("1010")

                dispatcher.utter_message(text=response)

        return []
