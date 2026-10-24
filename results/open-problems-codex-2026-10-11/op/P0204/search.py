import urllib.request, urllib.parse, concurrent.futures, pathlib, json, datetime, re
ROOT=pathlib.Path(__file__).resolve().parent
queries={
 'source':'https://www.yuval-peres-books.com/markov-chains-and-mixing-times/',
 'arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:monotone AND (all:mixing OR all:walk)')+'&max_results=40',
 'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('monotone subsets hypercube mixing')+'&per-page=20',
 'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('Ding Mossel monotone mixing hypercube')+'&rows=15',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('monotone hypercube mixing')+'&limit=20&fields=title,authors,year,externalIds,url,abstract',
 'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('monotone hypercube mixing'),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'P0204-research/1.0'})
  with urllib.request.urlopen(req,timeout=55) as r: data=r.read().decode('utf8','replace')
  (ROOT/(name+'.txt')).write_text(data,encoding='utf8')
  return name,url,'OK',data
 except Exception as e: return name,url,str(e),''
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 results=list(ex.map(fetch,queries.items()))
with (ROOT/'LITERATURE.md').open('a',encoding='utf8') as f:
 for name,url,status,data in results:
  f.write(f'\n- 2026-10-11 | {name} | {url} | {status}; raw response: {name}.txt\n')
  print(name,status)
  if name=='source': print(re.sub('<[^>]+>',' ',data)[-28000:])
  elif name=='openalex' and data:
   for w in json.loads(data)['results']: print(w['id'],w['display_name'],w['publication_year'],w.get('doi'))
  elif name=='crossref' and data:
   for w in json.loads(data)['message']['items']: print(w.get('title'),w.get('DOI'))
  elif name=='semantic' and data: print(data[:18000])
  elif name=='arxiv' and data: print(data[:12000])
