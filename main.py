from datetime import datetime, timezone, timedelta
import requests
import json
from jinja2 import Environment, FileSystemLoader
# autoescapeでテンプレートの拡張子に基づき自動でエスケープ処理をしてくれる
env = Environment(loader=FileSystemLoader('./', encoding='utf8'), autoescape = True)
tmpl = env.get_template('template.xml')

json = requests.get('https://hashhub-research.com/api/articles?page=1&per=24').json()
articles = []
for article in json.get("articles"):
    article_data = requests.get('https://hashhub-research.com/api/articles/' + article.get("slug")).json().get('article')
    jst_posted_at = datetime.strptime(article.get("posted_at"), '%Y-%m-%d').astimezone(timezone(timedelta(hours=+9)))
    articles.append({
        "title": article.get("title"),
        "slug": article.get("slug"),
        "table_of_contents": article_data.get("table_of_contents"),
        "pubDate": jst_posted_at.strftime('%a, %d %b %Y %H:%M:%S %z'),
        "thumbnail": article.get("thumbnail"),
    })

xml = tmpl.render({"articles": articles})
with open('public/feed.xml',mode='w',encoding="utf-8") as f:
    f.write(str(xml))
    