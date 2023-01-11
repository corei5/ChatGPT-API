# ChatGPT-API

[![License](https://img.shields.io/github/license/terry3041/pyChatGPT.svg?color=green)](https://github.com/terry3041/pyChatGPT/blob/main/LICENSE)


REST API for the extract information from ChatGPT chat in python.

This API provides the ChatGPT chat output for a ``input``.

## Prerequisites

Please check requirements.txt file.

## Obtaining session_token

1. Go to https://chat.openai.com/chat and open the developer tools by `F12`.
2. Find the `__Secure-next-auth.session-token` cookie in `Application` > `Storage` > `Cookies` > `https://chat.openai.com`.
3. Copy the value in the `Cookie Value` field and paste it into the app/services/ChatGPT.py file (`session_token` variable).

![image](https://user-images.githubusercontent.com/19218518/206170122-61fbe94f-4b0c-4782-a344-e26ac0d4e2a7.png)


## Requirement by service:

| Service                    | Requirement(s)    |
|----------------------------|-------------------|
| `/ChatGpt_API/chatgpt`          | `text: summarize the paper "The War on Drugs and HIV/AIDS How the Criminalization of Drug Use Fuels the Global Pandemic"`|


## Output Demo  (Example)

```The paper "The War on Drugs and HIV/AIDS: How the Criminalization of Drug Use Fuels the Global Pandemic" argues that the criminalization of drug use has contributed to the spread of HIV/AIDS. The authors argue that criminalization makes it more difficult for people who use drugs to access harm reduction services like needle exchange programs, which can help prevent the spread of HIV. They also argue that criminalization leads to risky behavior, such as sharing needles, because people who use drugs are afraid to seek help. The authors argue that ending the criminalization of drug use and increasing access to harm reduction services would be an effective way to reduce the spread of HIV/AIDS.```

## Run in CMD (Example)

```commandline
curl -X 'POST' \
  'http://127.0.0.1:8000/ChatGpt_API/chatgpt?text=summarize%20the%20paper%20%22The%20War%20on%20Drugs%20and%20HIV%2FAIDS%20How%20the%20Criminalization%20of%20Drug%20Use%20Fuels%20the%20Global%20Pandemic%22' \
  -H 'accept: text/html' \
  -d ''
```

## How to run

### With ``docker-compose``


```commandline

```

### Manually
```commandline
Run FastAPI:

uvicorn main:app --reload

```
For local development you may run the web server using ``uvicorn`` with the ``--reload`` option:

```commandline
uvicorn app.main:app --host 0.0.0.0 --port 4321 --reload
```


## API Documentation
After successfully running the application, check the documentation at `localhost:4321/docs`
or `localhost:4321/redoc` (please adapt your `host:port` in case you configured them).


## Insipration
This project is inspired by

-   [ChatGPT](https://github.com/acheong08/ChatGPT)
-   [chatgpt-api](https://github.com/transitive-bullshit/chatgpt-api)
-   [pyChatGPT](https://github.com/terry3041/pyChatGPT)
