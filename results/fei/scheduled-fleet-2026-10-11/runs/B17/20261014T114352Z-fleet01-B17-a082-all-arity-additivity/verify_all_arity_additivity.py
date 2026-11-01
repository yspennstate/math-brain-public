#!/usr/bin/env python3
"""Deterministic diagnostics for the all-arity block half-tax transfer.

The proof is Schwonnek additivity plus the source scalar theorem.  These
floating tests are adversarial diagnostics only; they are not the proof.
"""
import json
import math
import numpy as np

SEED = 17082026
rng = np.random.default_rng(SEED)

def entropy(prob):
    p = np.asarray(prob, dtype=float)
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())

def h2(p):
    if p <= 0 or p >= 1:
        return 0.0
    return -p*math.log2(p) - (1-p)*math.log2(1-p)

def delta(p):
    return h2(p) + math.log2(max(p, 1-p))

def rot(p):
    return np.array([[math.sqrt(1-p), math.sqrt(p)],
                     [math.sqrt(p), -math.sqrt(1-p)]], dtype=float)

def kron_all(mats):
    ans = np.array([[1.0]])
    for a in mats:
        ans = np.kron(ans, a)
    return ans

def local_min(p, grid=200001):
    # Real states suffice for the qubit minimum.  Dense diagnostic only.
    t = np.linspace(0.0, math.pi, grid)
    z0, z1 = np.cos(t), np.sin(t)
    u0 = math.sqrt(1-p)*z0 + math.sqrt(p)*z1
    u1 = math.sqrt(p)*z0 - math.sqrt(1-p)*z1
    def hv(x):
        x = np.clip(x*x, 0, 1)
        y = np.zeros_like(x)
        m = (x > 0) & (x < 1)
        y[m] = -x[m]*np.log2(x[m])-(1-x[m])*np.log2(1-x[m])
        return y
    vals = hv(z0) + hv(u0)
    j = int(np.argmin(vals))
    return float(vals[j]), np.array([z0[j], z1[j]])

def main():
    biases_bank = [0.0, 1e-12, 1e-8, 1/64, .08, .125, .25, .49, .5,
                   .51, .75, 1-1e-8, 1.0]
    random_cases = 0
    worst_margin = float('inf')
    worst_case = None
    product_error = 0.0
    local_slack = float('inf')
    for k in range(1, 9):
        trials = 800 if k <= 5 else 250
        for trial in range(trials):
            ps = [biases_bank[(trial + 3*j + k) % len(biases_bank)]
                  if trial < len(biases_bank) else float(rng.random())
                  for j in range(k)]
            U = kron_all([rot(p) for p in ps])
            w = rng.normal(size=1 << k) + 1j*rng.normal(size=1 << k)
            w /= np.linalg.norm(w)
            lhs = entropy(abs(w)**2) + entropy(abs(U@w)**2)
            rhs = sum(h2(p)-.5*delta(p) for p in ps)
            margin = lhs-rhs
            if margin < worst_margin:
                worst_margin = margin
                worst_case = {'k':k, 'biases':ps, 'lhs':lhs, 'rhs':rhs}
            assert margin > -2e-11
            random_cases += 1
    # Product-state saturation of the exact tensor minimum, diagnosed on a
    # smaller bank using independently minimized local states.
    for ps in ([.03,.2,.49], [.125,.25,.5], [1e-8,.08,.4,.5]):
        mins=[]; vecs=[]
        for p in ps:
            m,z=local_min(p, 40001); mins.append(m); vecs.append(z)
            local_slack=min(local_slack,m-(h2(p)-.5*delta(p)))
        w=vecs[0]
        for z in vecs[1:]: w=np.kron(w,z)
        U=kron_all([rot(p) for p in ps])
        lhs=entropy(abs(w)**2)+entropy(abs(U@w)**2)
        product_error=max(product_error,abs(lhs-sum(mins)))
    out={
      'status':'PASS', 'seed':SEED, 'random_complex_states':random_cases,
      'arity_range':[1,8], 'worst_certified_formula_margin_observed':worst_margin,
      'worst_case':worst_case,
      'max_product_additivity_error':product_error,
      'minimum_local_half_tax_slack_on_product_tests':local_slack,
      'note':'diagnostic only; proof uses source scalar theorem and Schwonnek Proposition 1/Corollary 1'
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()

