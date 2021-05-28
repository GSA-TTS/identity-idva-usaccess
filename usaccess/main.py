"""
USAccess Microservice FastAPI Web App.
"""

import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/test")
async def test(request: Request):
    """
    test function
    """

    return JSONResponse(
        {
            "message": "debug response",
            "request": bytes.decode(await request.body()),
            "time": str(datetime.datetime.now()),
        }
    )
