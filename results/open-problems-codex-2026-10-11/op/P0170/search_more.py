import json, urllib.parse, xml.etree.ElementTree as ET
from pathlib import Path
from search import fetch
root=ET.parse('arxiv_api.xml'); ns={'a':'http://www.w3.org/2005/Atom'}
for e in root.findall('a:entry',ns):
 t=e.find('a:title',ns).text.replace('\n',' ')
 if any(s in t.lower() for s in ['independ','small prg','pseudorandom generator','decomposition','hyperconcentration','random restriction','sandwiching']):
  print(e.find('a:id',ns).text,t,flush=True)
qs={
 'arxiv_independence': 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"polynomial threshold" AND all:"independence"','max_results':60,'sortBy':'submittedDate','sortOrder':'descending'}),
 'arxiv_kane': 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'ti:"small PRG" OR ti:"poorly anticoncentrated" OR ti:"bounded independence"','max_results':40,'sortBy':'relevance'}),
 'openalex_retry': 'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Open problems in analysis of Boolean functions','per_page':3}),
 'semantic_source': 'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1204.6447?fields=title,year,citations.title,citations.year,citations.externalIds',
 'crossref_recent': 'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'bounded independence polynomial threshold functions','filter':'from-pub-date:2012-01-01','rows':30,'sort':'relevance'}),
 'paper_2103_07809': 'https://arxiv.org/pdf/2103.07809',
 'paper_2103_14134': 'https://arxiv.org/pdf/2103.14134',
 'paper_2504_10904': 'https://arxiv.org/pdf/2504.10904',
}
import concurrent.futures
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: list(pool.map(fetch,qs.items()))
import pymupdf
for name in ['paper_2103_07809','paper_2103_14134','paper_2504_10904']:
 try:
  doc=pymupdf.open(name+'.json',filetype='pdf')
  Path(name+'.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
  for i,p in enumerate(doc):
   text=p.get_text()
   if any(s in text.lower() for s in ['bounded independence','k-wise independence','k-independent','k-wise independent']):
    print(name,'PAGE',i+1,text[:5000],flush=True)
 except Exception as e: print(name,repr(e),flush=True)
