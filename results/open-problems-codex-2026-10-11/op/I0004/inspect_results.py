import pathlib,json,re,xml.etree.ElementTree as ET
from html.parser import HTMLParser
p=pathlib.Path(__file__).parent
class Text(HTMLParser):
 def __init__(self): super().__init__();self.parts=[]
 def handle_data(self,d): self.parts.append(d)
t=Text();t.feed((p/'source_html.txt').read_text(encoding='utf8'));s=' '.join(t.parts);(p/'source_plain.txt').write_text(s,encoding='utf8')
for term in ['irrational','Guillotin','Problem 3','Le Ny']:
 print('\nSOURCE',term)
 for m in list(re.finditer(re.escape(term),s))[:12]: print(s[max(0,m.start()-500):m.end()+1200])
j=json.loads((p/'crossref.txt').read_text());print('\nCROSSREF')
for a in j['message']['items']:print(a.get('title'),a.get('DOI'),a.get('published'))
root=ET.fromstring((p/'arxiv_rotation.txt').read_bytes());ns={'a':'http://www.w3.org/2005/Atom'}
print('\nARXIV')
for e in root.findall('a:entry',ns):print(e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns),e.findtext('a:summary',namespaces=ns))
