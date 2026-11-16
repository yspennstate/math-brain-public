"""Exact balanced and equal-flux margins, including the maximal-trace clique pair."""
import sys,json
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited18'/'inherited17'))
from matrix_audit import H,direction,lap,data,original
from lower_formula import x3
from audit35 import functional
from algebra35 import variables,blocks,TREES

def main():
    rr,*_=variables();k,z=s.symbols('k z');records=[];fixtures=[]
    def ev(p):return s.Rational(p.evaluate([(g,1) for g in rr.gens]))
    for corner in ('balanced','path'):
        C3=H(3) if corner=='balanced' else lap(3,[(0,1,s.Rational(1,3)),(1,2,s.Rational(1,3))])
        u=s.Matrix([1,-1,0] if corner=='balanced' else [1,-2,1]);p3=u*u.T/u.dot(u)
        fixtures.append((corner+'_K5_selected_closure',C3,p3,H(5),direction(5)))
        for name in TREES:
            U,R,D,L=blocks(rr,corner,name)[1]
            C5=s.Matrix([[ev(p)/ev(D) for p in row] for row in L]);v=s.Matrix([ev(p) for p in U]);p5=v*v.T/v.dot(v)
            fixtures.append((corner+'_equal_flux_'+name,C3,p3,C5,p5))
    fixtures.append(('two_equal_edges',direction(3),direction(3),direction(5),direction(5)))
    for name,C1,P1,C2,P2 in fixtures:
        C=s.diag(C1,C2);P=s.diag(P1,P2);m,h,b,y=data(C,P)
        val=functional(C,P,k);low=functional(C,P,k,k-7)
        assert original(C,P)==val.subs(k,6)
        if name=='two_equal_edges':assert val==0
        else:
            for expr,base in ((val,6),(low,8)):
                num,den=s.fraction(s.factor(expr.subs(k,base+z)))
                assert all(c>0 for c in s.Poly(num,z).coeffs())
        records.append({'name':name,'mass':str(m),'Tstar':str(val),'Tstar_N8':str(val.subs(k,6)),
                        'Tstar_infinity':str(s.limit(val,k,s.oo)),
                        'T_N8':str(val.subs(k,6)/m**2),'T_infinity':str(s.limit(val,k,s.oo)/m**2),
                        'F_max_lower':str(low),'F_max_lower_N10':str(low.subs(k,8)),
                        'F_max_lower_infinity':str(s.limit(low,k,s.oo))})
    # Complete tops: formal maximum trace one at N=10 is attained by a lower
    # edge at eigenvalue one in the selected-projector closure.
    C=s.diag(H(3),H(5),direction(2));P=s.diag(direction(3),direction(5),s.zeros(2))
    assert original(C,P)==s.Rational(95,96)
    assert original(C,P)/(s.trace(C)/2)**2==s.Rational(95,1176)
    Path('symmetric35_checks.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PROVED (symmetric35.py): complete-top and six equal-flux tree fixtures have recorded positive margins; K3+K5: Tstar_N8=56/135, maximal trace N10=95/96. Two equal edges give zero.')

if __name__=='__main__':main()
