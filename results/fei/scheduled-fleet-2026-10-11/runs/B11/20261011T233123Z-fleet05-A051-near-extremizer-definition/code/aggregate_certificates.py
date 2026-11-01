"""Check census completeness, signed comparisons, and sharp squeeze example."""
from pathlib import Path
from fractions import Fraction as F
import json, ast
import descent_compositions as d

ROOT=Path(__file__).resolve().parent.parent
summary=json.loads((ROOT/'out/full_SUMMARY.json').read_text())
assert summary['completed']==summary['case_count']==1150
assert sum(r['labelled_blocks'] for r in summary['cases'])==470340
assert sum(r['block_orbits'] for r in summary['cases'])==117240
assert all(F(r['phi'][1])<F(227,50) for r in summary['cases'])
def phivec(i):
    case=json.loads((ROOT/f'out/full_case_{i:04d}.json').read_text())
    return next(r['ratio'] for r in case['all_orbits'] if r['mask']==case['minimizing_masks'][0])
def Rvec(i):
    r=summary['cases'][i]
    return d.enc({int(p):F(x)/F(r['I']) for p,x in r['H'].items()})
results=[]
for n in range(6,10):
    ix=[i for i,r in enumerate(summary['cases']) if r['n']==n]
    wp=max(ix,key=lambda i:F(summary['cases'][i]['phi'][0]))
    wr=max(ix,key=lambda i:F(summary['cases'][i]['ratio_H_I'][0]))
    tiesp=[]; tiesr=[]
    for i in ix:
        r=summary['cases'][i]
        if F(r['phi'][1])>=F(summary['cases'][wp]['phi'][0]):
            assert phivec(i)==phivec(wp); tiesp.append(i)
        if F(r['ratio_H_I'][1])>=F(summary['cases'][wr]['ratio_H_I'][0]):
            assert Rvec(i)==Rvec(wr); tiesr.append(i)
        # Certify the universal pointwise bound by a signed linear log expression.
        delta=d.add([(1,{int(p):F(x) for p,x in phivec(i).items()}),(-F(n,n-1),{int(p):F(x) for p,x in Rvec(i).items()})])
        assert not delta or d.interval(delta)[1]<0
    r=summary['cases'][wp]; rr=summary['cases'][wr]
    results.append({'n':n,'formula_count':len(ix),'max_phi_interval':r['phi'],'max_phi_tree':r['tree'],'max_phi_case_indices':tiesp,'max_phi_minimizer_block_sizes':r['minimizing_block_sizes'],'max_R_interval':rr['ratio_H_I'],'max_R_tree':rr['tree'],'max_R_case_indices':tiesr,'max_phi_over_R_in_census_upper_display':max(float(F(summary['cases'][i]['phi_over_H_I'][1])) for i in ix)})

sharp=((((),()),((),())),(((),()),((),())))
isx=next(i for i,r in enumerate(summary['cases']) if ast.literal_eval(r['tree'])==sharp)
assert phivec(isx)==d.enc({int(p):F(x)*F(8,7) for p,x in Rvec(isx).items()})

seed=json.loads((ROOT/'out/SEEDED_FULL_SUMMARY.json').read_text())
assert seed['status']=='PASS'
assert all(F(r['phi'][1])<F(227,50) for r in seed['seed_cases'])
out={'status':'EXACT_CERTIFICATES_PASS','n_groups':results,'census_formula_count':1150,'block_orbits':117240,'labelled_blocks':470340,'all_phi_strictly_below_227_over_50':True,'largest_phi_upper_endpoint':str(max(F(r['phi'][1]) for r in summary['cases'])),'sharp_factor_example':{'case_index':isx,'n':8,'tree':repr(sharp),'phi_over_R_exact':'8/7','minimizer_block_sizes':summary['cases'][isx]['minimizing_block_sizes']},'seeded_cases':seed['seed_cases'],'independent_labelled_replay_cases':len(seed['replay_cases']),'independent_labelled_block_checks':seed['total_labelled_blocks'],'independent_checker_assertions':seed['assertions'],'independent_checker_runtime_seconds':seed['runtime_seconds'],'source_data':'Exact per-function orbit and labelled-block files in out/; every decisive comparison is rational interval or symbolic equality. Decimal displays are noncertifying.'}
d.save('out/AGGREGATE_CERTIFICATES.json',out)
print(json.dumps({'status':out['status'],'formula_count':1150,'block_orbits':117240,'labelled_blocks':470340,'all_below_4_54':True,'sharp_ratio':'8/7','replay_cases':len(seed['replay_cases'])},indent=2))
