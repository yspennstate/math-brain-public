"""Independent original-matrix audits of the new sparse constructions."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited17'))
import sympy as s
from algebra44 import variables,tree,numerator,pair,block
from inherited17.matrix_audit import data,original,H,direction
from inherited17.lower_formula import x3

def functional(C,P,k,lowertrace=0):
    m,h,b,y=data(C,P)
    return s.factor(2*(s.trace(C)-s.trace(C*C))+2*(k+2)*b/k+x3(k,m+lowertrace/2,h)-y)

def main():
    rr,*_=variables();point=(1,2,3,2,1,3,0)
    sub=dict(zip(rr.symbols,point))
    def ev(p):
        val=p.evaluate([(g,int(sub[sym]))for g,sym in zip(rr.gens,rr.symbols)])
        return s.Rational(val)
    cases=[('star','star',1,1),('star','path',1,1),('path','path',1,1),
           ('star','rank',1,0),('star','rank',1,1),('path','rank',1,0),('path','rank',1,1),
           ('rank','rank',0,0),('rank','rank',0,1),('rank','rank',1,1)]
    for left,right,e1,e2 in cases:
        cs=[];ps=[];ws=[]
        for kind,off,ep in ((left,0,e1),(right,3,e2)):
            D,tr,sq,Q,B,hm,ym,K,L=block(rr,kind,off,ep)
            LL=s.Matrix([[ev(p)/ev(D)for p in row]for row in L])
            KK=s.Matrix([[ev(p)for p in row]for row in K]);cc=s.Matrix(range(1,KK.cols+1))
            u=KK*cc;pp=u*u.T/u.dot(u)
            assert LL*u==u and sum(u)==0
            assert all(LL[i,j]<=0 for i in range(4)for j in range(i+1,4))
            cs.append(LL);ps.append(pp);ws.append(cc)
        C=s.diag(*cs);P=s.diag(*ps)
        for lower in (False,True):
            M,den,Q1,Q2=pair(rr,left,right,e1,e2,lower)
            c=s.kronecker_product(*ws)
            for kval in ((6,9)if not lower else(8,11)):
                sub[rr.symbols[-1]]=kval-(8 if lower else 6)
                MM=s.Matrix([[ev(p)for p in row]for row in M])
                norms=(ws[0].T*s.Matrix([[ev(p)for p in row]for row in Q1])*ws[0])[0]
                norms*=(ws[1].T*s.Matrix([[ev(p)for p in row]for row in Q2])*ws[1])[0]
                val=(c.T*MM*c)[0]/(ev(den)*norms)
                difference=s.factor(val-functional(C,P,s.Integer(kval),s.Integer(kval-7)if lower else s.Integer(0)))
                assert difference==0,(left,right,e1,e2,lower,kval,difference)
                if not lower:
                    L=s.diag(C,s.zeros(kval-6));Pi=s.diag(P,s.zeros(kval-6))
                    assert original(L,Pi)==val
                if left!='rank' and right!='rank':
                    num,den2=numerator(rr,tree(rr,left,0),tree(rr,right,3),lower)
                    assert s.factor(ev(num)/ev(den2)-val)==0
    # Full matrices with a feasible rational lower block, independent of
    # the spectral relaxation used at the formal trace endpoint.
    U=s.Matrix([3,1,-1,-3]);V=s.Matrix([3,-1,1,-3])
    pc=U*U.T/U.dot(U);pd=V*V.T/V.dot(V)
    C=s.diag(H(4)-(H(4)-pc)/10,H(4)-(H(4)-pd)/5)
    P=s.diag(pc,pd);D=s.Rational(9,10)*direction(2)
    L=s.diag(C,D);Pi=s.diag(P,s.zeros(2));kk=s.Integer(8)
    assert original(L,Pi)==functional(C,P,kk,s.trace(D))+2*(s.trace(D)-s.trace(D*D))
    assert original(L,Pi)>0
    print('PROVED (audit44.py): sparse scalar and tensor polynomials agree with exact original matrix definitions at rational fixtures; lower-block formula checked independently.')

if __name__=='__main__':main()
