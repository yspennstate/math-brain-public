#!/usr/bin/env python3
"""Exact-rational audit of PROOF.md. Standard library only; no sampling."""
import csv
import itertools
import json
import os
import resource
from fractions import Fraction as F
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
# macOS rejects lowering RLIMIT_DATA in this sandbox. The audit holds only a few
# thousand short rational rows; record and verify the actual peak RSS below.
ROOT = Path(__file__).resolve().parent

def affine_integral(a, b, left, right):
    return a * (right * right - left * left) / 2 + b * (right - left)

def cells(h, eps=F(0)):
    """Partition where the exact stop/continue costs and error choices are affine."""
    base = sorted(set((F(0), F(1), *h)))
    result = []
    const_c = 2 + sum((1-v for v in h), F(0))
    for l, u in zip(base, base[1:]):
        count = sum(v < (l+u)/2 for v in h)
        # S=x+1+count; C=-x+const_c; D=2x+b.
        b = 1 + count - const_c
        points = {l, u}
        for level in (-eps, F(0), eps):
            root = (level-b)/2
            if l < root < u:
                points.add(root)
        points = sorted(points)
        result.extend((p,q,count,b,const_c) for p,q in zip(points, points[1:]))
    return result

def value_two(h):
    out = F(0)
    for l,u,count,b,cc in cells(h):
        if 2*((l+u)/2)+b <= 0:
            out += affine_integral(F(1), F(1+count), l,u)
        else:
            out += affine_integral(F(-1), cc, l,u)
    return out

def audit_two(h, eps, mode):
    # Method A integrates the actual chosen S or C, then subtracts the optimum.
    actual = F(0)
    # Method B integrates |D| only on the misclassification intervals.
    residual = F(0)
    for l,u,count,b,cc in cells(h, eps):
        mid = (l+u)/2
        d = 2*mid+b
        err = {'upper': eps, 'lower': -eps,
               'adversarial': eps if d > 0 else -eps,
               'helpful': -eps if d > 0 else eps}[mode]
        stop = d <= err
        optimal_stop = d <= 0
        actual += affine_integral(F(1), F(1+count), l,u) if stop else affine_integral(F(-1), cc, l,u)
        if stop != optimal_stop:
            sign = 1 if d > 0 else -1
            residual += affine_integral(F(2*sign), sign*b,l,u)
    regret = actual-value_two(h)
    assert regret == residual and regret >= 0
    bound = eps**2/(2 if mode in ('adversarial','helpful') else 4)
    assert regret <= bound, (h,eps,mode,regret,bound)
    return regret, bound

histories = [h for k in range(5) for h in itertools.combinations_with_replacement(
    [F(i,4) for i in range(5)], k)]
rows = []
for h in histories:
    for eps in (F(1,16),F(1,8),F(1,4),F(1,2)):
        for mode in ('upper','lower','adversarial','helpful'):
            regret,bound = audit_two(h,eps,mode)
            rows.append([','.join(map(str,h)),str(eps),mode,str(regret),str(bound)])
with (ROOT/'penultimate_audit.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(['history','epsilon','mode','exact_regret','certificate']); w.writerows(rows)

# Third-to-last slope: evaluate W_2 exactly, rather than assuming its monotonicity.
slope_checks=0
for h in histories:
    xs = [F(i,16) for i in range(17)]
    ds = [1+sum(v<x for v in h)+2*x-value_two((*h,x)) for x in xs]
    for i in range(len(xs)-1):
        assert ds[i+1]-ds[i] >= 2*(xs[i+1]-xs[i])
        slope_checks += 1

# Constant by direct stage sum, separately by expanded polynomial.
constants=[]
for n in range(2,31):
    direct=sum((F((r-1)**2*(n-r)**2,2*(2 if r==2 else r-1)) for r in range(2,n+1)), F(0))
    closed=F((n-1)**2*((n-1)**2-1),24)-F((n-2)**2,4)
    assert direct==closed
    constants.append({'n':n,'A_n':str(direct)})
assert constants[3]['A_n']=='31/4'

# Independent closed-form integrations for the sharp n=2 witnesses.
e=F(1,4)
tminus=(1-e)/2; tplus=(1+e)/2
# Antiderivatives of S=1+x and C=2-x.
def s_int(l,u): return (u+u*u/2)-(l+l*l/2)
def c_int(l,u): return (2*u-u*u/2)-(2*l-l*l/2)
base=F(5,4)
one_sided=s_int(F(0),tminus)+c_int(tminus,F(1))-base
two_sided=s_int(F(0),tminus)+c_int(tminus,F(1,2))+s_int(F(1,2),tplus)+c_int(tplus,F(1))-base
assert one_sided==F(1,64)==e*e/4
assert two_sided==F(1,32)==e*e/2

# The pinned-threshold counterexample, checked both by costs and by (17).
delta=F(1,100)
h=(F(1,2),)
optimal=value_two(h)
bad=s_int(F(0),F(1,2))+affine_integral(F(1),F(2),F(1,2),F(1,2)+delta)+affine_integral(F(-1),F(5,2),F(1,2)+delta,F(1))
pinned=bad-optimal
assert pinned==delta/2+delta**2==F(51,10000)

summary={
    'arithmetic':'fractions.Fraction throughout; no floating-point tests',
    'penultimate_histories':len(histories),
    'penultimate_policy_checks':len(rows),
    'third_to_last_slope_checks':slope_checks,
    'stage_sum_vs_closed_form_checks':len(constants),
    'sharp_two_sided_epsilon_1_over_4':str(two_sided),
    'sharp_one_sided_epsilon_1_over_4':str(one_sided),
    'pinned_threshold_regret_delta_1_over_100':str(pinned),
    'n5_rounding_coefficient':'31/4',
    'n5_M100_regret_certificate':str(F(31,4*100**2)),
    'constants':constants,
    'priority':os.getpriority(os.PRIO_PROCESS,0),
    'peak_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    'all_checks_passed':True,
}
assert summary['peak_rss_bytes_macos'] < 1024**3
(ROOT/'audit_results.json').write_text(json.dumps(summary,indent=2)+'\n')
for key,value in summary.items():
    if key!='constants': print(f'{key}: {value}')
