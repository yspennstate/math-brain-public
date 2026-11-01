from research import fetch,ROOT
import concurrent.futures,urllib.parse as U,json,xml.etree.ElementTree as E
qs={
'arxiv_purchasing':'https://export.arxiv.org/api/query?id_list=1605.06072,2503.19999,2302.12029',
'arxiv_authors':'https://export.arxiv.org/api/query?search_query='+U.quote('au:Aldous AND (all:online OR all:spanning)')+'&max_results=30',
'openalex_retry':'https://api.openalex.org/works?search='+U.quote('online random weight minimal spanning trees')+'&per_page=5',
'openalex_title':'https://api.openalex.org/works?filter=title.search:'+U.quote('Online Random Weight Minimal Spanning Trees')+'&per_page=5',
'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/search?query='+U.quote('Aldous Angel Berestycki online')+'&limit=5&fields=title,year,authors,citationCount,url',
'crossref_purchasing':'https://api.crossref.org/works?query.title='+U.quote('Online purchasing under uncertainty')+'&rows=5',
'github_exact':'https://api.github.com/search/repositories?q='+U.quote('"Aldous" "spanning"'),
'purchasing_pdf':'https://arxiv.org/pdf/1605.06072',
'disjoint_pdf':'https://arxiv.org/pdf/2503.19999',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: rs=list(ex.map(fetch,qs.items()))
with (ROOT/'LITERATURE.md').open('a',encoding='utf-8') as f:
 for a,b,c,d in rs:f.write(f'\n2026-10-11 | {a} | {b} | {c} ({d} bytes)\n')
for r in rs:print(r)
import pymupdf
for name in ['purchasing_pdf','disjoint_pdf']:
 try:
  doc=pymupdf.open(stream=(ROOT/(name+'.txt')).read_bytes(),filetype='pdf')
  (ROOT/(name+'_extracted.txt')).write_text('\n'.join(p.get_text() for p in doc),encoding='utf-8')
 except Exception as e:print(name,e)
