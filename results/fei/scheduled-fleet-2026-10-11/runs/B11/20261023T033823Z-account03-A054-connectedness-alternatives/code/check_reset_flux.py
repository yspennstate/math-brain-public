import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time
R=Path(__file__).resolve().parents[1];A=R.parents[1]
old=A/'runs/20261014T055856Z-account05-A054-connectedness-alternatives/code/mathcore.py'
sp=importlib.util.spec_from_file_location('core',old);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
add=m.add;lv=m.logv
count=0;blocks=0;transforms=0;paid=0;t=time.perf_counter();positive=[]
def ct(x):return {2:F(x)} if x else {}
def ck(v):
 global count
 assert v;count+=1
 if time.perf_counter()-t>55:raise RuntimeError('frozen runtime exceeded')
def eq(x,y):ck(not add((x,1),(y,-1)))
def nn(v):ck(m.ge(v))
def flux(cs,n,i):
 N=1<<n;labels={x:k for k,c in enumerate(cs) for x,z in enumerate(c) if z}
 return F(sum(x^(1<<i) in labels and labels[x]!=labels[x^(1<<i)] for x in labels),N)
def test(n,g,i,j,fixture=False):
 global transforms,blocks,paid
 N=1<<n;p=F(sum(g),N)
 if not p:return
 cs=m.components(g);T=lambda x:x^(((x>>j)&1)<<i)
 h=tuple(g[T(x)] for x in range(N));ds=[tuple(c[T(x)] for x in range(N)) for c in cs]
 Iold=4*m.edges(g,N-1);Inew=4*m.edges(h,N-1);rho=Iold-Inew
 oldlabel=sum((4*m.edges(c,N-1) for c in cs),F(0));newlabel=sum((4*m.edges(c,N-1) for c in ds),F(0))
 gam=[flux(ds,n,z) for z in range(n)];inf=[4*m.edges(h,1<<z) for z in range(n)];ga=sum(gam,F(0));rhoL=oldlabel-newlabel
 ck(oldlabel==Iold);ck(newlabel==Inew+2*ga);ck(rhoL==rho-2*ga)
 ck(m.spec(tuple(1-2*z for z in g)).count(F(0))==m.spec(tuple(1-2*z for z in h)).count(F(0)))
 transforms+=1
 for mask in range(1,N-1):
  r=mask.bit_count();W={}
  for c in ds:
   fibers={}
   for x,z in enumerate(c):
    if z:fibers[x&~mask]=fibers.get(x&~mask,0)+1
   for num in fibers.values():W=add((W,1),(lv(F(1<<r,num)),F(num,N)))
  q=sum((inf[z] for z in range(n) if mask>>z&1),F(0));gc=sum((gam[z] for z in range(n) if mask>>z&1),F(0))
  nn(add((ct(q+2*gc),1),(W,-2)))
  nn(add((ct(r*max(inf)+2*gc),1),(W,-2)))
  if r==1:eq(W,ct(q/2+gc))
  if rho>=0 and rhoL>=0:
   for u in {F(0),rhoL/2}:
    rem=rho-u;ck(2*gc<=rem)
    # This tests the funding algebra only when the true fiber criterion holds.
    if m.ge(add((W,1),(ct(r*p/2),-1))):
     ck(r*p<=q+2*gc);ck(4*r*p<=4*q+4*rem)
     L=m.ledger(tuple(1-2*z for z in h),mask)[0]
     nn(add((ct(F(37,4)*(q+rem)),1),(L,-1)));paid+=1
     if gc>0 and L and len(positive)<3:positive.append({'n':n,'root_mask':str(sum(z<<x for x,z in enumerate(g))),'shear':[i,j],'query':mask,'rho':str(rho),'rho_L':str(rhoL),'old_debit':str(u),'gamma':str(gc),'L':m.vec(L)})
  blocks+=1
 if fixture:
  Wc=ct(inf[2]/2+gam[2])
  return {'n':n,'p':str(p),'I':str(Iold),'rho':str(rho),'rho_L':str(rhoL),'gamma_c':str(gam[2]),'gamma_all':str(ga),'Inf_c':str(inf[2]),'W_c':m.vec(Wc),'components':[sum(c) for c in cs]}
pilot='--pilot' in sys.argv
for n in range(1,3 if pilot else 4):
 for mask in range(1<<(1<<n)):
  g=tuple((mask>>x)&1 for x in range(1<<n))
  for i in range(n):
   for j in range(n):
    if i!=j:test(n,g,i,j)
records=[]
for k in [0,2,3,4]:
 n=4+k;N=1<<n;q=F(1,1<<k)
 g=tuple(int((x>>4)==0 and (((x&1)*((x>>1)&1)+((x>>2)&1)*((x>>3)&1))%2==0)) for x in range(N))
 v=test(n,g,0,2,True);records.append(v)
 ck(F(v['p'])==5*q/8);ck(F(v['rho'])==0);ck(F(v['gamma_c'])==q/8);ck(F(v['gamma_all'])==q/8);ck(F(v['rho_L'])==-q/4)
 ck(F(v['Inf_c'])==q/2);eq({int(z):F(c) for z,c in v['W_c'].items()},ct(3*q/8))
 ck(3*q/8>5*q/16);ck(q/2<5*q/8);ck(F(v['I'])==(2+F(5*k,4))*q)
# Boundary guard: a parity-to-literal shear creates flux using all release.
ck(F(1)==2*F(1,2));ck(2*F(1,2)>F(1)-F(1,2))
out={'status':'PASS','pilot':pilot,'assertions':count,'transforms':transforms,'block_cases':blocks,'paid_actual_terminal_cases':paid,'seconds':time.perf_counter()-t,'fixtures':records,'positive_crossing_payment_cases':positive,'old_debit_guard':'rho=1,gamma=1/2,u=1/2 leaves insufficient R=1/2'}
(R/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='fixtures'}))
