#Insomnia generated CODE + all headers

import requests

url = "https://shop.metro.bg/ordercapture.customercart.v1/carts/d38eb941-c05e-45e4-a935-28d0d0adcbcd"

querystring = {"customerId":"1001100022726355","cardholderNumber":"1","storeId":"00022","country":"BG","locale":"bg-BG","fsdAddressId":"1001100022726355994-AD0532EI","status":"ACTIVE","__t":"1668148914504"}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://shop.metro.bg/shop/cart",
    "CallTreeId": "CB33CE35-8916-4897-859A-9D0733B18AB7||BTOC-6D0EFBF9-94E2-479E-958D-566A772ACA84",
    "Content-Type": "application/json; charset=UTF-8",
    "x-timeout-ms": "5000",
    "Connection": "keep-alive",
    "Cookie": "selectedLocale_BG=bg-BG; anonymousUserId=B9292B61-7381-4964-982C-9DFD170AB125; allowedCookieCategories=necessary%7Cfunctional%7Cperformance%7Cpromotional%7CUncategorized; _gcl_au=1.1.1979650770.1667748124; _ga_4N83E9ZK99=GS1.1.1668148870.8.0.1668148913.17.0.0; _ga=GA1.1.300302328.1667748124; local_ga_4N83E9ZK99=GS1.1.1668148875.12.1.1668148912.23.0.0; local_ga=GA1.1.1334358693.1667748255; idamUserIdToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IktfYWE1NTAxNWEtMjA2YS0xMWVkLTk4ZDUtZTJjYzEyYjBkYzUwIn0.eyJleHAiOjE2NjgxNTA2NzQsImlhdCI6MTY2ODE0ODg3NCwiYXVkIjoiQlRFWCIsInNlc3Npb25fc3RhdGUiOiJTSjRidXRmUnlvdTU4NkhTX0J5Y0xRbXZkWTFhRlp6cUwxelp6STJDS2VJLmVwdkNkcExDIiwiaXNzIjoiaHR0cHM6Ly9pZGFtLm1ldHJvLmJnIiwiZW1haWwiOiJvZmZpY2VAdGVydmlvbi5iZyIsIm5vbmNlIjoiZTEwODlhMzU5NTc2NGE3Y2E3ZGVjYmI2YWFiNmNjYzYiLCJjX2hhc2giOiIiLCJzdWIiOiJVX2Y0MjBhY2E4LWY2OTMtNGMxNS1iOTIzLTc1NWY5NTc3ZTIwMCIsImF0X2hhc2giOiJHcngzdFRHNlhUdHBZaTB0WVNKQ2lRIiwicmVhbG0iOiJTU09fQ1VTVF9CRyIsImF1dGhfdGltZSI6MTY2ODA5NjUzNiwiYW1yIjpbIlVTRVJfQ1JFREVOVElBTFMiXX0.ATQ-8efw6svo_QhjtY-luAQp-t8Zhj58h9vlO7buJsPaT46_1dEftI0ed1EhZGJkEWuJ-bBxg6f33XUx6FvFdQNsjcvh1QpQ7-spjGlLZPg82_AiHE7Dz_5_J466u5oMPb2AoDMbBUppzkhnBuNZbavV9ASuuQjKYkkRCRKUofGNQ4qkWA-PQVjtG3di0zCKbS7-ED6yjNPicdjq1onQrP0Q7eSxQK_vWtE6QcGzm40cJv3tSk3M0hB_Ez3BC8ON0_i8H6u3GtI675FWO-eP2SbW9jNoKxJRXEXHkxplTBcS_5Fn5QPYlzpaYwLDZioiX15th7jbWDYd4lu8kzG4kqq-8SE1CTo; USER_TYPE=CUST; INTERNAL_LOGIN_DISABLE_SSO=false; SES2_customerAdr_1001100022726355={%22addressId%22:%221001100022726355994-AD0532EI%22%2C%22addressHash%22:%221001100022726355994-AD0532EI%22%2C%22storeId%22:%2200022%22}; SES2_customerAdr_={%22addressId%22:null%2C%22addressHash%22:null%2C%22storeId%22:%2200022%22}; UserSettings=SelectedStore=1b1fc6ac-2ad6-4243-806e-a4a28c96dff4&SelectedAddress=1001100022726355994-ad0532ei; _fbp=fb.1.1667933732915.898298703; BIGipServerbetty.metrosystems.net-80=!SrZwnePILm21ZAsEdKzHuTxiWd+ak9uyWmo21F5HcXmHsTUyT3uz/INnwNu9TFcHl5xZ473A0/WmUJA=; abGroups={%22CI_ARTICLE_BANNER%22:%22B%22%2C%22SD_NEW_SUGGESTIONS%22:%22B%22%2C%22QUICKENTRY_SEARCH_BACKEND%22:%22B%22%2C%22CI_USE_SEARCH_INSTEAD_OF_SIMPLESEARCH%22:%22A%22%2C%22SD_USE_SOLR_ALT%22:%22A%22}; _dd_s=rum=0&expire=1668149813340; compressedJWT=eNpVUslyozAU/KKkWIwTjphV2JINiE2XFAhsEEvswTbL149IMlMzB5Wq+r3ufls5u1Vu0/pYu0G4ABHVrvpazu6VynAFXSojkSSgPuhuVcTeiu2K2L+SWGEkAAPorkIWgC1gyCYJFEvLBbjxD7kRZUVyUUhTZWlrrvyliMHKr0niC+UXN3oUdivkdnTnegKduU5HDCyC73xbnUnIcxxeS6eIuT0OoI/wf3jtbrwIDqWJIBYLfHCqHRbGoWgseHAIDi0wpCJaNX9+OpB2dzrYBPqmGoB6rIsICbnstl/+jev4BphXnNqWkttqRXSO93cKevfJa6WAXSnokEhl/5nH0ZzoYEh0V6S28h1j5ggNc4KGNkIGZMjSBWHOq6eVV9HO/8ylqSGJeyxikc/D/eFZ3zm936ZSFVEpmsNOHUg0/u2f+wgZ98R2JJF4+uH5f7SfxTrHvv3GeS88X/3qpYs6/pbMJE/aoXbtiXTWQKWQzxRd867gPuhKJOWU1//GCD+Qtll1s5jXwUwJscuEMBAhhvPRgOseN5TrQZxKR8MUIQsnOI91liC+88hME78F7HNCLN1A7G2O2Fwguyxn79WeLFP/pZyDqhTwZKB79FmehIpcy4ZugxRJKrulDksoPPRbYYBdvu3fNI9WzU2++KH1a9KCMTxcBF/QnjYZdE2DCksdP3hYqDOZIc+uiuWqWmSquO9dZC+f6q5dWPKopkXQp+VdUufar6SsIzrztVFZjh8vG0c7oMXaMCfUczKpcpV5Ul8G+uWk1rFiKgA802BQxlu4z/dGmHvtqNHtC79s+jIIzUIOdikxcd6NGfNUo5s+NHqsUG+oikcbXXm0+5DV+G24Kafzrrb3W5DWSPYngWDsMiFafMFxzki9NzuRYHPQWSm8P+4b5eLZ/e1sVKXztrnL3sOu4v02fDlnPja8y720oo/xNyjtS54=; tsession={%22sessionId%22:%22F1194409-43C6-43CA-82B7-51497109D43F%22%2C%22timestamp%22:1668148875000}; _ts=l+c70013b093154bbc9094be5707a89581; _gid=GA1.2.1519885248.1668148881; _gat_UA-118296439-9=1",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)