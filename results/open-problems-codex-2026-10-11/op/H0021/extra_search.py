import requests, pathlib,xml.etree.ElementTree as E,json
from urllib.parse import quote
ns={'a':'http://www.w3.org/2005/Atom'}
u='http://export.arxiv.org/api/query?search_query='+quote('ti:"Hamilton cycles" AND au:Krivelevich')+'&max_results=15'
r=requests.get(u,timeout=30);pathlib.Path('hamilton_search.txt').write_bytes(r.content)
a=json.loads(pathlib.Path('search_log.json').read_text());a.append(dict(service='arxiv_hamilton',url=u,status=r.status_code,date='2026-10-12'));pathlib.Path('search_log.json').write_text(json.dumps(a,indent=2))
for x in E.fromstring(r.content).findall('a:entry',ns):print(x.findtext('a:id',namespaces=ns),x.findtext('a:title',namespaces=ns))
u='http://export.arxiv.org/api/query?search_query='+quote('(all:"spanning trees" OR all:"bounded-degree trees" OR all:"tree universality") AND submittedDate:[202608060000 TO 202610122359]')+'&start=80&max_results=80&sortBy=submittedDate&sortOrder=descending'
r=requests.get(u,timeout=30);pathlib.Path('arxiv_recent2.txt').write_bytes(r.content)
a.append(dict(service='arxiv_recent_page2',url=u,status=r.status_code,date='2026-10-12'));pathlib.Path('search_log.json').write_text(json.dumps(a,indent=2))
for x in E.fromstring(r.content).findall('a:entry',ns):
 t=x.findtext('a:title',namespaces=ns);s=x.findtext('a:summary',namespaces=ns)
 print(x.findtext('a:id',namespaces=ns),t.replace('\n',' '))
 if 'univers' in s.lower():print(s)
