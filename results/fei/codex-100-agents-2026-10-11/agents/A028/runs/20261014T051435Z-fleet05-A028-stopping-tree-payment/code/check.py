from exact import *
import exact as E

count=0; partial_count=0; prefix_count=0
def cert(term):
 check(not term or enclosure(term)[0]>=0)
def case(na,a,k,ng,g,nh,h):
 global count,partial_count,prefix_count
 N=1<<k; p=F(a.count(-1),len(a)); V=4*p*(1-p)
 ga=tuple(F(x,len(g)) for x in walsh(g)); hb=tuple(F(x,len(h)) for x in walsh(h))
 data_g=tuple(g[z+(x<<k)] for y in range(1<<nh) for x in range(1<<ng) for z in range(N))
 data_h=tuple(h[z+(y<<k)] for y in range(1<<nh) for x in range(1<<ng) for z in range(N))
 f=tuple(data_h[x] if sign==-1 else data_g[x] for sign in a for x in range(len(data_g)))
 gamma=F(sum(x!=y for x,y in zip(data_g,data_h)),len(data_g))
 H,I=stats(f)[2:]; Hp_a=stats(a)[1]; Ia=stats(a)[3]
 Hg,Ig=stats(g)[2:]; Hh,Ih=stats(h)[2:]
 Pi=add(H,scale(Hg,-(1-p)),scale(Hh,-p)); Q=gamma*Ia
 K=tuple(x*y for x,y in zip(data_g,data_h)); IK=stats(K)[3]
 R=2*p*(1-p)*IK
 check(I==Q+(1-p)*Ig+p*Ih)
 check(edges(f,range(k+ng+nh,k+ng+nh+na))==Q)
 check(IK==edges(K,range(k+ng+nh)))
 B=[]; J=[]
 Ghat=tuple(F(x,len(data_g)) for x in walsh(data_g))
 Hhat=tuple(F(x,len(data_h)) for x in walsh(data_h))
 for x,y in zip(Ghat,Hhat):
  q=(1-p)*x*x+p*y*y
  z=p*(1-p)*(x-y)**2
  B.append(add(eta(z),eta(q-z),scale(eta(q),-1)))
  J.append(add(eta(q),scale(eta(x*x),-(1-p)),scale(eta(y*y),-p)))
 BB,JJ=add(*B),add(*J); w=V*gamma
 adjust=scale(lg(V),w) if V else {}
 check(Pi==add(JJ,BB,scale(Hp_a,gamma),adjust))
 # 3log2(e)<13/3, using ln2>9/13. Tested upper bound is strictly more conservative.
 cert(add(scale(Hp_a,gamma),{2:F(13,3)*Q+R},scale(Pi,-1)))
 cert(add({2:F(26,9)*Q},scale(JJ,-1)))
 cert(add(eta(w),eta(1-w),scale(BB,-1)))
 check(R<=2*p*(1-p)*Ig+2*(1-p)*p*Ih)
 for j in range(na):
  a0=tuple(a[x] for x in range(len(a)) if not (x>>j)&1)
  a1=tuple(a[x] for x in range(len(a)) if (x>>j)&1)
  p0=F(a0.count(-1),len(a0)); p1=F(a1.count(-1),len(a1))
  R0=2*p0*(1-p0)*IK; R1=2*p1*(1-p1)*IK
  release=(p0-p1)**2*IK/2
  check(R-(R0+R1)/2==release>=0)
  check(abs(p0-p1)<=edges(a,[j]))
 for i in range(k+ng+nh):
  ik=edges(K,[i]); ig=edges(data_g,[i]); ih=edges(data_h,[i])
  check(ik<=ig+ih)
 # True shared-only calibration and uniform PRIVATE conditional law.
 if ng==nh==1:
  partial_count+=1
  vg=1-sum(x*x for x in ga[:N]); vh=1-sum(x*x for x in hb[:N])
  rg=tuple(x*x for x in ga[:N])+tuple(vg/N for _ in range(N))
  rh=tuple(x*x for x in hb[:N])+tuple(vh/N for _ in range(N))
  ca=tuple(F(x,len(a)) for x in walsh(a))
  refs=[]; cg_cost={}; ch_cost={}
  for q,ref in zip(stats(g)[0],rg):
   if q: cg_cost=add(cg_cost,scale(lg(1/ref),q))
  for q,ref in zip(stats(h)[0],rh):
   if q: ch_cost=add(ch_cost,scale(lg(1/ref),q))
  for u in range(1<<na):
   for t in range(1<<(k+ng+nh)):
    shared=t&(N-1); x=(t>>k)&1; y=(t>>(k+1))&1
    if x==y==0:
     amp=(1-p)*ga[shared]+p*hb[shared] if u==0 else -ca[u]*(hb[shared]-ga[shared])/2
     ref=amp*amp
    elif x and y:ref=F(0)
    elif x:ref=((1-p)**2 if u==0 else ca[u]**2/4)*rg[shared+N]
    else:ref=(p*p if u==0 else ca[u]**2/4)*rh[shared+N]
    refs.append(ref)
  check(sum(refs)==1)
  ce={}
  for q,ref in zip(stats(f)[0],refs):
   if q:
    check(ref>0)
    ce=add(ce,scale(lg(1/ref),q))
  check(ce==add(scale(cg_cost,1-p),scale(ch_cost,p),Pi))
  check(add(ce,scale(H,-1))==add(scale(add(cg_cost,scale(Hg,-1)),1-p),scale(add(ch_cost,scale(Hh,-1)),p)))
 count+=1
 if time.monotonic()-START>(55 if MODE=='pilot' else 600):raise RuntimeError('frozen cutoff')

controllers=list(tables(1 if MODE=='pilot' else 2))
for na,code,a in controllers:
 for k in range(0,(1 if MODE=='pilot' else 2)+1):
  cores=[t for n,c,t in tables(k) if n==k]
  for g in cores:
   for h in cores:case(na,a,k,0,g,0,h)
 cores=[(-1,-1,-1,-1),(1,1,1,1),(1,-1,1,-1),(1,1,-1,-1)] if MODE=='pilot' else [t for n,c,t in tables(2) if n==2]
 for g in cores:
  for h in cores:case(na,a,1,1,g,1,h)

out={'helper':'A028-general-controller-reserve-v1','mode':MODE,'status':'PASS','cases':count,
 'partially_shared_reference_cases':partial_count,'assertions_passed':E.checks,'compute_seconds':time.monotonic()-START,
 'arithmetic':'integer/Fraction/canonical-prime-log/outward-atanh24','scope':'Finite exact validation corroborates all-dimensional analytic proof'}
(ROOT/'out'/f'{MODE}_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
