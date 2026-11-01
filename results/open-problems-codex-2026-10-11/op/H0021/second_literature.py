import pathlib,requests,json,xml.etree.ElementTree as E
from urllib.parse import quote
u='http://export.arxiv.org/api/query?search_query='+quote('au:Hefetz AND au:Krivelevich AND (all:"spanning" OR all:"threshold")')+'&max_results=25'
r=requests.get(u,timeout=35);pathlib.Path('second_literature_arxiv.txt').write_bytes(r.content)
log={'date':'2026-10-12','service':'arxiv_second_attempt','url':u,'status':r.status_code,'bytes':len(r.content)}
pathlib.Path('second_search_log.json').write_text(json.dumps([log],indent=2),encoding='utf8')
ns={'a':'http://www.w3.org/2005/Atom'}
for x in E.fromstring(r.content).findall('a:entry',ns):
 print(x.findtext('a:id',namespaces=ns),x.findtext('a:title',namespaces=ns))
 s=x.findtext('a:summary',namespaces=ns)
 if 'tree' in s.lower():print(s)
