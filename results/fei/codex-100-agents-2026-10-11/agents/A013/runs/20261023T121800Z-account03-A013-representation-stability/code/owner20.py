from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
R=Path(__file__).resolve().parents[1];START=time.perf_counter();CHECKS=0
def ck(v):
 global CHECKS
 assert v,CHECKS
 CHECKS+=1
 assert time.perf_counter()-START<50
def enc(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return {str(k):enc(x) for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [enc(x) for x in v]
 return v
def save(name,v):
 (R/'out').mkdir(exist_ok=True)
 (R/'out'/name).write_text(json.dumps(enc(v),indent=2)+'\n',encoding='utf-8')
def fw(v):
 a=list(v);h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def spec(v):return tuple(F(x*x,len(v)**2) for x in fw(v))
def influence(v):return F(sum(v[x]!=v[x^(1<<j)] for j in range((len(v)-1).bit_length()) for x in range(len(v))),len(v))
def factor(n):
 ans={};p=2
 while p*p<=n:
  while n%p==0:n//=p;ans[p]=ans.get(p,0)+1
  p+=1
 if n>1:ans[n]=ans.get(n,0)+1
 return ans
def linear(*args):
 ans={}
 for w,s in args:
  for p,c in s.items():ans[p]=ans.get(p,F(0))+w*c
 return {p:c for p,c in ans.items() if c}
def logterm(s,w,x):
 t={}
 for sign,n in ((1,x.numerator),(-1,x.denominator)):
  for p,e in factor(n).items():t[p]=t.get(p,F(0))+sign*e*w
 return linear((1,s),(1,t))
def ce(p,q):
 out={}
 for x,y in zip(p,q):
  if x:ck(y>0);out=logterm(out,x,1/y)
 return out
def ent(p):return ce(p,p)
def kl(p,q):return linear((1,ce(p,q)),(-1,ent(p)))
@lru_cache(None)
def ln_int(n):
 k=n.bit_length()-1;x=F(n,1<<k)
 def series(x):
  u=(x-1)/(x+1);lo=sum((2*u**(2*j+1)/F(2*j+1) for j in range(24)),F(0))
  return lo,lo+2*u**49/F(49)/(1-u*u)
 lo,hi=series(x);l2,h2=series(F(2));return lo+k*l2,hi+k*h2
def interval(s,constant=F(0)):
 lo=hi=constant
 for p,c in s.items():
  l,h=ln_int(p);lo+=c*(l if c>=0 else h);hi+=c*(h if c>=0 else l)
 return lo,hi
def bits(iv):
 l,h=ln_int(2)
 return min(x/y for x in iv for y in (l,h)),max(x/y for x in iv for y in (l,h))
def marginal(q,i):
 n=(len(q)-1).bit_length()
 def ins(t):return (t&((1<<i)-1))|((t>>i)<<(i+1))
 return tuple(q[ins(t)]+q[ins(t)|(1<<i)] for t in range(1<<(n-1)))
def cofactor(v,i,b):
 def ins(t):return (t&((1<<i)-1))|((t>>i)<<(i+1))|(b<<i)
 return tuple(v[ins(t)] for t in range(len(v)//2))
def half_profile(p,q):
 p0,q0=p[0],q[0]
 if q0 in (0,1):ck(p0==q0);return q,{}
 r=(p0+q0)/2;ratio=(1-r)/(1-q0)
 new=(r,)+tuple(ratio*x for x in q[1:]);ck(sum(new)==1)
 for x,y in zip(q[1:],new[1:]):ck(y==ratio*x)
 charge=kl(new,q)
 saving=linear((1,ce(p,q)),(-1,ce(p,new)))
 rebate=linear((1,saving),(-1,charge))
 symmetric=linear((1,kl(new,q)),(1,kl(q,new)))
 ck(rebate==symmetric);ck(interval(charge)[0]>=0);ck(interval(rebate)[0]>=0)
 return new,charge
TARGET=Path('agents/A012/runs/20261023T053904Z-account03-A012-sparse-activation-accounting/out/NEXT_TARGET.json')
d=json.loads(TARGET.read_text(encoding='utf-8'));ROOTF=tuple(d['F']);ROOTQ=tuple(map(F,d['root_Q']));ROOTP=spec(ROOTF);ROOTH=ent(ROOTP);ROOTI=influence(ROOTF)
ck(ROOTP==ROOTQ);ck(ROOTI==F(7,8));OLD=F(5,4)
ROOT_MARGIN_SIG=linear((4*ROOTI,{2:F(1)}),(-1,ROOTH));ROOT_CONSTANT=2*ROOTI-OLD
AVG_CHILD_H=linear((F(1,2),ent(spec(tuple(d['G'])))),(F(1,2),ent(spec(tuple(d['H'])))))
ORIGINAL_CHILD_BANK=linear((3,{2:F(1)}),(-1,AVG_CHILD_H))
ORIGINAL_SELECTOR_BANK=linear((F(1,2),{2:F(1)}),(-1,ROOTH),(1,AVG_CHILD_H))
ck(linear((1,ORIGINAL_CHILD_BANK),(1,ORIGINAL_SELECTOR_BANK))==ROOT_MARGIN_SIG)
@lru_cache(None)
def policies(available):
 out=[('stop',)]
 for j in available:
  rest=tuple(x for x in available if x!=j)
  for u in policies(rest):
   for v in policies(rest):out.append((j,u,v))
 return tuple(out)
POLICIES=policies((0,1,2));ck(len(POLICIES)==244)
def walk(tree,v=ROOTF,q=ROOTQ,coords=(0,1,2,3,4,5),fixed=(),reach=F(1),updated=False):
 p=spec(v);h=ent(p);i=influence(v);fees={};transactions=[]
 if set(fixed)=={0,1} and not updated:
  before=q;q,fee=half_profile(p,q);updated=True;fees=linear((reach,fee))
  transactions=[{'reach':reach,'p_empty':p[0],'q_empty':before[0],'r_empty':q[0],'full_conversion':fee,'truth':v,'oldQ':before,'newQ':q}]
 if tree[0]=='stop':
  term=linear((reach,ce(p,q)));termkl=linear((reach,kl(p,q)))
  b_rem=F(0)
  for original in (0,1,2):
   if original in coords:
    j=coords.index(original);b_rem+=reach*F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v))*2
  return {'ce':term,'kl':termkl,'h':linear((reach,h)),'i':reach*i,'query_entropy':{},'fees':fees,'queried_influence':F(0),'old_remaining_coefficient':b_rem,'old_retired_coefficient':F(0),'leaves':[{'reach':reach,'truth':v,'P':p,'Q':q,'coords':coords,'KL':kl(p,q),'off_target_mass':sum(y for x,y in zip(p,q) if not x)}],'transactions':transactions}
 original=tree[0];j=coords.index(original);ck(original in (0,1,2));children=[]
 for bit in (0,1):children.append(walk(tree[bit+1],cofactor(v,j,bit),marginal(q,j),tuple(x for x in coords if x!=original),fixed+(original,),reach/2,updated))
 out={k:linear((1,children[0][k]),(1,children[1][k])) for k in ('ce','kl','h','query_entropy','fees')}
 dh=linear((1,h),(-F(1,2),ent(spec(cofactor(v,j,0)))),(-F(1,2),ent(spec(cofactor(v,j,1)))))
 out['query_entropy']=linear((1,out['query_entropy']),(reach,dh));out['fees']=linear((1,out['fees']),(1,fees))
 inf=F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v))
 out['i']=sum(x['i'] for x in children);out['queried_influence']=sum(x['queried_influence'] for x in children)+reach*inf
 out['old_retired_coefficient']=sum(x['old_retired_coefficient'] for x in children)+2*reach*inf
 out['old_remaining_coefficient']=sum(x['old_remaining_coefficient'] for x in children)
 out['leaves']=sum((x['leaves'] for x in children),[]);out['transactions']=transactions+sum((x['transactions'] for x in children),[])
 return out
