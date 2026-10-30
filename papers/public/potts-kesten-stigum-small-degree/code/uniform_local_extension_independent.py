"""Independent QQ polynomial reconstruction with no computer-algebra imports.

The state is a few hundred rational coefficients, below 10 MB. Reconstructing
the rational prefix sums after cancelling d=1/l^2 avoids a slow generic CAS.
"""
import hashlib,json,math,pathlib,time
from fractions import Fraction as F
ROOT=pathlib.Path(__file__).resolve().parent
ONE={(0,0):F(1)};ELL={(1,0):F(1)};R={(0,1):F(1)}

def add(*args):
    out={}
    for poly in args:
        for key,value in poly.items():out[key]=out.get(key,F(0))+value
    return {key:value for key,value in out.items() if value}

def scale(poly,value):return {key:value*v for key,v in poly.items() if value*v}

def mul(*args):
    result=ONE
    for poly in args:
        out={}
        for (a,b),v in result.items():
            for (c,d),w in poly.items():out[a+c,b+d]=out.get((a+c,b+d),F(0))+v*w
        result={key:value for key,value in out.items() if value}
    return result

def expected_numerator(m,margin):
    # w=l^2, K=k*w; the interval coordinate is k=2+r*(1/w-2).
    w=mul(ELL,ELL);D=add(ONE,scale(w,-1));plus=add(ONE,ELL)
    K=add(R,scale(mul(add(ONE,scale(R,-1)),w),2))
    Km=add(K,scale(w,-1));Kmm=add(K,scale(w,-2))
    H1=add(mul(K,Km),scale(mul(w,w),-2))
    H2=mul(K,Km,Kmm)
    N=scale(add(mul(K,Km),scale(add(ONE,scale(K,-1)),2)),F(5,2))
    # Cu=N/D; Ct=J/D. The summed j,j(j-1) formulas give H1,H2.
    J=scale(mul(plus,N),F(1,3))
    w2=mul(w,w);w3=mul(w2,w);w4=mul(w2,w2);D2=mul(D,D);D3=mul(D2,D)
    A=add(scale(mul(N,w3,D),F(1,9)),scale(mul(H2,D3),F(1,216)),
          scale(mul(plus,N,H1,w,D),F(1,18)),scale(mul(plus,H2,D2),F(5,108)))
    Bpre=scale(add(scale(mul(J,J,w3),3),mul(ELL,N,J,w3),scale(mul(N,N,w4),F(1,12))),F(1,9))
    X=add(scale(mul(ELL,J),3),scale(mul(N,w),F(1,2)))
    Y=add(scale(mul(ELL,J,w),F(1,2)),scale(mul(N,w2),F(1,12)))
    Z=add(scale(mul(ELL,J),F(1,2)),scale(mul(N,w),F(1,12)))
    Bmerge=scale(mul(plus,add(scale(mul(X,ELL,J,H1),F(1,2)),
                    scale(mul(Y,N,H1),F(1,2)),
                    mul(D,add(scale(mul(X,H2),F(5,18)),scale(mul(Z,H2),F(5,6)))))),F(1,9))
    B=add(Bpre,Bmerge);g=scale(mul(K,Km),F(1,12))
    # This returns D^3*((1-margin)*g-m*A_k-m^2*B_k).
    return add(scale(mul(g,D3),1-margin),scale(A,-m),scale(B,-m*m))

def load(name,phase):
    data=json.loads(ROOT.joinpath(f'uniform_local_{name}_{phase}.json').read_text(encoding='utf-8'))
    return {tuple(key):F(value) for key,value in data.pop('poly')},data

def axis_check(before,after,axis,n):
    expected={}
    for key,value in before.items():
        for j in range(key[axis],n+1):
            kk=list(key);kk[axis]=j;kk=tuple(kk)
            expected[kk]=expected.get(kk,F(0))+value*F(math.comb(j,key[axis]),math.comb(n,key[axis]))
    expected={key:value for key,value in expected.items() if value}
    assert set(after)==set(expected)
    first=next(iter(expected));factor=after[first]/expected[first];assert factor>0
    assert all(after[key]==factor*value for key,value in expected.items())
    return str(factor)

