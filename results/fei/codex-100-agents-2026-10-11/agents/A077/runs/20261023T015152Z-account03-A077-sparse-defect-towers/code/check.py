"""A077 masked-carrier-v1: exact, frozen shared census and same-source histories."""
from pathlib import Path
import sys, itertools, json, time, hashlib
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'code'))
import arithmetic as A
from arithmetic import F,coeff,H,I,inf,B,child,plus,Phi,phi,bounds,eq,equal_expr,leq
pilot='--pilot' in sys.argv
start=time.perf_counter(); limit=55 if pilot else 180
counts={'review_roots':0,'review_shared_queries':0,'carrier_states':0,'carrier_queries':0,'balanced_pairs':0,'masked_queries':0,'mixed_nodes':0,'mixed_leaves':0,'direct_roots':0}
def guard():
    if time.perf_counter()-start>limit:raise RuntimeError('Frozen runtime exceeded')
def save(name,x):
    (ROOT/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def delt(t,i):return plus((H(t),F(1)),(H(child(t,i,0)),F(-1,2)),(H(child(t,i,1)),F(-1,2)))
def xi(v,w,p):
    return plus(*[(plus((phi((a+b)**2),F(1,2)),(phi((a-b)**2),F(1,2)),(phi(a*a),F(-1)),(phi(b*b),F(-1))),p) for a,b in zip(coeff(v)[1:],coeff(w)[1:])])
def two(v,w,d):return tuple(v[x] if s==0 else w[x] if s==1 else 1 for s in range(1<<d) for x in range(len(v)))
def direct(t):
    eq(coeff(t),tuple(F(sum(a*(-1 if (s&x).bit_count()%2 else 1) for x,a in enumerate(t)),len(t)) for s in range(len(t))))
    for i in range(len(t).bit_length()-1):eq(inf(t,i),F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)))
    counts['direct_roots']+=1

# Independent review of A076 v8 sections2-4: full physical shared roots.
for n in range(2 if pilot else 3):
 for v in itertools.product((-1,1),repeat=1<<n):
  for w in itertools.product((-1,1),repeat=1<<n):
   for d in (1,2,3):
    guard();p=F(1,1<<d);t=two(v,w,d);mu=F(sum(v),len(v));nu=F(sum(w),len(w))
    j=2*p*F(sum(a!=b for a,b in zip(v,w)),len(v));eq(inf(t,n),j)
    rel=p*(2-mu*mu-nu*nu)
    q=2-mu-nu;c=mu-nu
    empty=plus((Phi((1-p*q)**2,p*p*c*c),F(1)),(Phi(p*p*q*q,p*p*c*c),1/(2*p)-1))
    ct=coeff(t)
    empty_direct=plus(*[(Phi(ct[s]**2,ct[s|(1<<n)]**2),F(1)) for s in range(len(t)) if not s>>n&1 and s%len(v)==0])
    equal_expr(plus((empty,F(1)),(empty_direct,F(-1))))
    leq(empty,6*j);leq(plus((B(t,n),F(1)),(empty,F(-1))),rel)
    leq(delt(t,n),rel+9*j)
    for k in range(1,d):
     j=p*(2-mu-nu);eq(inf(t,n+k),j);leq(delt(t,n+k),6*j)
    if n<=1 and d<=2:direct(t)
    counts['review_roots']+=1;counts['review_shared_queries']+=d
    coeff.cache_clear()
save('REVIEW_VALIDATION.json',{'helper_version':'masked-carrier-v1','pilot':pilot,'counts':dict(counts),'exact_assertions_so_far':A.checks,'status':'PASS','seconds':time.perf_counter()-start})

# A state records the actual carrier and edited labels after each shared restriction.
def maj(s):return 1 if s.bit_count()<=1 else -1
def carrier(fixed):
 rem=tuple(i for i,a in enumerate(fixed) if a is None);h=[];active={}
 for x in range(1<<len(rem)):
  s=sum((a<<i) for i,a in enumerate(fixed) if a is not None)+sum(((x>>j&1)<<i) for j,i in enumerate(rem))
  h.append(maj(s))
  if s in (0,1):active[x]='v' if s==0 else 'w'
 return tuple(h),active,tuple('s'+str(i+1) for i in rem)
def mask(h,active):return tuple(0 if s in active else a for s,a in enumerate(h))
def imin(h,active,i):
 total=F(0)
 for s in range(len(h)):
  a=s in active;b=(s^(1<<i)) in active
  total+=F(0) if a and b else F(1,2) if a or b else F(h[s]!=h[s^(1<<i)])
 return total/len(h)
def wrapper(h,active,v,w):
 return tuple((v if active[s]=='v' else w)[x] if s in active else h[s] for s in range(len(h)) for x in range(len(v)))
