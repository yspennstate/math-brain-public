import urllib.request, urllib.parse, concurrent.futures, pathlib,json
q={
 'source_v2':'https://arxiv.org/pdf/2505.19104v2',
 'arxiv_selection':'http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"optimal transport" AND (all:selection OR all:nonunique OR all:rectangles)')+'&start=0&max_results=40&sortBy=submittedDate&sortOrder=descending',
 'openalex_retry':'https://api.openalex.org/works?search='+urllib.parse.quote('"Distributional Limit Theory for Optimal Transport"')+'&per_page=5',
 'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2505.19104/citations?fields=title,year,externalIds&limit=100',
 'crossref_recent':'https://api.crossref.org/works?query='+urllib.parse.quote('empirical optimal transport nonunique Euclidean')+'&filter=from-pub-date:2026-07-13&rows=20',
 'github_rectangles':'https://api.github.com/search/repositories?q='+urllib.parse.quote('optimal transport rectangles')}
def f(k,u):
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as r:b=r.read()
  pathlib.Path(k+('.pdf' if k=='source_v2' else '.txt')).write_bytes(b)
  return {'service':k,'url':u,'date':'2026-10-12','status':'ok','bytes':len(b)}
 except Exception as e:return {'service':k,'url':u,'date':'2026-10-12','status':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:a=list(ex.map(lambda kv:f(*kv),q.items()))
pathlib.Path('search_log2.json').write_text(json.dumps(a,indent=2));print(json.dumps(a,indent=2))
if pathlib.Path('source_v2.pdf').exists():
 import pymupdf
 d=pymupdf.open('source_v2.pdf');pathlib.Path('source_v2_text.txt').write_text('\n'.join(f'PDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8');print('v2 pages',len(d))
