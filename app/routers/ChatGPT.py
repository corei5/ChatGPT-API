import sys


sys.path.append("..")

from fastapi import APIRouter, UploadFile, Form, File
from fastapi.responses import HTMLResponse

from app.common.util.decorators import log
from app.services.ChatGPT import ChatGpt_Class

router = APIRouter(
    prefix='/ChatGpt_API',
    tags=['ChatGpt_API']
)




@router.post('/chatgpt', response_class=HTMLResponse, status_code=200)
@log(__name__)
def chatgpt(text):
    chatGpt_class = ChatGpt_Class()
    resp = chatGpt_class.ChatGpt_output(text)
    return resp