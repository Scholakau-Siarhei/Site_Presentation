"""This is locators for API page"""

"""For Pizza"""
URL_PIZZA = "https://dominos.by/api/web/pages?path=%2Fpizza&language=en&cityId=2"
headers_pizza = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': '_gcl_au=1.1.1747184498.1687546128; _ym_uid=1687546129860396183; _ym_d=1687546129; '
            '_tt_enable_cookie=1; _ttp=s9WBmjncqfvwcbtOf3VMseX5KrU; _fbp=fb.1.1687796267759.'
            '481841012; _gcl_aw=GCL.1687953717.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-'
            'wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB; _gac_UA-71584615-1='
            '1.1687953725.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzSX2v0yNKlVILIw15QhVW'
            'YNWyUC_qSG0aAuYxEALw_wcB; cityId=2; popup-banner-shown=true; _gid=GA1.2.579693227.'
            '1689159727; csrftoken=REIxLYamkfEBVOHHAa0JRMhjRGF2i3ru; sessionid=q38ympxtmkqegil0g'
            'f3o7g29y1ysawpz; language=en; _ym_isad=1; _ym_visorc=w; _ga=GA1.2.1512419877.'
            '1687546129; _ga_FTX05WYR3P=GS1.2.1689609717.7.1.1689612429.12.0.0; _ga_BZNP2GVXYY='
            'GS1.1.1689609717.66.1.1689612429.0.0.0; csrftoken=7aifepPCyID8G84RjxJxTZ6C1hrM35s9; '
            'sessionid=853wacmcn55wckztb1x85olubx0griar',
  'If-None-Match': 'W/"a7e73-oE2tUzvA0PN3JUaxQzNlf/BmN3M"',
  'Referer': 'https://dominos.by/pizza',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/114.0.0.0 Safari/537.36',
  'X-NewRelic-ID': 'VwIOWFNUCBAEVFFUAQIDVFA=',
  'correlation-id': 'e6d887e5-d5bc-421f-be79-6e6c0710af83',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0OTk1NzAiLCJhcCI6IjQwMDY5NTE1Mi'
              'IsImlkIjoiMjUzZjQ5ZmZmODI5YWY5ZCIsInRyIjoiZTNjNTE5ZTE2MDNkN2VmNjRiN2ZiZGMwYWU2OGIyM'
              'DAiLCJ0aSI6MTY4OTYxMjUwNDA2OX19',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'traceparent': '00-e3c519e1603d7ef64b7fbdc0ae68b200-253f49fff829af9d-01',
  'tracestate': '3499570@nr=0-1-3499570-400695152-253f49fff829af9d----1689612504069'
}

"""For Lunch"""
URL_LUNCH = "https://dominos.by/api/web/pages?path=%2Flunch&language=en&cityId=2"
headers_lunch = {
  'authority': 'dominos.by',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'cookie': '_gcl_au=1.1.1747184498.1687546128; _ym_uid=1687546129860396183; _ym_d=1687546129; '
            '_tt_enable_cookie=1; _ttp=s9WBmjncqfvwcbtOf3VMseX5KrU; _fbp=fb.1.1687796267759.'
            '481841012; _gcl_aw=GCL.1687953717.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzS'
            'X2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB; _gac_UA-71584615-1=1.1687953725.Cj0KCQjw'
            'tO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB;'
            ' cityId=2; popup-banner-shown=true; _gid=GA1.2.579693227.1689159727; csrftoken=REIxLYa'
            'mkfEBVOHHAa0JRMhjRGF2i3ru; sessionid=q38ympxtmkqegil0gf3o7g29y1ysawpz; language=en; '
            '_ym_isad=1; _ga=GA1.2.1512419877.1687546129; _gat_UA-71584615-1=1; _ym_visorc=w; '
            '_ga_FTX05WYR3P=GS1.2.1689666147.8.1.1689666151.56.0.0; _ga_BZNP2GVXYY=GS1.1.'
            '1689666147.68.0.1689666151.0.0.0; csrftoken=7aifepPCyID8G84RjxJxTZ6C1hrM35s9; '
            'sessionid=853wacmcn55wckztb1x85olubx0griar',
  'correlation-id': '4b057c52-2359-4d9e-a813-a892ebcd956d',
  'if-none-match': 'W/"f5f-UWHqse0Croj1gOg+a43nYWAAO0M"',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0OTk1NzAiLCJhcCI6IjQwMDY5NTE1Mi'
              'IsImlkIjoiM2M4OWIzMTEyMTc5MmRiYyIsInRyIjoiMzRhOTViNzNjMmM3ZWUzZDgzZmRlY2MwNDBjZDZmM'
              'DAiLCJ0aSI6MTY4OTY2NjE2MTA1NH19',
  'referer': 'https://dominos.by/lunch',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'traceparent': '00-34a95b73c2c7ee3d83fdecc040cd6f00-3c89b31121792dbc-01',
  'tracestate': '3499570@nr=0-1-3499570-400695152-3c89b31121792dbc----1689666161054',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/114.0.0.0 Safari/537.36',
  'x-newrelic-id': 'VwIOWFNUCBAEVFFUAQIDVFA='
}

