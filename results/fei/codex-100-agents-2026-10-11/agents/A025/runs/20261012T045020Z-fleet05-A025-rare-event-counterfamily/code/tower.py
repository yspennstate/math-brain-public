"""Exact compressed Fourier and physical face ledgers for nested bent-flip events."""
from collections import Counter
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path
import json,time,sys
R=Path(__file__).resolve().parents[1]
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
START=time.monotonic(); LIMIT=60 if MODE=='pilot' else 1800
CHECKS=0; SCALE=1<<100; SIGNS={}; LOGS={}

def ck(ok):
 global CHECKS
 assert ok
 CHECKS+=1

def guard():
 if time.monotonic()-START>LIMIT:raise TimeoutError('frozen cap')

def fwht(a):
 a=list(a);h=1
 while h<len(a):
  for s in range(0,len(a),2*h):
   for j in range(s,s+h):u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
  h*=2
 return a

def inf(table):
 N=len(table);n=N.bit_length()-1
 return F(sum(table[x]!=table[x^(1<<i)] for x in range(N) for i in range(n)),N)

def atan_log(x):
 z=(x-1)/(x+1);p=z;total=F(0)
 for j in range(40):total+=2*p/(2*j+1);p*=z*z
 return total,total+2*p/(81*(1-z*z))
LN2=atan_log(F(2))

@lru_cache(maxsize=8192)
def log2_interval(x):
 assert x>0
 e=x.bit_length()-1
 if x==1<<e:return e*SCALE,e*SCALE
 lo,hi=atan_log(F(x,1<<e));lo=e+lo/LN2[1];hi=e+hi/LN2[0]
 lo=lo*SCALE;hi=hi*SCALE
 ans=(lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator))
 LOGS[str(x)]=[str(v) for v in ans]
 return ans

def sign(expr):
 key=tuple(sorted((x,c) for x,c in expr.items() if c and x!=1))
 if key in SIGNS:return SIGNS[key]['sign']
 lo=hi=0
 for x,c in key:
  a,b=log2_interval(x)
  if c>=0:lo+=c*a;hi+=c*b
  else:lo+=c*b;hi+=c*a
 if not key:s=0
 elif lo>0:s=1
 elif hi<0:s=-1
 else:
  # Exact equality/sign fallback only on the compressed local logarithm expression.
  num=den=1
  if sum(abs(c)*x.bit_length() for x,c in key)>200000:
   raise ArithmeticError('unresolved interval; no expensive power fallback')
  for x,c in key:
   if c>0:num*=pow(x,c)
   else:den*=pow(x,-c)
  s=(num>den)-(num<den)
 SIGNS[key]={'sign':s,'lo':str(lo),'hi':str(hi),'method':'exact_zero' if not key else 'interval' if lo>0 or hi<0 else 'integer_product','expression':[[str(x),str(c)] for x,c in key]}
 return s

# A block is (k, assigned-data mask, data values, selector -1/0/1, live controls, inactive).
@lru_cache(maxsize=4096)
def local(block):
 k,mask,val,y,r,off=block
 live=[i for i in range(k) if not mask>>i&1];n=len(live)+(y==-1)
 D=[];M=[]
 for t in range(1<<n):
  x=val
  for j,i in enumerate(live):x|=((t>>j)&1)<<i
  yy=(t>>len(live))&1 if y==-1 else y
  parity=sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2))%2
  D.append(parity);M.append(int(x==0 and yy==1))
 ck(all(not (a and b) for a,b in zip(D,M)))
 return tuple(D),tuple(M),tuple(fwht(D)),tuple(fwht(M)),n

@lru_cache(maxsize=8192)
def moments(state):
 if not state:return F(1),F(0),F(0),0
 prev=state[:-1];block=state[-1];p,i,q,np=moments(prev)
 D,M,_,_,nl=local(block);N=1<<nl
 nd=nl+block[4]+np
 if block[5]:return F(0),F(0),F(0),nd
 a=F(1,1<<block[4]);d=F(sum(D),N);m=F(sum(M),N)
 f0=[1-2*x for x in D];f1=[1-2*(x+y) for x,y in zip(D,M)]
 il=(1-p)*inf(f0)+p*inf(f1)
 # Q local is affine in the previous event: compute its two endpoint face laws.
 def Qlocal(f):
  n=nl;faces=0
  for u in range(n):
   for v in range(u):
    for x in range(N):
     if x&((1<<u)|(1<<v)):continue
     faces+=f[x]*f[x^(1<<u)]*f[x^(1<<v)]*f[x^(1<<u)^(1<<v)]==-1
  return F(2*faces,N)
 ql=(1-p)*Qlocal(f0)+p*Qlocal(f1)
 # Mixed local/previous faces use the boundary of M (the switching region).
 total_local_I=il+m*i
 total_local_Q=ql+m*q+inf([1-2*x for x in M])*i/2
 r=block[4];mean=d+m*p
 return a*mean,a*(total_local_I+2*r*mean),a*(total_local_Q+r*total_local_I+r*(r-1)*mean),nd

