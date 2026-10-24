import json,time
from fractions import Fraction as F
from helper import c
start=time.perf_counter()
def scale(e,a):
 z={};c.add(z,e,a);return z
def sub(a,b):
 z=dict(a);c.add(z,b,-1);return z
def avg(a,b):
 z=scale(a,F(1,2));c.add(z,b,F(1,2));return z
def serial(e):return c.b.serial(e)
def record(e):
 lo,hi=c.interval(e);return {'prime_logs':serial(e),'lower':str(lo),'upper':str(hi)}
def eta(t):
 e={}
 if t:c.b.addlog(e,t.numerator,-t);c.b.addlog(e,t.denominator,t)
 return e
def point(d):
 N=1<<d;delta=F(1,N);empty=(1-2*delta)**2;atom=4*delta**2
 assert empty+(N-1)*atom==1
 H=eta(empty);c.add(H,eta(atom),N-1)
 return H,2*d*delta
rows=[]
for d in range(1,13):
 delta=F(1,1<<d);H,I=point(d);S4=sub(c.const(2*I),scale(H,F(1,2)));V=c.phi(delta,1-delta)
 c.positive(sub(c.const(4*I),H))
 if d>=4:c.positive(sub(sub(V,S4),c.const(delta*(d-5))))
 Ht,It=point(2*d);St=sub(c.const(4*It),Ht);c.positive(St)
 Snew=dict(S4);c.add(Snew,St)
 if d>=8:c.positive(sub(sub(V,Snew),c.const(delta*(d-F(11,2)))))
 # Source Q, complete inherited Maj3 bill; full normalized point laws retained.
 Q=c.phi((1-delta)**2,delta**2);c.add(Q,c.const(2*delta*(1-delta)))
 rows.append({'d':d,'delta':str(delta),'V':record(V),'S4':record(S4),'V_minus_S4':record(sub(V,S4)),'both_nonconstant_tensor_V_minus_S4':record(sub(V,Snew)),'actual_retained_Q_minus_S4':record(sub(Q,S4)),'inherited_delta_separate':str(delta)})
 c.dump('point_capacity_controls.json',{'status':'PASS','cases':len(rows),'rows':rows,'note':'All-dimensional conclusions PROOF section3; inherited Maj3 charge is recorded separately.'})
b=tuple(1 if x&7==0 else -1 for x in range(64));minus=list(b);minus[0]=-minus[0];minus=tuple(minus)
f=tuple(y for pair in zip(minus,b) for y in pair);h=tuple(1 if x.bit_count()>=2 else -1 for x in range(8))
s=c.shadow(f);actual=c.physical(c.compose(f,h));gp=c.physical(b);gm=c.physical(minus)
assert gp['I']==gm['I']==F(3,4) and s['delta']==F(1,64)
c.positive(sub(c.const(4*gp['I']),gp['H']));c.positive(sub(c.const(4*gm['I']),gm['H']))
T=avg(gp['H'],gm['H']);Idata=sum(actual['d'][3:]);assert Idata==F(3,4)
S4=sub(c.const(4*Idata),T);R0=sub(S4,s['B']);c.add(R0,c.const(-s['delta']));c.positive(R0)
queryrows=[]
for j in range(6):
 fs=[c.split(f,j+1,v) for v in [0,1]];ss=[c.shadow(z) for z in fs];As=[c.physical(c.compose(z,h)) for z in fs]
 Ts=[avg(c.physical(z['gp'])['H'],c.physical(z['gm'])['H']) for z in ss];Tchild=avg(*Ts);Db=sub(T,Tchild)
 Qchild=avg(ss[0]['B'],ss[1]['B']);Hchild=avg(As[0]['H'],As[1]['H']);Df=sub(actual['H'],Hchild)
 assert (ss[0]['delta']+ss[1]['delta'])/2==s['delta']
 M=dict(S4);c.add(M,Db);c.add(M,Df,-1);c.add(M,Qchild,-1);c.add(M,c.const(-s['delta']));c.positive(M)
 debit=dict(Df);c.add(debit,Qchild);c.add(debit,s['B'],-1);c.add(debit,Db,-1);assert sub(R0,debit)==M
 extra=sub(Hchild,Tchild);c.add(extra,Qchild,-1);c.add(extra,c.const(-s['delta']))
 full=sub(M,extra);assert full==sub(c.const(4*Idata),actual['H']);c.positive(full)
 Vchild=avg(ss[0]['h2'],ss[1]['h2']);release=sub(s['h2'],Vchild);c.positive(release)
 queryrows.append({'data_coordinate':j,'class':'active' if j<3 else 'dummy','physical_I':str(actual['d'][3+j]),'original_bank_S4':record(S4),'original_booked_margin':record(R0),'signed_new_debit':record(debit),'remaining_margin':record(M),'complete_terminal_entropy_after_query':record(Tchild),'remaining_actual_encoder_correction':record(extra),'margin_after_all_actual_decrements':record(full),'information_reserve_release':record(release),'child_product_influences':[str(z['Ip']) for z in ss]})
 c.dump('neutral_query_controls.json',{'status':'PASS','cases':len(queryrows),'rows':queryrows,'note':'Six alternative first queries, each starts with the same booked root bank; their margins are NOT added.'})
 assert time.perf_counter()-start<60
result={'status':'PASS','point_dimensions':12,'both_nonconstant_point_tensor_dimensions':12,'neutral_first_queries':6,'elapsed_seconds':time.perf_counter()-start}
c.dump('controls_summary.json',result);print(json.dumps(result))
