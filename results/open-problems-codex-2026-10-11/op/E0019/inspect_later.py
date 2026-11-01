from pathlib import Path
import xml.etree.ElementTree as E,json
for name in ['linear2024','singular2020','torus2017']:
 s=Path(name+'.txt').read_text(encoding='utf8');print('\nFILE',name);print(s[:18000] if name=='linear2024' else s[:10000])
r=E.parse('general_regular.json');n={'a':'http://www.w3.org/2005/Atom'}
for x in r.findall('a:entry',n):
 title=x.find('a:title',n).text
 if any(z in title.lower() for z in ['switch','piecewise','pdmp']):print(x.find('a:id',n).text,title,x.find('a:summary',n).text)
r=json.load(open('crossref_exact.json',encoding='utf8'))
for x in r['message']['items']:print(x.get('title'),x.get('DOI'),x.get('published'))