@lru_cache(maxsize=4096)
def joint_hist(g,h):
 """Histogram of paired integer Fourier sums of E_g,E_h excluding empty row."""
 if not g:return (), (1,1),0
 hist,empty,np=joint_hist(g[:-1],h[:-1]);G=g[-1];H=h[-1]
 Dg,Mg,Wdg,Wmg,nl=local(G);Dh,Mh,Wdh,Wmh,nlh=local(H)
 ck(nl==nlh and G[4]==H[4]);r=G[4];copies=1<<r
 ag=0 if G[5] else 1;ah=0 if H[5] else 1
 local_groups=Counter(zip(Wdg,Wmg,Wdh,Wmh));out=Counter()
 for (d1,m1,d2,m2),count in local_groups.items():
  for (u,v),mult in hist:out[(ag*m1*u,ah*m2*v)]+=count*copies*mult
  out[(ag*(d1*(1<<np)+m1*empty[0]),ah*(d2*(1<<np)+m2*empty[1]))]+=count*copies
 emp=(ag*(Wdg[0]*(1<<np)+Wmg[0]*empty[0]),ah*(Wdh[0]*(1<<np)+Wmh[0]*empty[1]))
 out[emp]-=1
 if not out[emp]:del out[emp]
 n=np+nl+r
 ck(sum(out.values())==(1<<n)-1)
 return tuple(out.items()),emp,n

def split(state,c):
 layer,kind,index=c;block=list(state[layer]);g=list(state);h=list(state)
 if kind=='x':
  ck(not block[1]>>index&1)
  b0=block[:];b1=block[:];b0[1]|=1<<index;b1[1]|=1<<index;b1[2]|=1<<index
 elif kind=='y':
  ck(block[3]==-1);b0=block[:];b1=block[:];b0[3]=0;b1[3]=1
 else:
  ck(block[4]>0);b0=block[:];b1=block[:];b0[4]-=1;b1[4]-=1;b1[5]=1
 g[layer]=tuple(b0);h[layer]=tuple(b1)
 return tuple(g),tuple(h)

def product_moments(state,c):
 """d=Pr(E_g xor E_h), and I(1-2(E_g xor E_h))/2, from local tables."""
 g,h=split(state,c);layer=c[0]
 p,ip,_,_=moments(state[:layer]);G=g[layer];H=h[layer]
 Dg,Mg,_,_,nl=local(G);Dh,Mh,_,_,_=local(H);N=1<<nl
 W0=[(0 if G[5] else a)^(0 if H[5] else b) for a,b in zip(Dg,Dh)]
 W1=[(0 if G[5] else a+m)^(0 if H[5] else b+v) for a,m,b,v in zip(Dg,Mg,Dh,Mh)]
 mean=(1-p)*F(sum(W0),N)+p*F(sum(W1),N)
 il=(1-p)*inf([1-2*x for x in W0])+p*inf([1-2*x for x in W1])
 change=F(sum(x!=y for x,y in zip(W0,W1)),N)
 r=G[4];a=F(1,1<<r)
 d=a*mean;ii=a*(il+change*ip+2*r*mean)
 for B in state[layer+1:]:
  D,M,_,_,nl=local(B)
  if B[5] or not sum(M):d=F(0);ii=F(0);continue
  gate=F(sum(M),len(M)*(1<<B[4]))
  # M is a point mask on live data and selector, multiplied by point controls.
  Rgate=B[4]+nl
  ii=gate*(ii+2*Rgate*d);d*=gate
 return d,ii/2

def badness(g,h,d):
 hist,empty,n=joint_hist(g,h);N=1<<n
 coeffs=[((-2*u,-2*v),count) for (u,v),count in hist]
 coeffs.append(((N-2*empty[0],N-2*empty[1]),1))
 expr=Counter();dn=0;norm=0
 for (u,v),count in coeffs:
  A=(u+v)**2;B=(u-v)**2;T=A+B;dn+=count*B;norm+=count*T
  for x,c in [(T,T),(A,-A),(B,-B)]:
   if x:expr[x]+=count*c
 ck(norm==(2*N)**2);ck(F(dn,(2*N)**2)==d)
 expr[2]-=4*dn
 return sign(expr)>0

def orders(k,r,L):
 layers=list(reversed(range(L)))
 xs=[(j,'x',i) for j in layers for i in range(k)]
 ys=[(j,'y',0) for j in layers]
 zs=[(j,'z',i) for j in layers for i in range(r)]
 return {'selector_first':ys+zs+xs,'control_first':zs+ys+xs,'data_first':xs+zs+ys,'control_data_selector':zs+xs+ys}

