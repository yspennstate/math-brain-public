from pathlib import Path
s=Path('new_html_plain.txt').read_text();i=s.find('1.1  Introduction'); print(s[7000:16500])
import xml.etree.ElementTree as E
r=E.fromstring(Path('arxiv_exact.txt').read_text()); ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns): print(e.find('a:id',ns).text,e.find('a:title',ns).text)
