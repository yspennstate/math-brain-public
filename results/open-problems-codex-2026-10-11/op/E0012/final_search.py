import json,pathlib,urllib.request,concurrent.futures,xml.etree.ElementTree as E
for w in json.load(open('crossref_exact.json',encoding='utf8'))['message']['items']:
 print('EXACT CROSSREF',w.get('title'),w.get('DOI'),w.get('published'),w.get('URL'))
for w in json.load(open('semantic_retry.json',encoding='utf8')).get('data',[]):print('SOURCE CITING',w.get('citingPaper'))
qs={
'arxiv_targeted':'https://export.arxiv.org/api/query?search_query=all:%22colicin%22+OR+all:%22allelopathic%22+OR+all:%22allelopathy%22&sortBy=submittedDate&sortOrder=descending&max_results=100',
'openalex_doi_filter':'https://api.openalex.org/works?filter=doi:https://doi.org/10.1214/08-AAP590&per-page=1',
'semantic_later':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2305.17016/citations?limit=100&fields=title,year,authors,externalIds',
'crossref_later':'https://api.crossref.org/works?query=Durrett%20Levin%20allelopathy%20Lanchier%20Mercer&rows=15'}
def f(k,u):
 try:
  d=urllib.request.urlopen(u,timeout=35).read();pathlib.Path(k+'.json').write_bytes(d);return [k,u,'OK',len(d)]
 except Exception as e:return [k,u,'ERROR',str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:r=list(ex.map(lambda kv:f(*kv),qs.items()))
with open('LITERATURE.md','a',encoding='utf8') as out:
 for row in r:out.write('\n2026-10-12 '+repr(row)+'\n')
print('SEARCHES',r)
for k,u,st,*_ in r:
 if st!='OK':continue
 if k.startswith('arxiv'):
  ns={'a':'http://www.w3.org/2005/Atom'}
  for e in E.parse(k+'.json').findall('a:entry',ns):print('ARXIV LATER',e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns))
 elif k.startswith('semantic'):print('PAPER CITATIONS',json.load(open(k+'.json',encoding='utf8')))
 elif k.startswith('crossref'):
  for w in json.load(open(k+'.json',encoding='utf8'))['message']['items']:print('CROSSREF LATER',w.get('title'),w.get('DOI'),w.get('published'))
