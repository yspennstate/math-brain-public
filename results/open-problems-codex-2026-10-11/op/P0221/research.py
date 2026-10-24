import concurrent.futures, urllib.request, urllib.parse, pathlib, json, datetime
ROOT=pathlib.Path(__file__).resolve().parent
urls={
'source':'https://www.stat.berkeley.edu/~aldous/Research/OP/Beres2008.pdf',
'author':'https://www.stat.berkeley.edu/~aldous/Research/OP/index.html',
'arxiv':'https://export.arxiv.org/api/query?search_query=all:'+urllib.parse.quote('"online" AND "spanning tree"')+'&max_results=30',
'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('Online random weight minimal spanning trees')+'&per-page=20',
'crossref':'https://api.crossref.org/works?query.bibliographic='+urllib.parse.quote('Online random weight minimal spanning trees')+'&rows=20',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('Online random weight minimal spanning trees')+'&limit=20&fields=title,authors,year,url,externalIds',
'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('online random spanning tree'),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (ROOT/(name+('.pdf' if name=='source' else '.txt'))).write_bytes(data)
  return name,url,'OK',len(data)
 except Exception as e:return name,url,'ERROR '+str(e),0
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: results=list(ex.map(fetch,urls.items()))
 with (ROOT/'LITERATURE.md').open('a',encoding='utf-8') as f:
  for name,url,status,size in results:
   f.write(f'\n2026-10-11 | {name} | {url} | {status} ({size} bytes)\n')
 for r in results:print(r)
 try:
  import pymupdf
  doc=pymupdf.open(ROOT/'source.pdf')
  (ROOT/'source_extracted.txt').write_text('\n'.join(f'\nPAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
 except Exception as e:print('PDF extraction:',e)
