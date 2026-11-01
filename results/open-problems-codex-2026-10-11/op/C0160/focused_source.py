from pathlib import Path
import pymupdf
d=pymupdf.open('survey.pdf')
for i in [1,2,3,10,11,12,13,14]: print('PDF PAGE',i+1,'\n',d[i].get_text())
for i,p in enumerate(d):
 t=p.get_text()
 if 'Theorem 3.1' in t or 'Theorem 3.2' in t or 'Theorem 3.3' in t or 'Theorem 3.4' in t or 'Theorem 3.5' in t: print('THEOREM PAGE',i+1,'\n',t)
