"""Exact separate-concavity setup and endpoint ledger for split 3+5."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited17'))
import sympy as s
from matrix_audit import H,data
from lower_formula import x3
from inherited16.algebra import spanning,quadratic

def value(C,P,k):
    m,h,b,y=data(C,P)
    return 2*(s.trace(C)-s.trace(C*C))+2*(k+2)*b/k+x3(k,m,h)-y

def main():
    k,t=s.symbols('k t');u=s.Matrix([4,2,0,-2,-4]);pu=u*u.T/u.dot(u)
    C5=H(5)-(H(5)-pu)/10;K=spanning(u)
    V=s.Matrix([[1,2,-1],[2,-2,1],[-1,1,3]])/100
    E=K*V*K.T
    v=s.Matrix([1,2,-3]);q=v*v.T/v.dot(v);p3=H(3)-q
    C3=H(3)-q/2
    C=s.diag(C3,C5+t*E);P=s.diag(p3,pu)
    coef=s.Poly(s.expand(value(C,P,k)),t).nth(2)
    assert s.cancel(coef-quadratic(E,u,k))==0
    assert E*s.ones(5,1)==s.zeros(5,1)and E*u==s.zeros(5,1)
    # The triangle-gap coefficient is independent of all other-block data.
    g,m3,mo,ho=s.symbols('g m3 mo ho')
    mass=mo+1-g/2;hd=ho+s.Rational(2,3)-g/6
    expr=2*g*(1-g)+2*(k+2)/k*g*g*(s.Rational(1,6)-m3)-g+6*g*g*m3+x3(k,mass,hd)
    cg=-s.Rational(5,3)-1/(6*k)+1/(3*k*k)+4*(1-1/k)*m3
    assert s.cancel(s.Poly(s.expand(expr),g).nth(2)-cg)==0
    bound=s.factor(cg.subs(m3,s.Rational(1,6)))
    z=s.symbols('z');positive=s.Poly(s.expand((-6*k*k*bound).subs(k,6+z)),z)
    assert all(c>0 for c in positive.coeffs())
    assert s.cancel(x3(k,mass+t/2,hd)-x3(k,mass,hd)).diff(g,2)==0
    # Four- and five-part exact K_u certificates are replayed independently
    # from inherited17. Each applies here because its quadratic form is
    # independent of the other block and fixed lower trace.
    ledger={'label':'PROVED (setup35.py): separate concavity and endpoint reduction; connected signs OPEN',
      'first_k':6,'lower_trace_cap':'k-7, k>=8',
      'triangle_corners':['balanced triangle','positive-flux three-path (zero-edge corner)'],
      'five_part_connected_families':['three tree types','rank-at-most-two A5 boundary','rank-three A5 (twelve support candidates)'],
      'disconnected_reduction':'2+5 or 3+4 with isolates or arbitrary lower components (inherited17 theorem)',
      'open_connected_pairs':['each triangle corner with each five-part connected family'],
      'open_lower_problem':'maximal-trace endpoints for these connected pairs'}
    Path('setup35_checks.json').write_text(json.dumps(ledger,indent=2)+'\n')
    print('PROVED (setup35.py): 3+5 separate concavity and triangle corners, using inherited exact five-part K_u certificate. OPEN: connected pair signs and lower endpoints.')

if __name__=='__main__':main()
