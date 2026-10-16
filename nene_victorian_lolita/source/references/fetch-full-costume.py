from pathlib import Path
import urllib.request,urllib.parse,urllib.error,json,hashlib
r=Path(__file__).resolve().parent
url='https://pjsekai.gamedbs.jp/chara/model3d?c=1&q='+urllib.parse.quote('スパカリバルーンドレス')
items=[('balloon-model-search.html',url),('trained-cutout.png','https://storage.sekai.best/sekai-jp-assets/character/member_cutout_trm/res015_no012/after_training.png')]
sources=json.loads((r/'sources.json').read_text(encoding='utf-8'))
for name,url in items:
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60) as stream:data=stream.read()
  (r/name).write_bytes(data);sources.append({'file':name,'url':url,'sha256':hashlib.sha256(data).hexdigest()});print(name,len(data),flush=True)
 except urllib.error.HTTPError as e:print(name,'HTTP',e.code,flush=True)
(r/'sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
