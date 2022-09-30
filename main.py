import requests
from fake_useragent import UserAgent

lineNotifyToken = "XXXXXX"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://production.dataviz.cnn.io/index/fearandgreed/graphdata'
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    res = requests.get(url, headers=headers)
    # print(res.json())
    nowScore = int(res.json()['fear_and_greed']['score'])
    nowRating = str(res.json()['fear_and_greed']['rating'])
    pre1WeekRating = int(res.json()['fear_and_greed']['previous_1_week'])
    pre1MonthRating = int(res.json()['fear_and_greed']['previous_1_month'])
    msg = '\nType: S&P500\nNow score: ' + str(nowScore) + ' \\ ' + str(
        nowRating) + '\n' + 'Last Week Score: ' + str(
            pre1WeekRating) + '\n' + 'Last Month Score: ' + str(
                pre1MonthRating)

    # print(data)

    if nowScore <= 25 or nowScore >= 75:
        headers = {'Authorization': 'Bearer ' + lineNotifyToken}
        data = {'message': msg}
        requests.post('https://notify-api.line.me/api/notify',
                      headers=headers,
                      data=data)
