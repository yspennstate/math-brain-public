from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, time, itertools, sys

RUN=Path(__file__).resolve().parents[1]
COUNT=0
def ck(x):
    global COUNT
    COUNT+=1
    if not x: raise AssertionError(COUNT)

def walsh(f):
    a=list(f);s=1
    while s<len(a):
        for j in range(0,len(a),2*s):
            for t in range(j,j+s): a[t],a[t+s]=a[t]+a[t+s],a[t]-a[t+s]
        s*=2
    return [F(x,len(a)) for x in a]

def influence(f):
    return F(sum(f[x]!=f[x^(1<<j)] for x in range(len(f)) for j in range(len(f).bit_length()-1)),len(f))

def child(f,j,b):
    return [f[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(f)//2)]

QFIX=1<<100
@lru_cache(None)
def ln_range(x):
    z=(x-1)/(x+1);total=0
    for i in range(24):
        a=2*z**(2*i+1)/F(2*i+1);total+=(a.numerator*QFIX)//a.denominator
    tail=2*z**49/(49*(1-z*z))
    return F(total,QFIX),F(total+24,QFIX)+tail

@lru_cache(None)
def log2(x):
    assert x>0
    e=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/F(2)**e
    if y<1:e-=1;y*=2
    assert 1<=y<2
    lo,hi=ln_range(y);l2,h2=ln_range(F(2))
    lower=e+lo/h2;upper=e+hi/l2;grid=1<<80
    return F((lower.numerator*grid)//lower.denominator,grid),F(-((-upper.numerator*grid)//upper.denominator),grid)

def ce(p,q):
    lo=F(0);hi=F(0)
    for a,b in zip(p,q):
        if a:
            ck(b>0);l,h=log2(1/b);lo+=a*l;hi+=a*h
    return lo,hi

def cost_expression(p,q,scale=F(1)):
    out={}
    for a,b in zip(p,q):
        if a:out[b]=out.get(b,F(0))+scale*a
    return {b:a for b,a in out.items() if a}

def spectrum(f):
    a=walsh(f);p=[x*x for x in a]
    ck(sum(p)==1)
    ck(sum(t.bit_count()*x for t,x in enumerate(p))==influence(f))
    return a,p

def root(w,m):
    n=w+2+m
    g=[(1-2*int((x&((1<<w)-1))==0))*(1-2*int((x>>w)==0)) for x in range(1<<(w+2))]
    f=[g[x&((1<<(w+2))-1)]*(-1 if (x&((1<<n)-1))==0 and x>>n else 1) for x in range(1<<(n+1))]
    a=walsh(g);d=F(1,1<<n);W=2*d-(1<<(w+2))*d*d
    q=[(1-W)*a[x]*a[x] if x<len(a) else d*d for x in range(len(f))]
    ck(sum(q)==1)
    af,p=spectrum(f)
    ck(all(af[t]==(a[t] if t<len(a) else 0)-d for t in range(1<<n)))
    ck(all(af[t]==d for t in range(1<<n,len(f))))
    # Independent direct character reconstruction of original tensor coefficients.
    for t in range(len(g)):
        direct=F(sum(y*(-1 if (t&x).bit_count()%2 else 1) for x,y in enumerate(g)),len(g))
        ck(direct==a[t])
    return g,f,q,p

def run_case(w,m):
    g,f,q,p=root(w,m);lo,hi=ce(p,q)
    ck(hi<F(1005,256))
    # Enumerate each labeled restriction; test the physical edited-path identity.
    n=w+2+m;d=F(1,1<<n);qwide=F(1,1<<(w-1));states=0
    for pattern in itertools.product([-1,0,1],repeat=w):
        fixed={i:b for i,b in enumerate(pattern) if b!=-1};t=len(fixed)
        fl=f;gl=g
        for i in sorted(fixed,reverse=True):fl=child(fl,i,fixed[i]);gl=child(gl,i,fixed[i])
        _,pl=spectrum(fl);states+=1
        # Unedited branches agree exactly; the unique zero path has the literal correction.
        if any(fixed.values()): ck(influence(fl)==influence(gl))
        else:
            ck(influence(fl)==influence(gl)+F(1,1<<(n-t))*(m-w-1+t))
            # Width-two factor prevents constant endpoints, even at t=w.
            ck(influence(fl)>0)
        for i in range(w-t):
            f0=child(fl,i,0);f1=child(fl,i,1)
            query=F(sum(fl[x]!=fl[x^(1<<i)] for x in range(len(fl))),len(fl))
            ck(influence(fl)==query+(influence(f0)+influence(f1))/2)
    results=[]
    for policy in ['forward','reverse','adaptive','branch_stop']:
        releases=[];leaf_cost=F(0);leaf_I=F(0);leaves=0;zero_fibers=0
        def visit(ff,qq,labels,reach,depth):
            nonlocal leaf_cost,leaf_I,leaves,zero_fibers
            available=[i for i,label in enumerate(labels) if label<w]
            if not available or (policy=='branch_stop' and depth>=1 and ff[0]<0):
                _,pp=spectrum(ff);leaf_cost+=reach*ce(pp,qq)[1];leaf_I+=reach*influence(ff);leaves+=1;return
            j=available[-1] if policy=='reverse' or (policy=='adaptive' and ff[0]<0) else available[0]
            aa,pp=spectrum(ff);parentlo=ce(pp,qq)[0]
            kids=[child(ff,j,b) for b in [0,1]];ps=[spectrum(x)[1] for x in kids]
            raws=[[],[]]
            for x in range(len(ff)//2):
                t=(x&((1<<j)-1))|((x>>j)<<(j+1));mass=pp[t]+pp[t+(1<<j)];rr=qq[t]+qq[t+(1<<j)]
                ck((ps[0][x]+ps[1][x])/2==mass)
                if mass:
                    for b in [0,1]:raws[b].append(rr*ps[b][x]/mass)
                else:
                    zero_fibers+=1
                    for b in [0,1]:raws[b].append(rr)
            zs=[sum(x) for x in raws];ck(sum(zs)==2);ck(all(z>0 for z in zs))
            qs=[[x/zs[b] for x in raws[b]] for b in [0,1]]
            costs=[ce(ps[b],qs[b]) for b in [0,1]]
            # Exact zero release cannot be certified by subtracting nonzero-width
            # intervals. Cancel identical rational-log terms before any sign test.
            expr=cost_expression(pp,qq)
            for b in [0,1]:
                for x,a in cost_expression(ps[b],qs[b],F(1,2)).items():expr[x]=expr.get(x,F(0))-a
            expr={x:a for x,a in expr.items() if a}
            if expr:ck(parentlo-(costs[0][1]+costs[1][1])/2>=0)
            else:ck(True)
            releases.append([str(z) for z in zs])
            for b in [0,1]:visit(kids[b],qs[b],labels[:j]+labels[j+1:],reach/2,depth+1)
        visit(f,q,list(range(n+1)),F(1),0)
        ck(leaf_I>=F(63,64));ck(4*leaf_I-leaf_cost>F(3,256));ck(leaf_cost<=hi)
        results.append({'policy':policy,'leaves':leaves,'mean_I':str(leaf_I),'CE_upper':str(leaf_cost),'zero_fibers_retained':zero_fibers,'normalizers':releases})
    return {'w':w,'m':m,'states':states,'root_CE_interval':[str(lo),str(hi)],'histories':results}

def main():
    start=time.perf_counter();pilot='--pilot' in sys.argv
    domain=[(4,0)] if pilot else [(w,m) for w in [4,5] for m in [0,1,2]]
    data=[run_case(w,m) for w,m in domain]
    # The all-parameter proof uses these recurrences, not a finite-width extrapolation.
    for m in range(101):ck(16*m+37<=37*(1<<m))
    for w in range(4,101):
        ck(F(4*w+6,8*w+4)<=1)
        ck(F(4*w+2,1<<(w-1))<=F(9,4))
    out={'status':'PASS','arithmetic':'exact integer/Fraction and outward rational log intervals','assertions':COUNT,'seconds':time.perf_counter()-start,'cases':data,'rung':'finite certificate; universal parameter proof is in REVIEW.md; no Lean certification'}
    (RUN/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
if __name__=='__main__':main()