cert=[]
for fixed in itertools.product((None,0,1),repeat=3):
 h,act,sh=carrier(fixed);m=mask(h,act);counts['carrier_states']+=1
 for i in range(len(sh)):
  low=imin(h,act,i);bill=B(m,i);leq(bill,2*low)
  cert.append({'fixed':list(fixed),'query':sh[i],'mask':list(m),'physical_influence_lower_bound':str(low),'empty_erasure_log_expression':{str(x):str(c) for x,c in bill.items()},'empty_erasure_interval':[str(a) for a in bounds(bill)],'price2_margin_interval':[str(2*low-b) for b in reversed(bounds(bill))]})
  counts['carrier_queries']+=1
save('CARRIER_CERTIFICATE.json',{'status':'PASS','domain':'all 27 partial assignments of three shared bits, every remaining coordinate','cases':cert})

for n in range(1,2 if pilot else 3):
 tabs=[t for t in itertools.product((-1,1),repeat=1<<n) if sum(t)==0]
 for v in tabs:
  for w in tabs:
   counts['balanced_pairs']+=1
   for fixed in itertools.product((None,0,1),repeat=3):
    guard();h,act,sh=carrier(fixed);m=mask(h,act);t=wrapper(h,act,v,w);p=F(1,len(h));r=len(sh);T=plus(*[(H(v if a=='v' else w),p) for a in act.values()]);R=r*p*len(act)
    X=xi(v,w,p) if len(act)==2 else {}
    equal_expr(plus((H(t),F(1)),(T,F(-1)),(X,F(-1)),(H(m),F(-1)),({F(2):2*R},F(-1))))
    for j in range(r):
     low=imin(h,act,j);eq(inf(t,n+j)>=low,True)
     # Complete empty-private erasure and all nonempty rows are partitioned exactly.
     ct=coeff(t);be=plus(*[(Phi(ct[s]**2,ct[s|(1<<(n+j))]**2),F(1)) for s in range(len(t)) if not s>>(n+j)&1 and s%len(v)==0])
     equal_expr(plus((be,F(1)),(B(m,j),F(-1))))
     leq(plus((B(t,n+j),F(1)),(be,F(-1))),p*len(act))
     leq(delt(t,n+j),p*len(act)+5*inf(t,n+j))
     counts['masked_queries']+=1
    coeff.cache_clear()

# Actual k4,m2 source, first x1 debit already booked; both x1 answers retained.
names=('z1','z2','z3','z4','x1','x2','y')
v0=tuple((-1 if x>>6&1 else 1)*(-1 if ((x&1)*(x>>1&1)+(x>>2&1)*(x>>3&1))%2 else 1) for x in range(128))
w0=tuple((-1 if x>>6&1 else 1)*(-1 if x%64==0 else 1) for x in range(128))
eq(I(v0),F(3));equal_expr(plus((H(v0),F(1)),({F(2):4},F(-1))))
e0=F(1,8);S=11*e0;old=4*e0;D0=e0;budget=S-old-D0
eq(S,5*e0*I(v0)-4*e0);eq(budget>=4*e0,True)
policies=[('s2','z1','s1','x2','s3','y'),('s1','z1','s2','x2','s3','y'),('z1','s3','x2','s2','s1','y')]
ledger=[];policy_results=[]
def term(st):
 p=F(1,len(st['h']))
 return plus(*[(H(st[a]),p) for a in st['act'].values()])
def reserve(st):return len(st['sh'])*F(len(st['act']),len(st['h']))
def account(st):
 if st['freeze'] is not None:return st['freeze']
 if len(st['act'])<2:return {}
 p=F(1,len(st['h']))
 return plus(({F(2):p*st['beta']},F(1)),(st['chi0'],-p),(xi(st['v'],st['w'],p),F(1)))
def branch(st,name,bit):
 z=dict(st)
 if name in st['pr']:
  idx=st['pr'].index(name);z['pr']=tuple(a for a in st['pr'] if a!=name)
  z['v']=child(st['v'],idx,bit);z['w']=child(st['w'],idx,bit)
 else:
  idx=st['sh'].index(name);z['sh']=tuple(a for a in st['sh'] if a!=name)
  z['h']=child(st['h'],idx,bit);oldact=st['act'];newact={}
  for x in range(len(z['h'])):
   oldx=(x&((1<<idx)-1))+((x>>idx)<<(idx+1))+(bit<<idx)
   if oldx in oldact:newact[x]=oldact[oldx]
  z['act']=newact
  if len(oldact)==2 and len(newact)==1:z['freeze']=account(st)
  # If both vertices die before separation, no earmark is reissued to carrier.
 return z
