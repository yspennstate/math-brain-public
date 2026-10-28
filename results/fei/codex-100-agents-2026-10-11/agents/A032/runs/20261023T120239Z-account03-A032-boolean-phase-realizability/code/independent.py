from pathlib import Path
from fractions import Fraction as F
import json,time
root=Path(__file__).resolve().parents[1];t0=time.perf_counter();checks=0
def ck(b):
 global checks
 checks+=1;assert b,checks
 assert time.perf_counter()-t0<55
def character(f):
 return [sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(f)) for s in range(len(f))]
def spectral(f):return [F(v*v,len(f)**2) for v in character(f)]
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,list):return [enc(v) for v in x]
 return x
a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1];b=[1-v*v for v in a]
core=[-1]+[1]*7;pc=spectral(core);ck(pc==[F(9,16)]+[F(1,16)]*7)
q=[]
for s in range(8):q.append(F(1,4)**s.bit_count()*F(3,4)**(3-s.bit_count()))
ck(sum(q)==1)
for sig in [-1,1]:
 h=[(-1 if (x&7).bit_count()%2 else 1)*core[x>>3] for x in range(64)]
 parent=[aa+sig*bb*v for v in h for aa,bb in zip(a,b)]
 raw=character(parent);p=[F(v*v,len(parent)**2) for v in raw]
 children=[]
 for x1 in [0,1]:
  ch=[parent[(x&15)|((x&~15)<<1)|(x1<<4)] for x in range(len(parent)//2)]
  ck(set(ch)=={-1,1});pp=spectral(ch);children.append(pp)
 ck(children[0]==children[1]);ck(sum(p[t] for t in range(len(p)) if t&16)==F(3,8))
 for s in range(len(children[0])):
  s0=(s&15)|((s&~15)<<1);ck(not(p[s0] and p[s0|16]));ck(p[s0]+p[s0|16]==children[0][s])
 ck(sum(p)==1)
 # Squared convolution rechecked by physical Boolean identity, and raw mean0
 # for each actual seed prefix singleton is checked without FWHT.
 for bit in [0,1,2]:ck(sum(v*(-1 if x&(1<<bit) else 1) for x,v in enumerate(h))==0)
 if sig==1:
  witness={'core_truth_table':core,'core_spectrum':pc,'target_product_reference':q,'parent_truth_table':parent,'raw_parent_walsh':raw,'child_spectra':children}
# Exact ghost threshold for tau=2-9/8 log2(3). No numerical logarithms.
ghosts=[F(j,64) for j in range(64)]+[F(1,3)];paid=unpaid=0;signs=[]
for rho in ghosts:
 d=rho.denominator;n=rho.numerator
 left=2**16*(d-n)**8;right=3**9*d**8
 sign=(left>right)-(left<right);paid+=sign<=0;unpaid+=sign>0
 ck(sign!=0)
 # Direct exact product identity for the complete cost's eighth power.
 ratio=F(2**16,3**9)*(1-rho)**8
 ck((ratio>1)==(sign>0));signs.append({'rho':rho,'increment_sign':sign})
ck(3**3<2**5);ck(3**9>2**14);ck(paid and unpaid)
result={'PASS':True,'checks':checks,'seconds':time.perf_counter()-t0,'direct_character_wrapper_bits':10,'ghost_threshold_cases':65,'paid_cases':paid,'positive_charge_cases':unpaid,'formal_status':'NOT_CLAIMED','witness':witness,'ghost_signs':signs}
(root/'out/independent.json').write_text(json.dumps(enc(result),indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:enc(v) for k,v in result.items() if k not in ['witness','ghost_signs']}))
