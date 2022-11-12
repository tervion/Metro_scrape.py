import requests

url = "https://shop.metro.bg/explore.login.v1/auth/loginWithIdamAccessToken"

querystring = {"country":"BG"}

payload = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IktfYWE1NTAxNWEtMjA2YS0xMWVkLTk4ZDUtZTJjYzEyYjBkYzUwIn0.eyJrZXlNYXAiOnsiY2RtIjp7InBlcnNvbiI6IjRlYWViOTEwLTI0M2EtMTFlZC1iYTY4LTMxNWMxYjczMjFiZiJ9fSwiZW1haWwiOiJvZmZpY2VAdGVydmlvbi5iZyIsImFjY291bnRDb250ZXh0IjoiIiwiY291bnRyeSI6IkJHIiwibG9jYWxlIjoiYmctQkciLCJpYXQiOjE2NjgyMzYzOTAsImF1ZCI6IkJURVgiLCJ1c2VyVHlwZSI6IkNVU1QiLCJpc3MiOiJodHRwczovL2lkYW0ubWV0cm8uYmciLCJleHAiOjE2NjgyMzk5OTAsImF1dGhvcml6YXRpb24iOltdLCJyZWFsbSI6IlNTT19DVVNUX0JHIiwic3ViIjoiVV9mNDIwYWNhOC1mNjkzLTRjMTUtYjkyMy03NTVmOTU3N2UyMDAiLCJ1cG4iOiJvZmZpY2VAdGVydmlvbi5iZyJ9.AV77vQMwhXmbCZr5CnpdWgWWFIv9yzP1pbYnTK6NNoa426D4DcueUvmFTvR5rhsvTaLHxASizs-41iREVOMuXQ7dKgxDNk10m6Xp_ZgZjav9E-686UxwFPEzzDw3O2YSg7ozm4KTfdleo8boaS2tXe72cCOtEJlerwP6GPDRojr7GnXfJl5H6tYR4FVFPZbFHfQ1RFzgFDzGx9eDqmkYMkw5lztN54di5yr6GtWKRJYJIm4a8vXWSCwq3p0aDadv8QZoo_-TiWFDiqSH2THSaCrsfyst1LJmDTMJV_HDJ7LKrDXqnS22XPSN8pWOyl3h5GGrBKC1e8YhfDUuS5K93l2a0rXw7qs"
headers = {
    "cookie": "BIGipServerbetty.metrosystems.net-80=!qQj%2Bdjr3JVKOnuYEdKzHuTxiWd%2Bak1dp6JVXDGvPolbpAYOl23mCyTlpyRdQEte99U5xnOiePdTagAU%3D; selectedLocale_BG=bg-BG",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "CallTreeId": "B4F182AE-5B95-48B2-A951-FD48A45A92EA||SSto-0D73F0C7-BB61-47EE-AB5A-CF308CA3502D",
    "Connection": "keep-alive",
    "Content-Type": "*/*",
    "Cookie": "selectedLocale_BG=bg-BG; BIGipServerbetty.metrosystems.net-80=\u00213kgLlKQiCJXbqfZlllsv0yPj1IQ7JBxkatTApc3GN/vzrgdGX/g+JkYaAhNCqzkbwYHhF/GVD3ppXz0=; anonymousUserId=80A4E748-E248-4AAF-B5AA-C6C5E25D3829; idamUserIdToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IktfYWE1NTAxNWEtMjA2YS0xMWVkLTk4ZDUtZTJjYzEyYjBkYzUwIn0.eyJleHAiOjE2NjgyMzgxOTAsImlhdCI6MTY2ODIzNjM5MCwiYXVkIjoiQlRFWCIsInNlc3Npb25fc3RhdGUiOiJKUHNtR1lGQTJsR0tOUEVqenFQakFhYXlCVG9DSUVtOTROeWFKWGQ0eVRRLmJ3VGZOMWVYIiwiaXNzIjoiaHR0cHM6Ly9pZGFtLm1ldHJvLmJnIiwiZW1haWwiOiJvZmZpY2VAdGVydmlvbi5iZyIsIm5vbmNlIjoiNjNkZDc5Y2UxNmU1NGZjMDk0NGM2MTdiZTMwNDg0NjEiLCJjX2hhc2giOiIiLCJzdWIiOiJVX2Y0MjBhY2E4LWY2OTMtNGMxNS1iOTIzLTc1NWY5NTc3ZTIwMCIsImF0X2hhc2giOiJ3UUk1SDdkU3ZIY3hCZWZkTjQzbmlnIiwicmVhbG0iOiJTU09fQ1VTVF9CRyIsImF1dGhfdGltZSI6MTY2ODIzNjM4OSwiYW1yIjpbIlVTRVJfQ1JFREVOVElBTFMiXX0.AWhs1lkkQhXLpR0Rga8N5z1lG-CRHMRPDhYN7GrVfNhSNz44_V6Uk1re5zfbPDrhA3n3CKmIduu9fFBbJde7NePUwW7b06H3yUFdmYM7PS4Wunvpt1G7gjK4fG5YQHZZ2xl1wo-DHbBKzFBdAlaz9g9jbr0XWRWbB6Dl5aIx0Ok7urxG4D_8cnQ9mwdiTYnG3GTlP0FeUbVg74fzFZ9g4qCWL9cl7zjZiQEIPuqMsQj4EGRuKsf7WdkurnJVQUn_-cJ0OXPUcpEi29s30YmlgBY5Zl3TXgQ1hl_CCtllTmbaokemc9ySo8PC3dPDGkqe6fX-DrNnbK2jx_usPMQBIpYL2RYKooY; USER_TYPE=CUST; compressedJWT=eNpVUtuSojAU/KKZAgSRR0UuQQiCMUDeJCiEm64ot6/fMDO7tfuQSlWf092nT3KdnCK1KPOZczrPQITM0T6vk/OgK28BHbqCIokBc3WnyKJgwXZZFD5IpJTkBDrQPITLCaxB+ziSFRC9uYB+HMKTWZ/DFdYTnLWEG3D+nEVg4TMSh8L1i4vfmVULqYVfXE+gE9dpyB6J4Lvf0iZy5j02n6VRxNQaOtBi9B/OHDnAXnc1oIfEDLl2sUPC0GWV6bk2QWcTdIkIF82fm3ak3h1di3ihoZ0AG1iGoZCunPrLv3LscA+mBaeWqaSWVhB9yfeioHV6PisF5YOCBop0FfZphKdYB12sOyK1lO9aaQze3hi9/XbwSrDyymSGiPPYuPAK2oT3VBorEjt+Fol8H84Pz/zuacM6kQpMJTydG60jePibn/sIF+6JLCyRaPzhhX+0+2zZY1t/4zwL79e+sjS44We+GKSnDayXTKQxOyqd+U7hI20y7gMfRFKOKfu3RvgHqatF9xLxOUpDgmU+eXOl+Gir+HtveUeZcj0PJZK/B7OPKsXTB3aJIX9zbCRxWIPyPsIykb3Skzh38FE+34LPUNh2mcIEszkWFRtvwuW2eb1fMHC1vGrVuRnKm6+i591JbmrEgjFztutioxszSOsxRaskH1nbX/dgxMmHPPb2fJCwGx0PR7U+mlP1bqlRvg+bjo6yKeyiQY9jOVVyNHXufYcrWdY/nmxkihIY5d5LNlk1nKZKtDI30+R9icrk/WE/LSi4j0qzq/zXalhLqsqCtL0/bXeXRl3YSg809i9GRNiRBk1NdMTRVaBv7OuXVOlj76oI61aa7airgnhdxCLdiXLfyHKUPY2pzzuinvNKdd3wdcN5bwppejjErQST9BLX6xzdIzPQh3VJf0mWTc+O3kfxVthCNXAv0wbEDXlK66KsxJDS/DfqK04u; SES2_customerAdr_1001100022726355={%22addressId%22:%221001100022726355994-AD0532EI%22%2C%22addressHash%22:%221001100022726355994-AD0532EI%22%2C%22storeId%22:%2200022%22}; SES2_customerAdr_={%22addressId%22:null%2C%22addressHash%22:null%2C%22storeId%22:%2200022%22}; _ts=l+8f70167ae7c94cda9e8adea4a3d7f9ac; allowedCookieCategories=necessary%7Cfunctional%7Cperformance%7Cpromotional%7CUncategorized; UserSettings=SelectedStore=1b1fc6ac-2ad6-4243-806e-a4a28c96dff4; abGroups={%22CI_ARTICLE_BANNER%22:%22B%22%2C%22SD_NEW_SUGGESTIONS%22:%22B%22%2C%22QUICKENTRY_SEARCH_BACKEND%22:%22A%22%2C%22CI_USE_SEARCH_INSTEAD_OF_SIMPLESEARCH%22:%22A%22%2C%22SD_USE_SOLR_ALT%22:%22A%22}",
    "Origin": "https://shop.metro.bg",
    "Referer": "https://shop.metro.bg/shop/cart?itm_pm=cookie_consent_accept_button",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "X-Qos-Priority": "HIGH",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": ""Linux""
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)

