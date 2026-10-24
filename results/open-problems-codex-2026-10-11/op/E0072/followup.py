import research
import json, urllib.parse, xml.etree.ElementTree as ET
from pathlib import Path
P=Path(__file__).resolve().parent
queries={
 'arxiv_cancellation': 'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"cancellation norm" OR all:"spelling length" OR (all:"bi-invariant" AND all:"random walks")')+'&max_results=30',
 'openalex_doi': 'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.1406.0763',
 'semantic_citations': 'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1406.0763/citations?limit=100&fields=title,authors,year,url',
}
results=[research.fetch(x) for x in queries.items()]
try:
 d=json.loads((P/'openalex_doi.txt').read_text())
 wid=d['id'].split('/')[-1]
 results.append(research.fetch(('openalex_citing','https://api.openalex.org/works?filter=cites:'+wid+'&per-page=100')))
except Exception as e:
 # Issue an explicit citing-work lookup using the source's persistent DOI.
 results.append(research.fetch(('openalex_citing','https://api.openalex.org/works?filter=cites:https://doi.org/10.48550/arXiv.1406.0763&per-page=100')))
(P/'followup_search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print('FOLLOWUP',json.dumps(results),flush=True)
ns={'a':'http://www.w3.org/2005/Atom'}
for name in ['arxiv','arxiv_cancellation']:
 try:
  root=ET.fromstring((P/(name+'.txt')).read_text())
  entries=[{'title':e.findtext('a:title',namespaces=ns),'url':e.findtext('a:id',namespaces=ns),'authors':[a.findtext('a:name',namespaces=ns) for a in e.findall('a:author',ns)],'abstract':e.findtext('a:summary',namespaces=ns)} for e in root.findall('a:entry',ns)]
  (P/(name+'_summary.json')).write_text(json.dumps(entries,indent=2),encoding='utf-8')
  print(name,json.dumps(entries),flush=True)
 except Exception as e:print(name,str(e),flush=True)
