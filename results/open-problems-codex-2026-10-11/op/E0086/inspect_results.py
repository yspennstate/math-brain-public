from pathlib import Path
s=Path('source.txt').read_text(encoding='utf-8'); print(s[s.index('Let K(n'):s.index('Let K(n')+1000])
import xml.etree.ElementTree as E,json
ns={'a':'http://www.w3.org/2005/Atom'}
for name in ['boundary','covered']:
 root=E.fromstring(Path('search_arxiv_'+name+'.txt').read_text(encoding='utf-8'))
 for e in root.findall('a:entry',ns):
  print(e.find('a:id',ns).text,e.find('a:title',ns).text.replace('\n',' '))
for w in json.loads(Path('search_crossref_boundary.txt').read_text())['message']['items'][:8]: print('CR',w.get('title'),w.get('DOI'))
