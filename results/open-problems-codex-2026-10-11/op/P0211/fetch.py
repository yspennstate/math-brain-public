import urllib.request, pathlib, concurrent.futures, json, urllib.parse, datetime
P=pathlib.Path('.')
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0'})
  b=urllib.request.urlopen(req,timeout=45).read(); (P/name).write_bytes(b)
  return name, url, len(b), 'OK'
 except Exception as e: return name,url,0,str(e)
q=urllib.parse.quote
jobs=[('coag_frag_mix.pdf','https://www.stat.berkeley.edu/~aldous/Research/OP/coag_frag_mix.pdf'),('hingant_yvinec.pdf','https://arxiv.org/pdf/1609.00697'),('granovsky.pdf','https://www.stat.berkeley.edu/~aldous/Research/OP/granovsky.pdf'),('arxiv.xml','http://export.arxiv.org/api/query?search_query='+q('all:"coagulation fragmentation" AND (all:"spectral gap" OR all:"mixing" OR all:"relaxation")')+'&max_results=30'),('openalex.json','https://api.openalex.org/works?search='+q('coagulation fragmentation spectral gap')+'&per-page=30'),('crossref.json','https://api.crossref.org/works?query='+q('coagulation fragmentation relaxation polymer')+'&rows=30'),('semantic.json','https://api.semanticscholar.org/graph/v1/paper/search?query='+q('coagulation fragmentation spectral gap')+'&limit=30&fields=title,authors,year,externalIds,url,abstract'),('github.json','https://api.github.com/search/repositories?q='+q('coagulation fragmentation'))]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: results=list(ex.map(fetch,jobs))
with open('search_log.jsonl','a',encoding='utf8') as f:
 for row in results: f.write(json.dumps({'date':'2026-10-11','file':row[0],'url':row[1],'bytes':row[2],'status':row[3]})+'\n')
print(json.dumps(results,indent=2))
try:
 import pymupdf
 for name in ['coag_frag_mix','hingant_yvinec','granovsky']:
  doc=pymupdf.open(name+'.pdf'); text='\n'.join('PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc)); pathlib.Path(name+'.txt').write_text(text,encoding='utf8')
 print(pathlib.Path('coag_frag_mix.txt').read_text(encoding='utf8'))
except ImportError:
 import pypdf
 for name in ['coag_frag_mix','hingant_yvinec','granovsky']:
  doc=pypdf.PdfReader(name+'.pdf'); text='\n'.join('PAGE '+str(i+1)+'\n'+p.extract_text() for i,p in enumerate(doc.pages)); pathlib.Path(name+'.txt').write_text(text,encoding='utf8')
 print(pathlib.Path('coag_frag_mix.txt').read_text(encoding='utf8'))