HEADER:

{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "K_aa55015a-206a-11ed-98d5-e2cc12b0dc50"
}

PAYLOAD:DATA

{

  "keyMap": {

    "cdm": {

      "person": "4eaeb910-243a-11ed-ba68-315c1b7321bf"

    }

  },

  "email": "office@tervion.bg",

  "accountContext": "",

  "country": "BG",

  "locale": "bg-BG",

  "iat": 1668236390,

  "aud": "BTEX",

  "userType": "CUST",

  "iss": "https://idam.metro.bg",

  "exp": 1668239990,

  "authorization": [],

  "realm": "SSO_CUST_BG",

  "sub": "U_f420aca8-f693-4c15-b923-755f9577e200",

  "upn": "office@tervion.bg"

}

VERIFY SIGNATURE

RSASHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  ,
  {
  "e": "AQAB",
  "kty": "RSA",
  "n": "ApmXRtqOGJPJrzaNXFVU6tzqJ5V9qEx-JoYYGUMxZDGThbiWueKP5ktOsTU5fBKvM23EmEWyyffB-I1lxftOZCy-Jl2ubLWqHRG6sjVMYTaL6qJ0osNAZ-k5ALrI1xj0IiGZUQr2elIp0Gj94ferSh-MazUHw8YP2bnxzcCL1wyLH3jGq6TALMTJFPobCO_HPT_SZC_tyQ7kQW4cSOONIuuF4j8LUMIUcAQuUPL_DEwwqbXYHI7CRdqAMPcn_q1KHPgXl1VhMlcualKfA9cDXY_WstVp9UK6y-7JMRTVHna0nkRft3BgH_3fBk-e6j_GRyLF0GJHc-UcZyIck1b9U-PHYPB9GGU"
}
)
