"""PROVED: rational arithmetic for normalized integer frames and their rays."""
from fractions import Fraction as F



def frame_data(U,W,r):
    assert sum(U)==sum(W)==sum(x*y for x,y in zip(U,W))==0
    t,n=sum(x*x for x in U),sum(x*x for x in W)
    assert t>0 and n>0
    A=F(sum(x**4 for x in U),t*t)
    B=F(sum(x**4 for x in W),n*n)
    C=F(sum(x*x*y*y for x,y in zip(U,W)),t*n)
    d,e,f,h=sum(x**3 for x in U),sum(x*x*y for x,y in zip(U,W)),sum(x*y*y for x,y in zip(U,W)),sum(x**3 for x in W)
    d2,e2,f2,h2=F(d*d,t**3),F(e*e,t*t*n),F(f*f,t*n*n),F(h*h,n**3)
    df,eh=F(d*f,t*t*n),F(e*h,t*n*n)
    lu,lw=F(14,9)*(A+C-F(1,5)),F(14,9)*(B+C-F(1,5))
    P=F(58,45)-F(40,9)*A-F(34,9)*C+F(8,3)*d2+F(2,3)*e2+2*df
    Q=F(2,9)*(A+B-F(2,5))-F(8,9)*C+F(10,3)*(e2+f2)+2*df+2*eh
    R=F(58,45)-F(40,9)*B-F(34,9)*C+F(8,3)*h2+F(2,3)*f2+2*eh
    edgeD=[-1-r-20*(F(U[i]*U[j],t)+r*F(W[i]*W[j],n)) for i in range(5) for j in range(i+1,5)]
    D=max([3-r]+edgeD)
    a=2/D
    lam=(2+a*(1+r))/4
    weights=[F(1,10)+a*((1+r)/20+F(U[i]*U[j],t)+r*F(W[i]*W[j],n))
             for i in range(5) for j in range(i+1,5)]
    assert min(weights)>=0
    T5=a*(lu+r*lw+a*(P+r*Q+r*r*R))
    ss=a*(1+r);ff=a*(A+C)+a*r*(B+C)
    KK=a*a*(A+r*r*B+2*r*C-(1+r*r)/5-d2-(1+2*r)*e2-(2*r+r*r)*f2-r*r*h2)
    T=T5-KK/3+(1-lam)*(162+169*ss-260*ff)/720
    return dict(moments=(A,B,C),a=a,lam=lam,weights=weights,T=T,
                L=lu+r*lw,Na=a*(d2+2*e2+f2)+a*r*(e2+2*f2+h2),
                Ja=a*(d2+2*df+f2)+a*r*(e2+2*eh+h2))

