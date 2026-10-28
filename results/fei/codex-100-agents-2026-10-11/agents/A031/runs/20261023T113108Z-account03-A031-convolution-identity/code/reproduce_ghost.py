from pathlib import Path
from fractions import Fraction as F
from math import lcm
from itertools import product
import json,time
R=Path(__file__).resolve().parents[1];checks=0;start=time.monotonic()
def ck(b):
 global checks
 assert b
 checks+=1
def prod(xs):
 a=F(1)
 for x in xs:a*=x
 return a
d=json.loads((R/'out/GHOST_CHECK.json').read_text(encoding='utf-8'))
for row in d['positive_KKT_cases']:
 p=[F(x) for x in row['p']];q=[F(x) for x in row['Q']];t=[F(x) for x in row['tilts']];lam=F(row['lambda'])
 rp=[q[i]*(1+t[i]) for i in range(6)];rm=[q[i]*(1-t[i]) for i in range(6)];ck(sum(rp)==sum(rm)==sum(q)==sum(p)==1)
 ck(all((rp[i]+rm[i])/2==q[i] for i in range(6)))
 for z in [0,1]:
  for j in [0,1]:
   i=3*z+j;ck(abs(t[i])<1);ck(p[i]*t[i]/(1-t[i]*t[i])==(-1)**z*lam*q[i])
  ck(t[3*z+2]==(-1)**z)
  delta=sum(q[i]*t[i] for i in range(3*z,3*z+3));g=sum(q[i] for i in range(3*z,3*z+3) if p[i]==0);ck(abs(delta)>g)
 # Objective identity checked as an exact rational product; no logarithm helper imported.
 scale=lcm(*(2*v.denominator for v in p));direct=F(1);formula=F(1)
 for i in range(6):
  if not p[i]:continue
  e=scale*p[i]/2;ck(e.denominator==1)
  direct*=((q[i]/rp[i])*(q[i]/rm[i]))**e.numerator;formula*=(1/(1-t[i]*t[i]))**e.numerator
 ck(direct==formula);ck(formula>1)
for row in d['zero_cost_boundary_cases']:
 g=F(row['g']);v=F(row['fraction']);q=(F(1,2)-g)/2;Q=[q,q,g,q,q,g];t=[F(0),F(0),v,F(0),F(0),-v]
 rp=[Q[i]*(1+t[i]) for i in range(6)];rm=[Q[i]*(1-t[i]) for i in range(6)];ck(sum(rp)==sum(rm)==1);ck(rp[0]==rm[0]==Q[0]);ck(rp[1]==rm[1]==Q[1]);ck(abs(g*v)<=g)
# Negative control: dropping exact within-block matching makes proportional allocation suboptimal.
Q=[F(3,8),F(1,8)]*2;plus=[F(9,16),F(3,16),F(3,16),F(1,16)];minus=[F(3,16),F(1,16),F(9,16),F(3,16)];eps=F(1,64)
cp=[plus[i]+eps*[1,-1,-1,1][i] for i in range(4)];cm=[minus[i]-eps*[1,-1,-1,1][i] for i in range(4)]
ck(sum(cp)==sum(cm)==1);ck(all((cp[i]+cm[i])/2==Q[i] for i in range(4)));ck([sum(cp[:2]),sum(cp[2:])]==[F(3,4),F(1,4)]);ck(prod([plus[i]/cp[i]*minus[i]/cm[i] for i in range(4)])<1)
# Actual Boolean parity and both full nonempty-profile references, independently reconstructed.
vals=[(-1)**x.bit_count() for x in range(16)];amp={s:F(sum(vals[x]*(-1)**((x&s).bit_count()) for x in range(16)),16) for s in range(16)}
for U in range(16):ck(sum(amp[S]*amp[S^U] for S in range(16))==int(U==0))
Qp={9:F(1,2),10:F(1,4),15:F(1,4)};qbar={S:Qp.get(S,0)+Qp.get(S|8,0) for S in range(8)};Rplus={1:F(5,8),2:F(1,8),7:F(1,4)};Rminus={1:F(3,8),2:F(3,8),7:F(1,4)}
ck(sum(Qp.values())==sum(Rplus.values())==sum(Rminus.values())==1)
for u in [0,1]:
 ac={S:amp[S]+(-1)**u*amp[S|8] for S in range(8)};ck(ac[7]==(-1)**u);ck(sum(v*v for v in ac.values())==1)
ck(all((Rplus.get(S,0)+Rminus.get(S,0))/2==qbar[S] for S in range(8)));ck(Qp[15]==Rplus[7]==Rminus[7]==F(1,4));ck(Qp.get(0,0)==Rplus.get(0,0)==Rminus.get(0,0)==0)
def walsh(vals):
 ar=list(vals);step=1
 while step<len(ar):
  for b in range(0,len(ar),2*step):
   for j in range(b,b+step):x,y=ar[j],ar[j+step];ar[j],ar[j+step]=x+y,x-y
  step*=2
 return [F(x,len(ar)) for x in ar]
wrappers=active=0
seedQ={9:F(1,2),10:F(1,4),15:F(1,4)};newSeed=[{1:F(5,8),2:F(1,8),7:F(1,4)},{1:F(3,8),2:F(3,8),7:F(1,4)}]
for controller in product([-1,0,1],repeat=4):
 aa=walsh(controller);bb=walsh([1-v*v for v in controller]);beta=F(sum(1-v*v for v in controller),4)
 for sigma in [-1,1]:
  vals=[controller[x>>4]+sigma*(1-controller[x>>4]**2)*(-1)**((x&15).bit_count()) for x in range(64)];ck(all(v in [-1,1] for v in vals));ar=walsh(vals)
  ref={S:(aa[S>>4]**2 if (S&15)==0 else bb[S>>4]**2*seedQ.get(S&15,F(0))) for S in range(64)};ck(sum(ref.values())==1);ck(sum(ar[S]**2 for S in range(64) if S&8)==beta)
  ps=[]
  for u in [0,1]:
   # Insert the fixed physical seed bit3 into the32-bit child truth-table index.
   words=[(x&7)|((x>>3)<<4)|(u<<3) for x in range(32)];ac=walsh([vals[x] for x in words]);pp={}
   nr={}
   for index,w in enumerate(words):
    S=w&~8;ck(ac[index]==ar[S]+(-1)**u*ar[S|8]);ck(ar[S]*ar[S|8]==0);pp[S]=ac[index]**2
    nr[S]=aa[S>>4]**2 if (S&15)==0 else bb[S>>4]**2*newSeed[u].get(S&15,F(0))
    inherited=ref[S]+ref[S|8]
    if pp[S]:ck(nr[S]==inherited and nr[S]>0)
   ck(sum(pp.values())==sum(nr.values())==1);ps.append(pp)
  ck(ps[0]==ps[1]);wrappers+=1;active+=int(beta>0)
ck(wrappers==162);ck(time.monotonic()-start<55)
out={'checks':checks,'seconds':time.monotonic()-start,'rational_dual_cases':len(d['positive_KKT_cases']),'zero_capacity_cases':len(d['zero_cost_boundary_cases']),'coherent_controllers':wrappers,'active_seed_queries':active,'matched_conditional_hypothesis_negative_control':'PASS: compatible nonproportional law strictly cheaper without that hypothesis','actual_parity_full_ghost_normalization':'PASS','proof_scope':'Generic sharp constrained reference optimization; actual Boolean free profile change for every coherent controller; no universal initial source'}
(R/'out/GHOST_REPRODUCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
