"""Bounded numerical checks of exact proof identities, not limit simulations."""
import json, math, random, platform
rng=random.Random(20261024)
secant_error=0.0
crossing_cases=0
for _ in range(10000):
    u=math.exp(rng.uniform(-4,4)); w=rng.uniform(-20,20); d=rng.uniform(-.9,.9)
    ell=min(1.0,-u/(d*w)) if d*w<0 else 1.0
    rhs=d*(ell*(u*u+w*w)+d*u*w*ell*ell)
    lhs=(w+d*u)*max(u+d*w,0)-w*u
    err=abs(lhs-rhs)/max(1,abs(lhs),abs(rhs))
    secant_error=max(secant_error,err)
    assert err<2e-12
    crossing_cases+=int(u+d*w<=0)

def exp_apply(a,c,b,t,r):
    gap=math.hypot(a-b,2*c)
    lo=(a+b-gap)/2; hi=(a+b+gap)/2
    low=((hi-a)*r[0]-c*r[1],-c*r[0]+(hi-b)*r[1])
    low=(low[0]/gap,low[1]/gap)
    return tuple(math.exp(-lo*t)*low[j]+math.exp(-hi*t)*(r[j]-low[j]) for j in range(2))

def integral(a,c,b,t,r):
    v=exp_apply(a,c,b,t,r); w=(r[0]-v[0],r[1]-v[1]); det=a*b-c*c
    return ((b*w[0]-c*w[1])/det,(a*w[1]-c*w[0])/det)

counts={'coordinate_1':0,'coordinate_2':0,'none':0}
root_error=0.0
for _ in range(1000):
    s0,s1,s2,p1,p2=[math.exp(rng.uniform(-1,1)) for _ in range(5)]
    c=s0/2; a=(s0+s1)/2+p1; b=(s0+s2)/2+p2
    r=(math.exp(rng.uniform(-2,2)),math.exp(rng.uniform(-2,2)))
    ratio=r[1]/r[0]
    j=0 if ratio>b/c else 1 if ratio<c/a else None
    if j is None:
        counts['none']+=1
        for t in (.01,.1,1,10,100):
            assert min(integral(a,c,b,t,r))>-1e-12
        continue
    counts['coordinate_'+str(j+1)]+=1
    left=1e-10; right=1.0
    while integral(a,c,b,right,r)[j]>=0:
        right*=2
        assert right<1e6
    for _ in range(90):
        mid=(left+right)/2
        if integral(a,c,b,mid,r)[j]>0: left=mid
        else: right=mid
    tau=(left+right)/2; rs=exp_apply(a,c,b,tau,r); js=integral(a,c,b,tau,r)
    root_error=max(root_error,abs(js[j]))
    assert rs[j]<0 and rs[1-j]>0
    aa=a-p1 if j==0 else a; bb=b-p2 if j==1 else b
    for t in (.01,.1,1,10):
        after=exp_apply(aa,c,bb,t,rs)
        ja=integral(aa,c,bb,t,rs)
        assert after[j]<0 and after[1-j]>0
        assert js[j]+ja[j]<1e-12 and js[1-j]+ja[1-j]>0
print(json.dumps({'scope':'Numerical checks of algebra and deterministic hybrid geometry only; not proof or finite-width convergence experiment','python':platform.python_version(),'seed':20261024,'secant_cases':10000,'negative_overshoot_cases':crossing_cases,'max_relative_secant_error':secant_error,'hybrid_cases':1000,'classifications':counts,'max_cumulative_root_error':root_error,'all_assertions_passed':True},indent=2))
