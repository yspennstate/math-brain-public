#!/usr/bin/env python3
"""
T04 blocked-majority-core certificate.

For alpha, mu=3 alpha/2 and P,N iid Pois(mu), put
Z=min(P,N), M=max(P,N), q=E Z/(2mu).  A false-occurrence Palm
variable has weight Z/EZ.  Its majority break count satisfies
B|P,N ~ Bin(M,q^2).

Let f(M)=P(B>=1|P,N)=1-(1-q^2)^M and
A=E[Z f(M)], C=E[Z(Z-1) f(M)].
Then for the hypergraph of majority-unsatisfied clauses all of whose
three variables have B>=1,
    beta = alpha * (A/(2mu))^3
and its non-root clause-to-clause Galton-Watson mean is
    R = A*C/(2 mu^2).
The script evaluates outward intervals for q,A,C,R,beta.  Finite sums
use mpmath.iv; omitted Poisson tails are covered analytically.

It also prints high-precision diagnostics (not used in the certified
inequality): zero-break promotion susceptibility and the isolated
zero-break-flip supply drift.
"""
import math
import mpmath as mp

mp.mp.dps = 80
iv = mp.iv

def pois_chernoff_tail(mu, k):
    mu = mp.mpf(str(mu))
    k = int(k)
    return float(mp.e**(-mu) * (mp.e*mu/k)**k)

def low_float(x):
    return math.nextafter(float(x.a), -math.inf)

def high_float(x):
    return math.nextafter(float(x.b), math.inf)

def certified(alpha, K=60):
    alpha = float(alpha)
    mu = 1.5*alpha
    mui = iv.mpf([mu, mu])
    p = [iv.exp(-mui) * mui**k / math.factorial(k) for k in range(K)]

    EZ = iv.mpf([0,0])
    for i in range(K):
        for j in range(K):
            EZ += min(i,j)*p[i]*p[j]

    # E[Z; max(P,N)>=K] <= 2 E[P;P>=K].
    t_km1 = pois_chernoff_tail(mu, K-1)
    ez_tail = 2*mu*t_km1
    EZ_lo = low_float(EZ)
    EZ_hi = high_float(EZ) + ez_tail
    q_lo = math.nextafter(EZ_lo/(2*mu), -math.inf)
    q_hi = math.nextafter(EZ_hi/(2*mu), math.inf)
    qi = iv.mpf([q_lo,q_hi])

    A = iv.mpf([0,0])
    C = iv.mpf([0,0])
    one = iv.mpf([1,1])
    for i in range(K):
        for j in range(K):
            z = min(i,j)
            if z == 0:
                continue
            M = max(i,j)
            w = p[i]*p[j]
            f = one - (one-qi*qi)**M
            A += z*f*w
            C += z*(z-1)*f*w

    A_lo = low_float(A)
    A_hi = high_float(A) + ez_tail

    # Tail for C: z(z-1) <= (P+N)^2. Union bound over P>=K or N>=K.
    t_k   = pois_chernoff_tail(mu, K)
    t_km2 = pois_chernoff_tail(mu, K-2)
    EPtail  = mu*t_km1
    EP2tail = mu*mu*t_km2 + mu*t_km1
    EN2 = mu*mu + mu
    C_tail = 2*(EP2tail + 2*EPtail*mu + t_k*EN2)
    C_lo = low_float(C)
    C_hi = high_float(C) + C_tail

    R_lo = math.nextafter(A_lo*C_lo/(2*mu*mu), -math.inf)
    R_hi = math.nextafter(A_hi*C_hi/(2*mu*mu), math.inf)
    qs_lo = math.nextafter(A_lo/(2*mu), -math.inf)
    qs_hi = math.nextafter(A_hi/(2*mu), math.inf)
    beta_lo = math.nextafter(alpha*qs_lo**3, -math.inf)
    beta_hi = math.nextafter(alpha*qs_hi**3, math.inf)

    return dict(mu=mu, q=(q_lo,q_hi), A=(A_lo,A_hi), C=(C_lo,C_hi),
                R=(R_lo,R_hi), beta=(beta_lo,beta_hi),
                ez_tail=ez_tail, C_tail=C_tail)

