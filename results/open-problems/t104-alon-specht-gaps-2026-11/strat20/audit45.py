"""Independent exact rational audits against the original centered functional."""
import sys,json
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited19'/'inherited18'/'inherited17'))
from matrix_audit import H,direction,data,original
from lower_formula import x3
from algebra45 import variables,blocks,numerator,FOUR,FIVE
from inherited16.split34_algebra import tree_data
from memory_guard import install

def functional(C,P,k,lowertrace=0):
    m,h,b,y=data(C,P)
    value=s.factor(2*(s.trace(C)-s.trace(C*C))+2*(k+2)*b/k+x3(k,m+s.sympify(lowertrace)/2,h)-y)
    assert not value.has(s.Float)
    return value

def main():
    install(850_000_000);rr,*_=variables();point=[2,3,1,2,3,4,1,0]
    def ev(p):return s.Rational(p.evaluate(list(zip(rr.gens,point))))
    fixtures=[]
    for left in FOUR:
        for right in FIVE:
            cs=[];ps=[]
            for U,R,D,L in blocks(rr,left,right):
                C=s.Matrix([[ev(p)/ev(D) for p in row] for row in L]);u=s.Matrix([ev(p) for p in U])
                assert C*u==u and sum(u)==0
                assert all(C[i,j]<=0 for i in range(C.rows) for j in range(i+1,C.rows))
                cs.append(C);ps.append(u*u.T/u.dot(u))
            C=s.diag(*cs);P=s.diag(*ps);fixtures.append((left+'_'+right,C,P))
            num,den=numerator(rr,left,right)
            for kval in (7,10):
                point[-1]=kval-7
                assert ev(num)/ev(den)==functional(C,P,s.Integer(kval))
                assert ev(num)>0
            point[-1]=0
    for n in (4,5):
        u=s.Matrix([3,1,-1,-3] if n==4 else [4,2,0,-2,-4]);q=u*u.T/u.dot(u)
        cn=H(n)-(H(n)-q)/10
        cm=H(9-n);pm=direction(9-n)
        fixtures.append(('generic_'+str(n),s.diag(cn,cm),s.diag(q,pm)))
    for name,C,P in fixtures:
        assert P*P==P and s.trace(P)==2 and C*P==P
        m,h,b,y=data(C,P);gap=s.diag(H(4),H(5))-C
        # generic5 is listed with blocks reversed.
        if name=='generic_5':gap=s.diag(H(5),H(4))-C
        d=sum(P[i,i]*gap[i,i] for i in range(9))
        assert m==(7-s.trace(gap))/2 and h==s.Rational(31,20)-d
        assert 0<=b<=d<=s.Rational(11,20)
        for extra in (0,2,5):
            assert original(s.diag(C,s.zeros(extra)),s.diag(P,s.zeros(extra)))==functional(C,P,s.Integer(7+extra))
        D=s.Rational(9,10)*direction(2)
        assert original(s.diag(C,D),s.diag(P,s.zeros(2)))==functional(C,P,s.Integer(9),s.trace(D))+2*(s.trace(D)-s.trace(D*D))
        assert original(s.diag(C,D),s.diag(P,s.zeros(2)))>0
    print('PROVED (audit45.py):',len(fixtures),'exact original-definition audits, padding and feasible lower edges.')
if __name__=='__main__':main()
