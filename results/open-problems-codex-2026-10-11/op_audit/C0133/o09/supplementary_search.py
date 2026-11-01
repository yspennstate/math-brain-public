import urllib.request, urllib.parse, json, concurrent.futures
from pathlib import Path
urls={
'crossref_search':'https://api.crossref.org/works?query='+urllib.parse.quote('excited random walk non transient zero velocity')+'&rows=12',
'arxiv_html_search':'https://arxiv.org/search/?query='+urllib.parse.quote('excited random walk zero velocity')+'&searchtype=all',
'santos':'https://arxiv.org/pdf/1909.03159'
}
def run(pair):
 name,url=pair
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'ProbabilityAudit/1.0'}),timeout=35) as r: data=r.read(); status=r.status
  suffix='.pdf' if data.startswith(b'%PDF') else '.txt'
  Path(name+suffix).write_bytes(data)
  return {'name':name,'url':url,'status':status,'bytes':len(data),'file':name+suffix}
 except Exception as e: return {'name':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: log=list(pool.map(run,urls.items()))
Path('supplementary_retrieval_log.json').write_text(json.dumps(log,indent=2),encoding='utf-8'); print(json.dumps(log,indent=2))
p=Path('crossref_search.txt')
if p.exists():
 data=json.loads(p.read_text(encoding='utf-8'))
 for w in data['message']['items']: print(w.get('title'),w.get('DOI'),w.get('abstract','')[:1000])
p=Path('santos.pdf')
if p.exists():
 import pymupdf
 d=pymupdf.open(p); s='\n'.join(page.get_text() for page in d); Path('santos_extracted.txt').write_text(s,encoding='utf-8'); print('SANTOS\n'+s[:6500])
