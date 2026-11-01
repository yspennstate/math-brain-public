from fractions import Fraction as F

L0 = F(61,100)

def qpoly(D,p,lam,u):
    m = 1 + p*(D-1)
    return D*u*u + (lam*(D+1)-D)*u + lam*lam - lam*m

def cert(D,p,L,u):
    c = 1-L
    M = D-(D-1)*L
    b = D*c/M
    J = (D-1)*(b/(b+D*u-c))**2
    tau = (1+L)/(D+L)
    theta = p*tau/(1-p+p*tau)
    H = L*J
    C = L/c-p*H
    delta = 1+(D-1)*theta-(D-1)*C*theta*(1-theta)
    margin = 2*delta/(1+(D-1)*theta+L)**2
    Jold = (D-1)*(b/(D-c+b))**2
    return dict(c=c,b=b,J=J,Jold=Jold,tau=tau,theta=theta,H=H,C=C,delta=delta,margin=margin)

def conditions(D,p0,L,u,target):
    q0 = qpoly(D,p0,L0,u)
    slope = (D+1)*u + 2*L0 - (1+p0*(D-1))
    static = D*(1-L)-(1+L)

    e0 = cert(D,p0,L0,u)
    eL = cert(D,p0,L,u)

    Cprime_lb = 1/(1-L0)**2 - p0*F(D-1,D*D)/(u*u)
    theta_cond = e0["C"]*(1-2*eL["theta"])-1

    t = eL["tau"]
    C0 = L/(1-L)
    H = eL["H"]
    Np = 1-C0 + p0*(C0*(1+t)+t-1+2*H) - 3*H*p0*p0 + H*(1-t)*p0**3
    Nprime = (C0*(1+t)+t-1+2*H) - 6*H*p0 + 3*H*(1-t)*p0*p0

    assert q0 >= 0, ("mean upper bound invalid", D, q0)
    assert slope > 0, ("Q not increasing in lambda", D, slope)
    assert static >= 0, ("static-ratio hypothesis invalid", D, static)
    assert Cprime_lb > 0, ("C monotonicity lower bound invalid", D, Cprime_lb)
    assert theta_cond > 0, ("F not decreasing in theta on rectangle", D, theta_cond)
    assert Np < 0, ("endpoint p derivative not negative", D, Np)
    assert Nprime > 0, ("N not increasing on p interval", D, Nprime)
    assert eL["J"] > eL["Jold"], ("new score does not improve old score", D)
    assert eL["delta"] > 0, ("delta not positive", D, eL["delta"])
    assert eL["margin"] > target, ("margin too small", D, eL["margin"], target)

    return q0,slope,static,Cprime_lb,theta_cond,Np,Nprime,eL

cases = [
    ("A_D12_endpoint", 12, F(1,2), F(1679,2500), F(743,1000), F(1,90000)),
    ("B_D51_breadth", 51, F(2,5), F(2,3), F(18,25), F(1,4600)),
    ("C_D244_breadth", 244, F(19,50), F(2,3), F(713,1000), F(1,51000)),
]

for name,D,p0,L,u,target in cases:
    q0,slope,static,Cp,thc,Np,Npr,e = conditions(D,p0,L,u,target)
    print(name)
    print("  D,p0,L,u =", D,p0,L,u)
    print("  Q(u;lambda0,p0) =", q0, "~", float(q0))
    print("  dQ/dlambda lower =", slope, "~", float(slope))
    print("  static ratio slack =", static, "~", float(static))
    print("  Cprime lower =", Cp, "~", float(Cp))
    print("  theta monotonic slack =", thc, "~", float(thc))
    print("  N(p0) =", Np, "~", float(Np))
    print("  Nprime(p0) =", Npr, "~", float(Npr))
    print("  J_new/J_old =", e["J"]/e["Jold"], "~", float(e["J"]/e["Jold"]))
    print("  delta =", e["delta"], "~", float(e["delta"]))
    print("  derivative margin =", e["margin"], "~", float(e["margin"]))
    print("  claimed simple margin >", target, "=", float(target))

# Immediate sufficient-certificate boundaries for the same rational mean caps.
fails = [
    ("A_next_endpoint", 12, F(1,2), F(67161,100000), F(743,1000)),
    ("B_next_support", 52, F(2,5), F(2,3), F(18,25)),
    ("C_next_support", 245, F(19,50), F(2,3), F(713,1000)),
]
for name,D,p,L,u in fails:
    q0 = qpoly(D,p,L0,u)
    e = cert(D,p,L,u)
    assert q0 >= 0
    assert e["delta"] < 0
    print(name)
    print("  Q mean-cap certificate =", q0, "~", float(q0))
    print("  delta =", e["delta"], "~", float(e["delta"]))

print("ALL_EXACT_CHECKS_PASS")
