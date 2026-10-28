from exact import *
from pathlib import Path
import argparse,time,math
R=Path(__file__).resolve().parents[1];ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args();start=time.perf_counter();checks=0
def ck(b):
 global checks
 assert b
 checks+=1
def activated(H,p,k):
 a=Q(1,1<<k);m=1-2*p
 return add(scale(a,sub(H,ell(m*m))), (2*a*k*(1-m*m),)*2,
            ell((1-2*a*p)**2),scale((1<<k)-1,ell(4*a*a*p*p)))
def bound(H,I,p,k):
 a=Q(1,1<<k);hf=activated(H,p,k);IF=a*(I+2*k*p);control=2*a*k*p
 upper=a*H[0]+(4+Q(5,k))*control
 ck(hf[1]<=upper)
 # The substantive uniform remainder is proportional to p, not O(1).
 ck(hf[1]/a<=H[0]+8*k*p+10*p)
 if k>=2:
  gap=sub((IF,IF),h2(a*p));ck(gap[0]>=Q(2*k-3,4*k)*IF)
 v=4*a*p*(1-a*p);cn=sub(hf,h2(v));ck(cn[1]<=hf[1])
 return hf,IF
records=[]
n=2 if args.pilot else 3
for mask in range(1,(1<<(1<<n))-1):
 tab=[-1 if mask>>i&1 else 1 for i in range(1<<n)]
 w=walsh(tab);p=Q(tab.count(-1),len(tab));ps=[x*x for x in w];H=ent_counts(Counter(ps));I=sum(i.bit_count()*ps[i] for i in range(len(ps)))
 for k in ([1,4] if args.pilot else [1,2,4,8]):
  a=Q(1,1<<k);ft=[tab[x&((1<<n)-1)] if x>>n==0 else 1 for x in range(1<<(n+k))]
  fw=walsh(ft);fp=[x*x for x in fw];pred=[]
  for T in range(1<<k):
   for S in range(1<<n):pred.append((1-2*a*p)**2 if T==S==0 else 4*a*a*p*p if S==0 else a*a*ps[S])
  ck(fp==pred);ck(sum(fp)==1)
  hf,IF=bound(H,I,p,k);ck(overlap(hf,ent_counts(Counter(fp))))
  ck(IF==sum(s.bit_count()*fp[s] for s in range(len(fp))))
  for j in range(n+k):
   e=Q(sum(ft[x]!=ft[x^(1<<j)] for x in range(len(ft))),len(ft))
   ck(e==sum(fp[s] for s in range(len(fp)) if s>>j&1))
  records.append({'mask':mask,'n':n,'k':k,'p':p,'I_seed':I,'H_seed':H,'I':IF,'H':hf})
dump(R/'out'/('PILOT_BOOLEAN_CASES.json' if args.pilot else 'BOOLEAN_CASES.json'),records)
closed=[]
for n in ([4] if args.pilot else [1,2,4,8,16,32,128]):
 delta=Q(1,1<<n);mass=4*delta*delta;m0=1-2*delta
 Hseed=add(ell(m0*m0),scale((1<<n)-1,ell(mass)));Iseed=2*n*delta
 for sign in [-1,1]:
  for t in ([1] if args.pilot else [1,2,4]):
   m=(sign*m0)**t;p=(1-m)/2;HG=scale(t,Hseed);IG=t*Iseed
   # Exact grouped tensor multiplicities: each occupied copy contributes one nonempty atom.
   cs=Counter()
   for j in range(t+1):cs[(m0*m0)**(t-j)*mass**j]+=math.comb(t,j)*((1<<n)-1)**j
   ck(sum(x*c for x,c in cs.items())==1);ck(overlap(HG,ent_counts(cs)))
   for k in ([4] if args.pilot else [1,4,16]):
    hf,IF=bound(HG,IG,p,k);closed.append({'n':n,'sign':sign,'t':t,'k':k,'p_tensor':p,'I_seed':Iseed,'I_tensor':IG,'H':hf,'I':IF})
dump(R/'out'/('PILOT_CLOSED_CASES.json' if args.pilot else 'CLOSED_CASES.json'),closed)
# A sign check that should fail if one mistakes the asymptotic constant4 for a finite charge.
p=Q(1,2);k=2;a=Q(1,4);hf=activated((Q(0),Q(0)),p,k)
ck(hf[0]>4*(2*a*k*p))
ck(time.perf_counter()-start<55)
out={'verdict':'PASS','actual_boolean_fixtures':len(records),'closed_actual_tensor_fixtures':len(closed),'assertions':checks,'seconds':time.perf_counter()-start,'memory_estimate_mb':120,'negative_control':'PASS: charging selector influence at exactly4 fails at dictator k2; finite5/k correction retained'}
dump(R/'out'/('ACTIVATION_PILOT.json' if args.pilot else 'ACTIVATION_VALIDATION.json'),out);print(json.dumps(out))
