import pathlib, urllib.request, json, concurrent.futures, datetime
P=pathlib.Path(__file__).resolve().parent
qs=[
('OpenAlex','source DOI lookup','https://api.openalex.org/works/https://doi.org/10.4310/ICM.2014.v3.21'),
('OpenAlex','citing arxiv source via DOI','https://api.openalex.org/works?filter=cites:W2102466745&per-page=200'),
('SemanticScholar','source arXiv and citation metadata','https://api.semanticscholar.org/graph/v1/paper/ARXIV:1406.2707?fields=title,year,citations.title,citations.year,citations.externalIds'),
('Crossref','determinantal stochastic domination','https://api.crossref.org/works?query=determinantal%20stochastic%20domination&rows=30'),
('arxiv','determinantal product measures','https://export.arxiv.org/api/query?search_query=all:%22determinantal%22+AND+all:%22product+measure%22&max_results=70'),
('arxiv','Lyons conjecture 5.7','https://export.arxiv.org/api/query?search_query=all:%22Lyons%22+AND+all:%22conjecture%22+AND+all:%22determinantal%22&max_results=70'),
]
def run(item):
 s,q,u=item;d={'service':s,'query':q,'url':u,'date':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'mathematical-research'}),timeout=30) as r:b=r.read();d['status']=r.status
  f='followup_'+str(qs.index(item))+'.raw';P.joinpath(f).write_bytes(b);d['raw_file']=f
 except Exception as e:d['error']=str(e)
 return d
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:r=list(ex.map(run,qs))
P.joinpath('followup_results.json').write_text(json.dumps(r,indent=2),encoding='utf8');print(json.dumps(r,indent=2))
# Read two actual candidate papers; no guessed theorem attribution.
for aid in ['2412.13751','2009.09141']:
 try:
  with urllib.request.urlopen('https://arxiv.org/pdf/'+aid,timeout=40) as r:b=r.read()
  P.joinpath(aid+'.pdf').write_bytes(b)
  import pymupdf
  d=pymupdf.open(P/(aid+'.pdf'));P.joinpath(aid+'.txt').write_text('\n'.join(p.get_text() for p in d),encoding='utf8')
  print('fetched',aid,len(d),'pages')
 except Exception as e:print(aid,str(e))
