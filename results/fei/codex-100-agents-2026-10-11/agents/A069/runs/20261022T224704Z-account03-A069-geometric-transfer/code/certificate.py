from pathlib import Path
from fractions import Fraction as R
from functools import lru_cache
from itertools import product
import time,json,hashlib
RUN=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1;assert x,checks
 assert time.monotonic()-start<55,'55s frozen guard'
def fw(v):
 v=list(v);step=1
 while step<len(v):
  for j in range(0,len(v),2*step):
   for i in range(j,j+step):
    x,y=v[i],v[i+step];v[i],v[i+step]=x+y,x-y
  step*=2
 return v
@lru_cache(None)
def factors(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def add(*terms):
 d={}
 for w,b in terms:
  for p,v in b.items():d[p]=d.get(p,R(0))+w*v
 return {p:v for p,v in d.items() if v}
@lru_cache(None)
def log(q):
 q=R(q);assert q>0
 return add((1,factors(q.numerator)),(-1,factors(q.denominator)))
def h(q):return add(*[(-v,log(v)) for v in (q,1-q) if v])
def ln(q):
 z=(q-1)/(q+1)
 lo=2*sum((z**(2*j+1)/R(2*j+1) for j in range(24)),R(0))
 return lo,lo+2*z**49/(49*(1-z*z))
ln2=ln(R(2))
@lru_cache(None)
def ilog(q):
 q=R(q);k=0
 while q<1:q*=2;k-=1
 while q>=2:q/=2;k+=1
 lo,hi=ln(q)
 return R(k)+lo/ln2[1],R(k)+hi/ln2[0]
def interval(ex):
 lo=hi=R(0)
 for p,w in ex.items():
  a,b=ilog(p);lo+=w*(a if w>0 else b);hi+=w*(b if w>0 else a)
 return lo,hi
def nonnegative(ex):return not ex or interval(ex)[0]>=0
def maj(v):return 1 if sum(v)>0 else -1
a=[maj([maj([2*((x>>i)&1)-1 for i in range(j,j+3)]) for j in (0,3,6)]) for x in range(512)]
b=a.copy();b[0]*=-1
weights=[R(1,1<<(1+3*((s!=0)+sum(bool(s&(7<<j)) for j in (0,3,6))))) for s in range(512)]
Z=sum(weights);ref=[w/Z for w in weights];ck(sum(ref)==1);ck(Z==R(6959,8192))
stats={};core_excess_total={};positive_lo=positive_hi=R(0);bad_rows=[]
for depth in range(10):
 ry=[sum(ref[s] for s in range(512) if s>>depth==t) for t in range(1<<(9-depth))]
 ck(sum(ry)==1)
 for prefix in range(1<<depth):
  aa=[a[prefix|(y<<depth)] for y in range(1<<(9-depth))];bb=[b[prefix|(y<<depth)] for y in range(1<<(9-depth))]
  N=len(aa);Ps=[[R(z*z,N*N) for z in fw(v)] for v in (aa,bb)]
  B=add(*[(-p/2,log(ry[t])) for P in Ps for t,p in enumerate(P) if p])
  A=sum(p*t.bit_count()/2 for P in Ps for t,p in enumerate(P))
  d=R(sum(x!=y for x,y in zip(aa,bb)),N)
  ck(all(sum(P)==1 for P in Ps));ck(A==sum(R(sum(v[x]!=v[x^(1<<j)] for x in range(N)),2*N) for v in [aa,bb] for j in range(9-depth)))
  stats[depth,prefix]={'A':A,'B':B,'d':d,'a':aa,'b':bb,'R':ry}
for (depth,prefix),p in stats.items():
 if depth==9:continue
 cs=[stats[depth+1,prefix|(v<<depth)] for v in (0,1)];prob=R(1,1<<depth)
 j=p['A']-(cs[0]['A']+cs[1]['A'])/2
 ck(j>=0);ck(p['d']==(cs[0]['d']+cs[1]['d'])/2)
 deltaB=add((1,p['B']),(-R(1,2),cs[0]['B']),(-R(1,2),cs[1]['B']))
 e=add((1,deltaB),(-4*j,log(2)));lo,hi=interval(e)
 if not e:ck(lo==hi==0)
 elif hi<0:pass
 else:
  ck(lo>0);positive_lo+=prob*lo;positive_hi+=prob*hi
 core_excess_total=add((1,core_excess_total),(prob,e))
 full=add((1,e),(1,h(p['d']/4)),(-R(1,2),h(cs[0]['d']/4)),(-R(1,2),h(cs[1]['d']/4)))
 if full and interval(full)[0]>0 and j>0:
  bad_rows.append({'depth':depth,'prefix':prefix,'Inf':str(j),'excess_interval':list(map(str,interval(full))),'child_A':[str(c['A']) for c in cs]})
ck(positive_hi<R(7,12));ck(interval(h(R(1,512)))[1]<R(1,32))
ck(R(7,12)+R(1,128)<R(3,5));ck(R(5,8)-R(3,5)==R(1,40))
root=stats[0,0];source=add((4*root['A'],log(2)),(-1,root['B']))
rootlo,roothi=interval(source);ck(rootlo>R(3,4))
children=[]
for v in (0,1):
 c=stats[1,v];sigma=add((4*c['A'],log(2)),(-1,c['B']));lo,hi=interval(sigma)
 ck(lo>R(1,2));ck(c['A']>0);children.append({'prefix':v,'A':str(c['A']),'source_surplus_interval':[str(lo),str(hi)]})
ck(core_excess_total==add((1,root['B']),(-4*root['A'],log(2))))
ck(len(bad_rows)==3)
ck(all(all(R(v)>0 for v in r['child_A']) for r in bad_rows if r['depth'] in (0,2)))
def formula(p,m):
 r=R(1,1<<m);d=p['d'];beta=2*r*(1-r)
 C=add((1,p['B']),(1,h(d*r*r)),(2+2*(1-2*d)*r,log(2)),(beta,log((1-r)/r*R(20,7))))
 I=p['A']+1+(m+1-2*d)*r
 return I,C
fullfixtures=0
for depth,prefix in [(0,0),(1,0),(2,0)]:
 p=stats[depth,prefix];Ncore=len(p['a']);tab=[]
 for x in range(8*Ncore):
  c=x&1;u=(x>>1)&1;z=(x>>2)&1;y=x>>3
  val=[p['a'][y],p['b'][y],-p['b'][y],-p['a'][y]][c+2*u]
  tab.append(val*(-1 if c==0 and z==0 else 1))
 N=len(tab);P=[R(w*w,N*N) for w in fw(tab)];alpha=sum(q for s,q in enumerate(P) if s&7)
 ck(alpha==1-p['d']/4)
 tail=[R(0),R(1,4),R(1,4),R(1,16),R(7,40),R(7,40),R(7,160),R(7,160)]
 C={}
 for s,q in enumerate(P):
  if q:
   ctrl=s&7;rd=(1-alpha) if ctrl==0 else alpha*tail[ctrl]
   C=add((1,C),(-q,log(p['R'][s>>3]*rd)))
 I,expected=formula(p,1);ck(C==expected)
 ck(I==sum(q*s.bit_count() for s,q in enumerate(P)))
 ck(I==sum(R(sum(tab[x]!=tab[x^(1<<j)] for x in range(N)),N) for j in range((N-1).bit_length())))
 fullfixtures+=1
boundary=[]
for d in (0,1):
 for m in (1,2):
  p={'A':R(0),'B':{},'d':R(d)};I,C=formula(p,m);lo,hi=interval(C)
  ck(4*I-hi>1);boundary.append({'d':d,'m':m,'surplus_lower':str(4*I-hi)})
ck(20**5<2**8*7**5);ck(2*13**4<16**4)
# Independent all-pairs flag review. Every tree's leaf transcript is built
# from actual two-bit inputs, with a common auxiliary thinning parameter.
histories=0
for ca,cb in product(range(16),repeat=2):
 D=[int(bool(ca>>x&1)!=bool(cb>>x&1)) for x in range(4)];d=R(sum(D),4)
 trees=[None]+[(i,mask) for i in (0,1) for mask in range(4)]
 for tree in trees:
  leaves=[];nodes=[]
  if tree is None:leaves=[list(range(4))]
  else:
   i,mask=tree;nodes=[list(range(4))]
   for bit in (0,1):
    cell=[x for x in range(4) if (x>>i)&1==bit]
    if (mask>>bit)&1:
     nodes.append(cell);leaves.extend([[x] for x in cell])
    else:leaves.append(cell)
  for t in (R(0),R(1,4),R(1)):
   J=add((1,h(t*d)),*[( -R(len(cell),4),h(t*R(sum(D[x] for x in cell),len(cell)))) for cell in leaves])
   aug=add((t,h(d)),*[( -t*R(len(cell),4),h(R(sum(D[x] for x in cell),len(cell)))) for cell in leaves])
   ck(nonnegative(J));ck(nonnegative(add((1,aug),(-1,J))))
   ck(nonnegative(add((t,h(d)),(-1,J))))
   # Decrements along the actual reached nodes sum to the same joint MI.
   chain={}
   for cell in nodes:
    if len(cell)==4:
     cuts=[[x for x in cell if (x>>tree[0])&1==v] for v in (0,1)]
    else:cuts=[[x] for x in cell]
    chain=add((1,chain),(R(len(cell),4),h(t*R(sum(D[x] for x in cell),len(cell)))),*[( -R(len(cut),4),h(t*R(sum(D[x] for x in cut),len(cut)))) for cut in cuts])
   ck(chain==J);histories+=1
ck(histories==6912);ck(fullfixtures==3);ck(len(stats)==1023)
out={'status':'PASS','assertions':checks,'core_nodes':1023,'core_queries':511,'full_reference_fixtures':fullfixtures,'review_histories':histories,'reference_normalizer':str(Z),'positive_core_excess_interval':[str(positive_lo),str(positive_hi)],'positive_core_excess_upper':'7/12','root_source_surplus_interval':[str(rootlo),str(roothi)],'children':children,'relevant_bad_rows':bad_rows,'terminal_endpoint_certificates':boundary,'all_m_payment':{'single_owner':'actual first child Y0=0, original probability1/2','original_bank':'5/8 < (1/2)(4I_child-C_child)','cumulative_core_plus_single_flag_bound':'<7/12+1/128<3/5','remaining':'greater than1/40','no_reset':True},'elapsed_seconds':time.monotonic()-start,'spec_sha256':hashlib.sha256((RUN/'FROZEN_CERTIFICATE_SPEC_V2.json').read_bytes()).hexdigest(),'arithmetic':'Fraction and prime-log identities with rigorous atanh intervals'}
(RUN/'out/CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['positive_core_excess_interval','root_source_surplus_interval','children','relevant_bad_rows','terminal_endpoint_certificates']}))
