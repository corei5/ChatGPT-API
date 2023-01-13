import logging
from pyChatGPT import ChatGPT

from googletrans import Translator
translator = Translator()

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

class ChatGpt_Class:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        super().__init__()

    def ChatGpt_login(self):
        session_token = ''
        api = ChatGPT(session_token)  # auth with session token
        return api

    def ChatGpt_output(self,text, language):
        try:
            api = self.ChatGpt_login()
            try:
                text_conv_eng = translator.translate(text, dest='en')
                print(text_conv_eng.text)
                resp = api.send_message(text_conv_eng.text)
                print(language)
                message = translator.translate(resp['message'], dest=str(language))
                return message.text
            except Exception as e:
                print(e)
                return "Getting error from ChatGpt"
        except Exception as e:
            print(e)
            return "Not able to login in ChatGpt"

