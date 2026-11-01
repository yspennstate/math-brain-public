from pathlib import Path
from fractions import Fraction as F
from itertools import combinations_with_replacement, islice
from math import comb
import json, time, argparse, hashlib
from rational import fw, log, add, interval

RUN=Path(__file__).resolve().parents[1]
checks=0
def ck(x):
 global checks
 checks+=1
 if not x: raise AssertionError(checks)
def push(h,key,N,K):
 n,k=h.get(key,(0,0));h[key]=(n+N,k+K)
def conv(A,B):
 H={}
 for (a,s),(N,K) in A.items():
  for (b,t),(M,L) in B.items():push(H,(a+b,s*t),N*M,K*M+L*N)
 return H
def parent(ch):
 H={}
 for c in ch:
  for (a,s),(N,K) in c['hist'].items():push(H,(a+1,s),N,K)
 for (a,s),(N,K) in conv(conv(ch[0]['hist'],ch[1]['hist']),ch[2]['hist']).items():push(H,(a+1,-s),N,K)
 val=1 if sum(c['value'] for c in ch)>0 else -1
 piv=sum(c['piv'] for i,c in enumerate(ch) if ch[(i+1)%3]['value']!=ch[(i+2)%3]['value'])
 return dict(hist=H,value=val,piv=piv,x=sum((c['x'] for c in ch),()))
def levels(pilot):
 lev=[[dict(hist={(0,s):(1,1)},value=s,piv=1,x=(s,)) for s in [1,-1]]]
 for d in range(1,4):
  prev=lev[-1]; triples=combinations_with_replacement(range(len(prev)),3)
  if pilot and d==3:triples=islice(triples,4)
  lev.append([parent([prev[i] for i in ix]) for ix in triples])
 return lev
def evalg(x):
 if len(x)==1:return x[0]
 m=len(x)//3
 return 1 if sum(evalg(x[i*m:(i+1)*m]) for i in range(3))>0 else -1
def truth(n):return [evalg(tuple(-1 if x>>i&1 else 1 for i in range(n))) for x in range(1<<n)]
def spectrum(v):return [F(a,len(v)) for a in fw(v)]
def ce(P,R):return add(*[(a,log(1/r)) for a,r in zip(P,R) if a])
def influence(A):return sum((S.bit_count()*a*a for S,a in enumerate(A)),F(0))
def point_bill(node,d):
 n=3**d;J=F(3,2)**d;delta=F(2,1<<n);H=node['hist']
 mass=energy=F(0);code={};support=degree=0;entropy=F(0)
 for (a,s),(N,K) in H.items():
  p=F(1,1<<(2*a));support+=N;degree+=K;entropy+=N*p*2*a
  q=(p+F(1,1<<n))/2;v=(s*node['value']*F(1,1<<a)-delta)**2
  mass+=N*v;energy+=K*v;code=add((1,code),(N*v,log(1/q)))
 zeros=(1<<n)-support;zero_degrees=n*(1<<(n-1))-degree
 mass+=zeros*delta*delta;energy+=zero_degrees*delta*delta
 code=add((1,code),(zeros*delta*delta*(n+1),{2:1}))
 ck(mass==1);ck(energy==J+delta*(n-2*node['piv']));ck(entropy==4*J-4)
 ck(sum(N*F(1,1<<(2*a)) for (a,s),(N,K) in H.items())==1)
 ck(sum(K*F(1,1<<(2*a)) for (a,s),(N,K) in H.items())==J)
 ck(sum(s*N*F(1,1<<a) for (a,s),(N,K) in H.items())==node['value'])
 lo,hi=interval(code);margin=(4*energy-hi,4*energy-lo)
 admitted=1024*n*J*F(1,1<<n)<=1
 if admitted:ck(margin[0]>=F(271,128))
 return code,energy,margin,admitted
