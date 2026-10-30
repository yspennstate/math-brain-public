from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
import json,time,math,sys
R=Path(__file__).resolve().parents[1];O=R/'out';O.mkdir(exist_ok=True)
t0=time.perf_counter();checks=0
a0=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1]
def ck(b):
    global checks
    checks+=1;assert b,checks
    assert time.perf_counter()-t0<(60 if '--pilot' in sys.argv else 180),'frozen runtime exceeded'
def fw(a):
    a=list(a);j=1
    while j<len(a):
        for s in range(0,len(a),2*j):
            for k in range(s,s+j):a[k],a[k+j]=a[k]+a[k+j],a[k]-a[k+j]
        j*=2
    return a
def direct(a):return [sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(a)) for s in range(len(a))]
def coeff(a):return [Q(x,len(a)) for x in fw(a)]
def law(a):return [x*x for x in coeff(a)]
@lru_cache(None)
def fact(n):
    r=[];p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:r.append((p,e))
        p+=1
    if n>1:r.append((n,1))
    return tuple(r)
def add(*terms):
    ans={}
    for c,x in terms:
        for p,v in x.items():ans[p]=ans.get(p,Q(0))+c*v
    return {p:v for p,v in ans.items() if v}
@lru_cache(None)
def lr(x):
    ans={}
    for n,sgn in [(x.numerator,1),(x.denominator,-1)]:
        for p,e in fact(n):ans[p]=ans.get(p,Q(0))+sgn*e
    return {p:v for p,v in ans.items() if v}
def ce(p,q):
    ck(all(y>0 or x==0 for x,y in zip(p,q)))
    return add(*[(-x,lr(y)) for x,y in zip(p,q) if x])
@lru_cache(None)
def hc(p):return ce(p,p)
def H(p):return hc(tuple(p))
def D(p,q):return add((1,ce(p,q)),(-1,H(p)))
def lnat(v):
    x=(v-1)/(v+1);s=Q(0);power=x
    for j in range(34):s+=2*power/(2*j+1);power*=x*x
    return s,s+2*power/(69*(1-x*x))
LN2=lnat(Q(2))
@lru_cache(None)
def logbounds(p):
    k=p.bit_length()-1;lo,hi=lnat(Q(p,1<<k))
    return Q(k)+lo/LN2[1],Q(k)+hi/LN2[0]
@lru_cache(None)
def xb(items):
    lo=hi=Q(0)
    for p,c in items:
        u,v=logbounds(p);lo+=c*(u if c>=0 else v);hi+=c*(v if c>=0 else u)
    return lo,hi
def bounds(x):return xb(tuple(sorted(x.items())))
def nonpositive(x):
    if not x:return
    ck(bounds(x)[1]<0)
