import requests
from vars import SOLIDER, AUTH
#TODO Solider & Auth needs to be updated


def download_request(addition_url: str, medic_center_id, file_name):
    url = f"https://meditik.medical.idf.il/api/printouts/{addition_url}{medic_center_id}"

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=1, i',
        'referer': f'https://meditik.medical.idf.il/appointments/{medic_center_id}',
        'request-id': '|d34289357033438e9c7b860911cfc747.3bb08af482d44a7b',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'soldier': SOLIDER,
        'traceparent': '00-d34289357033438e9c7b860911cfc747-3bb08af482d44a7b-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Authorization': AUTH,
        'Cookie': 'incap_ses_1456_3163703=ODv4L8xnRAIgw7dbn8A0FA6S8mcAAAAAfKYiNMpc+pK2tuU5BpzFXw==; nlbi_3163703=glweOfbLRnedKft9HQIjegAAAAA2ixaGSrr9OLMhtbogVP03; visid_incap_3163703=aZNsZY5CTE6qJhPj3ZZ/INeR8mcAAAAAQUIPAAAAAAA0XKxWnNL0ILR1mw9rivky'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    open(f'{file_name}.pdf', 'wb').write(response.content)
