import urllib.request,urllib.parse,xml.etree.ElementTree as E,json,pathlib,concurrent.futures
urls={
'arxiv_targeted':'http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('(all:percolation AND (all:subcritical OR all:"finite graphs" OR all:"spectral radius")) AND submittedDate:[20260819 TO 20261013]')+'&max_results=100&sortBy=submittedDate&sortOrder=descending',
'course_pdf':'https://arxiv.org/pdf/2609.28552',
'crossref_later':'https://api.crossref.org/works?query='+urllib.parse.quote('percolation finite graphs spectral radius')+'&filter=from-pub-date:2026-08-19,until-pub-date:2026-10-12&rows=30',
'arxiv_cubic':'http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"percolation" AND (all:"finite trees" OR all:"largest cluster" OR all:"Galton-Watson")')+'&max_results=35&sortBy=relevance'}
def f(it):
 n,u=it
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'ResearchVerification/1.0'}),timeout=45) as r:d=r.read();c=r.status
  ext='.pdf' if n.endswith('pdf') else '.xml' if n.startswith('arxiv') else '.json'
  pathlib.Path(n+ext).write_bytes(d)
  return dict(service=n,url=u,status=c,bytes=len(d),date='2026-10-12')
 except Exception as e:return dict(service=n,url=u,error=str(e),date='2026-10-12')
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:r=list(ex.map(f,urls.items()))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+r,indent=2));print(json.dumps(r,indent=2))
ns={'a':'http://www.w3.org/2005/Atom'}
for name in ['arxiv_targeted','arxiv_cubic']:
 if pathlib.Path(name+'.xml').exists():
  print(name)
  for e in E.parse(name+'.xml').getroot().findall('a:entry',ns):print(e.find('a:id',ns).text,' '.join(e.find('a:title',ns).text.split()))
if pathlib.Path('course_pdf.pdf').exists():
 import pymupdf
 d=pymupdf.open('course_pdf.pdf');s='\n'.join(f'--- PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d));pathlib.Path('course.txt').write_text(s,encoding='utf-8')
 for term in ['2608.19145','Christoph','spectral radius','subcritical']:
  at=s.find(term);print('COURSE',term,at,s[max(0,at-200):at+1200] if at>=0 else '')
