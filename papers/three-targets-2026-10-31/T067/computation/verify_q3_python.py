"""Independent dependency-free exact integer expansion of T067 q3 certificates.

Reimplements the displayed six-variable polynomial identities in the manuscript
appendix, without importing either C++ encoder or any saved coefficient table.
Python integers are arbitrary precision; no numerical sign decisions are used.
"""
from itertools import permutations
from fractions import Fraction as Q
from pathlib import Path
import hashlib, json, math, time

# Six 6-bit exponent fields, sufficient for all degrees below 64.
def var(i): return {1 << (6*i): 1}
def add(*ps):
    r={}
    for p in ps:
        for k,v in p.items(): r[k]=r.get(k,0)+v
    return {k:v for k,v in r.items() if v}
def scale(p,c): return {k:v*c for k,v in p.items() if v*c}
def mul(p,q):
    if len(p)>len(q): p,q=q,p
    r={}
    for k,v in p.items():
        for l,w in q.items():
            z=k+l
            r[z]=r.get(z,0)+v*w
    return {k:v for k,v in r.items() if v}
def prod(*ps):
    r={0:1}
    for p in ps:r=mul(r,p)
    return r
def powp(p,n):return prod(*([p]*n))
def forms(off):
    a,b,c=[var(off+j) for j in range(3)]
    s=add(a,b,c)
    x=add(scale(powp(a,2),4),scale(prod(a,b),2),powp(b,2))
    y=add(scale(powp(a,3),8),scale(prod(a,a,b),6),scale(prod(a,b,b),-3),scale(powp(b,3),-1))
    h=add(scale(prod(y,s),4),scale(prod(x,x),-1))
    f=add(scale(prod(x,s),3),scale(y,-1))
    g=add(scale(powp(s,2),4),scale(x,-1))
    p=[add(scale(a,6),scale(b,3),scale(c,2)),add(scale(b,3),scale(c,2)),scale(c,2)]
    return s,x,y,h,f,g,p

def certificate(mode):
    s,x,y,h,f,g,p=forms(0)
    t,X,Y,H,F,G,q=forms(3)
    s2,t2=powp(s,2),powp(t,2)
    strict=prod(x,X,s2,t2)
    if mode==0:
        k=add(scale(prod(x,s2,powp(t,4)),8000),scale(prod(X,t2,powp(s,4)),8000),scale(prod(h,F,t),-125),scale(prod(f,H,s),-125),scale(strict,-2))
    else:
        k=add(scale(prod(h,G,t2),-125),scale(prod(g,H,s2),-125),scale(strict,-1))
    zs=[]; ns=[]
    for perm in permutations(range(3)):
        u=[prod(p[j],q[perm[j]]) for j in range(3)]
        z=add(*u)
        w=[add(scale(v,3),scale(z,-1)) for v in u]
        v=add(*(prod(v,v) for v in w))
        n=add(scale(prod(z,*w),36),scale(prod(v,v),-1)) if mode else v
        zs.append(z);ns.append(n)
    power=3 if mode else 1
    denominator=prod(*(z for z in zs for _ in range(power)))
    result=scale(prod(k,denominator),81 if mode else 27)
    terms=[]
    for i,n in enumerate(ns):
        rest=prod(*(z for j,z in enumerate(zs) if i!=j for _ in range(power)))
        terms.append(prod(n,rest))
        print(f'mode={mode} summand={i+1}/6 terms={len(terms[-1])}',flush=True)
    summands=prod(add(*terms),powp(s,3),powp(t,3))
    result=add(result,scale(summands,250 if mode else -2000))
    return result

def exponents(k):return tuple((k>>(6*j))&63 for j in range(6))
def evaluate(poly,weights):
    powers=[[w**e for e in range(23)] for w in weights]
    return sum(v*math.prod(powers[j][e] for j,e in enumerate(exponents(k))) for k,v in poly.items())
def inv(p):
    v=[3*x-1 for x in p]
    x=sum(x*x for x in v)/6
    y=sum(x*x*x for x in v)/6
    return x,y,y-x*x/2,Q(3,2)*x-y,1-x
