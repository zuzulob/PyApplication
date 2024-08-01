# function_app.py

import logging
from textblob import TextBlob
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    text = req.params.get('text')
    if not text:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            text = req_body.get('text')

    if text:
        blob = TextBlob(text)
        sentiment = blob.sentiment
        return func.HttpResponse(f"Text: {text}\nSentiment: {sentiment}", status_code=200)
    else:
        return func.HttpResponse(
            "Please pass a text on the query string or in the request body",
            status_code=400
        )