def analyze(tree):
 x=walk(tree)
 ck(linear((1,x['h']),(1,x['query_entropy']),(-1,ROOTH))=={})
 ck(ROOTI==x['i']+x['queried_influence']);ck(x['old_remaining_coefficient']+x['old_retired_coefficient']==OLD)
 liability=linear((1,x['kl']),(1,x['fees']))
 fullcost=linear((1,x['ce']),(1,x['query_entropy']),(1,x['fees']))
 ck(fullcost==linear((1,ROOTH),(1,liability)))
 marginsig=linear((1,ROOT_MARGIN_SIG),(-1,liability));iv=interval(marginsig,ROOT_CONSTANT)
 ck(iv[0]>0 or iv[1]<0)
 return x,{'tree':tree,'margin_natural':iv,'margin_bits':bits(iv),'liability_KL_plus_conversion':liability,'executed_entropy':x['query_entropy'],'terminal_CE':x['ce'],'conversion_fees':x['fees'],'remaining_I':x['i'],'queried_I':x['queried_influence'],'old_remaining_coefficient':x['old_remaining_coefficient'],'old_retired_coefficient':x['old_retired_coefficient']}
def main(mode):
 if mode=='pilot':
  tree=(0,(1,(2,('stop',),('stop',)),(2,('stop',),('stop',))),(1,(2,('stop',),('stop',)),(2,('stop',),('stop',))))
  x,row=analyze(tree);save('PILOT.json',{'status':'PASS','assertions':CHECKS,'result':row,'full_leaves':x['leaves'],'transactions':x['transactions'],'seconds':time.perf_counter()-START})
  print(json.dumps({'status':'PASS','mode':'pilot','margin_bits':list(map(float,row['margin_bits'])),'assertions':CHECKS,'seconds':time.perf_counter()-START}));return
 records=[]
 for tree in POLICIES:
  _,row=analyze(tree);records.append(row)
 positive=sum(x['margin_natural'][0]>0 for x in records);worst=min(records,key=lambda x:x['margin_natural'][0])
 save('ALL_POLICIES.json',{'status':'PASS','cases':244,'assertions':CHECKS,'positive':positive,'negative':244-positive,'worst':worst,'records':records,'root_original_margin_natural':interval(ROOT_MARGIN_SIG,ROOT_CONSTANT),'postvariance_original_child_bank_natural':interval(ORIGINAL_CHILD_BANK),'unused_original_selector_bank_natural':interval(ORIGINAL_SELECTOR_BANK,ROOT_CONSTANT),'seconds':time.perf_counter()-START})
 print(json.dumps({'status':'PASS','positive':positive,'negative':244-positive,'worst_margin_bits':list(map(float,worst['margin_bits'])),'assertions':CHECKS,'seconds':time.perf_counter()-START}))
if __name__=='__main__':main(sys.argv[1])
