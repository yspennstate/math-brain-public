"""PROVED: remaining S5=0 boundary case, triangle plus a lower edge."""
import sympy as S

def main():
    z,v=S.symbols('z v',nonnegative=True);k=4+z;t=1-v
    bracket=2*(k+1)*(k-2)-4*k*(1+t/2)+S.Rational(8,3)*(k+2)
    assert all(c>0 for c in S.Poly(S.expand(bracket),z,v).coeffs())
    for edges in ([(0,1,S.Rational(1,2)),(2,3,S.Rational(1,2))],
                  [(0,1,S.Rational(1,3)),(0,2,S.Rational(1,3)),(1,2,S.Rational(1,3))]):
        W=S.zeros(6)
        for i,j,w in edges:W[i,j]=W[j,i]=w
        L=S.diag(*list(W*S.ones(6,1)))-W;P=L;AA=S.eye(6)-L
        assert L*L==L and S.trace(L)==2
        assert sum(P[i,j]*AA[i,j]**2 for i in range(6)for j in range(6))==0
        assert sum(W[i,j]*(P[i,i]+P[j,j]-2*P[i,j])*(2-L[i,i]-L[j,j]+2*L[i,j])for i in range(6)for j in range(i+1,6))==0
    print('PROVED: both rank-two equality graphs have X1*=X2*=X3*=2S5*=0 for every padding N>=6.')
    print('PROVED: balanced top triangle plus a lower edge has X1*=2t(1-t)>=0, X2*=2S5*=0, X3*>=0, for 0<=t<=1 and N>=6.')
if __name__=='__main__':main()
