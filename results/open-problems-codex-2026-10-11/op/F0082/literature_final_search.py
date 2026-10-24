import json,urllib.request,pathlib,concurrent.futures,xml.etree.ElementTree as E
q={
'arxiv_planar':'https://export.arxiv.org/api/query?search_query=all:%22planar%20matching%22%20AND%20all:Poisson&max_results=40',
'crossref_source':'https://api.crossref.org/works?query.title=Poisson%20matching&query.author=Holroyd&rows=5',
'openalex_citing':'https://api.openalex.org/works?filter=cites:W2109829856&per-page=100'}
# The guessed OpenAlex ID is deliberately NOT used: resolve source first.
q.pop('openalex_citing')
def f(kv):
 k,u=kv
 try:
  b=urllib.request.urlopen(u,timeout=35).read();pathlib.Path(k+('.xml' if k.startswith('arxiv') else '.json')).write_bytes(b);s=f'OK {len(b)} bytes'
 except Exception as e:s=str(e)
 return k,u,s
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=2).map(f,q.items()));print(r)
with open('LITERATURE.md','a',encoding='utf8') as o:
 for k,u,s in r:o.write(f'- 2026-10-11 {k}: {u} — {s}.\n')
if pathlib.Path('crossref_source.json').exists():
 for e in json.load(open('crossref_source.json',encoding='utf8'))['message']['items']:print(e.get('title'),e.get('DOI'),e.get('published'),e.get('volume'),e.get('page'))
if pathlib.Path('arxiv_planar.xml').exists():
 ns={'a':'http://www.w3.org/2005/Atom'}
 for e in E.parse('arxiv_planar.xml').getroot().findall('a:entry',ns):print(e.find('a:title',ns).text,e.find('a:id',ns).text)
