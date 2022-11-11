Authenticate.py

#SELF NOTE: Types of tokens - Id & Access
#SELF NOTE: Extract token data tool: https://jwt.io

#Login: Request URL
https://idam.metro.bg/web/authc/authenticate
https://shop.metro.bg/explore.login.v1/auth/loginWithIdamAccessToken?country=BG

#Data: Acces Token

#cURL: 
https://shop.metro.bg/explore.login.v1/auth/loginWithIdamAccessToken
#File name: filename
/explore.login.v1/auth/loginWithIdamAccessToken
#Referer:
https://shop.metro.bg/shop/cart?itm_pm=cookie_consent_accept_button

#1. RESPONSE DATA

#1.1. Responce_JWT:
eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJJc3N1ZXIiLCJhdWQiOiJBdWRpZW5jZSIsImp0aSI6IlpDYTlUSVU3b2htRml3cHJsNnhzWFEiLCJzdWIiOiJiZXR0eSIsImVudGl0bGVtZW50cyI6ImZDT1IiLCJzdG9yZUVudHMiOm51bGwsInVTdG9yZUVudHMiOiJ4QVMseENMT1dTLHhBT0wsdkFMLHZTUFIsY1NDT1IsY1NDT1csZlBPLGZMRE9SIiwidVN0b3JlcyI6IkJHRDIyIiwicGF5bG9hZCI6IntcInJvbGVcIjpcImN1c3RvbWVyXCIsXCJ1cG5cIjpcIjEwMDExMDAwMjI3MjYzNTVcIixcImNhcmRob2xkZXJOdW1iZXJcIjpcIjFcIixcInRlY2hVc2VyUm9sZVwiOm51bGwsXCJ0aWVyTGV2ZWxcIjpcIjRcIixcImNvdW50cnlcIjpcIkJHXCJ9IiwicmVmcmVzaEZvcmNlZCI6ZmFsc2UsInNpbmdsZVNpZ25PbiI6ZmFsc2UsInZhbGlkdW50aWwiOjE2NjgxNzEwOTg0MjgsImV4cCI6MTY2ODE3MTA5OCwiaXNzdWVEYXRlIjoxNjY4MTY3NDk4NDI4fQ.dKlJvZL79MskLZHBfurWDfTnZbd6peR3yj1teEAeo1LJeDJaKmBy6xROGJxZ1fz3uAqde0Av167vCqXKHAByeHOO3gFPm-jiP2mWf2SOPrdz3qPmjH6Z90PJEFAjOI7C0SMpxsdZmA6R6GbjDNge6oQf4wrJKzehvelsop2ME5eH-LuFKIuUuGmIeq9x2sTSzV059Pd4Gcj4dv8jTo7fAd7OicmUcuYaLfxQfVmsNk3QLP6_fAnP6PIJBNtR9p0B7cxo7jlavW0sFFqokMXNQXaU6xKh0JAkeKjZPKVFF-OAyiECqGujbOMlo0C9O-CdifkhhI92BS472UaH0KLVAg

#1.2. Responce_compresed_JWT:
eNpVUsmSozgQ/aLqYLHxcMSsEiAwZrMuEyDAIMDGhY2Br29RVTPRfVAo4uVbMlMqF1jnJmm8Bp6jFfCogfKvcoEDEd0NhEREPE5B46iwLpLThh2LJBhwsqf4DEbQD1x2BhLoBu0SdtE5jsRcqJ9B34nEgiO61Wti6Jt+LRKw6RucBlz5pY1fhdlxuRk/mR9HFubTYy3kwTfflBccMY7Feun3fG6+R3CLw7/wBu5OsTuWOnJDvggdqz6G3HssWsN1LBxGBhgvPNo8f24y4u7oOyZ2A10+g+bdFDHichF2X/kttAINLBtOTGOfm3KNVYbfngTc4MR6JYAOBPSIJ2Iw5Um8pCoYUxXyxNx/16j+djV9djXl7VIguvSyopDpmnnT1aQP7rkwtziFXpHwbB/wR2d8c25BdxHqmAjxEvXyiOP3//OzHC5jmaEZCziZf3TBf95Tse3x1n3jbBbGl79m6eOenTXT8UR61G0z4d4YiRCxnaIh7wuWgwYs7P28+bOG2Qfp2s03S1gfVBcQvc5o1d9eeOVcet3ecUeYnxteBE/TRTdU9p76brIUsTeP9UsadIDeZ0QvO8YRkdbukAZ21elXYXdwws5BdsfWwdaxen0mWhXecF5IQxmIC+Wfpa6Ud96BpQYzuz8u0hx4JpwxX63iS3kUJadMvHSY1EdqW8pxKS3PE6+G33/Qxhf6pBLOnv9ZrOLD76klYZnzoW4o1AMHlTu7wzwWuFekQDJzqqFrKd1P1e79Ce21rKeyG++D4Or70vpwXoYNXtHL7EH5kGdhDM9rzO1lv9iZhO6K6R8a3g+VUhw8tu+IvC6ZU82nKu5H1Ionx5f+rZSbL/kAHtEzkAfueCDz/UC7bEq40TAe99ZN0SnNImm2aw4qbWlT7NuxYXx4ytLo6sN80dxzuzunyt6HWjRVW9dAFo7n3UGIMouznVi5/ga9v0tE

