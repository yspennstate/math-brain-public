from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,time,sys,itertools
ROOT=Path(__file__).resolve().parents[1]
checks=0
def ok(b,msg=''):
 global checks
 checks+=1
 if not b:raise AssertionError(msg)
@lru_cache(None)
def factors(n):
 d=2;out={}
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def add(a,b,w=Q(1)):
 c=dict(a)
 for p,x in b.items():
  c[p]=c.get(p,Q(0))+w*x
  if not c[p]:del c[p]
 return c
@lru_cache(None)
def cost_cached(p):
 if not p:return ()
 c={}
 for x,k in factors(p.denominator).items():c[x]=p*k
 for x,k in factors(p.numerator).items():c[x]=c.get(x,Q(0))-p*k
 return tuple(sorted((x,w) for x,w in c.items() if w))
def cost(p):return dict(cost_cached(Q(p)))
def entropy(a):
 c={}
 for x in a:c=add(c,cost(x*x))
 return c
def phi(a,b):return add(add(cost(a),cost(b)),cost(a+b),-1)
def paird(a,b):
 return add(add(cost(a*a),cost(b*b)),add(cost((a+b)**2),cost((a-b)**2)),-Q(1,2))
@lru_cache(None)
def ln(q):
 q=Q(q);shift=0
 while q<1:q*=2;shift-=1
 while q>2:q/=2;shift+=1
 u=(q-1)/(q+1);v=Q(0)
 for j in range(32):v+=2*u**(2*j+1)/Q(2*j+1)
 tail=2*u**65/(65*(1-u*u))
 if shift:
  l,h=ln(Q(2));return v+shift*(l if shift>0 else h),v+tail+shift*(h if shift>0 else l)
 return v,v+tail
@lru_cache(None)
def bounds_cached(c):
 l=h=Q(0)
 for p,w in c:
  a,b=ln(Q(p));l+=w*(a if w>=0 else b);h+=w*(b if w>=0 else a)
 return l,h
def bounds(c):return bounds_cached(tuple(sorted(c.items())))
def le(a,b={},msg=''):
 dif=add(a,b,-1)
 ok(not dif or bounds(dif)[1]<=0,msg)
def rational_const(x):
 # x is a quantity in natural units; ln2 is not introduced.
 return Q(x)
def leconst(a,c,msg=''):ok(bounds(a)[1]<=c if a else 0<=c,msg)
def minimum(a,b):
 if a==b:return a
 l,h=bounds(add(a,b,-1))
 if h<=0:return a
 if l>=0:return b
 raise AssertionError('insufficient precision to order cap')
@lru_cache(None)
def walsh(t):
 a=list(t);k=1
 while k<len(a):
  for j in range(0,len(a),2*k):
   for i in range(k):u,v=a[j+i],a[j+i+k];a[j+i],a[j+i+k]=u+v,u-v
  k*=2
 return tuple(Q(x,len(a)) for x in a)
def influence(a,i=None):
 return sum(x*x*(s.bit_count() if i is None else ((s>>i)&1)) for s,x in enumerate(a))
def slice_table(t,i,b):
 return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))
@lru_cache(None)
def state(c,u,v):
 nz=(len(c)).bit_length()-1;nu=len(u).bit_length()-1;nv=len(v).bit_length()-1
 full=tuple(1 if c[z]==0 else u[y] if c[z]==1 else v[x]
   for x in range(len(v)) for y in range(len(u)) for z in range(len(c)))
 a=walsh(full);h=entropy(a);U={};R={};qs=[];vs=[]
 for j,tab in enumerate((u,v),1):
  q=Q(c.count(j),len(c));mean=Q(sum(tab),len(tab));var=1-mean*mean
  U=add(U,add(entropy(walsh(tab)),cost(mean*mean),-1),q)
  R=add(R,cost(q),var);qs.append(q);vs.append(var)
 return {'H':h,'U':U,'R':R,'a':a,'I':influence(a),'q':qs,'V':vs,'n':(nz,nu,nv)}
