"""Exact rational coefficient profiles with outward fixed-point log bounds, v1."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
P=192; Q=1<<P; K=80
def ceildiv(a,b):return -((-a)//b)
def scale(iv,r):
    assert r>=0
    return iv[0]*r.numerator//r.denominator,ceildiv(iv[1]*r.numerator,r.denominator)
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def constant(r):return scale((Q,Q),F(r))
def ln_unit(a,b):
    assert b<=a<=2*b
    zlo=(a-b)*Q//(a+b);zhi=ceildiv((a-b)*Q,a+b)
    zl2=zlo*zlo//Q;zh2=ceildiv(zhi*zhi,Q)
    pl,ph=zlo,zhi;lo=hi=0
    for j in range(K):
        lo+=2*pl//(2*j+1);hi+=ceildiv(2*ph,2*j+1)
        pl=pl*zl2//Q;ph=ceildiv(ph*zh2,Q)
    # Analytic remainder <= 2*(1/3)^(2K+1)/((2K+1)*(1-1/9)).
    hi+=ceildiv(18*Q,8*(2*K+1)*3**(2*K+1))
    return lo,hi
LN2=ln_unit(2,1)
@lru_cache(maxsize=30000)
def log2(r):
    assert r>0
    a,b=r.numerator,r.denominator;e=a.bit_length()-b.bit_length()
    if e>=0:
        if a<b<<e:e-=1
    elif a<<(-e)<b:e-=1
    if e>=0:bb=b<<e;aa=a
    else:aa=a<<(-e);bb=b
    if aa==bb:return e*Q,e*Q
    l,h=ln_unit(aa,bb)
    return e*Q+(l*Q//LN2[1]),e*Q+ceildiv(h*Q,LN2[0])
@lru_cache(maxsize=30000)
def phi_ratio(a,b,d):
    assert a>=0 and b>=0 and d>0
    if not a or not b:return 0,0
    return plus(scale(log2((a+b)/a),a/d),scale(log2((a+b)/b),b/d))
def lex_profile(n,t):
    profiles=[]
    for i in range(n):
        alpha=F(t%(1<<(i+1)),1<<(i+1));u=1-2*alpha;d=1-abs(u)
        if not d:continue
        J=constant(2-2*d)
        for j in range(i+1,n):
            c=1-2*((t>>j)&1)
            J=plus(J,scale(phi_ratio((u-c)**2,d*d,d),F(1,2)))
            u=(u+c)/2;d/=2
        ratio=plus(J,phi_ratio(u*u,d*d,d))
        profiles.append({'i':i,'influence':str(d),'ratio_interval':ratio})
    return profiles
def fwht(a):
    a=a.copy();h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for l in range(j,j+h):u,v=a[l],a[l+h];a[l],a[l+h]=u+v,u-v
        h*=2
    return [F(v,len(a)) for v in a]
OUTER=fwht([-1 if x<3 else 1 for x in range(32)])
def section(mu,j):
    v=1-mu*mu;rows=[]
    for T in range(32):
        if T&(1<<j):continue
        a=b=F(0)
        for U in range(32):
            if U&(1<<j) or U&T!=T:continue
            exponent=(U^T).bit_count()
            a+=OUTER[U]*mu**exponent;b+=OUTER[U|(1<<j)]*mu**exponent
        rows.append((T,a,b,v**T.bit_count()))
    q=sum(w*b*b for T,a,b,w in rows)
    return q,rows
def compositions(maxdepth):
    mu=F(0);classes=[{'path':'','influence':F(1),'J':(0,0)}];outputs=[]
    for depth in range(1,maxdepth+1):
        pp=(1+mu)/2;pm=(1-mu)/2
        munext=1-2*pp**3*(1-pm*pm)
        new=[]
        for tag,j in [('B',0),('T',2)]:
            q,rows=section(mu,j)
            assert q==(pp**3*pm if tag=='B' else pp*pp*(1-pm*pm))
            assert rows[0][2]==-q and rows[0][1]+mu*rows[0][2]==munext
            for old in classes:
                di=old['influence'];J=old['J']
                for T,a,b,w in rows:
                    if T and b and w:
                        J=plus(J,scale(phi_ratio((a+mu*b)**2,b*b*di*di,di),w/q))
                dni=q*di;ratio=plus(J,phi_ratio(munext*munext,dni*dni,dni))
                new.append({'path':old['path']+tag,'influence':dni,'J':J,'ratio_interval':ratio})
        best=min(new,key=lambda v:v['ratio_interval'][1])
        lower=min(c['ratio_interval'][0] for c in new)
        upper=best['ratio_interval'][1]
        outputs.append({'depth':depth,'physical_dimension':5**depth,'mean':str(munext),'classes':[dict(c,influence=str(c['influence'])) for c in new],'minimum_interval':[lower,upper],'best_path':best['path']})
        mu=munext;classes=new
    return outputs
def decimal(iv):
    # Display only; certificate consists of the integer endpoints divided by Q.
    return [str(float(F(x,Q))) for x in iv]
def main():
    start=time.perf_counter();lex=[]
    for n in range(5,25):
        t=(1<<n)//10;rows=lex_profile(n,t);best=min(rows,key=lambda r:r['ratio_interval'][1])
        lex.append({'n':n,'t':t,'minimum_interval':[min(r['ratio_interval'][0] for r in rows),best['ratio_interval'][1]],'best_i':best['i'],'display':decimal(best['ratio_interval']),'profiles':rows})
        assert time.perf_counter()-start<55
    comp=compositions(4)
    for c in comp:c['display']=decimal(c['minimum_interval'])
    result={'version':'profiles.py/v1','scale_bits':P,'ln_terms':K,'lex':lex,'composition':comp,'runtime_seconds':time.perf_counter()-start}
    (ROOT/'out'/'PROFILES.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'lex':[(r['n'],r['best_i'],r['display']) for r in lex],'composition':[(c['depth'],c['best_path'],c['display']) for c in comp],'runtime_seconds':result['runtime_seconds']}))
if __name__=='__main__':main()
