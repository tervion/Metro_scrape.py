#SELF NOTE: Types of tokens - Id & Access
#SELF NOTE: Extract token data tool: https://jwt.io

curl 'https://idam.metro.bg/web/authc/authenticate' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H $'Cookie: TSbcb913d5078=08a625aae3ab20003e73c4fd648aa67ee379b63ea1fabd45902d8764b9cd7a6b291685a5d339e0ae08d47f558a185801eda3150925464713021cdf27ac72259085ddb7a53d1323d41f55f665f84564fb914bdac942cd27498bdd97ded07913599164c27a36f34f489a0e0abe5a179cd37d46a3572123e6949a3d125fed85963f1a2194e8606c61c4481fc09ba93eb8f5f2b704499569b14657c733099a20b2f664c8ece673f13f6dbbe20b0ab3659ead880ee0e5a2c546172a422f4b1551e3ad7998b98f2f3435124624774c5537fd10a017d1aaee5b6452e3847527e3462b6ac89c4c08ec06183023f4c310a2a4596303045d1b7cffed6c6859c67f4adb0bfc39ae55e93c6c3a5c503ec245e279bcefdef329a189d8f941d70c793e51de541df5b76476abd8d9a8fba1e9f216a3c1b13bda6b209f259f97983cd6a3586f371e28d68d2b10a7eae6c511dcadcd674e8df56919a76626896f1ef63debd1607c41bc684edd2f0d0c8126ebffbc5819f2c587f89f9b605c753330bfcf697f95b90856b0ccf4db926f04; TS00000000076=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d09d000db00110cbd517c033f9e00a766304105770d9e5617ff2b82418778c303e6901cab617d880134f21af992c52bd0848eabaac4e67f2d467382b45f5b2bcd3c24a73750494ea0de38f9862100359296e051ed62fde2651e4a2498cb9a312f9aabd1ddbeb8b7dea5e65a7e972050222203e70a2376a422121219b4133e940ff4bb84c6ccd36982ca59d8488247d47bd07205a470e14aad82592ffbc08d0aa5f457152dae9b17bdfcb32f58eaf5fd5d49d12404a1b64bb2ecd2415db00b01bfff8c890c93ee452fcb4da06f70514f2f7ad621; TSPD_101_DID=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d0638000196598a6788f820190fd91126bd4561c594ef755e85f5172c6ea635a2f76f666492ff65060daba3d822cc765a8bb390376693b6754cc759; BIGipServeridam.metrosystems.net-80=\u00217fsxS8fkT+qSuQxlllsv0yPj1IQ7JOUaBQydVbRGSBx/xQL5PSC8YRrhQ9xlYvGEIElTtaZkFawfJeY=; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; barrier=ARFCzCofonmfhkeucC99NXBklTCbhmmBEKpIfLkg6ttKpzJzMME3U2B0YnciQn513eazXeCCeX/vhXRUWFgSLjlSrVW4RagJN80dM6Lu82EtpWamHudu7uE18pk=; TSbcb913d5029=08a625aae3ab28004afb46397463362b9f9eb8775d7ab74376c8aa0ef56d5f4a7274ec113f0566c968f054ad818055dc; TS7a8c3458027=08a625aae3ab200064365697b73c5e5f7e0d285f4b43bbec1b16f9e4b7ba7fd88adf26d5f8a5bb5108905514e411300033fae4ebbb2a8b760474d894f8725925896c0cf7269a4cc221c9cf90585b03b68800c9294f3321d827000e8baa023fb6; _dd_s=rum=1&id=eee04a66-6cf6-4e1a-843c-972dcf235171&created=1668201465597&expire=1668202415769' \
  -H 'DR-Trace-ID: idam-trace-id' \
  -H 'Origin: https://idam.metro.bg' \
  -H 'Referer: https://idam.metro.bg/web/Signin?scope=openid+clnt%3DBTEX&locale_id=bg-BG&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token+id_token&nonce=9849d97781d64d8eb2768e792769f202&state=fc764b0c9c404b96909b551ae5c2b4e2' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'X-Security-Request: required' \
  -H 'sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw 'user_id=asd&password=asd&user_type=CUST&client_id=BTEX&response_type=token+id_token&country_code=BG&locale_id=bg-BG&realm_id=SSO_CUST_BG&account_id=&redirect_url=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&state=fc764b0c9c404b96909b551ae5c2b4e2&nonce=9849d97781d64d8eb2768e792769f202&scope=openid+clnt%3DBTEX&code_challenge=&code_challenge_method=' \

#================================================================================================#

url = "https://idam.metro.bg/web/authc/authenticate"

querystring = {"onComplete":"gifebb6lcz","ajaxAction":"0501000201","time":"1668201909968"}

