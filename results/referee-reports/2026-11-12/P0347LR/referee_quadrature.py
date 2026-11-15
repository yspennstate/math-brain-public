"""Independent quadrature of (4), canceled linear form, and endpoint diagnostics."""
import json
from math import factorial
import mpmath as mp

def run(dps):
    mp.mp.dps=dps
    z=mp.zeta(2)
    def g(x):
        if x==0 or x==1:return mp.mpf(0)
        return (x*mp.log(x)+(1-x)*mp.log1p(-x))/z
    def integ(f):
        return mp.quad(lambda x:f(x)/(2*x*(1-x)) if 0<x<1 else 0,
                       [0,mp.mpf('.01'),mp.mpf('.25'),mp.mpf('.5'),mp.mpf('.75'),mp.mpf('.99'),1])
    a=[mp.mpf(1),mp.mpf(0)];details=[]
    for k in range(2,9):
        terms=[]
        for aa in range(k):
            for bb in range(k):
                c=k-aa-bb
                if c<0 or a[aa]==0 or a[bb]==0:continue
                coeff=mp.mpf(factorial(k))/(factorial(aa)*factorial(bb)*factorial(c))*a[aa]*a[bb]
                terms.append((aa,bb,c,coeff))
        R=lambda x:sum(co*x**aa*(1-x)**bb*g(x)**c for aa,bb,c,co in terms)
        raw_integral=integ(R);drift=k*a[k-1];hk=mp.harmonic(k-1)
        ak=(drift+raw_integral)/hk
        # Evaluate the four categories separately, with cancellation inside the integrand.
        linear= k*a[k-1]*integ(lambda x:g(x)*(x**(k-1)+(1-x)**(k-1)-1))
        cat=[]
        for typ in range(3):
            ts=[t for t in terms if (t[2]==0 if typ==0 else t[2]==1 and t[0]>0 and t[1]>0 if typ==1 else t[2]>=2)]
            cat.append(integ(lambda x:sum(co*x**aa*(1-x)**bb*g(x)**c for aa,bb,c,co in ts)))
        canceled=(linear+sum(cat))/hk
        assert abs(ak-canceled)<mp.mpf(10)**(-dps+8)
        a.append(ak)
        details.append({'k':k,'a':mp.nstr(ak,dps-5),'raw_R':mp.nstr(raw_integral,30),
            'drift':mp.nstr(drift,30),'canceled_linear':mp.nstr(linear,30),
            'c0':mp.nstr(cat[0],30),'c1_cross':mp.nstr(cat[1],30),'cge2':mp.nstr(cat[2],30),
            'canceled_difference':mp.nstr(ak-canceled,8),
            'factorial_ratio':mp.nstr(abs(ak)/(2**k*factorial(k)),20)})
        print(dps,k,mp.nstr(ak,24),flush=True)
    assert abs(a[2]-(2*mp.zeta(3)-z)/z**2)<mp.mpf(10)**(-dps+8)
    J3=6*mp.zeta(4)-3*mp.zeta(3)-mp.mpf('1.5')*z
    assert abs(a[3]-(a[2]/z-2*J3/(3*z**3)))<mp.mpf(10)**(-dps+8)
    endpoint=[]
    for e in [3,6,12,24]:
        x=mp.mpf(10)**(-e);F=(x*x*mp.log(x)+(1-x)**2*mp.log1p(-x))/(2*x*(1-x))
        old=x*abs(mp.log(x))
        endpoint.append({'x':str(x),'integrand':mp.nstr(F,30),'ratio_to_old_bound':mp.nstr(abs(F)/old,20)})
    return {'dps':dps,'moments':details,'entropy_mass':mp.nstr(integ(lambda x:-g(x)),35),
            'majorant_sum':mp.nstr(mp.mpf(1)/2+mp.mpf(1)/12+mp.mpf(1)/24+mp.exp(mp.mpf('.5'))-mp.mpf('1.5'),35),
            'endpoint_counterexample':endpoint}

data=[run(40),run(65)]
data[1]['max_precision_discrepancy']=str(max(abs(mp.mpf(u['a'])-mp.mpf(v['a'])) for u,v in zip(data[0]['moments'],data[1]['moments'])))
json.dump(data,open('referee_quadrature.json','w'),indent=2)
