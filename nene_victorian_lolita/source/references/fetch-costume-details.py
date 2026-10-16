from pathlib import Path
import urllib.request,json,hashlib
r=Path(__file__).resolve().parent
items=[('costume-front.png','https://img.game8.jp/8807091/5a6b83cc682743e048470798173cbfbb.png/original'),('hat-accessory.png','https://img.game8.jp/8809375/608bbe59b5efdb1870df27c5a471a6e3.png/original'),('hairstyle.png','https://img.game8.jp/9396959/3f23ca26e7ae0fe95a8056af6c121c23.png/original'),('release-announcement.html','https://www.4gamer.net/games/476/G047609/20211228045/'),('gallery-model-list.html','https://pjsekai.gamedbs.jp/chara/model3d/510?c=1')]
sources=json.loads((r/'sources.json').read_text(encoding='utf-8'))
for name,url in items:
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60) as stream:data=stream.read()
  (r/name).write_bytes(data);sources.append({'file':name,'url':url,'sha256':hashlib.sha256(data).hexdigest()});print(name,len(data),flush=True)
 except urllib.error.HTTPError as e:print(name,'HTTP',e.code,flush=True)
(r/'sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
