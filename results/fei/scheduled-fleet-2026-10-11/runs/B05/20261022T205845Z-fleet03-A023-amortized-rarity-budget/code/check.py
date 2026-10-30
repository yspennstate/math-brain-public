"""Frozen exact checks; inherited arithmetic only, no inherited conclusions."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import importlib.util, json, time, hashlib, sys
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parents[1]
HELPER=RUN.parents[1]/'runs/20261014T022245Z-fleet05-A023-amortized-rarity-budget/code/check_block.py'
spec=importlib.util.spec_from_file_location('exact',HELPER)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
START=time.perf_counter();CHECKS=0
def ck(v):
 global CHECKS
 assert v
 CHECKS+=1
 if time.perf_counter()-START>60: raise RuntimeError('Frozen 60-second cap')
def save(name,obj): (RUN/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def dump(v): return {str(k):str(x) for k,x in v.items()}
def Hhist(hist):
 out={}
 for p,count in hist.items():
  if p: h.lg(out,p,-count*p)
 return out
def walsh(v):
 a=list(v);s=1
 while s<len(a):
  for st in range(0,len(a),2*s):
   for j in range(st,st+s):a[j],a[j+s]=a[j]+a[j+s],a[j]-a[j+s]
  s*=2
 return a
def influence(v):
 N=len(v)
 return Q(sum(v[x]!=v[x^(1<<i)] for i in range(N.bit_length()-1) for x in range(N)),N)
def compressed(m):
 M=1<<m;L=1<<(m//2);d=Q(1,M);e=Q(1,L)
 # Signs aligned with b(v)chi_v have mean e on the whole spectrum.
 single=Counter()
 single[(e-2*d)**2]+=M//2+L//2
 single[(e+2*d)**2]+=M//2-L//2
 root=Counter({d:M//2})
 root[(e-d)**2]+=M//4+L//2
 root[(e+d)**2]+=M//4-L//2
 D=h.add((1,h.rational(m)),(-1,Hhist(single)))
 J=h.add((1,h.rational(m*(1-Q(3,2)*d))),(-1,Hhist(root)))
 H=h.add((1,Hhist(root)),(1,h.rational(3*m*d)))
 ck(sum(p*n for p,n in single.items())==1)
 ck(sum(p*n for p,n in root.items())==1-Q(3,2)*d)
 ck(h.sign(D)>=0)
 ck(h.sign(h.add((1,D),(-1,h.rational(12*d))))<0)
 ck(h.sign(h.add((-1,J),(-1,h.rational(Q(33,40)*d))))<0)
 for eta in [0,1]:
  R=(Q(3*m,2)-Q(eta,2))*d
  HT=h.add((1,h.rational(m)),(-Q(1,2),D))
  E=h.add((1,H),(-1,HT),(-1,h.rational(R)))
  expected=h.add((Q(1,2),D),(-1,J),(1,h.rational(Q(eta,2)*d)))
  ck(E==expected)
  ck(h.sign(h.add((1,E),(-1,h.rational(Q(313,80)*2*d))))<0)
 return d,root,D,J,H
def direct(m,v,w):
 M=1<<m
 b=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2)) for x in range(M)]
 bv=[-t if x==v else t for x,t in enumerate(b)]
 bw=[-t if x==w else t for x,t in enumerate(b)]
 cores=[g+[-t for t in g] for g in [b,bv,bw]]
 f=[cores[0 if not (x&1) else (2 if x&2 else 1)][x>>2] for x in range(8*M)]
 W=walsh(f);N=len(f);hist=Counter(Q(t*t,N*N) for t in W if t)
 delta,root,D,J,H=compressed_cache[m]
 expected=Counter(root);expected[delta*delta]+=3*M//2
 ck(hist==expected)
 ck(Hhist(hist)==H)
 IT=sum(p*influence(g) for p,g in zip([Q(1,2),Q(1,4),Q(1,4)],cores))
 IC=2*delta;ck(influence(f)==IT+IC)
 eta=int((v^w).bit_count()==1)
 R=2*sum(pi*pj*influence([x*y for x,y in zip(cores[i],cores[j])]) for i,j,pi,pj in [(0,1,Q(1,2),Q(1,4)),(0,2,Q(1,2),Q(1,4)),(1,2,Q(1,4),Q(1,4))])
 ck(R==(Q(3*m,2)-Q(eta,2))*delta);ck(R<=2*IT)
 for g in cores:
  ck(influence(g)>=1+Q(m,2)-2*m*delta)
  ck(h.sign(h.add((1,h.ent(tuple(g))),(-1,h.rational(2*influence(g)))))<=0)
 ck(h.sign(h.add((1,H),(-1,h.rational(4*influence(f)))))<0)
 return {'m':m,'v':v,'w':w,'adjacent':eta,'I_C':str(IC),'R':str(R),'I_T':str(IT)}
compressed_cache={m:compressed(m) for m in range(4,41,2)}
rows=[]
with (RUN/'out/direct_rows.jsonl').open('w',encoding='utf-8') as out:
 for m,pairs in [(4,[(v,w) for v in range(16) for w in range(16) if v!=w]),(6,[(0,w) for w in range(1,9)])]:
  for v,w in pairs:
   row=direct(m,v,w);rows.append(row);out.write(json.dumps(row)+'\n');out.flush()
save('scalar_rows.json',[{'m':m,'D':dump(x[2]),'J':dump(x[3]),'H':dump(x[4])} for m,x in compressed_cache.items()])
save('sign_certificates.json',list(h.SIGNS.values()))
save('helper_receipt.json',{'path':str(HELPER),'sha256':hashlib.sha256(HELPER.read_bytes()).hexdigest()})
result={'status':'PASS','direct_cases':len(rows),'scalar_cases':len(compressed_cache),'case_count':len(rows)+len(compressed_cache),'exact_assertions':CHECKS,'sign_certificates':len(h.SIGNS),'elapsed_seconds':time.perf_counter()-START,'scope':'Finite checks support the separately written all-m analytic proof; no universal FEI claim.'}
save('validation.json',result);print(json.dumps(result))
