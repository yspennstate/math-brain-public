from fractions import Fraction as R
from functools import lru_cache
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
N=24;BITS=64;SCALE=1<<BITS
def down(x):return R(x.numerator*SCALE//x.denominator,SCALE)
def up(x):return -down(-x)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    vals=[x*y for x in a for y in b];return min(vals),max(vals)
def div(a,b):
    assert b[0]>0 or b[1]<0
    vals=[x/y for x in a for y in b];return min(vals),max(vals)
def sq(a):return (R(0) if a[0]<=0<=a[1] else min(x*x for x in a),max(x*x for x in a))
def powi(a,n):
    if n==0:return R(1),R(1)
    if n==2:return sq(a)
    if n%2==0:return powi(sq(a),n//2)
    return mul(a,powi(a,n-1))
def const(x):return R(x),R(x)
def series(x):
    z=(x-1)/(x+1);zz=z*z;t=z;total=R(0)
    for j in range(N):total+=t/(2*j+1);t*=zz
    tail=2*abs(t)/((2*N+1)*(1-zz))
    return 2*total-tail,2*total+tail
L2=series(R(2))
@lru_cache(maxsize=12000)
def log2(x):
    assert x>0;k=0
    while x<1:x*=2;k-=1
    while x>2:x/=2;k+=1
    v=series(x);corners=[a/b+k for a in v for b in L2]
    return down(min(corners)),up(max(corners))
def log_interval(a):return log2(a[0])[0],log2(a[1])[1]
def model(m):
    one=const(1);plus=add(m,one);minus=sub(m,one);v=sub(one,sq(m));c=sq(m)
    S=sub(add(sq(m),mul(const(2),m)),one)
    P=sub(sub(add(add(powi(m,4),mul(const(4),powi(m,3))),mul(const(2),sq(m))),mul(const(4),m)),const(11))
    d0=div(mul(mul(minus,powi(plus,3)),add(m,const(3))),const(16))
    C0=div(mul(S,P),const(16))
    u0=div(sq(C0),sq(d0))
    ua=sq(div(mul(mul(minus,plus),add(m,const(3))),S))
    ub=sq(div(S,plus));uc=sq(plus)
    w0=sq(d0)
    wa=div(mul(mul(sq(S),sq(plus)),add(mul(const(4),mul(v,sq(plus))),mul(const(2),sq(v)))),const(256))
    wb=div(mul(mul(sq(v),powi(plus,4)),sq(add(m,const(3)))),const(256))
    wc=mul(v,mul(sq(minus),mul(powi(plus,4),sq(add(m,const(3))))))
    wc=add(wc,mul(const(4),mul(sq(v),mul(sq(plus),sq(S)))))
    wc=add(wc,mul(const(2),mul(powi(v,3),sq(S))))
    wc=add(wc,mul(const(4),mul(powi(v,3),powi(plus,4))))
    wc=add(wc,mul(const(4),mul(powi(v,4),sq(plus))))
    wc=div(add(wc,powi(v,5)),const(256))
    return c,[(w0,u0),(wa,ua),(wb,ub),(wc,uc)]
def slope_bound(lo,hi):
    c,groups=model((lo,hi));a=const(0)
    for weight,u in groups:
        ratio=div(u,c)
        if ratio[0]<=0:return None
        a=add(a,mul(weight,log_interval(ratio)))
    return down(a[0]),up(a[1])
def cover(lo,hi,maxdepth=11):
    stack=[(lo,hi,0)];leaves=[];visited=0;start=time.perf_counter()
    while stack:
        a,b,depth=stack.pop();visited+=1;iv=slope_bound(a,b)
        if iv is not None and iv[0]>0:
            leaves.append({'m_box':[str(a),str(b)],'A_interval':[str(x) for x in iv]})
        elif depth==maxdepth:raise AssertionError(('unresolved',str(a),str(b),iv))
        else:
            mid=(a+b)/2;stack.extend([(a,mid,depth+1),(mid,b,depth+1)])
        if time.perf_counter()-start>110:raise RuntimeError('Frozen budget exceeded')
    leaves.sort(key=lambda x:R(x['m_box'][0]))
    assert R(leaves[0]['m_box'][0])==lo and R(leaves[-1]['m_box'][1])==hi
    for x,y in zip(leaves,leaves[1:]):assert x['m_box'][1]==y['m_box'][0]
    return {'domain':[str(lo),str(hi)],'leaves':leaves,'visited':visited,'min_certified_A_lower':str(min(R(x['A_interval'][0]) for x in leaves))}
def main():
    start=time.perf_counter();(ROOT/'out').mkdir(exist_ok=True)
    covers=[]
    for name,lo,hi in [('MINORITY_ORIENTATION',R(9,16),R(7,8)),('COMPLEMENT_ORIENTATION',R(-9,16),R(-1,2))]:
        cert=cover(lo,hi)
        (ROOT/'out'/(name+'.json')).write_text(json.dumps(cert,indent=2),encoding='utf-8')
        covers.append(cert);print(name,'leaves',len(cert['leaves']),'lower',cert['min_certified_A_lower'],flush=True)
    # Check grouped exact weights against a separately derived Walsh profile
    # at fixed rational points, without importing another agent's code.
    from pilot import WH
    checks=0
    for m in [R(9,16),R(3,4),R(7,8),R(-9,16),R(-1,2)]:
        c,groups=model((m,m));uu=[];dd=[]
        for T in range(0,64,2):
            k=T.bit_count();C=d=R(0)
            for W in range(64):
                if W&T==T:C+=R(WH[W],64)*m**(W.bit_count()-k)
                if W&(T|1)==T|1:d+=R(WH[W],64)*m**(W.bit_count()-k-1)
            U=(1-m*m)**k*C*C;D=(1-m*m)**k*d*d
            uu.append(U);dd.append(D)
        assert sum(dd)==(1-m)*(1+m)**3*(3+m)/16;checks+=1
        for weight,u in groups:
            assert weight[0]==weight[1] and u[0]==u[1]
            assert sum(D for U,D in zip(uu,dd) if U/D==u[0])==weight[0];checks+=1
    result={'continuum_domain':'every original minority p in [1/16,1/2], all t>=0','orientation':'unchanged if p<=7/32; complement if p>7/32','interval_boxes':sum(len(x['leaves']) for x in covers),'visited_boxes':sum(x['visited'] for x in covers),'exact_grouping_checks':checks,'analytic_boundary_domains':['t=0 via geometric mean lemma','m in [-1/2,0] via pointwise U>=m^2 D','m=0 via phi positivity'],'runtime_seconds':time.perf_counter()-start,'proof_status':'certificate checked; full analytic implication requires PROOF.md; independent review pending'}
    (ROOT/'out'/'CONTINUUM_RESULT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
