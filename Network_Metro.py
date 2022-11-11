import requests

url = "https://idam.metro.bg/authorize/api/oauth2/check_session_iframe)"

payload = "user_id=asd&password=asd&user_type=CUST&client_id=BTEX&response_type=token%2Bid_token&country_code=BG&locale_id=bg-BG&realm_id=SSO_CUST_BG&account_id=&redirect_url=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&state=fc764b0c9c404b96909b551ae5c2b4e2&nonce=9849d97781d64d8eb2768e792769f202&scope=openid%2Bclnt%3DBTEX&code_challenge=&code_challenge_method="
headers = {
    "cookie": "TSPD_BDR=08a625aae3ab2000660fc51cde1f44c3fda147ece6f882f4ec6db8beb701085c34eb59d8e6469638084ecdc5bc0a4000514eb416d9f417363cb3459d6089635d8b7e4b83e38bc45482afad7accc76d716e1aced169f0c2ad35ae1fea54187628fbb98e8bd8e3952287ddb74f367619bb; TSbcb913d5075=deleted; TSbcb913d5029=08a625aae3ab28008620521277008b851fdcbb8cb30abf655340f501b1a5e0c88ecc6f9076797c0b8c59788323b4acc7; TSbcb913d5078=08a625aae3ab2000156472ca6bbc44ca8c51e9cf1f3ae93568d70bebc6235997c6544abddd20b1b50831be065918600173857ab0aa646ebb518722b4c8d46c9d3a9e039c28a66985f3d9b374b5f3de14f20b4d3cdb29f633363bcc3cb9ee2d8b75f95de8a728f0367a9f3baeff007ff138759fbe629f2d0d556e5d90e964f99842eafe4e6c0deb87173668e214e94188902586144f111541303db43b64840a7ebffb794df6fd325fdf5f46cbb8d0a52873021bfc5e3bd564213bf4890c31eacaacf296c45d916a28957aacddde3a07f538defddda7e2f6f632dc558dfacb2b4d549d011164f08cf9e2ee2a975927a0e6c07d958a22f5c426c609e311be52fc1035674e30b4838dd0539046d8c228a623534ff16a5c12c9c91423b1f25801c6b1d56e20a0f9083b9f15cb194d45c4611a2496df19df1300b6e57fdf9632efb979fc2e02851280effe363c8ed72ba809164a1a2cef5666649d7b4fa4c3aad8c36c86e80773c1deb674bb4bbc1c4be09e7a94309f53e6d2dbd9bffa427bfc97d9a35bc8b993ba2fcfd627091d6120ca2c5b; TS7a8c3458027=08a625aae3ab20001bd0ac4165b53e3599fbc1e771f4bb82d920c0cbd6d900576be5c746de86c60e08f78bb74e11300096c8d3a6c713e1aa9ff5199069df3b19a0917570a5e0fb1d7ec75f854459b78980938969c51eea12ec8a37ff76208ab8; BIGipServeridam.metrosystems.net-80=!NXSJTdtgHVWcR8HUzUGSRTsG4v6oUb8lOuo1eqqq6yqvz14ZmX%2BKXrJNo%2BNgp0caJN7XxEpEjIunVIo%3D; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; TS010a0d4d030=0169fc3859c8a1694c718dd4c9cbc5f955a0e6e3888514ce92d8f852fbf8de5ee327208d910c0444ad93b2f86eb1189e96dfcb973d",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "TSbcb913d5078=08a625aae3ab20003e73c4fd648aa67ee379b63ea1fabd45902d8764b9cd7a6b291685a5d339e0ae08d47f558a185801eda3150925464713021cdf27ac72259085ddb7a53d1323d41f55f665f84564fb914bdac942cd27498bdd97ded07913599164c27a36f34f489a0e0abe5a179cd37d46a3572123e6949a3d125fed85963f1a2194e8606c61c4481fc09ba93eb8f5f2b704499569b14657c733099a20b2f664c8ece673f13f6dbbe20b0ab3659ead880ee0e5a2c546172a422f4b1551e3ad7998b98f2f3435124624774c5537fd10a017d1aaee5b6452e3847527e3462b6ac89c4c08ec06183023f4c310a2a4596303045d1b7cffed6c6859c67f4adb0bfc39ae55e93c6c3a5c503ec245e279bcefdef329a189d8f941d70c793e51de541df5b76476abd8d9a8fba1e9f216a3c1b13bda6b209f259f97983cd6a3586f371e28d68d2b10a7eae6c511dcadcd674e8df56919a76626896f1ef63debd1607c41bc684edd2f0d0c8126ebffbc5819f2c587f89f9b605c753330bfcf697f95b90856b0ccf4db926f04; TS00000000076=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d09d000db00110cbd517c033f9e00a766304105770d9e5617ff2b82418778c303e6901cab617d880134f21af992c52bd0848eabaac4e67f2d467382b45f5b2bcd3c24a73750494ea0de38f9862100359296e051ed62fde2651e4a2498cb9a312f9aabd1ddbeb8b7dea5e65a7e972050222203e70a2376a422121219b4133e940ff4bb84c6ccd36982ca59d8488247d47bd07205a470e14aad82592ffbc08d0aa5f457152dae9b17bdfcb32f58eaf5fd5d49d12404a1b64bb2ecd2415db00b01bfff8c890c93ee452fcb4da06f70514f2f7ad621; TSPD_101_DID=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d0638000196598a6788f820190fd91126bd4561c594ef755e85f5172c6ea635a2f76f666492ff65060daba3d822cc765a8bb390376693b6754cc759; BIGipServeridam.metrosystems.net-80=\u00217fsxS8fkT+qSuQxlllsv0yPj1IQ7JOUaBQydVbRGSBx/xQL5PSC8YRrhQ9xlYvGEIElTtaZkFawfJeY=; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; barrier=ARFCzCofonmfhkeucC99NXBklTCbhmmBEKpIfLkg6ttKpzJzMME3U2B0YnciQn513eazXeCCeX/vhXRUWFgSLjlSrVW4RagJN80dM6Lu82EtpWamHudu7uE18pk=; TSbcb913d5029=08a625aae3ab28004afb46397463362b9f9eb8775d7ab74376c8aa0ef56d5f4a7274ec113f0566c968f054ad818055dc; TS7a8c3458027=08a625aae3ab200064365697b73c5e5f7e0d285f4b43bbec1b16f9e4b7ba7fd88adf26d5f8a5bb5108905514e411300033fae4ebbb2a8b760474d894f8725925896c0cf7269a4cc221c9cf90585b03b68800c9294f3321d827000e8baa023fb6; _dd_s=rum=1&id=eee04a66-6cf6-4e1a-843c-972dcf235171&created=1668201465597&expire=1668202415769",
    "DR-Trace-ID": "idam-trace-id",
    "Origin": "https://idam.metro.bg",
    "Referer": "https://idam.metro.bg/web/Signin?scope=openid+clnt%3DBTEX&locale_id=bg-BG&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token+id_token&nonce=9849d97781d64d8eb2768e792769f202&state=fc764b0c9c404b96909b551ae5c2b4e2",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "X-Security-Request": "required",
    "sec-ch-ua": ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": ""Linux""
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

import http.client

conn = http.client.HTTPSConnection("idam.metro.bg")

payload = "user_id=asd&password=asd&user_type=CUST&client_id=BTEX&response_type=token%2Bid_token&country_code=BG&locale_id=bg-BG&realm_id=SSO_CUST_BG&account_id=&redirect_url=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&state=fc764b0c9c404b96909b551ae5c2b4e2&nonce=9849d97781d64d8eb2768e792769f202&scope=openid%2Bclnt%3DBTEX&code_challenge=&code_challenge_method="

headers = {
    'cookie': "TSPD_BDR=08a625aae3ab2000660fc51cde1f44c3fda147ece6f882f4ec6db8beb701085c34eb59d8e6469638084ecdc5bc0a4000514eb416d9f417363cb3459d6089635d8b7e4b83e38bc45482afad7accc76d716e1aced169f0c2ad35ae1fea54187628fbb98e8bd8e3952287ddb74f367619bb; TSbcb913d5075=deleted; TSbcb913d5029=08a625aae3ab28008620521277008b851fdcbb8cb30abf655340f501b1a5e0c88ecc6f9076797c0b8c59788323b4acc7; TSbcb913d5078=08a625aae3ab2000156472ca6bbc44ca8c51e9cf1f3ae93568d70bebc6235997c6544abddd20b1b50831be065918600173857ab0aa646ebb518722b4c8d46c9d3a9e039c28a66985f3d9b374b5f3de14f20b4d3cdb29f633363bcc3cb9ee2d8b75f95de8a728f0367a9f3baeff007ff138759fbe629f2d0d556e5d90e964f99842eafe4e6c0deb87173668e214e94188902586144f111541303db43b64840a7ebffb794df6fd325fdf5f46cbb8d0a52873021bfc5e3bd564213bf4890c31eacaacf296c45d916a28957aacddde3a07f538defddda7e2f6f632dc558dfacb2b4d549d011164f08cf9e2ee2a975927a0e6c07d958a22f5c426c609e311be52fc1035674e30b4838dd0539046d8c228a623534ff16a5c12c9c91423b1f25801c6b1d56e20a0f9083b9f15cb194d45c4611a2496df19df1300b6e57fdf9632efb979fc2e02851280effe363c8ed72ba809164a1a2cef5666649d7b4fa4c3aad8c36c86e80773c1deb674bb4bbc1c4be09e7a94309f53e6d2dbd9bffa427bfc97d9a35bc8b993ba2fcfd627091d6120ca2c5b; TS7a8c3458027=08a625aae3ab20001bd0ac4165b53e3599fbc1e771f4bb82d920c0cbd6d900576be5c746de86c60e08f78bb74e11300096c8d3a6c713e1aa9ff5199069df3b19a0917570a5e0fb1d7ec75f854459b78980938969c51eea12ec8a37ff76208ab8; BIGipServeridam.metrosystems.net-80=!NXSJTdtgHVWcR8HUzUGSRTsG4v6oUb8lOuo1eqqq6yqvz14ZmX%2BKXrJNo%2BNgp0caJN7XxEpEjIunVIo%3D; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; TS010a0d4d030=0169fc3859c8a1694c718dd4c9cbc5f955a0e6e3888514ce92d8f852fbf8de5ee327208d910c0444ad93b2f86eb1189e96dfcb973d",
    'Accept': "*/*",
    'Accept-Language': "en-US,en;q=0.9",
    'Connection': "keep-alive",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "TSbcb913d5078=08a625aae3ab20003e73c4fd648aa67ee379b63ea1fabd45902d8764b9cd7a6b291685a5d339e0ae08d47f558a185801eda3150925464713021cdf27ac72259085ddb7a53d1323d41f55f665f84564fb914bdac942cd27498bdd97ded07913599164c27a36f34f489a0e0abe5a179cd37d46a3572123e6949a3d125fed85963f1a2194e8606c61c4481fc09ba93eb8f5f2b704499569b14657c733099a20b2f664c8ece673f13f6dbbe20b0ab3659ead880ee0e5a2c546172a422f4b1551e3ad7998b98f2f3435124624774c5537fd10a017d1aaee5b6452e3847527e3462b6ac89c4c08ec06183023f4c310a2a4596303045d1b7cffed6c6859c67f4adb0bfc39ae55e93c6c3a5c503ec245e279bcefdef329a189d8f941d70c793e51de541df5b76476abd8d9a8fba1e9f216a3c1b13bda6b209f259f97983cd6a3586f371e28d68d2b10a7eae6c511dcadcd674e8df56919a76626896f1ef63debd1607c41bc684edd2f0d0c8126ebffbc5819f2c587f89f9b605c753330bfcf697f95b90856b0ccf4db926f04; TS00000000076=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d09d000db00110cbd517c033f9e00a766304105770d9e5617ff2b82418778c303e6901cab617d880134f21af992c52bd0848eabaac4e67f2d467382b45f5b2bcd3c24a73750494ea0de38f9862100359296e051ed62fde2651e4a2498cb9a312f9aabd1ddbeb8b7dea5e65a7e972050222203e70a2376a422121219b4133e940ff4bb84c6ccd36982ca59d8488247d47bd07205a470e14aad82592ffbc08d0aa5f457152dae9b17bdfcb32f58eaf5fd5d49d12404a1b64bb2ecd2415db00b01bfff8c890c93ee452fcb4da06f70514f2f7ad621; TSPD_101_DID=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d0638000196598a6788f820190fd91126bd4561c594ef755e85f5172c6ea635a2f76f666492ff65060daba3d822cc765a8bb390376693b6754cc759; BIGipServeridam.metrosystems.net-80=\u00217fsxS8fkT+qSuQxlllsv0yPj1IQ7JOUaBQydVbRGSBx/xQL5PSC8YRrhQ9xlYvGEIElTtaZkFawfJeY=; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; barrier=ARFCzCofonmfhkeucC99NXBklTCbhmmBEKpIfLkg6ttKpzJzMME3U2B0YnciQn513eazXeCCeX/vhXRUWFgSLjlSrVW4RagJN80dM6Lu82EtpWamHudu7uE18pk=; TSbcb913d5029=08a625aae3ab28004afb46397463362b9f9eb8775d7ab74376c8aa0ef56d5f4a7274ec113f0566c968f054ad818055dc; TS7a8c3458027=08a625aae3ab200064365697b73c5e5f7e0d285f4b43bbec1b16f9e4b7ba7fd88adf26d5f8a5bb5108905514e411300033fae4ebbb2a8b760474d894f8725925896c0cf7269a4cc221c9cf90585b03b68800c9294f3321d827000e8baa023fb6; _dd_s=rum=1&id=eee04a66-6cf6-4e1a-843c-972dcf235171&created=1668201465597&expire=1668202415769",
    'DR-Trace-ID': "idam-trace-id",
    'Origin': "https://idam.metro.bg",
    'Referer': "https://idam.metro.bg/web/Signin?scope=openid+clnt%3DBTEX&locale_id=bg-BG&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token+id_token&nonce=9849d97781d64d8eb2768e792769f202&state=fc764b0c9c404b96909b551ae5c2b4e2",
    'Sec-Fetch-Dest': "empty",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Site': "same-origin",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest",
    'X-Security-Request': "required",
    'sec-ch-ua': ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': ""Linux""
    }

conn.request("POST", "/authorize/api/oauth2/check_session_iframe)", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

#==========================================================================================================================================================#

import requests

url = "https://idam.metro.bg/authorize/api/oauth2/authorize"

payload = "user_id=asd&password=asd&user_type=CUST&client_id=BTEX&response_type=token%2Bid_token&country_code=BG&locale_id=bg-BG&realm_id=SSO_CUST_BG&account_id=&redirect_url=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&state=fc764b0c9c404b96909b551ae5c2b4e2&nonce=9849d97781d64d8eb2768e792769f202&scope=openid%2Bclnt%3DBTEX&code_challenge=&code_challenge_method="
headers = {
    "cookie": "TSPD_BDR=08a625aae3ab2000e8a415550224c951450c387f200ac5da36d739e9068da26a2c0cf94d4685f68008b64cd57e0a4000de1943599ba69f7e4f88ce7937963c26053f06f2da3bd2830e7ac16daff8802dcb36e6a8cdbd1477d640147f19f16868d66ebe6498ca2080f5736313a661e45f; TSbcb913d5075=deleted; TSbcb913d5029=08a625aae3ab28008620521277008b851fdcbb8cb30abf655340f501b1a5e0c88ecc6f9076797c0b8c59788323b4acc7; TSbcb913d5078=08a625aae3ab200085717a9b4bf41dd6f0669ff7578b43f3b04f6a419de7b11837e0bc9d29a09d9708e2732b881858019ef37e22e672cbf0eb2b68bffa1fa8ec17567032516115bb61427f459cdcb504494b027e5328591cd251de160af8fbb03c458defb9003cdea0320a5e9d02db32c57506a7ad99133d5cadb8e1d013dc8dbb983dc43f444a1bf5b73b47ad0ae09ae9d495635e40bfde3a049c4054b339cfab676a2445f08a699114a41037a3bc5b71b74532f127e2c98b7f714ae35c3b9eca9bbac1ad968588517f89732153fbb0afca6272cde8c59b0405946c57166824d62bacf78f4437d332398b8b108703f4589c13ff3975c240e445d33f87f3f69c636159f4cbb3a33f01456a1ef22c0151b451a9b6dc024389d0151651d21f5e6de3d7b45d06f38c801663928d8deb316d4465c039b2e9388a95c132eeb205637e515b6c6c4f9c6b9317f74ba89065f2c8145138a92f050b3d874246e449a032fa55b4f78907be1d31eee5e91df0a6cf1a4befc5a2edfcf61297438691690bc9ffb9cb028cf39b5d90; TS7a8c3458027=08a625aae3ab20001916e613debdbdecc7ce6b7e5d590173a5e59ebd0ff0a931bc2722af1a6c42b90830eb5afe113000861ea9c45f049531c6401fcdf965d13a6a0eeb4b9d3d64420f826bb8a40277c98b5ad164c83c7a881a08215f8ba9c065; BIGipServeridam.metrosystems.net-80=!NXSJTdtgHVWcR8HUzUGSRTsG4v6oUb8lOuo1eqqq6yqvz14ZmX%2BKXrJNo%2BNgp0caJN7XxEpEjIunVIo%3D; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; TS010a0d4d030=0169fc3859c8a1694c718dd4c9cbc5f955a0e6e3888514ce92d8f852fbf8de5ee327208d910c0444ad93b2f86eb1189e96dfcb973d",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "TSbcb913d5078=08a625aae3ab20003e73c4fd648aa67ee379b63ea1fabd45902d8764b9cd7a6b291685a5d339e0ae08d47f558a185801eda3150925464713021cdf27ac72259085ddb7a53d1323d41f55f665f84564fb914bdac942cd27498bdd97ded07913599164c27a36f34f489a0e0abe5a179cd37d46a3572123e6949a3d125fed85963f1a2194e8606c61c4481fc09ba93eb8f5f2b704499569b14657c733099a20b2f664c8ece673f13f6dbbe20b0ab3659ead880ee0e5a2c546172a422f4b1551e3ad7998b98f2f3435124624774c5537fd10a017d1aaee5b6452e3847527e3462b6ac89c4c08ec06183023f4c310a2a4596303045d1b7cffed6c6859c67f4adb0bfc39ae55e93c6c3a5c503ec245e279bcefdef329a189d8f941d70c793e51de541df5b76476abd8d9a8fba1e9f216a3c1b13bda6b209f259f97983cd6a3586f371e28d68d2b10a7eae6c511dcadcd674e8df56919a76626896f1ef63debd1607c41bc684edd2f0d0c8126ebffbc5819f2c587f89f9b605c753330bfcf697f95b90856b0ccf4db926f04; TS00000000076=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d09d000db00110cbd517c033f9e00a766304105770d9e5617ff2b82418778c303e6901cab617d880134f21af992c52bd0848eabaac4e67f2d467382b45f5b2bcd3c24a73750494ea0de38f9862100359296e051ed62fde2651e4a2498cb9a312f9aabd1ddbeb8b7dea5e65a7e972050222203e70a2376a422121219b4133e940ff4bb84c6ccd36982ca59d8488247d47bd07205a470e14aad82592ffbc08d0aa5f457152dae9b17bdfcb32f58eaf5fd5d49d12404a1b64bb2ecd2415db00b01bfff8c890c93ee452fcb4da06f70514f2f7ad621; TSPD_101_DID=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d0638000196598a6788f820190fd91126bd4561c594ef755e85f5172c6ea635a2f76f666492ff65060daba3d822cc765a8bb390376693b6754cc759; BIGipServeridam.metrosystems.net-80=\u00217fsxS8fkT+qSuQxlllsv0yPj1IQ7JOUaBQydVbRGSBx/xQL5PSC8YRrhQ9xlYvGEIElTtaZkFawfJeY=; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; barrier=ARFCzCofonmfhkeucC99NXBklTCbhmmBEKpIfLkg6ttKpzJzMME3U2B0YnciQn513eazXeCCeX/vhXRUWFgSLjlSrVW4RagJN80dM6Lu82EtpWamHudu7uE18pk=; TSbcb913d5029=08a625aae3ab28004afb46397463362b9f9eb8775d7ab74376c8aa0ef56d5f4a7274ec113f0566c968f054ad818055dc; TS7a8c3458027=08a625aae3ab200064365697b73c5e5f7e0d285f4b43bbec1b16f9e4b7ba7fd88adf26d5f8a5bb5108905514e411300033fae4ebbb2a8b760474d894f8725925896c0cf7269a4cc221c9cf90585b03b68800c9294f3321d827000e8baa023fb6; _dd_s=rum=1&id=eee04a66-6cf6-4e1a-843c-972dcf235171&created=1668201465597&expire=1668202415769",
    "DR-Trace-ID": "idam-trace-id",
    "Origin": "https://idam.metro.bg",
    "Referer": "https://idam.metro.bg/web/Signin?scope=openid+clnt%3DBTEX&locale_id=bg-BG&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token+id_token&nonce=9849d97781d64d8eb2768e792769f202&state=fc764b0c9c404b96909b551ae5c2b4e2",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "X-Security-Request": "required",
    "sec-ch-ua": ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": ""Linux""
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

import http.client

conn = http.client.HTTPSConnection("idam.metro.bg")

payload = "user_id=asd&password=asd&user_type=CUST&client_id=BTEX&response_type=token%2Bid_token&country_code=BG&locale_id=bg-BG&realm_id=SSO_CUST_BG&account_id=&redirect_url=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&state=fc764b0c9c404b96909b551ae5c2b4e2&nonce=9849d97781d64d8eb2768e792769f202&scope=openid%2Bclnt%3DBTEX&code_challenge=&code_challenge_method="

headers = {
    'cookie': "TSPD_BDR=08a625aae3ab2000e8a415550224c951450c387f200ac5da36d739e9068da26a2c0cf94d4685f68008b64cd57e0a4000de1943599ba69f7e4f88ce7937963c26053f06f2da3bd2830e7ac16daff8802dcb36e6a8cdbd1477d640147f19f16868d66ebe6498ca2080f5736313a661e45f; TSbcb913d5075=deleted; TSbcb913d5029=08a625aae3ab28008620521277008b851fdcbb8cb30abf655340f501b1a5e0c88ecc6f9076797c0b8c59788323b4acc7; TSbcb913d5078=08a625aae3ab200085717a9b4bf41dd6f0669ff7578b43f3b04f6a419de7b11837e0bc9d29a09d9708e2732b881858019ef37e22e672cbf0eb2b68bffa1fa8ec17567032516115bb61427f459cdcb504494b027e5328591cd251de160af8fbb03c458defb9003cdea0320a5e9d02db32c57506a7ad99133d5cadb8e1d013dc8dbb983dc43f444a1bf5b73b47ad0ae09ae9d495635e40bfde3a049c4054b339cfab676a2445f08a699114a41037a3bc5b71b74532f127e2c98b7f714ae35c3b9eca9bbac1ad968588517f89732153fbb0afca6272cde8c59b0405946c57166824d62bacf78f4437d332398b8b108703f4589c13ff3975c240e445d33f87f3f69c636159f4cbb3a33f01456a1ef22c0151b451a9b6dc024389d0151651d21f5e6de3d7b45d06f38c801663928d8deb316d4465c039b2e9388a95c132eeb205637e515b6c6c4f9c6b9317f74ba89065f2c8145138a92f050b3d874246e449a032fa55b4f78907be1d31eee5e91df0a6cf1a4befc5a2edfcf61297438691690bc9ffb9cb028cf39b5d90; TS7a8c3458027=08a625aae3ab20001916e613debdbdecc7ce6b7e5d590173a5e59ebd0ff0a931bc2722af1a6c42b90830eb5afe113000861ea9c45f049531c6401fcdf965d13a6a0eeb4b9d3d64420f826bb8a40277c98b5ad164c83c7a881a08215f8ba9c065; BIGipServeridam.metrosystems.net-80=!NXSJTdtgHVWcR8HUzUGSRTsG4v6oUb8lOuo1eqqq6yqvz14ZmX%2BKXrJNo%2BNgp0caJN7XxEpEjIunVIo%3D; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; TS010a0d4d030=0169fc3859c8a1694c718dd4c9cbc5f955a0e6e3888514ce92d8f852fbf8de5ee327208d910c0444ad93b2f86eb1189e96dfcb973d",
    'Accept': "*/*",
    'Accept-Language': "en-US,en;q=0.9",
    'Connection': "keep-alive",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "TSbcb913d5078=08a625aae3ab20003e73c4fd648aa67ee379b63ea1fabd45902d8764b9cd7a6b291685a5d339e0ae08d47f558a185801eda3150925464713021cdf27ac72259085ddb7a53d1323d41f55f665f84564fb914bdac942cd27498bdd97ded07913599164c27a36f34f489a0e0abe5a179cd37d46a3572123e6949a3d125fed85963f1a2194e8606c61c4481fc09ba93eb8f5f2b704499569b14657c733099a20b2f664c8ece673f13f6dbbe20b0ab3659ead880ee0e5a2c546172a422f4b1551e3ad7998b98f2f3435124624774c5537fd10a017d1aaee5b6452e3847527e3462b6ac89c4c08ec06183023f4c310a2a4596303045d1b7cffed6c6859c67f4adb0bfc39ae55e93c6c3a5c503ec245e279bcefdef329a189d8f941d70c793e51de541df5b76476abd8d9a8fba1e9f216a3c1b13bda6b209f259f97983cd6a3586f371e28d68d2b10a7eae6c511dcadcd674e8df56919a76626896f1ef63debd1607c41bc684edd2f0d0c8126ebffbc5819f2c587f89f9b605c753330bfcf697f95b90856b0ccf4db926f04; TS00000000076=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d09d000db00110cbd517c033f9e00a766304105770d9e5617ff2b82418778c303e6901cab617d880134f21af992c52bd0848eabaac4e67f2d467382b45f5b2bcd3c24a73750494ea0de38f9862100359296e051ed62fde2651e4a2498cb9a312f9aabd1ddbeb8b7dea5e65a7e972050222203e70a2376a422121219b4133e940ff4bb84c6ccd36982ca59d8488247d47bd07205a470e14aad82592ffbc08d0aa5f457152dae9b17bdfcb32f58eaf5fd5d49d12404a1b64bb2ecd2415db00b01bfff8c890c93ee452fcb4da06f70514f2f7ad621; TSPD_101_DID=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d0638000196598a6788f820190fd91126bd4561c594ef755e85f5172c6ea635a2f76f666492ff65060daba3d822cc765a8bb390376693b6754cc759; BIGipServeridam.metrosystems.net-80=\u00217fsxS8fkT+qSuQxlllsv0yPj1IQ7JOUaBQydVbRGSBx/xQL5PSC8YRrhQ9xlYvGEIElTtaZkFawfJeY=; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; barrier=ARFCzCofonmfhkeucC99NXBklTCbhmmBEKpIfLkg6ttKpzJzMME3U2B0YnciQn513eazXeCCeX/vhXRUWFgSLjlSrVW4RagJN80dM6Lu82EtpWamHudu7uE18pk=; TSbcb913d5029=08a625aae3ab28004afb46397463362b9f9eb8775d7ab74376c8aa0ef56d5f4a7274ec113f0566c968f054ad818055dc; TS7a8c3458027=08a625aae3ab200064365697b73c5e5f7e0d285f4b43bbec1b16f9e4b7ba7fd88adf26d5f8a5bb5108905514e411300033fae4ebbb2a8b760474d894f8725925896c0cf7269a4cc221c9cf90585b03b68800c9294f3321d827000e8baa023fb6; _dd_s=rum=1&id=eee04a66-6cf6-4e1a-843c-972dcf235171&created=1668201465597&expire=1668202415769",
    'DR-Trace-ID': "idam-trace-id",
    'Origin': "https://idam.metro.bg",
    'Referer': "https://idam.metro.bg/web/Signin?scope=openid+clnt%3DBTEX&locale_id=bg-BG&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token+id_token&nonce=9849d97781d64d8eb2768e792769f202&state=fc764b0c9c404b96909b551ae5c2b4e2",
    'Sec-Fetch-Dest': "empty",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Site': "same-origin",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest",
    'X-Security-Request': "required",
    'sec-ch-ua': ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': ""Linux""
    }

conn.request("POST", "/authorize/api/oauth2/authorize", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

#==========================================================================================================================================================#

import requests

url = "https://idam.metro.bg/web/Signin"

payload = "user_id=asd&password=asd&user_type=CUST&client_id=BTEX&response_type=token%2Bid_token&country_code=BG&locale_id=bg-BG&realm_id=SSO_CUST_BG&account_id=&redirect_url=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&state=fc764b0c9c404b96909b551ae5c2b4e2&nonce=9849d97781d64d8eb2768e792769f202&scope=openid%2Bclnt%3DBTEX&code_challenge=&code_challenge_method="
headers = {
    "cookie": "TSPD_BDR=08a625aae3ab2000a1857a1471426cb5f98a6c404f6634e10544a21ca7b4839cc7c514b3eed7205808960c19610a400044635dfe5c3281f34dc2da11232edfe260107a394e25396a70a8d6fbeedc8813643ddd9930d506ef376e2974e7ae573ec257e34a99c7f5bb17166b6f70c6cef1; TSbcb913d5029=08a625aae3ab28008620521277008b851fdcbb8cb30abf655340f501b1a5e0c88ecc6f9076797c0b8c59788323b4acc7; TSbcb913d5078=08a625aae3ab20005c244974b1e5809d70bbf607933d239dbe53ea6e928ee5a0bd0888cec1a5edb6088e4a26f9184001367fdfd386ccc6f3362fcf3d1831949377ad935027b77c10033f47fe261298176f0d5b9978a0bb32b7e5ad8cde6daf2e8843a8acee49389bb042ad4ee388cbbccddd293527fa2ce329c73865c367e147b12f99cef63b8d7df4b9e5c0624c9a05e5ea27506242d76671fee7a5d2c92ba0b24a5cd563d5d40ccd68842de051bc98848fa07791b593fab44539a666eeeafa6d4ceb8d8db31677e513400d5c0e887b5a27e4f0e24d55767239ae29ed1612ab0f2aa3ee4d014e2e4947c3e1e89a050b776b6f8b76df71f336ded61cb575ef44d9db885b03a48e987c4266e94c0509915730bc189b141db97d38fb54ed5f7ef73ed4032698bd0d8e32eb3889c0285a089f445cd29b706c5eb125988a931038ed4067376b6ad7ae9a10479e3ef78e56b333230d0ada22b95b55d6d7f3e2361545b3fba5d546eaa54249ef1fecf893ae6b; TS7a8c3458027=08a625aae3ab2000d37a6b60d10627dad188f25a21cdfa53bbb028734d1301ac43779eb396e0f6dc08feeea122113000abf2778da6b05dddf0470c1696e179b2d641b4a289e071b2d6d05296d129e94fb9ad9baf62073bd4b2a151e0f72887e8; BIGipServeridam.metrosystems.net-80=!NXSJTdtgHVWcR8HUzUGSRTsG4v6oUb8lOuo1eqqq6yqvz14ZmX%2BKXrJNo%2BNgp0caJN7XxEpEjIunVIo%3D; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; TS010a0d4d030=0169fc3859c8a1694c718dd4c9cbc5f955a0e6e3888514ce92d8f852fbf8de5ee327208d910c0444ad93b2f86eb1189e96dfcb973d",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "TSbcb913d5078=08a625aae3ab20003e73c4fd648aa67ee379b63ea1fabd45902d8764b9cd7a6b291685a5d339e0ae08d47f558a185801eda3150925464713021cdf27ac72259085ddb7a53d1323d41f55f665f84564fb914bdac942cd27498bdd97ded07913599164c27a36f34f489a0e0abe5a179cd37d46a3572123e6949a3d125fed85963f1a2194e8606c61c4481fc09ba93eb8f5f2b704499569b14657c733099a20b2f664c8ece673f13f6dbbe20b0ab3659ead880ee0e5a2c546172a422f4b1551e3ad7998b98f2f3435124624774c5537fd10a017d1aaee5b6452e3847527e3462b6ac89c4c08ec06183023f4c310a2a4596303045d1b7cffed6c6859c67f4adb0bfc39ae55e93c6c3a5c503ec245e279bcefdef329a189d8f941d70c793e51de541df5b76476abd8d9a8fba1e9f216a3c1b13bda6b209f259f97983cd6a3586f371e28d68d2b10a7eae6c511dcadcd674e8df56919a76626896f1ef63debd1607c41bc684edd2f0d0c8126ebffbc5819f2c587f89f9b605c753330bfcf697f95b90856b0ccf4db926f04; TS00000000076=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d09d000db00110cbd517c033f9e00a766304105770d9e5617ff2b82418778c303e6901cab617d880134f21af992c52bd0848eabaac4e67f2d467382b45f5b2bcd3c24a73750494ea0de38f9862100359296e051ed62fde2651e4a2498cb9a312f9aabd1ddbeb8b7dea5e65a7e972050222203e70a2376a422121219b4133e940ff4bb84c6ccd36982ca59d8488247d47bd07205a470e14aad82592ffbc08d0aa5f457152dae9b17bdfcb32f58eaf5fd5d49d12404a1b64bb2ecd2415db00b01bfff8c890c93ee452fcb4da06f70514f2f7ad621; TSPD_101_DID=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d0638000196598a6788f820190fd91126bd4561c594ef755e85f5172c6ea635a2f76f666492ff65060daba3d822cc765a8bb390376693b6754cc759; BIGipServeridam.metrosystems.net-80=\u00217fsxS8fkT+qSuQxlllsv0yPj1IQ7JOUaBQydVbRGSBx/xQL5PSC8YRrhQ9xlYvGEIElTtaZkFawfJeY=; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; barrier=ARFCzCofonmfhkeucC99NXBklTCbhmmBEKpIfLkg6ttKpzJzMME3U2B0YnciQn513eazXeCCeX/vhXRUWFgSLjlSrVW4RagJN80dM6Lu82EtpWamHudu7uE18pk=; TSbcb913d5029=08a625aae3ab28004afb46397463362b9f9eb8775d7ab74376c8aa0ef56d5f4a7274ec113f0566c968f054ad818055dc; TS7a8c3458027=08a625aae3ab200064365697b73c5e5f7e0d285f4b43bbec1b16f9e4b7ba7fd88adf26d5f8a5bb5108905514e411300033fae4ebbb2a8b760474d894f8725925896c0cf7269a4cc221c9cf90585b03b68800c9294f3321d827000e8baa023fb6; _dd_s=rum=1&id=eee04a66-6cf6-4e1a-843c-972dcf235171&created=1668201465597&expire=1668202415769",
    "DR-Trace-ID": "idam-trace-id",
    "Origin": "https://idam.metro.bg",
    "Referer": "https://idam.metro.bg/web/Signin?scope=openid+clnt%3DBTEX&locale_id=bg-BG&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token+id_token&nonce=9849d97781d64d8eb2768e792769f202&state=fc764b0c9c404b96909b551ae5c2b4e2",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "X-Security-Request": "required",
    "sec-ch-ua": ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": ""Linux""
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

import http.client

conn = http.client.HTTPSConnection("idam.metro.bg")

payload = "user_id=asd&password=asd&user_type=CUST&client_id=BTEX&response_type=token%2Bid_token&country_code=BG&locale_id=bg-BG&realm_id=SSO_CUST_BG&account_id=&redirect_url=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&state=fc764b0c9c404b96909b551ae5c2b4e2&nonce=9849d97781d64d8eb2768e792769f202&scope=openid%2Bclnt%3DBTEX&code_challenge=&code_challenge_method="

headers = {
    'cookie': "TSPD_BDR=08a625aae3ab2000a1857a1471426cb5f98a6c404f6634e10544a21ca7b4839cc7c514b3eed7205808960c19610a400044635dfe5c3281f34dc2da11232edfe260107a394e25396a70a8d6fbeedc8813643ddd9930d506ef376e2974e7ae573ec257e34a99c7f5bb17166b6f70c6cef1; TSbcb913d5029=08a625aae3ab28008620521277008b851fdcbb8cb30abf655340f501b1a5e0c88ecc6f9076797c0b8c59788323b4acc7; TSbcb913d5078=08a625aae3ab20005c244974b1e5809d70bbf607933d239dbe53ea6e928ee5a0bd0888cec1a5edb6088e4a26f9184001367fdfd386ccc6f3362fcf3d1831949377ad935027b77c10033f47fe261298176f0d5b9978a0bb32b7e5ad8cde6daf2e8843a8acee49389bb042ad4ee388cbbccddd293527fa2ce329c73865c367e147b12f99cef63b8d7df4b9e5c0624c9a05e5ea27506242d76671fee7a5d2c92ba0b24a5cd563d5d40ccd68842de051bc98848fa07791b593fab44539a666eeeafa6d4ceb8d8db31677e513400d5c0e887b5a27e4f0e24d55767239ae29ed1612ab0f2aa3ee4d014e2e4947c3e1e89a050b776b6f8b76df71f336ded61cb575ef44d9db885b03a48e987c4266e94c0509915730bc189b141db97d38fb54ed5f7ef73ed4032698bd0d8e32eb3889c0285a089f445cd29b706c5eb125988a931038ed4067376b6ad7ae9a10479e3ef78e56b333230d0ada22b95b55d6d7f3e2361545b3fba5d546eaa54249ef1fecf893ae6b; TS7a8c3458027=08a625aae3ab2000d37a6b60d10627dad188f25a21cdfa53bbb028734d1301ac43779eb396e0f6dc08feeea122113000abf2778da6b05dddf0470c1696e179b2d641b4a289e071b2d6d05296d129e94fb9ad9baf62073bd4b2a151e0f72887e8; BIGipServeridam.metrosystems.net-80=!NXSJTdtgHVWcR8HUzUGSRTsG4v6oUb8lOuo1eqqq6yqvz14ZmX%2BKXrJNo%2BNgp0caJN7XxEpEjIunVIo%3D; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; TS010a0d4d030=0169fc3859c8a1694c718dd4c9cbc5f955a0e6e3888514ce92d8f852fbf8de5ee327208d910c0444ad93b2f86eb1189e96dfcb973d",
    'Accept': "*/*",
    'Accept-Language': "en-US,en;q=0.9",
    'Connection': "keep-alive",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "TSbcb913d5078=08a625aae3ab20003e73c4fd648aa67ee379b63ea1fabd45902d8764b9cd7a6b291685a5d339e0ae08d47f558a185801eda3150925464713021cdf27ac72259085ddb7a53d1323d41f55f665f84564fb914bdac942cd27498bdd97ded07913599164c27a36f34f489a0e0abe5a179cd37d46a3572123e6949a3d125fed85963f1a2194e8606c61c4481fc09ba93eb8f5f2b704499569b14657c733099a20b2f664c8ece673f13f6dbbe20b0ab3659ead880ee0e5a2c546172a422f4b1551e3ad7998b98f2f3435124624774c5537fd10a017d1aaee5b6452e3847527e3462b6ac89c4c08ec06183023f4c310a2a4596303045d1b7cffed6c6859c67f4adb0bfc39ae55e93c6c3a5c503ec245e279bcefdef329a189d8f941d70c793e51de541df5b76476abd8d9a8fba1e9f216a3c1b13bda6b209f259f97983cd6a3586f371e28d68d2b10a7eae6c511dcadcd674e8df56919a76626896f1ef63debd1607c41bc684edd2f0d0c8126ebffbc5819f2c587f89f9b605c753330bfcf697f95b90856b0ccf4db926f04; TS00000000076=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d09d000db00110cbd517c033f9e00a766304105770d9e5617ff2b82418778c303e6901cab617d880134f21af992c52bd0848eabaac4e67f2d467382b45f5b2bcd3c24a73750494ea0de38f9862100359296e051ed62fde2651e4a2498cb9a312f9aabd1ddbeb8b7dea5e65a7e972050222203e70a2376a422121219b4133e940ff4bb84c6ccd36982ca59d8488247d47bd07205a470e14aad82592ffbc08d0aa5f457152dae9b17bdfcb32f58eaf5fd5d49d12404a1b64bb2ecd2415db00b01bfff8c890c93ee452fcb4da06f70514f2f7ad621; TSPD_101_DID=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d0638000196598a6788f820190fd91126bd4561c594ef755e85f5172c6ea635a2f76f666492ff65060daba3d822cc765a8bb390376693b6754cc759; BIGipServeridam.metrosystems.net-80=\u00217fsxS8fkT+qSuQxlllsv0yPj1IQ7JOUaBQydVbRGSBx/xQL5PSC8YRrhQ9xlYvGEIElTtaZkFawfJeY=; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; barrier=ARFCzCofonmfhkeucC99NXBklTCbhmmBEKpIfLkg6ttKpzJzMME3U2B0YnciQn513eazXeCCeX/vhXRUWFgSLjlSrVW4RagJN80dM6Lu82EtpWamHudu7uE18pk=; TSbcb913d5029=08a625aae3ab28004afb46397463362b9f9eb8775d7ab74376c8aa0ef56d5f4a7274ec113f0566c968f054ad818055dc; TS7a8c3458027=08a625aae3ab200064365697b73c5e5f7e0d285f4b43bbec1b16f9e4b7ba7fd88adf26d5f8a5bb5108905514e411300033fae4ebbb2a8b760474d894f8725925896c0cf7269a4cc221c9cf90585b03b68800c9294f3321d827000e8baa023fb6; _dd_s=rum=1&id=eee04a66-6cf6-4e1a-843c-972dcf235171&created=1668201465597&expire=1668202415769",
    'DR-Trace-ID': "idam-trace-id",
    'Origin': "https://idam.metro.bg",
    'Referer': "https://idam.metro.bg/web/Signin?scope=openid+clnt%3DBTEX&locale_id=bg-BG&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token+id_token&nonce=9849d97781d64d8eb2768e792769f202&state=fc764b0c9c404b96909b551ae5c2b4e2",
    'Sec-Fetch-Dest': "empty",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Site': "same-origin",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest",
    'X-Security-Request': "required",
    'sec-ch-ua': ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': ""Linux""
    }

conn.request("POST", "/web/Signin", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

#==========================================================================================================================================================#

import requests

url = "https://shop.metro.bg/shop/cart"

payload = "user_id=asd&password=asd&user_type=CUST&client_id=BTEX&response_type=token%2Bid_token&country_code=BG&locale_id=bg-BG&realm_id=SSO_CUST_BG&account_id=&redirect_url=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&state=fc764b0c9c404b96909b551ae5c2b4e2&nonce=9849d97781d64d8eb2768e792769f202&scope=openid%2Bclnt%3DBTEX&code_challenge=&code_challenge_method="
headers = {
    "cookie": "BIGipServerbetty.metrosystems.net-80=!qQj%2Bdjr3JVKOnuYEdKzHuTxiWd%2Bak1dp6JVXDGvPolbpAYOl23mCyTlpyRdQEte99U5xnOiePdTagAU%3D; selectedLocale_BG=bg-BG",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "TSbcb913d5078=08a625aae3ab20003e73c4fd648aa67ee379b63ea1fabd45902d8764b9cd7a6b291685a5d339e0ae08d47f558a185801eda3150925464713021cdf27ac72259085ddb7a53d1323d41f55f665f84564fb914bdac942cd27498bdd97ded07913599164c27a36f34f489a0e0abe5a179cd37d46a3572123e6949a3d125fed85963f1a2194e8606c61c4481fc09ba93eb8f5f2b704499569b14657c733099a20b2f664c8ece673f13f6dbbe20b0ab3659ead880ee0e5a2c546172a422f4b1551e3ad7998b98f2f3435124624774c5537fd10a017d1aaee5b6452e3847527e3462b6ac89c4c08ec06183023f4c310a2a4596303045d1b7cffed6c6859c67f4adb0bfc39ae55e93c6c3a5c503ec245e279bcefdef329a189d8f941d70c793e51de541df5b76476abd8d9a8fba1e9f216a3c1b13bda6b209f259f97983cd6a3586f371e28d68d2b10a7eae6c511dcadcd674e8df56919a76626896f1ef63debd1607c41bc684edd2f0d0c8126ebffbc5819f2c587f89f9b605c753330bfcf697f95b90856b0ccf4db926f04; TS00000000076=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d09d000db00110cbd517c033f9e00a766304105770d9e5617ff2b82418778c303e6901cab617d880134f21af992c52bd0848eabaac4e67f2d467382b45f5b2bcd3c24a73750494ea0de38f9862100359296e051ed62fde2651e4a2498cb9a312f9aabd1ddbeb8b7dea5e65a7e972050222203e70a2376a422121219b4133e940ff4bb84c6ccd36982ca59d8488247d47bd07205a470e14aad82592ffbc08d0aa5f457152dae9b17bdfcb32f58eaf5fd5d49d12404a1b64bb2ecd2415db00b01bfff8c890c93ee452fcb4da06f70514f2f7ad621; TSPD_101_DID=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d0638000196598a6788f820190fd91126bd4561c594ef755e85f5172c6ea635a2f76f666492ff65060daba3d822cc765a8bb390376693b6754cc759; BIGipServeridam.metrosystems.net-80=\u00217fsxS8fkT+qSuQxlllsv0yPj1IQ7JOUaBQydVbRGSBx/xQL5PSC8YRrhQ9xlYvGEIElTtaZkFawfJeY=; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; barrier=ARFCzCofonmfhkeucC99NXBklTCbhmmBEKpIfLkg6ttKpzJzMME3U2B0YnciQn513eazXeCCeX/vhXRUWFgSLjlSrVW4RagJN80dM6Lu82EtpWamHudu7uE18pk=; TSbcb913d5029=08a625aae3ab28004afb46397463362b9f9eb8775d7ab74376c8aa0ef56d5f4a7274ec113f0566c968f054ad818055dc; TS7a8c3458027=08a625aae3ab200064365697b73c5e5f7e0d285f4b43bbec1b16f9e4b7ba7fd88adf26d5f8a5bb5108905514e411300033fae4ebbb2a8b760474d894f8725925896c0cf7269a4cc221c9cf90585b03b68800c9294f3321d827000e8baa023fb6; _dd_s=rum=1&id=eee04a66-6cf6-4e1a-843c-972dcf235171&created=1668201465597&expire=1668202415769",
    "DR-Trace-ID": "idam-trace-id",
    "Origin": "https://idam.metro.bg",
    "Referer": "https://idam.metro.bg/web/Signin?scope=openid+clnt%3DBTEX&locale_id=bg-BG&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token+id_token&nonce=9849d97781d64d8eb2768e792769f202&state=fc764b0c9c404b96909b551ae5c2b4e2",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "X-Security-Request": "required",
    "sec-ch-ua": ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": ""Linux""
}

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)

import http.client

conn = http.client.HTTPSConnection("shop.metro.bg")

payload = "user_id=asd&password=asd&user_type=CUST&client_id=BTEX&response_type=token%2Bid_token&country_code=BG&locale_id=bg-BG&realm_id=SSO_CUST_BG&account_id=&redirect_url=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&state=fc764b0c9c404b96909b551ae5c2b4e2&nonce=9849d97781d64d8eb2768e792769f202&scope=openid%2Bclnt%3DBTEX&code_challenge=&code_challenge_method="

headers = {
    'cookie': "BIGipServerbetty.metrosystems.net-80=!qQj%2Bdjr3JVKOnuYEdKzHuTxiWd%2Bak1dp6JVXDGvPolbpAYOl23mCyTlpyRdQEte99U5xnOiePdTagAU%3D; selectedLocale_BG=bg-BG",
    'Accept': "*/*",
    'Accept-Language': "en-US,en;q=0.9",
    'Connection': "keep-alive",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "TSbcb913d5078=08a625aae3ab20003e73c4fd648aa67ee379b63ea1fabd45902d8764b9cd7a6b291685a5d339e0ae08d47f558a185801eda3150925464713021cdf27ac72259085ddb7a53d1323d41f55f665f84564fb914bdac942cd27498bdd97ded07913599164c27a36f34f489a0e0abe5a179cd37d46a3572123e6949a3d125fed85963f1a2194e8606c61c4481fc09ba93eb8f5f2b704499569b14657c733099a20b2f664c8ece673f13f6dbbe20b0ab3659ead880ee0e5a2c546172a422f4b1551e3ad7998b98f2f3435124624774c5537fd10a017d1aaee5b6452e3847527e3462b6ac89c4c08ec06183023f4c310a2a4596303045d1b7cffed6c6859c67f4adb0bfc39ae55e93c6c3a5c503ec245e279bcefdef329a189d8f941d70c793e51de541df5b76476abd8d9a8fba1e9f216a3c1b13bda6b209f259f97983cd6a3586f371e28d68d2b10a7eae6c511dcadcd674e8df56919a76626896f1ef63debd1607c41bc684edd2f0d0c8126ebffbc5819f2c587f89f9b605c753330bfcf697f95b90856b0ccf4db926f04; TS00000000076=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d09d000db00110cbd517c033f9e00a766304105770d9e5617ff2b82418778c303e6901cab617d880134f21af992c52bd0848eabaac4e67f2d467382b45f5b2bcd3c24a73750494ea0de38f9862100359296e051ed62fde2651e4a2498cb9a312f9aabd1ddbeb8b7dea5e65a7e972050222203e70a2376a422121219b4133e940ff4bb84c6ccd36982ca59d8488247d47bd07205a470e14aad82592ffbc08d0aa5f457152dae9b17bdfcb32f58eaf5fd5d49d12404a1b64bb2ecd2415db00b01bfff8c890c93ee452fcb4da06f70514f2f7ad621; TSPD_101_DID=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d0638000196598a6788f820190fd91126bd4561c594ef755e85f5172c6ea635a2f76f666492ff65060daba3d822cc765a8bb390376693b6754cc759; BIGipServeridam.metrosystems.net-80=\u00217fsxS8fkT+qSuQxlllsv0yPj1IQ7JOUaBQydVbRGSBx/xQL5PSC8YRrhQ9xlYvGEIElTtaZkFawfJeY=; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; barrier=ARFCzCofonmfhkeucC99NXBklTCbhmmBEKpIfLkg6ttKpzJzMME3U2B0YnciQn513eazXeCCeX/vhXRUWFgSLjlSrVW4RagJN80dM6Lu82EtpWamHudu7uE18pk=; TSbcb913d5029=08a625aae3ab28004afb46397463362b9f9eb8775d7ab74376c8aa0ef56d5f4a7274ec113f0566c968f054ad818055dc; TS7a8c3458027=08a625aae3ab200064365697b73c5e5f7e0d285f4b43bbec1b16f9e4b7ba7fd88adf26d5f8a5bb5108905514e411300033fae4ebbb2a8b760474d894f8725925896c0cf7269a4cc221c9cf90585b03b68800c9294f3321d827000e8baa023fb6; _dd_s=rum=1&id=eee04a66-6cf6-4e1a-843c-972dcf235171&created=1668201465597&expire=1668202415769",
    'DR-Trace-ID': "idam-trace-id",
    'Origin': "https://idam.metro.bg",
    'Referer': "https://idam.metro.bg/web/Signin?scope=openid+clnt%3DBTEX&locale_id=bg-BG&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token+id_token&nonce=9849d97781d64d8eb2768e792769f202&state=fc764b0c9c404b96909b551ae5c2b4e2",
    'Sec-Fetch-Dest': "empty",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Site': "same-origin",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest",
    'X-Security-Request': "required",
    'sec-ch-ua': ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': ""Linux""
    }

conn.request("GET", "/shop/cart", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

#==========================================================================================================================================================#

import requests

url = "https://idam.metro.bg/web/authc/authenticate"

payload = "user_id=asd&password=asd&user_type=CUST&client_id=BTEX&response_type=token%2Bid_token&country_code=BG&locale_id=bg-BG&realm_id=SSO_CUST_BG&account_id=&redirect_url=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&state=fc764b0c9c404b96909b551ae5c2b4e2&nonce=9849d97781d64d8eb2768e792769f202&scope=openid%2Bclnt%3DBTEX&code_challenge=&code_challenge_method="
headers = {
    "cookie": "TSPD_BDR=08a625aae3ab200080bac0a15841aeb6f296f48c7c720d829184b273c422046df6293acad34e0c3108ebaa001d0a4000539675d3da4dc2b3e53c6c906c1e9ab7633104a3dad1db26cdce2397d10c87b502b685dc5ccc7bddd9f7cdc86e1ef38834f5ed144e50155e7ca71ac9833d3f27; TSbcb913d5029=08a625aae3ab28008620521277008b851fdcbb8cb30abf655340f501b1a5e0c88ecc6f9076797c0b8c59788323b4acc7; TSbcb913d5078=08a625aae3ab2000e9d3b7c72f6d24586476bf79de8a7cb43e078eea8304a10a3a1d92cc08e8e25e08ab93f6e41850013f575e7c55c2b0b01bed26daf58c753bd02ea702b6c269573c8cf30dfea0e3d15f87c0e4631ef968e1dd73181989381a9fa46ea96b636a2bf46136c9cd3ed7a10ef7a90f7faedd31be1b128edfc9cb9690786a7f19eb5ae8ae6ddb4d5964103cf94b591afd90209eb1abc34dbeaef97b896d9ee868c4875331621cc85476e12c46a53301e70a0897b72699be345b4d9aa0865b11c273b8c10813212f70a587f79ef0e62f5cd75ff71777c15f0da9527062c70a596840fa51ceba1fd9e9ab1230fcfe971785fe85f03dea9bccb6a05f1c369e6feda66571720ed889031d1c6648b0449bd33ab4b5823a21aa45749839a39bd7e60846fd6db3358750525a59c09ade731038cbf8f7b663748381c0e8fa2783956c6c67b70e931dfa17986af7cc2c6154acf8d18508583c09e246c85907db8e990b50b5fa89bcec7f3a8ca81c9c85873914655f669d9633ff9a6a42d7e6c1; TS7a8c3458027=08a625aae3ab20006eacc0aaa41121a3dd43815d5856a5f3007771672b0b900172d8c950536d05bd08fddb78ee1130006daa6f34ac3bf969d18a0612fd3c637f36dc2ac50921cfe5072d7ca6dbfec3734f97863c380e307d5299cd2c141e914a; BIGipServeridam.metrosystems.net-80=!NXSJTdtgHVWcR8HUzUGSRTsG4v6oUb8lOuo1eqqq6yqvz14ZmX%2BKXrJNo%2BNgp0caJN7XxEpEjIunVIo%3D; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; TS010a0d4d030=0169fc3859c8a1694c718dd4c9cbc5f955a0e6e3888514ce92d8f852fbf8de5ee327208d910c0444ad93b2f86eb1189e96dfcb973d",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "TSbcb913d5078=08a625aae3ab20003e73c4fd648aa67ee379b63ea1fabd45902d8764b9cd7a6b291685a5d339e0ae08d47f558a185801eda3150925464713021cdf27ac72259085ddb7a53d1323d41f55f665f84564fb914bdac942cd27498bdd97ded07913599164c27a36f34f489a0e0abe5a179cd37d46a3572123e6949a3d125fed85963f1a2194e8606c61c4481fc09ba93eb8f5f2b704499569b14657c733099a20b2f664c8ece673f13f6dbbe20b0ab3659ead880ee0e5a2c546172a422f4b1551e3ad7998b98f2f3435124624774c5537fd10a017d1aaee5b6452e3847527e3462b6ac89c4c08ec06183023f4c310a2a4596303045d1b7cffed6c6859c67f4adb0bfc39ae55e93c6c3a5c503ec245e279bcefdef329a189d8f941d70c793e51de541df5b76476abd8d9a8fba1e9f216a3c1b13bda6b209f259f97983cd6a3586f371e28d68d2b10a7eae6c511dcadcd674e8df56919a76626896f1ef63debd1607c41bc684edd2f0d0c8126ebffbc5819f2c587f89f9b605c753330bfcf697f95b90856b0ccf4db926f04; TS00000000076=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d09d000db00110cbd517c033f9e00a766304105770d9e5617ff2b82418778c303e6901cab617d880134f21af992c52bd0848eabaac4e67f2d467382b45f5b2bcd3c24a73750494ea0de38f9862100359296e051ed62fde2651e4a2498cb9a312f9aabd1ddbeb8b7dea5e65a7e972050222203e70a2376a422121219b4133e940ff4bb84c6ccd36982ca59d8488247d47bd07205a470e14aad82592ffbc08d0aa5f457152dae9b17bdfcb32f58eaf5fd5d49d12404a1b64bb2ecd2415db00b01bfff8c890c93ee452fcb4da06f70514f2f7ad621; TSPD_101_DID=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d0638000196598a6788f820190fd91126bd4561c594ef755e85f5172c6ea635a2f76f666492ff65060daba3d822cc765a8bb390376693b6754cc759; BIGipServeridam.metrosystems.net-80=\u00217fsxS8fkT+qSuQxlllsv0yPj1IQ7JOUaBQydVbRGSBx/xQL5PSC8YRrhQ9xlYvGEIElTtaZkFawfJeY=; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; barrier=ARFCzCofonmfhkeucC99NXBklTCbhmmBEKpIfLkg6ttKpzJzMME3U2B0YnciQn513eazXeCCeX/vhXRUWFgSLjlSrVW4RagJN80dM6Lu82EtpWamHudu7uE18pk=; TSbcb913d5029=08a625aae3ab28004afb46397463362b9f9eb8775d7ab74376c8aa0ef56d5f4a7274ec113f0566c968f054ad818055dc; TS7a8c3458027=08a625aae3ab200064365697b73c5e5f7e0d285f4b43bbec1b16f9e4b7ba7fd88adf26d5f8a5bb5108905514e411300033fae4ebbb2a8b760474d894f8725925896c0cf7269a4cc221c9cf90585b03b68800c9294f3321d827000e8baa023fb6; _dd_s=rum=1&id=eee04a66-6cf6-4e1a-843c-972dcf235171&created=1668201465597&expire=1668202415769",
    "DR-Trace-ID": "idam-trace-id",
    "Origin": "https://idam.metro.bg",
    "Referer": "https://idam.metro.bg/web/Signin?scope=openid+clnt%3DBTEX&locale_id=bg-BG&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token+id_token&nonce=9849d97781d64d8eb2768e792769f202&state=fc764b0c9c404b96909b551ae5c2b4e2",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "X-Security-Request": "required",
    "sec-ch-ua": ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": ""Linux""
}

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)

import http.client

conn = http.client.HTTPSConnection("idam.metro.bg")

payload = "user_id=asd&password=asd&user_type=CUST&client_id=BTEX&response_type=token%2Bid_token&country_code=BG&locale_id=bg-BG&realm_id=SSO_CUST_BG&account_id=&redirect_url=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&state=fc764b0c9c404b96909b551ae5c2b4e2&nonce=9849d97781d64d8eb2768e792769f202&scope=openid%2Bclnt%3DBTEX&code_challenge=&code_challenge_method="

headers = {
    'cookie': "TSPD_BDR=08a625aae3ab200080bac0a15841aeb6f296f48c7c720d829184b273c422046df6293acad34e0c3108ebaa001d0a4000539675d3da4dc2b3e53c6c906c1e9ab7633104a3dad1db26cdce2397d10c87b502b685dc5ccc7bddd9f7cdc86e1ef38834f5ed144e50155e7ca71ac9833d3f27; TSbcb913d5029=08a625aae3ab28008620521277008b851fdcbb8cb30abf655340f501b1a5e0c88ecc6f9076797c0b8c59788323b4acc7; TSbcb913d5078=08a625aae3ab2000e9d3b7c72f6d24586476bf79de8a7cb43e078eea8304a10a3a1d92cc08e8e25e08ab93f6e41850013f575e7c55c2b0b01bed26daf58c753bd02ea702b6c269573c8cf30dfea0e3d15f87c0e4631ef968e1dd73181989381a9fa46ea96b636a2bf46136c9cd3ed7a10ef7a90f7faedd31be1b128edfc9cb9690786a7f19eb5ae8ae6ddb4d5964103cf94b591afd90209eb1abc34dbeaef97b896d9ee868c4875331621cc85476e12c46a53301e70a0897b72699be345b4d9aa0865b11c273b8c10813212f70a587f79ef0e62f5cd75ff71777c15f0da9527062c70a596840fa51ceba1fd9e9ab1230fcfe971785fe85f03dea9bccb6a05f1c369e6feda66571720ed889031d1c6648b0449bd33ab4b5823a21aa45749839a39bd7e60846fd6db3358750525a59c09ade731038cbf8f7b663748381c0e8fa2783956c6c67b70e931dfa17986af7cc2c6154acf8d18508583c09e246c85907db8e990b50b5fa89bcec7f3a8ca81c9c85873914655f669d9633ff9a6a42d7e6c1; TS7a8c3458027=08a625aae3ab20006eacc0aaa41121a3dd43815d5856a5f3007771672b0b900172d8c950536d05bd08fddb78ee1130006daa6f34ac3bf969d18a0612fd3c637f36dc2ac50921cfe5072d7ca6dbfec3734f97863c380e307d5299cd2c141e914a; BIGipServeridam.metrosystems.net-80=!NXSJTdtgHVWcR8HUzUGSRTsG4v6oUb8lOuo1eqqq6yqvz14ZmX%2BKXrJNo%2BNgp0caJN7XxEpEjIunVIo%3D; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; TS010a0d4d030=0169fc3859c8a1694c718dd4c9cbc5f955a0e6e3888514ce92d8f852fbf8de5ee327208d910c0444ad93b2f86eb1189e96dfcb973d",
    'Accept': "*/*",
    'Accept-Language': "en-US,en;q=0.9",
    'Connection': "keep-alive",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "TSbcb913d5078=08a625aae3ab20003e73c4fd648aa67ee379b63ea1fabd45902d8764b9cd7a6b291685a5d339e0ae08d47f558a185801eda3150925464713021cdf27ac72259085ddb7a53d1323d41f55f665f84564fb914bdac942cd27498bdd97ded07913599164c27a36f34f489a0e0abe5a179cd37d46a3572123e6949a3d125fed85963f1a2194e8606c61c4481fc09ba93eb8f5f2b704499569b14657c733099a20b2f664c8ece673f13f6dbbe20b0ab3659ead880ee0e5a2c546172a422f4b1551e3ad7998b98f2f3435124624774c5537fd10a017d1aaee5b6452e3847527e3462b6ac89c4c08ec06183023f4c310a2a4596303045d1b7cffed6c6859c67f4adb0bfc39ae55e93c6c3a5c503ec245e279bcefdef329a189d8f941d70c793e51de541df5b76476abd8d9a8fba1e9f216a3c1b13bda6b209f259f97983cd6a3586f371e28d68d2b10a7eae6c511dcadcd674e8df56919a76626896f1ef63debd1607c41bc684edd2f0d0c8126ebffbc5819f2c587f89f9b605c753330bfcf697f95b90856b0ccf4db926f04; TS00000000076=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d09d000db00110cbd517c033f9e00a766304105770d9e5617ff2b82418778c303e6901cab617d880134f21af992c52bd0848eabaac4e67f2d467382b45f5b2bcd3c24a73750494ea0de38f9862100359296e051ed62fde2651e4a2498cb9a312f9aabd1ddbeb8b7dea5e65a7e972050222203e70a2376a422121219b4133e940ff4bb84c6ccd36982ca59d8488247d47bd07205a470e14aad82592ffbc08d0aa5f457152dae9b17bdfcb32f58eaf5fd5d49d12404a1b64bb2ecd2415db00b01bfff8c890c93ee452fcb4da06f70514f2f7ad621; TSPD_101_DID=08a625aae3ab2800918f46af19d5db611e1e1d5e45f135319c27b41a2a9ca3b4baa16f63a9a1e4dc6f238b44846fea4d083fa35a9d0638000196598a6788f820190fd91126bd4561c594ef755e85f5172c6ea635a2f76f666492ff65060daba3d822cc765a8bb390376693b6754cc759; BIGipServeridam.metrosystems.net-80=\u00217fsxS8fkT+qSuQxlllsv0yPj1IQ7JOUaBQydVbRGSBx/xQL5PSC8YRrhQ9xlYvGEIElTtaZkFawfJeY=; TS010a0d4d=0179c221a7d84e035721141d2f7d8f6ab83fb804977c63ab22a0a186605197ea2d1a96daea0c6c2f8f948c2ecf00300e19c3e629c2fa62713e479c7b6d1979e8bf25504b15; barrier=ARFCzCofonmfhkeucC99NXBklTCbhmmBEKpIfLkg6ttKpzJzMME3U2B0YnciQn513eazXeCCeX/vhXRUWFgSLjlSrVW4RagJN80dM6Lu82EtpWamHudu7uE18pk=; TSbcb913d5029=08a625aae3ab28004afb46397463362b9f9eb8775d7ab74376c8aa0ef56d5f4a7274ec113f0566c968f054ad818055dc; TS7a8c3458027=08a625aae3ab200064365697b73c5e5f7e0d285f4b43bbec1b16f9e4b7ba7fd88adf26d5f8a5bb5108905514e411300033fae4ebbb2a8b760474d894f8725925896c0cf7269a4cc221c9cf90585b03b68800c9294f3321d827000e8baa023fb6; _dd_s=rum=1&id=eee04a66-6cf6-4e1a-843c-972dcf235171&created=1668201465597&expire=1668202415769",
    'DR-Trace-ID': "idam-trace-id",
    'Origin': "https://idam.metro.bg",
    'Referer': "https://idam.metro.bg/web/Signin?scope=openid+clnt%3DBTEX&locale_id=bg-BG&redirect_uri=https%3A%2F%2Fshop.metro.bg%2Fshop%2Fcart%3FidamRedirect%3D1&client_id=BTEX&country_code=BG&realm_id=SSO_CUST_BG&user_type=CUST&DR-Trace-ID=idam-trace-id&response_type=token+id_token&nonce=9849d97781d64d8eb2768e792769f202&state=fc764b0c9c404b96909b551ae5c2b4e2",
    'Sec-Fetch-Dest': "empty",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Site': "same-origin",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest",
    'X-Security-Request': "required",
    'sec-ch-ua': ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': ""Linux""
    }

conn.request("GET", "/web/authc/authenticate", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

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
