from pathlib import Path
from fractions import Fraction as F
from itertools import product,permutations,combinations_with_replacement
from math import comb,prod
import importlib.util,sys,json,time
sys.dont_write_bytecode=True
B=Path(__file__).resolve().parents[1];O=B/'out';pilot='--pilot' in sys.argv;start=time.monotonic();checks=0;visits=0;limit=55 if pilot else 240
spec=importlib.util.spec_from_file_location('own_parent_maps',B.parent/'20261021T161852Z-fleet03-A010-universal-residual-falsifier/code/check.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
def ck(p):
 global checks
 checks+=1
 assert p,checks
def deadline():ck(time.monotonic()-start<limit)
def save(name,x):(O/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='\n')
def logs(x):
 x=F(x);j=0
 while x<1:x*=2;j-=1
 while x>=2:x/=2;j+=1
 def ln(y):
  z=(y-1)/(y+1);l=2*sum((z**(2*i+1)/F(2*i+1) for i in range(20)),F(0));return l,l+2*z**41/(41*(1-z*z))
 l,u=ln(x);l2,u2=ln(F(2));return j+l/u2,j+u/l2
def fifo(A,E,n):
 """Construct histories forward in FIFO order, rather than enumerate parent maps."""
 global visits
 C={};runs=0;vertices=[v for v in range(n) if A>>v&1]
 if not vertices:return {0:F(1)},1
 if any(not any(v in e for e in E) for v in vertices):return {},0
 for assign in product(*[[i for i,e in enumerate(E) if v in e] for v in vertices]):
  blocks={i:tuple(v for v,j in zip(vertices,assign) if j==i) for i in sorted(set(assign))};U=list(blocks)
  adj={i:{j for j in U if j!=i and any(v in E[j] for v in blocks[i])} for i in U};reach={}
  for i in U:
   found={i};pending=[i]
   while pending:
    j=pending.pop()
    for k in adj[j]-found:found.add(k);pending.append(k)
   reach[i]=found
  comps=sorted({frozenset(j for j in U if j in reach[i] and i in reach[j]) for i in U},key=min)
  sources=[S for S in comps if not any(j in adj[i] for i in U if i not in S for j in S)]
  T=sum(1<<i for i in U)
  def walk(queue,discovered,p):
   nonlocal runs
   global visits
   visits+=1
   if visits%1000==0:deadline()
   if not queue:
    if len(discovered)==len(U):C[T]=C.get(T,F(0))+p;runs+=1
    return
   i=queue[0];rest=queue[1:];s=len(blocks[i]);und=[j for j in U if j not in discovered]
   opts=[[None]+[v for v in blocks[i] if v in E[j]] for j in und]
   for choices in product(*opts):
    slots={v:[] for v in blocks[i]}
    for j,v in zip(und,choices):
     if v is not None:slots[v].append(j)
    c=sum(map(len,slots.values()));factor=F(1,s*(s+1)*comb(2,s)*(c+1)*(c+2)*comb(s+c-1,c))
    for words in product(*[list(permutations(slots[v])) for v in sorted(slots)]):
     children=tuple(j for word in words for j in word)
     walk(rest+children,discovered|set(children),p*factor)
  for roots in product(*[sorted(S) for S in sources]):walk(tuple(sorted(roots)),set(roots),F(1,4**len(roots)))
 return C,runs
def components(E):
 unseen=set(v for e in E for v in e);out=[]
 while unseen:
  found={min(unseen)}
  while True:
   extended=found|{v for e in E if found.intersection(e) for v in e}
   if extended==found:break
   found=extended
  unseen-=found;out.append(found)
 return out
def convolution(A,E,n):
 out={0:F(1)}
 for V in components(E):
  idx=[i for i,e in enumerate(E) if e[0] in V];local=tuple(E[i] for i in idx);mask=sum(1<<v for v in V);AA=A&mask
  coef,_=old.full(AA,local,n) if AA else ({0:F(1)},1)
  lifted={sum(1<<idx[j] for j in range(len(idx)) if T>>j&1):c for T,c in coef.items()}
  out={T|S:a*b for T,a in out.items() for S,b in lifted.items()}
 return out
graphs=[((0,1),(2,3)),((0,1),(1,2),(3,4)),((0,1),(1,2),(3,4),(4,5)),((0,2),(0,3),(1,2),(1,3),(4,5)),((0,1),(2,3),(4,5))]
factorrows=[]
for E in graphs[:2] if pilot else graphs:
 n=1+max(v for e in E for v in e);totalruns=0
 for A in range(1,1<<n):
  c,r=fifo(A,E,n);p,pr=old.full(A,E,n);ck(c==p==convolution(A,E,n) and r==pr);totalruns+=r
 factorrows.append({'edges':E,'n':n,'outputs':(1<<n)-1,'distinct_runs':totalruns});save('FACTOR_CHECKPOINT.json',factorrows);deadline()
def spectrum(values):
 w=values[:];step=1
 while step<len(w):
  for i in range(0,len(w),2*step):
   for j in range(i,i+step):w[j],w[j+step]=w[j]+w[j+step],w[j]-w[j+step]
  step*=2
 return [F(z,len(w)) for z in w]
def influence(values,n):return F(sum(values[x]!=values[x^(1<<j)] for x in range(1<<n) for j in range(n)),1<<n)
reviews=[];tables=0
def inspect(a,b,H):
 global tables
 tables+=1;n=a+b;G=[(i,a+j) for i in range(a) for j in range(b) if (i,j) not in H];d=max([sum(i==x for x,y in H) for i in range(a)]+[sum(j==y for x,y in H) for j in range(b)])
 f=[1 if any(x>>i&1 and x>>j&1 for i,j in G) else -1 for x in range(1<<n)]
 f0=[1 if (x&((1<<a)-1)) and (x>>a) else -1 for x in range(1<<n)]
 event=[int(f0[x]==1 and f[x]==-1) for x in range(1<<n)];delta=[-2*z for z in event];df=spectrum(delta);ff=spectrum(f);I=influence(f,n);J=influence(event,n);e=sum(event);u=F(1,2**a);v=F(1,2**b)
 ck(sum(A.bit_count()*z*z for A,z in enumerate(df))==J);ck(sum(A.bit_count()*z*z for A,z in enumerate(ff))==I);ck(J<=2*n*e*u*v)
 ck(all(f[x]==f0[x]+delta[x] for x in range(1<<n)))
 if d<=2:
  h=len(H);wl=sum(sum(x==i for x,y in H)==2 for i in range(a));wr=sum(sum(y==j for x,y in H)==2 for j in range(b));c4=sum(all((i,j) in H for i in X for j in Y) for X in __import__('itertools').combinations(range(a),2) for Y in __import__('itertools').combinations(range(b),2))
  ck(e==h+wl+wr+c4 and 4*e<=9*h and 2*e<=9*a)
 if d and d<=a/2:ck(e<=a*(2**d-1)*2**(d-1))
 if a>=4 and d<=a/2:
  lower=2*a*u*(1-F(1,2**(b-d)));ck(I>=lower>0)
  # Our physical larger-side sample has b=4, so log b is EXACTLY2.
  ck(b==4);ck(2*J/I<=F(b*b)*F(2)**(2*d-b)/(1-F(1,2**(b-d))))
 return d
pairs=[(2,2)] if pilot else [(2,2),(2,3),(3,3)]
for a,b in pairs:
 seen=0;degree2=0
 for mask in range(1<<(a*b)):
  H={(i,j) for i in range(a) for j in range(b) if mask>>(i*b+j)&1};d=inspect(a,b,H);seen+=1;degree2+=d<=2
 reviews.append({'a':a,'b':b,'tables':seen,'degree_two':degree2});save('REVIEW_CHECKPOINT.json',reviews);deadline()
if not pilot:
 def matchings(i=0,used=frozenset(),edges=frozenset()):
  if i==4:yield edges;return
  yield from matchings(i+1,used,edges)
  for j in range(4):
   if j not in used:yield from matchings(i+1,used|{j},edges|{(i,j)})
 mm=0
 for H in matchings():inspect(4,4,H);mm+=1
 ck(mm==209);reviews.append({'a':4,'b':4,'matchings':mm});deadline()
cross=None
if not pilot:
 E0=((0,2),(0,3),(1,2),(1,3));E=E0+tuple((x+4,y+4) for x,y in E0);n=8
 local={A:old.full(A,E0,4)[0] for A in range(1,16)};local[0]={0:F(1)}
 states=[((1<<s)-1)|(((1<<t)-1)<<2) for s,t in [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]];reps=0
 for A0,A1 in combinations_with_replacement(states,2):
  A=A0|(A1<<4)
  if not A:continue
  z,rr=fifo(A,E,n);p,pr=old.full(A,E,n);ck(z==p==convolution(A,E,n) and rr==pr);reps+=1
 ck(reps==20)
 lam=F(1,4);D=(1+lam/4)**8-1;DR=(1+F(1,2)/4)**8-1;W={A:sum(c*lam**T.bit_count() for T,c in local[A].items()) for A in local};WR={A:sum(c*F(1,2)**T.bit_count() for T,c in local[A].items()) for A in local}
 f=[1 if any(x>>i&1 and x>>j&1 for i,j in E) else -1 for x in range(256)];ff=spectrum(f);P=[z*z for z in ff];I=influence(f,8);mass=F(0)
 for A in range(1,256):
  Q=W[A&15]*W[A>>4]/D;mass+=Q;ck(Q>0);ck(W[A&15]*W[A>>4]<=WR[A&15]*WR[A>>4]/2**((A.bit_count()+1)//2))
 for S in range(1,16):
  lf=spectrum([1 if any(x>>i&1 and x>>j&1 for i,j in E0) else -1 for x in range(16)])
  ck(sum(P[A] for A in range(256) if A&15==S)==F(7,16)*lf[S]**2)
 ck(mass<=1 and I==F(21,16))
 # Direct source obstruction: E is computed relative to full K44.
 full=[1 if (x&3 or x&48) and (x&12 or x&192) else -1 for x in range(256)]
 exc=[int(full[x]==1 and f[x]==-1) for x in range(256)];J=influence(exc,8);ck(J/I==F(4,7))
 c0=c1=d0=d1=F(0)
 for A in range(1,256):
  lo,hi=logs(D/(W[A&15]*W[A>>4]));c0+=P[A]*lo;c1+=P[A]*hi
  lo,hi=logs(DR/(WR[A&15]*WR[A>>4]));d0+=P[A]*lo;d1+=P[A]*hi
 ck(c1<F(71,8)*I and d1<F(63,8)*I)
 cross={'representatives':reps,'all_outputs':255,'I':str(I),'J':str(J),'J_over_I':str(J/I),'full_queue_mass':str(mass),'uniform_cost_interval_bits':list(map(str,[c0,c1])),'retuned_cost_interval_bits':list(map(str,[d0,d1]))};deadline()
controls=None
if not pilot:
 # A deliberately invalid shared-coordinate product has an exact128-fold error.
 Ec=((0,1),(1,2));co,ct=fifo(2,Ec,3);cp,cpt=old.full(2,Ec,3);ck(co==cp and ct==cpt)
 lam=F(1,2);actual=sum(z*lam**T.bit_count() for T,z in co.items());wrong=(lam/32)**2
 ck(actual==F(1,32) and actual/wrong==128)
 # Dropping local root-normalizer corrections is already false on two AND2s.
 ee=((0,1),(2,3));D=F(9,16);localD=F(1,4);c0=c1=F(0)
 pp=spectrum([1 if any(x>>i&1 and x>>j&1 for i,j in ee) else -1 for x in range(16)])
 for A in range(1,16):
  num=sum(old.full(A,ee,4)[0].values());lo,hi=logs(D/num);c0+=pp[A]**2*lo;c1+=pp[A]**2*hi
 l3,u3=logs(F(3));local_lo=2+l3/4;local_hi=2+u3/4
 ck(c0-F(3,2)*local_hi>F(81,64));controls={'shared_coordinate_actual_numerator':str(actual),'invalid_product_numerator':str(wrong),'error_factor':128,'naive_complete_cost_composition_gap_lower_bits':str(c0-F(3,2)*local_hi),'exact_gap_expression':'(63/32)log2(3)-27/16 >81/64'}
 save('CONTROLS.json',controls)
scalar=0
for m in range(2,9 if pilot else 65):
 u=F(1,2**m);q=2*u-u*u;ck(m*u<=F(1,2));ck((2-u)/(1-u)<=F(7,3))
 for r in range(2,9 if pilot else 65):
  Ib=4*m*u*(1-u);If=r*q**(r-1)*Ib;vf=4*q**r*(1-q**r);ck(vf/If<=F(7,3*r*m));scalar+=1
for a in range(4,9 if pilot else 33):
 for b in range(a,9 if pilot else 33):
  for d in range(a//2+1):
   ck(1-F(1,2**(b-d))>=F(3,4))
   if 4*d<=a:ck(F(b**4,2**b)<=F(81,4))
   if a*a*4**d<=2**a:ck(F(b*b)*F(2)**(2*d-b)<=1)
ck(72**4<2**25);deadline()
result={'status':'PASS','helper':'A010-component-queue-v1','pilot':pilot,'factorization_graphs':factorrows,'fifo_calls':visits,'review_tables':tables,'source_review':reviews,'crossed':cross,'negative_controls':controls,'scalar_rm_pairs':scalar,'assertions':checks,'seconds':time.monotonic()-start}
save('PILOT.json' if pilot else 'CHECK.json',result);print(json.dumps({k:v for k,v in result.items() if k not in ('factorization_graphs','source_review','crossed','negative_controls')}))
