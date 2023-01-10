# ChatGPT-API

REST API for the extract information from ChatGPT in python.

This API provides the ChatGPT output for a ``input``.

## Prerequisites

We require a python version `3.7` or above.

Requirement by service:

| Service                    | Requirement(s)    |
|----------------------------|-------------------|
| `/ChatGpt_API/chatgpt`          | `summarize the paper "The War on Drugs and HIV/AIDS How the Criminalization of Drug Use Fuels the Global Pandemic"`|


## Output Demo  (Example)
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
