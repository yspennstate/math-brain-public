import pathlib, urllib.request, json, concurrent.futures, datetime
root=pathlib.Path.cwd()
queries={
 'source':'https://arxiv.org/pdf/0906.2293',
 'arxiv':'https://export.arxiv.org/api/query?search_query=all:colicin&max_results=30',
 'openalex':'https://api.openalex.org/works?search=colicin%20interacting%20particle&per-page=30',
 'crossref':'https://api.crossref.org/works?query=colicin%20spatial%20model&rows=30',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query=colicin%20spatial%20model&limit=30&fields=title,authors,year,externalIds,abstract',
 'github':'https://api.github.com/search/repositories?q=colicin+model&per_page=30',
 'openalex_source':'https://api.openalex.org/works/https://doi.org/10.1214/09-PS153'
}
def fetch(k,u):
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'ResearchAudit/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (root/(k+('.pdf' if k=='source' else '.json'))).write_bytes(data)
  return k,'OK',len(data),u
 except Exception as e: return k,'ERROR',str(e),u
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 rows=list(ex.map(lambda kv:fetch(*kv),queries.items()))
(root/'search_log.json').write_text(json.dumps(rows,indent=2))
with (root/'LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('# Literature audit\nDate: 2026-10-12 (machine date). API coverage limited to responses returned.\n')
 for row in rows: f.write('\n'+repr(row)+'\n')
print(json.dumps(rows,indent=2))
try:
 import pymupdf
 doc=pymupdf.open(root/'source.pdf'); (root/'source.txt').write_text('\n'.join(p.get_text() for p in doc),encoding='utf8')
 print('PDF extracted',len(doc))
except Exception as e: print('PDF extraction',repr(e))
