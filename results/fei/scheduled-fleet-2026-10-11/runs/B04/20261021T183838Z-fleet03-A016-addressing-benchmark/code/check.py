from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import json, time, sys
R=Path(__file__).resolve().parents[1]
T=time.perf_counter(); COUNT=0; CACHE={}
def ck(x,why):
 global COUNT
 assert x,why
 COUNT+=1
 assert time.perf_counter()-T<60,'frozen 60 second runtime'
def walsh(a):
 a=list(a);h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def law(a):return [Q(x*x,len(a)**2) for x in walsh(a)]
def inf(p):return sum((i.bit_count()*v for i,v in enumerate(p)),Q(0))
def ln(q):
 z=(q-1)/(q+1);v=z;s=Q(0)
 for j in range(32):s+=2*v/(2*j+1);v*=z*z
 return s,s+2*v/(65*(1-z*z))
LN2=ln(Q(2))
def log(q):
 if q in CACHE:return CACHE[q]
 x=q;e=0
 while x<1:x*=2;e-=1
 while x>=2:x/=2;e+=1
 lo,hi=ln(x);D=1<<72
 CACHE[q]=(Q(((e+lo/LN2[1])*D).__floor__(),D),Q(((e+hi/LN2[0])*D).__ceil__(),D))
 return CACHE[q]
def ce(p,q):
 ck(sum(q)==1,'normalized complete reference')
 groups=defaultdict(Q)
 for x,y in zip(p,q):
  ck(not x or y>0,'finite cost support')
  if x:groups[y]-=x
 lo=hi=Q(0)
 for x,w in groups.items():
  a,b=log(x)
  if w<0:a,b=b,a
  lo+=w*a;hi+=w*b
 return lo,hi
