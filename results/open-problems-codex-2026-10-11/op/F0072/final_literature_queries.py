import research_fetch as f
import json,urllib.parse,xml.etree.ElementTree as ET
R=f.ROOT
queries={
 'openalex_exact_sos':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'"continuous SOS"','per-page':30}),
 'sakagawa_page':'https://link.springer.com/article/10.1007/s10955-009-9745-x',
}
results=[]
for q in queries.items():
 r=f.fetch(q);results.append(r);print(json.dumps(r),flush=True)
(R/'final_search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
p=R/'openalex_exact_sos.json'
if p.exists():
 for x in json.loads(p.read_text(encoding='utf8')).get('results',[]):
  print(x.get('title'),x.get('publication_year'),x.get('doi'),flush=True)
  inv=x.get('abstract_inverted_index')
  if inv:
   words={k:v for v,positions in inv.items() for k in positions};print(' '.join(words[k] for k in sorted(words)),flush=True)
p=R/'sakagawa_page.json'
if p.exists():
 s=p.read_text(encoding='utf8')
 for term in ['Abstract','gradient','self-potential','Gaussian']:
  k=s.find(term);print(term,s[max(0,k-100):k+1800],flush=True)
