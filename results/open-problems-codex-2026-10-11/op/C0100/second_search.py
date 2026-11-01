import requests,pathlib,json,concurrent.futures,xml.etree.ElementTree as E
jobs={'arxiv_identity_dirichlet':'https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:identity+AND+all:Dirichlet)&max_results=30','crossref_identity_dirichlet':'https://api.crossref.org/works?query.bibliographic=sandpile%20identity%20Dirichlet%20scaling%20limit&rows=15'}
def f(k,u):
 try:
  r=requests.get(u,timeout=40);pathlib.Path(k+('.xml' if k.startswith('arxiv') else '.json')).write_bytes(r.content);return {'date':'2026-10-12','service':k,'url':u,'status':r.status_code}
 except Exception as e:return {'date':'2026-10-12','service':k,'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:rs=list(ex.map(lambda x:f(*x),jobs.items()))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+rs,indent=2));print(json.dumps(rs,indent=2))
ns={'a':'http://www.w3.org/2005/Atom'}
r=E.parse('arxiv_identity_dirichlet.xml').getroot()
for e in r.findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns))
print('CROSSREF')
for e in json.load(open('crossref_identity_dirichlet.json'))['message']['items']:print(e.get('title'),e.get('DOI'))
