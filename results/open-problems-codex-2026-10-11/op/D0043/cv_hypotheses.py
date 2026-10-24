from pathlib import Path
import pymupdf
r=Path(__file__).resolve().parent
doc=pymupdf.open(r/'CV.pdf')
for i in [2,3,4]:print('CV PDF PAGE',i+1,doc[i].get_text(),flush=True)
text=(r/'CV.txt').read_text(encoding='utf8')
for w in ['Example 1.','Assumptions 1.1','V0(x) =','Theorem 1.7']:
 pos=text.find(w);print(w,text[max(0,pos-300):pos+3000],flush=True)
doc=pymupdf.open(r/'KRV.pdf'); print('KRV PDF PAGE 9',doc[8].get_text(),flush=True)