payload = ""
headers = {
    "cookie": "TSPD_BDR=08a625aae3ab20005addbe5c693ec25927785dbb96aa7eb5aba12a76e5fe57150ce1e5421d3e145e0805de64a70a40000283d5703ada65b03d183e24d9d71c21f3984a9ea02919e1dc80c862c0ca45d06731d106cacdddc729c124255b6ac8de1eef3a4099e92f252613156e981b8be6; TSbcb913d5029=08a625aae3ab28008620521277008b851fdcbb8cb30abf655340f501b1a5e0c88ecc6f9076797c0b8c59788323b4acc7; TSbcb913d5078=08a625aae3ab20009c9760a81d1fca978d58eec422fe667814e95f6f0e48a9f0ff7aaa53c6f38756089b00508c1860013d19beb755ff58060d3c2313dfec912291f37720fbbbba848060057788bd68f539c184298395b626e16fa5ecfdd5002e770cf19a68d0c16846de5dfcea7ea45fd6c6f94466a5e166c61b581b8e746799b5fc7ed39cd2837cfa53639bed79cfe36bb861f3f14b58fd60050ec97aaa50556bcde33cec8c6f71eeb4351b2d5f88e8d33f2acdb93b1c61d8b3a2fe3a80eeab93de779d4afaa2e4178f8c187476b39c1d21453c11837763a1b55ac1566abb567ae50bfd40440a67e815ce583647c1d690b68c6e3adc40baf156a6b1d015a49d1a965b9599371e841458a71b5add3011ec9de30fa88dc6b7b5116a98854176b1fecbddaef04a8c273a87b641f79faf91f745c129c739f16c9b64d3a1552370be042518351a6d8068d6a3ea4874b0a7053de9a4d41c6eef0d5978622be63827c89d69459d7ce753b7eff1faa29c924703a17177a1bc60d8e35bce4c38dda4b0a5d8dc8d9d2d0e3a4477ace29eed12d023; TS7a8c3458027=08a625aae3ab20000cc300cab4a1596c954122375f8b1736569d2a955ff144f4189a367934fec95908e713480311300083b25ffe037d56ff9de30bf095073d78bf031719687917c3ac5e20e7ae16e060bd98ec8f28528bf6e0d7a37fdbcb0806; BIGipServeridam.metrosystems.net-80=!NXSJTdtgHVWcR8HUzUGSRTsG4v6oUb8lOuo1eqqq6yqvz14ZmX%2BKXrJNo%2BNgp0caJN7XxEpEjIunVIo%3D; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; TS010a0d4d030=0169fc3859c8a1694c718dd4c9cbc5f955a0e6e3888514ce92d8f852fbf8de5ee327208d910c0444ad93b2f86eb1189e96dfcb973d",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "TSPD_BDR=08a625aae3ab2000f9a2fa12efbb2079e884c0df28177ef8ac4f4692f7ea03f2ee89af41d6eeb8e4083e8d9c420a4000ab0af90e83a1f193410fde3f56f5f9f147599b94e1a913deda976941e601750cf96440df48b87ac22c6610445f57eb8bdbb589c1263a1f269e18350f7c84c3a5; TS00000000076=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d09d000db00110cbd517c033f9e00a766304105770d9e5617ff2b82418778c303e6901cab617d880134f21af992c52bd0848eabaac4e67f2d467382b45f5b2bcd3c24a73750494ea0de38f9862100359296e051ed62fde2651e4a2498cb9a312f9aabd1ddbeb8b7dea5e65a7e972050222203e70a2376a422121219b4133e940ff4bb84c6ccd36982ca59d8488247d47bd07205a470e14aad82592ffbc08d0aa5f457152dae9b17bdfcb32f58eaf5fd5d49d12404a1b64bb2ecd2415db00b01bfff8c890c93ee452fcb4da06f70514f2f7ad621; TSPD_101_DID=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d0638000196598a6788f820190fd91126bd4561c594ef755e85f5172c6ea635a2f76f666492ff65060daba3d822cc765a8bb390376693b6754cc759; BIGipServeridam.metrosystems.net-80=\u00217fsxS8fkT+qSuQxlllsv0yPj1IQ7JOUaBQydVbRGSBx/xQL5PSC8YRrhQ9xlYvGEIElTtaZkFawfJeY=; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; barrier=ARFCzCofonmfhkeucC99NXBklTCbhmmBEKpIfLkg6ttKpzJzMME3U2B0YnciQn513eazXeCCeX/vhXRUWFgSLjlSrVW4RagJN80dM6Lu82EtpWamHudu7uE18pk=; TSbcb913d5029=08a625aae3ab28003ab54447159417f795501e7e3b38765ace62e8be9aae5206b32485c88b1af3f3a38634803b255256; _dd_s=rum=1&id=eee04a66-6cf6-4e1a-843c-972dcf235171&created=1668201465597&expire=1668202809740; TSbcb913d5078=08a625aae3ab2000d1c27c14089e42dd23a8229d4d548f4ebe82d0a1ca4edb770755412a1217a1a108596b1fa718500190060bce427e6acf44d2a6614437391c0b541fdebe8d9e729d99a7d540a03490d02aa5149621b290e2146bfb9e90657b539472cec1140f568ab913aae257dc8f5cb941bde2f347bad43d3e5436c72b0a17012be32c9ace4589fa2a9392a8cb691d5d0f1ea81eddecab14104be830f60eee1399fc7172c2ee1a47aff7d2caa0daaa5398a076adb02ed63f883a95af50dbc8a9bcd0c0028f097b87e0e70cfb11538eda73aa453c5618d30b5bfbeb3f00e5cd6d50316bb90b736c5263ee29bee8981549fa025acdd23df775f5dac3a2fff262a2423a4dc63f9e9ae24d15a0265eb87d97f86b58bf0b5527cdacf009d3636861b3a8fe46c17ee9c6866cff201da95d905586832b5ce7dd60219827307e4effa3672414286f526f88227f4589ab4af2c0a8e9721b8da1db0836c66c57aa7ff13b9bf05e6eb7b80b3413944a51d2730b214d33755a0848a06a743900f8b8f629; TS7a8c3458027=08a625aae3ab20008896b0f90872c871557013151f12b6e3aa4d05c7cbcb7a52276fb71152716d4308b875e1231130001fbcb2b88327be3780c03c867229758121f06e8ef79cf8a9e2c6689ed28516e9e196e75a620a1d8d3c7626b4db87767d",
    "Referer": "https://idam.metro.bg/web/Signin?scope=openid+clnt%3DBTEX&locale_id=bg-BG&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token+id_token&nonce=9849d97781d64d8eb2768e792769f202&state=fc764b0c9c404b96909b551ae5c2b4e2",
    "Sec-Fetch-Dest": "iframe",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "sec-ch-ua": ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": ""Linux""
}

import http.client

conn = http.client.HTTPSConnection("idam.metro.bg")

payload = ""

