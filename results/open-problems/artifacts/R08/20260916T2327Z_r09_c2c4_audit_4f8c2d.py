#!/usr/bin/env python3
import sympy as sp

p,t,u=sp.symbols("p t u")
print("R08 independent exact audit of R09 20260916T2232Z C2*C4 recovery")

F4=(1-p)**2*(1+2*p*t+3*p**2*t**2)+p**3*(4-3*p)*t**3
assert sp.expand(F4.subs(t,1)-1)==0
mu4=sp.factor(sp.diff(F4,t).subs(t,1))
assert sp.expand(mu4-p*(2+2*p+2*p**2-3*p**3))==0
print("F4 probabilities / mean: PASS")

H=sp.expand(p*mu4-1)
assert H == -3*p**5+2*p**4+2*p**3+2*p**2-1
lo=sp.Rational(11151,20000); hi=sp.Rational(13939,25000)
assert H.subs(p,lo)<0<H.subs(p,hi)
crit_der=sp.expand(sp.diff(p*mu4,p))
print("critical polynomial bracket: PASS")

elim=sp.factor(F4.subs(t,u)-(u-1+p)/p)
Q=p**4*(3*p-4)*u**2+p**3*(2*p-3)*u+(p**3-2*p**2+1)
assert sp.factor(elim + (u-1)*Q/p)==0
assert sp.factor(Q.subs(u,1)+H)==0
assert sp.factor(p**3-2*p**2+1-(p-1)*(p**2-p-1))==0
print("fixed-point elimination / branch-sign identities: PASS")

D=-8*p**4+28*p**3-23*p**2-12*p+16
ustar=-(2*p**2-3*p+sp.sqrt(D))/(2*p**2*(3*p-4))
assert sp.simplify(Q.subs(u,ustar))==0
vstar=(ustar-1+p)/p
theta=sp.simplify(1-ustar*vstar)

A=54*p**8-477*p**7+1674*p**6-3288*p**5+3841*p**4-1338*p**3-3360*p**2+4800*p-1920
B=1728*p**13-25632*p**12+150606*p**11-437346*p**10+546471*p**9+294186*p**8-1911180*p**7+2300491*p**6-370272*p**5-1577694*p**4+1281040*p**3-480*p**2-374784*p+122880
rhs=(D**2*A+p*B*sp.sqrt(D))/(p**7*(3*p-4)**4*D**2)
assert sp.simplify(sp.diff(theta,p,2)-rhs)==0
print("theta second derivative formula: PASS")

def bernstein_coeffs(poly, var):
    poly=sp.Poly(sp.expand(poly),var)
    n=poly.degree()
    a=[poly.nth(j) for j in range(n+1)]
    out=[]
    for k in range(n+1):
        s=sp.Rational(0)
        for j in range(k+1):
            s += a[j]*sp.binomial(k,j)/sp.binomial(n,j)
        out.append(sp.factor(s))
    recon=sum(out[k]*sp.binomial(n,k)*var**k*(1-var)**(n-k) for k in range(n+1))
    assert sp.expand(recon-poly.as_expr())==0
    return out

for name, poly in [("D",D),("-A",-A),("B",B)]:
    bc=bernstein_coeffs(poly,p)
    assert all(c>0 for c in bc)
    print(name,"Bernstein coefficients positive:",len(bc),"PASS")

T=13824*p**23-315648*p**22+3123072*p**21-17394720*p**20+58539929*p**19-113818081*p**18+84186710*p**17+136515571*p**16-365453213*p**15+150787765*p**14+418270231*p**13-397180184*p**12-446325581*p**11+674284977*p**10+421102215*p**9-1098358635*p**8+153376275*p**7+846351135*p**6-511305216*p**5-214036224*p**4+280304640*p**3-29491200*p**2-47923200*p+14745600
bcT=bernstein_coeffs(T,p)
assert all(c>0 for c in bcT)
assert sp.expand(D**3*A**2-p**2*B**2+4*(p-1)*(3*p-4)**4*T)==0
print("T Bernstein positivity and squared sign identity: PASS")

assert sp.factor(crit_der - p*(4+6*p+8*p**2-15*p**3)) == 0
bcM=bernstein_coeffs(4+6*p+8*p**2-15*p**3,p)
assert all(c>0 for c in bcM)
print("critical mean product strictly increasing on (0,1): PASS")

print("curvature sign deduction theta''<0 on (pc,1): PASS")
print("R08-AUDIT-R09-TANG-Q411-C2C4-05 = PASS")
print("ALL_EXACT_CHECKS_PASS")
