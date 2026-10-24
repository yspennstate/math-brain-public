import urllib.request,urllib.parse,json,pathlib,concurrent.futures,datetime,xml.etree.ElementTree as E
root=pathlib.Path(__file__).resolve().parent
queries={
'arxiv_higher':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'(ti:"higher order" AND all:"random matrices") OR (all:"multicritical" AND cat:math.PR) OR (all:"exotic" AND au:Virag)','max_results':60}),
'arxiv_critical':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"critical edge" AND (cat:math.PR OR cat:math-ph)','max_results':40}),
'arxiv_virag':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'ti:"Operator limits of random matrices"','max_results':5}),
'openalex_retry':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Operator limits of random matrices','per_page':5}),
'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1804.06953?fields=title,authors,year,citations.title,citations.year,citations.externalIds',
'crossref_higher':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.bibliographic':'higher order Tracy Widom stochastic operator','rows':15}),
'github_exotic':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'"stochastic Airy"'}),
}
def get(pair):
 name,url=pair
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'D0043-research/1.0'}),timeout=30) as r:data=r.read(12000000)
  (root/(name+('.xml' if name.startswith('arxiv') else '.json'))).write_bytes(data)
  result=f'{name}: {len(data)} bytes'
 except Exception as e:result=f'{name}: ERROR {e}'
 print(result,flush=True)
 return {'date':str(datetime.datetime.now()),'service':name,'url':url,'result':result}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(get,queries.items()))
(root/'followup_search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
f=root/'openalex_retry.json'
if f.exists():
 d=json.loads(f.read_text());print('OPENALEX RESULTS',[(x['id'],x['title'],x.get('doi')) for x in d['results']],flush=True)
 for x in d['results']:
  if x['title'].lower()=='operator limits of random matrices':
   url='https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:'+x['id'].split('/')[-1],'per_page':100})
   res=get(('openalex_citing',url));results.append(res)
   (root/'followup_search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
