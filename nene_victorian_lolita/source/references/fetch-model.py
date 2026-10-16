from pathlib import Path
from html.parser import HTMLParser
import urllib.request,urllib.parse,json,hashlib
r=Path(__file__).resolve().parent
url='https://pjsekai.gamedbs.jp/chara/model3d?c=7&q='+urllib.parse.quote('スパカリバルーンドレス')
with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60) as stream:data=stream.read()
(r/'nene-costume-model-page.html').write_bytes(data)
class P(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='a' and '/image/chara/3dc/' in a.get('href',''):self.urls.append(a['href'])
p=P();p.feed(data.decode('utf-8'));sources=json.loads((r/'sources.json').read_text(encoding='utf-8'));sources.append({'file':'nene-costume-model-page.html','url':url,'sha256':hashlib.sha256(data).hexdigest()})
for i,u in enumerate(p.urls):
 with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60) as stream:b=stream.read()
 name=f'costume-model-{i+1}.webp';(r/name).write_bytes(b);sources.append({'file':name,'url':u,'sha256':hashlib.sha256(b).hexdigest()});print(name,len(b),flush=True)
(r/'sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Matching Nene model images:',len(p.urls))
