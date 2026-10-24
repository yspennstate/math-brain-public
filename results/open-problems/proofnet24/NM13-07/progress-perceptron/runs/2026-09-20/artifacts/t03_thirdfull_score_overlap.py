#!/usr/bin/env python3
"""Numerical self-check for NM13-07 T03 third-full score-overlap identities.

This is a numerical sanity check, not an interval certificate.  It evaluates the
closed one-step Gaussian kernel by product Gauss--Hermite quadrature and checks
exact semigroup identities against the independently supplied NM13-03
alpha=12.288 stationary point.
"""
import math
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp

ALPHA = 12.288
P3 = 0.599126773053267
P2 = 0.969080522852930
Q3 = 0.228731793616387
Q2 = 0.638442418504189
C3 = 2.86661591200020
C2 = 13.0870435401505
GAMMA_SQ = 0.0766524281089569
GAMMA_P = 3.26204123769656


def gh(n):
    x, w = hermgauss(n)
    return np.sqrt(2.0) * x, w / np.sqrt(np.pi)


def reconstruct_q_sector(p2, p3, q2, q3):
    c3 = math.sqrt(p3/q3)/(p2-p3) - math.sqrt(q3/p3)/(q2-q3)
    gamma_p = 0.5*(1-q2)/(1-p2)*(p2-p3)/(q2-q3)*math.sqrt(q3/p3)
    c2 = ((p2-p3)/(q2-q3)*math.sqrt(q3/p3))/(1-p2) \
         - ((q2-q3)/(p2-p3)*math.sqrt(p3/q3))/(1-q2)
    return c2, c3, gamma_p


def kernel_moments(p2, p3, c2, c3, gamma_sq, n):
    B = c2/(4.0*gamma_sq)
    m = c3/c2
    U, wu = gh(n)
    V, wv = gh(n)
    logwu = np.log(wu)
    s2 = 1.0-p2
    s = math.sqrt(s2)
    A = 1.0 + 2.0*B*s2
    rtA = math.sqrt(A)
    sd = math.sqrt(p2-p3)
    sp3 = math.sqrt(p3)
    logphi0 = -0.5*math.log(2.0*math.pi)

    Q = M1 = M2 = MB = QM = 0.0
    for v, ov in zip(V, wv):
        x = sd*U + sp3*v - 1.0
        a = x/s
        b = x/(s*rtA)
        logt1 = log_ndtr(-a)
        logt2 = -0.5*math.log(A) - B*x*x/A + log_ndtr(b)
        logf = np.logaddexp(logt1, logt2)
        frac1 = np.exp(logt1-logf)
        frac2 = np.exp(logt2-logf)

        mills_mina = np.exp(logphi0 - 0.5*a*a - log_ndtr(-a))
        ux1 = -mills_mina/s
        mills_b = np.exp(logphi0 - 0.5*b*b - log_ndtr(b))
        ux2 = -2.0*B*x/A + mills_b/(s*rtA)
        ux = frac1*ux1 + frac2*ux2

        uB2 = -s2/A - x*x/(A*A) - x*s*(A**-1.5)*mills_b
        uB = frac2*uB2

        lt = logwu + m*logf
        lz = logsumexp(lt)
        tw = np.exp(lt-lz)
        mean_ux = float(np.dot(tw, ux))
        mean_ux2 = float(np.dot(tw, ux*ux))
        mean_uB = float(np.dot(tw, uB))
        mean_u = float(np.dot(tw, logf))

        Q += ov*lz
        M1 += ov*mean_ux*mean_ux
        M2 += ov*mean_ux2
        MB += ov*(-mean_uB)
        QM += ov*mean_u

    QB = -m*MB
    return dict(B=B, m=m, Q=float(Q), M1=float(M1), M2=float(M2),
                MB=float(MB), QM=float(QM), QB=float(QB))


def q_only(p2, p3, c2, c3, B, n):
    gamma_sq = c2/(4.0*B)
    return kernel_moments(p2, p3, c2, c3, gamma_sq, n)["Q"]


