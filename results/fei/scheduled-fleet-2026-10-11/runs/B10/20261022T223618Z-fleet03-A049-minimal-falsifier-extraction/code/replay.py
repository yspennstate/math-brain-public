"""Different entropy representation, independently coded logs and direct tables."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,hashlib
out=Path(__file__).resolve().parents[1]/'out';start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x;checks+=1
def plus(*a):return sum((x[0] for x in a),Q()),sum((x[1] for x in a),Q())
def times(a,k):return (k*a[0],k*a[1]) if k>=0 else (k*a[1],k*a[0])
def product(a,b):
 vals=[x*y for x in a for y in b];return min(vals),max(vals)
def rawlog(x):
 u=(x-1)/(x+1);s=Q();p=u
 for j in range(40):s+=p/(2*j+1);p*=u*u
 return 2*s,2*s+2*p/(81*(1-u*u))
unit=rawlog(Q(2))
@lru_cache(None)
def lg(x):
 x=Q(x);ck(x>0);k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 a,b=rawlog(x);return Q(k)+a/unit[1],Q(k)+b/unit[0]
def ph(x):return times(lg(x),-x) if x else (Q(),Q())
def ent(p):return plus(*(ph(x) for x in p if x))
def hb(x):return plus(ph(x),ph(1-x))
def hbrange(a,b):
 aa,bb=hb(a),hb(b)
 return min(aa[0],bb[0]),Q(1) if a<=Q(1,2)<=b else max(aa[1],bb[1])
def interval(v):
 d=10**12
 return [str(Q(v[0].numerator*d//v[0].denominator,d)),str(Q(-((-v[1].numerator*d)//v[1].denominator),d))]
w=json.loads((out/'WITNESS.json').read_text(encoding='utf-8'));lo,hi=map(Q,w['c']);r,m=w['r'],w['m'];ck((r,m)==(3,9))
delta=Q(1,8);mu=Q(3,4)**9;t=(1-mu)/2;p0=(1-t)**2/4;v=1-p0
groups=[(Q(1,2),2),(t/2,1),(Q(1,16),27)]
def pol(c):
 p=Q(1)
 for d,n in groups:p*=(1-c*d/v)**n
 return p-(1-c)
ck(pol(lo)<0<pol(hi));ck(0<lo<hi<1)
sumh=plus(*(times(hbrange(lo*d/v,hi*d/v),n) for d,n in groups))
hc=hbrange(lo,hi);difference=plus(sumh,times(hc,-1))
CE=plus(hb(v),product((v/hi,v/lo),difference))
I=1+t/2+Q(27,16);excess=plus(CE,(-4*I,-4*I))
ck(excess[0]>Q(1,6) and excess[1]<Q(3,16))
original=list(map(Q,w['CE']));ck(CE[0]<=original[1] and original[0]<=CE[1])
hp=ent([Q(9,16)]+[Q(1,16)]*7);Hh=times(hp,9)
H0=plus((Q(2),Q(2)),times(plus(ph((1-t)**2),ph(t*t),times(plus(Hh,times(ph(mu*mu),-1)),Q(1,2)),(4*t*(1-t),4*t*(1-t))),Q(1,2)))
Hf=plus((Q(9,4),Q(9,4)),times(hp,2));If=Q(21,8);R=I-If
S=plus((4*If,4*If),times(Hf,-1));A=plus(CE,times(H0,-1));edge=plus(H0,times(Hf,-1),(-4*R,-4*R));ck(edge[0]>0)
liability=plus(A,edge);short=plus(liability,times(S,-1));ck(short[0]>Q(1,6));ck(H0[1]<8 and H0[1]<4*I)
small=[]
for rr,mm in [(1,1),(2,1),(2,2),(3,1),(3,2)]:
 n=3+rr*mm;N=1<<n
 def core(z):
  sign=1
  for j in range(mm):
   if (z>>(rr*j))&((1<<rr)-1)==(1<<rr)-1:sign=-sign
  return sign
 table=[(-1 if u&2 else 1) if not u&1 else core(u>>3) if u&4 else 1 for u in range(N)]
 # Direct character summation, no Walsh helper or tensor spectrum assumed.
 mass=[Q(sum(table[u]*(-1)**((s&u).bit_count()) for u in range(N))**2,N*N) for s in range(N)]
 ck(sum(mass)==1)
 ds=[sum((mass[s] for s in range(N) if s>>j&1),Q()) for j in range(n)]
 dd=Q(1,1<<rr);tt=(1-(1-2*dd)**mm)/2
 ck(ds==[Q(1,2),Q(1,2),tt/2]+[dd/2]*(rr*mm));ck(mass[0]==(1-tt)**2/4)
 for j in range(n):ck(ds[j]==Q(sum(table[u]!=table[u^(1<<j)] for u in range(N)),N))
 pp=ent([(1-2*dd)**2]+[4*dd*dd]*((1<<rr)-1));mh=times(pp,mm);muu=(1-2*dd)**mm
 formula=plus((Q(2),Q(2)),times(plus(ph((1-tt)**2),ph(tt*tt),times(plus(mh,times(ph(muu*muu),-1)),Q(1,2)),(4*tt*(1-tt),4*tt*(1-tt))),Q(1,2)))
 actual=ent(mass);ck(actual[0]<=formula[1] and formula[0]<=actual[1])
 small.append({'r':rr,'m':mm,'n':n,'table_sha256':hashlib.sha256(bytes(x+1 for x in table)).hexdigest()})
result={'status':'PASS','assertions':checks,'elapsed_seconds':time.perf_counter()-start,'representation':'H(Q)=h2(v)+(v/c)*(sum_i h2(c*Inf_i/v)-h2(c)); independently coded 40-term rational logarithms','CE':interval(CE),'excess':interval(excess),'H0':interval(H0),'Hf':interval(Hf),'I':str(I),'If':str(If),'R':str(R),'unused_terminal_S4':interval(S),'source_A':interval(A),'signed_query_deficit':interval(edge),'complete_liability_minus_S4':interval(short),'small_direct_tables':small}
(out/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
circuit={'type':'exact Boolean straight-line circuit','variables':['x','a','b']+[f'z{j}' for j in range(27)],'bit_domain':[0,1],'sign_output_domain':[-1,1],'gates':[{'name':f'q{j}','op':'AND','inputs':[f'z{3*j+k}' for k in range(3)]} for j in range(9)]+[{'name':'hbit','op':'XOR','inputs':[f'q{j}' for j in range(9)]},{'name':'selected','op':'AND','inputs':['b','hbit']},{'name':'fbit','op':'MUX','selector':'x','zero':'a','one':'selected'}],'sign_output':'1-2*fbit','truth_table_order':'LSB order x,a,b,z0,...,z26','normalizer_definition':'unique c in witness rational bracket satisfying product(1-c*Inf_i/v)=1-c','enumerate_truth_table':False}
(out/'CIRCUIT.json').write_text(json.dumps(circuit,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
