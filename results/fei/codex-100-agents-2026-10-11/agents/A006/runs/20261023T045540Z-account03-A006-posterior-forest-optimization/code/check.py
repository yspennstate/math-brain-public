from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
import json,sys,time,math
B=Path(__file__).resolve().parent.parent
start=time.monotonic();assertions=0
def ck(q):
 global assertions
 assertions+=1
 assert q,assertions
def walsh(a):
 a=list(a);h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def influence(a,n):return F(sum(a[x]!=a[x^(1<<j)] for x in range(len(a)) for j in range(n)),len(a))
def prime_cubes(a,n):
 cubes=[]
 for z in product((-1,0,1),repeat=n):
  M=sum(1<<i for i,v in enumerate(z) if v!=-1);V=sum(1<<i for i,v in enumerate(z) if v==1)
  if all(a[x]==1 for x in range(1<<n) if x&M==V):cubes.append((M,V))
 return {(M,V) for M,V in cubes if not any((M^(1<<i),V&~(1<<i)) in cubes for i in range(n) if M>>i&1)}
def review_signed():
 pairs=0
 for aa in range(1,15):
  a=[1 if aa>>x&1 else -1 for x in range(4)];qa=F(a.count(-1),4);wa=walsh(a);pa=prime_cubes(a,2)
  for bb in range(1,15):
   b=[1 if bb>>x&1 else -1 for x in range(4)];qb=F(b.count(-1),4);wb=walsh(b);pb=prime_cubes(b,2)
   f=[1 if a[x&3]==1 or b[x>>2]==1 else -1 for x in range(16)];w=walsh(f)
   ck(influence(f,4)==qb*influence(a,2)+qa*influence(b,2))
   ck(prime_cubes(f,4)==pa|{(M<<2,V<<2) for M,V in pb})
   for s in range(1,4):
    ck(sum(F(w[s|(t<<2)]**2,256) for t in range(4))==qb*F(wa[s]**2,16))
    ck(sum(F(w[t|(s<<2)]**2,256) for t in range(4))==qa*F(wb[s]**2,16))
   pairs+=1
 return pairs
def forests():
 out=[]
 for p in product(range(-1,3),repeat=3):
  if any(p[i]==i for i in range(3)):continue
  good=True
  for i in range(3):
   seen=set();j=i
   while j!=-1:
    if j in seen:good=False;break
    seen.add(j);j=p[j]
  if good:out.append(p)
 return out
def fifo(p,rank):
 q=sorted((i for i in range(len(p)) if p[i]==-1),key=lambda i:rank[i]);out=[]
 while q:
  i=q.pop(0);out.append(i);q+=sorted((j for j in range(len(p)) if p[j]==i),key=lambda j:rank[j])
 return out
def review_merges():
 fs=forests();ck(len(fs)==16);count=0
 for positions in combinations(range(6),3):
  left=list(positions);right=[i for i in range(6) if i not in left];rank=left+right
  seen=set()
  for p in fs:
   for q in fs:
    par=p+tuple(j+3 if j!=-1 else -1 for j in q);word=fifo(par,rank)
    ck([i for i in word if i<3]==fifo(p,left))
    ck([i-3 for i in word if i>=3]==fifo(q,right))
    identity=(tuple(sorted((i for i in range(6) if par[i]==-1),key=lambda i:rank[i])),par,tuple(word))
    ck(identity not in seen);seen.add(identity);count+=1
 return count
def submass(m,center,rights):
 # Actual distinct roots and owned blocks in ONE component. Gate=(left,right).
 lam=F(1,2*m);histories={}
 if not center:
  for choices in product(range(m),repeat=len(rights)):
   blocks=tuple(sorted((((i,j),(('R',j),)) for i,j in zip(choices,rights))))
   ck(blocks not in histories);histories[blocks]=(lam/32)**len(rights)
  expected=F(1,64)**len(rights)
 elif not rights:
  for j in range(m):histories[(((0,j),(('L',0),)),)]=lam/32
  expected=F(1,64)
 else:
  first=rights[0]
  for choices in product(range(m),repeat=len(rights)-1):
   blocks=[((0,first),(('L',0),('R',first)))]+[((i,j),(('R',j),)) for i,j in zip(choices,rights[1:])]
   blocks=tuple(sorted(blocks));ck(blocks not in histories)
   owned=[x for gate,z in blocks for x in z]
   ck(len(owned)==len(set(owned))==len(rights)+1)
   ck(len({gate for gate,z in blocks})==len(blocks))
   histories[blocks]=lam/48*(lam/32)**(len(rights)-1)
  expected=F(2,3*m)*F(1,64)**len(rights)
 mass=sum(histories.values(),F(0));ck(mass==expected)
 if center or rights:ck(mass>=F(1,64)**(len(rights)+center)*F(2,3*m))
 else:ck(mass==1)
 return mass,len(histories)
