"""Independent complete root/child entropy recurrence; no last-frequency packet."""
from pathlib import Path
from fractions import Fraction as Q
import json,time
import check as c

def chain(r,l,terminal_mean):
 p=Q(1,1<<r);b=1-p;N=(1<<r)-1;m=Q(terminal_mean);H=(0,0);I=Q(1) if terminal_mean==0 else Q(0)
 W=c.add(c.eta(b*b),c.times(c.eta(p*p),Q(N)))
 for k in range(l):
  a=Q((-1)**k);M=p*a+b*m
  H=c.add(c.times(H,b),c.eta(M*M),c.times(c.eta(p*p*(a-m)**2),Q(N)),c.neg(c.times(c.eta(m*m),b)),c.times(W,1-m*m))
  I=b*I+r*p*(1-a*m);m=M
 return H,I,m

start=time.perf_counter();rows=[]
for r,l in [(3,32),(4,128),(5,256)]:
 root,I,m=chain(r,l,0);left,_,_=chain(r,l,1);right,_,_=chain(r,l,-1);p=Q(1,1<<r);b=1-p;e=b**l
 D=c.times(c.add(root,c.neg(c.times(c.add(left,right),Q(1,2)))),1/e)
 source=c.compressed(r,l);c.check(not(D[1]<source['D'][0] or source['D'][1]<D[0]))
 expected=e+2*r*(1-e)/(2-p)-(r*p*p*b**(l-1)/(2-p) if l%2 else 0)
 c.check(I==expected)
 rows.append({'r':r,'l':l,'D_over_I_query':c.serial(D),'H_root':c.serial(root),'H_children':[c.serial(left),c.serial(right)],'I_total':str(I)})
elapsed=time.perf_counter()-start;c.check(elapsed<55)
result={'status':'PASS','seconds':elapsed,'checks':c.CHECKS,'rows':rows,'method':'full-disjoint-substitution entropy recurrence, independent of last-frequency division'}
(c.ROOT/'out/INDEPENDENT_RECURRENCE.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','seconds':elapsed,'checks':c.CHECKS,'ratios':[x['D_over_I_query']['display'] for x in rows]}))
