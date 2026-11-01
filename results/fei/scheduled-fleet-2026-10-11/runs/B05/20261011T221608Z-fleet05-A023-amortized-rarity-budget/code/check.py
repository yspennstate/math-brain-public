"""A023 v1: exact signed spectra and formal log-vector certificates."""
from fractions import Fraction as F
from pathlib import Path
import json, time, hashlib
ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(x):
    global checks
    assert x
    checks+=1
def walsh(v):
    a=list(v); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for t in range(j,j+step):
                u,w=a[t],a[t+step]; a[t],a[t+step]=u+w,u-w
        step*=2
    return [F(x,len(a)) for x in a]
def factors(n):
    d=2; out={}
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def logterm(out,q,c):
    if not q or not c:return
    for n,sgn in [(q.numerator,1),(q.denominator,-1)]:
        for prime,e in factors(n).items():
            out[prime]=out.get(prime,F(0))+c*sgn*e
            if not out[prime]: del out[prime]
def entropy(ps):
    out={}
    for q in ps: logterm(out,q,-q)
    return out
def add(*terms):
    out={}
    for c,v in terms:
        for prime,e in v.items():
            out[prime]=out.get(prime,F(0))+c*e
            if not out[prime]:del out[prime]
    return out
def infl(v):
    n=(len(v)-1).bit_length()
    return [F(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v)) for i in range(n)]
def activation(v,r):return [v[x] if z==0 else 1 for z in range(1<<r) for x in range(len(v))]
def packet(v):
    # last coordinate queried; children share all earlier physical labels
    N=len(v)//2; a,b=walsh(v[:N]),walsh(v[N:]); j={}; js={}; L={}; mu=F(0)
    for x,y in zip(a,b):
        q=(x*x+y*y)/2; e=(x-y)**2/4; m=(abs(x)-abs(y))**2/4
        mu+=m
        if q:
            logterm(j,q/m if m else F(1),m)
            logterm(js,q/e if e else F(1),e)
            logterm(L,q/e if e else F(1),e)
            logterm(L,q/(q-e) if q!=e else F(1),q-e)
    return j,js,L,mu
def run_case(v,r):
    a=walsh(v); m=a[0]; deficit=1-m; p=F(1,1<<r)
    full=activation(v,r); c=walsh(full); ii=infl(full); base=infl(v)
    ck(sum(c0*c0 for c0 in c)==1)
    for U in range(1<<r):
        for T in range(len(v)):
            expected=(1-p*deficit if U==0 else -p*deficit) if T==0 else p*a[T]
            ck(c[U*len(v)+T]==expected)
    ck(ii[:len(base)]==[p*t for t in base]); ck(ii[len(base):]==[p*deficit]*r)
    H=entropy([x*x for x in a]); target=add((p,H))
    logterm(target,m*m,p*m*m)
    logterm(target,deficit*deficit,-(p-p*p)*deficit*deficit)
    logterm(target,(1-p*deficit)**2,-(1-p*deficit)**2)
    target[2]=target.get(2,F(0))+2*r*p*deficit*(2-p*deficit)
    target={k:v for k,v in target.items() if v}
    ck(entropy([x*x for x in c])==target)
    signed_total={}; terminal=add((p,H)); inc={}; minority_total={}
    for s in range(1,r+1):
        u=F(1,1<<s); w=p/u; d=u*deficit
        parent=activation(v,s)
        j,js,L,mu=packet(parent)
        ck(mu<=d)
        # exact signed formula, even at negative core-mean endpoint
        formula={}; logterm(formula,(1-2*d+2*d*d)/(d*d) if d else F(1),d*d)
        formula[2]=formula.get(2,F(0))+d-d*d
        formula={k:v for k,v in formula.items() if v}
        ck(js==formula)
        if s>=2 or m>=0:ck(j==js)
        signed_total=add((1,signed_total),(w,js)); minority_total=add((1,minority_total),(w,j))
        Hp=entropy([x*x for x in walsh(parent)]); Ha=entropy([x*x for x in walsh(activation(v,s-1))])
        inc=add((1,inc),(w,Hp),(-w/2,Ha))
        if m==0:
            # independent reconstruction of A021's mismatch law
            ck(mu==u); ck(js==formula)
    ck(add((1,inc),(1,terminal))==entropy([x*x for x in c]))
    return minority_total,terminal
def main():
    start=time.perf_counter(); cases=0
    for n in range(1,4):
        for mask in range(1<<(1<<n)):
            v=[-1 if (mask>>x)&1 else 1 for x in range(1<<n)]
            for r in range(1,4):run_case(v,r); cases+=1
    # quadratic bent cores, selector point surgery, both complete query orders
    surgery=[]
    for k in [2,4,6]:
        b=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2)) for x in range(1<<k)]
        bp=b.copy(); bp[0]=-bp[0]; core=b+bp
        ck(sum(infl(core))==F(k,2)+(k+1)*F(1,1<<k))
        for r in [1,2,3]:
            jt,term=run_case(core,r); cases+=1
            # selector-first: root debt plus half of each child's control debt
            G=activation(b,r); HH=activation(bp,r); root=packet(G+HH)[0]
            jG,_=run_case(b,r); jH,_=run_case(bp,r)
            selector=add((1,root),(F(1,2),jG),(F(1,2),jH))
            terminal=add((F(1,1<<(r+1)),entropy([x*x for x in walsh(b)])),(F(1,1<<(r+1)),entropy([x*x for x in walsh(bp)])))
            ck(add((1,term),(-1,terminal))==add((F(1,1<<r),entropy([x*x for x in walsh(core)])),(-1,terminal)))
            surgery.append({'k':k,'r':r,'control_J_log_vector':{str(t):str(z) for t,z in jt.items()},'selector_J_log_vector':{str(t):str(z) for t,z in selector.items()}})
    out={'helper_version':'A023-v1','cases':cases,'assertions':checks,'arithmetic':'integer Walsh, Fraction, rational prime-log vectors; no numerical entropy signs','elapsed_seconds':time.perf_counter()-start,'surgery':surgery,'status':'PASS'}
    (ROOT/'out'/'validation.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='surgery'}))
if __name__=='__main__':main()
