from pathlib import Path
from fractions import Fraction as F
import json, time, math, hashlib, sys
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic()
checks=0
def ck(x):
 global checks
 assert x
 checks+=1
def ln_int(x,N=18):
 x=F(x); shift=x.numerator.bit_length()-x.denominator.bit_length()
 x=x/(F(2)**shift)
 if x<1: x*=2; shift-=1
 grid=2**96; q=(x.numerator*grid)//x.denominator
 low=F(q,grid); high=F(q+1,grid)
 def series(v):
  t=(v-1)/(v+1); s=sum((t**(2*j+1)/F(2*j+1) for j in range(N)),F(0))*2
  return s,s+2*t**(2*N+1)/((2*N+1)*(1-t*t))
 if x-1<F(1,2**80):
  u=x-1;lo=u-u*u/2;hi=u
 else:
  lo=series(low)[0]; hi=series(high)[1]
 l2,h2=series(F(2))
 return (lo+shift*l2,hi+shift*h2) if shift>=0 else (lo+shift*h2,hi+shift*l2)
def log2_int(x):
 a,b=ln_int(x); c,d=ln_int(F(2)); vals=[a/c,a/d,b/c,b/d]
 return min(vals),max(vals)
def ent_int(x):
 if not x: return F(0),F(0)
 a,b=log2_int(1/x); return x*a,x*b
def h_int(x):
 a,b=ent_int(x); c,d=ent_int(1-x); return a+c,b+d
def midpoint(z): return float((z[0]+z[1])/2)
def entropy(v): return sum(-float(p)*math.log2(float(p)) for p in v if p)
def walsh(a):
 a=list(a); j=1
 while j<len(a):
  for base in range(0,len(a),2*j):
   for q in range(base,base+j):
    u,v=a[q],a[q+j]; a[q],a[q+j]=u+v,u-v
  j*=2
 return a
def conditional(P,i):
 B=0.; mi=F(0); seen=set()
 for s in range(len(P)):
  if s&(1<<i): mi+=P[s]
  t=s&~(1<<i)
  if t in seen: continue
  seen.add(t); a,b=P[t],P[t|(1<<i)]; z=a+b
  if z: B+=float(z)*entropy([a/z,b/z])
 return mi,B
def block_v(w,d):
 v=[F(1)]
 for j in range(1,w+1):
  v.append((4*d*(1-d))**j*(1-F(2)**(2-j)*(1-d)**(w-j))**2)
 Z=sum(math.comb(w,j)*v[j] for j in range(w+1))
 ints=[ent_int(v[j]) for j in range(1,w+1)]
 T=(sum(math.comb(w,j)*ints[j-1][0] for j in range(1,w+1))/Z,sum(math.comb(w,j)*ints[j-1][1] for j in range(1,w+1))/Z)
 return v,Z,T
v,Z,T3=block_v(3,F(1,4)); ck(Z==F(319,256))
H3=entropy([F(9,16)]+[F(1,16)]*7)
K3=(3*h_int(F(1,4))[0]-F(0),3*h_int(F(1,4))[1])
H3i=tuple(sum(ent_int(p)[j] for p in [F(9,16)]+[F(1,16)]*7) for j in (0,1))
K3=(K3[0]-H3i[1],K3[1]-H3i[0]); ck(K3[0]>0); ck(T3[0]>0)
out={'addressing':[],'tribes':[],'bent_direct':[],'bent_grouped':[]}
for a in [1,2,3,4]:
 m=2**a; w=F(m-1,m)**(m-1); ks=tuple(-x for x in reversed(log2_int(w)))
 ck(ks[0]>0)
 # character orthogonality checked exactly, giving C(U)=w*1[U=0].
 for V in range(m): ck(sum((-1)**((V&b).bit_count()) for b in range(m))==(m if V==0 else 0))
 Tc=2*midpoint(ks)+midpoint(T3)
 out['addressing'].append({'a':a,'support_mass':str(w),'Z':str(w*w*Z),'H':2*a+H3,'TC':midpoint(ks)+midpoint(K3),'K_support':midpoint(ks),'K_shape':midpoint(K3),'T':Tc,'T_over_H':Tc/(2*a+H3)})
