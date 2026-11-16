"""Universal polynomial identities for all six tree pairs and transfer matrices."""
import sys,itertools
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited20'))
from algebra55 import variables,blocks,numerator,FIVE,block,assemble
from transfer55 import construct,controls
from inherited20.inherited19.inherited18.inherited17.memory_guard import install
from sympy.polys.domains import QQ

def main():
    install(850_000_000);rr,*_=variables()
    # Check each local five-by-five contraction before multiplying block denominators.
    # This avoids expanding terms that cancel between the two blocks.
    for kind in FIVE:
        for U,R,D,L in blocks(rr,kind,kind):
            assert all(sum(L[i][j] for j in range(5))==0 for i in range(5))
            assert all(sum(L[i][j]*U[j]for j in range(5))==D*U[i]for i in range(5))
            P=[[U[i]*U[j]for j in range(5)]for i in range(5)]
            directY=-2*sum(L[i][j]*(P[i][i]+P[j][j]-2*P[i][j])*(2*D-L[i][i]-L[j][j]+2*L[i][j])for i in range(5)for j in range(i+1,5))
            localY=-2*sum(L[i][j]*(U[i]-U[j])**2*(2*D-L[i][i]-L[j][j]+2*L[i][j])for i in range(5)for j in range(i+1,5))
            assert directY==localY
            assert sum(L[i][j]*L[j][i]for i in range(5)for j in range(5))==sum(p*p for row in L for p in row)
        print(kind,'local direct matrix contractions PASS',flush=True)
    k,R,D,tr,sq,B,hn,Y,mass=s.symbols('k R D tr sq B hn Y mass')
    from inherited20.inherited19.inherited18.inherited17.lower_formula import x3
    direct=2*(tr/D-sq/D**2)+2*(k+2)*B/(k*R*D**2)-Y/(R*D**2)+x3(k,mass/(2*D),hn/(R*D))
    assert s.cancel(R*D**2*k**2*direct-assemble(k,R,D,tr,sq,B,hn,Y,mass))==0
    # Direct sums give the following ten-by-ten contractions exactly.
    r1,r2,d1,d2,t1,t2,q1,q2,b1,b2,h1,h2,y1,y2=s.symbols('r1 r2 d1 d2 t1 t2 q1 q2 b1 b2 h1 h2 y1 y2')
    r=r1*r2;d=d1*d2
    assert s.cancel((t1*d2+t2*d1)/d-(t1/d1+t2/d2))==0
    assert s.cancel((q1*d2**2+q2*d1**2)/d**2-(q1/d1**2+q2/d2**2))==0
    for a1,a2 in ((b1,b2),(y1,y2)):
        assert s.cancel((r2*d2**2*a1+r1*d1**2*a2)/(r*d**2)-(a1/(r1*d1**2)+a2/(r2*d2**2)))==0
    assert s.cancel((r2*d2*h1+r1*d1*h2)/(r*d)-(h1/(r1*d1)+h2/(r2*d2)))==0
    tr1,sq1,b1,h1,y1,t,d,b5,sq5,y5=s.symbols('tr1 sq1 b1 h1 y1 t d b5 sq5 y5')
    old=2*(4-t-sq5)+s.Rational(14,5)*b5-y5+x3(s.Integer(5),(5-t)/2,s.Rational(13,10)-d)
    new=2*(tr1-sq1+4-t-sq5)+s.Rational(5,2)*(b1+b5)-y1-y5+x3(s.Integer(8),(tr1+4-t)/2,h1+s.Rational(4,5)-d)
    delta=2*(tr1-sq1)+s.Rational(5,2)*b1-y1-s.Rational(3,10)*d+x3(s.Integer(8),(tr1+4-t)/2,h1+s.Rational(4,5)-d)-x3(s.Integer(5),(5-t)/2,s.Rational(13,10)-d)
    assert s.cancel(new-old-delta-s.Rational(3,10)*(d-b5))==0
    for kind,ep,tm in [('rank',0,3),('rank',1,3)]+[(kind,1,2)for kind in FIVE]:
        for dd in (QQ.zero,QQ(3,10)):
            rr,M=construct(kind,ep,dd,tm);D,tr,sq,Q,B,H,Y,K,L=block(rr,kind,ep)
            t=rr.gens[-1]*tm;mass=(tr+(4-t)*D)/2;oldmass=(5-t)/2
            oldx=(oldmass-1)*(36-20*oldmass+14*(QQ(13,10)-dd))/25
            assert all(sum(K[i][a]for i in range(5))==0 for a in range(len(Q)))
            for a in range(len(Q)):
                for b in range(len(Q)):
                    assert Q[a][b]==sum(K[i][a]*K[i][b]for i in range(5))
                    hh=sum(K[i][a]*K[i][b]*L[i][i]for i in range(5))+(QQ(4,5)-dd)*D*Q[a][b]
                    nx=(mass-D)*(108*D*Q[a][b]-32*mass*Q[a][b]+20*hh)/64
                    direct=2*(D*tr-sq)*Q[a][b]+QQ(5,2)*B[a][b]-Y[a][b]+nx-oldx*D*D*Q[a][b]-(QQ(3,10)*dd+QQ(1,100))*D*D*Q[a][b]
                    assert M[a][b]==direct and M[a][b]==M[b][a]
            cs=controls(rr,M);v=rr.gens[-1]
            for a in range(len(M)):
                for b in range(len(M)):
                    assert M[a][b]==cs[0][a][b]*(1-v)**2+2*cs[1][a][b]*v*(1-v)+cs[2][a][b]*v**2
    print('PROVED (symbolic55.py): local direct matrix identities, universal block denominator identity, exact transfer moment matrices and Bernstein reconstructions.')
if __name__=='__main__':main()
