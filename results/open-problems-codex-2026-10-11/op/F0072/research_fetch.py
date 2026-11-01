from pathlib import Path
import urllib.request, urllib.parse, json, concurrent.futures, datetime
ROOT=Path(__file__).resolve().parent
queries={
 'source_pdf':'https://arxiv.org/pdf/math/0509695',
 'arxiv_sos':'http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"entropic repulsion" AND all:"solid-on-solid"','max_results':30}),
 'openalex_sos':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'continuous solid on solid entropic repulsion','per-page':30}),
 'openalex_source':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Localization and delocalization of random interfaces','per-page':5}),
 'crossref_sos':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'continuous solid on solid entropic repulsion','rows':30}),
 'semantic_sos':'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'continuous solid on solid entropic repulsion','limit':30,'fields':'title,authors,year,url,abstract,externalIds'}),
 'github_sos':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'"entropic repulsion" "SOS"','per_page':20}),
 'arxiv_absolute':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"random surfaces" AND all:"absolute value"','max_results':30}),
 'openalex_laplace':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'entropic repulsion non uniformly convex continuous interface','per-page':30}),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'F0072 mathematical research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as response: data=response.read()
  (ROOT/(name+('.pdf' if name=='source_pdf' else '.json'))).write_bytes(data)
  result={'service_query':name,'url':url,'date':str(datetime.date.today()),'bytes':len(data),'status':'ok'}
 except Exception as e: result={'service_query':name,'url':url,'date':str(datetime.date.today()),'status':repr(e)}
 return result
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
  results=list(ex.map(fetch,queries.items()))
 (ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
 for r in results: print(json.dumps(r),flush=True)
 try:
  import pymupdf
  doc=pymupdf.open(ROOT/'source_pdf.pdf')
  (ROOT/'source.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
  print('Extracted source using pymupdf')
 except Exception as e:
  try:
   import pypdf
   doc=pypdf.PdfReader(ROOT/'source_pdf.pdf')
   (ROOT/'source.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+p.extract_text() for i,p in enumerate(doc.pages)),encoding='utf8')
   print('Extracted source using pypdf')
  except Exception as e: print('PDF extraction failed:',repr(e))
