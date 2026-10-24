from pathlib import Path
import xml.etree.ElementTree as E,json,requests,concurrent.futures
ns={'a':'http://www.w3.org/2005/Atom'}
root=E.parse('arxiv_fractions.xml').getroot()
for e in root.findall('a:entry',ns):
 print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns).replace('\n',' '))
 print(e.findtext('a:summary',namespaces=ns).replace('\n',' ')[:600])
print('CROSSREF TARGET')
for e in json.loads(Path('crossref_target.json').read_text())['message']['items'][:20]:print(e.get('title'),e.get('DOI'))
jobs={'crossref_source':'https://api.crossref.org/works?query.title=Laplacian%20growth%20sandpiles%20and%20scaling%20limits&rows=3','arxiv_identity_recent':'https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:identity+OR+all:pattern)+AND+submittedDate:[20170101+TO+20261012]&max_results=100&sortBy=submittedDate&sortOrder=descending','arxiv_convergence':'https://arxiv.org/pdf/1105.0111'}
def f(k,u):
 try:
  r=requests.get(u,timeout=45);Path(k+('.pdf' if k=='arxiv_convergence' else '.xml' if k=='arxiv_identity_recent' else '.json')).write_bytes(r.content)
  if k=='arxiv_convergence':
   import pymupdf
   d=pymupdf.open(stream=r.content,filetype='pdf');Path('convergence.txt').write_text('\n'.join(f'\nPAGE {i+1}\n'+x.get_text() for i,x in enumerate(d)),encoding='utf8')
  return dict(service=k,url=u,status=r.status_code,bytes=len(r.content),date='2026-10-12')
 except Exception as e:return dict(service=k,url=u,error=str(e),date='2026-10-12')
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(lambda x:f(*x),jobs.items()))
p=Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+r,indent=2));print(json.dumps(r,indent=2))