def physical(m):
 n=4*m;N=1<<n;mask=(1<<m)-1;f0=[];f1=[];z=[];e=[]
 # coordinates L1,R1,L2,R2, each m; connector bits0 and3m.
 for x in range(N):
  L1=x&mask;R1=(x>>m)&mask;L2=(x>>(2*m))&mask;R2=(x>>(3*m))&mask
  a=bool(L1 and R1 or L2 and R2);bridge=bool(x&1 and x>>(3*m)&1)
  f0.append(1 if a else -1);f1.append(1 if a or bridge else -1)
  z.append(bridge and not a);e.append(bool((L1 or L2) and (R1 or R2) and not a))
 W=sum(1<<j for j in [0,3*m]+list(range(m,3*m)))
 delta=[b-a for a,b in zip(f0,f1)];wd=walsh(delta);w0=walsh(f0);w1=walsh(f1)
 t=F(1,2**m);p=F(1,2**(2*m+2));I0=influence(f0,n);I1=influence(f1,n);J=influence(e,n)
 ck(I0==8*m*t*t*(1-t)*(2-t));ck(I1==I0-(m-1)*t*t)
 ck(J==8*m*t*t*(1-t));ck(sum(z)==N*p)
 ck(all(delta[x]==2*z[x] for x in range(N)))
 for s in range(N):
  ck((abs(wd[s])==2*p*N) if s&~W==0 else wd[s]==0)
 ck(F(sum(w*w for w in wd),N*N)==t*t)
 ck(F(sum(s.bit_count()*w*w for s,w in enumerate(wd)),N*N)==(m+1)*t*t)
 ck(I1==F(sum(s.bit_count()*w*w for s,w in enumerate(w1)),N*N))
 ck(all(w1[s]==w0[s]+wd[s] for s in range(N)))
 masses={};rootchoices=0
 for S in range(1<<(m+1)):
  center=bool(S>>m);rights=[j for j in range(m) if S>>j&1]
  masses[S],c=submass(m,center,rights);rootchoices+=c
 d=2*m+2;nonemptysets=0
 for S in range(1,1<<d):
  a=S&((1<<(m+1))-1);b=S>>(m+1)
  # A pair of actual local ALL-ROOT histories has one fixed global merge.
  ck(masses[a]*masses[b]>=F(1,64)**S.bit_count()*F(2,3*m)**2)
  nonemptysets+=1
 return dict(m=m,physical_inputs_per_function=N,I0=str(I0),I1=str(I1),J=str(J),cylinder_probability=str(p),cylinder_nonempty_sets=nonemptysets,distinct_local_root_choices=rootchoices)
def scalars():
 c=0
 for m in range(2,257):
  t=F(1,2**m);a=8*m*t*t*(1-t)*(2-t);b=a-(m-1)*t*t
  ck(b>=F(19,2)*m*t*t);ck(a<=F(21,19)*b)
  ck(3*m<=2**(m+1));ck(6*(m+1)<=9*m)
  ck(F(1,8*m)+F(1,2*m*m)<=F(3,16));c+=1
 ck(F(1491,76)+F(91,38)+F(9,32)<23)
 for a in range(4,65):
  for b in range(a,65):
   for d in range(a//2+1):
    tail=F(b*b)*F(2)**(2*d-b)/(1-F(2)**(-(b-d)))
    if 4*d<=a:ck(F(91,8)+2*tail<22)
    if a*a*4**d<=2**a:ck(F(91,8)+2*tail<15)
 # All-parameter proof uses these exact inequalities and inductions.
 for b in range(4,257):ck(F(b**4,2**b)<=F(81,4))
 for h in range(257):ck(F((h+4)**2,16*2**h)<=1)
 return c
def main():
 pilot='--pilot' in sys.argv
 result={'status':'PASS','helper_version':'A006-connected-connector-v1','pilot':pilot}
 result['signed_component_pairs']=review_signed()
 result['unique_FIFO_merges']=review_merges()
 result['rows']=[physical(m) for m in ((2,3) if pilot else (2,3,4))]
 result['scalar_m_cases']=scalars()
 result['assertions']=assertions;result['seconds']=time.monotonic()-start
 ck(result['seconds']<(55 if pilot else 120))
 (B/'out').mkdir(exist_ok=True)
 tag='PILOT' if pilot else 'CHECK'
 (B/'out'/f'{tag}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result))
if __name__=='__main__':main()
