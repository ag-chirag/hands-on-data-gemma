import os
import data_gemma as dg
from dotenv import load_dotenv
import logging

load_dotenv()

# Initialize Data Commons API client
DC_API_KEY = os.getenv('DC_API_KEY')

class DataCommonsClient:
    def __init__(self):
        self.data_fetcher = dg.DataCommons(api_key=DC_API_KEY)

    def call_dc(self, questions: list[str]) -> dict[str, dg.base.DataCommonsCall]:

        try:
            q2resp = self.data_fetcher.calln(questions, self.data_fetcher.point)
        except Exception as e:
            logging.warning(e)
            q2resp = {}
            pass

        return  q2resp
    
    @staticmethod
    def pretty_print(q2resp: dict[str, dg.base.DataCommonsCall]):
        markdown_output = "# Data Commons Response\n"
        for k, v in q2resp.items():
            markdown_output += f"**{k}**\n\n"
            markdown_output += f"{v.answer()}\n\n"
        return markdown_output