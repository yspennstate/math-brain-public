"""Universal polynomial audits of tree numerators and the transfer comparison."""
import sympy as s
from algebra45 import variables,blocks,numerator,FOUR,FIVE
from inherited19.inherited18.inherited17.memory_guard import install
from inherited19.inherited18.inherited17.lower_formula import x3
from transfer45 import construct,controls

def main():
    install(850_000_000);rr,*_=variables()
    for left in FOUR:
        for right in FIVE:
            (U,R1,D1,L1),(V,R2,D2,L2)=blocks(rr,left,right)
            R=R1*R2;D=D1*D2;n=9
            L=[[rr.zero for j in range(n)] for i in range(n)]
            P=[[rr.zero for j in range(n)] for i in range(n)]
            for W,Rother,Dother,B,off in ((U,R2,D2,L1,0),(V,R1,D1,L2,4)):
                for i in range(len(W)):
                    for j in range(len(W)):
                        L[i+off][j+off]=Dother*B[i][j];P[i+off][j+off]=Rother*W[i]*W[j]
            tr=sum(L[i][i] for i in range(n));sq=sum(p*p for row in L for p in row)
            B=sum(P[i][j]*(int(i==j)*D-L[i][j])**2 for i in range(n) for j in range(n))
            h=sum(P[i][i]*L[i][i] for i in range(n))
            Y=-2*sum(L[i][j]*(P[i][i]+P[j][j]-2*P[i][j])*(2*D-L[i][i]-L[j][j]+2*L[i][j]) for i in range(n) for j in range(i+1,n))
            k=7+rr.gens[-1];mass=tr
            direct=2*R*k*k*(D*tr-sq)+2*k*(k+2)*B-k*k*Y
            direct+=(mass-2*D)/2*(2*(k+1)*(k-2)*R*D-2*k*R*mass+2*(k+2)*h)
            num,den=numerator(rr,left,right)
            assert num==direct and den==R*D*D*k*k
            print(left,right,'direct 9x9 polynomial identity PASS',flush=True)
    # Transfer identity with independent scalar moments. All five-side
    # trace-square and Y terms cancel; replacing b5 by d5 costs >=0.
    tr4,sq4,b4,h4,y4,t,d,b5,sq5,y5=s.symbols('tr4 sq4 b4 h4 y4 t d b5 sq5 y5')
    old=2*(4-t-sq5)+s.Rational(14,5)*b5-y5+x3(s.Integer(5),(5-t)/2,s.Rational(13,10)-d)
    new=2*(tr4-sq4+4-t-sq5)+s.Rational(18,7)*(b4+b5)-y4-y5+x3(s.Integer(7),(tr4+4-t)/2,h4+s.Rational(4,5)-d)
    bound=2*(tr4-sq4)+s.Rational(18,7)*b4-y4-s.Rational(8,35)*d+x3(s.Integer(7),(tr4+4-t)/2,h4+s.Rational(4,5)-d)-x3(s.Integer(5),(5-t)/2,s.Rational(13,10)-d)
    assert s.cancel(new-old-bound-s.Rational(8,35)*(d-b5))==0
    # Reconstruct each transfer matrix from direct four-block moment tensors.
    from inherited19.inherited18.algebra44 import block
    from sympy.polys.domains import QQ
    for kind,ep,tm in [('rank',0,3),('rank',1,3),('star',1,2),('path',1,2)]:
        for dd in (QQ.zero,QQ(3,10)):
            rr,M=construct(kind,ep,5,1,QQ(13,10),dd,tm,QQ(1,100))
            D,tr,sq,Q,B,H,Y,K,L=block(rr,kind,0,ep)
            t=rr.gens[-1]*tm;mass=(tr+(4-t)*D)/2
            oldmass=(5-t)/2
            oldx=(oldmass-1)*(2*6*3-20*oldmass+14*(QQ(13,10)-dd))/25
            for a in range(len(Q)):
                for b in range(len(Q)):
                    assert Q[a][b]==sum(K[i][a]*K[i][b] for i in range(4))
                    hh=sum(K[i][a]*K[i][b]*L[i][i] for i in range(4))+(QQ(4,5)-dd)*D*Q[a][b]
                    nx=(mass-D)*(80*D*Q[a][b]-28*mass*Q[a][b]+18*hh)/49
                    direct=2*(D*tr-sq)*Q[a][b]+QQ(18,7)*B[a][b]-Y[a][b]+nx-oldx*D*D*Q[a][b]-(QQ(8,35)*dd+QQ(1,100))*D*D*Q[a][b]
                    assert M[a][b]==direct
            cs=controls(rr,M);v=rr.gens[-1]
            for a in range(len(M)):
                for b in range(len(M)):
                    assert M[a][b]==cs[0][a][b]*(1-v)**2+2*cs[1][a][b]*v*(1-v)+cs[2][a][b]*v**2
                    assert M[a][b]==M[b][a]
    print('PROVED (symbolic45.py): six universal direct tree identities; transfer cancellation, moment matrices and exact Bernstein reconstruction.')
if __name__=='__main__':main()