def root_query(v,R,i):
 n=(len(v)).bit_length()-1;A=spectrum(v);P=[a*a for a in A]
 others=[j for j in range(n) if j!=i]
 def pack(t):return sum(((t>>j)&1)<<q for q,j in enumerate(others))
 Rp=[F(0)]*(1<<(n-1))
 for S,r in enumerate(R):Rp[pack(S)]+=r
 children=[]
 for bit in [0,1]:
  w=[]
  for t in range(1<<(n-1)):
   x=sum(((t>>q)&1)<<j for q,j in enumerate(others)) | (bit<<i)
   w.append(v[x])
  B=spectrum(w);children.append((B,ce([b*b for b in B],Rp)))
 ex=add((1,ce(P,R)),(-F(1,2),children[0][1]),(-F(1,2),children[1][1]))
 direct={}
 for S,a in enumerate(A):
  if a:direct=add((1,direct),(a*a,log(Rp[pack(S)]/R[S])))
 ck(ex==direct)
 ck(influence(A)==sum(a*a for S,a in enumerate(A) if S>>i&1)+sum(influence(b) for b,c in children)/2)
 # Every term in direct is nonnegative because the reference is marginalized.
 ck(all(Rp[pack(S)]>=R[S]>0 for S in range(1<<n)))
def main(pilot=False):
 start=time.perf_counter();lev=levels(pilot);rows=[];admitted=0;mins={};direct_tables={d:truth(3**d) for d in [1,2]}
 for d in [1,2,3]:
  n=3**d
  for idx,node in enumerate(lev[d]):
   ex,I,margin,ok=point_bill(node,d);admitted+=int(ok)
   if d not in mins or margin[0]<F(mins[d]['lower']):mins[d]=dict(lower=str(margin[0]),upper=str(margin[1]),orbit=idx,pivotal_at_edit=node['piv'])
   if d<=2:
    v=direct_tables[d];A=spectrum(v);x=sum((s==-1)<<j for j,s in enumerate(node['x']))
    H={}
    for S,a in enumerate(A):
     if a:
      ck(abs(a).numerator==1);q=abs(a).denominator;ck(q&(q-1)==0)
      sign=(1 if a>0 else -1)*(-1 if (S&x).bit_count()%2 else 1)
      push(H,(q.bit_length()-1,sign),1,S.bit_count())
    ck(H==node['hist']);ck(v[x]==node['value']);ck(sum(v[x]!=v[x^(1<<j)] for j in range(n))==node['piv'])
    w=v.copy();w[x]*=-1;B=spectrum(w);P=[b*b for b in B];R=[(a*a+F(1,1<<n))/2 for a in A]
    ck(sum(P)==1);ck(influence(B)==I);ck(ce(P,R)==ex)
  ck(len(lev[d])==([4,20,4 if pilot else 1540][d-1]))
 # Exhaust all actual 3-bit Boolean functions, including constants and every edit size.
 g=direct_tables[1];A=spectrum(g);R=[(a*a+F(1,8))/2 for a in A];J=F(3,2);B0=4*J-3;L=4
 for table in range(256):
  v=[-1 if table>>x&1 else 1 for x in range(8)];B=spectrum(v);rho=F(sum(a!=b for a,b in zip(v,g)),8)
  lo,hi=interval(ce([b*b for b in B],R));q=hi-B0-4*rho*L
  ck(q<=0 or q*q<=16*rho*B0*L)
  If=influence(B);q=If+J-4*3*rho
  ck(q<=0 or q*q<=4*If*J)
  for i in range(3):root_query(v,R,i)
 endpoints=[]
 for d in range(1,7):
  n=3**d;J=F(3,2)**d;bound=F(1<<n)/(1024*n*J);k=bound.numerator//bound.denominator
  ck(F(k,1<<n)*1024*n*J<=1);ck(F(k+1,1<<n)*1024*n*J>1)
  endpoints.append(dict(depth=d,n=n,I_clean=str(J),max_edits=k))
 ck(endpoints[2]['max_edits']==1438)
 ck(F(3)-F(28,32)-F(1,128)==F(271,128));ck(F(271,128)-2==F(15,128));ck(F(3,2)**2>2)
 elapsed=time.perf_counter()-start
 ck(elapsed<55)
 result=dict(status='PASS',checks=checks,elapsed_seconds=elapsed,point_orbits=[len(x) for x in lev],admitted_point_orbits=admitted,all_three_bit_functions=256,min_point_reserve=mins,radius_endpoints=endpoints,arithmetic='Integer/Fraction plus certified24-term atanh log intervals; zero floating sign decisions',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),full_fei='OPEN')
 (RUN/'out').mkdir(exist_ok=True);(RUN/'out'/('pilot.json' if pilot else 'results.json')).write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'))
 print(json.dumps({k:result[k] for k in ['status','checks','elapsed_seconds','point_orbits','admitted_point_orbits']}))

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args();main(args.pilot)
