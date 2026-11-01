import urllib.request,pathlib,json,concurrent.futures,xml.etree.ElementTree as E,urllib.parse
urls={
'regular_trees_pdf':'https://arxiv.org/pdf/1007.4508',
'arxiv_finite_tree':'http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:percolation AND (ti:"tree" OR ti:"trees") AND (all:"finite" OR all:"largest")')+'&max_results=60&sortBy=relevance'}
def f(it):
 n,u=it
 try:
  with urllib.request.urlopen(u,timeout=40) as r:d=r.read();code=r.status
  pathlib.Path(n+('.pdf' if n.endswith('pdf') else '.xml')).write_bytes(d)
  return dict(service=n,url=u,status=code,bytes=len(d),date='2026-10-12')
 except Exception as e:return dict(service=n,url=u,error=str(e),date='2026-10-12')
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:r=list(ex.map(f,urls.items()))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+r,indent=2));print(json.dumps(r))
if pathlib.Path('regular_trees_pdf.pdf').exists():
 import pymupdf
 d=pymupdf.open('regular_trees_pdf.pdf');s='\n'.join(f'--- PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d));pathlib.Path('regular_trees.txt').write_text(s,encoding='utf-8');print(s[:15000])
