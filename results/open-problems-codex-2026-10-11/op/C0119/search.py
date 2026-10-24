import urllib.request, urllib.parse, json, pathlib, concurrent.futures, datetime
ROOT=pathlib.Path(__file__).resolve().parent
queries={
 'source_pdf':'https://arxiv.org/pdf/0810.4221',
 'arxiv':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"directed polymer" AND (all:chaos OR all:superconcentration)','start':0,'max_results':60}),
 'openalex_search':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'directed polymers disorder chaos','per-page':30}),
 'openalex_source':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Chaos concentration and multiple valleys','per-page':5}),
 'crossref':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'directed polymers chaos','rows':30}),
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'directed polymers chaos','limit':30,'fields':'title,authors,year,url,externalIds,abstract'}),
 'github':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'directed polymer chaos','per_page':20}),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'C0119-research/1.0'})
  with urllib.request.urlopen(req,timeout=60) as r: data=r.read()
  suffix='.pdf' if name=='source_pdf' else '.txt'
  (ROOT/(name+suffix)).write_bytes(data)
  return {'name':name,'url':url,'date':str(datetime.date.today()),'bytes':len(data),'status':'ok'}
 except Exception as e: return {'name':name,'url':url,'date':str(datetime.date.today()),'status':str(e)}
if __name__=='__main__':
 results=list(concurrent.futures.ThreadPoolExecutor(max_workers=6).map(fetch,queries.items()))
 (ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
 print(json.dumps(results,indent=2))
 try:
  import pymupdf
  doc=pymupdf.open(ROOT/'source_pdf.pdf')
  (ROOT/'source.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
  print('PDF text extracted',len(doc))
 except Exception as e: print('PDF extraction:',e)