"""For Chicken"""
URL_CHICKEN = "https://dominos.by/api/web/pages?path=%2Fwings&language=en&cityId=2"
headers_chicken = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': '_gcl_au=1.1.1747184498.1687546128; _ym_uid=1687546129860396183; _ym_d=1687546129;'
            ' _tt_enable_cookie=1; _ttp=s9WBmjncqfvwcbtOf3VMseX5KrU; _fbp=fb.1.1687796267759.'
            '481841012; _gcl_aw=GCL.1687953717.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-'
            'wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB; _gac_UA-71584615-1=1.'
            '1687953725.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC'
            '_qSG0aAuYxEALw_wcB; cityId=2; popup-banner-shown=true; _gid=GA1.2.579693227.'
            '1689159727; csrftoken=REIxLYamkfEBVOHHAa0JRMhjRGF2i3ru; '
            'sessionid=q38ympxtmkqegil0gf3o7g29y1ysawpz; language=en; _ym_isad=1; '
            '_ga=GA1.2.1512419877.1687546129; _ym_visorc=w; _gat_UA-71584615-1=1; '
            '_ga_FTX05WYR3P=GS1.2.1689666147.8.1.1689666297.20.0.0; _ga_BZNP2GVXYY=GS1.1.1689666147'
            '.68.1.1689666297.0.0.0; csrftoken=7aifepPCyID8G84RjxJxTZ6C1hrM35s9; '
            'sessionid=853wacmcn55wckztb1x85olubx0griar',
  'If-None-Match': 'W/"1c2f-cNeMuvhv5YuVP9CmCRNzmPVnxWk"',
  'Referer': 'https://dominos.by/wings',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'X-NewRelic-ID': 'VwIOWFNUCBAEVFFUAQIDVFA=',
  'correlation-id': '6fc9ba06-9720-480f-8770-f84c7a3a674e',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0OTk1NzAiLCJhcCI6IjQwMDY5NTE1Mi'
              'IsImlkIjoiNDY0ZjFlOThmZmQ2OGQ1ZSIsInRyIjoiZmFlZGQ4MjQ0MDBlNDRhZjcwNThmZTVlZGE2NTY2M'
              'DAiLCJ0aSI6MTY4OTY2NjMwMDMyNX19',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'traceparent': '00-faedd824400e44af7058fe5eda656600-464f1e98ffd68d5e-01',
  'tracestate': '3499570@nr=0-1-3499570-400695152-464f1e98ffd68d5e----1689666300325'
}

