from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import argparse,itertools,math,json,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();assertions=0
pa=argparse.ArgumentParser();pa.add_argument('--pilot',action='store_true');args=pa.parse_args();budget=60 if args.pilot else 300
def ck(x):
 global assertions
 assertions+=1;assert x
 if time.monotonic()-start>budget:raise TimeoutError('Frozen compute budget')
def walsh(a):
 a=list(a);h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):
    u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
  h*=2
 return a
def ln_small(x):
 z=(x-1)/(x+1);lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(18)),F(0))
 return lo,lo+2*z**37/(37*(1-z*z))
ln2=ln_small(F(2))
@lru_cache(None)
def lg(x):
 x=F(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 lo,hi=ln_small(x);return lo/ln2[1]+k,hi/ln2[0]+k
def CE(P,Q):
 lo=hi=F(0)
 for p,q in zip(P,Q):
  if p:
   ck(q>0);a,b=lg(1/q);lo+=p*a;hi+=p*b
 return lo,hi
def components(n,edges,exclude=None):
 todo=set(range(n))-{exclude} if exclude is not None else set(range(n));out=[]
 while todo:
  seed=min(todo);todo.remove(seed);part={seed};front=[seed]
  while front:
   u=front.pop()
   for a,b in edges:
    v=b if a==u else a if b==u else None
    if v in todo:todo.remove(v);part.add(v);front.append(v)
  out.append(sorted(part))
 return out
def matchings(edges,A):
 e=[pair for pair in edges if all(A&(1<<v) for v in pair)];out=[]
 for mask in range(1<<len(e)):
  M=[];used=0
  for j,pair in enumerate(e):
   if mask&(1<<j):
    em=sum(1<<v for v in pair)
    if used&em:break
    used|=em;M.append(pair)
  else:
   if all(used&sum(1<<v for v in pair) for pair in e):out.append(M)
 return out
def occupation(n,edges,A,lam,D):
 total=F(0)
 for M in matchings(edges,A):
  vertices=[v for pair in M for v in pair];where={v:i for i,v in enumerate(vertices)}
  U=[u for u in range(n) if A&(1<<u) and u not in where]
  poly={tuple(0 for _ in vertices):F(1)};choices=[]
  for u in U:
   terms=[];individual=[];ext=F(0)
   for a,b in edges:
    v=b if a==u else a if b==u else None
    if v is None:continue
    if not A&(1<<v):ext+=lam/32;individual.append((None,lam/32))
    else:ck(v in where);terms.append((where[v],lam/8));individual.append((where[v],lam/8))
   if ext:terms.append((None,ext))
   choices.append(individual);nxt={}
   for h,c in poly.items():
    for index,w in terms:
     h2=list(h)
     if index is not None:h2[index]+=1
     h2=tuple(h2);nxt[h2]=nxt.get(h2,F(0))+c*w
   poly=nxt
  def J(h):
   val=F(1)
   for j in range(len(M)):
    a,b=h[2*j],h[2*j+1];c=a+b;val*=F(math.factorial(a)*math.factorial(b),(c+1)**2*(c+2))
   return val
  convolution=sum((c*J(h) for h,c in poly.items()),F(0));independent=F(0)
  for selected in itertools.product(*choices):
   h=[0]*len(vertices);c=F(1)
   for index,w in selected:
    c*=w
    if index is not None:h[index]+=1
   independent+=c*J(h)
  ck(convolution==independent);total+=(lam/24)**len(M)*convolution/D
 return total
def outward(interval):
 scale=10**8;lo,hi=interval
 return [str(F(math.floor(lo*scale),scale)),str(F(math.ceil(hi*scale),scale))]
rows=[];candidates=0;sets=0;wins={'occupation':0,'product':0,'unresolved':0}
for n in ([3] if args.pilot else [3,4,5]):
 universe=list(itertools.combinations(range(n),2))
 for mask in range(1<<len(universe)):
  candidates+=1;edges=[e for j,e in enumerate(universe) if mask&(1<<j)]
  if len(components(n,edges))!=1:continue
  cuts=[x for x in range(n) if len(components(n,edges,x))>1]
  if not cuts:continue
  x=cuts[0];parts=components(n,edges,x);Y=parts[0];Z=sorted(set(range(n))-{x}-set(Y))
  deg=[sum(u in e for e in edges) for u in range(n)];lam=F(1,max(deg));ck(all(d*lam<=1 for d in deg))
  D=(1+lam/4)**len(edges)-1;emasks=[sum(1<<v for v in e) for e in edges]
  C=[int(not any(z&e==e for e in emasks)) for z in range(1<<n)];s=F(sum(C),1<<n);v=4*s*(1-s)
  fh=walsh([1-2*c for c in C]);ch=walsh(C);p=[F(h*h,1<<(2*n)) for h in fh]
  I=sum((A.bit_count()*mass for A,mass in enumerate(p)),F(0));ck(sum(p)==1);ck(p[0]==1-v);ck(I>=v)
  hats=[];As=[]
  for bit in (0,1):
   branches=[]
   for block in (Y,Z):
    vectors=[];allowed=sum(1<<u for u in block)|(1<<x);relevant=[e for e in emasks if e&~allowed==0]
    for z in range(1<<len(block)):
     zfull=(bit<<x)+sum(((z>>j)&1)<<vertex for j,vertex in enumerate(block))
     vectors.append(int(not any(zfull&e==e for e in relevant)))
    branches.append([F(t,len(vectors)) for t in walsh(vectors)])
   hats.append(branches);As.append(branches[0][0]*branches[1][0])
  ck(sum(As)/2==s);qC=[]
  for A in range(1<<n):
   U=sum(((A>>vertex)&1)<<j for j,vertex in enumerate(Y));V=sum(((A>>vertex)&1)<<j for j,vertex in enumerate(Z))
   a=hats[0][0][U]*hats[0][1][V];b=hats[1][0][U]*hats[1][1][V]
   ck(((a-b)/2 if A&(1<<x) else (a+b)/2)==F(ch[A],1<<n));qC.append((a*a+b*b)/(4*s))
  ck(sum(qC)==1);qe=qC[0];ck(qe>=s/2)
  product=[1-v]+[v*q/(1-qe) for q in qC[1:]];ck(sum(product)==1)
  masses=[F(0)]+[occupation(n,edges,A,lam,D) for A in range(1,1<<n)]
  ck(all(m>0 for m in masses[1:]));massZ=sum(masses);ck(0<massZ<=1)
  occ=[1-v]+[v*m/massZ for m in masses[1:]];mix=[(a+b)/2 for a,b in zip(product,occ)]
  blocker=[s]+[(1-s)*m/massZ for m in masses[1:]];ck(sum(occ)==sum(mix)==sum(blocker)==1)
  ck(all(m>=a/2 and m>=b/2 for a,b,m in zip(product[1:],occ[1:],mix[1:])))
  H=CE(p,p);Cp=CE(p,product);Co=CE(p,occ);Cm=CE(p,mix);ck(Cp[1]-H[0]<=2*I)
  ck(all(occ[A]==v*blocker[A]/(1-s) for A in range(1,1<<n)))
  PC=[F(t*t,1<<(2*n))/s for t in ch];CEC=CE(PC,blocker)
  hb=CE([v,1-v],[v,1-v]);hs=CE([s,1-s],[s,1-s])
  converted=(hb[0]+4*s*(CEC[0]-hs[1]),hb[1]+4*s*(CEC[1]-hs[0]));ck(converted[0]<=Co[1] and Co[0]<=converted[1])
  rawce=CE(p[1:],masses[1:]);raw=(hb[0]+rawce[0],hb[1]+rawce[1]);lz=lg(massZ)
  normalized=(raw[0]+v*lz[0],raw[1]+v*lz[1]);ck(normalized[0]<=Co[1] and Co[0]<=normalized[1])
  if Co[1]<Cp[0]:wins['occupation']+=1
  elif Cp[1]<Co[0]:wins['product']+=1
  else:wins['unresolved']+=1
  sets+=(1<<n)-1
  rows.append({'n':n,'edge_mask':mask,'edges':edges,'separator':x,'Y':Y,'Z':Z,'lambda':str(lam),'s':str(s),'v':str(v),'I':str(I),'occupation_Z':str(massZ),'H_over_I':outward((H[0]/I,H[1]/I)),'product_CE_over_I':outward((Cp[0]/I,Cp[1]/I)),'occupation_CE_over_I':outward((Co[0]/I,Co[1]/I)),'mixture_CE_over_I':outward((Cm[0]/I,Cm[1]/I)),'product_excess_over_I':outward(((Cp[0]-H[1])/I,(Cp[1]-H[0])/I)),'complete_nonempty_occupation_masses':[str(t) for t in masses[1:]]})
  (R/'out/checkpoint.json').write_text(json.dumps({'graphs_complete':len(rows),'candidates':candidates,'assertions':assertions,'elapsed_seconds':time.monotonic()-start},indent=2)+'\n')
out={'helper':'A014-occupation-separator-v1','mode':'pilot' if args.pilot else 'full','labelled_candidates':candidates,'selected_graphs':len(rows),'all_nonempty_sets':sets,'wins':wins,'assertions':assertions,'elapsed_seconds':time.monotonic()-start,'rows':rows}
(R/('out/pilot.json' if args.pilot else 'out/check.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
