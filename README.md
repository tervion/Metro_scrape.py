What have I done:

I need to scrape some data from a website that req login.

I copy paste the code of 2 tutorials made by John Watson Rooney called:
 
<a href="https://www.youtube.com/watch?v=H2-5ecFwHHQ&list=PLJa3hX5xIVdUs9GxTAopVOd1tQ4e54-rd&index=7&t=503s">The Biggest Mistake Beginners Make When Web Scraping</a>
<a href="https://www.youtube.com/watch?v=G7s0eGOaRPE&list=PLJa3hX5xIVdUs9GxTAopVOd1tQ4e54-rd&index=6">Login and Scrape Data with Playwright and Python</a>

Than I combined them and added some JavaScript to scroll to the bottom of the page. Than I found an article called: 
<a href="https://scrapfly.io/blog/how-to-avoid-web-scraping-blocking-headers/">How Headers Are Used to Block Web Scrapers and How to Fix It</a>

Thus replacing "import requests" with "import httpx" and added the HEADERS as per given from Insomnia. From what I understand browsers return headers in certain order and this is an often overlooked web scraper identification method. Primarily because many http clients in various programming languages implement their own header ordering - making identification of web scrapers very easy! If this is true I need to figure out a way to return my cookies header following the correct order, which by the way I have no clue how to figure out but I believe its #11 or #3 judging by the code generated by Insomnia. How ever no matter what I do I always get: error 401 You must provide a http header.