def evaluate(poly,l,r):return sum(value*l**key[0]*r**key[1] for key,value in poly.items())

def direct_recursion(d,k):
    l=F(1,math.isqrt(d));assert l*l==F(1,d)
    d=F(d);Z=F(k*(k-1),2)+d*(d-k);Cu=5*Z/(d*(d-1));Ct=Cu*(1+l)/3
    A=Cu/(9*d*d*(d-1));B=d/(9*(d-1))*(3*Ct*Ct/d**3+l*Cu*Ct/d**3+Cu*Cu/(12*d**4))
    ve=Cu/d**2;te=l*Ct/d
    for j in range(2,k):
        uj=(j*Cu+F(5,2)*j*(j-1))/d**2;tj=j*l*Ct/d+F(5,6)*j*(j-1)/d**2
        A+=F(j*(j-1),1)/(72*d**3)+(uj/(2*d)+j*Cu/(2*d**3))/(9*(1-l))
        B+=(3*tj*te+(uj*te+tj*ve)/2+uj*ve/12)/(9*(1-l))
    return A,B,F(k*(k-1),1)/(12*d*d)

def main():
    for name in ('radius01_d42',):
        start=time.monotonic();raw,meta=load(name,'raw');current=raw;scales=[]
        for axis in (0,1):
            nxt,_=load(name,f'bern{axis+1}');scales.append(axis_check(current,nxt,axis,meta['degrees'][axis]));current=nxt
        assert all(value>0 for value in current.values())
        m=F(meta['M_radius']);margin=F(meta['retained_drift_fraction']);upper=F(meta['lambda_upper'])
        poly=expected_numerator(m,margin)
        expected={key:value*F(meta['denominator_positive_content'])*upper**key[0] for key,value in poly.items()}
        restored=scale(raw,F(meta['raw_content_divided_out'])/F(meta['raw_common_multiplier']))
        assert restored==expected
        # Additional independent exact values use the unsummed j recurrence.
        rows=[]
        for d in ((4,9,16,25,49) if name=='all_d3' else (49,64,81,100,121,144,225,400)):
            for k in sorted({2,3,d//2,d}):
                l=F(1,math.isqrt(d));r=F(k-2,d-2);A,B,g=direct_recursion(d,k)
                gap=(1-margin)*g-m*A-m*m*B
                assert evaluate(poly,l,r)==(1-l*l)**3*gap and gap>=0
                rows.append({'d':d,'k':k,'gap':str(gap)})
        report={'status':'PASS independent all-coefficient rational reconstruction',
          'name':name,'M_radius':str(m),'posterior_x_radius':str(m/9),'lambda_upper':str(upper),
          'retained_drift_fraction':str(margin),'degrees':meta['degrees'],'positive_coefficients':len(current),
          'implicit_zero_coefficients':math.prod(n+1 for n in meta['degrees'])-len(current),
          'positive_axis_scales':scales,'full_polynomial_identity':True,'direct_prefix_recursion_checks':rows,
          'estimated_memory_bytes':10*1024**2,'wall_seconds':time.monotonic()-start,
          'sha256':{f'uniform_local_{name}_{phase}.json':hashlib.sha256(ROOT.joinpath(f'uniform_local_{name}_{phase}.json').read_bytes()).hexdigest() for phase in ('raw','bern1','bern2','report')}}
        report['sha256']['uniform_local_extension_independent.py']=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
        ROOT.joinpath(f'uniform_local_{name}_fast_independent.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
        assert time.monotonic()-start<120
        print(json.dumps({key:value for key,value in report.items() if key not in ('sha256','direct_prefix_recursion_checks')}),flush=True)

if __name__=='__main__':main()
