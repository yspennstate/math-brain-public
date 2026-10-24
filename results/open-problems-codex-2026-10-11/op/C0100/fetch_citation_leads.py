import requests,json,pathlib,xml.etree.ElementTree as E
url='https://export.arxiv.org/api/query?id_list=1911.01762,2009.05968,2609.21359&max_results=3'
r=requests.get(url,timeout=40);pathlib.Path('citation_leads.xml').write_bytes(r.content)
log=json.loads(pathlib.Path('search_log.json').read_text());log.append(dict(service='arxiv_citation_leads',url=url,status=r.status_code,date='2026-10-12'));pathlib.Path('search_log.json').write_text(json.dumps(log,indent=2))
ns={'a':'http://www.w3.org/2005/Atom'}
for e in E.fromstring(r.content).findall('a:entry',ns):
 print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns));print(e.findtext('a:summary',namespaces=ns))
