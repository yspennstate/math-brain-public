from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,argparse
R=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
start=time.perf_counter();checks=0
NEG={0,1,2,4,8,16,32,6,17,40}
def h(x):return -1 if x in NEG else 1
def ck(z):
 global checks
 assert z
 checks+=1
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mul(a,x):return (a[0]*x,a[1]*x) if x>=0 else (a[1]*x,a[0]*x)
def series(z):
 p=z;total=F(0)
 for j in range(32):total+=2*p/(2*j+1);p*=z*z
 return total,total+2*p/(65*(1-z*z))
LN=series(F(1,3));D=1<<80;Z=1<<128
@lru_cache(None)
def lg(x):
 ck(x>0); y=x;k=0
 while y<1:y*=2;k-=1
 while y>=2:y/=2;k+=1
 z=(y-1)/(y+1);zl=F((z*Z).__floor__(),Z);zh=F((z*Z).__ceil__(),Z)
 a=series(zl)[0];b=series(zh)[1]
 lo=k+a/LN[1];hi=k+b/LN[0]
 return F((lo*D).__floor__(),D),F((hi*D).__ceil__(),D)
def xlog(x):return mul(lg(x),x) if x else (F(0),F(0))
def phi(x,y):return sub(sub(xlog(x+y),xlog(x)),xlog(y)) if x and y else (F(0),F(0))
def entropy(p):
 z=(F(0),F(0))
 for x in p:z=sub(z,xlog(x))
 return z
def fwht(t):
 a=t[:];s=1
 while s<len(a):
  for j in range(0,len(a),2*s):
   for i in range(j,j+s):u,v=a[i],a[i+s];a[i],a[i+s]=u+v,u-v
  s*=2
 return a
def alpha(p):return (1-p)**4*(1+4*p-2*p*p)
def packets(p):
 m=1-2*p;v=4*p*(1-p);q=2*p*(1-p)**3*(2-p)
 rows=[]
 for mask in range(32):
  aa=dd=F(0)
  for x in range(32):
   weight=p**x.bit_count()*(1-p)**(5-x.bit_count())
   factor=F(1)
   for j in range(5):
    if mask&(1<<j):factor*=(-1 if x&(1<<j) else 1)-m
   hp,hn=h(x<<1),h((x<<1)|1)
   aa+=weight*factor*F(hp+hn,2);dd+=weight*factor*F(hp-hn,2)
  den=v**mask.bit_count()
  U=(aa+m*dd)**2/den;Dsq=dd*dd/den
  rows.append((mask,U,Dsq))
 ck(sum(x[2] for x in rows)==q)
 ck(sum(U+v*ds for _,U,ds in rows)==1)
 ck(sum(mask.bit_count()*U+(mask.bit_count()+1)*v*ds for mask,U,ds in rows)==6*v*q)
 ck(rows[0][1]==(1-2*alpha(p))**2)
 # Distinct independent physical pivotal expectation and monotone sign for all six positions.
 for j in range(6):
  qq=ee=F(0)
  for x in range(64):
   if x&(1<<j):continue
   w=p**x.bit_count()*(1-p)**(5-x.bit_count())
   delta=F(h(x)-h(x|(1<<j)),2)
   qq+=w*delta*delta;ee+=w*delta
  ck(qq==q);ck(ee==-q)
 return rows,v,q
def seed():
 t=[h(x) for x in range(64)];w=fwht(t);p=[F(y*y,4096) for y in w]
 ck(sum(p)==1);H=entropy(p);B=[];di=[]
 for j in range(6):
  b=(F(0),F(0))
  for s in range(64):
   if not s&(1<<j):b=add(b,phi(p[s],p[s|(1<<j)]))
  B.append(b);di.append(F(sum(t[x]!=t[x^(1<<j)] for x in range(64)),64))
 ck(len(set(di))==1);ck(len(set(B))==1);ck(di[0]==F(3,16));ck(all(F(w[1<<j]**2,4096)==di[0]**2 for j in range(6)))
 return {'p':F(5,32),'d':di[0],'t':di[0]**2,'I':6*di[0],'H':H,'B':B[0],'n':6}
def advance(g,p,label):
 rows,v,q=packets(p);M=(F(0),F(0))
 for _,U,ds in rows:M=add(M,phi(U,g['t']*ds))
 reserve=sub(M,mul(phi((1-2*p)**2,g['t']),q))
 Hp=entropy([val for _,U,ds in rows for val in (U,v*ds)])
 Cp=sub(Hp,mul(entropy([v,1-v]),6*q))
 z={'p':alpha(p),'d':q*g['d'],'t':q*q*g['t'],'I':6*q*g['I'],'H':add(mul(g['H'],6*q),Cp),'B':add(mul(g['B'],q),reserve),'n':6*g['n']}
 ck(z['I']==z['n']*z['d']);ck(z['t']==z['d']**2)
 return z,{'label':label,'chosen_p':p,'q':q,'reserve':reserve,'terminal_Cp':Cp,'outer_H':Hp}
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [encode(v) for v in x]
 return x
records=[]
def store(g,detail):
 rec={'state':g,'detail':detail,'minority':min(g['p'],1-g['p']),'E_interval':mul(g['B'],1/g['d']),'H_over_I_interval':mul(g['H'],1/g['I'])}
 rec['display']={k:[float(x) for x in rec[k]] for k in ['E_interval','H_over_I_interval']};rec['display']['minority']=float(rec['minority'])
 records.append(encode(rec))
 (R/'out'/('PILOT_PARTIAL.json' if args.pilot else 'ORBIT_PARTIAL.json')).write_text(json.dumps({'records':records,'assertions':checks},indent=2),encoding='utf-8')
g=seed();store(g,{'label':'seed'})
for level in range(1,2 if args.pilot else 4):
 s=min(g['p'],1-g['p']);p=s if s<=F(7,32) else 1-s
 ck(F(1,16)<=s<=F(1,2))
 g,det=advance(g,p,'prescribed_'+str(level));ck(det['reserve'][0]>0)
 store(g,det)
 if time.perf_counter()-start>(60 if args.pilot else 180):raise RuntimeError('frozen runtime cap')
conclusion={}
if not args.pilot:
 s=min(g['p'],1-g['p']);E=mul(g['B'],1/g['d'])
 ck(s<F(1,16));ck(E[0]>F(323,100))
 # Both orientations have negative next reserve: actual high-E rare-core obstruction.
 for chosen in [s,1-s]:
  child,det=advance(g,chosen,'rare_next_minority' if chosen==s else 'rare_next_complement')
  ck(det['reserve'][1]<0);ck(mul(child['B'],1/child['d'])[1]<E[0]);ck(min(child['p'],1-child['p'])<s)
  store(child,det)
 conclusion={'actual_rare_core_bits':g['n'],'minority_probability':s,'E_interval':E,'both_sign_next_reserves':'STRICTLY_NEGATIVE','both_next_E':'STRICTLY_BELOW_CORE_E','full_FEI':'OPEN; finite prefix only, no unbounded H/I'}
out={'status':'PASS','assertions':checks,'runtime_seconds':time.perf_counter()-start,'records':records,'conclusion':encode(conclusion)}
(R/'out'/('PILOT.json' if args.pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
