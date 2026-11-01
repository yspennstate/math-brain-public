from pathlib import Path
import json,xml.etree.ElementTree as E,urllib.request,concurrent.futures
ns={'a':'http://www.w3.org/2005/Atom'}
r=E.parse('arxiv_http.json')
for e in r.findall('a:entry',ns):print(e.find('a:id',ns).text,e.find('a:title',ns).text.strip())
urls={
'openalex_source_doi':'https://api.openalex.org/works/https://doi.org/10.1007/978-981-15-0302-3_6',
'openalex_citing_doi':'https://api.openalex.org/works?filter=cites:https%3A%2F%2Fdoi.org%2F10.1007%2F978-981-15-0302-3_6&per_page=100',
'semantic_citing':'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/978-981-15-0302-3_6/citations?fields=title,year,externalIds&limit=100'
}
def f(it):
 k,u=it
 try:
  b=urllib.request.urlopen(u,timeout=20).read();Path(k+'.json').write_bytes(b);s='OK '+str(len(b))
 except Exception as e:s=repr(e)
 return k,u,s
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rs=list(ex.map(f,urls.items()))
with open('LITERATURE.md','a',encoding='utf8') as out:
 for k,u,s in rs:out.write(f'- {k}: `{u}` — {s}\n')
print(rs)
