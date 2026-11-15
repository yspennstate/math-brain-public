import json,csv,math
from pathlib import Path
from symmetric import mask_vector

hp={}
if Path('certified_extrema.json').exists():
 for r in json.loads(Path('certified_extrema.json').read_text()):hp[r['n'],r['objective']]=r
if Path('suprema_certified.json').exists():
 for r in json.loads(Path('suprema_certified.json').read_text()):
  hp[r['n'],r['objective']]={'value':r['value_100_decimals'],'extremizers_up_to_global_sign':r['extremizers_up_to_global_sign']}
rows=[json.loads(Path(f'census_{n:02d}.json').read_text()) for n in range(1,25)]
fields=['A/I','B/I','Gamma/I','A/(I-1)','B/(I-1)','Gamma/(I-1)']
with open('census_counts.csv','w') as out:
 w=csv.DictWriter(out,fieldnames=['n','value_vectors','sign_representatives','nonconstant_representatives','balanced_representatives']);w.writeheader()
 for r in rows:w.writerow({'n':r['n'],'value_vectors':2*r['representatives'],'sign_representatives':r['representatives'],'nonconstant_representatives':r['nonconstant'],'balanced_representatives':r['balanced']})
lines=['# FEIB02 results','',
'Logs are base 2; A, B, Gamma and P are measured in bits, I in total influence. Ratios have units bits per unit influence. A value vector lists f_0 through f_n; + means +1. A mask fixes f_0=+1 and has bit t-1 set exactly when f_t=-1. Global negation preserves the results.','',
'## Exhaustive symmetric census','',
'Every one of the 2^(n+1) value vectors is covered through its global-sign representative. Constants are excluded from ratios. A dash denotes no balanced function with I>1. A separate integer interval census encloses every possible maximizer. Their exact logarithm expressions prove all remaining ties, and fixed-point positive-series bounds certify each supremum to 100 decimal places. Values below are rounded to ten decimal places. See extrema.csv for all objective values and value vectors, and suprema_certified.json for certified values and ties up to global sign.','',
'| n | A/I | B/I | Gamma/I | balanced A/(I-1) | balanced B/(I-1) | balanced Gamma/(I-1) |',
'|---:|---:|---:|---:|---:|---:|---:|']
csvrows=[]
for r in rows:
 n=r['n'];cells=[]
 for name in fields:
  entry=r['maxima'][name];ref=hp.get((n,name));val=float(ref['value']) if ref else entry['value'];cells.append('—' if val<0 else f'{val:.10f}')
 lines.append('| '+str(n)+' | '+' | '.join(cells)+' |')
 for name,entry in r['maxima'].items():
  if entry['value']<0:continue
  ref=hp.get((n,name));ext=ref['extremizers_up_to_global_sign'] if ref else [{'mask':entry['mask'],'value_vector':''.join('+' if x>0 else '-' for x in mask_vector(n,entry['mask']))}]
  for a in ext:csvrows.append({'n':n,'objective':name,'value':ref['value'] if ref else entry['value'],**a})
with open('extrema.csv','w') as out:
 w=csv.DictWriter(out,fieldnames=['n','objective','value','mask','value_vector']);w.writeheader();w.writerows(csvrows)