"""For Potato"""
URL_POTATO = "https://dominos.by/api/web/pages?path=%2Fpotato&language=en&cityId=2"
headers_potato = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': '_gcl_au=1.1.1747184498.1687546128; _ym_uid=1687546129860396183; _ym_d=1687546129; '
            '_tt_enable_cookie=1; _ttp=s9WBmjncqfvwcbtOf3VMseX5KrU; _fbp=fb.1.1687796267759.'
            '481841012; _gcl_aw=GCL.1687953717.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-'
            'wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB; _gac_UA-71584615-1=1.'
            '1687953725.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC'
            '_qSG0aAuYxEALw_wcB; cityId=2; popup-banner-shown=true; _gid=GA1.2.579693227.'
            '1689159727; csrftoken=REIxLYamkfEBVOHHAa0JRMhjRGF2i3ru; sessionid='
            'q38ympxtmkqegil0gf3o7g29y1ysawpz; language=en; _ym_isad=1; _ga=GA1.2.1512419877.'
            '1687546129; _ym_visorc=w; _ga_FTX05WYR3P=GS1.2.1689666147.8.1.1689666301.16.0.0; '
            '_ga_BZNP2GVXYY=GS1.1.1689666147.68.1.1689666301.0.0.0; csrftoken='
            '7aifepPCyID8G84RjxJxTZ6C1hrM35s9; sessionid=853wacmcn55wckztb1x85olubx0griar',
  'If-None-Match': 'W/"15b3-kmfql/xLdUd6OQoMY3pm4BwWe9U"',
  'Referer': 'https://dominos.by/potato',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'X-NewRelic-ID': 'VwIOWFNUCBAEVFFUAQIDVFA=',
  'correlation-id': '32fd86e7-087b-49e7-a561-8a16a37a552d',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0OTk1NzAiLCJhcCI6IjQwMDY5NTE1M'
              'iIsImlkIjoiN2YxNjMwM2UwODQxYWRlNSIsInRyIjoiMmFhYWFiMmE4NTlkZThmMDNiNTJkNTg4NzBkZD'
              'MxMDAiLCJ0aSI6MTY4OTY2NjQzOTI4MX19',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'traceparent': '00-2aaaab2a859de8f03b52d58870dd3100-7f16303e0841ade5-01',
  'tracestate': '3499570@nr=0-1-3499570-400695152-7f16303e0841ade5----1689666439281'
}

"""For Bread"""
URL_BREAD = "https://dominos.by/api/web/pages?path=%2Fbread&language=en&cityId=2"
headers_bread = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': '_gcl_au=1.1.1747184498.1687546128; _ym_uid=1687546129860396183; _ym_d=1687546129; '
            '_tt_enable_cookie=1; _ttp=s9WBmjncqfvwcbtOf3VMseX5KrU; _fbp=fb.1.1687796267759.'
            '481841012; _gcl_aw=GCL.1687953717.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-'
            'wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB; _gac_UA-71584615-1=1.'
            '1687953725.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzSX2v0yNKlVILIw15QhVWY'
            'NWyUC_qSG0aAuYxEALw_wcB; cityId=2; popup-banner-shown=true; _gid=GA1.2.579693227.'
            '1689159727; csrftoken=REIxLYamkfEBVOHHAa0JRMhjRGF2i3ru; sessionid=q38ympxtmkqegil'
            '0gf3o7g29y1ysawpz; language=en; _ym_isad=1; _ga=GA1.2.1512419877.1687546129; '
            '_ym_visorc=w; _gat_UA-71584615-1=1; _ga_FTX05WYR3P=GS1.2.1689666147.8.1.'
            '1689666440.60.0.0; _ga_BZNP2GVXYY=GS1.1.1689666147.68.1.1689666440.0.0.0; csrftoken'
            '=7aifepPCyID8G84RjxJxTZ6C1hrM35s9; sessionid=853wacmcn55wckztb1x85olubx0griar',
  'If-None-Match': 'W/"59ff-rVwaQe6BdZUjY3Ggj86PnS79Ue8"',
  'Referer': 'https://dominos.by/bread',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'X-NewRelic-ID': 'VwIOWFNUCBAEVFFUAQIDVFA=',
  'correlation-id': 'eefbb1a3-7b3d-4ab3-bbfe-16f552ce990d',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0OTk1NzAiLCJhcCI6IjQwMDY5NTE1Mi'
              'IsImlkIjoiODExY2ZiMWM1YzZjMGVhMCIsInRyIjoiOWI1NzI3MzRmYWE4YTFhNzIwZDdiZDMwNTZlNmE5'
              'MDAiLCJ0aSI6MTY4OTY2NjQ4MjE4Nn19',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'traceparent': '00-9b572734faa8a1a720d7bd3056e6a900-811cfb1c5c6c0ea0-01',
  'tracestate': '3499570@nr=0-1-3499570-400695152-811cfb1c5c6c0ea0----1689666482186'
}

