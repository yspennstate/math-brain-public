"""Algebra and high precision checks for an equal-connection mixed collar."""
import json,time,resource
from pathlib import Path
import sympy as sp
import mpmath as mp
from mp_core import *

def limiting(a,h):
    b0=h*(1-h);b1=mp.mpf('.5')-b0;k=b1/b0;K=2*mp.log(k)
    f=1/b0-1/(2*b1);g=1/(2*b1);v=1/b0-3
    return (f*f-(g-K)**2)/(f*f-g*g+f*K*(v+1/v)+K*K)

def q_weak(a,h,e):
    return kernel([a,mp.mpf('.5'),mp.mpf('.5'),e,0,e,0,h-mp.mpf('.5'),0])

def symbolic():
    a,h,z=sp.symbols('a h z',positive=True);b0=h*(1-h);b1=sp.Rational(1,2)-b0
    # Atom order is 0,1,2,12,3,13,23,123; z=e^2.
    p0=[(1-a)*b0,a*b0,(1-a)*b1,a*b1,(1-a)*b1,a*b1,(1-a)*b0,a*b0]
    c=[-2*h,2*h,2*h-1,1-2*h,2*h-1,1-2*h,2*(1-h),-2*(1-h)]
    gamma=sum(sign*c[i]/p0[i] for i,sign in ((7,1),(1,1),(2,1),(4,1),(0,-1),(3,-1),(5,-1),(6,-1)))
    ell=c[1]/p0[1]+c[4]/p0[4]-c[0]/p0[0]-c[5]/p0[5]
    P=sp.factor(ell-h*gamma);S=sp.factor(ell-(1-h)*gamma)
    assert sp.cancel(gamma-(2*h-1)/(a*(1-a)*b0*b1))==0
    assert sp.cancel(P-1/(a*(1-a)*b1))==0
    assert sp.cancel(S-(1-3*b0)/(a*(1-a)*b0*b1))==0
    # Independent full fixed-space Fisher matrix at zero connection.
    cvar=sp.symbols('cvar',positive=True)
    bg=(h+cvar)/2-h*cvar
    pg=[(1-a)*(1-h)*(1-cvar)-2*(1-cvar)*z,
        a*(1-h)*(1-cvar)+2*(1-cvar)*z,
        (1-a)*bg+(1-2*cvar)*z,a*bg+(2*cvar-1)*z,
        (1-a)*bg+(1-2*cvar)*z,a*bg+(2*cvar-1)*z,
        (1-a)*h*cvar+2*cvar*z,a*h*cvar-2*cvar*z]
    GG=sp.Matrix([[sp.diff(pp,vv).subs({cvar:1-h,z:0}) for vv in (a,h,cvar)]+[sp.sqrt(2)*cc] for pp,cc in zip(pg,c)])
    FF=sp.simplify(GG.T*sp.diag(*[1/pp for pp in p0])*GG)
    ff=1/b0-1/(2*b1);gg=1/(2*b1)
    assert all(sp.cancel(FF[i,j])==0 for i in (0,3) for j in (1,2))
    assert sp.cancel(FF[0,3])==0
    assert sp.cancel(FF[1,1]-ff)==0 and sp.cancel(FF[2,2]-ff)==0 and sp.cancel(FF[1,2]-gg)==0
    fisher0=str(FF)
    k,K=sp.symbols('k K',positive=True);f=2*k+1-1/k;g=1+1/k;v=2*k-1
    N=f*f-(g-K)**2;D=f*f-g*g+f*K*(v+1/v)+K*K
    target=K*(4*(k-1/k)+2*K/k-K*K)
    assert sp.cancel((K+1)*N-D-target)==0
    return dict(fixed_space_fisher_at_zero=fisher0,atom_constants=list(map(str,p0)),atom_slopes=list(map(str,c)),gamma_coefficient=str(sp.factor(gamma)),P=str(P),S=str(S),lower_bound_identity='(K+1)N-D = K[4(k-1/k)+2K/k-K^2]',symbolic_remainders='all zero')

def main():
    start=time.monotonic();out=symbolic();out['fixed_checks']=[];out['mixed_checks']=[]
    mp.mp.dps=160;a=mp.mpf('.37');h=mp.mpf('.1');m0=limiting(a,h)
    for j in (2,4,8,16,32):
        e=mp.mpf(10)**(-j);val=evaluate(q_weak(a,h,e))
        out['fixed_checks'].append(strings(dict(a=a,h=h,e=e,limit=m0,margin=val['margin'],error=val['margin']-m0,error_over_e2=(val['margin']-m0)/e**2)))
    for L in (10,20,60,150,400,1000):
        mp.mp.dps=120+int(6*L/mp.log(10));t=mp.exp(-L)
        for alpha,beta,eta in ((1,2,2),(.5,2,2),(2,2,2.1),(1,2,16)):
            a=1-t**mp.mpf(str(alpha));h=t**mp.mpf(str(beta));e=t**mp.mpf(str(eta));ev=evaluate(q_weak(a,h,e));m0=limiting(a,h)
            nu=a*(1-a)*h*(1-h);K=2*mp.log((mp.mpf('.5')-h*(1-h))/(h*(1-h)))
            threshold=nu**8/(mp.mpf('8e13')*(K+1))
            retries=0
            if eta==16:
                # Deep graph degeneration can consume thousands of digits in
                # the ambient solve. Resolve the proved remainder, rather than
                # interpreting a low-precision difference as an asymptotic error.
                while abs(ev['margin']-m0)>min(mp.mpf('4e13')*e**2/nu**8,mp.mpf('1e-70')):
                    mp.mp.dps*=2;retries+=1
                    if mp.mp.dps>50000:raise ArithmeticError('mixed remainder precision cap')
                    t=mp.exp(-L);a=1-t**mp.mpf(str(alpha));h=t**mp.mpf(str(beta));e=t**mp.mpf(str(eta))
                    ev=evaluate(q_weak(a,h,e));m0=limiting(a,h)
                    nu=a*(1-a)*h*(1-h);K=2*mp.log((mp.mpf('.5')-h*(1-h))/(h*(1-h)))
                    threshold=nu**8/(mp.mpf('8e13')*(K+1))
                print('resolved mixed remainder',L,mp.mp.dps,retries,flush=True)
            out['mixed_checks'].append(strings(dict(L=L,precision=mp.mp.dps,precision_retries=retries,alpha=alpha,beta=beta,eta=eta,margin=ev['margin'],limit=m0,scaled=ev['scaled'],error=abs(ev['margin']-m0),uniform_error_bound=mp.mpf('4e13')*e**2/nu**8,in_proved_collar=bool(e**2<=threshold),lower_bound=1/(2*(K+1)))))
    out['seconds']=time.monotonic()-start;out['peak_rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20
    Path('data/mixed_limit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
