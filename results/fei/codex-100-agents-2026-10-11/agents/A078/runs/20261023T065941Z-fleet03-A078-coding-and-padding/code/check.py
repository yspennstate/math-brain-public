from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
from math import comb
import json,time,hashlib,sys
from exact import add,g,entropy,fwht,walsh,infl,restrict,xi,mean,scalar,nonneg,interval
R=Path(__file__).resolve().parents[1];O=R/'out';pilot='--pilot' in sys.argv
spec={'helper_version':'A078-prime-log-16 from stage025441Z','family':'actual Maj_d with two adjacent edited Boolean profiles; both initial shared answers, third nonseparator query; original guarded bent4/spike2 donor','domain':{'d':[5] if pilot else [5,7],'private_n':[0,1] if pilot else [0,1,2],'ancestor_r':list(range(3,18,2)) if pilot else list(range(3,130,2))},'case_count':{'profile_pairs_per_d':20 if pilot else 276,'third_query_states':80 if pilot else 2208,'history_count':0 if pilot else 8},'symmetry':'permute nonseparator coordinates to first1,second2,third3; all profile tables and four answer pairs retained; edits0,e0 fixed by every such permutation','arithmetic':'integer FWHT/Fraction squared spectra; exact prime-log identities with outward16-term atanh; symbolic binomial recurrence; no floating-point acceptance','memory_estimate_MB':150,'max_runtime_seconds':55 if pilot else 180,'automatic_dimension_escalation':False}
(O/('FROZEN_PILOT.json' if pilot else 'FROZEN_SPEC.json')).write_text(json.dumps(spec,indent=2),encoding='utf-8')
start=time.monotonic();checks=0
def ck(b):
 global checks
 checks+=1;assert b,checks
 assert time.monotonic()-start<spec['max_runtime_seconds']
