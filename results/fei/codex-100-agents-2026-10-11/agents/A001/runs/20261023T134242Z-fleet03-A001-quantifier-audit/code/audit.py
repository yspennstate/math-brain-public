from helpers import *
import helpers,itertools
start=time.perf_counter(); pilot='--pilot' in sys.argv
def kl(p,q):
 ck(sum(p)==1 and 0<sum(q)<=1)
 ck(all(not x or y>0 for x,y in zip(p,q)))
 return add(*[(x,log(x/y)) for x,y in zip(p,q) if x])
def ce(p,q):return add((1,entropy(p)),(1,kl(p,q)))
def ge(d):ck(not d or interval(d)[0]>=0)
def gt(d):ck(interval(d)[0]>0)
def floorref(v,a,m,source_mass=F(1)):
 p=spectrum(v);e=F(1,1<<(a+m));pg=spectrum([v[2*x] if x else -v[0] for x in range(1<<a)])
 # Recover actual pre-edit source: selector=0 at x=0 is the unique flipped value.
 r=[((source_mass*pg[t] if t<len(pg) else 0)+3*e*e)/(1+3*e) for t in range(len(p)//2)]
 q=[p[2*t]+p[2*t+1] for t in range(len(r))]
 ck(all(q));return [r[t//2]*p[t]/q[t//2] for t in range(len(p))]
def inherited(v,Q,j):
 s=sum(Q);p=spectrum(v);pc=[spectrum(restrict(v,j,z)) for z in (0,1)]
 marg=[p[insert(t,j,0)]+p[insert(t,j,1)] for t in range(len(p)//2)]
 rm=[Q[insert(t,j,0)]+Q[insert(t,j,1)] for t in range(len(p)//2)]
 raw=[[rm[t]*pc[z][t]/marg[t] if marg[t] else rm[t] for t in range(len(marg))] for z in (0,1)]
 zz=list(map(sum,raw));ck(sum(zz)==2*s)
 out=[[s*x/zz[z] for x in raw[z]] for z in (0,1)]
 ck(all(sum(x)==s for x in out));return out
profiles=[];pathrows=[]
for a in range(2 if pilot else 4):
 for tail in itertools.product((-1,1),repeat=(1<<a)-1):
  g=(1,)+tail;amps=amplitudes(g);aa=[x for x in amps if x];N=len(aa)
  for m in (3,5,8):
   e=F(1,1<<(a+m));u=F(1,1<<m);M=1/e;W=2*e-N*e*e
   qold=[A*A-2*e*A+2*e*e for A in aa]
   rold=[(A*A+3*e*e)/(1+3*e) for A in aa]
   x=2*e*(1-N*e);y=3*e*(1-N*e)/(1+3*e)
   pf=qold+([x] if x else []);rf=rold+([y] if x else [])
   Df=kl(pf,rf)
   Dc=add(*[((A-e)**2,log((A-e)**2/((1-W)*A*A))) for A in aa if A!=e])
   chi=sum((q-r)**2/r for q,r in zip(pf,rf))
   oldchi=sum((q-r)**2/r for q,r in zip(qold,rold))
   ck(oldchi<=F(1681,64)*N*e*e)
   ck(chi-oldchi<=e/3)
   C=F(1,2)+F(5043,128)*u
   gt(add((1,const(C*e)),(-1,Df)))
   ck(C*u<=F(5555,8192));ck(F(7,8)-F(5555,8192)==F(1613,8192))
   ge(Df);ge(Dc)
   if m>=8:
    gt(add((1,Df),(-1,Dc),(-1,const(F(23,512)*e))))
    gt(add((1,const(e)),(-1,Df),(1,Dc)))
   profiles.append({'a':a,'m':m,'g':list(g),'Dfloor':record(Df),'Dcanonical':record(Dc),'C':str(C)})
  if pilot or a==0 or a>2 or totalinf(g)==0:continue
  m=3;v=tuple(g[y%len(g)]*(-1 if y==0 and s==0 else 1) for y in range(1<<(a+m)) for s in (0,1))
  p=spectrum(v);Ig=totalinf(g);IF=totalinf(v);Hroot=entropy(p);C0=F(4);K=31;U=F(69,8)*Ig
  ge(add((C0*Ig,const(1)),(-1,entropy(spectrum(g)))))
  for order,source_mass in itertools.product(itertools.permutations(range(a)),(F(1),F(1,2))):
   Q=floorref(v,a,m,source_mass)
   ge(add((1,const(C0*Ig)),(-1,ce(spectrum(g),[source_mass*x for x in spectrum(g)]))))
   cv=v;cQ=Q;remaining=list(range(a));reach=F(1);querybill={};signed={};extra={};siblings={};positive={}
   for orig in order:
    j=remaining.index(orig)+1;inheritedQ=inherited(cv,cQ,j)
    child=[tuple(restrict(cv,j,s)) for s in (0,1)];cp=[spectrum(z) for z in child]
    release=add((1,kl(spectrum(cv),cQ)),*[(F(-1,2),kl(cp[s],inheritedQ[s])) for s in (0,1)])
    ge(release)
    querybill=add((1,querybill),(reach,entropy(spectrum(cv))),*[(F(-reach,2),entropy(cp[s])) for s in (0,1)])
    signed=add((1,signed),(-reach,release));siblings=add((1,siblings),(reach/2,ce(cp[1],inheritedQ[1])))
    reach/=2;remaining.remove(orig);cv=child[0];cQ=inheritedQ[0]
    target=floorref(cv,len(remaining),m);debit=add((1,ce(cp[0],target)),(-1,ce(cp[0],cQ)))
    if debit and interval(debit)[0]>0:
     positive=add((1,positive),(reach,debit))
    elif debit:
     ck(interval(debit)[1]<0);extra=add((1,extra),(-reach,debit))
    signed=add((1,signed),(reach,debit));cQ=target
    terminal=add((1,siblings),(reach,ce(spectrum(cv),cQ)))
    lhs=add((1,ce(p,Q)),(1,signed))
    ck(lhs==add((1,querybill),(1,terminal)))
    # Preserve all old U and account for every complementary full terminal.
    booked=add((1,lhs),(1,extra))
    gt(add((1,const(K*IF-U)),(-1,booked),(-1,const(F(1613,8192)*Ig))))
   e0=F(1,1<<(a+m));C=F(1,2)+F(5043,128)*F(1,1<<m)
   gt(add((1,const((a+1)*C*e0)),(-1,positive)))
   pathrows.append({'a':a,'g':list(g),'order':list(order),'source_mass':str(source_mass),'initial_full_reference_mass':str(sum(Q)),'positive_booking':record(positive),'discarded_negative_reset_credit':record(extra),'final_signed_bill':record(lhs),'final_positive_booked_bill':record(booked),'original_influence':str(IF),'retained_old_U':str(U)})
result={'status':'PASS','pilot':pilot,'profiles':len(profiles),'source_paths':len(pathrows),'exact_assertions':helpers.count,'runtime_seconds':time.perf_counter()-start,'profiles_data':profiles,'paths_data':pathrows}
(RUN/'out'/('PILOT.json' if pilot else 'CERTIFICATE.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if not k.endswith('_data')}))
