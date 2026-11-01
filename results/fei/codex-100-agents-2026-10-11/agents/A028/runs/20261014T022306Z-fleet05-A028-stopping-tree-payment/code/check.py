from exact import *
import exact as E

def branches(k,max_private):
 for n in range(max_private+1):
  for code in range(1<<(1<<(k+n))):
   yield n,tuple(-1 if code>>x&1 else 1 for x in range(1<<(k+n)))
def case(k,ng,g,nh,h,r,fixture=False):
 p=F(1,1<<r); N=1<<k
 ga=tuple(F(x,len(g)) for x in walsh(g))
 hb=tuple(F(x,len(h)) for x in walsh(h))
 a,b=ga[:N],hb[:N]
 Vg=1-sum(x*x for x in a); Vh=1-sum(x*x for x in b)
 ts=tuple(x-y for x,y in zip(a,b)); D=sum(x*x for x in ts)
 f=tuple(g[z+(x<<k)] if c==0 else h[z+(y<<k)]
   for c in range(1<<r) for y in range(1<<nh) for x in range(1<<ng) for z in range(N))
 data=tuple(g[z+(x<<k)]!=h[z+(y<<k)] for y in range(1<<nh) for x in range(1<<ng) for z in range(N))
 d=F(sum(data),len(data)); Q=2*r*p*d
 Hg,Ig=stats(g)[2:]; Hh,Ih=stats(h)[2:]; H,I=stats(f)[2:]
 Pi=add(H,scale(Hg,-p),scale(Hh,-(1-p)))
 expr=add({2:2*r*p*(Vg+(1-p)*Vh+(1-p)*D)},scale(eta((1-p)**2),Vh),
  *(add(eta((p*x+(1-p)*y)**2),scale(eta(x*x),-p),scale(eta(y*y),-(1-p)),
      scale(lg(1/((x-y)**2)),p*(1-p)*(x-y)**2) if x!=y else {}) for x,y in zip(a,b)))
 check(Pi==expr)
 check(Vg+Vh+D==4*d)
 check(all(abs(t)<=2*d for t in ts))
 check(D/4<=min(d,N*d*d))
 check(I==Q+p*Ig+(1-p)*Ih)
 check(edges(f,range(k+ng+nh,k+ng+nh+r))==Q)
 # Rational upper relaxation of 4+(4k+6b+4b/e)/r, b<13/9,1/e<3/8.
 K=4+(4*k+F(65,6))/r
 gap=add({2:K*Q},scale(Pi,-1))
 check(not gap or enclosure(gap)[0]>=0)
 if r>=k:
  gap=add({2:14*Q},scale(Pi,-1))
  check(not gap or enclosure(gap)[0]>=0)
 if fixture:
  lower=(1-p)*(4+F(2*(k-4),r))
  gap=add(Pi,{2:-lower*Q})
  check(not gap or enclosure(gap)[0]>=0)
  check(d==F(1,1<<k))
  fixtures.append({'k':k,'r':r,'d':str(d),'Q':str(Q),'Pi_prime_log':{str(q):str(v) for q,v in Pi.items()},'ratio_lower_proved':str(lower)})
 return Pi,Q

fixtures=[]; cases=0
domains=[(1,0,[1,2]),(2,0,[2])] if MODE=='pilot' else [(1,1,range(1,5)),(2,0,range(1,5))]
for k,priv,rs in domains:
 for ng,g in branches(k,priv):
  for nh,h in branches(k,priv):
   for r in rs:
    case(k,ng,g,nh,h,r); cases+=1
    if time.monotonic()-START>(55 if MODE=='pilot' else 300):raise RuntimeError('frozen cutoff')
for k in ([4] if MODE=='pilot' else [4,6]):
 g=tuple(-1 if sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2))%2 else 1 for x in range(1<<k))
 h=(-1,)+g[1:]
 for r in [1,2,k]:
  case(k,0,g,0,h,r,True);cases+=1
  if time.monotonic()-START>(55 if MODE=='pilot' else 300):raise RuntimeError('frozen cutoff')
out={'helper':'A028-shared-point-selector-v1','mode':MODE,'status':'PASS','cases':cases,
 'assertions_passed':E.checks,'compute_seconds':time.monotonic()-START,'fixtures':fixtures,
 'arithmetic':'integer/Fraction/prime-log/outward-rational-atanh24','all_dimension_scope':'Analytic proof; finite checks corroborate only'}
(ROOT/'out'/f'{MODE}_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='fixtures'},indent=2))
