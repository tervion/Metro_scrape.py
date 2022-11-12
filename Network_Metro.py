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

import requests

url = "https://idam.metro.bg/authorize/api/oauth2/check_session_iframe"

querystring = {"country":"BG"}

payload = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IktfYWE1NTAxNWEtMjA2YS0xMWVkLTk4ZDUtZTJjYzEyYjBkYzUwIn0.eyJrZXlNYXAiOnsiY2RtIjp7InBlcnNvbiI6IjRlYWViOTEwLTI0M2EtMTFlZC1iYTY4LTMxNWMxYjczMjFiZiJ9fSwiZW1haWwiOiJvZmZpY2VAdGVydmlvbi5iZyIsImFjY291bnRDb250ZXh0IjoiIiwiY291bnRyeSI6IkJHIiwibG9jYWxlIjoiYmctQkciLCJpYXQiOjE2NjgyMzYzOTAsImF1ZCI6IkJURVgiLCJ1c2VyVHlwZSI6IkNVU1QiLCJpc3MiOiJodHRwczovL2lkYW0ubWV0cm8uYmciLCJleHAiOjE2NjgyMzk5OTAsImF1dGhvcml6YXRpb24iOltdLCJyZWFsbSI6IlNTT19DVVNUX0JHIiwic3ViIjoiVV9mNDIwYWNhOC1mNjkzLTRjMTUtYjkyMy03NTVmOTU3N2UyMDAiLCJ1cG4iOiJvZmZpY2VAdGVydmlvbi5iZyJ9.AV77vQMwhXmbCZr5CnpdWgWWFIv9yzP1pbYnTK6NNoa426D4DcueUvmFTvR5rhsvTaLHxASizs-41iREVOMuXQ7dKgxDNk10m6Xp_ZgZjav9E-686UxwFPEzzDw3O2YSg7ozm4KTfdleo8boaS2tXe72cCOtEJlerwP6GPDRojr7GnXfJl5H6tYR4FVFPZbFHfQ1RFzgFDzGx9eDqmkYMkw5lztN54di5yr6GtWKRJYJIm4a8vXWSCwq3p0aDadv8QZoo_-TiWFDiqSH2THSaCrsfyst1LJmDTMJV_HDJ7LKrDXqnS22XPSN8pWOyl3h5GGrBKC1e8YhfDUuS5K93l2a0rXw7qs"
headers = {
    "cookie": "TSbcb913d5075=deleted; TSbcb913d5029=08a625aae3ab280082ad880439e33adfd0f86da14f54bd9a76e5936d17480b4899c6fe486866dcfbd461330e34a48401; TSbcb913d5078=08a625aae3ab2000a1463c8668e5370a1b66e2994d7da8c02c5761fcdb589b8c85ae620fffb5fd1b08e9bdfe3f186001791e0a19357a0397c9dc297dd335d6eb5d50cbc615d525cc17d5122049aba8b7f895c2be19b82a4d4f082da8c516cbd2206a174b306aa6daabee704236febcfb74b0db749e45c4a16c4aa64440f483708c50fe4257593ab1c52013526e539aee0461b9e5fb6c295aeb88d104fc3c876890252c7dc491fd24d4c824d005ccbff8bd769ff4229325507c753134b9eae58496a2b7449218c5a78c628f374264c30682358d411de18e69e9fa51ecadac2ce0dd1dfcfc1cb3d30ddb8fa4693269a61cf1b2143348305dbab68e0270dbaf6761faf177dfb46ab04f1cc73c37dfd7c8cc3f35cb5abc4112c37f4ef0b96d3511d93d03d07f6460595ae42dc66afa73096aa327fedb326351ac80903b56b818bfc462d3a83f15c02ac28162517794b0635ed802ea0311be9cc076a42b754e7a538396175fce455ad812087d274637440483919e60b5a770ce71b0642b7a8450097db2d92be0772dc4ed7b26ab1352009464; TS7a8c3458027=08a625aae3ab20007ffea3efe1ba334932ca4663b37e26dc670784ce3cf4fc1bc890323616ab57b0086781d1e01130004d8532a06992a5f30f181d3ef3d3d411f3b0ffae1db37840c672c02d64fb71c6575670c56e7a69312caee12d8eb18f83; BIGipServeridam.metrosystems.net-80=!NXSJTdtgHVWcR8HUzUGSRTsG4v6oUb8lOuo1eqqq6yqvz14ZmX%2BKXrJNo%2BNgp0caJN7XxEpEjIunVIo%3D; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; TS010a0d4d030=0169fc3859c8a1694c718dd4c9cbc5f955a0e6e3888514ce92d8f852fbf8de5ee327208d910c0444ad93b2f86eb1189e96dfcb973d",
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

HEADER:ALGORITHM & TOKEN TYPE
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "token-signing-keypair"
}

PAYLOAD:DATA
{
  "SSO_CUST_BG": {
    "session_state": "47762a5b-8ecb-4c18-a5ac-463c29db0022|1669398792568",
    "sub": "U_f420aca8-f693-4c15-b923-755f9577e200"
  }
}

VERIFY SIGNATURE
SASHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
{
  "e": "AQAB",
  "kty": "RSA",
  "n": "ApmXRtqOGJPJrzaNXFVU6tzqJ5V9qEx-JoYYGUMxZDGThbiWueKP5ktOsTU5fBKvM23EmEWyyffB-I1lxftOZCy-Jl2ubLWqHRG6sjVMYTaL6qJ0osNAZ-k5ALrI1xj0IiGZUQr2elIp0Gj94ferSh-MazUHw8YP2bnxzcCL1wyLH3jGq6TALMTJFPobCO_HPT_SZC_tyQ7kQW4cSOONIuuF4j8LUMIUcAQuUPL_DEwwqbXYHI7CRdqAMPcn_q1KHPgXl1VhMlcualKfA9cDXY_WstVp9UK6y-7JMRTVHna0nkRft3BgH_3fBk-e6j_GRyLF0GJHc-UcZyIck1b9U-PHYPB9GGU"
}
)
