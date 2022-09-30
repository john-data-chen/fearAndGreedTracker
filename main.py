import requests
from fake_useragent import UserAgent
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

url = 'https://production.dataviz.cnn.io/index/fearandgreed/graphdata'
spreadsheet_key = ''  # in google sheet url

def crawler(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    res = requests.get(url, headers=headers)
    # print(res.json())
    nowScore = int(res.json()['fear_and_greed']['score'])
    nowRating = str(res.json()['fear_and_greed']['rating'])

    return {'nowScore': nowScore, 'nowRating': nowRating}


def gsheet(result):
    scopes = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'credentials.json', scopes)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key(spreadsheet_key).sheet1
    previousScore = int(sheet.acell('B2').value)
    print(previousScore)
    change = (result['nowScore'] - previousScore) / result['nowScore']
    # date score Indicator change
    date = datetime.now().strftime('%Y-%m-%d')
    values = [date, result['nowScore'], result['nowRating'], change]
    sheet.insert_row(values, 2)

if __name__ == '__main__':
    result = crawler(url)
    gsheet(result)
