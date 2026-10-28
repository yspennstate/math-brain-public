from pathlib import Path
from fractions import Fraction as F
import json,time
import intervals as a
B=Path(__file__).resolve().parents[1];start=time.monotonic();C=0;theta=F(1,6)
def ck(v):
 global C
 C+=1
 if not v:raise AssertionError(C)
def ce(p,q):
 s=a.const(0)
 for x,y in zip(p,q):
  if x:s=a.sub(s,a.scale(a.log2(y),x))
 return s
def kl(v,q):return a.sub(ce(a.spec(v),q),a.entropy(a.spec(v)))
def overlap(u,v):return max(u[0],v[0])<=min(u[1],v[1])
def same(v,q):return all(bool(x)==bool(y) for x,y in zip(a.spec(v),q))
def ref(v):
 p=a.spec(v);n=(len(v)-1).bit_length();E=sum(1<<i for i in range(n) if a.influence(v,i))
 if not E:return p
 q=[p[0]]+[(1-theta)*x for x in p[1:]];q[E]+=theta*(1-p[0])
 ck(sum(q)==1);return q
def act(v,q,eps):
 vv=tuple(eps if not x&1 else v[x>>1] for x in range(2*len(v)));p=a.spec(vv);Q=[F(0)]*len(p);Q[:2]=p[:2]
 for s in range(1,len(q)):Q[2*s]=Q[2*s+1]=q[s]/4
 ck(sum(Q)==1);return vv,Q
def h(m,k,r):
 out=[]
 for x in range(1<<(m+k)):
  t=x&((1<<m)-1);z=x>>m;y=(-1)**(z&1)
  if z in (2,3):y=-y
  if z==0 and t.bit_count()%3==r:y=-y
  out.append(y)
 return tuple(out)
rho=[[F(1),F(0),F(0)]];alt=[list(rho[0])]
for m in range(1,15):
 rho.append([(rho[-1][r]+rho[-1][(r-1)%3])/2 for r in range(3)])
 alt.append([(alt[-1][r]-alt[-1][(r-1)%3])/2 for r in range(3)])
