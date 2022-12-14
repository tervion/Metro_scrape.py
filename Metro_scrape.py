# Metro_scrape.py

import time
import httpx
from playwright.sync_api import sync_playwright

token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IktfYWE1NTAxNWEtMjA2YS0xMWVkLTk4ZDUtZTJjYzEyYjBkYzUwIn0.eyJrZXlNYXAiOnsiY2RtIjp7InBlcnNvbiI6IjRlYWViOTEwLTI0M2EtMTFlZC1iYTY4LTMxNWMxYjczMjFiZiJ9fSwiZW1haWwiOiJvZmZpY2VAdGVydmlvbi5iZyIsImFjY291bnRDb250ZXh0IjoiIiwiY291bnRyeSI6IkJHIiwibG9jYWxlIjoiYmctQkciLCJpYXQiOjE2NjgyMzYzOTAsImF1ZCI6IkJURVgiLCJ1c2VyVHlwZSI6IkNVU1QiLCJpc3MiOiJodHRwczovL2lkYW0ubWV0cm8uYmciLCJleHAiOjE2NjgyMzk5OTAsImF1dGhvcml6YXRpb24iOltdLCJyZWFsbSI6IlNTT19DVVNUX0JHIiwic3ViIjoiVV9mNDIwYWNhOC1mNjkzLTRjMTUtYjkyMy03NTVmOTU3N2UyMDAiLCJ1cG4iOiJvZmZpY2VAdGVydmlvbi5iZyJ9.AV77vQMwhXmbCZr5CnpdWgWWFIv9yzP1pbYnTK6NNoa426D4DcueUvmFTvR5rhsvTaLHxASizs-41iREVOMuXQ7dKgxDNk10m6Xp_ZgZjav9E-686UxwFPEzzDw3O2YSg7ozm4KTfdleo8boaS2tXe72cCOtEJlerwP6GPDRojr7GnXfJl5H6tYR4FVFPZbFHfQ1RFzgFDzGx9eDqmkYMkw5lztN54di5yr6GtWKRJYJIm4a8vXWSCwq3p0aDadv8QZoo_-TiWFDiqSH2THSaCrsfyst1LJmDTMJV_HDJ7LKrDXqnS22XPSN8pWOyl3h5GGrBKC1e8YhfDUuS5K93l2a0rXw7qs"
HEADERS = {
    "Authorization": "Bearer " + "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IktfYWE1NTAxNWEtMjA2YS0xMWVkLTk4ZDUtZTJjYzEyYjBkYzUwIn0",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://shop.metro.bg/shop/cart",
    "CallTreeId": "||BTOC-1BF47A0C-CCDD-47BB-A9DA-592009B5FB38",
    "Content-Type": "application/json; charset=UTF-8",
    "x-timeout-ms": "5000",
    "DNT": "1",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}

def get_cookie_playwright():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://shop.metro.bg/shop/cart')

        page.locator('input#user_id')
        page.hover('input#user_id')
        page.click('input#user_id')
        page.fill('input#user_id', 'office@tervion.bg')

        page.locator('input#password')
        page.hover('input#password')
        page.click('input#user_id')
        page.fill('input#password', 'Metro1234')

        page.locator('button[type=submit]')
        page.hover('button[type=submit]')
        page.click('button[type=submit]')
        page.click('button.btn-primary.accept-btn.field-accept-button-name')

        page.evaluate(
            """
            var intervalID = setInterval(function () {
                var scrollingElement = (document.scrollingElement || document.body);
                scrollingElement.scrollTop = scrollingElement.scrollHeight;
            }, 200);

            """
        )
        prev_height = None
        while True:
            curr_height = page.evaluate('(window.innerHeight + window.scrollY)')
            if not prev_height:
                prev_height = curr_height
                time.sleep(1)
            elif prev_height == curr_height:
                page.evaluate('clearInterval(intervalID)')
                break
            else:
                prev_height = curr_height
                time.sleep(1)
        page.reload()
        page.evaluate(
            """
            var intervalID = setInterval(function () {
                var scrollingElement = (document.scrollingElement || document.body);
                scrollingElement.scrollTop = scrollingElement.scrollHeight;
            }, 200);

            """
        )
        prev_height = None
        while True:
            curr_height = page.evaluate('(window.innerHeight + window.scrollY)')
            if not prev_height:
                prev_height = curr_height
                time.sleep(1)
            elif prev_height == curr_height:
                page.evaluate('clearInterval(intervalID)')
                break
            else:
                prev_height = curr_height
                time.sleep(1)

        cookie_for_requests = context.cookies()[3]['value']
        browser.close()
    return cookie_for_requests

def req_with_cookie(cookie_for_requests):
    cookies = dict(
        Cookie=f'BIGipServerbetty.metrosystems.net-80={cookie_for_requests};')
    r = httpx.get('https://shop.metro.bg/ordercapture.customercart.v1/carts/alias/current', cookies=cookies)
    return r.text

if __name__ == '__main__':
    data = req_with_cookie(get_cookie_playwright())
    print(data)

# Packages

#Playwright
#PyTest
#PyTest-Playwirght
#JavaScript
#TypeScript
#httpx