def ledger(state,order):
 @lru_cache(maxsize=4096)
 def visit(st,pos):
  guard();p,ii,qq,n=moments(st)
  if p in (0,1):return F(0),F(0),F(0),0,0
  c=order[pos];g,h=split(st,c);d,credit=product_moments(st,c)
  if not d:return visit(g,pos+1)
  isbad=badness(g,h,d)
  l=visit(g,pos+1);rr=visit(h,pos+1)
  res=(d+(l[0]+rr[0])/2,credit+(l[1]+rr[1])/2,(credit if isbad else 0)+(l[2]+rr[2])/2,int(isbad)+l[3]+rr[3],1+l[4]+rr[4])
  ck(res[0]==ii);ck(res[1]==qq)
  return res
 result=visit(state,0)
 return {'I':str(result[0]),'Q':str(result[1]),'bad_credit':str(result[2]),'ratio':str(result[2]/result[0]),'bad_nodes_DAG':result[3],'live_nodes_DAG':result[4],'cache':str(visit.cache_info())}

def state_initial(k,r,L):return tuple((k,0,0,-1,r,0) for _ in range(L))

def truth(state,x):
 e=1;offset=0
 for block in state:
  D,M,_,_,nl=local(block);r=block[4]
  localx=(x>>offset)&((1<<nl)-1);offset+=nl
  control=(x>>offset)&((1<<r)-1);offset+=r
  e=0 if block[5] or control else D[localx]+M[localx]*e
 return 1-2*e

def validate_small():
 # Independent full-cube transforms/edge/face enumeration, including restricted states.
 for k,r,L in [(2,0,1),(2,1,2),(2,0,3),(4,0,2)]:
  st=state_initial(k,r,L);n=moments(st)[3];N=1<<n
  vals=[truth(st,x) for x in range(N)];w=fwht(vals)
  p,ii,qq,_=moments(st)
  ck(p==F(sum(v==-1 for v in vals),N));ck(ii==inf(vals))
  faces=sum(vals[x]*vals[x^(1<<u)]*vals[x^(1<<v)]*vals[x^(1<<u)^(1<<v)]==-1 for u in range(n) for v in range(u) for x in range(N) if not x&((1<<u)|(1<<v)))
  ck(qq==F(2*faces,N))
  hist,empty,_=joint_hist(st,st)
  actual=Counter((-a//2,-a//2) for a in w[1:]);ck(dict(hist)==dict(actual));ck(empty==((N-w[0])//2,)*2)
  # Every root coordinate: match paired children spectra and direct product boundaries.
  coords=[];bit=0
  for j,B in enumerate(st):
   coords.extend(((j,'x',i),bit+i) for i in range(k));bit+=k
   coords.append(((j,'y',0),bit));bit+=1
   coords.extend(((j,'z',i),bit+i) for i in range(r));bit+=r
  for c,i in coords:
   g,h=split(st,c);d,credit=product_moments(st,c)
   gv=[];hv=[]
   for x in range(N//2):
    y=(x&((1<<i)-1))|((x>>i)<<(i+1));gv.append(vals[y]);hv.append(vals[y|(1<<i)])
   ck(d==F(sum(a!=b for a,b in zip(gv,hv)),N//2));ck(credit==inf([a*b for a,b in zip(gv,hv)])/2)
   ghist,gempty,_=joint_hist(g,h);gw=fwht(gv);hw=fwht(hv)
   direct=Counter((-a//2,-b//2) for a,b in zip(gw[1:],hw[1:]));ck(dict(ghist)==dict(direct));ck(gempty==((N//2-gw[0])//2,(N//2-hw[0])//2))

if __name__=='__main__':
 cases=[(2,1,2)] if MODE=='pilot' else [(k,r,L) for k in (2,4,6) for r in (0,1,2) for L in (1,2,3)]+[(k,2*k,L) for k in (4,6) for L in (2,3)]
 rows=[]
 if MODE=='pilot':validate_small()
 with (R/'out'/f'{MODE}_ROWS.jsonl').open('w',encoding='utf-8') as fp:
  for k,r,L in cases:
   st=state_initial(k,r,L);p,ii,qq,n=moments(st)
   row={'k':k,'r':r,'depth':L,'n':n,'negative_probability':str(p),'I':str(ii),'Q':str(qq),'orders':{}}
   for name,order in orders(k,r,L).items():row['orders'][name]=ledger(st,tuple(order))
   ck(all(F(v['I'])==ii and F(v['Q'])==qq for v in row['orders'].values()))
   rows.append(row);fp.write(json.dumps(row)+'\n');fp.flush()
   (R/'out'/f'{MODE}_CHECKPOINT.json').write_text(json.dumps({'finished_cases':len(rows),'seconds':time.monotonic()-START,'last_row':row},indent=2))
   print(json.dumps({'k':k,'r':r,'depth':L,'ratios':{name:v['ratio'] for name,v in row['orders'].items()}}),flush=True)
   guard()
 result={'mode':MODE,'family_cases':len(rows),'tree_ledgers':4*len(rows),'assertions_passed':CHECKS,'seconds':time.monotonic()-START,'rows':rows,'scale':str(SCALE),'sign_certificates':list(SIGNS.values()),'log_intervals':LOGS,'terminal_entropy':'zero: constant leaves'}
 (R/'out'/f'{MODE}_RESULTS.json').write_text(json.dumps(result,indent=2))
 print(json.dumps({k:v for k,v in result.items() if k not in ('rows','sign_certificates','log_intervals')}))