"""For Salads"""
URL_SALADS = "https://dominos.by/api/web/pages?path=%2Fgsalad&language=en&cityId=2"
headers_salads = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': '_gcl_au=1.1.1747184498.1687546128; _ym_uid=1687546129860396183; _ym_d=1687546129; '
            '_tt_enable_cookie=1; _ttp=s9WBmjncqfvwcbtOf3VMseX5KrU; _fbp=fb.1.1687796267759.'
            '481841012; _gcl_aw=GCL.1687953717.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-'
            'wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB; _gac_UA-71584615-1='
            '1.1687953725.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzSX2v0yNKlVILIw15QhV'
            'WYNWyUC_qSG0aAuYxEALw_wcB; cityId=2; popup-banner-shown=true; _gid=GA1.2.579693227.'
            '1689159727; csrftoken=REIxLYamkfEBVOHHAa0JRMhjRGF2i3ru; sessionid=q38ympxtmkqegil0'
            'gf3o7g29y1ysawpz; language=en; _ym_isad=1; _ga=GA1.2.1512419877.1687546129; _ym_v'
            'isorc=w; _ga_FTX05WYR3P=GS1.2.1689666147.8.1.1689666483.17.0.0; _ga_BZNP2GVXYY=GS1'
            '.1.1689666147.68.1.1689666483.0.0.0; csrftoken=7aifepPCyID8G84RjxJxTZ6C1hrM35s9; '
            'sessionid=853wacmcn55wckztb1x85olubx0griar',
  'If-None-Match': 'W/"307a-nx9QFIQmvPu/jRMDPx+h4Wnim4Q"',
  'Referer': 'https://dominos.by/gsalad',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'X-NewRelic-ID': 'VwIOWFNUCBAEVFFUAQIDVFA=',
  'correlation-id': '67bab2f9-c7c6-445b-806a-b536825f0494',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0OTk1NzAiLCJhcCI6IjQwMDY5NTE1M'
              'iIsImlkIjoiZTBlYjE3OGFiMjk3YTNkZCIsInRyIjoiN2VjMTRiZTZhNzQ0ZWRhODNlNzAxMDUxZWNlNj'
              'JlMDAiLCJ0aSI6MTY4OTY2NjUyMzYyMn19',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'traceparent': '00-7ec14be6a744eda83e701051ece62e00-e0eb178ab297a3dd-01',
  'tracestate': '3499570@nr=0-1-3499570-400695152-e0eb178ab297a3dd----1689666523622'
}

