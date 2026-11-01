from pathlib import Path
import sys,itertools,json,time,math
RUNDIR=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(RUNDIR/'code'))
import arithmetic as A
from arithmetic import F,coeff,H,I,inf,B,child,plus,Phi,phi,bounds,eq,leq,equal_expr
pilot='--pilot' in sys.argv;start=time.perf_counter();limit=55 if pilot else 180
counts={'root_pairs':0,'first_queries':0,'second_queries':0,'mixed_nodes':0,'mixed_leaves':0}
def guard():
 if time.perf_counter()-start>limit:raise RuntimeError('Frozen runtime limit; no escalation')
def save(name,x):(RUNDIR/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def delta(t,i):return plus((H(t),F(1)),(H(child(t,i,0)),F(-1,2)),(H(child(t,i,1)),F(-1,2)))
def variance(t):return 1-F(sum(t),len(t))**2
def xi(v,w,p):return plus(*[(plus((phi((a+b)**2),F(1,2)),(phi((a-b)**2),F(1,2)),(phi(a*a),F(-1)),(phi(b*b),F(-1))),p) for a,b in zip(coeff(v)[1:],coeff(w)[1:])])
def wrap(h,act,v,w):return tuple((v if act[s]=='v' else w)[x] if s in act else h[s] for s in range(len(h)) for x in range(len(v)))
def shared_check(t,h,act,v,w,j,order):
 n=len(v).bit_length()-1;p=F(1,len(h));mu=F(sum(v),len(v));nu=F(sum(w),len(w))
 m=tuple(mu if act.get(s)=='v' else nu if act.get(s)=='w' else h[s] for s in range(len(h)))
 ct=coeff(t);be=plus(*[(Phi(ct[s]**2,ct[s|(1<<(n+j))]**2),F(1)) for s in range(len(t)) if not s>>(n+j)&1 and s%len(v)==0])
 equal_expr(plus((be,F(1)),(B(m,j),F(-1))))
 release=p*(variance(v)+variance(w)) if act else F(0)
 leq(plus((B(t,n+j),F(1)),(be,F(-1))),release)
 leq(be,(2 if order==1 else 12)*inf(t,n+j))
 leq(delta(t,n+j),release+(5 if order==1 else 15)*inf(t,n+j))
 # Actual Boolean physical edges, including all original carrier pivots.
 eq(inf(t,n+j),F(sum(t[x]!=t[x^(1<<(n+j))] for x in range(len(t))),len(t)))
 if order==2:
  nn=len(h).bit_length()-1;alpha=F(math.comb(nn,nn//2),1<<nn)
  eq(inf(t,n+j),alpha+p*(2-mu-nu) if act else alpha)

domain=[(n,5) for n in range(2 if pilot else 3)]
if not pilot:domain += [(n,d) for d in (7,9) for n in (0,1)]
for n,d in domain:
 for v in itertools.product((-1,1),repeat=1<<n):
  for w in itertools.product((-1,1),repeat=1<<n):
   guard();h=tuple(1 if s.bit_count()<d/2 else -1 for s in range(1<<d));act={0:'v',1:'w'};t=wrap(h,act,v,w)
   shared_check(t,h,act,v,w,1,1);counts['first_queries']+=1;counts['root_pairs']+=1
   for answer in (0,1):
    hh=child(h,1,answer);aa={0:'v',1:'w'} if answer==0 else {};tt=child(t,n+1,answer)
    eq(tt,wrap(hh,aa,v,w));shared_check(tt,hh,aa,v,w,1,2);counts['second_queries']+=1
   coeff.cache_clear()
save('SECOND_QUERY_PILOT.json' if pilot else 'SECOND_QUERY.json',{'status':'PASS','counts':dict(counts),'exact_assertions':A.checks,'seconds':time.perf_counter()-start})

# k4,m2 original source, BOTH first x1 answers, early guard and two actual gates.
names=('z1','z2','z3','z4','x1','x2','y')
v0=tuple((-1 if z>>6&1 else 1)*(-1 if ((z&1)*(z>>1&1)+(z>>2&1)*(z>>3&1))%2 else 1) for z in range(128))
w0=tuple((-1 if z>>6&1 else 1)*(-1 if z%64==0 else 1) for z in range(128))
eq(I(v0),F(3));equal_expr(plus((H(v0),F(1)),({F(2):4},F(-1))))
e=F(1,32);S=11*e;old=4*e;D0=e;budget=S-old-D0
eq(budget>=4*e,True);eq(S,5*e*I(v0)-4*e)
policies=[('y','s2','z1','s3','x2'),('s2','y','s3','z1','x2'),('s2','z1','y','x2','s3')]
def table(st):return wrap(st['h'],st['act'],st['v'],st['w'])
def U(st):return plus(*[(H(st[a]),F(1,len(st['h']))) for a in st['act'].values()])
def reserve(st):return len(st['sh'])*F(1,len(st['h']))*sum((variance(st[a]) for a in st['act'].values()),F(0))
def bank(st):
 if not st['act']:return {}
 p=F(1,len(st['h']));return plus(({F(2):p*st['density']},F(1)),(xi(st['v'],st['w'],p),F(1)))
def branch(st,name,bit):
 out=dict(st)
 if name in st['pr']:
  j=st['pr'].index(name);out['pr']=tuple(a for a in st['pr'] if a!=name);out['v']=child(st['v'],j,bit);out['w']=child(st['w'],j,bit)
 else:
  j=st['sh'].index(name);out['sh']=tuple(a for a in st['sh'] if a!=name);out['h']=child(st['h'],j,bit);out['used']=st['used']+1
  act={}
  for s in range(len(out['h'])):
   oldindex=(s&((1<<j)-1))+((s>>j)<<(j+1))+(bit<<j)
   if oldindex in st['act']:act[s]=st['act'][oldindex]
  out['act']=act
 return out
states=[];summaries=[]
for policy in policies[:1 if pilot else 3]:
 for first in (0,1):
  v=child(v0,4,first);w=child(w0,4,first);h=tuple(1 if s.bit_count()<=2 else -1 for s in range(32))
  density=plus(({F(2):budget/e},F(1)),(xi(v,w,e),-1/e))
  # Density is a log expression; bank below uses it explicitly, not a rounded number.
  initial={'h':h,'act':{0:'v',1:'w'},'v':v,'w':w,'pr':tuple(a for a in names if a!='x1'),'sh':tuple('s'+str(j+1) for j in range(5)),'used':0,'density':density}
  def account(st):
   if not st['act']:return {}
   return plus((st['density'],F(1,len(st['h']))),(xi(st['v'],st['w'],F(1,len(st['h']))),F(1)))
  total={'H':{},'U':{},'R':F(0),'K':{},'price':F(0),'mass':F(0),'influence':F(0)}
  def walk(st,depth,reach,path):
   guard();t=table(st);kk=account(st);rr=reserve(st);uu=U(st);leq(plus((kk,F(-1))),0)
   entry={'policy':list(policy),'first_x1':first,'path':path,'reach':str(reach),'profile_means':[str(F(sum(st[a]),len(st[a]))) for a in ('v','w')],'H_interval':[str(a) for a in bounds(H(t))],'I':str(I(t)),'R':str(rr),'K_interval':[str(a) for a in bounds(kk)],'U_interval':[str(a) for a in bounds(uu)],'shared_used':st['used']}
   if depth==len(policy):
    entry['full_terminal_spectrum']=[str(a) for a in coeff(t)];entry['V_spectrum']=[str(a) for a in coeff(st['v'])];entry['W_spectrum']=[str(a) for a in coeff(st['w'])]
    total['H']=plus((total['H'],F(1)),(H(t),reach));total['U']=plus((total['U'],F(1)),(uu,reach));total['K']=plus((total['K'],F(1)),(kk,reach));total['R']+=reach*rr;total['mass']+=reach;counts['mixed_leaves']+=1;states.append(entry);return
   name=policy[depth];isprivate=name in st['pr'];j=st['pr'].index(name) if isprivate else len(st['pr'])+st['sh'].index(name)
   a,b=branch(st,name,0),branch(st,name,1);ta,tb=table(a),table(b);eq(ta,child(t,j,0));eq(tb,child(t,j,1))
   release=rr-(reserve(a)+reserve(b))/2;du=plus((uu,F(1)),(U(a),F(-1,2)),(U(b),F(-1,2)))
   residual=plus((H(t),F(1)),(H(ta),F(-1,2)),(H(tb),F(-1,2)),(du,F(-1)),(account(a),F(1,2)),(account(b),F(1,2)),(kk,F(-1)))
   price=12 if isprivate else 5 if st['used']==0 else 15
   leq(residual,release+price*inf(t,j));total['price']+=reach*price*inf(t,j);total['influence']+=reach*inf(t,j)
   eq(I(t)-(I(ta)+I(tb))/2,inf(t,j))
   if isprivate:
    entry['inherited_core_erasures']=[[str(a) for a in bounds(B(st[c],j))] for c in ('v','w')]
   states.append(entry);counts['mixed_nodes']+=1
   walk(a,depth+1,reach/2,path+name+'=0;');walk(b,depth+1,reach/2,path+name+'=1;')
  walk(initial,0,F(1),'')
  eq(total['mass'],F(1));leq(plus((total['K'],F(-1))),-(budget-4*e))
  residual=plus((H(table(initial)),F(1)),(total['H'],F(-1)),(total['K'],F(1)),(U(initial),F(-1)),(total['U'],F(1)))
  leq(residual,reserve(initial)+budget+total['price']-total['R'])
  summaries.append({'policy':list(policy),'first_x1':first,'original_surplus':str(S),'first_collision_debit':str(old),'other_old_debit':str(D0),'original_bent_entropy_allocation':str(4*e),'continuation_B':str(budget),'guaranteed_remaining':str(budget-4*e),'actual_expected_K_interval':[str(a) for a in bounds(total['K'])],'transaction_allowance':str(total['price'])})
save('MIXED_PILOT.json' if pilot else 'MIXED_LEDGER.json',{'status':'PASS','summaries':summaries,'states':states})
save('PILOT.json' if pilot else 'VALIDATION.json',{'status':'PASS','counts':counts,'exact_assertions':A.checks,'seconds':time.perf_counter()-start,'full_fei':'OPEN'})
print(json.dumps({'status':'PASS','pilot':pilot,'counts':counts,'exact_assertions':A.checks,'seconds':time.perf_counter()-start}))
