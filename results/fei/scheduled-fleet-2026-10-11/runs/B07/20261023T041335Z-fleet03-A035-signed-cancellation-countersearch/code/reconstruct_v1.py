"""Independent truth-table/FWHT and unrounded rational log reconstruction."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time,hashlib
R=Path(__file__).resolve().parents[1];COUNT=0;CACHE={}
def ck(v):
 global COUNT
 assert v;COUNT+=1
def ln(x):
 t=(x-1)/(x+1);power=t;s=F(0)
 for j in range(24):s+=power/(2*j+1);power*=t*t
 return 2*s,2*s+2*power/(49*(1-t*t))
def log(x):
 if x not in CACHE:
  k=x.numerator.bit_length()-x.denominator.bit_length();z=x/F(2)**k
  if z<1:k-=1;z*=2
  a,b=ln(z);c,d=ln(F(2));CACHE[x]=(k+a/d,k+b/c)
 return CACHE[x]
def add(*vs):return sum(v[0] for v in vs),sum(v[1] for v in vs)
def mul(v,c):return (v[0]*c,v[1]*c) if c>=0 else (v[1]*c,v[0]*c)
def sub(a,b):return add(a,mul(b,-1))
def avg(vs):return mul(add(*vs),F(1,len(vs)))
def overlap(v,w):ck(v[0]<=F(w[1]) and F(w[0])<=v[1])
def H(p):return add(*(mul(log(v),-v) for v in p.values() if v))
def marg(p,i):
 q={}
 for s,v in p.items():q[s&~(1<<i)]=q.get(s&~(1<<i),F(0))+v
 return q
def fair(p,i):
 q=marg(p,i);return {s|b:v/2 for s,v in q.items() for b in [0,1<<i]}
def CE(p,q):
 ck(sum(q.values())==1)
 ts=[]
 for s,v in p.items():
  if v:ck(q.get(s,0)>0);ts.append(mul(log(q[s]),-v))
 return add(*ts)
def B(p,i):return sub(H(p),H(marg(p,i)))
def cmi(p,i,j):return sub(add(H(marg(p,i)),H(marg(p,j))),add(H(p),H(marg(marg(p,i),j))))
def spectrum(L,h):
 n=2*L+4;fixed=dict(h);free=[i for i in range(n) if i not in fixed]
 blocks=[(1<<3)|1|4,(((1<<L)-1)<<4)|1|2,(((1<<L)-1)<<(4+L))|2|4]
 vals=[]
 for v in range(1<<len(free)):
  full=sum(b<<i for i,b in fixed.items())|sum(((v>>j)&1)<<i for j,i in enumerate(free))
  vals.append(2*int(all(full&e for e in blocks))-1)
 step=1
 while step<len(vals):
  for base in range(0,len(vals),2*step):
   for j in range(step):a,b=vals[base+j],vals[base+j+step];vals[base+j]=a+b;vals[base+j+step]=a-b
  step*=2
 a={sum(((s>>j)&1)<<i for j,i in enumerate(free)):F(v,len(vals)) for s,v in enumerate(vals)}
 p={s:v*v for s,v in a.items()};ck(sum(p.values())==1)
 return a,p
def case(L,main):
 z=4+L;roota,p=spectrum(L,());M=[]
 for i in range(2*L+4):
  r=marg(p,i)
  M.append(add(*(mul(log(r[s&~(1<<i)]/v),v) for s,v in p.items() if s>>i&1 and v)))
 Ip=sum(v for s,v in p.items() for i in [3]+list(range(4,2*L+4)) if s>>i&1)
 if L==1:
  for shift in range(1<<(2*L+4)):ck(sum(v*roota[s^shift] for s,v in roota.items())==int(shift==0))
 bx=B(p,3);bb=[];third=[];fourth=[];old=[];pos=[]
 for s in [0,1]:bb.append(B(spectrum(L,((3,s),))[1],1))
 for s,t in product([0,1],repeat=2):
  h=((3,s),(1,t));pa=spectrum(L,h)[1];old.append(CE(pa,fair(pa,0)));bills=[];ces=[]
  for u in [0,1]:
   hy=h+((4,u),);ya,yp=spectrum(L,hy);q=fair(yp,2);ces.append(CE(yp,q));fresh=[];inc=[]
   for v in [0,1]:
    leaf=hy+((z,v),);a,pf=spectrum(L,leaf)
    for S in a:ck(a[S]==ya[S]+(1 if v==0 else -1)*ya[S|(1<<z)])
    f=CE(pf,fair(pf,0));fresh.append(f);inc.append(CE(pf,marg(q,z)))
    mt=main['parents'][2*s+t]['terminals'][2*u+v];overlap(f,mt['CE']);overlap(H(pf),mt['H'])
   net=sub(add(B(yp,z),avg(fresh)),CE(yp,q));rho=cmi(yp,z,2);delta=sub(avg(fresh),avg(inc))
   mn=main['parents'][2*s+t]['fourth_nodes'][u]
   for val,key in [(net,'net'),(rho,'rho'),(delta,'Delta')]:overlap(val,mn[key])
   if L==2 and (s,t,u)==(1,0,1):
    ck(net[0]>F(1,10));pos.append(dict(net=[str(x) for x in net],Delta=[str(x) for x in delta],rho=[str(x) for x in rho]))
   bills.append(add(B(yp,z),avg(fresh)))
  fourth.append(add(B(pa,4),avg(bills)));third.append(add(B(pa,4),avg(ces)))
 prefix=add(add(*M),bx,avg(bb));bill=add(prefix,avg(fourth));spare=sub((17*Ip,17*Ip),bill)
 overlap(bill,main['fourth_bill']);overlap(add(prefix,avg(third)),main['third_bill']);ck(spare[0]>F(1,32));ck(Ip==F(main['I_private']))
 return dict(L=L,positive_witness=pos,spare=[str(x) for x in spare])
if __name__=='__main__':
 spec=dict(helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),domain=[1,2,3],case_count=3,max_runtime_seconds=55,memory_estimate_MB=90,arithmetic='Truth table integer FWHT; independent 24-term rational logs without outward rounding',symmetry='None')
 (R/'out/REPRO_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
 start=time.monotonic();main=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'));records=[]
 for L in [1,2,3]:records.append(case(L,next(r for r in main['cases'] if r['L']==L)));ck(time.monotonic()-start<55)
 ans=dict(records=records,checks=COUNT,runtime_seconds=time.monotonic()-start)
 (R/'out/REPRODUCE.json').write_text(json.dumps(ans,indent=2),encoding='utf-8')
 print(json.dumps(dict(checks=COUNT,seconds=ans['runtime_seconds'],positive_net_exceeds='1/10')))
