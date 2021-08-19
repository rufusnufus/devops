"""This module shows current Moscow Time."""
from datetime import datetime

import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def get_time():
    """Make GET request to WorldTimeAPI about current Moscow Time and return it.

    Returns
    -------
    html
        an html page with current Moscow time or with error code.
    """
    style = "\"background-image: url('https://wallpaperaccess.com/full/372581.jpg'); display: flex; justify-content: center; text-align: center; flex-direction: column; color: white; font-size: 30px;\""
    html_content = """
        <html>
            <head>
                <title>Moscow Current Time</title>
            </head>
            <body style=%s>
                <h1>Moscow time</h1>
                <h1>%s</h1>
            </body>
        </html>
        """
    response = requests.get("http://worldtimeapi.org/api/timezone/Europe/Moscow")
    if response.status_code == 200:
        date = datetime.strptime(response.json()["datetime"], "%Y-%m-%dT%H:%M:%S.%f%z")
        time = f"{date.hour}:{date.minute}:{date.second}"
        return HTMLResponse(content=html_content % (style, time), status_code=200)
    else:
        error = f"Error: {response.status_code}"
        return HTMLResponse(content=html_content % (style, error), status_code=404)