def aux(c,other,m,j):
 aa=[];cc=[]
 for y in range(len(other)):
  for label in c:
   aa.append(m if label==j else Q(1) if label==0 else Q(other[y]));cc.append(int(label==j))
 return walsh(tuple(aa)),walsh(tuple(cc))
def node_check(c,u,v,group,index):
 s=state(c,u,v);parts=[c,u,v];ch=[]
 for b in [0,1]:
  pp=parts.copy();pp[group]=slice_table(pp[group],index,b);ch.append(state(*pp))
 dH=add(s['H'],add(ch[0]['H'],ch[1]['H']),-Q(1,2))
 dU=add(s['U'],add(ch[0]['U'],ch[1]['U']),-Q(1,2))
 dR=add(s['R'],add(ch[0]['R'],ch[1]['R']),-Q(1,2))
 physical_index=sum(s['n'][:group])+index
 inf=influence(s['a'],physical_index)
 ok(s['I']==inf+(ch[0]['I']+ch[1]['I'])/2,'influence conservation')
 if group==0:
  ok(dU=={},'controller U martingale');le({},dR,'reserve reset sign')
  kl={}
  for j in [1,2]:
   q=s['q'][j-1]
   if not q:continue
   prob=ch[0]['q'][j-1]/(2*q)
   divergence=add(add({},cost(Q(1,2)),2),add(cost(prob),cost(1-prob)),-1)
   kl=add(kl,divergence,q*s['V'][j-1])
  ok(dR==kl,'exact physical conditional KL release')
  return dH,dR,{},Q(0),Q(0)
 j=group;tab=parts[group];oth=v if group==1 else u
 core=walsh(tab);m=core[0];beta=core[1<<index];t=beta*beta;var=1-m*m;q=s['q'][group-1]
 ok(inf==q*influence(core,index),'physical data weighting')
 ok(dR==add({},cost(q),t),'exact data R loss')
 aa,cc=aux(c,oth,m,j);M={};MV={};N={}
 for a,b in zip(aa,cc):
  M=add(M,phi(a*a,t*b*b));MV=add(MV,phi(a*a,var*b*b))
  N=add(N,add(paird(a,beta*b),phi(a*a,t*b*b),-1))
 ok(dH==add(add(dU,M),add(N,cost(t),-q)),'exact signed cancellation')
 le({},N,'N nonnegative');leconst(N,2*q*t,'N Hellinger bound')
 leconst(add(add(dH,dU,-1),dR,-1),3*q*t,'full data drift')
 if t and var:
  # qt ln(V/t) represented by eta(t/V) scaled by qV.
  second=add(add({},MV,t/var),cost(t/var),q*var)
  cap=minimum(MV,second);le(M,cap,'cap envelope')
 else:cap={};ok(M=={},'zero cap endpoint')
 leconst(add(cap,dR,-1),2*inf,'positive cap weaker certified constant')
 return dH,dR,cap,q*t,inf
