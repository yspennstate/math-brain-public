import urllib.request, urllib.parse, json, pathlib, datetime, concurrent.futures
ROOT=pathlib.Path(__file__).resolve().parent
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'F0033 mathematical literature research'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (ROOT/(name+'.pdf' if name=='jarai' else name+'.json')).write_bytes(data)
  result={'name':name,'url':url,'bytes':len(data),'status':'ok'}
 except Exception as e: result={'name':name,'url':url,'status':str(e)}
 with (ROOT/'search_log.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps({'date':'2026-10-12',**result})+'\n')
 return result
q=urllib.parse.quote
jobs=[('jarai','https://arxiv.org/pdf/1401.0354'),
 ('arxiv','http://export.arxiv.org/api/query?search_query='+q('all:sandpile AND all:avalanche')+'&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending'),
 ('openalex','https://api.openalex.org/works?search='+q('sandpile avalanche finiteness')+'&per-page=50'),
 ('crossref','https://api.crossref.org/works?query='+q('sandpile avalanches infinite volume')+'&rows=30'),
 ('semantic','https://api.semanticscholar.org/graph/v1/paper/search?query='+q('sandpile avalanche finiteness')+'&limit=50&fields=title,authors,year,abstract,url,externalIds'),
 ('github','https://api.github.com/search/repositories?q='+q('sandpile avalanche')),
 ('openalex_source','https://api.openalex.org/works?search='+q('Sandpile models Jarai')+'&per-page=10')]
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
  for r in ex.map(fetch,jobs): print(json.dumps(r))