#1.1.1 Response_JWT_decoded:

#1.1.1.1 Response_JWT_decoded-HEADER:
{"alg": "RS256"}

#1.1.1.2 Response_JWT_decoded-PAYLOAD
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

#1.1.1.3. Response_JWT_decoded-VERIFY SIGNATURE
RSASHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),)

{
  "e": "AQAB",
  "kty": "RSA",
  "n": "ApmXRtqOGJPJrzaNXFVU6tzqJ5V9qEx-JoYYGUMxZDGThbiWueKP5ktOsTU5fBKvM23EmEWyyffB-I1lxftOZCy-Jl2ubLWqHRG6sjVMYTaL6qJ0osNAZ-k5ALrI1xj0IiGZUQr2elIp0Gj94ferSh-MazUHw8YP2bnxzcCL1wyLH3jGq6TALMTJFPobCO_HPT_SZC_tyQ7kQW4cSOONIuuF4j8LUMIUcAQuUPL_DEwwqbXYHI7CRdqAMPcn_q1KHPgXl1VhMlcualKfA9cDXY_WstVp9UK6y-7JMRTVHna0nkRft3BgH_3fBk-e6j_GRyLF0GJHc-UcZyIck1b9U-PHYPB9GGU"
}

#1.1.1.4. Response_JWT_decoded-STATUS: Invalid Signature

#2. REQUEST DATA


#2.1. Req_payload
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IktfYWE1NTAxNWEtMjA2YS0xMWVkLTk4ZDUtZTJjYzEyYjBkYzUwIn0.eyJrZXlNYXAiOnsiY2RtIjp7InBlcnNvbiI6IjRlYWViOTEwLTI0M2EtMTFlZC1iYTY4LTMxNWMxYjczMjFiZiJ9fSwiZW1haWwiOiJvZmZpY2VAdGVydmlvbi5iZyIsImFjY291bnRDb250ZXh0IjoiIiwiY291bnRyeSI6IkJHIiwibG9jYWxlIjoiYmctQkciLCJpYXQiOjE2NjgxNjc0NDIsImF1ZCI6IkJURVgiLCJ1c2VyVHlwZSI6IkNVU1QiLCJpc3MiOiJodHRwczovL2lkYW0ubWV0cm8uYmciLCJleHAiOjE2NjgxNzEwNDIsImF1dGhvcml6YXRpb24iOltdLCJyZWFsbSI6IlNTT19DVVNUX0JHIiwic3ViIjoiVV9mNDIwYWNhOC1mNjkzLTRjMTUtYjkyMy03NTVmOTU3N2UyMDAiLCJ1cG4iOiJvZmZpY2VAdGVydmlvbi5iZyJ9.AMIdcNI3S2IMgL9HaW-_buWsNrja1Ikg4Gg13v-VFBpLsJqAqc8_tlRFgnKjx8yuyI_pCeH_yjCGYZUbpSECFd6o6HXQtMVASFQsFH8O105X2KoEzYlOAB1-k-fxLL34xaAU2x-pfP8FPPpflUw45iSezNx_XKtmd6Scp2p9xSZtg9om78ttPxiB5XKJAIBMXj802FOxNis6RjnxkavaEuxHNTaTg_ceH9Hc9EbZUvFFSg_7wlSWC2X28WuOaDnIjhE1gZtcehOlfQt44HigBHRuE5JcU203xpxZ92cjh1xXuOHvAc585p3YJtOoMSz45xcngAmcV-25ayA_gtkiOn5fsU0_eLA

#2.1.1. Req_payload_decoded:

#2.2.1.1. Req_payload_decoded-HEADER:
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "K_aa55015a-206a-11ed-98d5-e2cc12b0dc50"
}

