from pathlib import Path
from html.parser import HTMLParser
class P(HTMLParser):
 def __init__(self):super().__init__();self.s=[]
 def handle_data(self,d):self.s.append(d)
for f in ['cerf_html','new_abs','new_html']:
 p=P();p.feed(Path(f+'.txt').read_text());s=' '.join(p.s);Path(f+'_plain.txt').write_text(s,encoding='utf8')
 if f=='cerf_html':print('CERF',s[:8000])
 elif f=='new_abs': print('NEW ABS',s[s.find('Title:'):s.find('Submission history')+600])
 else:
  for key in ['Theorem 1.1','Theorem 1.2','site percolation','critical point','Cerf','θ (']:
   start=0
   for j in range(5):
    i=s.lower().find(key.lower(),start)
    if i<0:break
    print(key,s[max(0,i-300):i+2000]);start=i+len(key)
