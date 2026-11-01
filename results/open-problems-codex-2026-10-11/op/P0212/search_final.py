exec(open('search.py',encoding='utf8').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={
 'arxiv_mathlow':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('cat:math.PR AND all:coalescing AND (all:density OR all:genealogy)')+'&max_results=80&sortBy=submittedDate&sortOrder=descending',
 'arxiv_cbsep':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('ti:"Coalescing and branching simple symmetric exclusion process"')+'&max_results=10',
 'semantic_cbsep':'https://api.semanticscholar.org/graph/v1/paper/020d65a04951ea2d5d626cf83796d35c81175360?fields=title,authors,year,externalIds,url',
 'crossref_cbsep':'https://api.crossref.org/works?query.title='+urllib.parse.quote('Coalescing and branching simple symmetric exclusion process')+'&rows=3',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: results=list(pool.map(fetch,queries.items()))
with (root/'LITERATURE.md').open('a',encoding='utf8') as f:
 for name,url,state in results: f.write(f'- {name}, 2026-10-11: {url}\n  Result: {state}\n'); print(name,state)
import xml.etree.ElementTree as E
ns={'a':'http://www.w3.org/2005/Atom'}
for name in ['arxiv_mathlow','arxiv_cbsep']:
 p=root/(name+'.txt')
 if p.exists():
  for x in E.parse(p).getroot().findall('a:entry',ns): print(x.findtext('a:id',namespaces=ns),x.findtext('a:title',namespaces=ns))
if (root/'semantic_cbsep.txt').exists():print((root/'semantic_cbsep.txt').read_text())