def save(name,x):(O/name).write_text(json.dumps(x,indent=2),encoding='utf-8')
def je(x):return {str(p):str(v) for p,v in x.items()}
def D(a,b,c):return add((1,a),(-Q(1,2),b),(-Q(1,2),c))
def carrier(d):return tuple(1 if x.bit_count()<=d//2 else -1 for x in range(2**d))
def sc(h,ed,i,b):
 ee=tuple(((x&((1<<i)-1))|((x>>(i+1))<<i),t) for x,t in ed if (x>>i)&1==b)
 return restrict(h,i,b),ee
@lru_cache(maxsize=512)
def st(h,ed,v,w):
 r=len(h).bit_length()-1;p=Q(1,len(h));ee=dict(ed);vs=[v,w]
 f=tuple(vs[ee[s]][z] if s in ee else h[s] for z in range(len(v)) for s in range(len(h)))
 a=fwht(f);H=entropy(a);U=add(*[(p,entropy(fwht(vs[t]))) for s,t in ed]);rr=r*p*sum((1-mean(vs[t])**2 for s,t in ed),Q(0))
 X=xi(v,w,p) if len(ed)==2 else {}
 # COMPLETE empty-private sector, normalized as actual wrapper coefficients.
 ms=tuple(Q(sum(f[z*len(h)+s] for z in range(len(v))),len(v)) for s in range(len(h)))
 ma=fwht(ms)
 return f,a,H,U,rr,X,ma
def phi(a,b):return add((1,g(a)),(1,g(b)),(-1,g2sum(a*a+b*b)))
def g2sum(q):
 # g(sqrt(q)) requires no algebraic numbers: -q log2(q).
 from exact import logvec
 return {p:-q*c for p,c in logvec(q).items()} if q else {}
def erasure(a,i):
 return add(*[(1,add((1,g(a[t])),(1,g(a[t|(1<<i)])),(-1,g2sum(a[t]**2+a[t|(1<<i)]**2)))) for t in range(len(a)) if not (t>>i)&1])
algebra=[]
for r in spec['domain']['ancestor_r']:
 alpha=Q(comb(r+1,(r+1)//2),2**(r+1));A=[Q(0)]*(r+3)
 for l in range((r+1)//2+1):A[2*l+1]=(-1)**l*alpha*Q(comb((r+1)//2,l),comb(r+1,2*l))
 for k in range(1,r+1,2):ck(A[k+2]==-Q(k,r+1-k)*A[k])
 X=sum((comb(r-1,k)*A[k+1]**2 for k in range(0,r,2)),Q(0));Y=sum((comb(r-1,k)*A[k+3]**2 for k in range(0,r,2)),Q(0));Z=sum((comb(r-1,k)*A[k+2]**2 for k in range(1,r,2)),Q(0));P=sum((comb(r-1,k)*abs(A[k]*A[k+2]) for k in range(1,r,2)),Q(0))
 ck(X+Y+2*Z==alpha);ck(P<=X)
 beta=[2*A[k+1] if k%2==0 else A[k]+A[k+2] for k in range(r+1)]
 L=2*sum((comb(r-1,k)*abs(beta[k]*beta[k+1]) for k in range(r)),Q(0));q=Q(comb(r-1,(r+1)//2),2**(r-1))
 ck(L<=10*alpha);ck(q==alpha*Q(r-1,r));ck(10*alpha<=15*q)
 ck(Q(r*(r+1),(r+3)*(r-1))>=Q(1,2))
 # Avoid square roots: 8sqrt(p)+16p<=20q iff 64p<=(20q-16p)^2.
 p=Q(1,2**r);ck(20*q-16*p>=0);ck(64*p<=(20*q-16*p)**2)
 if r<=9:
  hh=tuple(1 if x.bit_count()<=(r+1)//2 else -1 for x in range(2**r));a=fwht(hh)
  ck(all(a[s]==beta[s.bit_count()] for s in range(2**r)));ck(infl(hh,1)==q)
 algebra.append({'r':r,'alpha':str(alpha),'X':str(X),'Y':str(Y),'Z':str(Z),'P':str(P),'L':str(L),'physical_q':str(q)})
save('ANCESTOR_ENERGY.json',algebra)
states=nonzero=private=0
for d in spec['domain']['d']:
 h0=carrier(d)
 for n in spec['domain']['private_n']:
  tables=[tuple(1-2*((mask>>x)&1) for x in range(2**n)) for mask in range(2**(2**n))]
  for v in tables:
   for w in tables:
    for b1,b2 in product([0,1],repeat=2):
     h,ed=sc(h0,((0,0),(1,1)),1,b1);h,ed=sc(h,ed,1,b2)
     f,a,H,U,rr,X,ma=st(h,ed,v,w);states+=1;r=d-2;p=Q(1,2**r)
     cc=[st(*sc(h,ed,1,b),v,w) for b in [0,1]];j=infl(f,1)
     ck(sum(z*z for z in a)==1)
     if states<=20:ck(a==walsh(f))
     Bm=erasure(ma,1);ck(nonneg(add((1,scalar(35*j)),(-1,Bm))))
     rel=rr-(cc[0][4]+cc[1][4])/2
     ck(rel==p*sum((1-mean([v,w][t])**2 for s,t in ed),Q(0)))
     ck(not D(U,cc[0][3],cc[1][3]))
     ck(nonneg(add((1,scalar(rel+38*j)),(-1,D(H,cc[0][2],cc[1][2])))))
     if ed:
      q=Q(comb(r-1,(r+1)//2),2**(r-1));ck(j==q+p*(2-mean(v)-mean(w)))
      nonzero+=int(mean(v)!=0 and mean(w)!=0)
      K=add((1,scalar(8*p)),(1,X));ks=[add((1,scalar(Q(8,len(sc(h,ed,1,b)[0])))),(1,cc[b][5])) if sc(h,ed,1,b)[1] else {} for b in [0,1]]
      ck(not D(K,*ks));ck(all(nonneg(k) for k in ks))
     for i in range(n):
      private+=1;c=[st(h,ed,restrict(v,i,b),restrict(w,i,b)) for b in [0,1]]
      relp=rr-(c[0][4]+c[1][4])/2;ji=infl(f,r+i)
      ck(nonneg(add((1,D(U,c[0][3],c[1][3])),(1,D(X,c[0][5],c[1][5])),(1,scalar(relp+12*ji)),(-1,D(H,c[0][2],c[1][2])))))
ck(states==spec['case_count']['third_query_states'])
history=[];ledger=[]
if not pilot:
 d=5;e=Q(1,32);S=11*e;oldfirst=4*e;D0=e;B=S-oldfirst-D0
 v=[];w=[]
 for x in range(128):
  z=x%16;y=1-2*((x>>6)&1);b=(-1)**((z&1)*((z>>1)&1)+((z>>2)&1)*((z>>3)&1))
  v.append(y*b);w.append(y*(1-2*(x%64==0)))
 v,w=tuple(v),tuple(w)
 orders=[['s1','y','s2','z0','s3','x2'],['y','s2','s3','x2','s1','z0'],['z0','s3','y','s1','x2','s2'],['s2','x2','s1','y','s3','z0']]
 for first in [0,1]:
  a,b=restrict(v,4,first),restrict(w,4,first);Xo=xi(a,b,e);C=add((1,scalar(B/e)),(-1/e,Xo))
  for pol,order in enumerate(orders):
   cost=[Q(0)]*4;leaves=[]
   def walk(h,ed,v,w,sl,pl,shared_count,depth,reach):
    f,ff,H,U,rr,X,ma=st(h,ed,v,w);p=Q(1,len(h));K=add((p,C),(1,X)) if ed else {};ck(nonneg(K))
    rec={'initial_x1':first,'policy':pol,'reach':str(reach),'depth':depth,'shared_count':shared_count,'shared_labels':sl,'private_labels':pl,'edits':ed,'means':[str(mean(v)),str(mean(w))],'H':je(H),'U':je(U),'R':str(rr),'K':je(K),'full_squared_spectrum':[str(z*z) for z in ff],'core_squared_spectra':[[str(z*z) for z in fwht(t)] for t in [v,w]]}
    if depth==len(order):
     rec['terminal']=True;ledger.append(rec);leaves.append((reach,H,U,rr,K));return
    label=order[depth];rec['terminal']=False;rec['query']=label;ledger.append(rec)
    if label in sl:
     i=sl.index(label);cost[shared_count+1]+=reach*infl(f,i)
     for t in [0,1]:walk(*sc(h,ed,i,t),v,w,sl[:i]+sl[i+1:],pl,shared_count+1,depth+1,reach/2)
    else:
     i=pl.index(label);cost[0]+=reach*infl(f,len(sl)+i)
     for t in [0,1]:walk(h,ed,restrict(v,i,t),restrict(w,i,t),sl,pl[:i]+pl[i+1:],shared_count,depth+1,reach/2)
   root=st(carrier(5),((0,0),(1,1)),a,b)
   walk(carrier(5),((0,0),(1,1)),a,b,['s0','s1','s2','s3','s4'],['z0','z1','z2','z3','x2','y'],0,0,Q(1))
   EH=add(*[(p,h) for p,h,u,r,k in leaves]);EU=add(*[(p,u) for p,h,u,r,k in leaves]);EK=add(*[(p,k) for p,h,u,r,k in leaves]);ER=sum((p*r for p,h,u,r,k in leaves),Q(0))
   paid=sum((c*k for c,k in zip(cost,[12,5,15,38])),Q(0))
   margin=add((1,root[3]),(-1,EU),(1,scalar(root[4]+B+paid-ER)),(-1,root[2]),(1,EH),(-1,EK))
   ck(nonneg(margin));ck(nonneg(add((1,EK),(-1,scalar(B-4*e)))))
   history.append({'initial_x1':first,'policy':pol,'order':order,'original_S':str(S),'old_first':str(oldfirst),'oldD0':str(D0),'B':str(B),'expected_K':je(EK),'minimum_expected_K':str(B-4*e),'expected_full_terminal_H':je(EH),'expected_core_U':je(EU),'expected_R':str(ER),'physical_query_costs':[str(c) for c in cost],'margin_interval':[str(t) for t in interval(margin)],'leaves':len(leaves)})
 save('MIXED_LEDGER.json',ledger);save('HISTORIES.json',history)
result={'status':'PASS','pilot':pilot,'exact_assertions':checks,'third_query_states':states,'private_queries':private,'active_both_nonzero_means':nonzero,'ancestor_energy_cases':len(algebra),'histories':len(history),'ledger_nodes':len(ledger),'runtime_seconds':time.monotonic()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
save('PILOT.json' if pilot else 'CHECK.json',result);print(json.dumps(result))
