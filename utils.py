# import requests

# cookies = {
#     'visitorId': '0000000003D201012D68117A7AFFA482',
#     'TealeafAkaSid': 'v6TxX2F5knvrPs0WmTFdpVIGjix8jdzZ',
#     'sapphire': '1',
#     'UserLocation': '92656|33.580|-117.740|CA|US',
#     'usprivacy': '1YY-',
#     'stateprivacycontrols': 'Y',
#     'sddStore': 'DSI_259|DSN_Aliso%20Viejo|DSZ_92656',
#     'fiatsCookie': 'DSI_259|DSN_Aliso%20Viejo|DSZ_92656',
#     'ci_pixmgr': 'other',
#     'accessToken': 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIxMjFjZWZjNS1jZjQ0LTQ3MTktOThmMi00Zjk1MmI1MmYyZDAiLCJpc3MiOiJNSTYiLCJleHAiOjE3MDc0MjI5MjMsImlhdCI6MTcwNzMzNjUyMywianRpIjoiVEdULjg5ZDk4MGE0MTliNDQyMDA5Y2U3NjkyMjMyNWJmYjZhLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjBhNWMxZTBkMjc1YzE0NzIyZmUwZjk5MWU2MzkyZTk2NTAxYjNjNDcxMGZkN2NlM2E2MWYzN2I2OTFjY2UzOTMiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.CzgAuhT3kBVTQUChH4m8WNa8osu4_3H1cSVIa9asqSHl8UVlq5vGDYuSQOJDW9TZdl1NP6uZwfSgt9cqET7E0or3cMhuZcW6IUGVUtertM5pmR75tn845xu6aY82Y0GQlElheWYlHSEj7f6nKn6ATDuaMcQeEp4KujE7HYXXEtRTb5_YWX6NS0zI29i8YRhtBP9fu2wDaQhQUPDhHPaIXNqB2pNf9iO0vV7P5JI9ApUegHnVpFjFnza3YZeQoH3YL0IsLI4JpLbuJF84Oe27YPu5FF2BJomnxPaQdWoJXHIUC082PeRq-g6pDIMBsG458pO3nkJnupM7-Cxzxj1k6w',
#     'idToken': 'eyJhbGciOiJub25lIn0.eyJzdWIiOiIxMjFjZWZjNS1jZjQ0LTQ3MTktOThmMi00Zjk1MmI1MmYyZDAiLCJpc3MiOiJNSTYiLCJleHAiOjE3MDc0MjI5MjMsImlhdCI6MTcwNzMzNjUyMywiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.',
#     'refreshToken': 'aOEkbwnnm2jem3w4KeQhH2pP69QSMvD7PX6jmR0GC80xubg_pyVPUgTNyc0PxcKrLU94uySxjbar407N7byfug',
#     '_mitata': 'YWFkMjMyYTIyYzFhZDQ0MGMxNTVhZTdmYWMxNWMxMjU3YzE5NzdjYmVjN2FjZWNlNDJkZDVlMzRkYWU1Zjk2MA==_/@#/1707372572_/@#/cdvrESozH3zJL7nN_/@#/NDY1YmJhNDIwZTcxNmY4NzUxZWU4NDc4ZjVkMDUzYzEzMTg3NmE3MGI2MWFiNGI0ODZmNjlmN2EzMTUwOGM4YQ==_/@#/000',
#     'ffsession': '{%22sessionHash%22:%2253e599c75c9e1706897491697%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=mattel&tref=typeahead%257Cterm%257C0%257C%257C%257C%257C%257Chistory&category=0%257CAll%257Cmatchallpartial%257Call+categories&searchTermRaw=%22%2C%22prevSearchTerm%22:%22mattel%22%2C%22sessionHit%22:9}',
# }

# headers = {
#     'authority': 'redsky.target.com',
#     'accept': 'application/json',
#     'accept-language': 'en-US,en;q=0.6',
#     'origin': 'https://www.target.com',
#     'referer': 'https://www.target.com/s?searchTerm=mattel&tref=typeahead%7Cterm%7C0%7C%7C%7C%7C%7Chistory&category=0%7CAll%7Cmatchallpartial%7Call+categories&searchTermRaw=',
#     'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'sec-gpc': '1',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
# }

# params = (
#     ('key', '9f36aeafbe60771e321a7cc95a78140772ab3e96'),
#     ('tcins', '14789178,88381250,89129728,88182368,14783201,89129732,89140823,89129731,82383740,87363491,87883158,87883202,90508398,88178854,90900047,90900060,90900054,90900053,89854310,90006879,88182369,89854179,90979980,90507511,88085384'),
#     ('store_id', '259'),
#     ('zip', '92656'),
#     ('state', 'CA'),
#     ('latitude', '33.580'),
#     ('longitude', '-117.740'),
#     ('scheduled_delivery_store_id', '259'),
#     ('required_store_id', '259'),
#     ('has_required_store_id', 'true'),
#     ('skip_price_promo', 'true'),
#     ('visitor_id', '0000000003D201012D68117A7AFFA482'),
#     ('channel', 'WEB'),
#     ('page', '/s/mattel'),
# )

# response = requests.get('https://redsky.target.com/redsky_aggregations/v1/web/product_summary_with_fulfillment_v1', headers=headers, params=params, cookies=cookies)
# response

import ssl
print(ssl.OPENSSL_VERSION)