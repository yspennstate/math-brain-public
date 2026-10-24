"""Finite numerical stress tests; these are not proofs of an asymptotic theorem."""
import json
from pathlib import Path
import numpy as np

rng = np.random.default_rng(310011)
records = []
for n in (4, 8, 16, 32, 64):
    J = np.diag(np.ones(n - 1), 1).astype(complex)
    C = J.copy()
    C[-1, 0] = 1
    for z in (0.25, 0.5 + 0.2j, 0.7j):
        v = np.array([z**k for k in range(n)])
        residual = (J - z*np.eye(n)) @ v
        expected = np.zeros(n, dtype=complex)
        expected[-1] = -z**n
        sj = np.linalg.svd(J-z*np.eye(n), compute_uv=False)
        sc = np.linalg.svd(C-z*np.eye(n), compute_uv=False)
        b = 2.0
        clip = lambda s: np.clip(np.log(np.maximum(s, np.finfo(float).tiny)), -b*np.log(n), b*np.log(n)).mean()
        diff = abs(clip(sj)-clip(sc))
        bound = 2*b*np.log(n)/n
        row = dict(n=n, z=[complex(z).real, complex(z).imag], residual_error=float(np.linalg.norm(residual-expected)), clipped_difference=float(diff), rank_one_bound=float(bound), cyclic_smin=float(sc[-1]), cyclic_lower_bound=float(1-abs(z)))
        assert row['residual_error'] < 1e-12
        assert diff <= bound+1e-12
        assert sc[-1] >= 1-abs(z)-1e-12
        records.append(row)

# Verify an explicit two-atom extraction in a finite probability law.
from fractions import Fraction as F
law = {0:F(1,4), 1:F(1,8), 4:F(5,8)}
q = 2*min(law[0], law[1])
residual_law = {x:(p-q/2 if x in (0,1) else p)/(1-q) for x,p in law.items()}
reconstructed = {x:(1-q)*residual_law[x] + (q/2 if x in (0,1) else 0) for x in law}
assert reconstructed == law
assert sum(residual_law.values()) == 1 and min(residual_law.values()) >= 0

out = dict(description='Finite checks only; Jordan model is not iid-entry C0031.', jordan=records, exact_mixture=dict(q=str(q), residual={str(x):str(p) for x,p in residual_law.items()}, reconstructed={str(x):str(p) for x,p in reconstructed.items()}))
Path('SECOND_CHECKS.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
print('Passed 15 Jordan/cyclic numerical cases and one exact rational mixture check.')
