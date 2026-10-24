import requests, concurrent.futures, json, math
from pathlib import Path
root=Path(__file__).parent
queries={
'openalex_net':'https://api.openalex.org/works?search=Brownian%20net&per-page=100',
'openalex_ancestors':'https://api.openalex.org/works?search=%22potential%20most%20recent%20common%20ancestors%22&per-page=25',
'arxiv_ancestors':'https://export.arxiv.org/api/query?search_query=all:%22potential%20most%20recent%20common%20ancestors%22&max_results=20'}
def fetch(item):
 name,url=item
 try:
  r=requests.get(url,timeout=35)
  (root/(name+'.response')).write_text(r.text,encoding='utf-8')
  result={'url':url,'status':r.status_code}
  if r.status_code==200 and name.startswith('openalex'):
   data=r.json(); result['total']=data.get('meta',{}).get('count')
   result['works']=[{'title':w['display_name'],'year':w['publication_year'],'doi':w.get('doi'),'id':w['id'],'abstract_inverted_index':w.get('abstract_inverted_index')} for w in data.get('results',[])]
  return name,result
 except Exception as e: return name,{'url':url,'error':str(e)}
res=dict(concurrent.futures.ThreadPoolExecutor(3).map(fetch,queries.items()))
(root/'independent_search.json').write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
for name,result in res.items():
 print(name,{k:v for k,v in result.items() if k!='works'})
 for w in result.get('works',[]):
  if 'brownian' in w['title'].lower() or name.endswith('ancestors'): print(w['year'],w['title'],w['doi'])
# Independent exact arithmetic tests for the deterministic strict-gap implication.
from fractions import Fraction
vals=[Fraction(i,3) for i in range(-6,7)]
checks=0
for l in vals:
 for f in vals:
  for g in vals:
   for r in vals:
    if l<=f<g<=r:
     assert l<r; checks+=1
print('Exact strict-gap tests:',checks)
# Check the claimed Psi bound on a logarithmic grid.
maxratio=0.0
for k in range(-600,601):
 v=10.0**(k/100)
 psi=math.exp(-v)/math.sqrt(math.pi*v)+1+math.erf(math.sqrt(v))
 bound=1/math.sqrt(math.pi*v)+2
 assert psi<=bound+1e-12
 maxratio=max(maxratio,psi/bound)
print('Psi bound: 1201 points passed; maximum ratio',maxratio)
(root/'computation_checks.json').write_text(json.dumps({'strict_gap_exact_cases':checks,'psi_grid_points':1201,'psi_max_ratio':maxratio},indent=2),encoding='utf-8')
