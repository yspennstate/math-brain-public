from pathlib import Path
import json,xml.etree.ElementTree as ET
R=Path(__file__).parent
out=[]
for name in ['arxiv.json','arxiv_endpoint.json']:
 p=R/name
 if not p.exists(): continue
 try:
  ns={'a':'http://www.w3.org/2005/Atom'}
  for e in ET.fromstring(p.read_bytes()).findall('a:entry',ns):
   out.append({'service':name,'id':e.find('a:id',ns).text,'title':e.find('a:title',ns).text,'published':e.find('a:published',ns).text,'summary':e.find('a:summary',ns).text})
 except Exception as e: out.append({'service':name,'error':str(e)})
for name in ['crossref.json','crossref_endpoint.json','openalex_retry.json','openalex_citations.json','openalex_doi.json','semantic_doi.json','github_retry.json']:
 p=R/name
 if not p.exists():continue
 try:
  d=json.loads(p.read_bytes())
  if name.startswith('crossref'):
   for x in d['message']['items']:out.append({'service':name,'title':x.get('title'),'DOI':x.get('DOI'),'published':x.get('published'),'authors':x.get('author')})
  elif name.startswith('openalex'):
   for x in d.get('results',[d]):out.append({'service':name,'title':x.get('title'),'id':x.get('id'),'date':x.get('publication_date'),'doi':x.get('doi'),'cited_by_count':x.get('cited_by_count')})
  else:out.append({'service':name,'response':d})
 except Exception as e:out.append({'service':name,'error':str(e)})
(R/'search_summary.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf8')
for x in out:
 if x.get('service','').startswith('arxiv'):
  print(x['id'],x['published'],x['title'].replace('\n',' ')); print(x['summary'][:900])
 else: print(json.dumps(x,ensure_ascii=False)[:1200])
