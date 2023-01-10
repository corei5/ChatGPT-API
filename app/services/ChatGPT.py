import logging
from pyChatGPT import ChatGPT

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

class ChatGpt_Class:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        super().__init__()

    def ChatGpt_login(self):
        session_token = '' # Add auth with session token
        api = ChatGPT(session_token)  # auth with session token
        return api

    def ChatGpt_output(self,text):
        try:
            api = self.ChatGpt_login()
            try:
                resp = api.send_message(text)
                return resp['message']
            except:
                return "Getting error from ChatGpt"
        except:
            return "Not able to login in ChatGpt"

