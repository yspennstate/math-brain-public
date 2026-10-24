from pathlib import Path
from html.parser import HTMLParser
class P(HTMLParser):
 def __init__(self):super().__init__();self.s=[]
 def handle_data(self,d):self.s.append(d)
for f in ['supercritical_html','site_locality_html']:
 p=P();p.feed(Path(f+'.txt').read_text());s=' '.join(p.s);Path(f+'_plain.txt').write_text(s,encoding='utf8')
 print('\nFILE',f)
 for key in ['Theorem 1.1','Theorem 1.2','site percolation','criticality','Cerf','θ ( p c']:
  start=0
  for j in range(3):
   i=s.lower().find(key.lower(),start)
   if i<0:break
   print('MATCH',key,s[max(0,i-180):i+2000]);start=i+len(key)
