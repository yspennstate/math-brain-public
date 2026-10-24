import urllib.request,urllib.parse,json,pathlib,concurrent.futures,xml.etree.ElementTree as ET
P=pathlib.Path(__file__).resolve().parent
jobs={
 'jacobi_arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('au:Sutton AND all:Jacobi')+'&max_results=10',
 'edelman_sutton':'https://arxiv.org/pdf/math-ph/0607038',
 'sutton_doi':'https://doi.org/10.1007/s10208-006-0215-9',
 'killip_nenciu':'https://arxiv.org/pdf/math/0410034',
 'sutton_mit':'https://math.mit.edu/~edelman/publications/betajacobi.pdf',
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'D0040-research/1.0'})
  with urllib.request.urlopen(req,timeout=40) as r: data=r.read(); mime=r.headers.get('Content-Type','')
  ispdf=data.startswith(b'%PDF'); path=P/(name+('.pdf' if ispdf else '.response')); path.write_bytes(data)
  result='OK '+str(len(data))+' '+str(path.name)
  if ispdf:
   try:
    import pymupdf
    doc=pymupdf.open(path); (P/(name+'.txt')).write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
    print(name,'PDF title/page 1:',doc[0].get_text()[:800],flush=True)
   except Exception as e: print(name,'EXTRACTION',repr(e),flush=True)
  elif name=='jacobi_arxiv':
   ns={'a':'http://www.w3.org/2005/Atom'}
   root=ET.fromstring(data)
   print([(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns)) for e in root.findall('a:entry',ns)],flush=True)
 except Exception as e: result='ERROR '+repr(e)
 with (P/'second_search_log.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(dict(date='2026-10-12',service=name,url=url,result=result))+'\n')
 print(name,result,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex: list(ex.map(fetch,jobs.items()))
