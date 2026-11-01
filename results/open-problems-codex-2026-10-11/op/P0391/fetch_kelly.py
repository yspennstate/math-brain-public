import urllib.request,pathlib,re,json
root=pathlib.Path(__file__).resolve().parent
url='https://www.statslab.cam.ac.uk/~frank/BOOK/'
try:
 with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research-check/1.0'}),timeout=40) as f:data=f.read()
 (root/'kelly_book_index.html').write_bytes(data)
 html=data.decode('utf-8',errors='replace')
 links=re.findall(r'href\s*=\s*[\"\']([^\"\']+)',html,re.I)
 record=dict(service='Kelly book webpage',query=url,date='2026-10-11',result='saved',links=links)
 print(json.dumps(record,indent=2))
except Exception as e:
 record=dict(service='Kelly book webpage',query=url,date='2026-10-11',result=str(e));print(record)
(root/'kelly_log.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
