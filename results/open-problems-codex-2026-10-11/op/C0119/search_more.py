from search import fetch, ROOT
import urllib.parse,json,concurrent.futures,xml.etree.ElementTree as ET
q={
 'arxiv_graham':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'ti:"Sublinear variance" AND au:Graham','max_results':10}),
 'arxiv_chaos':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'(all:"disorder chaos" OR all:"noise sensitivity") AND (all:polymer OR all:"last passage")','max_results':40}),
 'arxiv_alexander':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'ti:"Subgaussian concentration" AND au:Zygouras','max_results':5}),
 'crossref_source':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.title':'Chaos concentration and multiple valleys','rows':5}),
 'openalex_retry':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'"Chaos, concentration, and multiple valleys"','per_page':5}),
 'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:0810.4221?fields=title,year,citationCount,citations.title,citations.year,citations.externalIds',
}
res=list(concurrent.futures.ThreadPoolExecutor(max_workers=4).map(fetch,q.items()))
(ROOT/'search_more_log.json').write_text(json.dumps(res,indent=2),encoding='utf8')
print(json.dumps(res,indent=2))
for n in ['arxiv_graham','arxiv_chaos','arxiv_alexander']:
 try:
  ns={'a':'http://www.w3.org/2005/Atom'}
  for e in ET.parse(ROOT/(n+'.txt')).findall('a:entry',ns):
   print(e.find('a:id',ns).text,e.find('a:title',ns).text.strip(), e.find('a:summary',ns).text.strip()[:2400])
 except Exception as ex: print(ex)
