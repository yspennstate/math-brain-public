import research_fetch as f
import json,xml.etree.ElementTree as ET,urllib.parse,concurrent.futures
R=f.ROOT
queries={
 'arxiv_gradient_repulsion':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'ti:"entropic repulsion" AND (all:"gradient" OR all:"continuous")','max_results':50}),
 'arxiv_wetting':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'ti:"Wetting of gradient fields" OR ti:"Entropic Repulsion of the Massless Field" OR (au:"Brydges" AND au:"Spencer")','max_results':20}),
}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex: results=list(ex.map(f.fetch,queries.items()))
(R/'last_search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for x in results: print(json.dumps(x),flush=True)
ns={'a':'http://www.w3.org/2005/Atom'}
for name in queries:
 p=R/(name+'.json')
 if p.exists():
  for e in ET.fromstring(p.read_bytes()).findall('a:entry',ns):
   print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns))
   print(e.findtext('a:summary',namespaces=ns))
for name in ['openalex_citing','openalex_laplace']:
 d=json.loads((R/(name+'.json')).read_text(encoding='utf8'))
 for x in d.get('results',[]):
  title=x.get('title','')
  if any(s.lower() in title.lower() for s in ['Wetting of gradient','self-potentials','sub-quadratic','degenerate','Concentration inequalities']):
   print('LEAD',title,x.get('doi'),x.get('publication_year'),'; '.join(a.get('author',{}).get('display_name','') for a in x.get('authorships',[])))
   print(x.get('primary_location',{}).get('landing_page_url'))
   inv=x.get('abstract_inverted_index')
   if inv:
    words={k:v for v,positions in inv.items() for k in positions}; print(' '.join(words[k] for k in sorted(words)))
# Exact old references on the mixture, as given by Dario's bibliography.
s=(R/'degenerate_pdf.txt').read_text(encoding='utf8')
for term in ['[36]','[37]','[94]']:
 k=s.rfind(term);print('REFERENCE',s[k:k+1000])
