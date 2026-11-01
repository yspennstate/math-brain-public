"""Separate scalar and sector reconstruction: no shared mathematical helpers."""
import json,time
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];start=time.monotonic();count=0
def ck(x,label):
 global count
 count+=1
 assert x,label
 if time.monotonic()-start>55:raise RuntimeError('55-second watchdog')
def log(q):
 shift=0
 while q<1:q*=2;shift-=1
 while q>=2:q/=2;shift+=1
 def ln(q):
  t=(q-1)/(q+1);lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
  return lo,lo+2*t**65/(65*(1-t*t))
 a,b=ln(q);c,d=ln(F(2));return shift+a/d,shift+b/c
def add(*v):return sum((x[0] for x in v),F(0)),sum((x[1] for x in v),F(0))
def mul(v,q):return (v[0]*q,v[1]*q) if q>=0 else (v[1]*q,v[0]*q)
def sub(a,b):return add(a,mul(b,-1))
def exact(q):return F(q),F(q)
def atom(q):return mul(log(q),-q) if q else exact(0)
def h(q):return add(atom(q),atom(1-q))
def readv(v):return tuple(F(x) for x in v)
def overlap(a,b):return a[0]<=b[1] and b[0]<=a[1]
H={};T={};S={}
for k in range(1,17):
 e=F(1,2**k);H[k]=add(atom((1-2*e)**2),mul(atom(4*e*e),2**k-1));T[k]=sub(mul(h(2*e),k),H[k]);S[k]=sub(exact(8*k*e),H[k])
 ck(T[k][1]<F(5,8),'independent reset sign certificate')
 if k>=3:
  E=add(mul(h(F(1,4)),2),mul(h(e/2),k),exact(-1-2*(k-1)*e))
  ck(E[1]<F(37,32),'independent cumulative envelope')
C=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'));P=C['physical'];last=add(exact(3),mul(S[5],F(1,4)));debits=[];bills=[]
ck(overlap(last,readv(P['S0'])),'initial complete sector surplus')
for j,row in enumerate(P['history']):
 k=5-j;bill=mul(T[k],F(1,2**(j+2)));cur=add(exact(3),mul(S[k-1],F(1,2**(j+3))))
 debit=sub(cur,last);ck(debit[0]>0,'independent positive physical query')
 ck(bill[0]>0,'independent positive third full reset')
 ck(overlap(bill,readv(row['full_reset_bill'])),'actual reset sector price')
 ck(overlap(cur,readv(row['complete_surplus'])),'actual full final frontier surplus')
 ck(overlap(debit,readv(row['new_U_retained'])),'actual disjoint positive query debit')
 bills.append(bill);debits.append(debit);last=cur
ck(overlap(readv(P['L0']),readv(P['A'])),'original source booking kept unchanged')
remaining=sub(last,add(readv(P['A']),*debits,*bills,exact(F(11,32))))
ck(remaining[0]>F(1,32),'independently reconstructed original-owner payment')
ck(overlap(remaining,readv(P['remaining'])),'remaining account readback')
ck(2-F(37,32)-3*F(5,32)-F(11,32)==F(1,32),'uniform final exact rational gap')
out={'status':'PASS','assertions':count,'runtime_seconds':time.monotonic()-start,'method':'independent32-term atanh, direct physical sector formulas, no shared helper imports; author validation NOT external review','third_reset_bill':[str(x) for x in bills[-1]],'remaining':[str(x) for x in remaining]}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({k:out[k] for k in ['status','assertions','runtime_seconds']}))
