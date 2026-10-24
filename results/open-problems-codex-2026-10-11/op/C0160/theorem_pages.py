import pymupdf
d=pymupdf.open('survey.pdf')
for i in range(15,21): print('PDF PAGE',i+1,'\n',d[i].get_text())
for i,p in enumerate(d):
 t=p.get_text()
 if 'Theorem 9.1' in t or 'Theorem 9.2' in t: print('ENDPOINT THEOREM',i+1,'\n',t)