lines+=['','Balanced classes in even dimensions can be very small: zeros in the balanced columns can be exact parity values rather than missing computations. census_counts.csv records their sizes, independently checked by binomial subset sums.','',
'At n=24, P/I=0.9999998807907104; all P extrema, including balanced ratios, are in extrema.csv. A and P attain their maxima at a single-corner AND/OR vector in every enumerated dimension. This is an observation through n=24, not an all-dimensions extremal theorem.','',
'## Larger dimensions','',
'For the displayed dimensions all thresholds r=1,...,n and all parity-times-threshold vectors were evaluated, including every level. The parity convention is f_t=(-1)^t times the threshold at r. Hill-climbing results are lower bounds from an explicit finite proposal budget; they are not asserted to be local or global optima. Proposals emphasize the binomial bulk and use coordinate or short block flips.','',
'| n | best threshold B/I | best threshold Gamma/I | parity-threshold B/I | parity-threshold Gamma/I | value-vector B/I | value-vector Gamma/I |',
'|---:|---:|---:|---:|---:|---:|---:|']
for n in [25,32,64,128,256,512,1000,1024,2000]:
 t=json.loads(Path(f'thresholds_{n:04d}.json').read_text())
 p=Path(f'parity_thresholds_v3_{n:04d}.json');p=json.loads(p.read_text()) if p.exists() else None
 h=Path(f'hill_{n:04d}.json');h=json.loads(h.read_text()) if h.exists() else None
 vals=[t['maxima']['B/I']['value'],t['maxima']['Gamma/I']['value']]
 vals += [p['maxima']['B/I']['value'],p['maxima']['Gamma/I']['value']] if p else [None,None]
 hv=[s['final'][s['objective']] for s in h['searches']] if h else [None,None]
 if n==2000 and Path('gamma_refinement_2000.json').exists():
  ref=json.loads(Path('gamma_refinement_2000.json').read_text());hv[1]=max(hv[1],ref['best']['Gamma/I'])
 vals+=hv
 lines.append('| '+str(n)+' | '+' | '.join('—' if x is None else f'{x:.10f}' for x in vals)+' |')
