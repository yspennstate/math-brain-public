"""Reproducible algebra diagnostics for the one-bit reservoir bridge.

Exact rational checks on the five-site bridge; independent floating-point
physical determinants on an eight-site quadrature tree. Analytic proofs,
not finite numerical tests, establish the family theorem in X092.md.
"""
from pathlib import Path
import json
import math
import numpy as np
import sympy as s

R = s.Rational
checks = {"exact": 0, "numerical": 0}

def check(x, numerical=False):
    assert bool(x)
    checks["numerical" if numerical else "exact"] += 1

def simp(x):
    return s.cancel(s.expand_complex(x))

def phase(n, sites, z):
    v = s.zeros(n, 1)
    for j in sites:
        v[j] = 1
    return s.eye(n) + (z - 1) * v * v.H / len(sites)

def reflection(n, data):
    v = s.zeros(n, 1)
    for j, value in data.items():
        v[j] = value
    return s.eye(n) - 2 * v * v.H / (v.H * v)[0]

def exact_atom(K, mask):
    n = K.rows
    C = s.Matrix.hstack(*[K[:,j] if mask >> j & 1 else
                          (s.eye(n)-K)[:,j] for j in range(n)])
    return simp(C.det(method="domain-ge"))

def exact_law(K):
    return [exact_atom(K, mask) for mask in range(1 << K.rows)]

def to_np(K):
    return np.array(K.evalf(18).tolist(), dtype=complex)

def law(K):
    n = len(K)
    out = []
    for mask in range(1 << n):
        C = np.column_stack([K[:,j] if mask >> j & 1 else
                             np.eye(n)[:,j] - K[:,j] for j in range(n)])
        d = np.linalg.det(C)
        check(abs(d.imag) < 1e-14, True)
        out.append(d.real)
    return np.array(out)

def jets(K, A):
    p, plus, minus = law(K), law(K+A), law(K-A)
    return np.stack([p, (plus-minus)/2, plus+minus-2*p], axis=-1)

def entropy(p):
    p = np.asarray(p)
    p = p[p > 0]
    return -float(np.dot(p, np.log(p)))

def stats(j):
    p, pd, pdd = j.T
    good = p > 1e-25
    check(np.max(np.abs(j[~good])) < 1e-18 if (~good).any() else True, True)
    p, pd, pdd = p[good], pd[good], pdd[good]
    fi = float(np.sum(pd**2/p))
    acc = float(np.dot(pdd, np.log(p)))
    return fi, -fi-acc

t = R(1, 128)
z = simp((1+s.I*t)/(1-s.I*t))
Q0 = phase(4, range(4), z).applyfunc(simp)
bridge5 = phase(5, [3,4], z).applyfunc(simp)
Q05 = s.diag(Q0, 1)
F5 = (bridge5 * Q05).applyfunc(simp)
eta = simp(sum(1-abs(Q0[j,j])**2 for j in range(2)))
rho = simp(1-abs(bridge5[3,3])**2)
check((Q0.H*Q0).applyfunc(simp) == s.eye(4))
check((bridge5.H*bridge5).applyfunc(simp) == s.eye(5))
check(eta == R(3,32770))
check(rho == R(1,16385))
check(eta < R(1,4096))
check(rho < R(1,16384))
check(R(241,384)-R(39,4096) == R(7595,12288))
check(R(7595,12288) > R(3,5))
check(R(1,2)-R(39,4096) == R(2009,4096))
check(sum(R(7,4)**j/s.factorial(j) for j in range(5)) > R(16,3))

M = s.Matrix([[R(2,5),s.I/20],[-s.I/20,R(1,2)]])
Edef = s.Matrix([[R(1,10),R(1,40)],[R(1,40),R(1,8)]])
Eind = s.Matrix([[R(1,10),s.I/30],[-s.I/30,-R(1,10)]])
check(M*Edef != Edef*M)
for N in [M, M+Edef]:
    check((N-s.eye(2)/4).det() > 0)
    check((3*s.eye(2)/4-N).det() > 0)
    check((N-s.eye(2)/4)[0,0] > 0)
    check((3*s.eye(2)/4-N)[0,0] > 0)

Kcore = (Q0*s.diag(R(1,2),R(2,5),M)*Q0.H).applyfunc(simp)
corep = exact_law(Kcore)
B2 = bridge5.extract([3,4],[3,4])
channels2 = [exact_law((B2*s.diag(b,R(1,3))*B2.H).applyfunc(simp)) for b in [0,1]]
K5 = (bridge5*s.diag(Kcore,R(1,3))*bridge5.H).applyfunc(simp)
full5 = exact_law(K5)
for mask in range(32):
    a = mask & 7
    y = mask >> 3
    check(full5[mask] == sum(corep[a | (b<<3)]*channels2[b][y] for b in [0,1]))
check(sum(full5) == 1)
check(sum(corep) == 1)
for c in channels2:
    check(sum(c) == 1)