"""For Desserts"""
URL_DESSERTS = "https://dominos.by/api/web/pages?path=%2Fstarter&language=en&cityId=2"
headers_desserts = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': '_gcl_au=1.1.1747184498.1687546128; _ym_uid=1687546129860396183; _ym_d=1687546129; '
            '_tt_enable_cookie=1; _ttp=s9WBmjncqfvwcbtOf3VMseX5KrU; _fbp=fb.1.1687796267759.'
            '481841012; _gcl_aw=GCL.1687953717.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-'
            'wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB; _gac_UA-71584615-1='
            '1.1687953725.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzSX2v0yNKlVILIw15QhV'
            'WYNWyUC_qSG0aAuYxEALw_wcB; cityId=2; popup-banner-shown=true; _gid=GA1.2.579693227'
            '.1689159727; csrftoken=REIxLYamkfEBVOHHAa0JRMhjRGF2i3ru; sessionid='
            'q38ympxtmkqegil0gf3o7g29y1ysawpz; language=en; _ym_isad=1; _ga=GA1.2.1512419877.'
            '1687546129; _ym_visorc=w; _gat_UA-71584615-1=1; _ga_FTX05WYR3P=GS1.2.1689666147.8.'
            '1.1689666524.60.0.0; _ga_BZNP2GVXYY=GS1.1.1689666147.68.1.1689666524.0.0.0; csrftoken'
            '=7aifepPCyID8G84RjxJxTZ6C1hrM35s9; sessionid=853wacmcn55wckztb1x85olubx0griar',
  'If-None-Match': 'W/"5613-uBN+fHf7AZulbNESjxya9wvejq4"',
  'Referer': 'https://dominos.by/starter',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'X-NewRelic-ID': 'VwIOWFNUCBAEVFFUAQIDVFA=',
  'correlation-id': '91a53ab9-3e77-4d9b-9f5a-4545a4373a1d',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0OTk1NzAiLCJhcCI6IjQwMDY5NTE1Mi'
              'IsImlkIjoiZTkxNTE2NjQyZGEzY2JmYyIsInRyIjoiNGM5Y2JiMTI4YTg5MjRkNDJhNTc3Yzg5N2RlNTI4'
              'MDAiLCJ0aSI6MTY4OTY2NjU3Njc0NH19',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'traceparent': '00-4c9cbb128a8924d42a577c897de52800-e91516642da3cbfc-01',
  'tracestate': '3499570@nr=0-1-3499570-400695152-e91516642da3cbfc----1689666576744'
}

"""Select Drinks"""
URL_DRINKS = "https://dominos.by/api/web/pages?path=%2Fdrinks&language=en&cityId=2"
headers_drinks = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': '_gcl_au=1.1.1747184498.1687546128; _ym_uid=1687546129860396183; _ym_d=1687546129;'
            ' _tt_enable_cookie=1; _ttp=s9WBmjncqfvwcbtOf3VMseX5KrU; _fbp=fb.1.1687796267759.'
            '481841012; _gcl_aw=GCL.1687953717.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-'
            'wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB; _gac_UA-71584615-1='
            '1.1687953725.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzSX2v0yNKlVILIw15Q'
            'hVWYNWyUC_qSG0aAuYxEALw_wcB; cityId=2; popup-banner-shown=true; _gid=GA1.2.579693227.'
            '1689159727; csrftoken=REIxLYamkfEBVOHHAa0JRMhjRGF2i3ru; sessionid=q38ympxtmkqegil0'
            'gf3o7g29y1ysawpz; language=en; _ym_isad=1; _ga=GA1.2.1512419877.1687546129; '
            '_ym_visorc=w; _ga_FTX05WYR3P=GS1.2.1689666147.8.1.1689666577.7.0.0; _ga_BZNP2GVXYY'
            '=GS1.1.1689666147.68.1.1689666577.0.0.0; csrftoken=7aifepPCyID8G84RjxJxTZ6C1hrM35s9;'
            ' sessionid=853wacmcn55wckztb1x85olubx0griar',
  'If-None-Match': 'W/"a099-NVXsxvyPV071gFitxBezI0gso20"',
  'Referer': 'https://dominos.by/drinks',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'X-NewRelic-ID': 'VwIOWFNUCBAEVFFUAQIDVFA=',
  'correlation-id': 'aa54a31f-48db-4fce-843f-0b6e7cc10108',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0OTk1NzAiLCJhcCI6IjQwMDY5NTE1M'
              'iIsImlkIjoiNzA2YWU3ZGQwY2I3ODQ0NiIsInRyIjoiNWJhN2FkY2NhYjg2ODNhMDk0NmQxZGRlYmMzZT'
              'AzMDAiLCJ0aSI6MTY4OTY2NjY5MTYxNX19',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'traceparent': '00-5ba7adccab8683a0946d1ddebc3e0300-706ae7dd0cb78446-01',
  'tracestate': '3499570@nr=0-1-3499570-400695152-706ae7dd0cb78446----1689666691615'
}