for w in [2,3,4,6,8,12,16,24,32]:
 p=F(1,2**w); t=w; b=(1-p)**t; d=2*p*(1-p)**(t-1)
 if b<=F(1,2): continue
 vv,zz,tt=block_v(w,d); M=t*w*midpoint(h_int(d)); I=t*w*d
 e=(2*b-1)**2; mass=4*b*(1-b)
 H=midpoint(ent_int(e))-float(mass)*midpoint(log2_int(4*b*b))+float(8*b*t*p)*midpoint(log2_int((1-p)/p))
 ck(sum([e,mass])==1); ck(zz>=1); ck(tt[0]>=0)
 out['tribes'].append({'w':w,'t':t,'I':float(I),'H_over_I':H/float(I),'T_over_4I':t*midpoint(tt)/(4*float(I)),'M_minus_T4_over_I':(M-t*midpoint(tt)/4)/float(I),'TC_minus_T4_over_I':(M-H-t*midpoint(tt)/4)/float(I),'Z_block_float_illustrative':float(zz),'Z_block_sha256':hashlib.sha256((str(zz.numerator)+':'+str(zz.denominator)).encode()).hexdigest(),'support_mass':'1'})
for k in [2,4]:
 n=3*k+1; N=2**n; p=F(1,2**(2*k)); delta=F(1,2**k); dd=p*delta
 vals=[]
 for x in range(N):
  data=x&((1<<k)-1); control=(x>>k)&((1<<(2*k))-1); y=x>>(3*k)
  b=(-1)**sum(((data>>(2*j))&1)*((data>>(2*j+1))&1) for j in range(k//2))
  vals.append(1 if control else (b if not(y and data==0) else -1))
 W=walsh(vals); P=[F(z*z,N*N) for z in W]; ck(sum(P)==1)
 metrics=[]
 for i in range(n):
  d,B=conditional(P,i); direct=F(sum(vals[x]!=vals[x^(1<<i)] for x in range(N)),N); ck(d==direct)
  expected= p/F(2)+dd if i<k else (p*(1-F(1,2**(k//2))+delta) if i<3*k else dd)
  ck(d==expected); marginal=midpoint(h_int(d)); metrics.append({'i':i,'class':'data' if i<k else ('control' if i<3*k else 'selector'),'B_over_d':B/float(d),'MI_over_h':(marginal-B)/marginal})
 out['bent_direct'].append({'k':k,'n':n,'best_coordinate':min(metrics,key=lambda z:z['B_over_d']),'coordinate_metrics':metrics})
 # independent analytic signed coefficient formula, including all empty exceptions.
 small=walsh([(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2)) for x in range(2**k)])
 for s in range(N):
  T=s&((1<<k)-1); U=(s>>k)&((1<<(2*k))-1); Y=s>>(3*k)
  coeff=dd if Y else ((1 if T==0 and U==0 else 0)+p*(F(small[T],2**k)-(1 if T==0 else 0)-delta))
  ck(F(W[s],N)==coeff)
for k in [4,6,8,12,16,24,32]:
 p=F(1,2**(2*k)); delta=F(1,2**k); d=p*delta; s=F(1,2**(k//2)); N=2**(3*k)
 # Grouped selector packets: positive/negative nonempty data, empty data with U nonempty, all empty.
 pos=(2**k+2**(k//2))//2-1; neg=(2**k-2**(k//2))//2
 classes=[(pos*2**(2*k),p*(s-delta)),(neg*2**(2*k),p*(-s-delta)),(2**(2*k)-1,p*(s-1-delta)),(1,1+p*(s-1-delta))]
 ck(sum(mult*(m*m+d*d) for mult,m in classes)==1); ck(sum(mult*d*d for mult,m in classes)==d)
 lo=hi=F(0)
 for mult,m in classes:
  q=m*m+d*d; z=h_int(d*d/q); lo+=mult*q*z[0]; hi+=mult*q*z[1]
 hh=h_int(d); ck(lo>0); ck(hh[0]-hi>0)
 ck((hi-lo)/d<F(1,10**8))
 out['bent_grouped'].append({'k':k,'selector_B_over_d':midpoint((lo/d,hi/d)),'selector_B_over_d_interval_width':float((hi-lo)/d),'selector_MI_over_h':1-midpoint((lo,hi))/midpoint(hh),'selector_MI_over_B':(midpoint(hh)-midpoint((lo,hi)))/midpoint((lo,hi))})
out['checks']=checks; out['runtime_seconds']=time.monotonic()-start; out['log_certificate']='18-term rational atanh series after range reduction; outward analytic remainder'; out['illustrative_only']='Decimal-free floats of proven rational intervals or exact distributions; asymptotics proved in REPORT.md'
(ROOT/'out'/'verification.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'checks':checks,'runtime_seconds':out['runtime_seconds'],'output':'out/verification.json'}))