headers = {
    'cookie': "TSPD_BDR=08a625aae3ab20005addbe5c693ec25927785dbb96aa7eb5aba12a76e5fe57150ce1e5421d3e145e0805de64a70a40000283d5703ada65b03d183e24d9d71c21f3984a9ea02919e1dc80c862c0ca45d06731d106cacdddc729c124255b6ac8de1eef3a4099e92f252613156e981b8be6; TSbcb913d5029=08a625aae3ab28008620521277008b851fdcbb8cb30abf655340f501b1a5e0c88ecc6f9076797c0b8c59788323b4acc7; TSbcb913d5078=08a625aae3ab20009c9760a81d1fca978d58eec422fe667814e95f6f0e48a9f0ff7aaa53c6f38756089b00508c1860013d19beb755ff58060d3c2313dfec912291f37720fbbbba848060057788bd68f539c184298395b626e16fa5ecfdd5002e770cf19a68d0c16846de5dfcea7ea45fd6c6f94466a5e166c61b581b8e746799b5fc7ed39cd2837cfa53639bed79cfe36bb861f3f14b58fd60050ec97aaa50556bcde33cec8c6f71eeb4351b2d5f88e8d33f2acdb93b1c61d8b3a2fe3a80eeab93de779d4afaa2e4178f8c187476b39c1d21453c11837763a1b55ac1566abb567ae50bfd40440a67e815ce583647c1d690b68c6e3adc40baf156a6b1d015a49d1a965b9599371e841458a71b5add3011ec9de30fa88dc6b7b5116a98854176b1fecbddaef04a8c273a87b641f79faf91f745c129c739f16c9b64d3a1552370be042518351a6d8068d6a3ea4874b0a7053de9a4d41c6eef0d5978622be63827c89d69459d7ce753b7eff1faa29c924703a17177a1bc60d8e35bce4c38dda4b0a5d8dc8d9d2d0e3a4477ace29eed12d023; TS7a8c3458027=08a625aae3ab20000cc300cab4a1596c954122375f8b1736569d2a955ff144f4189a367934fec95908e713480311300083b25ffe037d56ff9de30bf095073d78bf031719687917c3ac5e20e7ae16e060bd98ec8f28528bf6e0d7a37fdbcb0806; BIGipServeridam.metrosystems.net-80=!NXSJTdtgHVWcR8HUzUGSRTsG4v6oUb8lOuo1eqqq6yqvz14ZmX%2BKXrJNo%2BNgp0caJN7XxEpEjIunVIo%3D; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; TS010a0d4d030=0169fc3859c8a1694c718dd4c9cbc5f955a0e6e3888514ce92d8f852fbf8de5ee327208d910c0444ad93b2f86eb1189e96dfcb973d",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'Accept-Language': "en-US,en;q=0.9",
    'Connection': "keep-alive",
    'Cookie': "TSPD_BDR=08a625aae3ab2000f9a2fa12efbb2079e884c0df28177ef8ac4f4692f7ea03f2ee89af41d6eeb8e4083e8d9c420a4000ab0af90e83a1f193410fde3f56f5f9f147599b94e1a913deda976941e601750cf96440df48b87ac22c6610445f57eb8bdbb589c1263a1f269e18350f7c84c3a5; TS00000000076=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d09d000db00110cbd517c033f9e00a766304105770d9e5617ff2b82418778c303e6901cab617d880134f21af992c52bd0848eabaac4e67f2d467382b45f5b2bcd3c24a73750494ea0de38f9862100359296e051ed62fde2651e4a2498cb9a312f9aabd1ddbeb8b7dea5e65a7e972050222203e70a2376a422121219b4133e940ff4bb84c6ccd36982ca59d8488247d47bd07205a470e14aad82592ffbc08d0aa5f457152dae9b17bdfcb32f58eaf5fd5d49d12404a1b64bb2ecd2415db00b01bfff8c890c93ee452fcb4da06f70514f2f7ad621; TSPD_101_DID=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d0638000196598a6788f820190fd91126bd4561c594ef755e85f5172c6ea635a2f76f666492ff65060daba3d822cc765a8bb390376693b6754cc759; BIGipServeridam.metrosystems.net-80=\u00217fsxS8fkT+qSuQxlllsv0yPj1IQ7JOUaBQydVbRGSBx/xQL5PSC8YRrhQ9xlYvGEIElTtaZkFawfJeY=; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; barrier=ARFCzCofonmfhkeucC99NXBklTCbhmmBEKpIfLkg6ttKpzJzMME3U2B0YnciQn513eazXeCCeX/vhXRUWFgSLjlSrVW4RagJN80dM6Lu82EtpWamHudu7uE18pk=; TSbcb913d5029=08a625aae3ab28003ab54447159417f795501e7e3b38765ace62e8be9aae5206b32485c88b1af3f3a38634803b255256; _dd_s=rum=1&id=eee04a66-6cf6-4e1a-843c-972dcf235171&created=1668201465597&expire=1668202809740; TSbcb913d5078=08a625aae3ab2000d1c27c14089e42dd23a8229d4d548f4ebe82d0a1ca4edb770755412a1217a1a108596b1fa718500190060bce427e6acf44d2a6614437391c0b541fdebe8d9e729d99a7d540a03490d02aa5149621b290e2146bfb9e90657b539472cec1140f568ab913aae257dc8f5cb941bde2f347bad43d3e5436c72b0a17012be32c9ace4589fa2a9392a8cb691d5d0f1ea81eddecab14104be830f60eee1399fc7172c2ee1a47aff7d2caa0daaa5398a076adb02ed63f883a95af50dbc8a9bcd0c0028f097b87e0e70cfb11538eda73aa453c5618d30b5bfbeb3f00e5cd6d50316bb90b736c5263ee29bee8981549fa025acdd23df775f5dac3a2fff262a2423a4dc63f9e9ae24d15a0265eb87d97f86b58bf0b5527cdacf009d3636861b3a8fe46c17ee9c6866cff201da95d905586832b5ce7dd60219827307e4effa3672414286f526f88227f4589ab4af2c0a8e9721b8da1db0836c66c57aa7ff13b9bf05e6eb7b80b3413944a51d2730b214d33755a0848a06a743900f8b8f629; TS7a8c3458027=08a625aae3ab20008896b0f90872c871557013151f12b6e3aa4d05c7cbcb7a52276fb71152716d4308b875e1231130001fbcb2b88327be3780c03c867229758121f06e8ef79cf8a9e2c6689ed28516e9e196e75a620a1d8d3c7626b4db87767d",
    'Referer': "https://idam.metro.bg/web/Signin?scope=openid+clnt%3DBTEX&locale_id=bg-BG&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token+id_token&nonce=9849d97781d64d8eb2768e792769f202&state=fc764b0c9c404b96909b551ae5c2b4e2",
    'Sec-Fetch-Dest': "iframe",
    'Sec-Fetch-Mode': "navigate",
    'Sec-Fetch-Site': "same-origin",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    'sec-ch-ua': ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': ""Linux""
    }

conn.request("GET", "/web/authc/authenticate?onComplete=gifebb6lcz&ajaxAction=0501000201&time=1668201909968", payload, headers)

res = conn.getresponse()
data = res.read()

#================================================================================================#

