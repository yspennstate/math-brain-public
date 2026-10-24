from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import json,time,sys
R=Path(__file__).resolve().parents[1];MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
START=time.monotonic();CAP=60 if MODE=='pilot' else 1800;CK=0;SCALE=1<<100
CERTS={};LOGS={}
def ck(ok):
 global CK
 assert ok;CK+=1
 if time.monotonic()-START>CAP:raise TimeoutError('frozen time cap')
def series(t):
 z=(t-1)/(t+1);p=z;s=F(0)
 for j in range(40):s+=2*p/(2*j+1);p*=z*z
 return s,s+2*p/(81*(1-z*z))
LN2=series(F(2))
@lru_cache(maxsize=12000)
def log(x):
 e=x.bit_length()-1
 if x==1<<e:return e*SCALE,e*SCALE
 lo,hi=series(F(x,1<<e));lo=(e+lo/LN2[1])*SCALE;hi=(e+hi/LN2[0])*SCALE
 bounds=lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator)
 LOGS[str(x)]=[str(y) for y in bounds]
 return bounds
def certify(expr):
 key=tuple(sorted((x,c) for x,c in expr.items() if c and x!=1))
 if key in CERTS:return CERTS[key]
 lo=hi=0
 for x,c in key:
  a,b=log(x)
  if c>0:lo+=c*a;hi+=c*b
  else:lo+=c*b;hi+=c*a
 ck(not key or lo>0 or hi<0)
 obj={'sign':0 if not key else 1 if lo>0 else -1,'lo':str(lo),'hi':str(hi),'expression':[[str(x),str(c)] for x,c in key]}
 CERTS[key]=obj
 return obj

# Groups S,W,U,V. Category records which groups have a nonempty spectral set.
TERMS=[(1,14),(1,5),(1,9),(-1,13),(-1,15)]
def controller_hat(widths,cat,child=None):
 ps=[F(1,1<<w) for w in widths]
 if child==0:return ps[1]*ps[2]*ps[3] if not cat&1 else F(0)
 value=F(0)
 for coef,support in TERMS:
  if cat&~support:continue
  term=F(coef)
  for j in range(4):
   if support>>j&1:term*=ps[j]
  value+=term
 return value
def categories(widths):
 for cat in range(16):
  count=1
  for j,w in enumerate(widths):
   if cat>>j&1:count*=(1<<w)-1
  if count:yield cat,count
def root_bad(j,L,U,V):
 t=j-1;widths=[t,L,U,V];N=1<<(sum(widths)+1)
 expr=Counter();dn=norm=0
 for cat,count in categories(widths):
  a=controller_hat(widths,cat,0);b=controller_hat(widths,cat,1)
  for core in (0,1):
   g=a if core else int(cat==0)-a
   h=b if core else int(cat==0)-b
   u=N*g;v=N*h;ck(u.denominator==v.denominator==1);u=int(u);v=int(v)
   A=(u+v)**2;B=(u-v)**2;T=A+B;dn+=count*B;norm+=count*T
   for x,c in [(T,T),(A,-A),(B,-B)]:
    if x:expr[x]+=count*c
 ck(norm==(2*N)**2)
 eta=F(1,1<<(L+U+V));q=F(1,1<<U);r=F(1,1<<V);e=q+r-q*r-eta
 d=F(e,1<<(t+1));ck(F(dn,(2*N)**2)==d)
 expr[2]-=4*dn;cert=certify(expr)
 return cert['sign']>0,d,cert

def quantities(s,L,U,V,coreI=F(1)):
 a=F(1,1<<s);q=F(1,1<<U);r=F(1,1<<V);eta=F(1,1<<(L+U+V));beta=q+r-q*r;e=beta-eta
 JB=(L+U+V)*eta;JC=U*q*(1-r)+V*r*(1-q);JD=JB+JC
 p=eta+a*e;Isep=s*a*e;Iother=(1-a)*JB+a*JC;Iterm=p*coreI
 raw=a*(s*JD+e*s*(s-1)/2+s*e*coreI)
 return {'alpha':a,'eta':eta,'e':e,'JB':JB,'JC':JC,'JD':JD,'terminal_probability':p,'I_separator':Isep,'I_other_controls':Iother,'I_terminal':Iterm,'I':Isep+Iother+Iterm,'raw_separator_credit':raw}

def root_entropy_sign(s,L,U,V,I):
 widths=[s,L,U,V];N=1<<(sum(widths)+1);expr=Counter();norm=0
 for cat,count in categories(widths):
  a=controller_hat(widths,cat)
  for core in (0,1):
   u=N*(a if core else int(cat==0)-a);ck(u.denominator==1);w=int(u)**2;norm+=count*w
   if w:expr[N*N]+=count*w;expr[w]-=count*w
 ck(norm==N*N)
 tariff=7*I*N*N;ck(tariff.denominator==1);expr[2]-=int(tariff)
 return certify(expr)

def process(s,L,U,V):
 values=quantities(s,L,U,V);bad=F(0);raw=F(0);nodes=[]
 for j in range(s,0,-1):
  flag,d,cert=root_bad(j,L,U,V);reach=F(1,1<<(s-j));rho=F(1,1<<(j-1))
  c=rho*(values['JD']+values['e']*(j-1)+values['e'])/2
  raw+=reach*c
  if flag:bad+=reach*c
  nodes.append({'remaining_selector_width':j,'reach':str(reach),'d':str(d),'c':str(c),'bad':flag,'sign':cert['sign'],'lo':cert['lo'],'hi':cert['hi']})
 ck(raw==values['raw_separator_credit'])
 family=U==V==1 and L==2*s
 if family:ck(bad==0);ck(root_entropy_sign(s,L,U,V,values['I'])['sign']<0)
 return {'s':s,'L':L,'R':U,'T':V,'n':s+L+U+V+1,'moments':{k:str(v) for k,v in values.items()},'separator_bad_credit':str(bad),'separator_bad_over_I':str(bad/values['I']),'raw_over_I':str(raw/values['I']),'raw_over_final_remaining_I':str(raw/(values['I']-values['I_separator'])),'nodes':nodes,'counterfamily':family}

if __name__=='__main__':
 cases=[(s,2*s,1,1) for s in range(1,5)] if MODE=='pilot' else [(s,L,U,V) for s in range(1,7) for L in range(1,4) for U in range(1,4) for V in range(1,4)]+[(s,2*s,1,1) for s in range(1,25)]
 rows=[]
 with (R/'out'/f'{MODE}_ROWS.jsonl').open('w') as fp:
  for s,L,U,V in cases:
   row=process(s,L,U,V);rows.append(row);fp.write(json.dumps(row)+'\n');fp.flush()
   if len(rows)%25==0:print('finished',len(rows),'seconds',time.monotonic()-START,flush=True)
 result={'mode':MODE,'family_cases':len(rows),'separator_node_occurrences':sum(len(x['nodes']) for x in rows),'assertions_passed':CK,'seconds':time.monotonic()-START,'max_dimension':max(x['n'] for x in rows),'rows':rows,'scale':str(SCALE),'certificates':list(CERTS.values()),'log_intervals':LOGS,'terminal_entropy':'pi H(g) retained; g=z has H=0'}
 (R/'out'/f'{MODE}_RESULTS.json').write_text(json.dumps(result,indent=2))
 print(json.dumps({k:v for k,v in result.items() if k not in ('rows','certificates','log_intervals')}))