if Path('thresholds_dense.jsonl').exists():
 dense=[json.loads(x) for x in Path('thresholds_dense.jsonl').read_text().splitlines()]
 lines+=['',f'The dense threshold sweep currently covers every dimension 1 through {dense[-1]["n"]}, all thresholds in each dimension; thresholds_dense.jsonl records the maxima and central threshold. For odd n the central threshold is balanced majority. The hill searches use the dimension grid above; dense parity coverage is described below.']
 outrows=[]
 for r in dense:
  n=r['n'];I=(2*n*math.comb(n-1,n//2))/(1<<n)
  center=r['central_threshold']
  z={'n':n,'central_r':center['r'],'balanced':bool(n%2),'I':I}
  for name in ['A/I','B/I','Gamma/I']:
   z[name]=center[name];z[name.replace('/I','/(I-1)')]=center[name]*I/(I-1) if n%2 and I>1 else None
  outrows.append(z)
 with open('majority.csv','w') as out:
  w=csv.DictWriter(out,fieldnames=list(outrows[0]));w.writeheader();w.writerows(outrows)
if Path('parity_dense.jsonl').exists() and Path('parity_dense.jsonl').stat().st_size:
 pd=[json.loads(x) for x in Path('parity_dense.jsonl').read_text().splitlines()]
 lines+=['',f'The independent Pascal sweep covers every parity-times-threshold vector in every dimension 2 through {pd[-1]["n"]}; n=1 gives a constant function and undefined influence ratios. parity_dense.jsonl and parity_family.csv give the per-dimension suprema.']
 with open('parity_family.csv','w') as out:
  w=csv.DictWriter(out,fieldnames=['n','A/I','A_threshold','B/I','B_threshold','Gamma/I','Gamma_threshold']);w.writeheader()
  for r in pd:w.writerow({'n':r['n'],'A/I':r['maxima']['A/I']['value'],'A_threshold':r['maxima']['A/I']['threshold'],'B/I':r['maxima']['B/I']['value'],'B_threshold':r['maxima']['B/I']['threshold'],'Gamma/I':r['maxima']['Gamma/I']['value'],'Gamma_threshold':r['maxima']['Gamma/I']['threshold']})
bal=[]
for n in [31,63,127,255,511,999,1023,1999]:
 p=Path(f'balanced_hill_v2_{n:04d}.json')
 if p.exists():
  for r in json.loads(p.read_text())['searches']:bal.append({'n':n,'objective':r['objective'],**r['balanced_ratios'],'value_vector':r['value_vector']})
if bal:
 with open('balanced_large.csv','w') as out:
  w=csv.DictWriter(out,fieldnames=list(bal[0]));w.writeheader();w.writerows(bal)
 lines+=['','Balanced paired-coordinate searches at odd dimensions through 1999 optimize the ratio over I-1 directly. balanced_large.csv gives all computed ratios and value vectors. At n=1999 they reach B/(I-1)=2.744446594676 and Gamma/(I-1)=1.360500539114. These remain bounded-search lower bounds.']
lines+=['',
'Parity-family outputs preserve tiny positive ratios in log2_ratios when the ordinary ratio underflows binary64. stable_log_check.log checks rare dimension-2000 functions at both 80 and 720 digits; ratio logarithms agree without needing precision proportional to n.','',
'The dimension-2000 value-vector column includes the independent periodic-run sweep in gamma_refinement_2000.json. The A search in hill_A_*.json used sixteen proposals per dimension and retained corner AND/OR; at n=2000 it gives A/I=2.998. Its positive influence is too small for binary64, so the output supplies log2 influence.','',
'Ordinary parity has A=B=Gamma=P=H=0 and I=n exactly, since its spectral law is a point mass on [n]. For odd n, balanced-majority ratios over I-1 are also given in majority.csv when the dense sweep is present. The threshold at r=1 gives A/I=3-4/n-(2-4/n)2^(-n) and P/I=1-2^(1-n) exactly.','',
'## Direct bounds and the FEI obstruction','',
'PROOFS.md proves B<=3.459354I and Gamma<=(8/5)I for every symmetric Boolean function. Above dimension 24 the proof is analytic; below it census_cert.c verifies an integer-only rational upper bound for every representative. constants.json and rational_constant_check.json check the constant two ways. The inherited bound A<=3.3252155I-Var follows by combining the supplied FEI benchmark with Theorem 1. No new direct sharper A bound is claimed.','',
'Theorem 1 with a uniform B/I bound cannot improve the supplied 4.650431 FEI constant: the three-variable vector +++- has B/I=1.3725562489182657..., exceeding the required 1.3252155. The dimension-2000 witnesses are much larger.','',
'The proved optimal-constant intervals are 3<=c_A<=3.3252155 (the upper bound inherits FEI), 2/ln 2<=c_B<=3.459354, and 1/ln 2<=c_Gamma<=8/5. PROOFS.md derives the lower limits from corner AND/OR and majority; majority_law_check.json verifies the exact finite derivative law and records the constants.','',
'## What the extremizers look like','',
'For B, the small-dimensional maximizers start as corner AND/OR functions, then become tails with extra short runs at distant weights. They need not be monotone. At n=24 one maximizing vector is +-++++++++++++++-----++++. The bulk of its negative mass is a one-sided binomial tail; the remote isolated change adjusts the spectral cancellations. At larger n, biased thresholds provide strong starting points and a few extra runs can improve them. This describes the computed witnesses and does not classify all extremizers.','',
'For Gamma, the maximizers have several alternating sign runs across the binomial bulk. At n=24 one is +++--+++---+++++---+++---. The unrestricted-coefficient means are small relative to the absolute restricted means, making cancellation a large fraction of dispersion. The searches at larger n favor oscillations on a scale comparable to sqrt(n), rather than a single threshold. Some seeds and proposals use that scale; the independent width/phase sweep also finds such witnesses. This describes the computed examples, not an asymptotic extremal theorem.','',
'## Checks and provenance','',
'census.c and census_cert.c are independent runs of the exact integer triangle. audit.py checks direct truth-table restrictions for every symmetric function through n=4, the general A+B=H and Theorem 1 identities on every Boolean function through n=4, exact Parseval and influence identities, and binomial up-transform identities at every census extremizer. audit_candidates.py checks balanced counts by a separate meet-in-the-middle subset-sum computation and compares all near-winners at 100 digits. audit_large.py checks selected large-n witnesses at high precision and tries the new inequalities on random symmetric functions. Output logs are audit.log, candidates_audit.log, family_check.log and large_audit.log.','',
'The recalled brain memory supplied the earlier derivative-envelope method and the distinction between the best FEI constant and the within-level bound. That recall helped. All writes stayed in this worker folder; no publishing, mesh posts, shared-memory writes or git operations were performed.']
Path('RESULTS.md').write_text('\n'.join(lines)+'\n')
print('wrote RESULTS.md and extrema.csv')
