"""Face-account-v1: full Boolean identities with residual address codimension."""
from pathlib import Path
import sys,json,itertools,time
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'code'))
import arithmetic as A
from arithmetic import F,coeff,H,I,inf,B,child,plus,phi,bounds,eq,leq,equal_expr
pilot='--pilot' in sys.argv;start=time.perf_counter();limit=55 if pilot else 600
counts={'roots':0,'partial_shared_states':0,'physical_queries':0,'mixed_nodes':0,'mixed_leaves':0,'handoffs':0,'suffix_free_queries':0,'suffix_free_positive_influence':0,'suffix_separator_queries':0}
def guard():
 if time.perf_counter()-start>limit:raise RuntimeError('Frozen runtime limit; no dimension escalation')
def save(name,x):(ROOT/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def mean(t):return F(sum(t),len(t))
def var(t):return 1-mean(t)**2
def collision(v,w,p):return plus(*[(plus((phi((a+b)**2),F(1,2)),(phi((a-b)**2),F(1,2)),(phi(a*a),F(-1)),(phi(b*b),F(-1))),p) for a,b in zip(coeff(v)[1:],coeff(w)[1:])])
def labels(st):return tuple(sorted(set(st['lab'])-{0}))
def geometry(st):
 live=labels(st)
 if not live:return live,F(0),0
 num=st['lab'].count(live[0]);den=len(st['lab']);p=F(num,den);codim=(den//num).bit_length()-1
 eq(F(1,1<<codim),p)
 for a in live:eq(st['lab'].count(a),num)
 return live,p,codim
def TT(st):return tuple(st['v'][a][x] if a else st['h'][s] for s,a in enumerate(st['lab']) for x in range(1<<len(st['pr'])))
def U(st):
 live,p,c=geometry(st);return plus(*[(H(st['v'][a]),p) for a in live])
def reserve(st):
 live,p,c=geometry(st);return c*p*sum((var(st['v'][a]) for a in live),F(0))
def X(st):
 live,p,c=geometry(st);return collision(st['v'][1],st['v'][2],p) if len(live)==2 else {}
def E(st):return H(tuple(mean(st['v'][a]) if a else F(st['h'][s]) for s,a in enumerate(st['lab'])))
def Z(st):
 live,p,c=geometry(st);return plus((E(st),F(1)),({F(2):reserve(st)+1},F(1)),*[(phi(mean(st['v'][a])**2),-p) for a in live])
def K(st):
 if st['frozen'] is not None:return st['frozen']
 live,p,c=geometry(st)
 return plus((st['density'],p),(X(st),F(1))) if len(live)==2 else {}
def branch(st,name,bit):
 z=dict(st)
 if name in st['pr']:
  j=st['pr'].index(name);z['pr']=tuple(a for a in st['pr'] if a!=name);z['v']={a:child(v,j,bit) for a,v in st['v'].items()}
 else:
  j=st['sh'].index(name);z['sh']=tuple(a for a in st['sh'] if a!=name);z['h']=child(st['h'],j,bit);z['lab']=child(st['lab'],j,bit)
  if len(labels(st))==2 and len(labels(z))==1:z['frozen']=K(st)
  elif len(labels(st))==2 and not labels(z):z['frozen']={}
 return z
def make(v,w,d=5,b=1,pr=None,budget=None):
 c=d-b;p=F(1,1<<c);budget=4*p if budget is None else budget
 h=tuple(1 if 2*s.bit_count()<d else -1 for s in range(1<<d))
 lab=tuple(1 if s% (1<<c)==0 else 2 if s%(1<<c)==1 else 0 for s in range(1<<d))
 density=plus(({F(2):budget/p},F(1)),(collision(v,w,p),-1/p))
 return {'h':h,'lab':lab,'v':{1:v,2:w},'pr':tuple(pr or ('x'+str(j) for j in range(len(v).bit_length()-1))),'sh':tuple('s'+str(j+1) for j in range(d)),'density':density,'frozen':None}
def identity(st):equal_expr(plus((H(TT(st)),F(1)),(U(st),F(-1)),(X(st),F(-1)),({F(2):reserve(st)},F(-1)),(Z(st),F(-1)),({F(2):1},F(1))))
def diff(fun,st,kids):return plus((fun(st),F(1)),(fun(kids[0]),F(-1,2)),(fun(kids[1]),F(-1,2)))
def local(st,kids):
 dh=diff(lambda s:H(TT(s)),st,kids);du=diff(U,st,kids);dx=diff(X,st,kids);dk=diff(K,st,kids);dz=diff(Z,st,kids);dr=reserve(st)-(reserve(kids[0])+reserve(kids[1]))/2
 equal_expr(plus((dh,F(1)),(du,F(-1)),(dx,F(-1)),(dz,F(-1)),({F(2):dr},F(-1))))
 leq(plus((dx,F(1)),(dk,F(-1))),0)
 leq(plus((dh,F(1)),(du,F(-1)),(dk,F(-1)),(dz,F(-1))),dr)
 return dh,du,dk,dr

for n in range(1 if pilot else 2):
 for v in itertools.product((-1,1),repeat=1<<n):
  for w in itertools.product((-1,1),repeat=1<<n):
   root=make(v,w);i0=I(root['h']);tt=TT(root)
   # Original actual physical shared ownership, never assuming all pivots survive.
   actualshared=sum((F(sum(tt[x]!=tt[x^(1<<(n+j))] for x in range(len(tt))),len(tt)) for j in range(5)),F(0))
   eq(actualshared,sum((inf(tt,n+j) for j in range(5)),F(0)));eq(3*i0<=5*actualshared,True)
   for fixed in itertools.product((-1,0,1),repeat=5):
    guard();st=root
    for name,bit in zip(root['sh'],fixed):
     if bit!=-1:st=branch(st,name,bit)
    identity(st);zz=Z(st);leq(plus((zz,F(-1))),0);leq(zz,35*i0);leq(plus((zz,F(1)),(H(st['h']),F(-1))),26)
    eq(reserve(st)<=1,True);leq(plus((K(st),F(-1))),0)
    for a in labels(st):
     indicator=tuple(F(lab==a) for lab in st['lab']);eq(sum(abs(x) for x in coeff(indicator)),F(1))
    for name in st['pr']+st['sh']:
     kids=[branch(st,name,bit) for bit in (0,1)];local(st,kids);counts['physical_queries']+=1
    counts['partial_shared_states']+=1
   counts['roots']+=1;coeff.cache_clear()
save('CENSUS_PILOT.json' if pilot else 'CENSUS.json',{'status':'PASS','counts':dict(counts),'assertions':A.checks,'seconds':time.perf_counter()-start})

pn=('z1','z2','z3','z4','x1','x2','y')
vv=tuple((-1 if x>>6&1 else 1)*(-1 if ((x&1)*(x>>1&1)+(x>>2&1)*(x>>3&1))%2 else 1) for x in range(128))
ww=tuple((-1 if x>>6&1 else 1)*(-1 if x%64==0 else 1) for x in range(128))
p0=F(1,16);S=11*p0;FIRST=4*p0;D0=p0;budget=S-FIRST-D0
eq(I(vv),F(3));equal_expr(plus((H(vv),F(1)),({F(2):4},F(-1))))
eq(5*p0*I(vv),4*p0+S)
policies=[(('y','s2','s3','x2','s4'),('s5','z1','s1')),(('s2','y','s3','x2','s4'),('s1','z1','s5'))]
ledger=[];results=[]
for prefix,suffix in policies[:1 if pilot else 2]:
 policy=prefix+suffix
 for first in (0,1):
  root=make(child(vv,4,first),child(ww,4,first),pr=tuple(a for a in pn if a!='x1'),budget=budget);i0=I(root['h']);quota=96*i0
  total={'H':{},'U':{},'K':{},'Z':{},'Lambda':{},'R':F(0),'I':F(0),'oldprivate':F(0),'spent':F(0),'oldL':F(0),'mass':F(0)}
  def walk(st,depth,reach,path='',oldL=F(0),shared_before=0,frozen=None):
   guard();tt=TT(st);identity(st);zz=Z(st);kk=K(st);leq(plus((zz,F(-1))),0);leq(plus((kk,F(-1))),0)
   if depth==len(prefix):
    frozen=plus(({F(2):quota-oldL},F(1)),(zz,F(-1)))
    leq(plus((frozen,F(-1))),-3*i0);equal_expr(plus((zz,F(1)),(frozen,F(1)),({F(2):oldL-quota},F(1))));counts['handoffs']+=1
   live,p,c=geometry(st)
   row={'policy':list(policy),'first_x1':first,'path':path,'reach':str(reach),'address_codimension':c,'remaining_shared':list(st['sh']),'event_mass':str(p),'live_faces':list(live),'number_edited_vertices':sum(a!=0 for a in st['lab']),'profile_means':{str(a):str(mean(st['v'][a])) for a in (1,2)},'H_interval':[str(a) for a in bounds(H(tt))],'I':str(I(tt)),'U_interval':[str(a) for a in bounds(U(st))],'R':str(reserve(st)),'K_interval':[str(a) for a in bounds(kk)],'Z_interval':[str(a) for a in bounds(zz)],'Lambda_interval':None if frozen is None else [str(a) for a in bounds(frozen)],'old_shared_L':str(oldL),'original_Q':str(quota)}
   ledger.append(row)
   if depth==len(policy):
    row['full_terminal_spectrum']=[str(a) for a in coeff(tt)];row['V_spectrum']=[str(a) for a in coeff(st['v'][1])];row['W_spectrum']=[str(a) for a in coeff(st['v'][2])]
    for key,expr in [('H',H(tt)),('U',U(st)),('K',kk),('Z',zz),('Lambda',frozen)]:total[key]=plus((total[key],F(1)),(expr,reach))
    total['R']+=reach*reserve(st);total['I']+=reach*I(tt);total['oldL']+=reach*oldL;total['mass']+=reach;counts['mixed_leaves']+=1;return
   name=policy[depth];idx=(st['pr']+st['sh']).index(name);kids=[branch(st,name,b) for b in (0,1)];shared=name in st['sh'];ij=inf(tt,idx)
   for bit,kid in enumerate(kids):eq(TT(kid),child(tt,idx,bit))
   dh,du,dk,dr=local(st,kids);newL=oldL
   if depth<len(prefix):
    price=(5,15,38)[shared_before] if shared else 12
    leq(plus((dh,F(1)),(du,F(-1)),(dk,F(-1))),dr+price*ij)
    if shared:newL+=price*ij
    else:total['oldprivate']+=reach*ij
   elif name=='s5':counts['suffix_free_queries']+=1;counts['suffix_free_positive_influence']+=int(ij>0)
   elif name=='s1':counts['suffix_separator_queries']+=1
   if not shared:row['inherited_full_core_erasures']={str(a):[str(x) for x in bounds(B(st['v'][a],idx))] for a in (1,2)}
   row.update({'query':name,'actual_query_influence':str(ij),'old_charge':str(newL-oldL),'reserve_release':str(dr)})
   total['spent']+=reach*ij;counts['mixed_nodes']+=1
   walk(kids[0],depth+1,reach/2,path+name+'=0;',newL,shared_before+int(shared),frozen)
   walk(kids[1],depth+1,reach/2,path+name+'=1;',newL,shared_before+int(shared),frozen)
  walk(root,0,F(1));eq(total['mass'],F(1));eq(I(TT(root))-total['I'],total['spent'])
  lhs=plus((H(TT(root)),F(1)),(total['H'],F(-1)),(total['U'],F(1)),(U(root),F(-1)),(total['K'],F(1)),(total['Z'],F(1)),(total['Lambda'],F(1)),({F(2):total['R']},F(1)))
  leq(lhs,reserve(root)+budget+quota+12*total['oldprivate']);leq(plus((total['K'],F(-1))),-2*p0);leq(plus((total['Lambda'],F(-1))),-3*i0)
  results.append({'policy':list(policy),'first_x1':first,'original_I0':str(i0),'original_Q':str(quota),'source_mass':str(p0),'original_bent_entropy_allocation':str(4*p0),'original_surplus':str(S),'first_collision_debit':str(FIRST),'other_old_D0':str(D0),'original_B':str(budget),'old_shared_charge_expectation':str(total['oldL']),'expected_K_interval':[str(a) for a in bounds(total['K'])],'expected_Lambda_interval':[str(a) for a in bounds(total['Lambda'])],'guaranteed_K':str(2*p0),'guaranteed_Lambda':str(3*i0)})
  coeff.cache_clear()
save('MIXED_PILOT.json' if pilot else 'MIXED_LEDGER.json',{'status':'PASS','histories':results,'states':ledger})
save('PILOT.json' if pilot else 'VALIDATION.json',{'status':'PASS','assertions':A.checks,'counts':counts,'seconds':time.perf_counter()-start,'full_fei':'OPEN'})
print(json.dumps({'status':'PASS','pilot':pilot,'assertions':A.checks,'counts':counts,'seconds':time.perf_counter()-start}))
