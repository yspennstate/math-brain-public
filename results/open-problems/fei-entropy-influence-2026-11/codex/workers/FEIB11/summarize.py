"""Build the numerical tables from receipts; reject any independent-census disagreement."""
import csv,json,math,hashlib
from pathlib import Path
from collections import defaultdict
def read(p):return json.loads(Path(p).read_text())
def fmt(x):return '0' if x==0 else f'{x:.10g}'
def table(headers,rows):return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(map(str,row))+' |' for row in rows])
ds=[read(f'census_n{n}_'+('npn' if n==5 else 'all')+'.json') for n in range(1,6)]
samples=[read(f'census_n{n}_sample.json') for n in [6,7]]
c=read('independent_census.json');d5=ds[-1];qkeys=list(d5['best_over_I'])
diff=0.
for row in c['maxima']:
    q=str(float(row['q']));a=d5['best_over_I'][q];b=d5['best_balanced_over_I_minus_1'][q]
    assert row['tt_hex']==a['tt_hex'] and row['balanced_tt_hex']==b['tt_hex']
    diff=max(diff,abs(row['ratio']-a['ratio']),abs(row['balanced_ratio']-b['ratio']))
assert diff<1e-11
constants=dict(singleton_t_one_third=2*(math.log(3)+1/(3*math.e))/math.log(2),singleton_upper_constant=4,
 quadratic_linear_coefficient=10+2/math.log(2),quadratic_linear_rounded_upper=13,
 address_WC_constant_lower_bound=2*math.log2(8/3),bent_WC_ratio=2*math.log2(4/3),tribes_WC_limit=math.log2(8/3)/math.log(2))
Path('proof_constants.json').write_text(json.dumps(constants,indent=2))
audit=read('audit.json');assert all(x['max_abs_error']==0 for x in audit['errors'].values())
out=['# Renyi containment results','',
 'All numerical tables below are CHECKED within the stated corpus. They are not universal bounds. All logarithmic costs and entropies are in bits; ratios have units of bits per unit total influence. Truth-table bit x is one exactly when f(x)=-1. Input and output negations and coordinate permutations preserve the statistics, so an NPN census suffices. A quoted witness need not be the unique extremizer.','',
 'PROVED: the raw quadratic target fails near constants. The valid general bounds obtained are L_1<=16I^2+13I and L_1=O(I log(2+I)); the latter follows from the read KKLMS theorem. Linear WC holds for monotone/unate, symmetric, read-once and fixed-real-degree classes. The general linear exponent is OPEN. See PROOFS.md and LITERATURE.md.','',
 '## Complete small-function census','',
 'CHECKED: compute.py enumerated every truth table through four variables. npn5.c independently generated 616,126 five-variable NPN classes, covering all 2^31 truth tables after output complements are identified. Its largest allocation is exactly 268,435,456 bytes. npn_generation.txt is the coverage receipt. verify_census.c independently recomputed every q maximum on every five-variable representative.','']
rows=[]
for d in ds:
    a=d['best_over_I']['1.0']
    rows.append([d['n'],d['count'],fmt(a['ratio']),'0x'+a['tt_hex'],fmt(a['I']),fmt(a['H_bits']),fmt(a['A_bits']),fmt(a['WC'])])
out+=[table(['n','tables / classes','max L_1/I','witness hex','I','H','A','WC'],rows),'',
 'For n=1 every nonconstant function is a dictator and the maximum is zero. Constants have I=0 and are omitted from ratios. The balanced denominator I-1 excludes dictators. At n=1 its domain is empty; at n=2 parity gives zero.','']
rows=[]
for d in ds:
    a=d['best_balanced_over_I_minus_1']['1.0']
    if 'tt_hex' not in a:rows.append([d['n'],'empty domain','—','—','—','—','—'])
    else:rows.append([d['n'],fmt(a['ratio']),'0x'+a['tt_hex'],fmt(a['I']),fmt(a['H_bits']),fmt(a['A_bits']),fmt(a['WC'])])
out+=[table(['n','max balanced L_1/(I-1)','witness hex','I','H','A','WC'],rows),'',
 'The n=4 maximum L_1/I is attained by width-two tribes with two tribes, up to NPN equivalence (witness 0x0357). The n=5 maximum is balanced, at 0x018bf5cd. The balanced normalized maximum at n=4 and n=5 is the H=3, I=1.5, A=2 function. A balanced (I-1) denominator is a descriptive statistic here; the O\u2019Donnell\u2013Tan entropy amplification theorem has not been transferred to WC.','',
 'CHECKED: H/I and A/I at the very same WC-maximizing functions, together with their independent maxima, are as follows. This prevents confusing a maximum of one functional with another.','']
rows=[]
for d in ds[1:]:
    a=d['best_over_I']['1.0'];comp=d['comparisons']
    rows.append([d['n'],fmt(a['ratio']),fmt(a['H_bits']/a['I']),fmt(a['A_bits']/a['I']),fmt(comp['H/I']['ratio']),fmt(comp['A/I']['ratio'])])
