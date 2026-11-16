"""Universal 4+4 lower-trace comparison; no old margin is spent."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited17'))
import sympy as s
from lower_formula import x3

def main():
    k,t,d,z,v,S,trace=s.symbols('k t d z v S trace');c=s.Rational(3,2)
    # S_i=H4-C_i, tau=sum tr S_i, d=sum P_ii(S_i)_ii.
    # 0<=tau<=4, h=3/2-d>=1, 0<=B<=d<=1/2 by Schur products.
    f=(4/k-s.Rational(2,3))*d+x3(k,(k-1-t)/2,c-d)-x3(s.Integer(6),(6-t)/2,c-d)
    records=[]
    for lo,hi in ((0,2),(2,4)):
        for dd in (s.Integer(0),s.Rational(1,2)):
            num=s.expand(s.cancel(144*k*k*(f-s.Rational(3,10))).subs({k:8+z,d:dd,t:lo+(hi-lo)*v}))
            p=s.Poly(num,v);assert p.degree()==2
            controls=[p.nth(0),p.nth(0)+p.nth(1)/2,p.nth(0)+p.nth(1)+p.nth(2)]
            assert s.expand(num-((1-v)**2*controls[0]+2*v*(1-v)*controls[1]+v*v*controls[2]))==0
            for i,control in enumerate(controls):
                q=s.Poly(control,z);assert q.degree()==2 and all(cc>0 for cc in q.all_coeffs())
                records.append(dict(tau_interval=[lo,hi],d=str(dd),control=i,polynomial=str(s.factor(control))))
    assert s.Poly(s.cancel(k*k*f),d).degree()==1
    B,e=s.symbols('B e')
    assert s.cancel((4/k-s.Rational(2,3))*(d-e)-(4/k-s.Rational(2,3))*d-2*(k-6)*e/(3*k))==0
    # Trace interpolation, independently reconstructed at n0=8.
    m,h,A=s.symbols('m h A');F=lambda a:A+x3(k,m+a/2,h)
    assert s.cancel(F(trace)-(1-trace/S)*F(0)-trace/S*F(S)-trace*(S-trace)/k)==0
    assert s.cancel((6-t)/2+(k-7)/2-(k-1-t)/2)==0
    Path('lower44_controls.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PROVED (lower44.py): F_k(k-7)>=F_6(0)+3/10 for all 4+4 top pairs, k>=8 and infinity; exact lower-trace interpolation.')

if __name__=='__main__':main()
