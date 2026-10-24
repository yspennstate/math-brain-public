from pathlib import Path
import urllib.request, urllib.parse, json, concurrent.futures, datetime
root=Path.cwd()
queries={
'kalai_pdf':'https://arxiv.org/pdf/1801.02602',
'arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"noise sensitivity" AND (all:"walks" OR all:"groups")')+'&max_results=40',
'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('noise sensitivity random walks groups')+'&per-page=30',
'openalex_source':'https://api.openalex.org/works/https://doi.org/10.1142/9789813272880_0017',
'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('noise sensitivity random walks Benjamini Brieussel')+'&rows=20',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('noise sensitivity random walks')+'&limit=20&fields=title,authors,year,url,abstract,externalIds',
'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('noise sensitivity random walks')}
def get(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'F0093-math-research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (root/(name+('.pdf' if name.endswith('pdf') else '.response'))).write_bytes(data)
  return name,url,'OK',len(data)
 except Exception as e:return name,url,str(e),0
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: results=list(ex.map(get,queries.items()))
with (root/'LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('# Literature search\n\nDate: 2026-10-12. Results are leads, not certified resolutions.\n\n')
 for name,url,status,size in results:f.write(f'- {name}: {url}\n  Result: {status}; {size} bytes.\n')
print(json.dumps(results,indent=2))
try:
 import pymupdf
 doc=pymupdf.open('kalai_pdf.pdf'); text='\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc));Path('kalai.txt').write_text(text,encoding='utf8')
 print(text[text.find('3.3.4',text.find('3.3.4')+1):][:8000])
except Exception as e:print('PDF extraction:',e)