def enc(v):
    if isinstance(v,Q):return str(v)
    if isinstance(v,dict):return {str(k):enc(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [enc(x) for x in v]
    return v
def save(n,v):(O/n).write_text(json.dumps(enc(v),indent=2)+'\n',encoding='utf-8')
def restr(st):
    free=[i for i in range(4) if st[i]<0]
    inds=[sum((st[i] if st[i]>=0 else (x>>free.index(i)&1))<<i for i in range(4)) for x in range(1<<len(free))]
    a=[a0[i] for i in inds];return a,[1-x*x for x in a]
def wrap(a,b,h,z):return [x+z*y*v for v in h for x,y in zip(a,b)]
def erasure(A,B,ph):
    # Only empty seed frequency has two occupied z labels.
    r=ph[0];return add(*[(1,add((1,H([x*x,y*y*r])),(-1,H([x*x+y*y*r])))) for x,y in zip(A,B)])

states=list(product([-1,0,1],repeat=4));cases=0;resets=0;biased=0
minrelease=None;fixed=[]
for n in range(4):
  for h in product([-1,1],repeat=1<<n):
    ph=law(h);m=Q(sum(h),len(h));r=m*m;nh=len(h)
    for st in states if n<=2 else [(-1,)*4]:
      if '--pilot' in sys.argv and cases==32:
        result={'PASS':True,'pilot':True,'pairs':cases,'checks':checks,'seconds':time.perf_counter()-t0}
        save('pilot.json',result);print(json.dumps(result));sys.exit(0)
      cases+=1;a,b=restr(st);A=coeff(a);B=coeff(b);beta=Q(sum(b),len(b));nu=len(a)
      if cases%100==0:save('CHECKPOINT.json',{'completed_pairs':cases-1,'checks':checks,'reset_cases':resets,'seconds':time.perf_counter()-t0,'next_seed':h,'next_state':st,'status':'RUNNING_NOT_A_CERTIFICATE'})
      par=[x*x*(1 if j==0 else 0) for j in range(nh) for x in A]+[y*y*p for p in ph for y in B]
      kids=[wrap(a,b,h,sig) for sig in [1,-1]];pk=[law(f) for f in kids]
      ck(all(v in [-1,1] for f in kids for v in f));ck(all(sum(p)==1 for p in pk))
      qbar=[(p+q)/2 for p,q in zip(*pk)]
      JS=add((1,H(qbar)),(-Q(1,2),H(pk[0])),(-Q(1,2),H(pk[1])))
      Bz=erasure(A,B,ph)
      ck(add((1,H(par)),(-Q(1,2),H(pk[0])),(-Q(1,2),H(pk[1])))==add((1,Bz),(1,JS)))
      # All supplied references retain reference-only labels.
      refs=[ph]
      tails=[] if nh==1 else [[Q(1,nh-1)]*(nh-1),[Q(i,nh*(nh-1)//2) for i in range(1,nh)]]
      for r0 in [Q(1,4),Q(1,2),Q(3,4)]:
        for tail in tails:refs.append([r0]+[(1-r0)*x for x in tail])
      if nh>1 and r==0:refs.append([Q(0)]+tails[0])
      refs=list(dict.fromkeys(tuple(x) for x in refs))
      targets=[] if nh==1 else [[Q(1,nh-1)]*(nh-1),[Q(0)]*(nh-2)+[Q(1)]]
      if nh==1:targets=[[]]
      for ref in refs:
        ck(sum(ref)==1);r0=ref[0]
        if r<1:ck(r0<1)
        bern=D([r,1-r],[r0,1-r0])
        tagged=[x*x*(1 if j==0 else 0) for j in range(nh) for x in A]+[y*y*p for p in ref for y in B]
        ck(sum(tagged)==1)
        old=ce(par,tagged)
        ck(old==add((1,H(par)),(beta,D(ph,ref))))
        for target in targets:
          for eps in [Q(0),Q(1,8)]:
            resets+=1
            tail=[] if r==1 else [x/(1-r0) for x in ref[1:]]
            mixed=[] if r==1 else [(1-eps)*x+eps*y for x,y in zip(tail,target)]
            qs=[]
            for sig in [1,-1]:
              qr=[(x+sig*m*y)**2 for x,y in zip(A,B)]
              for v in mixed:qr += [y*y*(1-r)*v for y in B]
              if r==1:qr += [Q(0)]*(nu*(nh-1))
              ck(sum(qr)==1);qs.append(qr)
            inc=add((1,Bz),(Q(1,2),ce(pk[0],qs[0])),(Q(1,2),ce(pk[1],qs[1])),(-1,old))
            taildiff={} if r==1 else add((1,D([x/(1-r) for x in ph[1:]],mixed)),(-1,D([x/(1-r) for x in ph[1:]],tail)))
            expected=add((-1,JS),(-beta,bern),(beta*(1-r),taildiff))
            ck(inc==expected)
            if eps==0:nonpositive(inc)
            else:
              ck(all(v>=(1-eps)*u for u,v in zip(tail,mixed)))
              nonpositive(add((1,taildiff),(-1,lr(Q(1,1-eps)))))
            if st==(-1,)*4 and r==Q(1,4) and r0==Q(1,2) and eps==Q(1,8):
              biased+=1
              nonpositive(add((1,inc),(1,{2:Q(1,64)})))
            if n==2 and h==(-1,1,1,1) and st==(-1,)*4 and r0==Q(1,2) and eps==Q(1,8) and target==targets[-1]:
              fixed.append({'seed':h,'reference':ref,'target_tail':target,'actual_children':kids,'child_spectra':pk,'fresh_references':qs,'erasure':Bz,'JS':JS,'increment':inc})
    if n==2 and h==(-1,1,1,1):
      # The reference-induced phase guess sqrt(R0)=1/3 cancels an occupied atom.
      a,b=restr((-1,)*4);A=coeff(a);B=coeff(b);ref=[Q(1,9)]+[Q(8,27)]*3
      child=wrap(a,b,h,-1);pc=law(child)
      naive=[(x-Q(1,3)*y)**2 for x,y in zip(A,B)]
      for v in ref[1:]:naive += [y*y*v for y in B]
      ck(sum(naive)==1);ck(pc[0]==Q(1,256));ck(naive[0]==0)
      ck(fw(child)==direct(child))
      ck(all(x>0 for x in ref))
      save('support_obstruction.json',{'seed':h,'source_reference':ref,'child_truth_table':child,'child_Walsh':fw(child),'true_empty_mass':pc[0],'naive_reference_empty_mass':naive[0],'naive_normalized_reference':naive,'parent_source_CE_finite':True,'child_naive_CE':'INFINITE'})
ck(cases==2038);ck(21**3>2**13);ck(21**18>2**79)
save('fixed_resets.json',fixed)
result={'PASS':True,'checks':checks,'seconds':time.perf_counter()-t0,'controller_seed_pairs':cases,'reset_cases':resets,'strict_root_biased_resets':biased,'support_obstruction':True,'formal_status':'NOT_CLAIMED','note':'All-dimensional reset theorem uses exact algebra and the pointwise likelihood floor; finite replay is validation, not extrapolation.'}
save('validation.json',result);print(json.dumps(result,indent=2))
