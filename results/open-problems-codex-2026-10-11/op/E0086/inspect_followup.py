from pathlib import Path
import json,xml.etree.ElementTree as E
p=Path('.')
d=json.loads(p.joinpath('search_semantic_citing.txt').read_text());print(json.dumps(d,ensure_ascii=False,indent=2))
ns={'a':'http://www.w3.org/2005/Atom'}
r=E.fromstring(p.joinpath('search_arxiv_okada.txt').read_text())
for e in r.findall('a:entry',ns):print(e.find('a:id',ns).text,e.find('a:title',ns).text.replace('\n',' '))
s=p.joinpath('search_favorite_2024.txt').read_text(encoding='utf-8'); print('FAVORITE TITLE',s[:1900]);
for word in ['1606.03787','Topics and problems','boundary','annul','Theorem 1.1']:
 print('FAVORITE',word,[s[max(0,i-130):i+280] for i in [s.find(word)] if i>=0])
b=p.joinpath('search_potential_book.txt').read_text(encoding='utf-8')
for word in ['Theorem 4.4.4','Proposition 4.4.2','a(x) =','π log']:
 i=b.find(word);print('BOOK',word,b[max(0,i-100):i+2200] if i>=0 else 'not found')
