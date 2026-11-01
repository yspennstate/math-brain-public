import urllib.request, urllib.parse, json, concurrent.futures, pathlib, datetime
p=pathlib.Path('.')
q='Topics and problems on favorite sites of random walks'
urls={
 'arxiv': 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"favorite sites" AND all:"random walks"','start':0,'max_results':30}),
 'openalex_source':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':q,'per-page':5}),
 'openalex_annulus':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'random walk generalized boundary local time annulus','per-page':15}),
 'crossref':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':q,'rows':8}),
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1606.03787?fields=title,authors,year,citationCount,citations.title,citations.year,citations.externalIds',
 'github':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'"favorite sites" "random walk"','per_page':10}),
}
def fetch(k,u):
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'ProbabilityResearch/1.0'})
  b=urllib.request.urlopen(req,timeout=45).read(); p.joinpath('search_'+k+'.txt').write_bytes(b)
  return k,u,'OK',len(b)
 except Exception as e:return k,u,'ERROR',str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 results=list(ex.map(lambda item:fetch(*item),urls.items()))
p.joinpath('search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
for row in results:print(row)
if p.joinpath('search_openalex_source.txt').exists():
 data=json.loads(p.joinpath('search_openalex_source.txt').read_text())
 for w in data['results']:print('SOURCE',w['id'],w['title'],w.get('doi'))
if p.joinpath('search_openalex_annulus.txt').exists():
 for w in json.loads(p.joinpath('search_openalex_annulus.txt').read_text())['results']:print('LEAD',w['publication_year'],w['title'],w.get('doi'))
