"""Exact rational fixtures checked against the original centered T definition."""
import sys
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited18'/'inherited17'))
from matrix_audit import H,direction,lap,data,original
from lower_formula import x3
from algebra35 import variables,blocks,numerator,TREES

def functional(C,P,k,lowertrace=0):
    m,h,b,y=data(C,P)
    val=s.factor(2*(s.trace(C)-s.trace(C*C))+2*(k+2)*b/k+x3(k,m+s.sympify(lowertrace)/2,h)-y)
    assert not val.has(s.Float)
    return val

def main():
    rr,*_=variables();point=[2,3,1,2,3,4,0]
    def ev(p):return s.Rational(p.evaluate(list(zip(rr.gens,point))))
    fixtures=[]
    for corner in ('balanced','path'):
        for name in TREES:
            cs=[];ps=[]
            for U,R,D,L in blocks(rr,corner,name):
                C=s.Matrix([[ev(p)/ev(D) for p in row] for row in L]);u=s.Matrix([ev(p) for p in U])
                assert C*u==u and sum(u)==0
                assert all(C[i,j]<=0 for i in range(C.rows) for j in range(i+1,C.rows))
                cs.append(C);ps.append(u*u.T/u.dot(u))
            C=s.diag(*cs);P=s.diag(*ps);fixtures.append((corner+'_'+name,C,P))
            for lower in (False,True):
                num,den=numerator(rr,corner,name,lower)
                for kval in ((6,9) if not lower else (8,11)):
                    point[-1]=kval-(8 if lower else 6)
                    val=ev(num)/ev(den)
                    assert val==functional(C,P,s.Integer(kval),s.Integer(kval-7) if lower else 0)
                    assert val>0
                    if not lower:
                        assert val==original(s.diag(C,s.zeros(kval-6)),s.diag(P,s.zeros(kval-6)))
            point[-1]=0
    # Generic feasible low-rank five-part, strictly inside the edge constraints.
    U=s.Matrix([4,2,0,-2,-4]);p5=U*U.T/U.dot(U)
    C5=H(5)-(H(5)-p5)/10
    # An exact rank-three A5 zero-edge chart point; PSD checked by I-C.
    V=s.Matrix([[-s.Rational(1,2),s.Rational(1,3)],[0,-s.Rational(2,3)],[-s.Rational(1,2),-s.Rational(1,6)],[2,0],[-1,s.Rational(1,2)]])
    S=V*V.T/10;Cchart=H(5)-S
    assert S*s.ones(5,1)==s.zeros(5,1) and s.trace(S)<1
    assert all(Cchart[i,j]<=0 for i in range(5) for j in range(i+1,5))
    null=s.Matrix.hstack(s.ones(5,1),V).T.nullspace()
    for cname,Cc,pc in (('complete',H(3),direction(3)),('path',lap(3,[(0,1,s.Rational(1,3)),(1,2,s.Rational(1,3))]),s.Matrix([1,-2,1])*s.Matrix([[1,-2,1]])/6)):
        for fname,cf,pf in [('generic',C5,p5)]+[('rank_three_'+str(i),Cchart,u*u.T/u.dot(u)) for i,u in enumerate(null)]:
            C=s.diag(Cc,cf);P=s.diag(pc,pf);fixtures.append((cname+'_'+fname,C,P))
    for name,C,P in fixtures:
        assert P*P==P and s.trace(P)==2 and C*P==P
        m,h,b,y=data(C,P);gap=s.diag(H(3),H(5))-C
        d=sum(P[i,i]*gap[i,i] for i in range(8))
        assert m==(6-s.trace(gap))/2 and h==s.Rational(22,15)-d
        assert 0<=b<=d<=s.Rational(7,15)
        for extra in (0,2,5):
            assert original(s.diag(C,s.zeros(extra)),s.diag(P,s.zeros(extra)))==functional(C,P,s.Integer(6+extra))
        D=s.Rational(9,10)*direction(2)
        L=s.diag(C,D);Pi=s.diag(P,s.zeros(2))
        assert original(L,Pi)==functional(C,P,s.Integer(8),s.trace(D))+2*(s.trace(D)-s.trace(D*D))
        assert original(L,Pi)>0
    print('PROVED (audit35.py):',len(fixtures),'rational 3+5 fixtures agree with the original centered functional, including padding, low-rank charts and feasible lower edges.')

if __name__=='__main__':main()
