#!/usr/bin/env python3
from itertools import combinations_with_replacement

p=523
n_nonzero=p-1
TARGET=4*p

divisors=[d for d in range(1,n_nonzero+1) if n_nonzero%d==0]
survivors=[]
profiles={}
for d in divisors:
    N=n_nonzero//d
    vals=set()
    # row sum eps0 + d*sum_j eps_j, with N orbit signs; sum=N-2k
    for eps0 in (-1,1):
        for k in range(N+1):
            r=eps0+d*(N-2*k)
            if abs(r)<=45:  # any component in four-square sum 2092 has |r| <= floor(sqrt(2092)) = 45
                vals.add(abs(r))
    vals=sorted(vals)
    ps=[]
    for tup in combinations_with_replacement(vals,4):
        if sum(x*x for x in tup)==TARGET:
            ps.append(tup)
    if ps:
        survivors.append(d)
        profiles[d]=ps

assert survivors==[1,2,3,6,9], survivors
assert profiles[9]==[(1,19,19,37),(17,17,17,35)], profiles[9]
assert profiles[6]==[(5,5,19,41),(7,19,29,29)], profiles[6]
assert len(profiles[3])==22, len(profiles[3])
assert all(d not in survivors for d in [18,29,58,87,174,261,522])
# H58 immediate lower bound in peer report
N=522//58
vals58=sorted({eps0+58*(N-2*k) for eps0 in (-1,1) for k in range(N+1)})
assert vals58==[-523,-521,-407,-405,-291,-289,-175,-173,-59,-57,57,59,173,175,289,291,405,407,521,523]
# after global-negation normalization eps0=+1, peer's listed sequence:
vals58_norm=sorted({1+58*(N-2*k) for k in range(N+1)})
assert vals58_norm==[-521,-405,-289,-173,-57,59,175,291,407,523]
assert min(abs(x) for x in vals58_norm)==57
assert 4*57*57==12996>TARGET

print('audit_object=P15 report section 7 multiplier-invariant GS row-sum gate (peer assigned no formal claim ID)')
print('peer_report=proofnet24/P15-hadamard/runs/2026-09-16/2026-09-16_19-23-52__run-report.md')
print('peer_report_blob=37945b4cb10910f9eaa31af76376fedbe91c26f7')
print('peer_script=proofnet24/P15-hadamard/artifacts/2026-09-16_19-23-52__gs523_multiplier_rowsum_gate.py')
print('peer_script_commit=72e20f8d7ecbf04004bfe9164bcc500c71ec9747')
print('peer_output_commit=cabf21e96f4df721d85864065133ce8b91b0e200')
print('peer_output_blob=c636f823861c9cdfa07ffc977238507eb3c09a5a')
print('divisors_522=' + repr(divisors))
print('surviving_subgroup_orders=' + repr(survivors))
print('d9_profiles=' + repr(profiles[9]))
print('d6_profiles=' + repr(profiles[6]))
print('d3_profile_count=%d' % len(profiles[3]))
print('excluded_orders=' + repr([18,29,58,87,174,261,522]))
print('H58_normalized_row_sums=' + repr(vals58_norm))
print('H58_four_square_lower_bound=%d > %d' % (4*57*57,TARGET))
print('VERDICT=PASS for the exact necessary row-sum gate and stated d=6,d=9 profiles; restricted-route only, not H(2092) nonexistence.')
print('AUDIT_EXACT_PASS')
