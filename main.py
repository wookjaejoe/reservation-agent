# noinspection SpellCheckingInspection

"""
- 웹 크롤링
- 사이트별 예약 가능 여부 수집
- 최초 수집 시, 예약 가능 사이트 알림
- 두번째 수집부터는 직전 수집 내용과 비교하여 새로 열린 사이트만 알림
"""

from datetime import date

from ticketplay.client import search


def main():
    res = search(
        check_in=date(2022, 8, 13),
        stay_count=2
    )
    print(res)


if __name__ == '__main__':
    main()
