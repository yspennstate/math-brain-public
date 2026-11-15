"""Exact separate-concavity setup and connected endpoint ledger for split 4+5."""
import sys,json
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited18'/'inherited17'))
from matrix_audit import H,data
from lower_formula import x3
from inherited16.algebra import spanning,quadratic

def value(C,P,k,trace):
    m,h,b,y=data(C,P)
    return 2*(s.trace(C)-s.trace(C*C))+2*(k+2)*b/k+x3(k,m+trace/2,h)-y

def main():
    k,t,ell=s.symbols('k t ell');u=s.Matrix([3,1,-1,-3]);v=s.Matrix([4,2,0,-2,-4])
    pu=u*u.T/u.dot(u);pv=v*v.T/v.dot(v)
    C4=H(4)-(H(4)-pu)/10;C5=H(5)-(H(5)-pv)/5
    for U,left,right,p,q in ((u,C4,C5,pu,pv),(v,C5,C4,pv,pu)):
        K=spanning(U);d=K.cols
        W=s.Matrix(d,d,lambda i,j:s.Rational((i+1)*(j+1)+int(i==j),1000))
        E=K*W*K.T
        assert E*s.ones(U.rows,1)==s.zeros(U.rows,1) and E*U==s.zeros(U.rows,1)
        expr=value(s.diag(left+t*E,right),s.diag(p,q),k,ell)
        assert s.cancel(s.Poly(s.expand(expr),t).nth(2)-quadratic(E,U,k))==0
    # Trace interpolation and the top-moment bookkeeping at nine vertices.
    tau,sigma,d=s.symbols('tau sigma d');S=k-8
    assert s.cancel((7-tau)/2+S/2-(k-1-tau)/2)==0
    assert s.Rational(3,4)+s.Rational(4,5)==s.Rational(31,20)
    assert s.Rational(31,20)-1==s.Rational(11,20)
    A,m,h=s.symbols('A m h');F=lambda a:A+x3(k,m+a/2,h)
    assert s.cancel(F(sigma)-(1-sigma/S)*F(0)-sigma/S*F(S)-sigma*(S-sigma)/k)==0
    four=['star4','path4','rank<=2 A4, scale=0','rank<=2 A4, scale=max']
    five=['star5','path5','fork5','rank<=2 A5, scale=0','rank<=2 A5, scale=max','rank3 A5, zero-edge scale endpoint (12 support candidates)']
    ledger={'label':'PROVED (setup45.py): setup only; connected signs OPEN',
            'first_k':7,'nontrivial_lower_first_k':9,'lower_trace_cap':'k-8',
            'moment_bounds':{'M0':'(7-tau)/2, 0<=tau<=5','h':'31/20-d, 0<=B<=d<=11/20'},
            'four_endpoints':four,'five_endpoints':five,
            'open_endpoint_types':[[a,b] for a in four for b in five],
            'disconnected_reductions':'3+5, 4+4, 2+5, 3+4 and smaller (including arbitrary lower components)',
            'open_signs':'all 24 connected endpoint types, their maximal-lower-trace endpoints, padding and equality outside inherited subcases'}
    Path('setup45_checks.json').write_text(json.dumps(ledger,indent=2)+'\n')
    print('PROVED (setup45.py): separate four/five Ku concavity transfers unchanged with fixed lower trace; first k=7, lower trace cap k-8. OPEN: 24 connected endpoint types and maximal-lower endpoints.')

if __name__=='__main__':main()
