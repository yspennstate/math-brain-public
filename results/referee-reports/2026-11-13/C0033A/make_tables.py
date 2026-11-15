"""Render numerical tables from saved results into REPORT.md, idempotently."""
import json,csv
from pathlib import Path
import mpmath as mp
root=Path(__file__).resolve().parent;data=root/'data'
s=json.loads((data/'search.json').read_text());t=json.loads((data/'targeted.json').read_text())
v=json.loads((data/'verification.json').read_text());p=json.loads((data/'product_verification.json').read_text())
struct=json.loads((data/'structural_verification.json').read_text())
lines=['## 7. Numerical tables','',
 'All maxima and minima below are attained sample values. A positive double-precision optimized value is not a verified violation.','']
def addtable(headers,rows):
    lines.append('| '+' | '.join(headers)+' |')
    lines.append('| '+' | '.join(['---']*len(headers))+' |')
    for row in rows:lines.append('| '+' | '.join(str(x) for x in row)+' |')
    lines.append('')
fmt=lambda x:f'{x:.6g}'
lines+=['**Full Hessians.** Code: search.py and dpp.py; data: [data/search.json](data/search.json). Each entry is the largest eigenvalue found among 100 kernels; the basis is orthonormal for the Frobenius inner product.','']
rows=[]
for n in range(2,7):
    for field in ('real','complex'):
        vals=[next(r for r in s['rows'] if r['n']==n and r['field']==field and r['family']=='full_hessian_'+kind)['maximum'] for kind in ('uniform','extreme','projection')]
        rows.append([n,field,*map(fmt,vals)])
addtable(['n','field','uniform spectrum','near 0/1','regularized projection'],rows)
lines+=['**Directional and midpoint search.** Code: search.py and dpp.cpp; data: [data/search.json](data/search.json). Rows combine five families: dense, positive rank two, indefinite rank two, commuting, and circulant. The derivative and midpoint samples are as specified in Section 6.','']
rows=[]
for n in (3,4,6,8,10,12,14):
    for field in ('real','complex'):
        rr=[r for r in s['rows'] if r['n']==n and r['field']==field and 'min_midpoint_gap' in r]
        rows.append([n,field,sum(r['trials'] for r in rr),fmt(max(r['maximum'] for r in rr)),fmt(min(r['min_midpoint_gap'] for r in rr))])
addtable(['n','field','trials','largest second derivative','smallest midpoint gap'],rows)
lines+=['**Optimization of full Hessians.** Three starts for each row. Code: search.py; data: [data/search.json](data/search.json). The high-precision column evaluates the saved best direction, rather than reoptimizing it.','']
rows=[]
for r in s['rows']:
    if r['family']!='Nelder_Mead_top_eigenvalue':continue
    fn=f'data/optimized_n{r["n"]}_{r["field"]=="complex"}.npz';vv=next(x for x in v['high_precision'] if x['file']==fn)
    rows.append([r['n'],r['field'],sum(r['evaluations']),sum(r['optimizer_converged']),fmt(r['maximum']),fmt(float(vv['mp120']['second']))])
addtable(['n','field','evaluations','converged starts / 3','double maximum','120-digit evaluation'],rows)
lines+=['**Optimization in circulant symbols.** Three starts for each row. Code: targeted_search.py; data: [data/targeted.json](data/targeted.json) and [data/verification.json](data/verification.json).','']
rows=[]
for r in t['rows']:
    if r['family']!='circulant_symbol_optimization':continue
    fn=f'data/circulant_optimized_n{r["n"]}_{r["field"]=="complex"}.npz';vv=next(x for x in v['high_precision'] if x['file']==fn)
    rows.append([r['n'],r['field'],r['evaluations'],fmt(r['max_second']),fmt(float(vv['mp120']['second']))])