#2.2.1.2.  Req_payload_decoded-PAYLOAD:
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
  "iat": 1668167442,
  "aud": "BTEX",
  "userType": "CUST",
  "iss": "https://idam.metro.bg",
  "exp": 1668171042,
  "authorization": [],
  "realm": "SSO_CUST_BG",
  "sub": "U_f420aca8-f693-4c15-b923-755f9577e200",
  "upn": "office@tervion.bg"
}

#2.2.1.3. Req_payload_decoded-VERIFY SIGNATURE
RSASHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),)

{
  "e": "AQAB",
  "kty": "RSA",
  "n": "ApmXRtqOGJPJrzaNXFVU6tzqJ5V9qEx-JoYYGUMxZDGThbiWueKP5ktOsTU5fBKvM23EmEWyyffB-I1lxftOZCy-Jl2ubLWqHRG6sjVMYTaL6qJ0osNAZ-k5ALrI1xj0IiGZUQr2elIp0Gj94ferSh-MazUHw8YP2bnxzcCL1wyLH3jGq6TALMTJFPobCO_HPT_SZC_tyQ7kQW4cSOONIuuF4j8LUMIUcAQuUPL_DEwwqbXYHI7CRdqAMPcn_q1KHPgXl1VhMlcualKfA9cDXY_WstVp9UK6y-7JMRTVHna0nkRft3BgH_3fBk-e6j_GRyLF0GJHc-UcZyIck1b9U-PHYPB9GGU"
}

#2.2.1.3. Req_payload_decoded-STATUS: Signature Verified

#3. COKIES DATA

#3.1. Cokies_compressed_JWT:
eNpVUltzojAU/kXd4SJaHlUChEoskATMiyNB7mhaEIRfv9B2d3YfMpn5znc55yTX0cljixfHwgnIBGVUOPqv6+gIrroL6HAVySyCxWHv5EnoLdguCX3BQq1kAWxhI6RLANew6lJqi8JVfZ9RP71G4jPANECy6WOVL/opCeGiL1jkS9cvLX0kVi3FFu1mP4mPs0/DDCzDb76lj4zMHHvupdHk2BpaeKP4P7xwVh512ytALpYTfLDzHZaGNqlM92AzTEzYnmS0eP7cvGX17v1gMdcHegCLoUgokmLVqb/yK8f2DTguOLdMLbb0nO1n/NZxeHP6uVcOS8Fhg2Su+n0c0jHawzbaOzK3tO9aCQbXAE/X2A5uCVW3PE0Iz7riuehy3vj3WHlWLHKOSSjP+3B+dOY35+bXJyWnXKEjafSW0eHv/HOOdJkzsUUVFj5/dP4f7z5Z9nirv/F5lpmvf83S0GY+0wWwnjeoXmZijdlyhcw7RSJukjkHCaZo73Hxb43NH6SuFt9LOPdRAgWV2RNNYECGq7iGu7zjis9+Lj4pRwOoLt5K7jgUlwjNb07BKfJrWN6fqDytZo6KDG9C5XZKvV8UkKMCn1EUvZz9cznZXSrCIZ+KeIX6eypdzwkRn7d9DlcX567FJDtJTxHq2xt6fjIwZt3GxNg7eNdtp+5Ce9chN7Gi6qgw/ullvW11yeGxe02lYxoGeIpDcvbeNHnAAEfatCbwXfbBh9DPnLjt7qiAYuyHYVIrfLm/OA49GyRVhGeSQLvkqGgn+hB+slm/jHWWnsPVTWzwGzgfPLLvzzyApIIaQGbAdSki4rXZAduskK3ATU6ie3aKS+Otrti6mFqx3vWNuQ7eNsKsgC8oifZdL9rXlbYmPqJPIEO356J7VFM2TVmbuZG+SvHGjgDYVNKHhTJx/yBYXtUleL3QbdM/Pkby2P4Gzs9OWw==

