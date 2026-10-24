import urllib.request, pathlib, json, urllib.parse
u='https://api.openalex.org/works?filter=cites:W2935248447&per_page=100'
try:
 with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as r:b=r.read()
 pathlib.Path('openalex_citations.txt').write_bytes(b)
 j=json.loads(b); print('count',j['meta']['count'])
 for w in j['results']: print(w['title'],w.get('doi'),w['publication_year'])
 s='OK '+str(len(b))+' bytes'
except Exception as e:s=str(e);print(s)
with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- 2026-10-11 OpenAlex citing works: '+u+'\n  '+s+'\n')
