import requests,pathlib,json,xml.etree.ElementTree as E
from urllib.parse import quote
u='http://export.arxiv.org/api/query?search_query='+quote('all:"universality" AND (all:"trees" OR all:"tree") AND submittedDate:[202608060000 TO 202610122359]')+'&max_results=100&sortBy=submittedDate&sortOrder=descending'
r=requests.get(u,timeout=35);pathlib.Path('arxiv_universality_recent.txt').write_bytes(r.content)
a=json.loads(pathlib.Path('search_log.json').read_text(encoding='utf8'));a.append(dict(service='arxiv_recent_universality',url=u,status=r.status_code,date='2026-10-12'));pathlib.Path('search_log.json').write_text(json.dumps(a,indent=2),encoding='utf8')
ns={'a':'http://www.w3.org/2005/Atom'}
root=E.fromstring(r.content);print('TOTAL',root.findtext('{http://a9.com/-/spec/opensearch/1.1/}totalResults'))
for x in root.findall('a:entry',ns):
 t=x.findtext('a:title',namespaces=ns);s=x.findtext('a:summary',namespaces=ns)
 print(x.findtext('a:id',namespaces=ns),t.replace('\n',' '))
 if any(w in s.lower() for w in ['random graph','spanning','bounded-degree']):print(s)
