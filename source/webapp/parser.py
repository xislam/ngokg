from datetime import datetime

import requests
from rest_framework.utils import json

from webapp.models import News


def MyCronJo():
    print('Запускаю!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    today = datetime.date(datetime.now())
    news_request = requests.get(f'http://newsline.kg/getNews.php?limit=30&last_dt={today}')
    new_news = json.loads(news_request.text)
    data = new_news['data']
    for item in data:
        dt = item['dt']
        title = item['title']
        img = item['img']
        link = item['link']
        desc = item['desc']
        site_name = item['site_name']
        # print(dt)
        # print(title)
        # print(img)
        # print(link)
        # print(desc)
        # print(site_name)
        News.objects.get_or_create(
            dt=dt,
            title=title,
            img=img,
            link=link,
            desc=desc,
            site_name=site_name
        )