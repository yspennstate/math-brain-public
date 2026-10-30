from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
R=Path(__file__).resolve().parents[1]; start=time.monotonic(); mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'; checks=0
def ck(x):
 global checks
 checks+=1; assert x,checks; assert time.monotonic()-start<(55 if mode=='pilot' else 180)
def ln(x):
 z=(x-1)/(x+1); s=sum((2*z**(2*j+1)/(2*j+1) for j in range(28)),F(0))
 return s,s+2*z**57/(57*(1-z*z))
L2=ln(F(2))
@lru_cache(None)
def lg(x):
 k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 a,b=ln(x);return F(k)+a/L2[1],F(k)+b/L2[0]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,t):return (a[0]*t,a[1]*t) if t>=0 else (a[1]*t,a[0]*t)
def sub(a,b):return add(a,mul(b,-1))
def pt(a):return F(a),F(a)
def CE(p,q):
 r=pt(0)
 for a,b in zip(p,q):
  if a:r=add(r,mul(lg(1/b),a))
 return r
def out(a):return {'lo':str(a[0]),'hi':str(a[1]),'approx':float(sum(a)/2)}
def wal(v):
 a=v[:];h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def sp(v):return [F(a*a,len(v)**2) for a in wal(v)]
def rest(v,j,b):return [v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(v)//2)]
def marg(p,j):return [a+b for a,b in zip(rest(p,j,0),rest(p,j,1))]
def inf(v,j):return F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v))
def TI(v):return sum((inf(v,j) for j in range(len(v).bit_length()-1)),F(0))
def grouped(m):
 A=F(1,1<<m);d=A*A;u=1+d; n=4**(m-1);np=(n+2**(m-1))//2
 cells=[];T=F(0)
 for sigma,count in [(1,np),(-1,n-np)]:
  for w in [0,1]:
   for b in [0,1]:
    if w:q=2*d*d;p=4*d*d;row=4*d*d
    else:
     q=2*d*(u-2*A*sigma*(b==0));p=4*d*((1-A*sigma)**2 if b==0 else d);row=4*d*(u-A*sigma)
    cells.append((p,q,row,count));T+=count*p*(row/(2*q)-1)
 ck(sum(p*c for p,q,r,c in cells)==1);ck(sum(q*c for p,q,r,c in cells)==1)
 ck(T==2*d/u)
 L=pt(0)
 for p,q,r,c in cells:L=add(L,mul(lg(r/q),p*c))
 ck(L[1]<1+3*d/u)
 # Stage18 likelihood sufficiency supplies L0<=1 and exact physical costs.
 Ebound=sub(add(pt(F(1,2)),mul(L,F(1,4))),pt(3*(F(1,4)+d)))
 ck(Ebound[1]<-F(9,4)*d)
 return {'m':m,'partner_CE_drop':out(L),'exact_log_linear_expectation':str(T),'rate3_block_upper_using_L0_le_1':out(Ebound)}
