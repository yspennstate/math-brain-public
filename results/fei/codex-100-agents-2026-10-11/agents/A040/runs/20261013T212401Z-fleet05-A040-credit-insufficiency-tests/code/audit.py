from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,math
ROOT=Path(__file__).resolve().parents[1]; START=time.monotonic(); ASSERTS=0
def ck(x):
 global ASSERTS
 assert x
 ASSERTS+=1
def add(*terms):
 out={}
 for mul,v in terms:
  for p,c in v.items():out[p]=out.get(p,F(0))+mul*c
 return {p:c for p,c in out.items() if c}
@lru_cache(None)
def factors(n):
 out={}; j=2
 while j*j<=n:
  while n%j==0:out[j]=out.get(j,0)+1;n//=j
  j=3 if j==2 else j+2
 if n>1:out[n]=out.get(n,0)+1
 return out
def logvec(x):
 x=F(x);return add((1,factors(x.numerator)),(-1,factors(x.denominator)))
def ev(x):return {} if not x else add((-x,logvec(x)))
def hv(x):return add((1,ev(x)),(1,ev(1-x)))
def entropy(ps):return add(*[(1,ev(x)) for x in ps if x])
@lru_cache(None)
def log_interval(x):
 x=F(x);shift=x.numerator.bit_length()-x.denominator.bit_length();x/=F(2)**shift
 if x<1:x*=2;shift-=1
 def ln(v):
  u=v-1
  if u<F(1,2**40):return u-u*u/2,u
  t=u/(v+1); n=24
  low=2*sum((t**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
  return low,low+2*t**(2*n+1)/((2*n+1)*(1-t*t))
 a,b=ln(x);c,d=ln(F(2));return a/d+shift,b/c+shift
def vi(v):
 low=high=F(0)
 for p,c in v.items():
  a,b=log_interval(F(p))
  if c>=0:low+=c*a;high+=c*b
  else:low+=c*b;high+=c*a
 return low,high
def approx(v):a,b=vi(v);return float((a+b)/2)
def serialize(v):return {str(p):str(c) for p,c in sorted(v.items())}
def interval_export(z):
 # Outward rounding for compact certificates, using exact rational decimal tokens.
 grid=10**30;lo,hi=z
 return {'lower':str(F((lo.numerator*grid)//lo.denominator,grid)),'upper':str(F(-((-hi.numerator*grid)//hi.denominator),grid))}
def wht(a):
 a=list(a);j=1
 while j<len(a):
  for start in range(0,len(a),2*j):
   for q in range(start,start+j):u,v=a[q],a[q+j];a[q],a[q+j]=u+v,u-v
  j*=2
 return a
def split(vals,i):
 lo=[];hi=[]
 for x in range(len(vals)):
  if not(x&(1<<i)):lo.append(vals[x]);hi.append(vals[x|(1<<i)])
 return tuple(lo),tuple(hi)
def physical_infs(vals):
 N=len(vals);n=N.bit_length()-1
 return [F(sum(vals[x]!=vals[x^(1<<i)] for x in range(N)),N) for i in range(n)]
def stats(vals):
 N=len(vals);n=N.bit_length()-1;W=wht(vals);P=[F(z*z,N*N) for z in W];ck(sum(P)==1)
 ds=[sum((P[s] for s in range(N) if s&(1<<i)),F(0)) for i in range(n)]
 ck(ds==physical_infs(vals));H=entropy(P);M=add(*[(1,hv(d)) for d in ds]);return P,ds,H,add((1,M),(-1,H))
def oddQ(vals):
 N=len(vals);n=N.bit_length()-1;count=0
 for i in range(n):
  for j in range(i):
   mask=(1<<i)|(1<<j)
   for x in range(N):
    if not(x&mask) and vals[x]*vals[x|(1<<i)]*vals[x|(1<<j)]*vals[x|mask]<0:count+=1
 return F(2*count,N)
def truth(k):
 vals=[]
 for v in range(2**(k+4)):
  x=v&((1<<k)-1);z=(v>>k)&7;y=(v>>(k+3))&1
  C=not(z&1) and (not(z&2) or not(z&4))
  bent=(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2))
  vals.append(1 if not C else (-1 if y and not x else bent))
 return tuple(vals)
def audit_tree(k):
 alpha=F(3,8);delta=F(1,2**k);a=1-F(1,2**(k//2))+delta;L=F(5,8)
 root=truth(k);rootP,rootds,rootH,rootTC=stats(root)
 nodes=[];leaves=[]; sums={q:{} for q in ['B','J','JS','Gamma']};D=F(0);Qall=Qbad=F(0)
 def recurse(vals,labels,weight,depth):
  nonlocal D,Qall,Qbad
  P,ds,H,TC=stats(vals)
  choose=next((j for j in [k+3,k,k+1,k+2] if j in labels and ds[labels.index(j)]>0),None)
  if len(set(vals))==1 or choose is None:
   active=len(set(vals))>1;leaves.append({'weight':weight,'H':H,'TC':TC,'I':sum(ds),'CE':F(k if active else 0),'active':active});return
  i=labels.index(choose);v0,v1=split(vals,i);labels2=labels[:i]+labels[i+1:]
  p0,d0,H0,TC0=stats(v0);p1,d1,H1,TC1=stats(v1)
  pair=[P[t]+P[t|(1<<i)] for t in range(len(P)) if not(t&(1<<i))]
  HP=entropy(pair);B=add((1,H),(-1,HP));J=add((1,hv(ds[i])),(-1,B))
  JS=add((1,HP),(-F(1,2),H0),(-F(1,2),H1))
  Gamma=add(*[(1,hv((d0[j]+d1[j])/2)) for j in range(len(d0))],* [(-F(1,2),hv(x)) for x in d0+d1])
  ck(add((1,TC),( -1,J),(1,JS),(-1,Gamma),(-F(1,2),TC0),(-F(1,2),TC1))=={})
  ck(sum(ds)==ds[i]+(sum(d0)+sum(d1))/2)
  prod=tuple(x*y for x,y in zip(v0,v1));Qnode=sum(physical_infs(prod))/2
  signv=add((1,B),(-4*ds[i],{2:F(1)}));bounds=vi(signv)
  if not signv:bad=False
  elif bounds[0]>0:bad=True
  elif bounds[1]<0:bad=False
  else:raise ArithmeticError('undecided strict K4 sign')
  ck(vi(J)[0]>=0 or not J)
  if depth>0:ck(not bad)
  for name,V in [('B',B),('J',J),('JS',JS),('Gamma',Gamma)]:sums[name]=add((1,sums[name]),(weight,V))
  D+=weight*ds[i];Qall+=weight*Qnode
  if bad:Qbad+=weight*Qnode
  nodes.append({'queried_original_coordinate':choose,'depth':depth,'weight':str(weight),'d':str(ds[i]),'Qnode':str(Qnode),'bad_K4':bad,'B_minus_4d_vector':serialize(signv),'B_minus_4d_interval':interval_export(bounds),'B':approx(B),'J_posterior':approx(J),'JS':approx(JS),'Gamma':approx(Gamma),'posterior_vector':serialize(J)})
  recurse(v0,labels2,weight/2,depth+1);recurse(v1,labels2,weight/2,depth+1)
 recurse(root,tuple(range(k+4)),F(1),0)
 Hleaf=add(*[(z['weight'],z['H']) for z in leaves]);TCleaf=add(*[(z['weight'],z['TC']) for z in leaves]);Ileaf=sum(z['weight']*z['I'] for z in leaves);CEleaf=sum(z['weight']*z['CE'] for z in leaves)
 ck(add((1,rootH),(-1,Hleaf),(-1,sums['B']),(-1,sums['JS']))=={})
 ck(add((1,sums['J']),(1,sums['Gamma']),(1,TCleaf),(-1,rootTC),(-1,sums['JS']))=={})
 ck(D==alpha*delta+a*L);ck(Ileaf==alpha*(F(k,2)+k*delta));ck(sum(rootds)==D+Ileaf)
 ck(CEleaf==alpha*k);ck(CEleaf<=2*Ileaf)
 ck(sum(z['weight'] for z in leaves if z['active'])==alpha)
 rootQ=alpha*delta*(k+F(5,3));ck(Qbad==rootQ);ck(nodes[0]['bad_K4'])
 # Exact face partition checked independently of the spectral TC/entropy ledger.
 def leaf_faces(vals,labels,weight):
  ds=physical_infs(vals)
  choose=next((j for j in [k+3,k,k+1,k+2] if j in labels and ds[labels.index(j)]>0),None)
  if len(set(vals))==1 or choose is None:return weight*oddQ(vals)
  i=labels.index(choose);v0,v1=split(vals,i);labs=labels[:i]+labels[i+1:]
  return leaf_faces(v0,labs,weight/2)+leaf_faces(v1,labs,weight/2)
 Qleaf=leaf_faces(root,tuple(range(k+4)),F(1));ck(oddQ(root)==Qall+Qleaf)
 result={'k':k,'n':k+4,'nodes':nodes,'root_I':str(sum(rootds)),'queried_I':str(D),'terminal_I':str(Ileaf),'terminal_CE':str(CEleaf),'terminal_H_vector':serialize(Hleaf),'terminal_KL_vector':serialize(add((CEleaf,{2:F(1)}),(-1,Hleaf))),'Q_bad':str(Qbad),'Q_bad_over_I':str(Qbad/sum(rootds)),'Q_all':str(Qall),'Q_leaf':str(Qleaf),'total_posteriors':{name:{'vector':serialize(V),'approx':approx(V)} for name,V in sums.items()},'root_H':approx(rootH),'terminal_H':approx(Hleaf),'terminal_CE_minus_H':approx(add((CEleaf,{2:F(1)}),(-1,Hleaf))),'root_B':nodes[0]['B'],'root_J':nodes[0]['J_posterior'],'root_J_over_B':nodes[0]['J_posterior']/nodes[0]['B'],'root_Q_over_J':float(rootQ)/nodes[0]['J_posterior'],'control_posteriors_positive':all(z['J_posterior']>0 for z in nodes[1:]),'ledger_equalities_exact':True}
 return result
def grouped(k):
 alpha=F(3,8);delta=F(1,2**k);s=F(1,2**(k//2));d=alpha*delta
 pos=(2**k+2**(k//2))//2-1;neg=(2**k-2**(k//2))//2
 classes=[(alpha*pos,(s-delta)**2+delta**2,delta**2),(alpha*neg,(-s-delta)**2+delta**2,delta**2),(alpha-alpha*alpha,(s-1-delta)**2+delta**2,delta**2),(F(1),(1+alpha*(s-1-delta))**2+delta**2*alpha*alpha,delta**2*alpha*alpha)]
 ck(sum(mult*q for mult,q,e in classes)==1);ck(sum(mult*e for mult,q,e in classes)==d)
 # Direct rational entropy avoids factoring the large grouped packet numerators.
 def ei(x):
  if not x:return F(0),F(0)
  lo,hi=log_interval(1/x);return x*lo,x*hi
 lo=hi=F(0)
 for mult,q,e in classes:
  v=e/q;el,eh=ei(v);fl,fh=ei(1-v);lo+=mult*q*(el+fl);hi+=mult*q*(eh+fh)
 el,eh=ei(d);fl,fh=ei(1-d);J=(el+fl-hi,eh+fh-lo)
 ck(lo>4*d);ck(J[0]>0);ck((hi-lo)/d<F(1,10**8))
 return {'k':k,'d':str(d),'B_over_d':float((lo+hi)/(2*d)),'J_over_d':float((J[0]+J[1])/(2*d)),'J_over_B':float((J[0]+J[1])/(lo+hi)),'Q_over_J':float(d*(k+F(5,3))*2/(J[0]+J[1])),'B_minus_4d_interval':interval_export((lo-4*d,hi-4*d)),'J_interval':interval_export(J),'relative_B_interval_width':float((hi-lo)/d)}
result={'physical_roots':[],'grouped':[]}
for k in [4,6,8,10]:
 result['physical_roots'].append(audit_tree(k));(ROOT/'out'/'RESULTS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
for k in [4,6,8,12,16,32,64]:
 result['grouped'].append(grouped(k));(ROOT/'out'/'RESULTS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
result['assertions']=ASSERTS;result['runtime_seconds']=time.monotonic()-START
(ROOT/'out'/'RESULTS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'assertions':ASSERTS,'runtime_seconds':result['runtime_seconds'],'physical_roots':len(result['physical_roots']),'grouped_roots':len(result['grouped'])}))
