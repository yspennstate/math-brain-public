from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,sys,time,hashlib,math

ROOT=Path(__file__).resolve().parents[1]
P=180; SCALE=1<<P; CHECKS=0
def check(a):
 global CHECKS
 assert a
 CHECKS+=1
def ceildiv(a,b): return -((-a)//b)
def mul(a,b): return (a[0]*b[0]//SCALE,ceildiv(a[1]*b[1],SCALE))
@lru_cache(None)
def ln(x):
 assert x>0
 n,d=x.numerator,x.denominator
 k=n.bit_length()-d.bit_length()
 if k>=0: y=Q(n,d<<k)
 else: y=Q(n<<(-k),d)
 if y<1: y*=2;k-=1
 if y>=2: y/=2;k+=1
 assert 1<=y<2
 z=(y-1)/(y+1); zz=(z.numerator*SCALE//z.denominator,ceildiv(z.numerator*SCALE,z.denominator))
 z2=mul(zz,zz); power=zz; lo=hi=0
 for j in range(100):
  lo+=2*power[0]//(2*j+1);hi+=ceildiv(2*power[1],2*j+1)
  power=mul(power,z2)
 # z<=1/3: positive-series tail <=3*z^201/201, enclosed by 3*power/201.
 hi+=ceildiv(3*power[1],201)
 if k:
  a,b=ln(Q(2)) if x!=2 else ln2_kernel()
  lo+=k*(a if k>0 else b);hi+=k*(b if k>0 else a)
 return lo,hi
def ln2_kernel():
 # Same finite series directly for z=1/3, avoiding range reduction recursion.
 z=Q(1,3);lo=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(100)),Q(0));hi=lo+3*z**201/201
 return lo.numerator*SCALE//lo.denominator,ceildiv(hi.numerator*SCALE,hi.denominator)
def times(iv,c):
 if c<0: return times((-iv[1],-iv[0]),-c)
 return (iv[0]*c.numerator//c.denominator,ceildiv(iv[1]*c.numerator,c.denominator))
def add(*args):return tuple(sum(x[i] for x in args) for i in [0,1])
def neg(iv):return -iv[1],-iv[0]
def eta(x):return (0,0) if not x else neg(times(ln(x),x))
def phi(a,b):return add(eta(a),eta(b),neg(eta(a+b)))
def rawd(x):return add(eta(x*x),neg(times(eta((x+1)**2),Q(1,2))),neg(times(eta((x-1)**2),Q(1,2))))
def bits(iv):
 a,b=ln(Q(2)); candidates=[Q(v,w) for v in iv for w in [a,b]]
 return min(candidates),max(candidates)
def serial(iv):
 a,b=bits(iv);return {'lo':str(a),'hi':str(b),'display':[float(a),float(b)]}
def fwht(vals):
 a=list(vals);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):u,v=a[k],a[k+h];a[k],a[k+h]=u+v,u-v
  h*=2
 return [Q(x,len(a)) for x in a]
def direct(vals):return [Q(sum(v*(-1)**((s&x).bit_count()) for x,v in enumerate(vals)),len(vals)) for s in range(len(vals))]
def H(vals,tf=fwht):return add(*(eta(x*x) for x in tf(vals)))
def exact_case(r,l,tf=fwht):
 p=Q(1,1<<r);b=1-p;e=b**l;N=1<<(r*l)
 K=[];E=[]
 for x in range(N):
  first=next((j for j in range(l) if (x>>(r*j))&((1<<r)-1)==0),None)
  E.append(int(first is None));K.append(0 if first is None else (-1)**(l-1-first))
 children=[[K[x]+s*E[x] for x in range(N)] for s in [1,-1]];f=children[0]+children[1]
 ks,es=map(tf,[K,E]); check(all(x in [-1,1] for x in f));check(sum(es[i]**2 for i in range(N))==e)
 check(Q(sum(children[0][i]!=children[1][i] for i in range(N)),N)==e)
 grouped={};S=(0,0);D=(0,0)
 for mask,(a,c) in enumerate(zip(ks,es)):
  if not c:check(a==0);continue
  j=max((j for j in range(l) if (mask>>(r*j))&((1<<r)-1)),default=-1)
  key=l-1-j if j>=0 else -1;ratio=a/c
  expected=((-1)**(l-1)*p*(1-(-b)**l)/((2-p)*e)) if key==-1 else (p-2*(-1)**key/b**key)/(2-p)
  check(ratio==expected);grouped[key]=grouped.get(key,Q(0))+c*c/e
  S=add(S,times(phi(a*a,c*c),1/e));D=add(D,times(rawd(ratio),c*c/e))
 check(grouped[-1]==e)
 for k in range(l):check(grouped[k]==p*b**k)
 actualD=times(add(H(f,tf),neg(times(add(H(children[0],tf),H(children[1],tf)),Q(1,2)))),1/e)
 check(not(actualD[1]<D[0] or D[1]<actualD[0]))
 comp=compressed(r,l)
 check(not(comp['B'][1]<S[0] or S[1]<comp['B'][0]));check(not(comp['D'][1]<D[0] or D[1]<comp['D'][0]))
 return {'r':r,'l':l,'n':r*l+1,'B_over_I':serial(S),'D_over_I':serial(D),'I':str(e),'terminal_entropies':[serial(H(c,tf)) for c in children]}
def compressed(r,l):
 p=Q(1,1<<r);b=1-p;e=b**l;S=D=(0,0)
 re=(-1)**(l-1)*p*(1-(-b)**l)/((2-p)*e)
 S=times(phi(re*re,Q(1)),e);D=times(rawd(re),e)
 moment=(0,0)
 for k in range(l):
  t=b**k;x=(p-2*(-1)**k/t)/(2-p);w=p*t
  S=add(S,times(phi(x*x,Q(1)),w));D=add(D,times(rawd(x),w))
  check(abs(x)>=1/t)
  moment=add(moment,times(ln(1/t),w))
 moment=add(moment,times(ln(1/e),e))
 expected=times(ln(1/b),b*(1-e)/p)
 check(not(moment[1]<expected[0] or expected[1]<moment[0]));check(moment[1]<SCALE)
 return {'r':r,'l':l,'n':r*l+1,'B':S,'D':D,'moment':moment,'I':f'((2^{r}-1)/2^{r})^{l}'}
def main(mode):
 start=time.perf_counter(); rows=[]
 if mode in ['pilot','reproduce']:
  for r,l in [(1,1),(1,2),(2,1),(2,2),(2,3)]:rows.append(exact_case(r,l,direct if mode=='reproduce' else fwht))
 else:
  for r,l in [(3,32),(4,128),(5,256),(6,512),(7,1024),(7,2048)]:
   a=compressed(r,l);rows.append({k:serial(v) if k in ['B','D'] else {'lo':str(Q(v[0],SCALE)),'hi':str(Q(v[1],SCALE))} if k=='moment' else v for k,v in a.items()})
   (ROOT/'out/PARTIAL_main.json').write_text(json.dumps({'rows':rows,'elapsed_s':time.perf_counter()-start}),encoding='utf-8')
  check(bits(a['D'])[0]>7)
 elapsed=time.perf_counter()-start;check(elapsed<55)
 result={'mode':mode,'status':'PASS','checks':CHECKS,'elapsed_s':elapsed,'precision_bits':P,'rows':rows,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (ROOT/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps({'mode':mode,'status':'PASS','checks':CHECKS,'elapsed_s':elapsed,'ratios':[(x['r'],x['l'],x.get('D',x.get('D_over_I'))['display']) for x in rows]}))
if __name__=='__main__':main(sys.argv[1])