def literal(m):
 A=F(1,1<<m);d=A*A; b=[(-1)**sum(((x>>(2*j))&3)==3 for j in range(m)) for x in range(1<<(2*m+1))]
 c=[v-2*(x==0) for x,v in enumerate(b)];qb=sp(b);q=sp(c);p=q
 v0,v1=rest(c,0,0),rest(c,0,1);p0,p1=sp(v0),sp(v1);q1=marg(q,0)
 v00,v01=rest(v0,0,0),rest(v0,0,1);p00,p01=sp(v00),sp(v01);q2=marg(q1,0)
 for v in [b,c,v0,v1,v00,v01]:ck(set(v)=={-1,1})
 for law in [qb,q,p0,p1,q1,p00,p01,q2]:ck(sum(law)==1)
 ck(all(x>0 for x in q+q1+q2));ck(inf(c,0)==F(1,2)+d);ck(inf(v0,0)==2*d)
 hc=CE(q,q);hb=CE(qb,qb);cp0=CE(p0,q1);cp1=CE(p1,q1);cp00=CE(p00,q2);cp01=CE(p01,q2)
 L0=sub(hc,mul(add(cp0,cp1),F(1,2)));L1=sub(cp0,mul(add(cp00,cp01),F(1,2)))
 ck(L0[1]<=1); E=pt(0)
 for C in [2,3]:
  e0=sub(L0,pt(C*inf(c,0)));e1=sub(L1,pt(C*inf(v0,0)))
  E=add(mul(e0,F(1,2)),mul(e1,F(1,4)))
  if C==3:ck(E[1]<-F(9,4)*d)
  else:ck(E[0]>0);E2=E
 # Direct complete frontier, not debit formula, is the second accounting lane.
 g=b+c;hg=CE(sp(g),sp(g));hbar=mul(add(hb,hc),F(1,2));D=sub(hg,hbar)
 IX=(TI(b)+TI(c))/2;S3=sub(pt(3*IX),hbar);r3=sub(S3,D)
 SF=mul(sub(pt(3*TI(b)),hb),F(1,2));HF=pt(0);KF=pt(0)
 for idx,(v,pv,qv,reach) in enumerate([(v1,p1,q1,F(1,4)),(v00,p00,q2,F(1,8)),(v01,p01,q2,F(1,8))]):
  cce=CE(pv,qv);hh=CE(pv,pv);kl=sub(cce,hh)
  SF=add(SF,mul(sub(pt(3*TI(v)),cce),reach));HF=add(HF,mul(hh,reach));KF=add(KF,mul(kl,reach))
  ck(kl[1]>=0)
  for pp,qq in zip(pv,qv):
   if pp:ck(pp<=2*qq if idx==0 else pp<=4*qq if idx==1 else pp*pp<2*qq*qq)
 diff=sub(SF,add(S3,E));ck(diff[0]<=0<=diff[1])
 residual=sub(SF,add(D,E));ck(residual[0]<=r3[1] and r3[0]<=residual[1]);ck(r3[0]>0)
 EH=add(E,KF);SH=add(SF,KF);resH=sub(SH,add(D,EH));ck(resH[0]<=r3[1] and r3[0]<=resH[1])
 ck(KF[1]<F(9,16));ck(EH[1]<F(9,16));ck(sub(r3,EH)[0]>m-F(9,16));ck(EH[0]>0)
 legacyEH=add(E2,KF);ck(legacyEH[1]<F(13,16));change=sub(E2,E);ck(change[0]<=F(1,4)+d<=change[1])
 # All log-linear partner ratios independently accumulated on literal labels.
 T=sum((p0[x]*(q2[x>>1]/(2*q1[x])-1) for x in range(len(p0))),F(0));ck(T==2*d/(1+d))
 return {'m':m,'L0':out(L0),'L1':out(L1),'rate3_original_reach_debit':out(E),'legacy_rate2_source_debit':out(E2),'legacy_rate2_entropy_debit':out(legacyEH),'original_reach_removed_influence':str(F(1,4)+d),'frontier_KL':out(KF),'actual_entropy_rate3_debit':out(EH),'original_rate3_residual':out(r3),'same_source_final_residual':out(residual)}
rows=[literal(m) for m in ([2] if mode=='pilot' else [2,3,4,5])]
groups=[grouped(m) for m in ([2] if mode=='pilot' else range(2,17))]
result={'status':'PASS','mode':mode,'checks':checks,'runtime_seconds':time.monotonic()-start,'literal':rows,'grouped':groups}
(R/'out').mkdir(exist_ok=True)
(R/'out'/('PILOT.json' if mode=='pilot' else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','mode':mode,'checks':checks,'runtime_seconds':result['runtime_seconds'],'literal_rows':len(rows),'grouped_rows':len(groups),'display':[{'m':r['m'],'E3':r['rate3_original_reach_debit']['approx'],'EH3':r['actual_entropy_rate3_debit']['approx']} for r in rows]}))