def residuals(n):
    d = kernel_moments(P2, P3, C2, C3, GAMMA_SQ, n)
    B, m = d["B"], d["m"]
    q3_pred = d["M1"]/(4.0*B*B*d["MB"])
    q2_pred = d["M2"]/(4.0*B*B*d["MB"])
    alpha_pred = C2*C2/(4.0*B*B*d["MB"])

    Aq = 2.0*GAMMA_P - C2*(1.0-Q2)
    Dq = Aq - C3*(Q2-Q3)
    Ac3 = (0.5*(P2*Q2-P3*Q3)
           - math.log(Dq/Aq)/(2.0*C3*C3)
           - (Q2-Q3)/(2.0*C3*Dq)
           - Q3*(Q2-Q3)/(2.0*Dq*Dq))
    Ac2 = (0.5*(1.0-P2*Q2)
           - math.log(Aq/(2.0*GAMMA_P))/(2.0*C2*C2)
           - (1.0-Q2)/(2.0*C2*Aq)
           + (1.0-Q2)/(2.0*C3)*(1.0/Aq-1.0/Dq)
           - Q3*(1.0-Q2)/(2.0*Dq*Dq))
    Qc2 = (B*d["QB"] - m*d["QM"])/C2
    rc3 = Ac3 + ALPHA*d["Q"]/(C3*C3) - ALPHA*d["QM"]/(C2*C3)
    rc2 = Ac2 - ALPHA*Qc2/C3

    Qp3 = -0.5*m*m*d["M1"]
    Qp2 = 0.5*m*(m-1.0)*d["M2"]
    rp3 = -0.5*Q3*C3 - ALPHA*Qp3/C3
    rp2 = -0.5*Q2*(C2-C3) - ALPHA*Qp2/C3
    rg = 1.0 + ALPHA*B*d["QB"]/(C3*GAMMA_SQ)
    return d, q3_pred, q2_pred, alpha_pred, (rp3, rp2, rc3, rc2, rg)


def finite_difference_check(n=120):
    d = kernel_moments(P2, P3, C2, C3, GAMMA_SQ, n)
    B, m = d["B"], d["m"]
    theory_p3 = -0.5*m*m*d["M1"]
    theory_p2 = 0.5*m*(m-1.0)*d["M2"]
    theory_B = d["QB"]
    h = 3.0e-5
    fd_p3 = (q_only(P2, P3+h, C2, C3, B, n)-q_only(P2, P3-h, C2, C3, B, n))/(2*h)
    fd_p2 = (q_only(P2+h, P3, C2, C3, B, n)-q_only(P2-h, P3, C2, C3, B, n))/(2*h)
    fd_B = (q_only(P2, P3, C2, C3, B+h, n)-q_only(P2, P3, C2, C3, B-h, n))/(2*h)
    return (theory_p3, fd_p3, theory_p2, fd_p2, theory_B, fd_B)


def main():
    c2r, c3r, gpr = reconstruct_q_sector(P2, P3, Q2, Q3)
    print("Q_SECTOR_RECON", repr(c2r), repr(c3r), repr(gpr))
    print("Q_SECTOR_DIFF", repr(c2r-C2), repr(c3r-C3), repr(gpr-GAMMA_P))
    last = None
    for n in (60, 80, 100, 120, 160):
        d, q3p, q2p, ap, rr = residuals(n)
        last = (d, q3p, q2p, ap, rr)
        print("GH", n,
              "Q", format(d["Q"], ".17g"),
              "q3_pred", format(q3p, ".17g"),
              "q2_pred", format(q2p, ".17g"),
              "alpha_pred", format(ap, ".17g"),
              "max_stat_res", format(max(abs(x) for x in rr), ".3e"))
    d, q3p, q2p, ap, rr = last
    print("GH160_MOMENTS", "M1", repr(d["M1"]), "M2", repr(d["M2"]),
          "MB", repr(d["MB"]), "QM", repr(d["QM"]), "QB", repr(d["QB"]))
    print("GH160_SCORE_RES", repr(q3p-Q3), repr(q2p-Q2), repr(ap-ALPHA))
    print("GH160_SOURCE_STATIONARITY", *(repr(x) for x in rr))
    fd = finite_difference_check(120)
    print("SEMIGROUP_DERIVATIVE_CHECK")
    print("Q_p3 theory/fd/diff", repr(fd[0]), repr(fd[1]), repr(fd[1]-fd[0]))
    print("Q_p2 theory/fd/diff", repr(fd[2]), repr(fd[3]), repr(fd[3]-fd[2]))
    print("Q_B  theory/fd/diff", repr(fd[4]), repr(fd[5]), repr(fd[5]-fd[4]))

    assert abs(c2r-C2) < 2e-12
    assert abs(c3r-C3) < 2e-12
    assert abs(gpr-GAMMA_P) < 2e-12
    assert abs(q3p-Q3) < 2e-10
    assert abs(q2p-Q2) < 2e-10
    assert abs(ap-ALPHA) < 2e-9
    assert max(abs(x) for x in rr) < 5e-10
    assert abs(fd[1]-fd[0]) < 1e-8
    assert abs(fd[3]-fd[2]) < 2e-7
    assert abs(fd[5]-fd[4]) < 2e-11
    print("ALL_NUMERICAL_SANITY_CHECKS_PASS")


if __name__ == "__main__":
    main()
