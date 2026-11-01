from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys,hashlib
ROOT=Path(__file__).resolve().parents[1];COUNT=0
def ck(x):
    global COUNT
    COUNT+=1
    assert x,COUNT
def add(*es):
    out={}
    for e in es:
        for p,c in e:out[p]=out.get(p,F(0))+c
    return tuple(sorted((p,c) for p,c in out.items() if c))
def scale(e,c):return tuple((p,a*c) for p,a in e if a*c)
@lru_cache(None)
def factors(n):
    a=[];p=2
    while p*p<=n:
        c=0
        while n%p==0:n//=p;c+=1
        if c:a.append((p,F(c)))
        p+=1
    if n>1:a.append((n,F(1)))
    return tuple(a)
def logexpr(x):return add(factors(x.numerator),scale(factors(x.denominator),-1))
@lru_cache(None)
def phi(x):return scale(logexpr(x),-x) if x else ()
@lru_cache(None)
def Phi(a,b):return add(phi(a),phi(b),scale(phi(a+b),-1))
@lru_cache(None)
def lp(p):
    y=F(p);k=0
    while y>=2:y/=2;k+=1
    z=(y-1)/(y+1);N=32
    def ln(q):
        t=(q-1)/(q+1)
        a=2*sum((t**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
        return a,a+2*t**(2*N+1)/(F(2*N+1)*(1-t*t))
    a,b=ln(y);c,d=ln(F(2));den=1<<100
    return F(((k+a/d)*den).__floor__(),den),F(((k+b/c)*den).__ceil__(),den)
def enclosure(e):
    lo=hi=F(0)
    for p,c in e:
        a,b=lp(p)
        lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi
def nonneg(e):
    if not e:return True
    return enclosure(e)[0]>=0
def constant(x):return ((2,F(x)),) if x else ()
def fwht(a):
    a=list(a);h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
        h*=2
    return a
@lru_cache(None)
def spectrum(vals):return tuple(F(a,len(vals)) for a in fwht(vals))
def H(vals):return add(*(phi(a*a) for a in spectrum(vals)))
def B(vals,i):
    a=spectrum(vals);bit=1<<i
    return add(*(Phi(a[t]*a[t],a[t|bit]*a[t|bit]) for t in range(len(a)) if not t&bit))
def inf(vals,i):
    return F(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals))),len(vals))
