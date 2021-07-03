import requests
import json
from jinja2 import Environment, FileSystemLoader
# autoescapeでテンプレートの拡張子に基づき自動でエスケープ処理をしてくれる
env = Environment(loader=FileSystemLoader('./', encoding='utf8'), autoescape = True)
tmpl = env.get_template('template.xml')

dict = requests.get('https://hashhub-research.com/api/articles?page=1&per=24').json()
# TODO: 投稿日時をpubData用に変換
xlm = tmpl.render(dict)
with open('public/feed.xml',mode='w',encoding="utf-8") as f:
    f.write(str(xlm))
