import re
import requests as req
from pathlib import Path

openapi = ""
path = Path(__file__).resolve().parent / 'weread.txt'

with open(path, 'r', encoding='utf-8') as file:
    data = file.read()
    data = data.replace('>>', '>')
    title = re.findall('《(.*)》', data)[0]
    content = '#阅读 #{} \n{}'.format(title, data)
#    print(content)
    resp = req.post(openapi, json={"content": content})
    print('推送成功' if resp.status_code != '200' else '推送失败')