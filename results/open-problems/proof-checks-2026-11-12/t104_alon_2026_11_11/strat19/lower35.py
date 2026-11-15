"""Universal 3+5 maximal-lower-trace comparison without spending old margins."""
import sys,json
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited18'/'inherited17'))
from lower_formula import x3
from transfer35 import bernstein

def main():
    k,t,d,z,v,S,trace=s.symbols('k t d z v S trace');c=s.Rational(22,15)
    # All top pairs: M0=(6-t)/2, 0<=t<=4, h=c-d, B<=d<=7/15.
    f=(4/k-s.Rational(2,3))*d+x3(k,(k-1-t)/2,c-d)-x3(s.Integer(6),(6-t)/2,c-d)
    records=[]
    for lo,hi in ((0,2),(2,4)):
        for dd in (s.Integer(0),s.Rational(7,15)):
            num=s.expand(s.cancel(144*k*k*(f-s.Rational(1,4))).subs({k:8+z,d:dd,t:lo+(hi-lo)*v}))
            controls=bernstein(num,(v,),(2,))
            for ids,control in controls:
                q=s.Poly(control,z)
                assert q.degree()==2 and all(cc>0 for cc in q.all_coeffs())
                records.append({'tau_interval':[lo,hi],'d':str(dd),'control':ids[0],'polynomial':str(s.factor(control))})
    assert s.Poly(s.cancel(k*k*f),d).degree()==1
    # Exact trace interpolation and relation of endpoint masses.
    m,h,A=s.symbols('m h A');F=lambda a:A+x3(k,m+a/2,h)
    assert s.cancel(F(trace)-(1-trace/S)*F(0)-trace/S*F(S)-trace*(S-trace)/k)==0
    assert s.cancel((6-t)/2+(k-7)/2-(k-1-t)/2)==0
    e=s.symbols('e')
    assert s.cancel((4/k-s.Rational(2,3))*(d-e)-(4/k-s.Rational(2,3))*d-2*(k-6)*e/(3*k))==0
    Path('lower35_controls.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PROVED (lower35.py): F_k(k-7)>=F_6(0)+1/4 for all 3+5 top pairs, k>=8 and infinity; exact trace interpolation.')

if __name__=='__main__':main()
