"""Independent rational audits against the original centered matrix definition."""
import sys,json,itertools
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited20'))
from audit45 import functional,H,direction,data,original
from algebra55 import variables,blocks,FIVE,block
from rank3_target55 import target
from inherited20.inherited19.inherited18.inherited17.memory_guard import install

def main():
    install(300_000_000);rr,*_=variables();point=[2,3,1,4,3,2,4,1,0];records=[]
    def ev(p):return s.Rational(p.evaluate(list(zip(rr.gens,point))))
    fixtures=[]
    for left,right in itertools.combinations_with_replacement(FIVE,2):
        cs=[];ps=[]
        for U,R,D,L in blocks(rr,left,right):
            C=s.Matrix([[ev(p)/ev(D)for p in row]for row in L]);u=s.Matrix([ev(p)for p in U]);P=u*u.T/u.dot(u)
            assert C*u==u and sum(u)==0
            cs.append(C);ps.append(P)
        fixtures.append((left+'_'+right,s.diag(*cs),s.diag(*ps)))
    for ep in (0,1):
        D,tr,sq,Q,B,HH,Y,K,L=block(rr,'rank',ep)
        C=s.Matrix([[ev(p)/ev(D)for p in row]for row in L]);U=s.Matrix([[ev(p)for p in row]for row in K])*s.Matrix([1,2,3]);P=U*U.T/U.dot(U)
        fixtures.append(('rank_endpoint_'+str(ep),s.diag(C,H(5)),s.diag(P,direction(5))))
    rank3=[];rt,MM,gs=target()
    for vals in ((1,0,s.Rational(1,10),0,-s.Rational(1,10),0),(2,-s.Rational(2,5),s.Rational(1,5),-s.Rational(3,10),-s.Rational(1,10),s.Rational(1,20))):
        t,x,y,v,w,z=vals;V=s.Matrix([[x,y],[v,w],[1-t-x-v,-z-y-w],[t,0],[-1,z]]);T=5*t;S=V*V.T/T;C=H(5)-S
        check=T*s.eye(2)-V.T*V
        assert check[0,0]>=0 and check[1,1]>=0 and check.det()>=0
        u=(s.ones(5,1).row_join(V)).T.nullspace()[0];P=u*u.T/u.dot(u)
        assert S*u==s.zeros(5,1) and s.trace(S)<=2 and C[3,4]==0
        single=functional(s.diag(direction(2),C),s.diag(direction(2),P),s.Integer(5));assert single>=s.Rational(1,5)
        def evr(p):return s.Rational(p.evaluate(list(zip(rt.gens,vals))))
        mat=s.Matrix([[evr(p)for p in row]for row in MM]);coef=u[:4,0]
        assert (coef.T*mat*coef)[0]==2*T*T*u.dot(u)*(single-s.Rational(1,5))
        rank3.append((C,P));records.append(dict(rank3_single=str(single)))
    fixtures.append(('rank3_pair',s.diag(rank3[0][0],rank3[1][0]),s.diag(rank3[0][1],rank3[1][1])))
    for name,C,P in fixtures:
        assert P*P==P and s.trace(P)==2 and C*P==P and C*s.ones(10,1)==s.zeros(10,1)
        assert all(C[i,j]<=0 for i in range(10)for j in range(i+1,10))
        m,h,b,y=data(C,P);gap=s.diag(H(5),H(5))-C;d=sum(P[i,i]*gap[i,i]for i in range(10))
        assert m==(8-s.trace(gap))/2 and h==s.Rational(8,5)-d and 0<=b<=d<=s.Rational(3,5)
        for extra in (0,2,5):
            val=original(s.diag(C,s.zeros(extra)),s.diag(P,s.zeros(extra)))
            assert val==functional(C,P,s.Integer(8+extra)) and val>0
        D=s.Rational(9,10)*direction(2)
        val=original(s.diag(C,D),s.diag(P,s.zeros(2)))
        assert val==functional(C,P,s.Integer(10),s.trace(D))+2*(s.trace(D)-s.trace(D*D)) and val>0
        if name=='rank3_pair':assert functional(C,P,s.Integer(8))>=s.Rational(11,50)
        records.append(dict(name=name,Tstar_N10=str(functional(C,P,s.Integer(8))),Tstar_lower_N12=str(val)))
    Path('audit55_checks.json').write_text(json.dumps(dict(label='PROVED (audit55.py)',fixtures=records),indent=2)+'\n')
    print('PROVED (audit55.py): nine exact matrix fixtures, padding and feasible lowers; rank-three target independently matches the original functional.')
if __name__=='__main__':main()
