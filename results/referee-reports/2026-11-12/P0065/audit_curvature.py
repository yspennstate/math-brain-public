"""Independent expansion at zero, checked with symbolic quotient differentiation."""
import signal
signal.alarm(280)
import json
import mpmath as mp
import sympy as sp


def main():
    t,n,u,A,b2,c2=sp.symbols('t n u A b2 c2',nonzero=True)
    B=1-u*t+b2*t*t/2
    C=n-A*t+c2*t*t/2
    W=B*C/(t-1+B+C)
    second=sp.simplify(sp.diff(W,t,2).subs(t,0))
    factored=b2*(1-1/n)+2*u*A/n+2*(1-u-A)*(1+u*(n-1))/n**2
    assert sp.simplify(second-factored)==0
    # Conditional expectations: E u=a, E u^2=v, E b2=2(v-a^2),
    # E A|N=n=n*a, independent of the auxiliary tree's variables.
    a,v=sp.symbols('a v')
    expanded=sp.Poly(sp.expand(factored),u,A,b2)
    expectation=0
    for powers,coeff in expanded.terms():
        up,ap,bp=powers
        assert ap<=1 and bp<=1
        umoment=[1,a,v][up]
        amoment=[1,n*a][ap]
        bmoment=[1,2*(v-a*a)][bp]
        expectation+=coeff*umoment*amoment*bmoment
    target=2*(v-a*a)-4*(v-a*a)/n+2*(1-2*a+v)/n**2
    assert sp.simplify(expectation-target)==0
    mp.mp.dps=60
    laws={'12':[(1,mp.mpf('.5')),(2,mp.mpf('.5'))],
          '24':[(2,mp.mpf('.5')),(4,mp.mpf('.5'))],
          '123':[(i,mp.mpf(1)/3) for i in (1,2,3)],
          'geom':[(i,mp.mpf(2)**-i) for i in range(1,401)]}
    results={}
    for name,law in laws.items():
        a=sum(p/n for n,p in law); v=sum(p/n**2 for n,p in law)
        ell=sum(p*mp.log(n) for n,p in law)
        h=sum(p*mp.log(n)/n for n,p in law)
        h2=sum(p*mp.log(n)/n**2 for n,p in law)
        slope=(1-a)*(a*ell-h)
        var=v-a*a
        curvature=-4*var*(h-a*ell)+2*(1-2*a+v)*(h2-v*ell)-(1-a)*var+2*slope*(2*a-a*a)
        m=sum(n*p for n,p in law)
        results[name]=dict(curvature=mp.nstr(curvature,45),
                           linear_prediction_quotient=mp.nstr(slope+mp.mpf('.01')*m*curvature,45))
    result=dict(formula='d2 = -4 Var(1/N) Cov(log N,1/N) + 2(1-2a+v) Cov(log N,1/N^2) - (1-a)Var(1/N) + 2 d1 (2a-a^2)',
                W2conditional=str(target),results=results)
    with open('curvature_results.json','w') as f: json.dump(result,f,indent=2)
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
