from pathlib import Path
import sympy as S,json
p=S.symbols('p'); q=1-p
parts=[]
def gen(a):
 if len(a)==4:parts.append(tuple(a));return
 for v in range(max(a,default=-1)+2):gen(a+[v])
gen([])
def orbit(a):
 sizes=sorted([a.count(v) for v in set(a)])
 if sizes==[1,1,1,1]:return 'sigma'
 if sizes==[4]:return 'epsilon'
 if sizes==[1,3]:return 'delta'
 if sizes==[2,2]:return 'crossing' if a[0]==a[2] else 'gamma'
 inds=[i for i in range(4) if a.count(a[i])==2]
 return 'beta' if (inds[1]-inds[0])%4==2 else 'alpha'
co={k:0 for k in ['sigma','alpha','beta','gamma','delta','epsilon']}; fail={k:S.Rational(0) for k in co};counts=dict.fromkeys(co,0)
for a in parts:
 k=orbit(a)
 if k=='crossing':continue
 counts[k]+=1
 pol=0
 for mask in range(16):
  roots=list(range(5))
  def find(x):
   while roots[x]!=x:x=roots[x]
   return x
  def join(x,y):roots[find(x)]=find(y)
  for i in range(4):
   for j in range(i):
    if a[i]==a[j]:join(i,j)
  for i in range(4):
   if mask>>i&1:join(i,4)
  pol+=(int(find(0)==find(4))-int(find(0)==find(2)))*p**mask.bit_count()*q**(4-mask.bit_count())
 co[k]+=S.expand(pol)
 m=sum(a[j]==a[0] for j in [1,2,3]);fail[k]+=S.Rational(1,2)**m
expected={'sigma':p,'alpha':2*p*(3-2*p),'beta':2*p-1,'gamma':2*p*q*(2-p),'delta':2*p**3-7*p**2+8*p-2,'epsilon':-q**3}
for k in co:
 assert S.expand(co[k]-q*expected[k])==0
print('orbit counts',counts);print('difference coefficients',co);print('critical detour failure orbit sums',fail)
assert counts=={'sigma':1,'alpha':4,'beta':2,'gamma':2,'delta':4,'epsilon':1}
assert fail=={'sigma':1,'alpha':3,'beta':S.Rational(3,2),'gamma':1,'delta':S.Rational(7,4),'epsilon':S.Rational(1,8)}
t=S.symbols('t');assert S.expand(3+S.Rational(15,4)*t*t-7*t-2*(S.Rational(2,3)-t)-S.Rational(15,4)*(t-S.Rational(2,3))**2)==0
Path('partition_checks.json').write_text(json.dumps({'orbit_sizes':counts,'difference_coefficients':{k:str(v) for k,v in co.items()},'failure_weights':{k:str(v) for k,v in fail.items()},'result':'ALL_EXACT_CHECKS_PASS'},indent=2),encoding='utf8')
print('ALL_EXACT_CHECKS_PASS')
