"""Exact clique and equal-flux fixture margins, including maximal lower trace."""
import json
from pathlib import Path
import sympy as s
from audit45 import functional,H,direction,data,original
from algebra45 import variables,blocks,FOUR,FIVE
from inherited19.inherited18.inherited17.memory_guard import install

def main():
    install(850_000_000);rr,*_=variables();k,z=s.symbols('k z');records=[]
    fixtures=[('K4_K5',H(4),direction(4),H(5),direction(5))]
    def ev(p):return s.Rational(p.evaluate([(g,1) for g in rr.gens]))
    for left in FOUR:
        for right in FIVE:
            vals=[]
            for U,R,D,L in blocks(rr,left,right):
                C=s.Matrix([[ev(p)/ev(D) for p in row] for row in L]);u=s.Matrix([ev(p) for p in U]);P=u*u.T/u.dot(u)
                vals.extend((C,P))
            fixtures.append((left+'_'+right,*vals))
    fixtures.append(('two_equal_edges',direction(4),direction(4),direction(5),direction(5)))
    for name,C1,P1,C2,P2 in fixtures:
        C=s.diag(C1,C2);P=s.diag(P1,P2);m,h,b,y=data(C,P)
        val=functional(C,P,k);low=functional(C,P,k,k-8)
        assert original(C,P)==val.subs(k,7)
        if name=='two_equal_edges':assert val==0
        else:
            for expr,base in ((val,7),(low,9)):
                num,den=s.fraction(s.factor(expr.subs(k,base+z)))
                assert all(c>0 for c in s.Poly(num,z).coeffs())
        records.append(dict(name=name,mass=str(m),Tstar=str(val),Tstar_N9=str(val.subs(k,7)),Tstar_infinity=str(s.limit(val,k,s.oo)),T_N9=str(val.subs(k,7)/m**2),T_infinity=str(s.limit(val,k,s.oo)/m**2),F_max_lower=str(low),F_max_lower_N11=str(low.subs(k,9)),F_max_lower_infinity=str(s.limit(low,k,s.oo))))
    C=s.diag(H(4),H(5),direction(2));P=s.diag(direction(4),direction(5),s.zeros(2))
    actual=original(C,P);assert actual==s.sympify(records[0]['F_max_lower_N11']) and actual>0
    records[0]['T_max_lower_N11']=str(actual/(s.trace(C)/2)**2)
    Path('symmetric45_checks.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PROVED (symmetric45.py):',json.dumps(records[0]),flush=True)
    print('PROVED (symmetric45.py): six equal-flux pairs strict with exact margins; two equal edges zero.')
if __name__=='__main__':main()
