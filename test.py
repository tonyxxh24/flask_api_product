import requests
import pandas as pd



keywords = 'baby products'

def get_products_summary():
    cookies = {
        'TealeafAkaSid': 'v6TxX2F5knvrPs0WmTFdpVIGjix8jdzZ',
        'sapphire': '1',
        'usprivacy': '1YY-',
        'stateprivacycontrols': 'Y',
        'fiatsCookie': 'DSI_259|DSN_Aliso%20Viejo|DSZ_92656',
        'visitorId': '018D8FCF2F790201876B2BAB437C557A',
        'UserLocation': '92612|33.660|-117.820|CA|US',
        'egsSessionId': 'c92e82ec-bf56-4c3c-ae0d-4f5f0230227d',
        'accessToken': 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIxMjFjZWZjNS1jZjQ0LTQ3MTktOThmMi00Zjk1MmI1MmYyZDAiLCJpc3MiOiJNSTYiLCJleHAiOjE3MDgyMDkzMzMsImlhdCI6MTcwODEyMjkzMywianRpIjoiVEdULjQ0MTVkZThiODgwNzQ2ZTNhZjJlZDAyOGM3NTc4Yjk3LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjQ4ZDhjYWM4NGFkNmEwOGJkZTliZjNkYjJiNDNjY2Y5MWY3Y2ZjNGNjM2JjZGVkYjhjMDdhY2FhYTNlZWQ4YmQiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.DlbKKftFAjAsWrE5fYcyA9fUCqEuNR8E-pXh-v2PsqSWKLHhgrHo3n4txV2XWxnHaBoQIq4ukLhKgsTrLpzT1vMTWb0Sa7FUCt7MBe4bQ5lFs7eopjYxxi9WMyuosK7ikT____9JDma1Ih__Xj-hRI9NYeEzCahm8LuUml-ANR8DLn9mF98_uRLMqqyuPSyPIVR3nrJOTTdQogbW7IpMRQotjiZq10yf63b0BA6XbOkY-vy-ER_wrhvMzcq_VB1pj1egryQJKPJVpvbDtr1KlTn5mJytvMf9OF_iFASg9FpC4gFRlrnK41C9wDFDBibtqGznI_aiKXIj2W1ll9UT8A',
        'idToken': 'eyJhbGciOiJub25lIn0.eyJzdWIiOiIxMjFjZWZjNS1jZjQ0LTQ3MTktOThmMi00Zjk1MmI1MmYyZDAiLCJpc3MiOiJNSTYiLCJleHAiOjE3MDgyMDkzMzMsImlhdCI6MTcwODEyMjkzMywiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.',
        'refreshToken': 'mYy6P3EOpuhUhCu9dnyL6Or6cBJFPdEvUyYPc3MpoIeIRPGca36IhkhjN2taSmSrLTI5VUK5iGXqwl2bUwl1hA',
        'ffsession': '{%22sessionHash%22:%2253e599c75c9e1706897491697%22%2C%22prevPageName%22:%22home%20page%22%2C%22prevPageType%22:%22home%20page%22%2C%22prevPageUrl%22:%22https://www.target.com/%22%2C%22prevSearchTerm%22:%22mattel%22%2C%22sessionHit%22:25}',
        'ci_pixmgr': 'other',
        'sddStore': 'DSI_3233|DSN_Irvine%20University%20Town%20Center|DSZ_92612',
        '_mitata': 'Y2RlZjAzM2MzNTc2YzM5MTcxYjhiODJlNDEzNGQ2MzJlMTZlNjc1NTdiNzc3NWYwYmYyN2VlYmE1ZmNhODI3OA==_/@#/1708122999_/@#/cTFNaWbiIZyWjCb7_/@#/MGJiM2YzNDUxZmU4MTNhZDU4NDE5NjAxMzFkNzM2ODVhNmQ5ZWM3MzlmNTQzODIzMjAzOWEyYTcyMmE3NGRkNA==_/@#/000',
    }

    headers = {
        'authority': 'redsky.target.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.7',
        'origin': 'https://www.target.com',
        'referer': 'https://www.target.com/s?searchTerm=body+products&category=0%7CAll%7Cmatchallpartial%7Call+categories&tref=typeahead%7Cterm%7C0%7Cbody+products%7Cbody+products%7C%7C%7Cservice%7C%7C%7C%7C%7Ccategory_v3&searchTermRaw=body+products',
        'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    params = (
        ('key', '9f36aeafbe60771e321a7cc95a78140772ab3e96'),
        ('channel', 'WEB'),
        ('count', '24'),
        ('default_purchasability_filter', 'true'),
        ('include_dmc_dmr', 'true'),
        ('include_sponsored', 'true'),
        ('keyword', 'body products'),
        ('new_search', 'true'),
        ('offset', '0'),
        ('page', '/s/body products'),
        ('platform', 'desktop'),
        ('pricing_store_id', '259'),
        ('scheduled_delivery_store_id', '3233'),
        ('store_ids', '259,300,3315,2163,2128'),
        ('useragent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'),
        ('visitor_id', '018D8FCF2F790201876B2BAB437C557A'),
        ('zip', '92612'),
    )

    response = requests.get('https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2', headers=headers, params=params, cookies=cookies)
    print(response)
    return response


#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&channel=WEB&count=24&default_purchasability_filter=true&include_dmc_dmr=true&include_sponsored=true&keyword=body+products&new_search=true&offset=0&page=%2Fs%2Fbody+products&platform=desktop&pricing_store_id=259&scheduled_delivery_store_id=3233&store_ids=259%2C300%2C3315%2C2163%2C2128&useragent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_15_7%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F121.0.0.0+Safari%2F537.36&visitor_id=018D8FCF2F790201876B2BAB437C557A&zip=92612', headers=headers, cookies=cookies)

# print(response)