def influence(vals):return sum((inf(vals,i) for i in range(len(vals).bit_length()-1)),F(0))
def restrict(vals,i,b):
    low=(1<<i)-1
    return tuple(vals[(x&low)|((x>>i)<<(i+1))|(b<<i)] for x in range(len(vals)//2))
def wrap(g,h):return tuple(g[x>>1] if x&1==0 else h[x>>1] for x in range(2*len(g)))
def common(g,h,kinds):
    ids=[0,1<<kinds.index('s')] if 's' in kinds else [0]
    ag,ah=spectrum(g),spectrum(h)
    return ids,ag,ah
def potential(g,h,kinds):
    ids,ag,ah=common(g,h,kinds)
    base=2-sum((ag[c]**2+ah[c]**2 for c in ids),F(0))
    return add(constant(base),*(add(phi((ag[c]+ah[c])**2/4),phi((ag[c]-ah[c])**2/4),scale(phi(ag[c]**2),F(-1,2)),scale(phi(ah[c]**2),F(-1,2))) for c in ids))
@lru_cache(None)
def node(g,h,kinds):
    f=wrap(g,h);ids,ag,ah=common(g,h,kinds)
    ck(H(f)==add(scale(H(g),F(1,2)),scale(H(h),F(1,2)),potential(g,h,kinds)))
    rows=[]
    for i,kind in enumerate(kinds):
        jf=inf(f,i+1);jg=inf(g,i);jh=inf(h,i)
        ck(jf==(jg+jh)/2)
        inherited=scale(add(B(g,i),B(h,i)),F(1,2))
        direct=add(B(f,i+1),scale(inherited,-1))
        if kind=='s':
            mu,nu,a,b=ag[0],ah[0],ag[1<<i],ah[1<<i]
            formula=add(scale(add(Phi((mu+nu)**2,(a+b)**2),Phi((mu-nu)**2,(a-b)**2)),F(1,4)),scale(add(Phi(mu*mu,a*a),Phi(nu*nu,b*b)),F(-1,2)))
        else:
            left,right=(ag,ah) if kind=='X' else (ah,ag)
            formula=();upper=();lower=()
            for c in ids:
                u,d,v=left[c],left[c|(1<<i)],right[c]
                ds=add(scale(add(Phi((u+v)**2,d*d),Phi((u-v)**2,d*d)),F(1,4)),scale(Phi(u*u,d*d),F(-1,2)))
                formula=add(formula,ds)
                upper=add(upper,scale(Phi(v*v,d*d),F(1,2)))
                lower=add(lower,scale(Phi(u*u,d*d),F(-1,2)))
                ck(nonneg(add(scale(Phi(v*v,d*d),F(1,2)),scale(ds,-1))))
            ck(nonneg(add(upper,scale(formula,-1))))
            ck(nonneg(add(formula,scale(lower,-1))))
        ck(direct==formula)
        ck(nonneg(add(constant(2*jf),scale(direct,-1))))
        ck(nonneg(add(constant(2*jf),direct)))
        rows.append((direct,jf,inherited))
    return tuple(rows)
def tree(g,h,kinds,policy,depth=0):
    rows=node(g,h,kinds)
    if not kinds or (policy=='partial' and depth>=1):
        return (),(),F(0),influence(wrap(g,h)),H(wrap(g,h)),scale(add(H(g),H(h)),F(1,2)),potential(g,h,kinds)
    if policy=='first':i=0
    elif policy=='last':i=len(kinds)-1
    else:i=max(range(len(kinds)),key=lambda j:(rows[j][1],-j))
    children=[tree(restrict(g,i,b),restrict(h,i,b),kinds[:i]+kinds[i+1:],policy,depth+1) for b in [0,1]]
    d,j,inh=rows[i]
    correction=add(d,*(scale(c[0],F(1,2)) for c in children))
    inherited=add(inh,*(scale(c[1],F(1,2)) for c in children))
    spent=j+sum((c[2]/2 for c in children),F(0))
    leafI=sum((c[3]/2 for c in children),F(0))
    leafH=add(*(scale(c[4],F(1,2)) for c in children))
    leafcore=add(*(scale(c[5],F(1,2)) for c in children))
    leafR=add(*(scale(c[6],F(1,2)) for c in children))
    ck(spent+leafI==influence(wrap(g,h)))
    ck(nonneg(add(constant(2*spent),scale(correction,-1))))
    ck(nonneg(add(constant(2*spent),correction)))
    ck(leafH==add(leafcore,leafR))
    potential_drop=add(potential(g,h,kinds),scale(leafR,-1))
    ck(nonneg(add(constant(5*spent),scale(potential_drop,-1))))
    ck(nonneg(add(constant(5*spent),potential_drop)))
    return correction,inherited,spent,leafI,leafH,leafcore,leafR
def embed(mask,x,y,branch):
    out=[]
    for bits in range(1<<(1+x+y)):
        key=(bits&1)|(((bits>>1)&((1<<x)-1))<<1) if branch=='G' else (bits&1)|((bits>>(1+x))<<1)
        out.append(1 if mask>>key&1 else -1)
    return tuple(out)
def serialize(e):return {str(p):str(c) for p,c in e}
def main():
    start=time.perf_counter();mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
    domains=[(0,0)] if mode=='pilot' else [(0,0),(0,1),(1,0),(1,1),(2,0),(0,2)]
    roots=trees=0;negative=None;sharp=None
    pairs=[]
    for x,y in domains:
        for gm in range(1<<(1<<(1+x))):
            for hm in range(1<<(1<<(1+y))):pairs.append((x,y,gm,hm))
    if mode=='full':
        masks=[0,255,170,128,150,216]
        pairs.extend((2,2,g,h) for g in masks for h in masks)
    for x,y,gm,hm in pairs:
        if time.perf_counter()-start>170:raise RuntimeError('frozen runtime limit')
        g=embed(gm,x,y,'G');h=embed(hm,x,y,'H');kinds=('s',)+('X',)*x+('Y',)*y
        rows=node(g,h,kinds)
        for i,(d,j,inh) in enumerate(rows):
            if d and enclosure(d)[1]<0 and negative is None:
                negative={'private_widths':[x,y],'G_mask':gm,'H_mask':hm,'queried_kind':kinds[i],'D':serialize(d),'D_interval':[str(z) for z in enclosure(d)],'Inf_F':str(j)}
            if j and d==constant(2*j) and sharp is None:
                sharp={'private_widths':[x,y],'G_mask':gm,'H_mask':hm,'query':kinds[i],'D':serialize(d),'Inf_F':str(j)}
        for policy in ['first','last','partial']:
            tree(g,h,kinds,policy);trees+=1
        roots+=1
    ck(sharp is not None)
    if mode=='full':ck(negative is not None)
    out={'helper_version':'A077-shared-bit-v1','mode':mode,'roots':roots,'trees':trees,'assertions':COUNT,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'integer FWHT/Fraction; exact prime-log equalities and rigorous rational intervals','sharp_fixture':sharp,'negative_fixture':negative,'cache_node_count':node.cache_info().currsize}
    p=ROOT/'out'/f'{mode}.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out));print('saved',p,'sha256',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
