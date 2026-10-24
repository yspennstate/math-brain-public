from pathlib import Path
from html.parser import HTMLParser
import json
class P(HTMLParser):
 def __init__(self):super().__init__();self.s=[]
 def handle_data(self,d):self.s.append(d)
for f in ['site_counter_abs','site_locality_abs','supercritical_abs']:
 p=P();p.feed(Path(f+'.txt').read_text());s=' '.join(p.s);Path(f+'_plain.txt').write_text(s,encoding='utf8');print(f,s[s.find('Title:'):s.find('Subjects:')])
x=json.loads(Path('crossref_recent.txt').read_text())
for it in x['message']['items']:
 title=' '.join(it.get('title',[]))
 print('CR recent',title,it.get('DOI'),it.get('published'))
