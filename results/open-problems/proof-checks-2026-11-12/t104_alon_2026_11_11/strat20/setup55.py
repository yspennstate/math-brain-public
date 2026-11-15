"""Exact split 5+5 setup; no new connected endpoint signs asserted."""
import sys,json
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited19'/'inherited18'/'inherited17'))
from matrix_audit import H,direction
from lower_formula import x3
from inherited16.algebra import spanning,quadratic
from audit45 import functional
from memory_guard import install

def main():
    install(850_000_000);k,t,ell=s.symbols('k t ell');u=s.Matrix([4,2,0,-2,-4]);v=s.Matrix([5,1,0,-2,-4])
    pu=u*u.T/u.dot(u);pv=v*v.T/v.dot(v)
    left=H(5)-(H(5)-pu)/10;right=H(5)-(H(5)-pv)/5
    for U,C,D,p,q in ((u,left,right,pu,pv),(v,right,left,pv,pu)):
        K=spanning(U);d=K.cols
        W=s.Matrix(d,d,lambda i,j:s.Rational((i+1)*(j+1)+int(i==j),1000));E=K*W*K.T
        assert E*s.ones(5,1)==s.zeros(5,1) and E*U==s.zeros(5,1)
        expr=functional(s.diag(C+t*E,D),s.diag(p,q),k,ell)
        assert s.cancel(s.Poly(s.expand(expr),t).nth(2)-quadratic(E,U,k))==0
    tau,trace,S,m,h,A=s.symbols('tau trace S m h A');F=lambda a:A+x3(k,m+a/2,h)
    assert s.cancel(F(trace)-(1-trace/S)*F(0)-trace/S*F(S)-trace*(S-trace)/k)==0
    assert s.cancel((8-tau)/2+(k-9)/2-(k-1-tau)/2)==0
    C=s.diag(H(5),H(5));P=s.diag(direction(5),direction(5))
    fixture=functional(C,P,k);lower=functional(C,P,k,k-9)
    assert fixture.subs(k,8)>0 and lower.subs(k,10)>0
    endpoints=['star5','path5','fork5','rank<=2 A5 scale=0','rank<=2 A5 scale=max','rank3 A5 zero-edge scale endpoint (12 support candidates)']
    ledger=dict(label='PROVED (setup55.py): setup only; endpoint signs OPEN outside inherited subcases',first_k=8,nontrivial_lower_first_k=10,lower_trace_cap='k-9',moment_bounds=dict(M0='(8-tau)/2, 0<=tau<=6',h='8/5-d, 0<=B<=d<=3/5'),endpoints=endpoints,ordered_endpoint_types=[[a,b] for a in endpoints for b in endpoints],unordered_endpoint_types=[[a,b] for i,a in enumerate(endpoints) for b in endpoints[i:]],clique_fixture=dict(Tstar=str(fixture),Tstar_N10=str(fixture.subs(k,8)),F_max_lower=str(lower),F_max_lower_N12=str(lower.subs(k,10))),disconnected_reductions='4+5 and smaller proved split classes, including arbitrary lowers',open='connected 5+5 signs, padding, equality and maximal-lower trace endpoints outside inherited S5=0 cases')
    Path('setup55_checks.json').write_text(json.dumps(ledger,indent=2)+'\n')
    print('PROVED (setup55.py): separate five-part concavity with fixed lower trace, k>=8, lower cap k-9; 36 ordered/21 unordered endpoint types. OPEN: their signs beyond inherited special cases.')
if __name__=='__main__':main()
