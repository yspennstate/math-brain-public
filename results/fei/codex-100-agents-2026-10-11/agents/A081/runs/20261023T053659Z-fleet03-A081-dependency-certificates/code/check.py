from pathlib import Path
from fractions import Fraction as F
import json,sys,time,importlib.util
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
old=R.parents[0]/'20261023T004705Z-fleet03-A081-dependency-certificates/code/check_resets.py'
sp=importlib.util.spec_from_file_location('prior_scalar',old);prior=importlib.util.module_from_spec(sp);sp.loader.exec_module(prior)
C=0
def ck(v):
 global C
 C+=1
 if not v:raise AssertionError(C)
def spectrum(f):
 a=[F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(f)),len(f)) for s in range(len(f))]
 p=[v*v for v in a];ck(sum(p)==1);return a,p
def child(f,j,b):
 return [f[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(f)//2)]
def canonical(f,labels):
 j=labels.index(6);g=child(f,j,0);a,_=spectrum(g);e=F(1,len(g));W=2*e-sum(v!=0 for v in a)*e*e
 q=[e*e for _ in f]
 for x,v in enumerate(a):
  if v:q[(x&((1<<j)-1))|((x>>j)<<(j+1))]=(1-W)*v*v
 for x,v in enumerate(g):
  ix=(x&((1<<j)-1))|((x>>j)<<(j+1));ck(f[ix]==v);ck(f[ix+(1<<j)]==v*(-1 if x==0 else 1))
 ck(sum(q)==1);return q
def split(f,q,labels,label):
 j=labels.index(label);kids=[child(f,j,b) for b in (0,1)];p=spectrum(f)[1];pp=[spectrum(k)[1] for k in kids];raw=[[],[]]
 for x in range(len(f)//2):
  ix=(x&((1<<j)-1))|((x>>j)<<(j+1));mass=p[ix]+p[ix+(1<<j)];ref=q[ix]+q[ix+(1<<j)]
  ck(mass==(pp[0][x]+pp[1][x])/2)
  for b in (0,1):raw[b].append(ref*pp[b][x]/mass if mass else ref)
 Z=[sum(row) for row in raw];ck(sum(Z)==2);ck(min(Z)>0)
 return kids,[[v/Z[b] for v in raw[b]] for b in (0,1)],labels[:j]+labels[j+1:],Z
def ce(f,q):return prior.expr(spectrum(f)[1],q)
def add(*args):return prior.add(*args)
def bounds(e):return prior.interval(e)
def main():
 start=time.perf_counter()
 g=[(1-2*int((x&15)==0))*(1-2*int((x&48)==0)) for x in range(64)]
 f=g+[(-v if x==0 else v) for x,v in enumerate(g)];labels=list(range(7));q=canonical(f,labels)
 root=ce(f,q);I=F(sum(sum(f[x]!=f[x^(1<<j)] for x in range(128)) for j in range(7)),128)
 ck(I==F(91,64));bank=4*I-bounds(root)[1];ck(bank>F(451,256))
 releases={};terminals={};charges=[];normalizers=[]
 reach=F(1)
 for label in [4,5,0]:
  before=ce(f,q);kids,old,ll,Z=split(f,q,labels,label);normalizers.append([str(z) for z in Z])
  rel=add((before,1),(ce(kids[0],old[0]),F(-1,2)),(ce(kids[1],old[1]),F(-1,2)))
  ck(bounds(rel)[0]>=0)
  releases=add((releases,1),(rel,reach));terminals=add((terminals,1),(ce(kids[1],old[1]),reach/2))
  fresh=canonical(kids[0],ll);e=add((ce(kids[0],fresh),reach/2),(ce(kids[0],old[0]),-reach/2));charges.append(e)
  if label==0:
   ck(Z[0]==F(529,452));p=spectrum(kids[0])[1]
   classes={}
   for triple in zip(p,old[0],fresh):classes[triple]=classes.get(triple,0)+1
   ck(classes=={(F(49,64),F(18375,33856),F(63,128)):1,(F(1,64),F(1695,33856),F(7,128)):7,(F(1,64),F(113,8464),F(1,64)):8})
  f,q,labels,reach=kids[0],fresh,ll,reach/2
 terminals=add((terminals,1),(ce(f,q),reach))
 ledger=add((releases,1),(terminals,1));expected=add((root,1),*((e,1) for e in charges));ck(ledger==expected)
 N=12250**49*3390**7*452**8;D=11109**49*3703**7*529**8
 ck(N>16*D);ck(N*N<512*D*D)
 ck(bounds(charges[2])[0]>F(1,128));ck(bounds(charges[2])[1]<F(9,1024))
 ck(bounds(charges[0])[1]<F(5,4));ck(bounds(charges[1])[1]<F(1,2))
 coarse=F(451,256)-F(5,4)-F(1,2)-F(9,1024);ck(coarse==F(3,1024))
 actual=bank-sum(max(F(0),bounds(e)[1]) for e in charges);ck(actual>coarse)
 ck(actual>2);ck(4*I-bounds(ledger)[1]>coarse);ck(time.perf_counter()-start<55)
 out={'status':'PASS','cases':1,'assertions':C,'prior_expr_assertions_not_added':prior.COUNT,'seconds':time.perf_counter()-start,'physical_influence':str(I),'third_normalizers':normalizers[-1],'third_N':str(N),'third_D':str(D),'third_charge_interval':[str(v) for v in bounds(charges[2])],'all_three_charge_intervals':[[str(v) for v in bounds(e)] for e in charges],'conservative_actual_reserve_lower':str(actual),'coarse_reserve_strictly_greater_than':str(coarse),'complete_ledger_exact_expression_identity':True,'FEI':'OPEN'}
 (R/'out/EXACT_CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
