import re
import requests as req
import os
import sys

openapi = ""
path = os.path.dirname(sys.argv[0])
with open(path + '/weread.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    data = data.replace('>>', '>')
    title = re.findall('《(.*)》', data)[0]
    content = '#阅读 #{} \n{}'.format(title, data)
#    print(content)
    resp = req.post(openapi, json={"content": content})
    print(resp.status_code)