def mm(A,D):return [[sum(A[i][k]*D[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
T=[[F((i==j)-(j==(i-1)%3),2) for j in range(3)] for i in range(3)]
T6=[[F(i==j) for j in range(3)] for i in range(3)]
for _ in range(6):T6=mm(T6,T)
ck(T6==[[-F(27,64)*(F(i==j)-F(1,3)) for j in range(3)] for i in range(3)])
for m in range(1,9):
 ck(alt[m+6]==[-F(27,64)*x for x in alt[m]])
 ck(sum(alt[m])==0)
for m in range(2,15):
 ds=[]
 for r in range(3):
  x,y=alt[m-1][r],alt[m-1][(r-1)%3];ck(x*x+y*y>0)
  d=(x*x-y*y)/(x*x+y*y);ds.append(d)
 ck(sum(bool(x) for x in ds)==2)
 ck(all(not x or abs(x)>=F(3,5) for x in ds))
 if m%2==0:ck(all(alt[m][r] for r in range(3)))
def eta(m,k,r):
 delta=F(1,2**k);mu=-2*delta*rho[m][r];u=mu*mu
 x,y=alt[m-1][r],alt[m-1][(r-1)%3];d=(x*x-y*y)/(x*x+y*y)
 x0,y0=rho[m-1][r],rho[m-1][(r-1)%3];d0=(x0*x0-y0*y0)/(x0*x0+y0*y0)
 return theta*(u*d0+(1-u)*d),d
for m in range(2,13,2):
 for k in (4,5,6,7,8):
  for r in range(3):
   e,d=eta(m,k,r)
   if d:ck(abs(e)>F(1,12))
   else:ck(abs(e)<=8*theta*F(1,2**(2*k)))
phase={'T6':[[str(x) for x in row] for row in T6],'alt_vectors':[[str(x) for x in row] for row in alt],'rho_vectors':[[str(x) for x in row] for row in rho],'exact_identity':'T^6=-(27/64)(I-J/3), and alt_m has sum0 for m>=1','good_states':'Exactly2of3 residues have |d_full|>=3/5; every even m>=2 has nonzero full coefficient for all residues'}
(B/'out/PHASE_CERTIFICATE.json').write_text(json.dumps(phase,indent=2)+'\n',encoding='utf8')
dense=[]
for m,k,r in [(4,4,r) for r in range(3)]+[(6,4,r) for r in range(3)]+[(8,4,0)]:
 v=h(m,k,r);p=a.spec(v);q=ref(v);ck(same(v,q))
 ck(p[0]==4*F(1,2**(2*k))*rho[m][r]**2)
 ck(p[-1]==4*F(1,2**(2*k))*alt[m][r]**2>0)
 ch,old=a.node(v,q,0)
 # Reconstruct the ACTUAL first reference outcome law independently.
 coeff=a.walsh(v);r0=F(0)
 for t in range(len(v)//2):
  pm=p[2*t]+p[2*t+1];qm=q[2*t]+q[2*t+1]
  kernel=(coeff[2*t]+coeff[2*t+1])**2/(2*pm) if pm else F(1,2)
  r0+=qm*kernel
 e,d=eta(m,k,r);ck(2*r0-1==e)
 outcome=a.scale(a.log2(1-e*e),F(-1,2));ck(outcome[0]>=0)
 grandchildren=[];incoming=[]
 for branch in (0,1):
  ck(same(ch[branch],old[branch]))
  cs,qs=a.node(ch[branch],old[branch],0)
  grandchildren.extend(cs);incoming.extend(qs)
 inherited=a.const(0);fresh=a.const(0)
 for index,(vv,qq) in enumerate(zip(grandchildren,incoming)):
  first=index//2;second=index%2
  ck(vv==h(m-2,k,(r-first-second)%3))
  rr=ref(vv);ck(same(vv,qq) and same(vv,rr))
  inherited=a.add(inherited,a.scale(kl(vv,qq),F(1,4)));fresh=a.add(fresh,a.scale(kl(vv,rr),F(1,4)))
 release=a.sub(kl(v,q),inherited);sig=a.sub(fresh,inherited)
 ck(release[1]>=outcome[0])
 ck(overlap(sig,a.add(a.sub(fresh,kl(v,q)),release)))
 dense.append({'m':m,'k':k,'r':r,'eta':str(e),'first_outcome_KL':a.outiv(outcome),'two_query_release':a.outiv(release),'actual_block_reset':a.outiv(sig),'same_support_all_nodes':True})

# Independent reconstruction of incoming A036 activation witnesses.
incoming_cases=[]
for k in (5,6):
 delta=F(1,2**k);oldv=[]
 for x in range(1<<(k+1)):
  j=x&1;z=x>>1;y=(-1)**(z&1)
  if z in (2,3):y=-y
  if j and z==0:y=-y
  oldv.append(y)
 oldv=tuple(oldv);ck(a.influence(oldv,0)==delta)
 for eps in (-1,1):
  vv,Q=act(oldv,ref(oldv),eps);cs,qs=a.node(vv,Q,1)
  sig=a.const(0)
  for bit in (0,1):
   core=tuple(a.restrict(oldv,0,bit));child,rr=act(core,ref(core),eps)
   ck(child==cs[bit] and same(child,rr) and same(child,qs[bit]))
   sig=a.add(sig,a.scale(a.sub(kl(child,rr),kl(child,qs[bit])),F(1,2)))
  # Reconstruct the source's closed formula with rigorous logarithms.
  ee=delta*delta;V=a.const(0)
  for c in (-1,1):
   Ac=(1-2*c*eps*delta+2*ee)/4
   V=a.add(V,a.scale(a.log2(1-ee/(24*Ac)),Ac))
  R=F(8192,3125)*(1+49*ee)**5/((1+80*ee)**4*(1+16*ee))
  et=F(1,6)*(F(3,10)-F(4,5)*ee-ee*(1+2*ee)/(2*(1+4*ee*ee)))
  formula=a.sub(a.add(V,a.scale(a.log2(R),ee)),a.scale(a.log2(1-et*et),F(1,2)))
  bound=a.scale(a.div(a.const(1),a.lnsmall(F(2))),F(1,2048))
  ck(overlap(sig,formula));ck(sig[0]>bound[1])
  incoming_cases.append({'k':k,'eps':eps,'sigma_interval':a.outiv(sig)})

# One complete original F_h source is exposed through b/x, no free reset.
v=h(4,4,0);q=ref(v);fv=a.fixture(v);pf=a.spec(fv);Q=[F(0)]*len(pf);Q[:8]=pf[:8]
for s in range(1,len(q)):
 for c in (0,1,4,5):Q[8*s+c]=q[s]/16
ck(sum(Q)==1 and same(fv,Q))
bc,bq=a.node(fv,Q,2);xc,xq=a.node(bc[1],bq[1],0)
expected=tuple(v[x>>1] for x in range(2*len(v)));embedded=[F(0)]*(2*len(q));embedded[::2]=q
ck(xc[1]==expected and xq[1]==embedded)
ck(overlap(kl(fv,Q),a.scale(kl(v,q),F(1,4))))

# Analytic all-dimension bounds and one actual Boolean family member.
ck(F(12*10,2**10)<1 and F(12*(3*10+2),2**10)==F(3,8))
ck(6**15<2**4*5**15)
N=65536;global_bill_lower=F(N-4,4608)-F(1,15);source_margin_upper=F(8)
ck(global_bill_lower==F(9059,640))
ck(global_bill_lower-source_margin_upper==F(3939,640)>0)
ck(F(1277,256)-(3+(F(3,8)+F(4,15))/4)>F(3,2))
account={'tail_bits':N,'z_bits':N,'original_F_dimension':2*N+3,'reset_blocks':N//2-1,'query_count':N-2,'source_margin_strict_lower':'3/2','source_margin_upper':'8','cumulative_global_sigma_strict_lower':str(global_bill_lower),'signed_net_shortfall_strict_lower':str(global_bill_lower-source_margin_upper),'old_quarter':'Retained; only worsens shortfall','meaning':'Exact analytic counterexample to unlimited prescribed same-profile full-spike reset payment; not a FEI counterexample'}
stress=[]
for r in range(3,11):
 copies=2**r;guards=2*(r+1);alpha=F(1,2**guards)
 deficit=alpha*(copies*F(3939,640)-4*(guards+1))
 ck(deficit>0)
 stress.append({'T':copies,'activation_controls':guards,'alpha':str(alpha),'remaining_deficit_strict_lower':str(deficit),'influence_upper':str(alpha*(guards+1+2*copies))})
account['sparse_tensor_cases']=stress
(B/'out/ACCOUNT_CERTIFICATE.json').write_text(json.dumps(account,indent=2)+'\n',encoding='utf8')
out={'status':'PASS','assertions':C,'channel_assertions':a.COUNT,'dense_blocks':dense,'incoming_A036':incoming_cases,'scalar_bias_cases':90,'period_certificate':'out/PHASE_CERTIFICATE.json','account':'out/ACCOUNT_CERTIFICATE.json','runtime_seconds':time.monotonic()-start}
(B/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ('status','assertions','channel_assertions','scalar_bias_cases','runtime_seconds')}))
