from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib
R=Path(__file__).resolve().parents[1];checks=0

def ck(x):
 global checks
 assert x
 checks+=1

def lo(o,k):return F(o[k][0])
def hi(o,k):return F(o[k][1])
p=json.loads((R/'out/PILOT.json').read_text(encoding='utf-8'))
ck(lo(p,'residual')>F(3429,100000));ck(hi(p,'residual')<F(7,200))
ck(lo(p,'inherited_full_bank')>F(1,40));ck(hi(p,'inherited_full_bank')<F(13,500))
ck(lo(p,'product_full_bank')>F(19,100));ck(hi(p,'signed_reset')<-F(1,6))
ck(hi(p,'conversion_debit')<0);ck(hi(p,'residual')<lo(p,'product_full_bank')/5)
ck(lo(p,'product_full_bank')-hi(p,'residual')>F(31,200))
n=json.loads((R/'out/NONFLAT.json').read_text(encoding='utf-8'))
for k,bound in [('inherited_full_bank',-F(7,1000)),('product_full_bank',-F(67,1000)),('conversion_debit',-F(47,1000))]:ck(hi(n,k)<bound)
ck(lo(n,'residual')>F(41,1000));ck(lo(n,'signed_reset')>F(3,50));ck(all(F(i)>0 for i in n['child_I']))
d=json.loads((R/'out/DICTATOR.json').read_text(encoding='utf-8'))
ck(lo(d,'residual')>F(8,5));ck(hi(d,'product_full_bank')<F(43,50))
# Separate O(N^2) character-sum representation, no FWHT or imported helper.
g=(-1,1,1,1);f=[]
for x in range(64):
 S,W,U,V=[(x>>k)&1 for k in range(4)];A=(W*U*V) or (S*(U or V));f.append(1+A*(g[x>>4]-1))
children=[[y for x,y in enumerate(f) if x>>4&1==b] for b in [0,1]]
def hist(v):
 N=len(v);return Counter(F(sum(y*(-1 if (m&x).bit_count()%2 else 1) for x,y in enumerate(v)),N)**2 for m in range(N))
ck(hist(f)==Counter({F(1,1024):44,F(9,1024):12,F(25,1024):4,F(49,1024):3,F(625,1024):1}))
ck(hist(children[0])==Counter({F(1,256):22,F(9,256):6,F(25,256):2,F(49,256):1,F(81,256):1}))
ck(hist(children[1])==Counter({F(1):1,F(0):31}))
# Distinct complete banks: entropy-only must not be mislabeled full CE.
ck(hi(p,'inherited_full_bank')<lo(p,'residual'))
ck(lo(p,'available_bank')>hi(p,'product_full_bank'))
summary={'status':'PASS','checks':checks,'method':'rational sign readback plus separate character-sum Walsh histograms','full_terminals_retained':True,'no_Lean_claim':True}
(R/'out/FINAL_AUDIT.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8');print(summary)
