"""Exact, bounded source-contract audit; no third-party imports or floating signs."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import prod
import argparse, hashlib, json, time

ROOT = Path(__file__).resolve().parents[1]
checks = 0

def check(b):
    global checks
    checks += 1
    assert b, checks

def walsh(v):
    a=list(v); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def truth(r):
    return [prod(-1 if ((x&1)==0 and (x>>(2*j+1)&3)==0) else 1
                 for j in range(r)) for x in range(1<<(2*r+1))]

def edge(v):
    n=(len(v)).bit_length()-1
    return [F(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v)) for i in range(n)]

def project(p, coords):
    q=[F(0) for _ in range(1<<len(coords))]
    for s,m in enumerate(p):
        t=sum(((s>>i)&1)<<j for j,i in enumerate(coords));q[t]+=m
    return q

def certificate(v, q):
    w=walsh(v); D=len(v)**2
    I=sum(edge(v)); exponent=4*I*D
    check(exponent.denominator==1)
    lhs=1<<int(exponent); rhs=1
    for wt,qt in zip(w,q):
        if wt:
            check(qt>0)
            lhs*=pow(qt.numerator,wt*wt)
            rhs*=pow(qt.denominator,wt*wt)
    check(lhs>=rhs)
    return {'D':D,'rate_exponent':int(exponent),'lhs_bits':lhs.bit_length(),
            'rhs_bits':rhs.bit_length(),
            'comparison_sha256':hashlib.sha256((str(lhs)+':'+str(rhs)).encode()).hexdigest()}

def run(widths):
    records=[];counts={};ghost=[]
    for r in widths:
        v=truth(r); n=2*r+1; N=len(v)
        w=walsh(v); original=[F(a*a,N*N) for a in w]
        check(F(sum(v),N)==(1+F(1,2**r))/2)
        check(sum(edge(v))==F(r+1,2)-F(1,2**(r+1)))
        count=0
        for a in product((-1,0,1),repeat=n):
            free=[i for i,z in enumerate(a) if z==-1]
            fixed=sum(z<<i for i,z in enumerate(a) if z!=-1)
            vr=[v[fixed+sum(((x>>j)&1)<<i for j,i in enumerate(free))]
                for x in range(1<<len(free))]
            essential=[i for i,inf in enumerate(edge(vr)) if inf]
            coords=[free[i] for i in essential]
            vc=[vr[sum(((x>>j)&1)<<i for j,i in enumerate(essential))]
                for x in range(1<<len(essential))]
            q=project(original,coords)
            check(sum(q)==1)
            wc=walsh(vc);check(sum(x*x for x in wc)==len(vc)**2)
            check(sum(edge(vc))==sum(F(x*x,len(vc)**2)*s.bit_count() for s,x in enumerate(wc)))
            # Independent closed formula for every projected ORIGINAL reference row.
            d=sum(i!=0 for i in coords); mu=F(1,2**r)
            if 0 in coords:
                for s,qs in enumerate(q):
                    expected=(1+(1 if (s&1)==0 else -1)*2*mu+F(1,2**d))/4 if (s>>1)==0 else F(1,2**(d+2))
                    check(qs==expected)
            else:
                for s,qs in enumerate(q):
                    check(qs==(F(1,2) if s==0 else 0)+F(1,2**(d+1)))
            cert=certificate(vc,q)
            records.append({'r':r,'assignment':a,'essential':coords,'truth':vc,
                            'reference':[[t.numerator,t.denominator] for t in q],**cert})
            count+=1
        counts[r]=count
        qghost=project(original,list(range(1,n)))
        alpha=(1+F(1,4**r))/2
        check(qghost[0]==alpha);check(F(1,2)<alpha<1)
        check(0<sum(qghost[1:]));check(project(original,[])[0]==1)
        ghost.append({'r':r,'irrelevant_coordinates':2*r,'alpha':[alpha.numerator,alpha.denominator]})
    # Rational inequalities used in the all-width proof, NOT an all-width census.
    for t in range(2,65):
        b=F(1,2**t)
        check(t-F(1,2)-2*b+(t-F(1,2))*b*b>0)
    check(F(45,16)<3);check(F(53,16)<5)
    check(F(11,8)-F(17,32)==F(27,32))
    return records,{'counts':counts,'ghost_controls':ghost,'checks':checks,'status':'PASS'}

if __name__=='__main__':
    import sys
    sys.set_int_max_str_digits(0)
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
    started=time.perf_counter();records,result=run([2] if args.pilot else [2,3])
    result['seconds']=time.perf_counter()-started
    result['helper_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    label='PILOT' if args.pilot else 'CHECKS'
    (ROOT/'out'/f'{label}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    if not args.pilot:
        (ROOT/'out'/'SOURCE_CERTIFICATES.json').write_text(json.dumps(records,separators=(',',':'))+'\n',encoding='utf-8')
    print(json.dumps(result))