#2. POST-LOGIN / Acces Token (POST: https://shop.metro.bg/explore.login.v1/auth/loginWithIdamAccessToken?country=BG) DATA:

    #2.1. Insomnia data: 

        #2.1.1. Insomnia data_cURL: 
         https://shop.metro.bg/explore.login.v1/auth/loginWithIdamAccessToken

        #2.1.2. Insomnia data_Referer:
         https://shop.metro.bg/shop/cart?itm_pm=cookie_consent_accept_button

    #2.2 HEADERS:

        #2.2.1. HEADERS_File name:
         /explore.login.v1/auth/loginWithIdamAccessToken

        #2.2.2. HEADERS_Response:

            #2.2.2.1. HEADERS_Response_Compressedjw:
             eNpVUtuSqjoU/CJ3IcLM+KhcQjIEBSKXvExBULkFUZTb1+8wM+fUOQ+pVPVa3b16JecJ5SlgxaFA/mmGa6dA2z/nCbVsgxcQsY2zphEsbA3lWegu2D4LvZaGakl92EHeSokP3yAflKBiUjLnDdH3WsLNO67dOTSzmBrGwp+zEC78gkaedP7mBq8M1FIKgqfQk9i06FCdrOFPP9hO9CR6LDELV9cpGDrYBOR/eIEUN8Dd2XAwWWfEtvI9kYYuq0xsW5ScTNjFa2fR/L1ZR+v90QYUe8bWh8VQZIEjpRtUf/tXyPJ0OC04A6aagm1ONYE3TwYb1ItZGSxbBrmzZhuvT8NgijTYRRpaM6D+1EpjwLoxYn034BJucBnPDhG8Ylx4OePeLZXHikbokIVrsQ/0yzN/ehqvjuU8YHIwnfi2o8Hwb37hIyXCk4BApuH4y/P+0e6zZY9N/YOLLKJ/+52FB1ycOTFoz7hTL5koNzsmn8ROnTblmfBxWiqrx7T4b42KD1JXi24SijlKQ3bK63jQd7MzY5GtWt5RYUIPk1g+6IaCdYFPQ5FEjnjzwIgjr4blbXTKWMGEyc7MBBeqF/cP83MbFnpxjebiRfSz/xpVcH5YbDxxP309XdP8pK7zcRl2CuBN7/sJB5O6ylHgFxfiul/BV8PeQy0n7wfpVE37lHQPQuvevOSuGxFnlQC9vbo7Jne06PD12H7JzR1JdkR4MstvB2Ub8sp+HxU95d1Ru+dFUp/iKsWJPfY7727uzlt716vHIXipPqq319QG3fPZTcf947aKWuMCrHP6YZ2O013+iAPnqukJOZ43pjdQ67IpyTWP5FuTHladYgDFo2E1Iu2+qR4t1C/eJZNwEXfI6uXQ8PqefbaIDi8D5R+fxsGLLPAc3CbN5maINRrsVm9vdCVdDw6HtbHJ6QzQ43bBRiO3uASZa1//Ak8RT5w=

                #2.2.2.1.1. HEADERS_Response_Compressedjw_DECODED_DATA:

                    #2.2.2.1.1.1. HEADERS_Response_Compressedjw_DECODED_DATA-HEADER:
                     {
                     "alg": "HS256"
                     }

                    #2.2.2.1.1.2. HEADERS_Response_Compressedjw_DECODED_DATA-PAYLOAD:
                     {}

                    #2.2.2.1.1.3. HEADERS_Response_Compressedjw_DECODED_DATA-VERIFY_SIGNATURE:
                     HMACSHA256(
                      base64UrlEncode(header) + "." +
                      base64UrlEncode(payload),
                      your-256-bit-secret)
                      secret base64 encoded #CHECKED

                    #2.2.2.1.1.4. HEADERS_Response_Compressedjw_DECODED_DATA-STATUS:
                     signature verified

            #2.2.2.2. HEADERS_Response_Cookie:
	         selectedLocale_BG=bg-BG; BIGipServerbetty.metrosystems.net-80=!DSVtpDmzT3BEq7Nlllsv0yPj1IQ7JKRF69YsVoXogC8V6zL3i62TkGZEpi5ltQ+WgE5zLUvXvFxPaoI=; anonymousUserId=0BA10A1C-D0C0-4F87-A007-9F5BE6E9C723; idamUserIdToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IktfYWE1NTAxNWEtMjA2YS0xMWVkLTk4ZDUtZTJjYzEyYjBkYzUwIn0.eyJleHAiOjE2NjgxNzg1NjksImlhdCI6MTY2ODE3Njc2OSwiYXVkIjoiQlRFWCIsInNlc3Npb25fc3RhdGUiOiJKeVd3WlhnVFFuUF83YTQ5bjMwYTQ3dktDVWpKMXcyVmxTbndZcFgxZ0tJLlBhcGRzY0lVIiwiaXNzIjoiaHR0cHM6Ly9pZGFtLm1ldHJvLmJnI…%22}; UserSettings=SelectedStore=1b1fc6ac-2ad6-4243-806e-a4a28c96dff4; _ts=l+ec5497ffaf02443490d6cc85a99a7380; allowedCookieCategories=necessary%7Cfunctional%7Cperformance%7Cpromotional%7CUncategorized; tsession={%22sessionId%22:%2236704EA8-DA97-466C-9A97-1FEAD5F41E7B%22%2C%22timestamp%22:1668176773000}; abGroups={%22CI_ARTICLE_BANNER%22:%22B%22%2C%22SD_NEW_SUGGESTIONS%22:%22A%22%2C%22QUICKENTRY_SEARCH_BACKEND%22:%22A%22%2C%22CI_USE_SEARCH_INSTEAD_OF_SIMPLESEARCH%22:%22A%22%2C%22SD_USE_SOLR_ALT%22:%22A%22}

                #2.2.2.2.1. HEADERS_Response_Cookie_DECODED_DATA:

                    #2.2.2.2.1.1. HEADERS_Response_Cookie_DECODED_DATA-HEADER:
                     {
                     "alg": "HS256"
                     }
                     
                    #2.2.2.2.1.2. HEADERS_Response_Cookie_DECODED_DATA-PAYLOAD:
                     "��k�̬���"

                    #2.2.2.2.1.3. HEADERS_Response_Cookie_DECODED_DATA-VERIFY_SIGNATURE:
                     HMACSHA256(
                      base64UrlEncode(header) + "." +
                      base64UrlEncode(payload),
                      your-256-bit-secret
                      secret base64 encoded) #UNCHECKED

                    #2.2.2.2.1.4. HEADERS_Response_Cookie_DECODED_DATA-STATUS:
                     signature verified

        #2.2.3. HEADERS_Request:

            #2.2.3.1. HEADERS_Rquest_Origin:
             https://shop.metro.bg

            #2.2.3.2. HEADERS_Rquest_Referer:
             https://shop.metro.bg/shop/authLoading

    #2.2. COOKIES

        #2.2.1. COOKIES_Request:

            #2.2.1.1. COOKIES_Request_compressedJWT	
             eNpVUtuSqjoU/CKmuOrwqFyDEi5CgLycMkEFBAZF5PL1O8zMPnXOQypVndXdq9fKZXYKYtHSK51TvAABlo76cZmdjkruCjpUggJOQXnUnCJPghXb50nY4USp8An0oOn48wlswL3nkyZ/Y76zqVi/4kY4nC0lQY3ydEW68pc8ASu/xGnIX765aMitmicWejE9ns5Mp8F6JICfekudccxqbNZLowjEGnvQouh/eOnIAXL7iwHdSMijo13sI37s87vpHm0cxSboMwGumr837XG9948WdkNDPYFyLHMEeSI59bf/3bFDHcwrTi1TIZZaYI3h7YuC1nmzXimoOgoaKFApfJMEzakG+lRzBGopP2+VMbq6Mbn6bnQrILlVtsCI8cpp5RW0Cb+ION1x6nh5IrB5OL8886emDetMLBAV0Rw3ao/R+G9+5sOfmWdkIREn0y8v/Kv9ztc5tvUPzrKwevU7S4Madpazgd+0gfWaCTdmT8WYzRR2pMmZD+ywqPik/O8bZh+kvq+654T1URkirG6Tp+8WuOxEGBnrHmXK9NwoEz3dkF3dlVxtLM8pZDtHRpaGNai+JlhlshtRES50hFU8XYMPon/9syWjzxVx1OqnW1w1J2d5kmbK1OvLiT2TXAMfB1f7gXEo9KpvAny/TT196bfwtADfe2/DIejh5S2q6gWYO5IZ3TXPvXPNAVt6xIFZpkOyzzQxjF79UB8OWPb8MbgRQebEfHMxdra8Tf0+P4aRRvBQSKjlT89AHy+JO4p0QA/luZfsXi8vj+FQmIZren68uT1fLpoqVR18snMO0yjIuPgU8eGoDcXTL+7roigHc4o4o4VplWEa4s+W1t1mQd5xbI9bOsm9Pugxl2VI2Hzqlg3H8dm3fNdI8xehsnHWoKLjKeDi8jgInPbKZfMxPzPuXN7T0zRug+7lRLCwI/OdclaZEj74A0xTTVk=

                #2.2.1.1.1. COOKIES_Request_compressedJWT_DECODED_DATA

                    #2.2.1.1.1. COOKIES_Request_compressedJWT_DECODED_DATA-HEADER:
                     {
                     "alg": "HS256"
                     }

                    #2.2.1.1.1. COOKIES_Request_compressedJWT_DECODED_DATA-PAYLOAD:
                     {}

                    #2.2.1.1.1. COOKIES_Request_compressedJWT_DECODED_DATA-VERIFY_SIGNATURE:
                     HMACSHA256(
                     	base64UrlEncode(header) + "." +
                     	base64UrlEncode(payload),
                     your-256-bit-secret)
                     secret base64 encoded #UNCHECKED
                     #2.2.1.1.1. COOKIES_Request_compressedJWT_DECODED_DATA-STATUS:
                     signature verified

    #2.3. REQUEST

        #2.3. REQUEST_Request_payload
         eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IktfYWE1NTAxNWEtMjA2YS0xMWVkLTk4ZDUtZTJjYzEyYjBkYzUwIn0.eyJrZXlNYXAiOnsiY2RtIjp7InBlcnNvbiI6IjRlYWViOTEwLTI0M2EtMTFlZC1iYTY4LTMxNWMxYjczMjFiZiJ9fSwiZW1haWwiOiJvZmZpY2VAdGVydmlvbi5iZyIsImFjY291bnRDb250ZXh0IjoiIiwiY291bnRyeSI6IkJHIiwibG9jYWxlIjoiYmctQkciLCJpYXQiOjE2NjgxNzY3NjksImF1ZCI6IkJURVgiLCJ1c2VyVHlwZSI6IkNVU1QiLCJpc3MiOiJodHRwczovL2lkYW0ubWV0cm8uYmciLCJleHAiOjE2NjgxODAzNjksImF1dGhvcml6YXRpb24iOltdLCJyZWFsbSI6IlNTT19DVVNUX0JHIiwic3ViIjoiVV9mNDIwYWNhOC1mNjkzLTRjMTUtYjkyMy03NTVmOTU3N2UyMDAiLCJ1cG4iOiJvZmZpY2VAdGVydmlvbi5iZyJ9.AKg-9BL-pPR--ZDHtB4qeMnu4BTsVMW5ywyLOq_c4Dnlyic1le-3Jphbk4BxsNyf4LA6EXrOBJwa5Yku3QHy-ruEVAApzEdzk1GotSh6tO57EKF-8_vKR5yfGwkfotpGejnWE-IWu5iynqWqv1aV3hSi4rD8b-ZqWUoO-SQrs8FtdcG_MBlz44mXw-nL8n1VYm-PsL_ODizskeKKIR81oVWewVD-vlsK55TOEx4tLw0XKcVIi8iYlPr2FMRkkaNDbwLCY80O_7oVI9LbDdRglDW-l-VlNTILSsBOzFuy0ko6rp9eRiqXhKCYaOQAsI5BWS-BV-wNsYrw2NS9Ps2BLG7DNPn_H1U

        #2.3.1. REQUEST_Request_payload_DECODED_DATA

            #2.3.1.1. REQUEST_Request_payload_DECODED_DATA-HEADER:
             {
             "alg": "RS256",
             "typ": "JWT",
            "kid": "K_aa55015a-206a-11ed-98d5-e2cc12b0dc50"
             }
    
            #2.3.1.2. REQUEST_Request_payload_DECODED_DATA-PAYLOAD
             {
             "keyMap": {
             "cdm": {
             "person": "4eaeb910-243a-11ed-ba68-315c1b7321bf"
             }

            #2.3.1.3. REQUEST_Request_payload_DECODED_DATA_VERIFY_SIGNATURE
             RSASHA256(
             	 base64UrlEncode(header) + "." +
             	 base64UrlEncode(payload),
                 {
             	 "e": "AQAB",
             	 "kty": "RSA",
             	 "n": "ApmXRtqOGJPJrzaNXFVU6tzqJ5V9qEx-JoYYGUMxZDGThbiWueKP5ktOsTU5fBKvM23EmEWyyffB-I1lxftOZCy-Jl2ubLWqHRG6sjVMYTaL6qJ0osNAZ-k5ALrI1xj0IiGZUQr2elIp0Gj94ferSh-MazUHw8YP2bnxzcCL1wyLH3jGq6TALMTJFPobCO_HPT_SZC_tyQ7kQW4cSOONIuuF4j8LUMIUcAQuUPL_DEwwqbXYHI7CRdqAMPcn_q1KHPgXl1VhMlcualKfA9cDXY_WstVp9UK6y-7JMRTVHna0nkRft3BgH_3fBk-e6j_GRyLF0GJHc-UcZyIck1b9U-PHYPB9GGU"
                 }                          
             	 )

            #2.3.1.4. REQUEST_Request_payload_DECODED_DATA-STATUS:
             signature verified

    #2.4. RESPONSE

        #2.4.1. JWT	
         eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJJc3N1ZXIiLCJhdWQiOiJBdWRpZW5jZSIsImp0aSI6Imw4Vkc0azhnTDBCamFqMlQzWFdYZEEiLCJzdWIiOiJiZXR0eSIsImVudGl0bGVtZW50cyI6ImZDT1IiLCJzdG9yZUVudHMiOm51bGwsInVTdG9yZUVudHMiOiJ4QVMseENMT1dTLHhBT0wsdkFMLHZTUFIsY1NDT1IsY1NDT1csZlBPLGZMRE9SIiwidVN0b3JlcyI6IkJHRDIyIiwicGF5bG9hZCI6IntcInJvbGVcIjpcImN1c3RvbWVyXCIsXCJ1cG5cIjpcIjEwMDExMDAwMjI3MjYzNTVcIixcImNhcmRob2xkZXJOdW1iZXJcIjpcIjFcIixcInRlY2hVc2VyUm9sZVwiOm51bGwsXCJ0aWVyTGV2ZWxcIjpcIjRcIixcImNvdW50cnlcIjpcIkJHXCJ9IiwicmVmcmVzaEZvcmNlZCI6ZmFsc2UsInNpbmdsZVNpZ25PbiI6ZmFsc2UsInZhbGlkdW50aWwiOjE2NjgxODAzNzM3MjksImV4cCI6MTY2ODE4MDM3MywiaXNzdWVEYXRlIjoxNjY4MTc2NzczNzI5fQ.cShLIiDigXziuTDeSux5GerHcxUmSbutQFFKZQN8fwA4GmnvSSamGy5-hJVSifTQQ_V_nc7WChT7O0UkyBbTsrTZlvFfhQQXTN-aGDpgQAc2sZisMgPp_2nqJ0LXTmaz26O49WmkL7x4DbmsPCqhialUYkbMaLxvARqFAe9LAv5PwVu5SJl9gbLGsttsyPBro-XpEfGHeb8HUPyq28YVNgCDaTPe3FRwZHf3jTghX2onbO-s4EG4RZWkxJCq3krpIDfRfd0MiYsJHv2WERvvcKpJZwuEJh8KEORXHGtwQnbdznwYCZVA-66Z-0gONmIlE3hZzGJrofMEn2pMjGdQLg

            #2.4.1.1. JWT_DECODED_DATA:

                #2.4.1.1.1. JWT_DECODED_DATA-HEADER:
                 {
                "alg": "RS256"
                 }

                 #2.4.1.1.2. JWT_DECODED_DATA-PAYLOAD:
                 {
                 "iss": "Issuer",
                 "aud": "Audience",
                 "jti": "ZCa9TIU7ohmFiwprl6xsXQ",
                 "sub": "betty",
                 "entitlements": "fCOR",
                 "storeEnts": null,
                 "uStoreEnts": "xAS,xCLOWS,xAOL,vAL,vSPR,cSCOR,cSCOW,fPO,fLDOR",
                 "uStores": "BGD22",
                 "payload": "{\"role\":\"customer\",\"upn\":\"1001100022726355\",\"cardholderNumber\":\"1\",\"techUserRole\":null,\"tierLevel\":\"4\",\"country\":\"BG\"}",
                 "refreshForced": false,
                 "singleSignOn": false,
                 "validuntil": 1668171098428,
                 "exp": 1668171098,
                 "issueDate": 1668167498428
                 }

                 #2.4.1.1.3. JJWT_DECODED_DATA-VERIFY_SIGNATURE:
                 RSASHA256(
                  base64UrlEncode(header) + "." +
                  base64UrlEncode(payload),)

                 {
                 "e": "AQAB",
                 "kty": "RSA",
                 "n": "ApmXRtqOGJPJrzaNXFVU6tzqJ5V9qEx-JoYYGUMxZDGThbiWueKP5ktOsTU5fBKvM23EmEWyyffB-I1lxftOZCy-Jl2ubLWqHRG6sjVMYTaL6qJ0osNAZ-k5ALrI1xj0IiGZUQr2elIp0Gj94ferSh-MazUHw8YP2bnxzcCL1wyLH3jGq6TALMTJFPobCO_HPT_SZC_tyQ7kQW4cSOONIuuF4j8LUMIUcAQuUPL_DEwwqbXYHI7CRdqAMPcn_q1KHPgXl1VhMlcualKfA9cDXY_WstVp9UK6y-7JMRTVHna0nkRft3BgH_3fBk-e6j_GRyLF0GJHc-UcZyIck1b9U-PHYPB9GGU"
                 }

                #2.4.1.1.4. JWT_decoded_DATA-STATUS: 
                 invalid signature

#================================================================================================#

#3. PRE-LOGIN / TOKEN ID (GET https://idam.metro.bg/web/Signin) DATA:

    #3.1. HEADERS

        #3.1.1. HEADERS_GET

        	#3.1.1.1. HEADERS_GET_Filename:
        	 /explore.login.v1/auth/singleSignOn

            #3.1.1.2. HEADERS_GET_URL:
             https://idam.metro.bg/web/Signin?scope=openid clnt=BTEX&locale_id=bg-BG&redirect_uri=https://shop.metro.bg/shop/cart?idamRedirect=1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token id_token&nonce=7f230be47a4743049f5e43c01159d12f&state=7a355ef3bc48458f8a866f1fa9070297

            #3.1.1.3. HEADERS_GET_scope:
             openid clnt=BTEX

            #3.1.1.4. HEADERS_GET_locale_id:
             bg-BG

            #3.1.1.5. HEADERS_GET_redirect_uri:
	         https://shop.metro.bg/shop/cart?idamRedirect=1

	        #3.1.1.6. HEADERS_GET_client_id:
	         BTEX

	        #3.1.1.7. HEADERS_GET_country_code:
	         BG

	        #3.1.1.8. HEADERS_GET_realm_id:
	         SSO_CUST_BG

	        #3.1.1.9. HEADERS_GET_realm_id:
	         SSO_CUST_BG

	        #3.1.1.10. HEADERS_GET_user_type:
	         CUST

	        #3.1.1.11. HEADERS_GET_DR-Trace-ID:
	         idam-trace-id

	        #3.1.1.12. HEADERS_GET_response_type:
	         token id_token #BINGO

	        #3.1.1.13. HEADERS_GET_nonce:
	         7f230be47a4743049f5e43c01159d12f

	        #3.1.1.14. HEADERS_GET_state
	         7a355ef3bc48458f8a866f1fa9070297

	    #3.1.2. HEADERS_Responce
	     #SKIP

	    #3.1.3. HEADERS_Request

	        #3.1.3.1. HEADERS_Responce_Cookie
	         TSbcb913d5029=08a625aae3ab2800cee9585f1880937c3e3e4f724bc9af5a62294fd6e54e8fa9d11e6bcade36f776a7cb12452cbc1332; TSbcb913d5078=08a625aae3ab200053e67e3b742d6c6bd926bbf9e7b1b04a25e5d7a473a0e268184ba77d7d1361180898b1bcee185801facfaf2841cb2bd4eb2b68bffa1fa8ec77155bffa1a244c975eb19697a5b2ef032492ddb6fa4c39cb2e8bc9d799341de61ccb22b8aea9fa53124c3e4b2d3643ab7aa4c5e394b1ccb6bb103badd56807da5f5faa1cb04204b5a92fd054dd91d11a95acf657ab1e8b46c9dcd215d9124758d9750edc4930aff8ad028740c0014de9da4a1af74d10b1b7b7929fdc6c8ef4ac5…a3; TSPD_101_DID=08a625aae3ab280025feb50a5ca0b69f1c3a04eb171a8681f9e1b7a3b50435556e19a40db3033d67a8a1ed7bf014bf5b08d25b2ae1063800ebe847966688bafd7f816dc51b5bd67668de11a8ab59ef16a1a57a395a01eb1ac01cd2b29185548745e72a11af66d4b651312cd5cf184feb; BIGipServeridam.metrosystems.net-80=!nOne0SYcLi/1J0Flllsv0yPj1IQ7JGO5NJHi17jkhFeQ7DUcH09Sg9bXNEeRuJWy+a9+mdXnufiogBo=; TS010a0d4d=0179c221a76fa9120bf05c740ccdd9dfd725a5c6ae419e5ed19cbcd2eb330782a6dfb32d82eeb98512e508c552458c7d50400454a0667fcec27979789cc8c0e34c6fa7080c

	            #3.1.3.1.1. HEADERS_Responce_Cookie_DECODED_DATA

	                #3.1.3.1.1.1. HEADERS_Responce_Cookie_DECODED_DATA-HEADER:
	                 {
                     "alg": "HS256"
                     }

                    #3.1.3.1.1.2. HEADERS_Responce_Cookie_DECODED_DATA-PAYLOAD:
                     "��k�̬���"

                    #3.1.3.1.1.3. HEADERS_Responce_Cookie_DECODED_DATA-VERIFY_SIGNATURE:
                     HMACSHA256(
  					 base64UrlEncode(header) + "." +
  					 base64UrlEncode(payload),
  					 your-256-bit-secret)
  					 secret base64 encoded #CHECK

  					#3.1.3.1.1.4. HEADERS_Responce_Cookie_DECODED_DATA-STATUS:
  					 signature verified

  			#3.1.4. HEADERS_Referer:
  			 https://idam.metro.bg/authorize/api/oauth2/authorize?client_id=BTEX&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&response_type=token%20id_token&scope=openid%20clnt%3DBTEX&state=7a355ef3bc48458f8a866f1fa9070297&nonce=7f230be47a4743049f5e43c01159d12f&realm_id=SSO_CUST_BG&country_code=BG&locale_id=bg-BG
    
     #3.2. COOKIES
     #SKIP

     #3.3. REQUEST
     #SKIP

     #3.4. RESPONSE
     #SKIP

#================================================================================================#

#4. PRE-LOGIN / TOKEN ID (GET https://idam.metro.bg/authorize/api/oauth2/authorize) DATA:

    #4.1 HEADERS

        #4.1.1 HEADERS_GET

        	#4.1.1.1 HEADERS_GET_Filename:
        	 /authorize/api/oauth2/authorize

            #4.1.1.2 HEADERS_GET_URL:
             https://idam.metro.bg/authorize/api/oauth2/authorize?client_id=BTEX&redirect_uri=https://shop.metro.bg/shop/cart?idamRedirect=1&response_type=token id_token&scope=openid clnt=BTEX&state=7a355ef3bc48458f8a866f1fa9070297&nonce=7f230be47a4743049f5e43c01159d12f&realm_id=SSO_CUST_BG&country_code=BG&locale_id=bg-BG

            #4.1.1.3. HEADERS_GET_client_id:
	         BTEX

            #4.1.1.4. HEADERS_GET_redirect_uri:
	         https://shop.metro.bg/shop/cart?idamRedirect=1

            #4.1.1.5. HEADERS_GET_response_type:
	         token id_token #BINGO

	        #4.1.1.6. HEADERS_GET_scope:
             openid clnt=BTEX

	        #4.1.1.7. HEADERS_GET_state
	         7a355ef3bc48458f8a866f1fa9070297

	        #4.1.1.8. HEADERS_GET_nonce:
	         7f230be47a4743049f5e43c01159d12f

	        #4.1.1.9. HEADERS_GET_realm_id:
	         SSO_CUST_BG

	        #4.1.1.10. HEADERS_GET_country_code:
	         BG

	        #4.1.1.11. HEADERS_GET_locale_id:
	         bg-BG

	        #4.1.1.12. HEADERS_GET_response_type:
	         token id_token #BINGO

	        #4.1.1.13. HEADERS_GET_nonce:
	         7f230be47a4743049f5e43c01159d12f


	    #4.1.2. HEADERS_Responce
	     #SKIP

	    	#4.1.3. HEADERS_Responce_Dr-Trace-Id:
			 idam-trace-id	

	    #4.1.3. HEADERS_Request

	        #4.1.3.1. HEADERS_Responce_Cookie
	         TSPD_101_RF=deleted; TSbcb913d5029=08a625aae3ab28009dd353a86c318fab861be9a344a1ad74b116a5eaab54cc9111a86b1cd896eec7e16614fac7feec73; TSbcb913d5078=08a625aae3ab200053e67e3b742d6c6bd926bbf9e7b1b04a25e5d7a473a0e268184ba77d7d1361180898b1bcee185801facfaf2841cb2bd4eb2b68bffa1fa8ec77155bffa1a244c975eb19697a5b2ef032492ddb6fa4c39cb2e8bc9d799341de61ccb22b8aea9fa53124c3e4b2d3643ab7aa4c5e394b1ccb6bb103badd56807da5f5faa1cb04204b5a92fd054dd91d11a95acf657ab1e8b46c9dcd215d9124758d9750edc4930aff8ad028740c0014de9da4a1af74d10…a3; TSPD_101_DID=08a625aae3ab280025feb50a5ca0b69f1c3a04eb171a8681f9e1b7a3b50435556e19a40db3033d67a8a1ed7bf014bf5b08d25b2ae1063800ebe847966688bafd7f816dc51b5bd67668de11a8ab59ef16a1a57a395a01eb1ac01cd2b29185548745e72a11af66d4b651312cd5cf184feb; BIGipServeridam.metrosystems.net-80=!nOne0SYcLi/1J0Flllsv0yPj1IQ7JGO5NJHi17jkhFeQ7DUcH09Sg9bXNEeRuJWy+a9+mdXnufiogBo=; TS010a0d4d=0179c221a76fa9120bf05c740ccdd9dfd725a5c6ae419e5ed19cbcd2eb330782a6dfb32d82eeb98512e508c552458c7d50400454a0667fcec27979789cc8c0e34c6fa7080c

	            #4.1.3.1.1 HEADERS_Responce_Cookie_DECODED_DATA

	                #4.1.3.1.1.1. HEADERS_Responce_Cookie_DECODED_DATA-HEADER:
	                 {
                     "alg": "HS256"
                     }

                    #4.1.3.1.1.2. HEADERS_Responce_Cookie_DECODED_DATA-PAYLOAD:
                     "��k�̬���"

                    #4.1.3.1.1.3. HEADERS_Responce_Cookie_DECODED_DATA-VERIFY_SIGNATURE:
                     HMACSHA256(
  					 base64UrlEncode(header) + "." +
  					 base64UrlEncode(payload),
  					 your-256-bit-secret)
  					 secret base64 encoded #UNCHECK

  					#4.1.3.1.1.4. HEADERS_Responce_Cookie_DECODED_DATA-STATUS:
  					 signature verified

  			#4.1.4. HEADERS_Referer:
  			 https://shop.metro.bg/
    
     #3.2. COOKIES
     #SKIP

     #3.3. REQUEST
     #SKIP

     #3.4. RESPONSE
     #SKIp

#================================================================================================#

#5. PRE-LOGIN / TOKEN ID (GET https://idam.metro.bg/authorize/api/oauth2/check_session_iframe) DATA:

    #5.1 HEADERS

        #5.1.1. HEADERS_GET

	    #5.1.2. HEADERS_Responce
	     #SKIP

	    	#4.1.3. HEADERS_Responce_Dr-Trace-Id:
			 idam-trace-id	

	    #5.1.3. HEADERS_Request

	        #5.1.3.1. HEADERS_Responce_Cookie
	         TSPD_101_RF=deleted; TSbcb913d5075=0402b10008a625aae3ab2800f3695b711659b4468f1b4b54fed3673f43649bb62ccea050b49428901158e5a9dd4ab27a4c8977de:08b9ef4b4e032000a03f146eb4e669a9d95f45402ce4ddc62d7087164389accf17d1e1aded42e2bfa00108a625aae3ab2800f3695b711659b4468f1b4b54fed3673f43649bb62ccea050b49428901158e5a9dd4ab27a4c8977de08b9ef4b4e10980064769d4a8a995fff293c0c33033028ec3d89e3e7962776d2e09e13a8a5270a179fc5b2ec5ad788d7a07458ea2b0890dbb5e977d2c8aaf008dfd0b61bb2ba5a8a92861f56a7da29011b1ed19cb7bb7b9bb613fe96b10fae2c…addressHash%22:null%2C%22storeId%22:%2200022%22}; UserSettings=SelectedStore=1b1fc6ac-2ad6-4243-806e-a4a28c96dff4&SelectedAddress=1001100022726355994-ad0532ei; _ts=l+17791e1ce19742bab7596cda02812a84; allowedCookieCategories=necessary%7Cfunctional%7Cperformance%7Cpromotional%7CUncategorized; _gcl_au=1.1.1059589367.1668189201; _ga_4N83E9ZK99=GS1.1.1668199195.2.0.1668199538.60.0.0; _ga=GA1.1.1686404970.1668189201; local_ga_4N83E9ZK99=GS1.1.1668199453.1.1.1668199539.59.0.0; local_ga=GA1.1.1373443744.1668199453

	            #5.1.3.1.1. HEADERS_Responce_Cookie_DECODED_DATA

	                #5.1.3.1.1.1. HEADERS_Responce_Cookie_DECODED_DATA-HEADER:
	                 {
                     "alg": "HS256"
                     }

                    #5.1.3.1.1.2. HEADERS_Responce_Cookie_DECODED_DATA-PAYLOAD:
                     ""

                    #5.1.3.1.1.3. HEADERS_Responce_Cookie_DECODED_DATA-VERIFY_SIGNATURE:
                     HMACSHA256(
  					 base64UrlEncode(header) + "." +
  					 base64UrlEncode(payload),
  					 your-256-bit-secret)
  					 secret base64 encoded #CHECK

  					#5.1.3.1.1.4. HEADERS_Responce_Cookie_DECODED_DATA-STATUS:
  					 invalid signature

  			#5.1.4. HEADERS_Referer:
  			 https://shop.metro.bg/
    
    #3.2. COOKIES
     	
     	#3.2.1. COOKIES_barrier:
     	 ARFCzCqYf9eUx7hLB5d5Yv56VLET5h7JzXNCpUxIUi+2cKVG8mxcV5vZtKmVa3FEtbHTAi2Ew8mXAkPF+jrJbmJze8RGRmltVrR3B381BkbQKYkvHwHLwAhuGnU=

     	#3.2.2. COOKIES_BIGipServeridam.metrosystems.net-80:
     	 !nOne0SYcLi/1J0Flllsv0yPj1IQ7JGO5NJHi17jkhFeQ7DUcH09Sg9bXNEeRuJWy+a9+mdXnufiogBo=

     	#3.2.3. COOKIES_local_ga:
     	 https://idam.metro.bg/authorize/api/oauth2/check_session_iframe

     	#3.2.4. COOKIES_local_ga_4N83E9ZK99:
     	 GS1.1.1668199453.1.1.1668199539.59.0.0

     	#3.2.5. COOKIES_metroIdentity:
     	 eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRva2VuLXNpZ25pbmcta2V5cGFpciJ9.eyJTU09fQ1VTVF9CRyI6eyJzZXNzaW9uX3N0YXRlIjoiNDc3NjJhNWItOGVjYi00YzE4LWE1YWMtNDYzYzI5ZGIwMDIyfDE2NjkzOTg3OTI1NjgiLCJzdWIiOiJVX2Y0MjBhY2E4LWY2OTMtNGMxNS1iOTIzLTc1NWY5NTc3ZTIwMCJ9fQ.lbsZ9ki67lnnl8mknIDZNWDNkfqm1AQMwCnvgOsfHqkxBpk5pnSy7B3pt4JKkeK0wtjDHMBGpzR60FBtU-qlwQYiK2vA1KE7OAcgHZohZq_GNQeJj8Fe98eeHAzszdntlbGyxLfAlTibRchX15fkfoRZYImxo2bu0MOsUoiYDNbtIsJj560Kq1MOlB1FpMBqYqeBJRoVZYTQP6_038RiS9zHg6GddFcS6oge8HEkyyz6pibsOJNe2XTtdfWdP3U5POk-vbbsUbmDvwtL2hOxAamGr_JRSsxIDjJoT-azKLlH9-n-z4V1wHmc_WXOWRcK624-AWapN7IGQOalhaMDIA

     		#3.2.5.1. COOKIES_metroIdentity_DECODED_DATA:

     			#3.2.5.1.1. HEADERS_Responce_Cookie_DECODED_DATA-HEADER:
	                 {
                     "alg": "RS256",
                     "typ": "JWT",
  					 "kid": "token-signing-keypair"
                     }

                #3.2.5.1.2. HEADERS_Responce_Cookie_DECODED_DATA-PAYLOAD:
                 {
  				 "SSO_CUST_BG": {
    			 "session_state": "47762a5b-8ecb-4c18-a5ac-463c29db0022|1669398792568",
    			 "sub": "U_f420aca8-f693-4c15-b923-755f9577e200"
  				  }
				 }

                #3.2.5.1.3. HEADERS_Responce_Cookie_DECODED_DATA-VERIFY_SIGNATURE:
                 HMACSHA256(
  				 base64UrlEncode(header) + "." +
  				 base64UrlEncode(payload),
  				 
  				 )
  				 

  				#3.2.5.1.4. HEADERS_Responce_Cookie_DECODED_DATA-STATUS:
  				 invalid signature

  		#3.2.5. COOKIES_oidcSessionTracker:
  		 eyJTU09fQ1VTVF9CRyI6IkJURVg6TkVYVENNUyJ9

  		#3.2.5. COOKIES_SES2_customerAdr_:
  		 {"addressId":null,"addressHash":null,"storeId":"00022"}

  		#3.2.5. COOKIES_SES2_customerAdr_1001100022726355:
  		 {"addressId":"1001100022726355994-AD0532EI","addressHash":"1001100022726355994-AD0532EI","storeId":"00022"}

  		#3.2.5. COOKIES_UserSettings:
  		 SelectedStore=1b1fc6ac-2ad6-4243-806e-a4a28c96dff4&SelectedAddress=1001100022726355994-ad0532ei

    #3.3. REQUEST
    #SKIP

    #3.4. RESPONSE
    #SKIp
