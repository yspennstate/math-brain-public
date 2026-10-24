import urllib.request,urllib.parse,xml.etree.ElementTree as E
from pathlib import Path
url='https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('ti:"growth" AND au:Bartholdi AND all:Grigorchuk')+'&max_results=15'
try:
 data=urllib.request.urlopen(url,timeout=30).read();Path('second_growth_search.response').write_bytes(data);root=E.fromstring(data);ns={'a':'http://www.w3.org/2005/Atom'}
 for e in root.findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns)[:2500])
 status='OK'
except Exception as e:status=str(e)
with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write('\n## Second attempt literature and brain queries\n\n- 2026-10-12 arXiv growth query: '+url+'; '+status+'\n- Read-only math-store recall: "Grigorchuk Liouville entropy noise sensitivity shared increments conditional entropy" and "Kaimanovich Vershik entropy criterion Liouville convolution total variation zero two law". General entropy and Pinsker hints; no specific solution.\n')
