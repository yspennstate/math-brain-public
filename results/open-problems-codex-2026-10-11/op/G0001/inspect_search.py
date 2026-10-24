from pathlib import Path
import re,json,xml.etree.ElementTree as ET
s=Path('cerf_abs.txt').read_text();print(re.sub('<[^>]+>',' ',s)[-20000:])
for f in ['semantic.txt','openalex.txt']:
 if Path(f).exists(): print(f,Path(f).read_text()[:12000])
r=ET.fromstring(Path('arxiv.txt').read_text());ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns):print(e.find('a:id',ns).text,e.find('a:title',ns).text)
x=json.loads(Path('crossref.txt').read_text())
for it in x['message']['items'][:12]:print('CR',it.get('title'),it.get('DOI'),it.get('published'))
