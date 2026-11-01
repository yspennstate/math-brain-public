import concurrent.futures, urllib.request, urllib.parse, json, pathlib, datetime
P=pathlib.Path(__file__).parent
q=lambda s:urllib.parse.quote(s)
urls={
 'kenyon_pdf':'https://arxiv.org/pdf/0910.3129',
 'arxiv_electric':'https://export.arxiv.org/api/query?search_query='+q('all:dimer AND (all:electric OR all:correlators OR all:bosonization)')+'&max_results=25',
 'openalex_electric':'https://api.openalex.org/works?search='+q('dimer electric correlators')+'&per-page=20',
 'openalex_source':'https://api.openalex.org/works?search='+q('Lectures on dimers')+'&per-page=5',
 'crossref':'https://api.crossref.org/works?query='+q('dimer electric correlators')+'&rows=20',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+q('dimer electric correlators')+'&limit=20&fields=title,authors,year,url,externalIds',
 'github':'https://api.github.com/search/repositories?q='+q('dimer electric correlators'),
 'openalex_chaos':'https://api.openalex.org/works?search='+q('dimer imaginary multiplicative chaos')+'&per-page=20',
}
def fetch(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'F0087-research/1.0'}),timeout=45); b=r.read(); (P/(k+('.pdf' if k.endswith('pdf') else '.json'))).write_bytes(b); result=f'{k}: HTTP {r.status}, {len(b)} bytes'
 except Exception as e: result=f'{k}: {e}'
 with (P/'SEARCH_LOG.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps({'date':str(datetime.date.today()),'service':k,'url':u,'result':result})+'\n')
 return result
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for x in ex.map(lambda kv:fetch(*kv),urls.items()):print(x)
try:
 import pymupdf
 doc=pymupdf.open(P/'kenyon_pdf.pdf'); (P/'kenyon.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 print('PDF extracted',len(doc))
except Exception as e:print('PDF extraction:',e)
