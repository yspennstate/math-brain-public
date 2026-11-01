import json, pathlib, datetime, concurrent.futures, subprocess, urllib.parse
ROOT=pathlib.Path(__file__).resolve().parent
queries=[
 ('arxiv','http://export.arxiv.org/api/query',{'search_query':'all:"star-scale" AND all:"Gaussian"','max_results':30}),
 ('arxiv_https','https://export.arxiv.org/api/query',{'search_query':'all:"star-scale" AND all:"classification"','max_results':30}),
 ('openalex','https://api.openalex.org/works',{'search':'star scale invariant random measures classification','per-page':30}),
 ('openalex_source','https://api.openalex.org/works',{'search':'Gaussian multiplicative chaos and applications a review','per-page':5}),
 ('crossref','https://api.crossref.org/works',{'query':'star scale invariant random measures classification','rows':25}),
 ('semantic_scholar','https://api.semanticscholar.org/graph/v1/paper/search',{'query':'star scale invariant random measures','limit':30,'fields':'title,authors,year,abstract,externalIds,url'}),
 ('github','https://api.github.com/search/repositories',{'q':'"star scale" "chaos"','per_page':20}),
 ('openalex_uniqueness','https://api.openalex.org/works',{'search':'uniqueness critical star scale invariant Gaussian multiplicative chaos','per-page':30}),
]
def fetch(item):
 name,url,params=item
 try:
  full=url+'?'+urllib.parse.urlencode(params)
  r=subprocess.run(['curl.exe','-L','--max-time','50','-sS','-w','\n%{http_code}',full],capture_output=True,text=True,encoding='utf8',timeout=65)
  body,_,code=r.stdout.rpartition('\n')
  (ROOT/(name+'.txt')).write_text(body,encoding='utf8')
  row={'date':str(datetime.date.today()),'service':name,'url':full,'query':params,'http_status':code,'returncode':r.returncode,'stderr':r.stderr}
  print(json.dumps(row),flush=True)
  return row
 except Exception as e:
  row={'date':str(datetime.date.today()),'service':name,'url':url,'query':params,'error':str(e)}
  print(json.dumps(row),flush=True)
  return row
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 rows=list(ex.map(fetch,queries))
(ROOT/'search_log.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
try:
 data=json.loads((ROOT/'openalex_source.txt').read_text(encoding='utf8'))
 for work in data.get('results',[]):
  print('SOURCE',work['id'],work['title'],flush=True)
  if work['title'].lower().startswith('gaussian multiplicative chaos and applications'):
   ident=work['id'].rsplit('/',1)[-1]
   row=fetch(('openalex_citing','https://api.openalex.org/works',{'filter':'cites:'+ident,'per-page':200,'sort':'publication_date:desc'}))
   rows.append(row)
   (ROOT/'search_log.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
   break
except Exception as e: print('CITATIONS ERROR',repr(e),flush=True)
