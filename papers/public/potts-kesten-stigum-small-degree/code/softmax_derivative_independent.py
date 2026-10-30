"""Independent Fraction/cumulant replay of the exact softmax box cover.

Does not import the producer or use its integer scaling/subdivision code.
"""
import hashlib,itertools,json,math,time
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp
HERE=Path(__file__).resolve().parent
u,v,t=sp.symbols('u v t');var=(u,v,t)

def independent_polynomials():
    p=(u,(1-u)*v,(1-u)*(1-v));N=sp.Rational(2,3)*(1-t+t*t)
    ans={}
    for name,h in [('endpoint',(0,t,1)),('middle',(t,0,1))]:
        mu=sum(p[i]*h[i] for i in range(3));r=h[0]-mu
        moments={k:sum(p[i]*(h[i]-mu)**k for i in range(3)) for k in (2,3,4)}
        d2=p[0]*(r*r-moments[2])
        d3=p[0]*(r**3-3*r*moments[2]-moments[3])
        d4=p[0]*(r**4-6*r*r*moments[2]-4*r*moments[3]+6*moments[2]**2-moments[4])
        for n,K,power,d in [(2,sp.Rational(1,5),1,d2),(4,sp.Rational(3,5),2,d4)]:
            for sign in (-1,1):ans[f'{name}_D{n}_{sign:+d}']=sp.Poly(K*N**power+sign*d,*var)
        ans[f'{name}_D3_squared']=sp.Poly(sp.Rational(4,25)*N**3-d3*d3,*var)
    return ans

def root_coefficients(poly,shape):
    terms=[(e,Q(int(c.p),int(c.q))) for e,c in poly.terms()]
    ans={}
    for k in itertools.product(*(range(n) for n in shape)):
        total=Q(0)
        for e,c in terms:
            if all(e[j]<=k[j] for j in range(3)):
                term=c
                for j in range(3):term*=Q(math.comb(k[j],e[j]),math.comb(shape[j]-1,e[j]))
                total+=term
        ans[k]=total
    return ans

def bisect(values,shape,axis):
    other=[j for j in range(3) if j!=axis];n=shape[axis]-1
    left={};right={}
    for fixed in itertools.product(*(range(shape[j]) for j in other)):
        base=dict(zip(other,fixed))
        def key(k):return tuple(k if j==axis else base[j] for j in range(3))
        row=[values[key(k)] for k in range(n+1)]
        L=[row[0]];R=[row[-1]]
        for _ in range(n):
            row=[(a+b)/2 for a,b in zip(row,row[1:])]
            L.append(row[0]);R.append(row[-1])
        for k in range(n+1):left[key(k)]=L[k];right[key(k)]=R[n-k]
    return left,right

def main():
    started=time.monotonic()
    source=HERE/'softmax_derivative_certificate.py';cert=HERE/'softmax_derivative_v1/report.json'
    report=json.loads(cert.read_text(encoding='utf-8'))
    assert report['status']=='EXACT BERNSTEIN COVER PASS'
    assert hashlib.sha256(source.read_bytes()).hexdigest()==report['source_sha256']
    rebuilt=independent_polynomials();assert len(rebuilt)==len(report['jobs'])==10
    receipts=[]
    for job in report['jobs']:
        poly=rebuilt.pop(job['name']);shape=tuple(poly.degree(z)+1 for z in var)
        assert tuple(job['shape'])==shape
        stored={(tuple(e),sp.Rational(c)) for e,c in job['root_power_terms']}
        assert stored==set(poly.terms())
        leaves={a['path']:a for a in job['leaves']};assert len(leaves)==len(job['leaves'])
        prefixes={p[:i] for p in leaves for i in range(len(p)+1)}
        seen=set();stack=[('',root_coefficients(poly,shape),int(job['root_denominator']))]
        while stack:
            path,coeffs,den=stack.pop()
            keys=itertools.product(*(range(n) for n in shape))
            integers=[]
            for key in keys:
                q=coeffs[key]*den;assert q.denominator==1
                integers.append(q.numerator)
            digest=hashlib.sha256(','.join(map(str,integers)).encode()).hexdigest()
            if not path:assert digest==job['root_sha256']
            if path in leaves:
                leaf=leaves[path];assert min(coeffs.values())>=0
                assert min(integers)==leaf['minimum'] and max(integers)==leaf['maximum']
                assert digest==leaf['sha256'];seen.add(path)
            else:
                assert path+'0' in prefixes and path+'1' in prefixes,'Cover has an unverified hole'
                axis=len(path)%3;left,right=bisect(coeffs,shape,axis)
                newden=den*2**(shape[axis]-1)
                stack.extend([(path+'1',right,newden),(path+'0',left,newden)])
        assert seen==set(leaves)
        receipts.append({'name':job['name'],'leaves':len(leaves),'complete_cover':True})
    assert not rebuilt
    result={'status':'INDEPENDENT EXACT FRACTION REPLAY PASS','at_seconds':time.monotonic()-started,
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'producer_sha256':report['source_sha256'],'certificate_sha256':hashlib.sha256(cert.read_bytes()).hexdigest(),
      'jobs':receipts,'scope':'Ten polynomial inequalities including all simplex boundary faces; analytic Lindeberg estimates are separate'}
    (HERE/'softmax_derivative_independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':main()