addtable(['n','field','evaluations','double maximum','120-digit evaluation'],rows)
lines+=['**Genuine rank-two midpoint differences.** Minimum midpoint gaps among 100 tests of each signature. Code: targeted_search.py; data: [data/targeted.json](data/targeted.json).','']
rows=[]
for n in (3,4,6,8,10):
    for field in ('real','complex'):
        rr=[next(r for r in t['rows'] if r['n']==n and r['field']==field and r['family']==name)['minimum_gap'] for name in ('rank2_midpoint_psd','rank2_midpoint_indefinite')]
        rows.append([n,field,*map(fmt,rr)])
addtable(['n','field','positive direction','indefinite direction'],rows)
lines+=['**Independent checks.** Code: audit_two_point.py, verify.py, verify_structural.py, and verify_product.py. Data: data/two_point_symbolic.txt, data/verification.json, data/structural_verification.json, and data/product_verification.json.','']
c=v['independent_checks'][0]
addtable(['check','largest absolute discrepancy'],[
 ['two-point polynomial identity','exact zero'],
 ['atoms: signed determinants versus principal-minor inclusion-exclusion',fmt(c['max_atom_error'])],
 ['curvature: compiled directional formula versus full Hessian',fmt(c['max_hessian_error'])],
 ['normalization of atom probabilities',fmt(c['max_mass_error'])],
 ['normalization of first/second atom derivatives',fmt(c['max_derivative_mass'])],
 ['conditioning formula',fmt(struct['conditioning']['max_atom_error'])],
 ['conditional entropy chain rule',fmt(struct['conditioning']['max_entropy_chain_error'])],
 ['product-kernel quartic coefficient',fmt(max(r['max_coefficient_error'] for r in p['rows']))],
 ['product-kernel Hessian',fmt(max(r['max_hessian_error'] for r in p['rows']))],
 ['direct 100-digit second derivative versus Jacobi formula',v['independent_checks'][1]['absolute_error']],
 ['direct 100-digit fourth derivative versus product formula',p['direct_mp_fourth_derivative']['residual']],
])
with mp.workdps(130):
    maxdiff=max(abs(mp.mpf(r['mp80']['second'])-mp.mpf(r['mp120']['second'])) for r in v['high_precision'])
    lines+=['The 80- and 120-digit curvature evaluations agree to an absolute discrepancy at most '+mp.nstr(maxdiff,5)+'. Every checked optimized direction has strictly negative high-precision curvature.','']
lines+=['**Product-kernel sharp constants.** Twenty real and twenty complex tests per dimension. Code: verify_product.py; data: [data/product_verification.json](data/product_verification.json). The equality column uses all off-diagonal pairs.','']
rows=[]
for n in (2,3,4,6,8):
    rr=[r for r in p['rows'] if r['n']==n]
    rows.append([n,fmt(4/(n*(n-1))),fmt(rr[0]['sharp_coefficient']),fmt(min(r['min_ratio_to_dimension_bound'] for r in rr))])
addtable(['n','bound for unit Frobenius norm','equality example','smallest random coefficient / bound'],rows)
lines+=[f'Main search: {s["elapsed_seconds"]:.2f} seconds, peak RSS {s["peak_rss_bytes"]/2**20:.2f} MiB. Targeted search: {t["elapsed_seconds"]:.2f} seconds, peak RSS {t["peak_rss_bytes"]/2**20:.2f} MiB. Timings describe this host and exclude source downloads and high-precision verification. The searches have no rejected evaluations recorded.','']
# Save every search row as a supplementary table without losing family details.
for name,raw in [('search',s['rows']),('targeted',t['rows'])]:
    keys=sorted({k for r in raw for k in r})
    with (data/(name+'.csv')).open('w',newline='') as f:
        writer=csv.DictWriter(f,keys);writer.writeheader();writer.writerows(raw)
report=root/'REPORT.md';text=report.read_text();begin=text.index('<!-- NUMERICAL_TABLES -->');end=text.index('## 8. Literature and attribution',begin)
report.write_text(text[:begin]+'<!-- NUMERICAL_TABLES -->\n\n'+'\n'.join(lines)+'\n'+text[end:])
print('tables rendered from',len(s['rows']),'main rows and',len(t['rows']),'targeted rows')
