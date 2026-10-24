from pathlib import Path
import xml.etree.ElementTree as E,urllib.request,concurrent.futures,json
ns={'a':'http://www.w3.org/2005/Atom'}
r=E.fromstring(Path('arxiv_2015.response').read_bytes())
for en in r.findall('a:entry',ns):print(en.findtext('a:id',namespaces=ns),en.findtext('a:title',namespaces=ns),en.findtext('a:summary',namespaces=ns))
urls={'old_pdf':'https://arxiv.org/pdf/1504.016 monotone','layered_pdf':'https://arxiv.org/pdf/2207.13173','arxiv_exact':'https://export.arxiv.org/api/query?search_query=(all:%222601.00291%22+OR+ti:%22monotonicity%22)+AND+all:%22percolation%22&max_results=100&sortBy=submittedDate&sortOrder=descending','openalex_citing':'https://api.openalex.org/works?filter=cites:doi:10.48550/arXiv.2601.00291&per-page=50'}
for en in r.findall('a:entry',ns):
 if 'remark' in en.findtext('a:title',namespaces=ns).lower():urls['old_pdf']='https://arxiv.org/pdf/'+en.findtext('a:id',namespaces=ns).split('/')[-1]
def get(k,u):
 try:
  b=urllib.request.urlopen(u,timeout=45).read();Path(k+('.pdf' if k.endswith('pdf') else '.response')).write_bytes(b);res=f'OK {len(b)}'
  if k.endswith('pdf'):
   import pymupdf
   d=pymupdf.open(stream=b,filetype='pdf');s='\n'.join(f'PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d));Path(k+'.txt').write_text(s,encoding='utf8');print(k,s[:11000])
 except Exception as e:res=str(e)
 with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write(f'\n- 2026-10-11 {k}: `{u}` — {res}\n')
 return k,res
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:print(list(ex.map(lambda x:get(*x),urls.items())))
