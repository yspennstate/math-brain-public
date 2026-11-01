import concurrent.futures, json, urllib.request, urllib.parse, pathlib, datetime
ROOT=pathlib.Path(__file__).resolve().parent
q=urllib.parse.quote
queries={
 'source_pdf':'https://arxiv.org/pdf/2608.26321',
 'source_abs':'https://arxiv.org/abs/2608.26321',
 'arxiv_api':'http://export.arxiv.org/api/query?search_query='+q('all:"non-backtracking" AND (all:"birthday" OR all:"Alon-Peres")')+'&max_results=30&sortBy=submittedDate&sortOrder=descending',
 'openalex':'https://api.openalex.org/works?search='+q('birthday paradox non-backtracking walks')+'&per-page=30',
 'crossref':'https://api.crossref.org/works?query='+q('Alon Peres non-backtracking birthday')+'&rows=20',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.26321?fields=title,authors,year,citations.title,citations.year,citations.externalIds',
 'github':'https://api.github.com/search/repositories?q='+q('"Alon-Peres"'),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'G0012-research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read(); status=r.status
  suffix='.pdf' if name=='source_pdf' else '.txt'
  (ROOT/(name+suffix)).write_bytes(data)
  result={'service':name,'url':url,'date':'2026-10-11','status':status,'bytes':len(data)}
 except Exception as e: result={'service':name,'url':url,'date':'2026-10-11','error':str(e)}
 with (ROOT/'LITERATURE.md').open('a',encoding='utf8') as f: f.write('\n'+json.dumps(result)+'\n')
 return result
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
  for result in pool.map(fetch,queries.items()): print(json.dumps(result))
 try:
  import pymupdf
  doc=pymupdf.open(ROOT/'source_pdf.pdf')
  (ROOT/'source.txt').write_text('\n'.join(page.get_text() for page in doc),encoding='utf8')
  print('PDF extracted',len(doc),'pages')
 except Exception as e: print('PDF extraction:',e)
