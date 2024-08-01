# function_app.py

import logging
import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = req.params.get('url')
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')

    if url:
        try:
            response = requests.get(url)
            return func.HttpResponse(f"URL: {url} responded with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            return func.HttpResponse(f"HTTP request failed: {e}", status_code=500)
    else:
        return func.HttpResponse(
            "Please pass a URL on the query string or in the request body",
            status_code=400
        )