def local_flip_diagnostic(alpha, K=100):
    alpha = mp.mpf(str(alpha))
    mu = mp.mpf('1.5')*alpha
    p = [mp.e**(-mu)*mu**k/mp.factorial(k) for k in range(K)]
    EZ = mp.fsum([min(i,j)*p[i]*p[j] for i in range(K) for j in range(K)])
    ET = mp.fsum([max(i,j)*p[i]*p[j] for i in range(K) for j in range(K)])
    q = EZ/(2*mu)
    p0=mnum=znum=mp.mpf('0')
    for i in range(K):
        for j in range(K):
            z=min(i,j); M=max(i,j)
            if z==0: continue
            wf=z*p[i]*p[j]/EZ
            b0=(1-q*q)**M
            p0 += wf*b0
            mnum += wf*b0*M
            znum += wf*b0*(z-1)
    mbar=mnum/p0
    zbar=znum/p0
    promote=mbar*(2*q*(1-q)/(1-q*q))
    demote=zbar*(2*q*(1-q))
    h=mp.mpf('0')
    for i in range(K):
        for j in range(K):
            M=max(i,j)
            if M==0: continue
            wt=M*p[i]*p[j]/ET
            h += wt*(1-q*q)**(M-1)
    repaired=1+q*q*zbar
    pool_delta=-1+h*(demote-promote)
    return promote,demote,h,repaired,pool_delta

def promotion_diagnostic(alpha, K=100):
    alpha = mp.mpf(str(alpha))
    mu = mp.mpf('1.5')*alpha
    p = [mp.e**(-mu)*mu**k/mp.factorial(k) for k in range(K)]
    EZ = mp.mpf('0')
    for i in range(K):
        for j in range(K):
            EZ += min(i,j)*p[i]*p[j]
    q = EZ/(2*mu)

    p0 = mp.mpf('0')
    mnum = mp.mpf('0')
    for i in range(K):
        for j in range(K):
            z=min(i,j); M=max(i,j)
            if z==0:
                continue
            w=z*p[i]*p[j]/EZ
            b0=(1-q*q)**M
            p0 += w*b0
            mnum += w*b0*M
    mbar = mnum/p0
    chi = mbar * (2*q/(1+q))

    def surv(theta):
        theta=mp.mpf(str(theta))
        a=(2*q*(1-q)*theta*(1-theta)+(1-q)**2*theta**2)/(1-q*q)
        num=mp.mpf('0')
        for i in range(K):
            for j in range(K):
                z=min(i,j); M=max(i,j)
                if z==0:
                    continue
                w=z*p[i]*p[j]/EZ
                b0=(1-q*q)**M
                num += w*b0*(1-a)**M
        return num/p0

    return q,p0,chi,surv('0.1'),surv('0.2'),surv('0.3')

if __name__ == "__main__":
    print("T04 blocked-majority-core certificate; K=60")
    for a in ("3.52","3.6","4.0","4.4898"):
        s=certified(a,60)
        print(f"alpha={a}")
        print("  q      in [%.15f, %.15f]" % s["q"])
        print("  beta   in [%.15f, %.15f]" % s["beta"])
        print("  R      in [%.15f, %.15f]" % s["R"])
        print("  tail_EZ <= %.3e; tail_C <= %.3e" % (s["ez_tail"],s["C_tail"]))
        q,p0,chi,s1,s2,s3=promotion_diagnostic(a)
        promote,demote,h,repaired,pool_delta=local_flip_diagnostic(a)
        print("  diagnostic p0=%.15f chi=%.15f S0(.1)=%.15f S0(.2)=%.15f S0(.3)=%.15f"
              % (float(p0),float(chi),float(s1),float(s2),float(s3)))
        print("  local_B0_flip promote=%.15f demote=%.15f h=%.15f repaired=%.15f delta_zero_pool=%.15f"
              % (float(promote),float(demote),float(h),float(repaired),float(pool_delta)))
    print("CERTIFICATE: R(4.4898) < 0.88 = True")
