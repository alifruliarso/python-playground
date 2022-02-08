"""https://gist.github.com/chitransh89/664444c994e9d36d582b44255349d8eb"""
import asyncio
from pyppeteer import launch
from urllib.parse import urlparse
import http.client
import json
import logging

URL = 'https://example.metabase.com/dashboard/4'
USERNAME = 'username'
PASSWORD = 'password'
PATH_TO_SAVE = 'example.png'
WIDTH = 1920
HEIGHT = 1920


def get_session():
    url = urlparse(URL)
    host_name = url.hostname

    if url.scheme == 'https':
        conn = http.client.HTTPSConnection(host_name)
    elif url.scheme == 'http':
        conn = http.client.HTTPConnection(host_name)
    else:
        raise Exception("Please use http or https protocol only")

    payload = json.dumps({"password": PASSWORD, "username": USERNAME})

    headers = {
      'Content-Type': 'application/json'
    }
    conn.request("POST", "/api/session/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    session_resp = json.loads(data.decode("utf-8"))
    return session_resp['id']


async def main():
    session_id =  get_session()
    logging.debug("Loading Browser ...")
    browser = await launch({'defaultViewport': {'width': WIDTH, 'height': HEIGHT}})
    logging.debug("Browser Loaded \n Opening Tab ...")
    page = await browser.newPage()

    await page.setCookie({
        'name': 'metabase.SESSION', 'value': session_id,
        'url': URL
    })
    logging.debug("Go to page ...")
    await page.goto(URL, {'waitUntil': 'networkidle2'})
    logging.debug("Taking Screenshot ...")
    await page.screenshot({'path': PATH_TO_SAVE})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())