def tree(c,u,v,policy):
 sizes=state(c,u,v)['n'];ids=tuple((g,i) for g,n in enumerate(sizes) for i in range(n))
 if policy==0:order=ids
 elif policy==1:order=tuple(x for x in ids if x[0])+tuple(x for x in ids if not x[0])
 else:order=tuple(sorted(ids,key=lambda x:(x[1],x[0])))
 root=state(c,u,v); maxdepth=len(ids)
 ctrlI=sum(influence(root['a'],i) for i in range(sizes[0]))
 le(root['R'],add({},cost(Q(1,2)),4*ctrlI),'initial exclusive-control reserve funding')
 totals=[{'H':{},'U':{},'R':{},'I':Q(0),'cap':{},'reset':{},'loss':{},'controller':{},'T':Q(0),'P':Q(0),'spent':Q(0)} for _ in range(maxdepth+1)]
 def visit(c,u,v,remaining,depth,weight,bankcap,reset,loss,ctr,T,P,spent):
  s=state(c,u,v);z=totals[depth]
  for name in ['H','U','R']:z[name]=add(z[name],s[name],weight)
  z['I']+=weight*s['I'];z['cap']=add(z['cap'],bankcap,weight);z['reset']=add(z['reset'],reset,weight)
  z['loss']=add(z['loss'],loss,weight);z['controller']=add(z['controller'],ctr,weight);z['T']+=weight*T;z['P']+=weight*P;z['spent']+=weight*spent
  if not any(remaining):return
  if policy==3:
   # Adaptive actual maximum influence; sign-dependent tie ordering.
   active=[(g,i) for g in range(3) for i in range(len(remaining[g]))]
   shift=[0,s['n'][0],s['n'][0]+s['n'][1]]
   g,i=max(active,key=lambda x:(influence(s['a'],shift[x[0]]+x[1]),(1 if s['a'][0]>=0 else -1)*(x[0]*4+x[1])))
  else:
   target=next(x for x in order if x[1] in remaining[x[0]])
   g=target[0];i=remaining[g].index(target[1])
  D,kappa,cap,t,p=node_check(c,u,v,g,i)
  rr=list(remaining);rr[g]=rr[g][:i]+rr[g][i+1:];rr=tuple(rr)
  for b in [0,1]:
   pp=[c,u,v];pp[g]=slice_table(pp[g],i,b)
   physical_index=sum(s['n'][:g])+i
   currentinf=influence(s['a'],physical_index)
   visit(*pp,rr,depth+1,weight/2,add(bankcap,cap),add(reset,kappa if g==0 else {}),add(loss,kappa if g!=0 else {}),add(ctr,add(D,kappa,-1) if g==0 else {}),T+t,P+p,spent+currentinf)
 # remaining is a tuple of original IDs; termination tests total length.
 visit(c,u,v,tuple(tuple(range(n)) for n in sizes),0,Q(1),{},{},{},{},Q(0),Q(0),Q(0))
 for z in totals:
  ok(add(add(z['R'],z['reset']),z['loss'])==root['R'],'exact stopped reserve conservation')
  ok(z['spent']+z['I']==root['I'],'same-tree stopped influence')
  leconst(add(add(add(z['cap'],z['R']),z['reset']),root['R'],-1),2*z['P'],'stopped cap including reset and terminal reserve')
  rhs=add(add(add(add(z['H'],root['U']),z['U'],-1),root['R']),z['R'],-1)
  rhs=add(rhs,z['controller'])
  leconst(add(root['H'],rhs,-1),3*z['T'],'stopped signed entropy ledger')
 return maxdepth
def tables(n):return [tuple(1-2*((m>>x)&1) for x in range(1<<n)) for m in range(1<<(1<<n))]
def main(pilot):
 start=time.perf_counter();roots=trees=0
 maps=list(itertools.product(range(3),repeat=4))
 for c in (maps[:1] if pilot else maps):
  for u in tables(1):
   for v in tables(1):
    for policy in range(4):tree(c,u,v,policy);trees+=1
    roots+=1
    if time.perf_counter()-start>180:raise RuntimeError('frozen main runtime exceeded')
 if not pilot:
  for c in [(1,0,0,0),(1,1,2,0)]:
   for u in tables(2):
    for v in tables(1):
     for policy in [2,3]:tree(c,u,v,policy);trees+=1
     roots+=1
 out={'status':'PASS','roots':roots,'trees':trees,'assertions':checks,'elapsed_seconds':time.perf_counter()-start,'max_truth_table_bits':5,'pilot':pilot,'arithmetic':'integer Walsh/Fraction and rational prime-log identities; rigorous 32-term atanh tails; finite cap uses weaker 2-nat data constant'}
 (ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps(out))
if __name__=='__main__':main('--pilot' in sys.argv)
