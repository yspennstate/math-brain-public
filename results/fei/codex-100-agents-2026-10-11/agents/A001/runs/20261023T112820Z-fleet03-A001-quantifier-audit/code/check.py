from helpers import *
import helpers

@lru_cache(None)
def P(v): return tuple(spectrum(v))
@lru_cache(None)
def H(v): return entropy(P(v))
@lru_cache(None)
def CE(p,q):
 ck(len(p)==len(q) and sum(p)==1 and 0<sum(q)<=1)
 ck(all(b>0 for a,b in zip(p,q) if a))
 return add(*[(-a,log(b)) for a,b in zip(p,q) if a])
def nonnegative(d): return not d or interval(d)[0]>=0
def marginal(q,j): return tuple(q[insert(t,j,0)]+q[insert(t,j,1)] for t in range(len(q)//2))
def inherit(v,Q,j):
 children=[tuple(transport(v,j,b)) for b in (0,1)];pc=[P(vv) for vv in children]
 m=marginal(P(v),j);r=marginal(Q,j);s=sum(Q)
 ck(tuple((a+b)/2 for a,b in zip(*pc))==m)
 raw=[tuple(r[t]*a/m[t] if m[t] else r[t] for t,a in enumerate(p)) for p in pc]
 zs=[sum(q) for q in raw];ck(sum(zs)==2*s and min(zs)>0)
 refs=[tuple(s*a/z for a in q) for q,z in zip(raw,zs)]
 ck(all(sum(q)==s for q in refs))
 Dparent=add((1,CE(P(v),Q)),(-1,H(v)))
 Dchild=add(*[(F(1,2),add((1,CE(p,q)),(-1,entropy(p)))) for p,q in zip(pc,refs)])
 ck(nonnegative(add((1,Dparent),(-1,Dchild))))
 return children,refs

def model(g,R,b,edited=True):
 a=len(g).bit_length()-1;n=a+b;t=F(1,1<<n);rho=t/2
 v=tuple(g[y&((1<<a)-1)]*(-1 if edited and y==0 and c==0 else 1) for y in range(1<<n) for c in (0,1))
 if not edited:
  Q=tuple(R[y] if c==0 and y<len(R) else F(0) for y in range(1<<n) for c in (0,1))
 else:
  data=P(v);q=tuple(data[2*y]+data[2*y+1] for y in range(1<<n));ck(min(q)>0)
  floor=tuple(((R[y] if y<len(R) else 0)+6*rho*t)/(1+6*rho) for y in range(1<<n))
  Q=tuple(floor[y]*data[2*y+c]/q[y] for y in range(1<<n) for c in (0,1))
  ck(sum(Q)==(sum(R)+6*rho)/(1+6*rho))
 CE(P(v),Q)
 return {'v':v,'Q':Q,'w':F(1),'g':g,'R':R,'b':b}

def mix(Q,style):
 if len(Q)==1:return Q,False
 tail=sum(Q[1:]);N=len(Q)-1
 if style=='uniform':T=(F(1,N),)*N
 else:
  z=min(range(1,len(Q)),key=lambda t:Q[t]);T=tuple(F(t==z) for t in range(1,len(Q)))
 out=(Q[0],)+tuple(F(3,4)*a+F(1,4)*tail*t for a,t in zip(Q[1:],T))
 ck(sum(out)==sum(Q) and out[0]==Q[0])
 ck(all(b>=F(3,4)*a for a,b in zip(Q[1:],out[1:])))
 return out,out!=Q

def data_shape(Q):
 if len(Q)<4:return None
 d=tuple(Q[2*t]+Q[2*t+1] for t in range(len(Q)//2));tail=sum(d[1:])
 return tuple(x/tail for x in d[1:]) if tail else None

def rec(d):
 lo,hi=interval(d)
 return {'prime_log':enc(d),'interval':[str(lo),str(hi)]}

start=time.perf_counter();rows=[];snapshots={};positive=changed=constants=data_changes=0
seeds=[]
for a in (1,2):
 for mask in range(1,(1<<(1<<a))-1):seeds.append((f'n{a}-table{mask}',tuple(1 if mask>>x&1 else -1 for x in range(1<<a))))
seeds += [('AND3',tuple(-1 if x==0 else 1 for x in range(8))),('parity3',tuple((-1)**x.bit_count() for x in range(8))),('Maj3',tuple(1 if x.bit_count()<=1 else -1 for x in range(8))),('nonpoint4',tuple(-1 if x in (0,1,2,4,8) else 1 for x in range(16)))]
ck(len(seeds)==20)
if '--pilot' in sys.argv:seeds=[seeds[0],seeds[-1]]
for name,g in seeds:
 Ig=totalinf(g);a=len(g).bit_length()-1;pg=P(g)
 ck(Ig>=F(2*a,1<<a))
 for reference in ('exact','half-mass'):
  R=pg if reference=='exact' else tuple((x+F(1,len(g)))/4 for x in pg)
  c=CE(pg,R);C0=F((16*interval(c)[1]/Ig).__ceil__(),16);K=4*C0+15;U=(C0+F(37,8))*Ig
  ck(nonnegative(add((1,const(C0*Ig)),(-1,c))))
  ck(nonnegative(add((1,c),(-1,H(g)),(1,log(sum(R))))))
  active=model(g,R,2);rootv=active['v'];Hroot=H(rootv);IF=totalinf(rootv)
  ck(IF==sum((F(S.bit_count())*mass for S,mass in enumerate(P(rootv))),F(0)))
  varroot=1-F(sum(rootv),len(rootv))**2;ck(varroot<=F(9,8)*Ig)
  stopped=[];old=CE(P(rootv),active['Q']);decrement={};stages=1+2+a
  for stage in range(stages):
   leaves=stopped+[active];ck(sum(z['w'] for z in leaves)==1)
   direct=add((1,Hroot),*[(z['w'],add((1,CE(P(z['v']),z['Q'])),(-1,H(z['v'])))) for z in leaves])
   terminal=add(*[(z['w'],CE(P(z['v']),z['Q'])) for z in leaves]);ck(old==direct==add((1,decrement),(1,terminal)))
   margin=add((1,const(K*IF-U)),(-1,old));ck(nonnegative(add((1,margin),(-1,const(F(7,8)*Ig)))))
   variance=sum((z['w']*(1-F(sum(z['v']),len(z['v']))**2) for z in leaves),F(0));ck(variance<=varroot)
   for style in ('uniform','point'):
    Z={};fresh=[]
    for z in leaves:
     Qnew,genuine=mix(z['Q'],style);price=add((1,CE(P(z['v']),Qnew)),(-1,CE(P(z['v']),z['Q'])))
     var=1-F(sum(z['v']),len(z['v']))**2
     ck(nonnegative(add((var,log(F(4,3))),(-1,price))))
     if not var:ck(not price);constants+=1
     if genuine:changed+=1
     if data_shape(z['Q']) is not None and data_shape(Qnew) is not None and data_shape(z['Q'])!=data_shape(Qnew):data_changes+=1
     if price and interval(price)[0]>0:positive+=1
     Z=add((1,Z),(z['w'],price));fresh.append((z,Qnew))
    ck(interval(add((1,const(F(15,32)*Ig)),(-1,Z)))[0]>0)
    newmargin=add((1,margin),(-1,Z));ck(interval(add((1,newmargin),(-1,const(F(13,32)*Ig))))[0]>0)
    freshdirect=add((1,decrement),*[(z['w'],CE(P(z['v']),Qnew)) for z,Qnew in fresh]);ck(freshdirect==add((1,old),(1,Z)))
    rows.append({'seed':name,'reference':reference,'stage':stage,'target':style,'Ig':str(Ig),'IF':str(IF),'original_C0':str(C0),'old_booking_U':str(U),'reached_variance':str(variance),'original_reserve_before':rec(margin),'reached_conversion_charge':rec(Z),'original_reserve_after':rec(newmargin),'complete_terminals':len(leaves)})
   if name=='parity3' and reference=='exact' and stage==1:snapshots['parity']=(leaves,old,decrement,U,K,IF,Ig)
   if stage==stages-1:break
   w=active['w'];v=active['v'];Q=active['Q']
   if active['b']:
    j=1+(len(active['g']).bit_length()-1);c0=model(active['g'],active['R'],active['b']-1);c1=model(active['g'],active['R'],active['b']-1,False)
   else:
    j=1;gg,RR=inherit(active['g'],active['R'],0);c0=model(gg[0],RR[0],0);c1=model(gg[1],RR[1],0,False)
   c0['w']=c1['w']=w/2
   ck(tuple(transport(v,j,0))==c0['v'] and tuple(transport(v,j,1))==c1['v'])
   dH=add((1,H(v)),(F(-1,2),H(c0['v'])),(F(-1,2),H(c1['v'])));ck(nonnegative(dH))
   event=add((1,dH),(F(1,2),CE(P(c0['v']),c0['Q'])),(F(1,2),CE(P(c1['v']),c1['Q'])),(-1,CE(P(v),Q)))
   old=add((1,old),(w,event));decrement=add((1,decrement),(w,dH));stopped.append(c1);active=c0
   ck(time.perf_counter()-start<spec['max_runtime_seconds'])

witness=None
if '--pilot' not in sys.argv:
 leaves,old,decrement,U,K,IF,Ig=snapshots['parity'];off=leaves[0];ch,refs=inherit(off['v'],off['Q'],1)
 ck(P(off['v'])==off['Q'] and P(ch[0])==P(ch[1])==refs[0]==refs[1])
 ck(P(off['v'])[1<<1]==off['Q'][1<<1]==0)
 ck(not add((1,H(off['v'])),(F(-1,2),H(ch[0])),(F(-1,2),H(ch[1]))))
 Z={}
 for v,Q in zip(ch,refs):
  Qnew=tuple(F(3,4)*mass+F(t==2,4) for t,mass in enumerate(Q));ck(Q[2]==0 and sum(Qnew)==sum(Q) and Qnew[0]==Q[0]);ck(data_shape(Q)!=data_shape(Qnew))
  price=add((1,CE(P(v),Qnew)),(-1,CE(P(v),Q)));ck(price==log(F(4,3)))
  Z=add((1,Z),(off['w']/2,price))
 ck(Z==add((F(1,2),log(F(4,3)))))
 remaining=add((1,const(K*IF-U)),(-1,old),(-1,Z));ck(interval(add((1,remaining),(-1,const(F(13,32)*Ig))))[0]>0)
 witness={'actual_matched_isospectral':True,'genuine_nonempty_data_change':True,'target_frequency':2,'local_query_refund':'0','query_membership_erasure':'0','positive_reached_reset':rec(Z),'same_old_U':str(U),'remaining_original_account':rec(remaining),'both_new_terminals_and_old_siblings_retained':True}
ck(4**12<2**5*3**12)
out={'status':'PASS','exact_assertions':helpers.count,'case_count':len(rows),'positive_leaf_prices':positive,'genuine_leaf_changes':changed,'constant_terminal_costs_retained':constants,'genuine_conditional_nonempty_data_changes':data_changes,'elapsed_seconds':time.perf_counter()-start,'witness':witness,'rows':rows}
(RUN/'out'/('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8',newline='')
print(json.dumps({k:v for k,v in out.items() if k not in ['rows','witness']}))