"""For Sauce"""
URL_SAUCE = "https://dominos.by/api/web/pages?path=%2Fsauce&language=en&cityId=2"
headers_sauce = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': '_gcl_au=1.1.1747184498.1687546128; _ym_uid=1687546129860396183; _ym_d=1687546129;'
            ' _tt_enable_cookie=1; _ttp=s9WBmjncqfvwcbtOf3VMseX5KrU; _fbp=fb.1.1687796267759.'
            '481841012; _gcl_aw=GCL.1687953717.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-'
            'wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB; _gac_UA-71584615-1='
            '1.1687953725.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzSX2v0yNKlVILIw15'
            'QhVWYNWyUC_qSG0aAuYxEALw_wcB; cityId=2; popup-banner-shown=true; _gid=GA1.2.'
            '579693227.1689159727; csrftoken=REIxLYamkfEBVOHHAa0JRMhjRGF2i3ru; sessionid='
            'q38ympxtmkqegil0gf3o7g29y1ysawpz; language=en; _ym_isad=1; _ga=GA1.2.1512419877.'
            '1687546129; _ym_visorc=w; _ga_FTX05WYR3P=GS1.2.1689666147.8.1.1689666692.60.0.0; '
            '_ga_BZNP2GVXYY=GS1.1.1689666147.68.1.1689666692.0.0.0; csrftoken=7aifepPCyID8G84R'
            'jxJxTZ6C1hrM35s9; sessionid=853wacmcn55wckztb1x85olubx0griar',
  'If-None-Match': 'W/"3363-R/Zk7wFTh4sEaHcEe4R2C5kWY+U"',
  'Referer': 'https://dominos.by/sauce',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'X-NewRelic-ID': 'VwIOWFNUCBAEVFFUAQIDVFA=',
  'correlation-id': 'b7a54bb6-5634-4209-bf39-204193cf09f0',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0OTk1NzAiLCJhcCI6IjQwMDY5NTE1'
              'MiIsImlkIjoiNDU2OTUxYzFlZTNlNTA4YSIsInRyIjoiNDZlYjkwZDQzNjgzYjNmNDJhMjk3YjFhNGNk'
              'ZDQzMDAiLCJ0aSI6MTY4OTY2NjgxODUyMX19',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'traceparent': '00-46eb90d43683b3f42a297b1a4cdd4300-456951c1ee3e508a-01',
  'tracestate': '3499570@nr=0-1-3499570-400695152-456951c1ee3e508a----1689666818521'
}

"""For Discount"""
URL_DISCOUNT = "https://dominos.by/api/web/pages?path=%2Fdiscount_campaign&language=en&cityId=2"
headers_discount = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': '_gcl_au=1.1.1747184498.1687546128; _ym_uid=1687546129860396183; _ym_d=1687546129; '
            '_tt_enable_cookie=1; _ttp=s9WBmjncqfvwcbtOf3VMseX5KrU; _fbp=fb.1.1687796267759.'
            '481841012; _gcl_aw=GCL.1687953717.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-'
            'wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB; _gac_UA-71584615-1='
            '1.1687953725.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzSX2v0yNKlVILIw15QhVW'
            'YNWyUC_qSG0aAuYxEALw_wcB; cityId=2; popup-banner-shown=true; _gid=GA1.2.579693227.'
            '1689159727; csrftoken=REIxLYamkfEBVOHHAa0JRMhjRGF2i3ru; sessionid=q38ympxtmkqegil'
            '0gf3o7g29y1ysawpz; language=en; _ym_isad=1; _ga=GA1.2.1512419877.1687546129; '
            '_ym_visorc=w; _gat_UA-71584615-1=1; _ga_FTX05WYR3P=GS1.2.1689666147.8.1.'
            '1689666819.60.0.0; _ga_BZNP2GVXYY=GS1.1.1689666147.68.1.1689666819.0.0.0; csrftoken='
            '7aifepPCyID8G84RjxJxTZ6C1hrM35s9; sessionid=853wacmcn55wckztb1x85olubx0griar',
  'Referer': 'https://dominos.by/discount_campaign',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'X-NewRelic-ID': 'VwIOWFNUCBAEVFFUAQIDVFA=',
  'correlation-id': 'df6fe0db-3ec5-40b7-afa9-aa08b9e0af6e',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0OTk1NzAiLCJhcCI6IjQwMDY5NTE1Mi'
              'IsImlkIjoiMzVmMmMwYWI4ZTBkODE3MyIsInRyIjoiMzI4MWViMTVkMWU5ODViOTI2OTE2MWQ1N2FhYzhl'
              'MDAiLCJ0aSI6MTY4OTY2Njg2MTYyN319',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'traceparent': '00-3281eb15d1e985b9269161d57aac8e00-35f2c0ab8e0d8173-01',
  'tracestate': '3499570@nr=0-1-3499570-400695152-35f2c0ab8e0d8173----1689666861627'
}