out+=[table(['n','max L_1/I','H/I at WC max','A/I at WC max','independent max H/I','independent max A/I'],rows),'',
 '## Large random samples','',
 'CHECKED: 200,000 draws per dimension, with seed 20261110+n. In each corpus 100,000 draws are independent unbiased truth tables and 100,000 are uniform among balanced truth tables. Draw counts are not claims of unique-function counts. Each maximum has a complete hexadecimal witness in its JSON receipt. These are sample maxima, not suprema over all functions at those dimensions.','']
rows=[]
for d in samples:
    a=d['best_over_I']['1.0'];b=d['best_balanced_over_I_minus_1']['1.0']
    rows.append([d['n'],fmt(a['ratio']),'0x'+a['tt_hex'],fmt(a['H_bits']/a['I']),fmt(a['A_bits']/a['I']),fmt(b['ratio']),'0x'+b['tt_hex']])
out+=[table(['n','sample max L_1/I','witness hex','same H/I','same A/I','sample max balanced L_1/(I-1)','balanced witness hex'],rows),'',
 'Receipts: census_n6_sample.json and census_n7_sample.json. The extra unbiased arm can also produce balanced tables; the total balanced counts are '+', '.join(f"n={d['n']}: {d['balanced_non_dictator_count']}" for d in samples)+'.','',
 '## Structured families','',
 'CHECKED: families.json contains explicit truth tables through n=18, including every requested family. There are 200 random read-once AND/OR/XOR formulas (50 each at n=6,7,10,14), and 40 further random uniform functions (10 each at those dimensions). analytic_families.json evaluates the PROVED compressed formulas at much larger dimensions with 180 decimal digits of working precision; it constructs no truth tables at those dimensions.','']
family=read('families.json');analytic=read('analytic_families.json');selected=[]
for row in family:
    name=row['name'];n=row['n']
    if (name=='AND' and n in [5,18]) or (name=='majority' and n==17) or (name=='tribes' and row.get('width')==3 and row.get('tribes')==5) or (name=='address_MUX' and row.get('address_bits')==3) or (name=='bent_quadratic_pairs' and n==18) or name.startswith('PM_'):selected.append(row)
for row in analytic:
    if (row['name']=='tribes' and row.get('width') in [8,128]) or (row['name']=='address_MUX' and row.get('address_bits')==128) or (row['name']=='majority' and row['n']==255):selected.append(row)
rows=[]
for r in selected:
    detail=''
    if 'width' in r:detail=f" w={r['width']}, t={r['tribes']}"
    if 'address_bits' in r:detail=f" k={r['address_bits']}"
    L=r['Lq_bits']['1.0'];I=r['I']
    rows.append([r['name']+detail,r['n'],fmt(I),fmt(L/I),fmt(r['H_bits']/I),fmt(r['A_bits']/I)])
out+=[table(['family','n','I','L_1/I','H/I','A/I'],rows),'',
 'PM_K33 is the nine-edge perfect-matching property. PM_K33_plus_9_coins is the balanced record construction: a coin acts on the two core sets consisting of a cross and that cross with its central edge removed. CHECKED: its H/(I-1) is '+fmt(next(r for r in family if r['name']=='PM_K33_plus_9_coins')['H_bits']/(next(r for r in family if r['name']=='PM_K33_plus_9_coins')['I']-1))+'. Both tables are saved in families.json; the 18-variable table is too long to print here.','',
 'CHECKED: maxima among the sampled read-once and additional random families are below. Full witnesses are copied to family_witnesses.json.','']
groups=defaultdict(list)
for r in family:
    if r['name'] in ['random_read_once_AND_OR_XOR','random_uniform']:groups[(r['name'],r['n'])].append(r)
fw=[];rows=[]
for (name,n),rs in groups.items():
    r=max(rs,key=lambda x:x['L_over_I'] if x['L_over_I'] is not None else -1);fw.append(r)
    rows.append([name,n,len(rs),fmt(r['L_over_I']),fmt(r['H_bits']/r['I']),fmt(r['A_bits']/r['I']),r['rep']])
Path('family_witnesses.json').write_text(json.dumps(fw,indent=2))
out+=[table(['sampled family','n','draws','max L_1/I','same H/I','same A/I','rep id'],rows),'',
 'PROVED: address functions force a universal WC constant at least 2log(8/3)='+fmt(constants['address_WC_constant_lower_bound'])+'. Their L_1/I approaches this bound from below as k grows. Asymptotically balanced tribes with growing width have limit '+fmt(constants['tribes_WC_limit'])+', and bent functions have ratio '+fmt(constants['bent_WC_ratio'])+'. The finite census and known families do not determine the global extremizers.','',
 'CHECKED: the failure of a raw CI^2 bound is visible directly in the AND formula. These ratios are computed before conversion to binary floating point; the WC float in the JSON can round to one, so use its stored Lq_bits and ratios.','']