#3.2. Cokies_idamUserIdToken:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IktfYWE1NTAxNWEtMjA2YS0xMWVkLTk4ZDUtZTJjYzEyYjBkYzUwIn0.eyJleHAiOjE2NjgxNjkyNDIsImlhdCI6MTY2ODE2NzQ0MiwiYXVkIjoiQlRFWCIsInNlc3Npb25fc3RhdGUiOiJSazBGWWppTVNBOURtVUlhdXpuTUpFR29UcmZNT3NSQVRCS2EtYlpiNlNVLktkUENVN3BPIiwiaXNzIjoiaHR0cHM6Ly9pZGFtLm1ldHJvLmJnIiwiZW1haWwiOiJvZmZpY2VAdGVydmlvbi5iZyIsIm5vbmNlIjoiYzZiOTRiYjYyYjI4NGJhYmE4YmIzY2U5NDg2Yjk5ZTMiLCJjX2hhc2giOiIiLCJzdWIiOiJVX2Y0MjBhY2E4LWY2OTMtNGMxNS1iOTIzLTc1NWY5NTc3ZTIwMCIsImF0X2hhc2giOiJiYXFWTjBWRUhKdnREbk5rTVR4MGx3IiwicmVhbG0iOiJTU09fQ1VTVF9CRyIsImF1dGhfdGltZSI6MTY2ODE2NzQ0MiwiYW1yIjpbIlVTRVJfQ1JFREVOVElBTFMiXX0.AIc7oB6ZUZlS0bNQ809z0txS46E8jD3ub_FXnpnIXJgFRNCOKVGZqk2pnaXyW6Kxai7x_PCtLHmzxKtnAlQrdk0Bt5fNRMq2m7G7HLh8PU6lSjUDvpJ-QD81MKSvedLVvDaropmcRTNs6L9lFsdT0qShFDIWIGiddmbHxfsWcYTXAElNiRpa-cGDfi8pbpq1X0bwvQchAzSh8BdstKJj-qjMi5XJEXqCXTR_xCvpHsjMLRE-aMelAHYbDvNRs_NURUsE8Qdr1V3u5YJxEDYZ84bBqoxNnrYTfjtUE2eX2wx7iKA3qbD-vd0pKqLuacqNy7MK2MfMsur9wBfdkjy8EvLlH_ntJik

#3.1.1 Cokies_compressed_JWT_decoded:

#3.1.1.1. Cokies_compressed_JWT_decoded-HEADER:
{}

#3.1.1.2. Cokies_compressed_JWT_decoded-PAYLOAD:
{}

#3.1.1.3. Cokies_compressed_JWT_decoded-VERIFY SIGNATURE:
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),)

{
  your-256-bit-secret
}

secret base64 encoded #CHECKED

#3.1.1.4. Cokies_compressed_JWT_decoded-STATUS: Signature Verified

#3.2.1. Cokies_compressed_JWT_decoded:

#3.2.1.1. Cokies_compressed_JWT_decoded-HEADER:
{"alg": "RS256"}

#3.2.1.2. Cokies_compressed_JWT_decoded-PAYLOAD:
{
  "exp": 1668169242,
  "iat": 1668167442,
  "aud": "BTEX",
  "session_state": "Rk0FYjiMSA9DmUIauznMJEGoTrfMOsRATBKa-bZb6SU.KdPCU7pO",
  "iss": "https://idam.metro.bg",
  "email": "office@tervion.bg",
  "nonce": "c6b94bb62b284baba8bb3ce9486b99e3",
  "c_hash": "",
  "sub": "U_f420aca8-f693-4c15-b923-755f9577e200",
  "at_hash": "baqVN0VEHJvtDnNkMTx0lw",
  "realm": "SSO_CUST_BG",
  "auth_time": 1668167442,
  "amr": [
    "USER_CREDENTIALS"
  ]
}

#3.2.1.3. Cokies_compressed_JWT_decoded-VERIFY SIGNATURE:
RSASHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),)

{
  "e": "AQAB",
  "kty": "RSA",
  "n": "ApmXRtqOGJPJrzaNXFVU6tzqJ5V9qEx-JoYYGUMxZDGThbiWueKP5ktOsTU5fBKvM23EmEWyyffB-I1lxftOZCy-Jl2ubLWqHRG6sjVMYTaL6qJ0osNAZ-k5ALrI1xj0IiGZUQr2elIp0Gj94ferSh-MazUHw8YP2bnxzcCL1wyLH3jGq6TALMTJFPobCO_HPT_SZC_tyQ7kQW4cSOONIuuF4j8LUMIUcAQuUPL_DEwwqbXYHI7CRdqAMPcn_q1KHPgXl1VhMlcualKfA9cDXY_WstVp9UK6y-7JMRTVHna0nkRft3BgH_3fBk-e6j_GRyLF0GJHc-UcZyIck1b9U-PHYPB9GGU"
}

#3.2.1.4. Cokies_compressed_JWT_decoded-STATUS: Signature Verified
