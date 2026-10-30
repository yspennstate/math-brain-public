from exact import *
import exact as E

def mean(t): return F(sum(t),len(t))
def mux(r,g,h):
    return tuple((g[x] if c==0 else h[y]) for c in range(1<<r) for y in range(len(h)) for x in range(len(g)))

counts={'point_selector':0,'shared_priority':0}
dim=1 if MODE=='pilot' else 2
rs=range(1,3 if MODE=='pilot' else 4)
for ng,cg,g in tables(dim):
  for nh,ch,h in tables(dim):
    mu,nu=mean(g),mean(h)
    Vg,Vh=1-mu*mu,1-nu*nu
    d=(1-mu*nu)/2
    for r in rs:
      p=F(1,1<<r); t=mu-nu; m=p*mu+(1-p)*nu
      f=mux(r,g,h)
      H,I=stats(f)[2:]
      Hg,Ig=stats(g)[2:]; Hh,Ih=stats(h)[2:]
      Pi=add(H,scale(Hg,-p),scale(Hh,-(1-p)))
      expected=add({2:2*r*p*(Vg+(1-p)*Vh+(1-p)*t*t)},
          scale(eta((1-p)**2),Vh),eta(m*m),scale(eta(mu*mu),-p),
          scale(eta(nu*nu),-(1-p)),scale(lg(1/(t*t)),p*(1-p)*t*t) if t else {})
      check(Pi==expected)
      Q=2*r*p*d
      check(I==Q+p*Ig+(1-p)*Ih)
      check(edges(f,range(ng+nh,ng+nh+r))==Q)
      actual,paid=tree(f,r)
      check(actual==Pi and paid==Q)
      margin=add({2:F(71,8)*Q},scale(Pi,-1))
      check(not margin or enclosure(margin)[0]>=0)
      check(abs(t)<=2*d and Vg+Vh+t*t==4*d)
      counts['point_selector']+=1
      if time.monotonic()-START>(60 if MODE=='pilot' else 600): raise RuntimeError('frozen cap')

# First physical bit z, then point A, then point B only if A fails.
rr=range(1,2 if MODE=='pilot' else 3)
for ng,cg,g in tables(1):
  for nh,ch,h in tables(1):
    for r in rr:
      for s in rr:
        p,q=F(1,1<<r),F(1,1<<s)
        hB=tuple(h[y] if b==0 else 1 for b in range(1<<s) for y in range(len(h)))
        inner=mux(r,g,hB)
        f=inner+(1,)*len(inner)
        mu,nu=mean(g),mean(h); a,b=1-mu,1-nu
        Qz=(1-mean(inner))/2
        QA=2*r*p*(1-mu*mean(hB))/2
        QB=s*q*b
        Q=Qz+QA/2+(1-p)*QB/2
        wg,wh=p/2,(1-p)*q/2
        H,I=stats(f)[2:]; Hg,Ig=stats(g)[2:]; Hh,Ih=stats(h)[2:]
        Pi=add(H,scale(Hg,-wg),scale(Hh,-wh))
        nominal=(r+1)*p*a/2+(s+1)*q*b/2
        correction=p*q*b*(r*mu-s-1)/2
        check(Q==nominal+correction)
        check(I==Q+wg*Ig+wh*Ih)
        check(edges(f,range(ng+nh,ng+nh+s+r+1))==Q)
        Hinner=stats(inner)[2]; HB=stats(hB)[2]
        decomposition=add(H,scale(Hinner,F(-1,2)),
          scale(add(Hinner,scale(Hg,-p),scale(HB,-(1-p))),F(1,2)),
          scale(add(HB,scale(Hh,-q)),(1-p)/2))
        check(Pi==decomposition)
        margin=add({2:F(71,8)*Q},scale(Pi,-1))
        check(not margin or enclosure(margin)[0]>=0)
        counts['shared_priority']+=1
        if time.monotonic()-START>(60 if MODE=='pilot' else 600): raise RuntimeError('frozen cap')

out={'helper':'A028-point-selector-v1','mode':MODE,'cases':counts,'total_cases':sum(counts.values()),
 'assertions_passed':E.checks,'compute_seconds':time.monotonic()-START,'max_dimension':7,
 'arithmetic':'integer/Fraction/prime-log/outward-rational-atanh24','status':'PASS',
 'scope':'Finite checks of analytic identities and bound; all-dimensional proof in REPORT.md'}
(ROOT/'out'/f'{MODE}_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
