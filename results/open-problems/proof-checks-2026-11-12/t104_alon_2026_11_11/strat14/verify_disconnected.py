"""Symbolic matrix derivation of both disconnected five-vertex formulas.

This supplements STRAT4's coefficient certificate: no finite sample substitutes
for either of the two continuous reductions used in the full theorem.
"""
from sympy.polys.rings import ring
from sympy.polys.domains import QQ

def replay():
    rr,b,v0,v1,v2=ring('b,v0,v1,v2',QQ)
    for size in (3,4):
        vv=[v0,v1,v2,-v0-v1-v2,rr.zero]if size==4 else [v0,v1,-v0-v1,rr.zero,rr.zero]
        U=[1,1,1,1,-4]if size==4 else [2,2,2,-3,-3]
        nu=sum(x*x for x in U);n=sum(x*x for x in vv)
        lam=(2+b)/3
        Qn=[[QQ(U[i]*U[j],nu)*n+vv[i]*vv[j]for j in range(5)]for i in range(5)]
        S=[[lam*QQ(U[i]*U[j],nu)*n+b*vv[i]*vv[j]for j in range(5)]for i in range(5)]
        Pi=[[QQ(5*int(i==j)-1,5)*n-Qn[i][j]for j in range(5)]for i in range(5)]
        tau=sum(S[i][i]for i in range(5))
        num=2*(lam*tau*n*n-sum(S[i][j]**2 for i in range(5)for j in range(5))*n)
        num+=QQ(10,3)*sum(Pi[i][j]*S[i][j]**2 for i in range(5)for j in range(5))
        num+=(1-lam)/3*(2*tau*n*n-QQ(10,3)*sum(Pi[i][i]*S[i][i]for i in range(5))*n)
        num-=2*sum((lam*n/5+S[i][j])*(2*n-Qn[i][i]-Qn[j][j]+2*Qn[i][j])*(S[i][i]+S[j][j]-2*S[i][j])for i in range(5)for j in range(i+1,5))
        q=sum(x**4 for x in vv);third=sum(x**3 for x in vv)
        expected=((20*n**3+(276*q*n-73*n**3)*b+(161*n**3-708*q*n+432*third**2)*b*b)/162 if size==4 else
                  ((10+196*b-314*b*b)*n**3+648*b*b*third**2)/243)
        assert num==expected
        assert all(sum(Qn[i][j]for j in range(5))==0 for i in range(5))
        assert all(sum(Qn[i][k]*Qn[k][j]for k in range(5))==n*Qn[i][j]for i in range(5)for j in range(5))
        print('PROVED (verify_disconnected.py): full symbolic matrix formula for component size',size,flush=True)
    # Exact checks of the 3+2 residual sign proof in STRAT4/RESULT.md.
    from fractions import Fraction as F
    assert 10+196*F(4,7)-314*F(4,7)**2==F(954,49)>0
    assert 143*F(4,7)**2-3*F(4,7)-32==F(636,49)>0
    assert 286*F(4,7)-3>0
    # The isolated-vertex formula is concave: m<=q-1/4, q>=1/4.
    assert 161-708*F(1,4)+432*(F(1,4)-F(1,4))==-16
    print('PROVED (verify_disconnected.py): rational endpoint signs and isolated concavity constants checked.',flush=True)

if __name__=='__main__':replay()
