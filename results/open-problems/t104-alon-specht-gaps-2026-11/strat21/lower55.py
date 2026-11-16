"""Exact universal lower-trace comparison and endpoint padding."""
import sys,json
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited20/inherited19'))
from transfer35 import bernstein
from inherited18.inherited17.lower_formula import x3
from inherited18.inherited17.memory_guard import install

def main():
    install(300_000_000)
    k,t,d,z,v,S,trace=s.symbols('k t d z v S trace');c=s.Rational(8,5)
    f=(4/k-s.Rational(1,2))*d+x3(k,(k-1-t)/2,c-d)-x3(s.Integer(8),(8-t)/2,c-d)
    records=[]
    for lo,hi in ((0,2),(2,4),(4,6)):
        for dd in (s.Integer(0),s.Rational(3,5)):
            p=s.expand(s.cancel(320*k*k*(f-s.Rational(1,4))).subs({k:10+z,d:dd,t:lo+(hi-lo)*v}))
            for ids,control in bernstein(p,(v,),(2,)):
                q=s.Poly(control,z)
                print(lo,hi,dd,ids,q.all_coeffs(),flush=True)
                assert all(cc>0 for cc in q.all_coeffs())
                records.append(dict(tau_interval=[lo,hi],d=str(dd),control=ids[0],polynomial=str(control)))
    assert s.Poly(s.cancel(k*k*f),d).degree()==1
    m,h,A=s.symbols('m h A');F=lambda a:A+x3(k,m+a/2,h)
    assert s.cancel(F(trace)-(1-trace/S)*F(0)-trace/S*F(S)-trace*(S-trace)/k)==0
    assert s.cancel((8-t)/2+(k-9)/2-(k-1-t)/2)==0
    M,h,B,dt,r,a=s.symbols('M h B dt r a')
    derivative=s.diff(s.expand(x3(1/r,M,h)+2*(1+2*r)*B),r)
    upper=4*dt+(M-1)*(-3-4*M+3*h)
    assert s.expand(upper.subs(dt,B)-derivative-(1-8*r)*(M-1)*(h-1))==0
    reduced=s.expand(upper.subs({M:s.Rational(3,2)+a,h:c-dt}))
    at0=-s.Rational(21,10)+s.Rational(5,2)*dt
    assert s.expand(reduced-at0+4*a*a+a*(s.Rational(31,5)+3*dt))==0
    assert at0.subs(dt,s.Rational(3,5))==-s.Rational(3,5)
    assert s.limit(x3(k,m+trace/2,h)-x3(k,m,h),k,s.oo)==trace
    Path('lower55_controls.json').write_text(json.dumps(dict(controls=records,lower_margin='1/4',inverse_padding_derivative_margin='3/5'),indent=2)+'\n')
    print('PROVED (lower55.py): maximal lower endpoint >= isolate k=8 plus 1/4 for k>=10; interpolation; transferred endpoints hardest at k=8, including infinity.')
if __name__=='__main__':main()