def oracle(mode,weights):
    a,b,c,d,e,f=weights;s=a+b+c;t=d+e+f
    P=(6*a+3*b+2*c,3*b+2*c,2*c); R=(6*d+3*e+2*f,3*e+2*f,2*f)
    p=[Q(v,6*s) for v in P];q=[Q(v,6*t) for v in R]
    xp,yp,hp,fp,gp=inv(p);xq,yq,hq,fq,gq=inv(q)
    fused=Q(0);den=1
    for perm in permutations(range(3)):
        U=[P[j]*R[perm[j]] for j in range(3)];Z=sum(U)
        den*=Z**(3 if mode else 1)
        if Z:
            ii=inv([Q(u,Z) for u in U]);z=Q(Z,12*s*t)
            fused+=z*ii[2 if mode else 0]/6
    gap=fused-hp*gq-gp*hq-xp*xq/1000 if mode else xp+xq-fused-hp*fq-fp*hq-xp*xq/1000
    return (1296000 if mode else 864000)*s**4*t**4*den*gap

def main():
    started=time.monotonic();results=[]
    cases=[(1,1,1,2,1,3),(1,2,3,3,2,1),(3,1,2,1,3,2),(0,1,0,0,1,1),(1,0,0,1,2,1),(0,0,1,3,1,0),(1,0,0,0,1,0),(0,1,0,0,1,0)]
    for mode,degree,expected_pos,expected_zero in [(0,10,3873,483),(1,22,71627,4549)]:
        start=time.monotonic();poly=certificate(mode)
        neg=sum(v<0 for v in poly.values());pos=sum(v>0 for v in poly.values())
        total=math.comb(degree+2,2)**2;zero=total-len(poly)
        for k in poly:
            ee=exponents(k)
            assert sum(ee[:3])==degree and sum(ee[3:])==degree
        assert neg==0 and pos==expected_pos and zero==expected_zero,(mode,neg,pos,zero)
        matches=[]
        for weights in cases:
            actual=evaluate(poly,weights);expected=oracle(mode,weights)
            assert actual==expected,(mode,weights)
            matches.append({'weights':weights,'exact_match':True})
        digest=hashlib.sha256()
        for k,v in sorted(poly.items()):digest.update((','.join(map(str,exponents(k)))+':'+str(v)+'\n').encode())
        table=Path(__file__).with_name('q3_independent_coefficients_'+('B' if mode else 'A')+'.tsv')
        triple=[(i,j,degree-i-j) for i in range(degree,-1,-1) for j in range(degree-i,-1,-1)]
        with table.open('w') as out:
            out.write('a\tb\tc\td\te\tf\tinteger_coefficient\n')
            for l in triple:
                for r in triple:
                    ee=l+r;k=sum(e<<(6*j) for j,e in enumerate(ee))
                    out.write('\t'.join(map(str,ee+(poly.get(k,0),)))+'\n')
        result={'mode':mode,'degree_per_block':degree,'positions':total,'positive':pos,'zero':zero,'negative':neg,'coefficient_sha256':digest.hexdigest(),'table_file':table.name,'table_sha256':hashlib.sha256(table.read_bytes()).hexdigest(),'identity_checks':matches,'seconds':time.monotonic()-start}
        results.append(result);print(json.dumps(result),flush=True)
    out={'status':'PASS','method':'Fresh independent Python arbitrary-integer expansion of displayed residual polynomials; no precomputed coefficient inputs; exact Fraction oracle identities at interior/boundary points.','manuscript':'A three-state posterior cone and reconstruction on finite-mean Galton-Watson trees, 31 October 2026','source_appendix':'paper/sections/certificate_appendix.tex','results':results,'seconds':time.monotonic()-started}
    output=Path(__file__).with_name('q3_python_result.json');output.write_text(json.dumps(out,indent=2)+'\n');print(str(output),flush=True)
if __name__=='__main__':main()
