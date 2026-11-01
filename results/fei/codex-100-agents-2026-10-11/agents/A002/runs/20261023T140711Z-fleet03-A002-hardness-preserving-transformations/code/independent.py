from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,itertools,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();c=0;applicable=0

def ok(x):
 global c
 assert x
 c+=1
 assert time.monotonic()-start<55

def rank(vs):
 basis={}
 for v in vs:
  while v:
   j=v.bit_length()-1
   if j in basis:v^=basis[j]
   else:basis[j]=v;break
 return len(basis)
bases=tuple(B for B in itertools.combinations(range(1,16),4) if rank(B)==4);ok(len(bases)==840)
@lru_cache(None)
def direct(f):
 W=tuple(sum(f[x]*(-1)**((x&s).bit_count()%2) for x in range(16)) for s in range(16))
 cost=tuple(sum(f[x]!=f[x^v] for x in range(16)) for v in range(16)); m=tuple(min(z,16-z) for z in cost)
 a=min(sum(m[v] for v in B) for B in bases)
 support=[s for s,w in enumerate(W) if w];r=rank(s^support[0] for s in support); beta=min((z for z in m if z),default=16)
 ok(sum(z*z for z in W)==256);return W,cost,m,a,r,beta
phases=(0,1,2,3,7,8,16,24,31,32,63,64,127,255,511,512,1023,1024,1536,2047)
mon=tuple(m for m in range(16) if m.bit_count()>=2)
roots=((1,)*16,tuple(-1 if x==0 else 1 for x in range(16)),tuple(-1 if x==1 else 1 for x in range(16)))
witness=None
for idx in phases:
 terms=tuple(m for j,m in enumerate(mon) if (idx>>j)&1)
 P=tuple(1-2*(sum(all((x>>j)&1 for j in range(4) if (m>>j)&1) for m in terms)%2) for x in range(16));wp,ip,mp,ap,r,beta=direct(P)
 for f in roots:
  wf,cf,mf,af,rf,bf=direct(f);neg=sum(x<0 for x in f)
  if beta<4*neg:continue
  applicable+=1;g=tuple(x*y for x,y in zip(f,P));wg,cg,mg,ag,rg,bg=direct(g)
  ok(ag-af>=ap-4*neg*r);ok(ag-af>=r*(beta-4*neg))
  for B in bases:
   # EVERY possible basis satisfies the source's full centered bound
   ok(sum(mg[v] for v in B)>=af+r*(beta-4*neg))
  for char in range(32):
   Pc=tuple(P[x]*(-1)**(((x&(char%16)).bit_count()+char//16)%2) for x in range(16));gc=tuple(x*y for x,y in zip(f,Pc));wc,cc,mc,ac,rc,bc=direct(gc)
   ok(mc==mg);ok(ac==ag);ok(sorted(z*z for z in wc)==sorted(z*z for z in wg))
  if idx==24 and neg==1:
   ok(Q(ap,16)==Q(5,4));ok(r==4);ok(Q(beta,16)==Q(1,4));ok(ap-r*beta==4)
   ok(r-Q(20*(ap-4*neg*r),16)==-1)
   witness={'phase':'x1*x2*x3+x1*x4','negative_point':f.index(-1),'rank':r,'a_phase':'5/4','beta':'1/4','old_charge':'0','new_charge':'1/4','K20_deficit_upper':'-1','actual_gain':str(Q(ag-af,16))}
# False uncentered replacement is refuted by a literal phase at a constant root
P=tuple((-1)**(x&1) for x in range(16));W,cost,m,ap,r,beta=direct(P)
ok(sum(cost[1<<j] for j in range(4))==16);ok(ap==0 and r==0);ok(ap<sum(cost[1<<j] for j in range(4)))
ok(witness is not None)
out={'status':'PASS','assertions':c,'candidate_pairs':60,'applicable_pairs':applicable,'bases_per_table':840,'phase_fixtures':20,'strict_witness':witness,'elapsed_seconds':time.monotonic()-start,'method':'direct characters, physical differences, EVERY independent unordered basis; no main helper imported'}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
