import research_fetch as f
from pathlib import Path
import json, urllib.parse, concurrent.futures, subprocess
R=f.ROOT
queries={
 'openalex_citing':'https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:W2172014396','per-page':200}),
 'openalex_citing_preprint':'https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:W4353013745','per-page':200}),
 'arxiv_continuous':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"continuous" AND (all:"SOS" OR all:"solid-on-solid") AND (all:"repulsion" OR all:"fluctuations")','max_results':50}),
 'arxiv_leads':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'id_list':'2609.07578,2302.00547,2609.01499','max_results':10}),
 'crossref_focused':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.title':'entropic repulsion interface','rows':30}),
 'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0509695?fields=title,citations.title,citations.year,citations.externalIds',
 'middle_pdf':'https://arxiv.org/pdf/2609.07578',
 'degenerate_pdf':'https://arxiv.org/pdf/2302.00547',
}
def get(item):
 name,url=item
 if name.endswith('_pdf'):
  import urllib.request
  try:
   with urllib.request.urlopen(url,timeout=45) as x: data=x.read()
   (R/(name+'.pdf')).write_bytes(data)
   import pymupdf
   doc=pymupdf.open(R/(name+'.pdf'))
   (R/(name+'.txt')).write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
   return {'service_query':name,'url':url,'status':'ok','bytes':len(data),'date':'2026-10-12'}
  except Exception as e: return {'service_query':name,'url':url,'status':repr(e),'date':'2026-10-12'}
 return f.fetch(item)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: results=list(ex.map(get,queries.items()))
(R/'followup_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for x in results: print(json.dumps(x),flush=True)
for name in ['openalex_citing','openalex_citing_preprint']:
 p=R/(name+'.json')
 if p.exists():
  d=json.loads(p.read_text(encoding='utf8')); print(name,'count',d.get('meta',{}).get('count'))
  for x in d.get('results',[]): print(x.get('publication_year'),x.get('title'),x.get('doi'))