# An independent eight-site physical test with one strongly mixing quadrature
# pair. Every background rate is strictly fractional.
n = 8
Q08 = s.diag(Q0,s.eye(4))
bridge = phase(n,[3,4],z).applyfunc(simp)
Q1 = reflection(n,{4:1,5:1,6:1})
Q2 = reflection(n,{5:1,6:s.I,7:1})
U = (Q2*Q1*bridge).applyfunc(simp)
F = (U*Q08).applyfunc(simp)
check((U.H*U).applyfunc(simp) == s.eye(n))
check((F.H*F).applyfunc(simp) == s.eye(n))
check(U[3,:] == bridge[3,:])
check(simp(1-abs(U[3,3])**2) == rho)
check(s.re(1*s.conjugate(-s.I)) == 0)
envrates = [R(1,3),R(1,2),R(3,5),R(2,3)]
UB = U.extract([3,4,5,6,7],[3,4,5,6,7])
C = [law(to_np((UB*s.diag(b,*envrates)*UB.H).applyfunc(simp))) for b in [0,1]]
for c in C:
    check(abs(c.sum()-1) < 3e-14, True)
    check(c.min() >= -1e-16, True)
    c[np.abs(c) < 1e-18] = 0  # exact structural zeros with determinant roundoff
K = to_np((U*s.diag(Kcore,*envrates)*U.H).applyfunc(simp))
core_np = to_np(Kcore)
results = {}
for name, E in [("definite",Edef),("indefinite",Eind)]:
    Acore = (Q0*s.diag(s.zeros(2),E)*Q0.H).applyfunc(simp)
    A = to_np((U*s.diag(Acore,s.zeros(4))*U.H).applyfunc(simp))
    jc = jets(core_np,to_np(Acore))
    jf = jets(K,A)
    joint = np.zeros((8,2,32,3))
    for a in range(8):
        for b in range(2):
            joint[a,b,:,:] = C[b][:,None]*jc[a|(b<<3),:][None,:]
    pred = joint.sum(axis=1)
    # Physical final ordering is (untouched three core bits, five output bits).
    pred_flat = np.array([pred[mask&7,mask>>3,:] for mask in range(256)])
    law_error = float(np.max(np.abs(pred_flat-jf)))
    check(law_error < 1e-14, True)
    fi0,hess0 = stats(jc)
    fi,hess = stats(jf)
    q = joint[:,:,:,0]
    qd = joint[:,:,:,1]
    qdd = joint[:,:,:,2]
    post = q / pred[:,None,:,0]
    good = q > 1e-25
    logpost = np.zeros_like(q)
    logpost[good] = np.log(post[good])
    Hpost = -float(np.sum(q*logpost))
    signed_R = float(np.sum(qdd*logpost))
    L = fi0-fi
    identity_error = abs(hess-hess0-L-signed_R)
    check(identity_error < 1e-12, True)
    eps = float(sum(q[a,b,y] for a in range(8) for b in range(2)
                    for y in range(32) if (y&1) != b))
    check(eps <= float(rho)+1e-15, True)
    check(Hpost <= entropy([eps,1-eps])+1e-14, True)
    delta = abs(float(E.det()))
    norm1 = float(np.sum(np.abs(np.linalg.eigvalsh(to_np(E)))))
    Lbound = 64*eps*norm1**2
    Rbound = 32*delta*Hpost
    check(L <= Lbound+1e-13, True)
    check(abs(signed_R) <= Rbound+1e-13, True)
    hc = entropy(jc[:,0])
    hf = entropy(jf[:,0])
    port = sum(jc[a|8,0] for a in range(8))
    affine_H = (1-port)*entropy(C[0])+port*entropy(C[1])
    entropy_error = abs(hf-hc-affine_H+Hpost)
    check(entropy_error < 1e-13, True)
    if name == "definite":
        lower = .6*float(s.trace(E))**2
        check(-hess >= lower, True)
    else:
        lower = fi
        check(-hess >= lower-1e-13, True)
    results[name] = dict(law_jet_error=law_error, curvature_identity_error=identity_error,
                        entropy_identity_error=entropy_error, decoder_error=eps,
                        posterior_bit_entropy=Hpost, fisher_loss=L,
                        signed_log_acceleration_correction=signed_R,
                        negative_curvature=-hess, proved_lower_bound=lower,
                        score_loss_bound=Lbound, log_correction_bound=Rbound)

background = [0,1,4,5,6,7]
global_anchor_leakage = float(sum(1-abs(complex(F[j,j]))**2 for j in background))
prior_entropy = sum(entropy([float(x),1-float(x)]) for x in [R(1,2),R(2,5),*envrates])
check(global_anchor_leakage > 1, True)
check(prior_entropy > 3, True)
report = dict(status="PASS",checks=checks,core_leakage=str(eta),bridge_leakage=str(rho),
              whole_frame_background_anchor_leakage=global_anchor_leakage,
              full_spectral_background_entropy=prior_entropy,results=results)
out = Path(__file__).with_name("certificate.json")
out.write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
