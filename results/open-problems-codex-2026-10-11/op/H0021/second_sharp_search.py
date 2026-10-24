import requests,pathlib,json,xml.etree.ElementTree as E
from urllib.parse import quote
u='http://export.arxiv.org/api/query?search_query='+quote('ti:"Sharp threshold" AND all:"spanning trees"')+'&max_results=30'
r=requests.get(u,timeout=35);pathlib.Path('second_sharp_tree_search.txt').write_bytes(r.content)
a=json.loads(pathlib.Path('second_search_log.json').read_text(encoding='utf8'));a.append(dict(date='2026-10-12',service='arxiv_exact_sharp_trees',url=u,status=r.status_code,bytes=len(r.content)));pathlib.Path('second_search_log.json').write_text(json.dumps(a,indent=2),encoding='utf8')
ns={'a':'http://www.w3.org/2005/Atom'}
for x in E.fromstring(r.content).findall('a:entry',ns):print(x.findtext('a:id',namespaces=ns),x.findtext('a:title',namespaces=ns),x.findtext('a:summary',namespaces=ns))
u='https://api.crossref.org/works?query.title='+quote('Sharp threshold for the appearance of certain spanning trees in random graphs')+'&rows=3'
r=requests.get(u,timeout=35);pathlib.Path('second_crossref_sharp.txt').write_bytes(r.content);a.append(dict(date='2026-10-12',service='crossref_sharp_trees',url=u,status=r.status_code,bytes=len(r.content)));pathlib.Path('second_search_log.json').write_text(json.dumps(a,indent=2),encoding='utf8')
for w in r.json().get('message',{}).get('items',[]):print(w.get('title'),w.get('DOI'),w.get('link'))