for policy in policies[:1 if pilot else 3]:
 for first in (0,1):
  v=child(v0,4,first);w=child(w0,4,first);h,act,sh=carrier((None,None,None))
  st={'h':h,'act':act,'sh':sh,'pr':tuple(a for a in names if a!='x1'),'v':v,'w':w,'freeze':None,'beta':budget/e0,'chi0':plus((xi(v,w,e0),1/e0))}
  totals={'H':{},'T':{},'R':F(0),'K':{},'paid':F(0),'mass':F(0)}
  def walk(st,depth,reach,path):
   guard();tt=wrapper(st['h'],st['act'],st['v'],st['w']);kk=account(st);rr=reserve(st);tr=term(st)
   leq(plus((kk,F(-1))),0)
   entry={'policy':list(policy),'first_x1':first,'path':path,'reach':str(reach),'shared':list(st['sh']),'private':list(st['pr']),'active_vertices':{str(x):a for x,a in st['act'].items()},'H_interval':[str(a) for a in bounds(H(tt))],'I':str(I(tt)),'R':str(rr),'K_interval':[str(a) for a in bounds(kk)],'T_interval':[str(a) for a in bounds(tr)]}
   if depth==len(policy):
    entry['terminal_coefficients']=[str(a) for a in coeff(tt)]
    entry['V_terminal_coefficients']=[str(a) for a in coeff(st['v'])]
    entry['W_terminal_coefficients']=[str(a) for a in coeff(st['w'])]
    ledger.append(entry);counts['mixed_leaves']+=1
    totals['H']=plus((totals['H'],F(1)),(H(tt),reach));totals['T']=plus((totals['T'],F(1)),(tr,reach));totals['K']=plus((totals['K'],F(1)),(kk,reach));totals['R']+=reach*rr;totals['mass']+=reach
    return
   name=policy[depth];idx=st['pr'].index(name) if name in st['pr'] else len(st['pr'])+st['sh'].index(name)
   a,b=branch(st,name,0),branch(st,name,1);ta=wrapper(a['h'],a['act'],a['v'],a['w']);tb=wrapper(b['h'],b['act'],b['v'],b['w'])
   eq(ta,child(tt,idx,0));eq(tb,child(tt,idx,1))
   dT=plus((tr,F(1)),(term(a),F(-1,2)),(term(b),F(-1,2)))
   residual=plus((H(tt),F(1)),(H(ta),F(-1,2)),(H(tb),F(-1,2)),(dT,F(-1)),(account(a),F(1,2)),(account(b),F(1,2)),(kk,F(-1)))
   release=rr-(reserve(a)+reserve(b))/2
   if name in st['pr']:
    # Guard y is queried only after every shared input is gone.
    eq(name!='y' or not st['sh'],True)
    equal_expr(plus((residual,F(1)),({F(2):release},F(-1))))
    entry['inherited_V_erasure_interval']=[str(a) for a in bounds(B(st['v'],st['pr'].index(name)))]
    entry['inherited_W_erasure_interval']=[str(a) for a in bounds(B(st['w'],st['pr'].index(name)))]
   else:
    cost=5*inf(tt,idx);leq(residual,release+cost);totals['paid']+=reach*cost
    entry['masked_carrier_erasure_interval']=[str(a) for a in bounds(B(mask(st['h'],st['act']),st['sh'].index(name)))]
   ledger.append(entry);counts['mixed_nodes']+=1
   walk(a,depth+1,reach/2,path+name+'=0;');walk(b,depth+1,reach/2,path+name+'=1;')
  walk(st,0,F(1),'')
  eq(totals['mass'],F(1));leq(plus((totals['K'],F(-1))),-(budget-4*e0))
  residual=plus((H(wrapper(h,act,v,w)),F(1)),(totals['H'],F(-1)),(totals['K'],F(1)),(term(st),F(-1)),(totals['T'],F(1)))
  leq(residual,reserve(st)+budget+totals['paid']-totals['R'])
  policy_results.append({'policy':list(policy),'first_x1':first,'original_C5_influence_allocation':str(5*e0*I(v0)),'original_bent_entropy_allocation':str(4*e0),'original_surplus':str(S),'first_old_debit':str(old),'other_old_debit':str(D0),'continuation_budget':str(budget),'guaranteed_terminal_account':str(S-old-D0-4*e0),'expected_terminal_account_interval':[str(a) for a in bounds(totals['K'])],'shared_price5_payment':str(totals['paid'])})
save('MIXED_LEDGER_PILOT.json' if pilot else 'MIXED_LEDGER.json',{'status':'PASS','policies':policy_results,'states':ledger})
save('PILOT.json' if pilot else 'VALIDATION.json',{'helper_version':'masked-carrier-v1','pilot':pilot,'counts':counts,'exact_assertions':A.checks,'elapsed_seconds':time.perf_counter()-start,'status':'PASS','full_fei':'OPEN','formal_check':'NOT_CLAIMED'})
print(json.dumps({'status':'PASS','pilot':pilot,'counts':counts,'exact_assertions':A.checks,'elapsed_seconds':time.perf_counter()-start}))