out+=[table(['AND n','I','L_1/I^2'],[[r['n'],fmt(r['I']),fmt(r['L_over_I_squared'])] for r in analytic if r['name']=='AND' and r['n']>=32]),'',
 '## The interpolation','',
 'CHECKED: the following are maxima over the complete five-variable NPN census, which also contains every smaller function by adding dummy variables. The last row is q=0, meaning the limit A. Sources: census_n5_npn.json and independent_census.json.','']
rows=[]
for q in qkeys:
    a=d5['best_over_I'][q];b=d5['best_balanced_over_I_minus_1'][q]
    rows.append([q,fmt(a['ratio']),'0x'+a['tt_hex'],fmt(b['ratio']),'0x'+b['tt_hex']])
out+=[table(['q','max L_q/I','witness hex','max balanced L_q/(I-1)','balanced witness hex'],rows),'',
 'CHECKED: growth over this grid is from '+fmt(d5['best_over_I']['1.0']['ratio'])+' to '+fmt(d5['best_over_I']['0.0']['ratio'])+', a factor '+fmt(d5['best_over_I']['0.0']['ratio']/d5['best_over_I']['1.0']['ratio'])+'. At small q the extremizer switches to AND_5. Finite-census boundedness as q decreases is not evidence of a dimension-uniform theorem by itself. The individual n=1,2,3,4 maxima and the n=6,7 sample grids are retained in their census JSON files.','',
 'PROVED: for each fixed q>0, FMEI would imply a linear bound with factor (1+1/q). Present general theorems yield the same factor times I log(2+I). Uniformity at q=0 is the OPEN containment conjecture.','',
 '## Independent checks and resources','',
 'CHECKED: audit.py uses dense direct integer character sums and an explicit containment incidence matrix on every truth table through four variables. It also recomputes every recorded extremizer using Python integers and alternating sums on restrictions, tests degree granularity and the monotone identity, and compares compressed family formulas with complete truth tables.','',
 table(['audit','result'],[
 ['all-through-four direct integer tables',sum(x['tables'] for x in audit['errors'].values())],
 ['maximum direct integer WC error',0],
 ['independent NPN4 class count',audit['independent_npn4']['classes']],
 ['five-variable independent C/Python maximum-ratio error',fmt(diff)],
 ['analytic/complete-table comparisons',audit['analytic_vs_truth_table']['rows']],
 ['maximum analytic comparison absolute error',fmt(audit['analytic_vs_truth_table']['max_abs_error'])],
 ['random NPN invariance checks',audit['npn_invariance']['tests']],
 ['tensor product checks',audit['proof_checks']['tensor_tests']],
 ['maximum tensor L_q error in bits',fmt(audit['proof_checks']['tensor_Lq_max_abs_error'])],
 ]),'',
 'CHECKED: restriction_address.json tests the data-coordinate and address-coordinate restriction formulas at k=1,2,3, then evaluates the PROVED induction obstruction for larger k. The local charge and uniform-coordinate charge both diverge. This disproves those induction rules, not the WC conjecture.','',
 'Reproduce all numerical receipts with `python3 run.py --regenerate-npn`, then `python3 summarize.py`. run.py uses one numerical thread and retains niceness at least 10. The initial direct `nice -n 10` calls emitted a sandbox warning; os.getpriority independently confirmed that the processes already inherited niceness 10. The final runner checks this without attempting an unnecessary priority change.','']
receipt=read('run_receipt.json')
out+=['CHECKED: run_receipt.json records the completed numerical run, with peak child RSS '+str(receipt['max_child_rss_bytes'])+' bytes ('+fmt(receipt['max_child_rss_bytes']/2**30)+' GiB), below the brief\u2019s per-process cap. Each compute mode has a separate resources_*.json receipt. The NPN file checksum is `'+audit['npn5_sha256']+'`. No external Python project code is imported; NumPy and mpmath are the numerical libraries used.','',
 'OPEN: the universal linear WC conjecture, its best constant and extremal families, and the uniform q-to-zero containment bound. No claimed proof of any of these is made.']
Path('RESULTS.md').write_text('\n'.join(out)+'\n')
final=dict(status='CHECKED',independent_census_max_ratio_error=diff,independent_census_witnesses_agree=True,
           all_scan_positive_violations={f'n{d["n"]}_{d["kind"]}':d['max_positive_violation'] for d in ds+samples},
           direct_table_counts={k:v['tables'] for k,v in audit['errors'].items()},family_truth_table_rows=len(family),analytic_family_rows=len(analytic),
           peak_child_rss_bytes=receipt['max_child_rss_bytes'])
assert all(v<=1e-11 for d in final['all_scan_positive_violations'].values() for v in d.values())
Path('final_audit.json').write_text(json.dumps(final,indent=2))
print(json.dumps({k:v for k,v in final.items() if k!='all_scan_positive_violations'},indent=2))
