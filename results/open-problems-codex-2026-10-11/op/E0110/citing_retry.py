import urllib.request,pathlib,json
u='https://api.openalex.org/works?filter=cites:W2935248447&per-page=50&select=id,doi,title,publication_year'
try:
 with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r:b=r.read()
 pathlib.Path('openalex_citations_retry.txt').write_bytes(b);j=json.loads(b); print(j);s=f'OK {len(b)} bytes'
except Exception as e:s=str(e);print(s)
with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- 2026-10-11 OpenAlex citing works retry: '+u+'\n  '+s+'\n')
