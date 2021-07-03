from datetime import datetime
import requests
import json
from jinja2 import Environment, FileSystemLoader
# autoescapeでテンプレートの拡張子に基づき自動でエスケープ処理をしてくれる
env = Environment(loader=FileSystemLoader('./', encoding='utf8'), autoescape = True)
tmpl = env.get_template('template.xml')

json = requests.get('https://hashhub-research.com/api/articles?page=1&per=24').json()
articles = []
for article in json.get("articles"):
    articles.append({
        "title": article.get("title"),
        "slug": article.get("slug"),
        "table_of_contents": article.get("table_of_contents"),
        "pubDate": datetime.strptime(article.get("created_at"), '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%a, %d %b %Y %H:%M:%S %z')
    })

xml = tmpl.render({"articles": articles})
with open('public/feed.xml',mode='w',encoding="utf-8") as f:
    f.write(str(xml))
