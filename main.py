import requests
import json
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('./', encoding='utf8'), autoescape = True)
tmpl = env.get_template('template.xlm')

dict = requests.get('https://hashhub-research.com/api/articles?page=1&per=24').json()
xlm = tmpl.render(dict)
with open('public/feed.xlm',mode='w',encoding="utf-8") as f:
    f.write(str(xlm))
