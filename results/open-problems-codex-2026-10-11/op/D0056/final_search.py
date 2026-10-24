import urllib.request,json,pathlib,concurrent.futures
urls={
'crossref_source':'https://api.crossref.org/works?query.title=A%20max-type%20recursive%20model%20some%20properties%20and%20open%20questions&rows=3',
'arxiv_http':'http://export.arxiv.org/api/query?search_query=all:%22Derrida%22+AND+all:%22Retaux%22&max_results=60',
'openalex_source_title':'https://api.openalex.org/works?filter=title.search:A%20max-type%20recursive%20model&per_page=5'
}
def f(it):
 k,u=it
 try:
  b=urllib.request.urlopen(u,timeout=25).read();pathlib.Path(k+'.json').write_bytes(b)
  out='OK '+str(len(b))
  if k=='crossref_source':
   d=json.loads(b)
   for p in d['message']['items']: print(p.get('title'),p.get('DOI'))
 except Exception as e:out=repr(e)
 return k,u,out
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rs=list(ex.map(f,urls.items()))
with open('LITERATURE.md','a',encoding='utf8') as out:
 for k,u,s in rs:out.write(f'- {k}: `{u}` — {s}\n')
print(rs)
