from fastapi.responses import HTMLResponse
from app_factory import create_app

app = create_app()


@app.get('/', response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title> WHO COVID-19 research papers classification API </title>
        </head>
        <body>
            Welcome to the Open Research Knowledge Graph NLP API
            <img src="https://orkg.org/og_image.png" alt="Simply Easy Learning" width="200" height="80">
        </body>
    </html>
    """