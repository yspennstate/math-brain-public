"""Audit saved data using independent identities and exact integer inequalities."""
import json, math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root/'data'/'enumeration.json').read_text())
graphs = data['graphs']
checks = []

for g,h in [('S3_complete_x_Z','S3_quotient_x_Z'),
            ('D8_complete_x_Z','D8_quotient_x_Z'),
            ('S3_sparse_x_Z','S3_quotient_x_Z')]:
    a,b = graphs[g]['counts'],graphs[h]['counts']
    for n in range(min(len(a),len(b))):
        lower = sum(b[k]*math.comb(k+1,n-k) for k in range(n+1) if 0<=n-k<=k+1)
        assert lower <= a[n], (g,h,n,lower,a[n])
    checks.append(f'Optional-edge coefficient injection: {g} / {h}')

for name,m in [('finite_S3_complete',6),('finite_S3_quotient',3),
               ('finite_D8_complete',8),('finite_D8_quotient',4)]:
    expected = [math.factorial(m-1)//math.factorial(m-1-n) if n<m else 0
                for n in range(len(graphs[name]['counts']))]
    assert graphs[name]['counts'] == expected
    checks.append(f'Finite complete graph falling-factorial identity: {name}')

assert graphs['S3_quotient_x_Z']['counts'] == graphs['square_cylinder_3']['counts']
checks.append('Independent graph definitions agree: K3 square Z = square cylinder of circumference 3')

# Monotone finite-strip paths give mu(K_m square Z) >= lambda_m, where
# sum_{k=0}^{m-1} (m-1)_k / lambda_m^(k+1) = 1.
def strip_lower(m):
    def value(lam):
        total,falling = 0.,1
        for k in range(m):
            if k: falling *= m-k
            total += falling/lam**(k+1)
        return total
    lo,hi = 1.,float(m+1)
    for _ in range(100):
        mid = (lo+hi)/2
        if value(mid)>1: lo=mid
        else: hi=mid
    return (lo+hi)/2

summary = {'checks':checks,'all_passed':True,
           'peak_rss_MiB':data['max_rss_bytes']/1024**2,
           'clique_strip_directed_lower_bounds':{str(m):strip_lower(m) for m in [2,3,4,6,8]},
           'comparisons':data['comparisons']}
(root/'data'/'verification.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