"""For News"""
URL_NEWS = "https://dominos.by/api/web/pages?path=%2Fnews&language=en&cityId=2"
headers_news = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': '_gcl_au=1.1.1747184498.1687546128; _ym_uid=1687546129860396183; _ym_d=1687546129; '
            '_tt_enable_cookie=1; _ttp=s9WBmjncqfvwcbtOf3VMseX5KrU; _fbp=fb.1.1687796267759.'
            '481841012; _gcl_aw=GCL.1687953717.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-'
            'wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB; _gac_UA-71584615-1=1.'
            '1687953725.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzSX2v0yNKlVILIw15QhVWY'
            'NWyUC_qSG0aAuYxEALw_wcB; cityId=2; popup-banner-shown=true; _gid=GA1.2.579693227.'
            '1689159727; csrftoken=REIxLYamkfEBVOHHAa0JRMhjRGF2i3ru; sessionid=q38ympxtmkqegil'
            '0gf3o7g29y1ysawpz; language=en; _ym_isad=1; _ga=GA1.2.1512419877.1687546129; '
            '_ym_visorc=w; _ga_FTX05WYR3P=GS1.2.1689666147.8.1.1689666862.17.0.0; _ga_BZNP2GVXYY='
            'GS1.1.1689666147.68.1.1689666862.0.0.0; csrftoken=7aifepPCyID8G84RjxJxTZ6C1hrM35s9; '
            'sessionid=853wacmcn55wckztb1x85olubx0griar',
  'Referer': 'https://dominos.by/news',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'X-NewRelic-ID': 'VwIOWFNUCBAEVFFUAQIDVFA=',
  'correlation-id': 'e766cca7-4043-48a2-9649-8e5a3b3b120c',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0OTk1NzAiLCJhcCI6IjQwMDY5NTE1'
              'MiIsImlkIjoiNWJiNTEwYzUwZjY2NTYzNSIsInRyIjoiODM5ZThlOTlhMWY3YzJkMTY2MWY4YjU2NWQy'
              'ZTU2MDAiLCJ0aSI6MTY4OTY2NzAxMDUxN319',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'traceparent': '00-839e8e99a1f7c2d1661f8b565d2e5600-5bb510c50f665635-01',
  'tracestate': '3499570@nr=0-1-3499570-400695152-5bb510c50f665635----1689667010517'
}

