import requests
from datetime import date
from model import SearchResult


def search(check_in: date, stay_count: int) -> SearchResult:
    result: dict = requests.post(
        'https://gwgs.ticketplay.zone/portal/realtime/productSearchJson',
        data={
            'check_in': check_in.strftime('%Y%m%d'),
            'stay_cnt': stay_count
        }
    ).json()

    code = result['RESULT_CODE']
    if code == 'SUCCESS':
        return SearchResult.from_list(result['RESULT_DATA'])
    else:
        raise Exception('Request failed.')
