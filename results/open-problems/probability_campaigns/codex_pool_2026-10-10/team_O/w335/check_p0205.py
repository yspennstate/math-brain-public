from fractions import Fraction as F
import json
import pathlib
import time

root = pathlib.Path(__file__).resolve().parent
start = time.perf_counter()
cases = 0
checks = 0
for n in (2, 3, 4, 8, 16, 32):
    for alpha in (F(1, 2), F(1)):
        previous_tau = None
        for p in (F(1, 100), F(1, 10), F(1, 2), F(9, 10), F(99, 100)):
            b = 1 - alpha * n / (n - 1)
            a = p / (1 - (1 - p) * b)
            mu = [(1 + (n - 1) * a) / n] + [(1 - a) / n] * (n - 1)
            P = [[1 - alpha if i == j else alpha / (n - 1) for j in range(n)] for i in range(n)]
            M = [[F(0) for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i != j:
                        M[i][j] = P[i][j] * min(F(1), mu[j] / mu[i])
                M[i][i] = 1 - sum(M[i])
            for j in range(n):
                assert mu[j] == (p if j == 0 else 0) + (1 - p) * sum(mu[i] * P[i][j] for i in range(n))
                checks += 1
            for i in range(n):
                assert sum(M[i]) == 1 and min(M[i]) >= 0
                checks += 1
                for j in range(n):
                    assert mu[i] * M[i][j] == mu[j] * M[j][i]
                    checks += 1
            lam = 1 - alpha * n / ((n - 1) * (1 + (n - 1) * a))
            f = [-(n - 1) * mu[1] / mu[0]] + [F(1)] * (n - 1)
            assert sum(mu[i] * f[i] for i in range(n)) == 0
            for i in range(n):
                assert sum(M[i][j] * f[j] for j in range(n)) == lam * f[i]
                checks += 1
            if n >= 3:
                g = [F(0), F(1), F(-1)] + [F(0)] * (n - 3)
                for i in range(n):
                    assert sum(M[i][j] * g[j] for j in range(n)) == b * g[i]
                    checks += 1
            assert lam >= b
            tau = 1 / (1 - lam)
            assert tau == (n - 1) / (alpha * n) * (1 + (n - 1) * a)
            if previous_tau is not None:
                assert tau > previous_tau
                checks += 1
            previous_tau = tau
            if alpha == F(1, 2):
                assert b >= 0 and lam >= 0 and all(M[i][i] >= F(1, 2) for i in range(n))
                checks += 1
            cases += 1

growth = []
for n in (2, 4, 16, 64, 256, 1024):
    alpha, p = F(1, 2), F(1, 2)
    b = 1 - alpha * n / (n - 1)
    a = p / (1 - (1 - p) * b)
    ratio = 1 + (n - 1) * a
    growth.append({'n': n, 'base_tau': float((n - 1) / (alpha * n)), 'metropolis_tau': float((n - 1) / (alpha * n) * ratio), 'ratio': float(ratio), 'ratio_per_n': float(ratio / n)})
receipt = {'command': 'python -X utf8 check_p0205.py', 'cases': cases, 'exact_assertions': checks, 'elapsed_seconds': round(time.perf_counter() - start, 6), 'growth': growth, 'result': 'PASS'}
(root / 'p0205_measurement.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
row = {'row_id': 'w335-P0205-lemma-002', 'problem_id': 'P0205', 'label': 'proof of special family; exact rational checks; pending auditor', 'statement': 'For the complete-Cayley proposal with holding 1-alpha and Geo0(p) target, tau(M)/tau(P)=1+(n-1)*p/(1-(1-p)*(1-alpha*n/(n-1))). For alpha=p=1/2 this ratio/n tends to 2/3; the proposal degree grows.', 'proof_path': str(root / 'P0205_proof.md'), 'measurement_path': str(root / 'p0205_measurement.json'), 'audit_status': 'pending_w347', 'created': '2026-10-10'}
with (root / 'results.jsonl').open('a', encoding='utf-8') as stream:
    stream.write(json.dumps(row) + '\n')
print(json.dumps(receipt, indent=2), flush=True)
