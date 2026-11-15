"""Exact symmetric fixtures and the selected-projector equality center."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited17'))
import sympy as s
from matrix_audit import H,direction,lap,data,original
from lower_formula import x3

def main():
    k,z=s.symbols('k z');records=[]
    fixtures=[]
    square=lap(4,[(0,1,s.Rational(1,4)),(1,2,s.Rational(1,4)),(2,3,s.Rational(1,4)),(3,0,s.Rational(1,4))])
    u=s.Matrix([1,-1,1,-1]);p=u*u.T/4
    fixtures.append(('two_balanced_squares',square,p,square,p))
    fixtures.append(('two_balanced_K4_selected_closure',H(4),direction(4),H(4),direction(4)))
    star=lap(4,[(0,i,s.Rational(1,4))for i in (1,2,3)]);v=s.Matrix([3,-1,-1,-1]);q=v*v.T/12
    fixtures.append(('two_balanced_stars',star,q,star,q))
    fixtures.append(('two_equal_edges',direction(4),direction(4),direction(4),direction(4)))
    for name,C1,P1,C2,P2 in fixtures:
        C=s.diag(C1,C2);P=s.diag(P1,P2)
        assert P*P==P and s.trace(P)==2 and C*P==P
        m,h,b,y=data(C,P)
        val=s.factor(2*(s.trace(C)-s.trace(C*C))+2*(k+2)*b/k+x3(k,m,h)-y)
        base=val.subs(k,6);inf=s.limit(val,k,s.oo)
        assert original(C,P)==base
        if name=='two_equal_edges':assert val==0
        else:
            num,den=s.fraction(s.factor(val.subs(k,6+z)))
            assert all(c>0 for c in s.Poly(num,z).coeffs())
            assert base>0 and inf>0
        records.append(dict(name=name,mass=str(m),Tstar=str(val),Tstar_N8=str(base),Tstar_infinity=str(inf),T_N8=str(base/m**2),T_infinity=str(inf/m**2)))
    Path('symmetric44_checks.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PROVED (symmetric44.py): symmetric square, clique and star pairs have positive exact margins; two equal edges have T=0 identically.')

if __name__=='__main__':main()