"""For Job"""
URL_JOB = "https://dominos.by/api/web/pages?path=%2Fjob&language=en&cityId=2"
headers_job = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': '_gcl_au=1.1.1747184498.1687546128; _ym_uid=1687546129860396183; _ym_d=1687546129; '
            '_tt_enable_cookie=1; _ttp=s9WBmjncqfvwcbtOf3VMseX5KrU; _fbp=fb.1.1687796267759.'
            '481841012; _gcl_aw=GCL.1687953717.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-'
            'wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB; _gac_UA-71584615-1=1.'
            '1687953725.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzSX2v0yNKlVILIw15QhVWY'
            'NWyUC_qSG0aAuYxEALw_wcB; cityId=2; popup-banner-shown=true; _gid=GA1.2.579693227.'
            '1689159727; csrftoken=REIxLYamkfEBVOHHAa0JRMhjRGF2i3ru; sessionid=q38ympxtmkqegil'
            '0gf3o7g29y1ysawpz; language=en; _ym_isad=1; _ga=GA1.2.1512419877.1687546129; '
            '_ym_visorc=w; _ga_FTX05WYR3P=GS1.2.1689666147.8.1.1689667011.60.0.0; _ga_BZNP2GVXYY='
            'GS1.1.1689666147.68.1.1689667011.0.0.0; csrftoken=7aifepPCyID8G84RjxJxTZ6C1hrM35s9; '
            'sessionid=853wacmcn55wckztb1x85olubx0griar',
  'Referer': 'https://dominos.by/job',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'X-NewRelic-ID': 'VwIOWFNUCBAEVFFUAQIDVFA=',
  'correlation-id': 'c7974f10-719c-445d-a3ce-e169f7ceffc7',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0OTk1NzAiLCJhcCI6IjQwMDY5NTE1Mi'
              'IsImlkIjoiMThmOTlkZTJiMjFhMzRmNSIsInRyIjoiMzRlNTA0ZDkxZmFiN2MxZDI3NDRlNjhjOWNmMmMz'
              'MDAiLCJ0aSI6MTY4OTY2NzA5NjY2MH19',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'traceparent': '00-34e504d91fab7c1d2744e68c9cf2c300-18f99de2b21a34f5-01',
  'tracestate': '3499570@nr=0-1-3499570-400695152-18f99de2b21a34f5----1689667096660'
}

"""For Loyalty program"""
URL_LOYALTY = "https://dominos.by/api/web/pages?path=%2Floyalty-program&language=en&cityId=2"
payload = {}
headers_loyalty = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': '_gcl_au=1.1.1747184498.1687546128; _ym_uid=1687546129860396183; _ym_d=1687546129; '
            '_tt_enable_cookie=1; _ttp=s9WBmjncqfvwcbtOf3VMseX5KrU; _fbp=fb.1.1687796267759.'
            '481841012; _gcl_aw=GCL.1687953717.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-'
            'wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC_qSG0aAuYxEALw_wcB; _gac_UA-71584615-1=1.'
            '1687953725.Cj0KCQjwtO-kBhDIARIsAL6Loret1VZCEZZj3-wp8tV8ZWrzSX2v0yNKlVILIw15QhVWYNWyUC'
            '_qSG0aAuYxEALw_wcB; cityId=2; popup-banner-shown=true; _gid=GA1.2.579693227.'
            '1689159727; csrftoken=REIxLYamkfEBVOHHAa0JRMhjRGF2i3ru; sessionid=q38ympxtmkqegil0gf3'
            'o7g29y1ysawpz; language=en; _ym_isad=1; _ga=GA1.2.1512419877.1687546129; '
            '_ym_visorc=w; _gat_UA-71584615-1=1; _ga_FTX05WYR3P=GS1.2.1689666147.8.1.1689667145.'
            '12.0.0; _ga_BZNP2GVXYY=GS1.1.1689666147.68.1.1689667145.0.0.0; csrftoken=7aifepPCyID8'
            'G84RjxJxTZ6C1hrM35s9; sessionid=853wacmcn55wckztb1x85olubx0griar',
  'Referer': 'https://dominos.by/loyalty-program',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'X-NewRelic-ID': 'VwIOWFNUCBAEVFFUAQIDVFA=',
  'correlation-id': '01b8a3c1-361d-41f4-a576-0064dae5964f',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0OTk1NzAiLCJhcCI6IjQwMDY5NTE1Mi'
              'IsImlkIjoiYTE1NzMzZGYzNDA0YWJiZiIsInRyIjoiZDg2MTNiNjQxYTM1YmE4YjA3NmUxZTQzNDgwY2Jk'
              'MDAiLCJ0aSI6MTY4OTY2NzE1MzgzMn19',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'traceparent': '00-d8613b641a35ba8b076e1e43480cbd00-a15733df3404abbf-01',
  'tracestate': '3499570@nr=0-1-3499570-400695152-a15733df3404abbf----1689667153832'
}
