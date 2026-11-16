"""Universal lower-trace comparison and padding bounds over exact rationals."""
import sys,json
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited19'))
from transfer35 import bernstein
from inherited18.inherited17.lower_formula import x3
from inherited18.inherited17.memory_guard import install

def main():
    install(850_000_000)
    k,t,d,z,v,S,trace=s.symbols('k t d z v S trace');c=s.Rational(31,20)
    f=(4/k-s.Rational(4,7))*d+x3(k,(k-1-t)/2,c-d)-x3(s.Integer(7),(7-t)/2,c-d)
    records=[]
    for lo,hi in ((0,2),(2,4),(4,5)):
        for dd in (s.Integer(0),s.Rational(11,20)):
            p=s.expand(s.cancel(980*k*k*(f-s.Rational(1,4))).subs({k:9+z,d:dd,t:lo+(hi-lo)*v}))
            for ids,control in bernstein(p,(v,),(2,)):
                q=s.Poly(control,z)
                assert q.degree()==2 and all(cc>0 for cc in q.all_coeffs())
                records.append(dict(tau_interval=[lo,hi],d=str(dd),control=ids[0],polynomial=str(control)))
    assert s.Poly(s.cancel(k*k*f),d).degree()==1
    m,h,A=s.symbols('m h A');F=lambda a:A+x3(k,m+a/2,h)
    assert s.cancel(F(trace)-(1-trace/S)*F(0)-trace/S*F(S)-trace*(S-trace)/k)==0
    assert s.cancel((7-t)/2+(k-8)/2-(k-1-t)/2)==0
    # Padding on the transferred endpoint domain: M>=3/2, 1<=h<=31/20.
    M,h,B,dt,r,a=s.symbols('M h B dt r a')
    derivative=s.diff(s.expand(x3(1/r,M,h)+2*(1+2*r)*B),r)
    upper=4*dt+(M-1)*(-s.Rational(22,7)-4*M+s.Rational(22,7)*h)
    assert s.expand(upper.subs(dt,B)-derivative-(s.Rational(8,7)-8*r)*(M-1)*(h-1))==0
    reduced=s.expand(upper.subs({M:s.Rational(3,2)+a,h:c-dt}))
    at0=-s.Rational(299,140)+s.Rational(17,7)*dt
    assert s.expand(reduced-at0+4*a*a+a*(s.Rational(439,70)+s.Rational(22,7)*dt))==0
    assert at0.subs(dt,s.Rational(11,20))==-s.Rational(4,5)
    # Fixed-graph infinity lower increment equals 2 tr(D-D^2)+trace.
    assert s.limit(x3(k,m+trace/2,h)-x3(k,m,h),k,s.oo)==trace
    Path('lower45_controls.json').write_text(json.dumps(dict(controls=records,lower_margin='1/4',inverse_padding_derivative_margin='4/5'),indent=2)+'\n')
    print('PROVED (lower45.py): maximal lower endpoint >= isolate k=7 plus 1/4 for k>=9 and infinity; interpolation; transferred endpoints hardest at k=7.')
if __name__=='__main__':main()
