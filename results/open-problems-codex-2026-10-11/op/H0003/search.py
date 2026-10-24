import urllib.request, urllib.parse, urllib.error, json, concurrent.futures
from pathlib import Path
P=Path(__file__).parent
q=urllib.parse.quote
title='Threshold cascades of interacting diffusions on unimodular random trees'
requests=[
('source_abs','https://arxiv.org/abs/2608.15987'),
('source_pdf','https://arxiv.org/pdf/2608.15987'),
('source_html','https://arxiv.org/html/2608.15987v1'),
('arxiv_id','http://export.arxiv.org/api/query?id_list=2608.15987'),
('arxiv_search','https://export.arxiv.org/api/query?search_query='+q('all:"Front-Markov" OR all:"Threshold cascades"')+'&max_results=30'),
('openalex','https://api.openalex.org/works?search='+q(title)+'&per-page=10'),
('crossref','https://api.crossref.org/works?query='+q(title)+'&rows=10'),
('semantic','https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.15987?fields=title,authors,year,citations.title,citations.externalIds,citations.year'),
('github','https://api.github.com/search/repositories?q='+q('"2608.15987"')),
('github_front','https://api.github.com/search/repositories?q='+q('"front-Markov"'))]
def get(item):
 name,url=item
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research verification contact-free/1.0'}),timeout=45) as r:
   data=r.read(); status=r.status; ct=r.headers.get('Content-Type','')
  ext='.pdf' if data.startswith(b'%PDF') else '.txt'
  P.joinpath(name+ext).write_bytes(data)
  result={'service':name,'url':url,'status':status,'bytes':len(data),'file':name+ext,'content_type':ct}
 except Exception as e: result={'service':name,'url':url,'error':str(e)}
 return result
if __name__ == '__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
  for result in ex.map(get,requests):
   with P.joinpath('search_log.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps({'date':'2026-10-12',**result})+'\n')
   with P.joinpath('LITERATURE.md').open('a',encoding='utf-8') as f: f.write('\n- 2026-10-12: '+json.dumps(result)+'\n')
   print(json.dumps(result),flush=True)
