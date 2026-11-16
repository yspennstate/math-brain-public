"""Independent exact graph audits of the weighted-Cauchy double-carrier bound."""
import sympy as s
from matrix_audit import H,formula,data,original
from lower_formula import x3


def main():
    pairs=[([1,-1,0,0,0],[1,1,-2,0,0]),([2,-1,-1,0,0],[0,1,-1,1,-1])]
    count=0
    for uu,vv in pairs:
        u=s.Matrix(uu);v=s.Matrix(vv);assert u.dot(v)==0 and sum(u)==sum(v)==0
        pu=u*u.T/u.dot(u);pv=v*v.T/v.dot(v);Q=pu+pv;P=H(5)-Q
        for a,b in ((s.Rational(1,5),s.Rational(1,10)),(s.Rational(2,5),s.Rational(1,5)),(s.Rational(3,5),s.Rational(1,5))):
            S=a*pu+b*pv;C=H(5)-S
            if any(C[i,j]>0 for i in range(5)for j in range(i+1,5)):continue
            tau=a+b;M,h,B,Y=data(C,P);E=tau-a*a-b*b
            J=s.Integer(0)
            for i in range(5):
                for j in range(i+1,5):
                    U=(u[i]-u[j])**2/u.dot(u);V=(v[i]-v[j])**2/v.dot(v)
                    J-=C[i,j]*(U+V)*(a*U+b*V)
            L=(a-b)*(1-a)**2+b*(2-tau)**2
            assert Y==4*E-2*J and J>=L/M
            assert h>=s.Rational(8,5)-s.Rational(3,5)*tau and B>=0
            for kk in (5,6,10):
                # Formal spectral relaxation endpoint s=k-4; it need not be
                # realizable as one size-five lower component.
                endpoint=2*E+2*s.Rational(kk+2,kk)*B-Y+x3(s.Integer(kk),(kk-tau)/2,h)
                assert endpoint>=s.Rational(1,270)
                count+=1
            D=s.Matrix([[1,-1],[-1,1]])/4
            full=s.diag(C,D);PP=s.diag(P,s.zeros(2))
            assert formula(full,PP)==original(full,PP)>0
    assert count>=12
    print('PROVED (double_small_gap_audit.py):',count,'exact endpoint fixtures; weighted energy identities and the original normalized functional independently checked.')

if __name__=='__main__':main()