def add(*xs):return sum((x[0] for x in xs),Q(0)),sum((x[1] for x in xs),Q(0))
def scale(x,w):return (w*x[0],w*x[1]) if w>=0 else (w*x[1],w*x[0])
def scalar(x):return x,x
def minus(a,b):return add(a,scale(b,-1))
def overlaps(a,b):return a[0]<=b[1] and b[0]<=a[1]
def restrict(a,i,b):
 return [a[(t&((1<<i)-1))|((t>>i)<<(i+1))|(b<<i)] for t in range(len(a)//2)]
def marginal(a,i):
 return [sum(a[(t&((1<<i)-1))|((t>>i)<<(i+1))|(b<<i)] for b in [0,1]) for t in range(len(a)//2)]
def full(h):
 N=len(h)
 return [1 if not(w&1) else h[(w>>1)%N]*([-1,1,1,1][(w>>1)//N]) for w in range(8*N)]
def fullref(q):return [(q[t%len(q)]/4+int(t==0))/4 for t in range(4*len(q)) for e in [0,1]]
def costs(p):
 cp=add(scalar(Q(5)),scale(log((9+p)*(1-p)),Q(-1,2)))
 cc=add(scalar(Q(5)),scale(log(9+p),Q(-5,8)),scale(log(1+p),Q(-3,8)))
 end=add(scale(cp,1-p),scale(cc,p))
 # Positive constant branch only; negative constant and parity branches are eligible.
 D=(max(Q(0),p*(cc[0]-3)/2),max(Q(0),p*(cc[1]-3)/2))
 return cp,cc,end,D
def conversion(p):
 mu=p/2;a=(1+mu)**2/(2*(1+mu*mu))
 kl=add(scale(log(2*a),a),scale(log(2*(1-a)),1-a))
 return scale(kl,(1+mu*mu)/2)
def nonflat(mask,k=5,rootcheck=False):
 B=[(mask>>i)&1 for i in range(8)];A=[B[v>>k] if not(v&((1<<k)-1)) else 0 for v in range(1<<(k+3))]
 p=Q(sum(A),len(A));pa=law(A);JA=4*inf(pa)
 ck(sum(pa)==p,'indicator Parseval')
 ck(JA==sum(A[v]!=A[v^(1<<i)] for v in range(len(A)) for i in range(k+3))/Q(len(A)),'indicator physical edges')
 child=[1 if A[w>>1] else (-1)**(w&1) for w in range(2*len(A))]
 P=law(child);qc=[(x+int(i==0))/2 for i,x in enumerate(P)];c=ce(P,qc);H=ce(P,P)
 ck(inf(P)==1-p+JA/2,'child influence')
 ck(H[1]-JA<1,'sufficient entropy bound')
 ck(c[1]-JA<2,'activation source-bank admission')
 cp,cc,end,D=costs(p);E=conversion(p)
 S=minus(scalar(2*inf(P)),scale(c,Q(1,2)))
 debit=add(minus(add(scale(c,Q(1,2)),scalar(Q(3))),end),E)
 rem=minus(minus(S,debit),D)
 ck(rem[0]>Q(5,128),'same original bank after all costs and positive terminal deficit')
 ck(E[1]<p*p if p else E==(0,0),'conversion bound including zero activation')
 ck(D[1]<Q(1,128),'positive terminal deficit retained')
 if rootcheck:
  h=[(-1)**(w&1) if A[w>>2] else (-1)**((w>>1)&1) for w in range(4*len(A))]
  ph=law(h);qh=[(x+int(i==1))/2 for i,x in enumerate(ph)]
  f=full(h);qr=fullref(qh);pf=law(f);cr=ce(pf,qr)
  ck(overlaps(cr,add(scale(c,Q(1,2)),scalar(Q(3)))),'independent root Walsh cost')
  ck(inf(pf)==Q(3,2)+JA/4,'root physical spectral influence')
  # Actual unequal-spectrum children after a nontrivial B coordinate.
  j=3+k
  q0=marginal(qr,1);f0=restrict(f,1,0);new=marginal(q0,j)
  ch=[restrict(f0,j,b) for b in [0,1]];pcs=[law(x) for x in ch]
  ck(marginal(law(f0),j)==[(x+y)/2 for x,y in zip(*pcs)],'proper unequal-spectrum erased law')
  avg=scale(add(ce(pcs[0],new),ce(pcs[1],new)),Q(1,2))
  charges=(Q(0),Q(0))
  for S,w in enumerate(law(f0)):
   if w:
    U=(S&((1<<j)-1))|((S>>(j+1))<<j)
    ck(new[U]>=q0[S]>0,'proper conditional support')
    charges=add(charges,scale(log(new[U]/q0[S]),w))
  ck(charges[0]>=0,'proper inherited node charge')
  ck(overlaps(minus(ce(law(f0),q0),avg),charges),'complete proper-query telescope')
 return {'mask':mask,'p':str(p),'indicator_influence':str(JA),'core_cost_minus_indicator_influence':[str(x-JA) for x in c],'remaining_bank_after_positive_deficit':[str(x) for x in rem],'root_Walsh_checked':rootcheck}
def review(k):
 d=Q(1,1<<k);h=[(-1)**(w&1) if (w>>2)==0 else (-1)**((w>>1)&1) for w in range(1<<(k+2))]
 ph=law(h);qh=[(x+int(i==1))/2 for i,x in enumerate(ph)];root=full(h);ref=fullref(qh);cr=ce(law(root),ref)
 ref=marginal(ref,1);last=None;maxdef=Q(0)
 for t in range(k+1):
  avg=(Q(0),Q(0));I=Q(0);positive=(Q(0),Q(0));negative=(Q(0),Q(0))
  for q in [0,1]:
   for active,w in [(True,Q(1,2*(1<<t))),(False,(1-Q(1,1<<t))/2)]:
    if not w:continue
    child=[(-1)**q if active and (y>>1)==0 else (-1)**(y&1) for y in range(1<<(k-t+1))]
    f=full(child);p=law(f);C=ce(p,ref);ii=inf(p);avg=add(avg,scale(C,w));I+=w*ii
    diff=minus(C,scalar(4*ii))
    if diff[0]>0:positive=add(positive,scale(diff,w))
    elif diff[1]<0:negative=add(negative,scale(diff,-w))
    else:ck(False,'undecided signed terminal')
  ck(I==Q(3,2)+(k-t-1)*d/2,'A020 exact all-prefix remaining influence')
  reserve=minus(scalar(4*I),avg)
  ck(reserve[0]>Q(5,4),'A020 all-prefix signed reserve')
  ck(overlaps(minus(negative,positive),reserve),'both signed terminal accounts')
  if last:ck(minus(last,avg)[0]>=0,'nonnegative cumulative query cost')
  last=avg;maxdef=max(maxdef,positive[1]);
  if t<k:ref=marginal(ref,2)
 cp,cc,end,D=costs(d);ck(overlaps(last,end),'A020 complete endpoint reconstruction')
 return {'k':k,'prefix_depths':k+1,'maximum_weighted_positive_deficit_upper':str(maxdef),'endpoint_interval':[str(x) for x in end]}
def main():
 pilot='--pilot' in sys.argv
 rows=[];reviewrows=[]
 for m in ([23] if pilot else range(256)):
  rows.append(nonflat(m,rootcheck=m in [0,1,3,7,23,105,127,255]))
  (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps({'status':'RUNNING','completed_cases':len(rows),'assertions':COUNT,'rows':rows}),encoding='utf-8')
 if not pilot:
  for k in [3,6,8]:reviewrows.append(review(k))
 result={'status':'PASS','activation_cases':len(rows),'review_cases':reviewrows,'assertions':COUNT,'runtime_seconds':time.perf_counter()-T,'rows':rows}
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ['rows','review_cases']}))
if __name__=='__main__':main()
