from pathlib import Path
import urllib.request,urllib.parse,json,hashlib
root=Path(__file__).resolve().parent
sources=[]
def fetch(name,url):
 with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"}),timeout=60) as r:data=r.read()
 (root/name).write_bytes(data);sources.append({'file':name,'url':url,'sha256':hashlib.sha256(data).hexdigest()});return data
u='https://raw.githubusercontent.com/Sekai-World/sekai-master-db-diff/main/cards.json'
with urllib.request.urlopen(u,timeout=60) as r:data=r.read()
card=next(c for c in json.loads(data) if c.get('prefix')=='きらびやかな夢の舞台' and c.get('characterId')==15)
assert card['cardRarityType']=='rarity_4'
(root/'balloon-card-game-data.json').write_text(json.dumps({'source':u,'database_sha256':hashlib.sha256(data).hexdigest(),'status':'non-official game-data mirror','card':card},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(card,ensure_ascii=False,indent=2),flush=True)
asset=card['assetbundleName']
fetch('trained-card.png',f'https://storage.sekai.best/sekai-jp-assets/character/member/{asset}/card_after_training.png')
fetch('official-profile.html','https://pjsekai.sega.jp/character/unite04/nene/index.html')
fetch('costume-guide.html','https://game8.jp/pjsekai/694561')
(root/'sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Downloaded trained card and source pages.')
