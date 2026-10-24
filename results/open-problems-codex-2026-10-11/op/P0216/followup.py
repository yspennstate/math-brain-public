from research import get,ROOT
import concurrent.futures,json,urllib.parse,xml.etree.ElementTree as ET
queries={
 'original':'https://www.stat.berkeley.edu/~aldous/Research/OP/common_subs.pdf',
 'notes':'https://www.stat.berkeley.edu/~aldous/Research/OP/substructures_posets.pdf',
 'arxiv_specific':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"common" AND (all:"posets" OR all:"two-dimensional partial")')+'&max_results=50',
 'crossref_specific':'https://api.crossref.org/works?query='+urllib.parse.quote('common induced random partial orders')+'&rows=20',
 'openalex_retry':'https://api.openalex.org/works?search='+urllib.parse.quote('Aldous common substructures')+'&per_page=10',
 'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('common random posets')+'&limit=10&fields=title,authors,year,url,externalIds',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: results=list(pool.map(get,queries.items()))
(ROOT/'followup_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for x in results: print(json.dumps(x))
for name in ['arxiv','arxiv_specific']:
 p=ROOT/(name+'.raw')
 if p.exists():
  root=ET.fromstring(p.read_bytes()); ns={'a':'http://www.w3.org/2005/Atom'}
  print(name,[(e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns)) for e in root.findall('a:entry',ns)])
for name in ['crossref','crossref_specific']:
 p=ROOT/(name+'.raw')
 if p.exists():
  d=json.loads(p.read_bytes()); print(name,[(x.get('title'),x.get('DOI')) for x in d['message']['items']])
for name in ['original','notes']:
 p=ROOT/(name+'.raw')
 if p.exists():
  try:
   import pymupdf
   doc=pymupdf.open(stream=p.read_bytes(),filetype='pdf')
  except ImportError:
   import pypdf
   doc=pypdf.PdfReader(p)
   txt='\n'.join(f'---PDF PAGE {i+1}---\n'+page.extract_text() for i,page in enumerate(doc.pages))
  else: txt='\n'.join(f'---PDF PAGE {i+1}---\n'+page.get_text() for i,page in enumerate(doc))
  (ROOT/(name+'.txt')).write_text(txt,encoding='utf8'); print(name,txt)
