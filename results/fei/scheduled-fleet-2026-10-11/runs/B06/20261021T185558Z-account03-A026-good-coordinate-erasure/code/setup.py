from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
A=R.parent.parent
(R/'out').mkdir(exist_ok=True)
old=A/'runs/20261011T232716Z-account05-A026-good-coordinate-erasure/code'
for name in ['transitive.py','transitive_v2.py']:
 (R/'code'/name).write_bytes((old/name).read_bytes())
src=A/'runs/20261014T040156Z-account05-A026-good-coordinate-erasure/code/core.py'
s=src.read_text(encoding='utf-8')
s=s.replace("OLD=ROOT.parent/'20261011T232716Z-account05-A026-good-coordinate-erasure'/'code'","OLD=ROOT/'code'")
(R/'code/core.py').write_text(s,encoding='utf-8')
spec={'helper_version':'A026-signed-JS-data-v1','family':'arbitrary balanced-encoder identities through 2 data bits; point-defect G on m+1 bits, quadratic bent H on m independent bits and dummy j, Maj3 encoder','parameter_domain':{'identity_data_dimensions':[1,2],'actual_bent_m':[2,4,6],'symbolic_spectrum_m':[4,6,8,10,12],'data_tree_m':4},'case_count':'272 ordered branch pairs; 528 physical coordinate rows; 3 actual bent roots; 5 symbolic roots; 3 prescribed data policies plus stopped prefixes','symmetry':'none on ordered branch pairs; single canonical bent phase and point origin, justified by explicit formulas, no exhaustive class claim','arithmetic':'integer Walsh, physical flip counts, Fraction, prime-log vectors; outward rational atanh intervals (48 terms, 2^140 rounding)','memory_estimate_mb':180,'max_runtime_seconds':55,'pilot':'m=2 actual root and all 16 ordered one-bit pairs, same 55 second guard','no_dimension_escalation':True}
(R/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
(A/'STATUS.md').write_text('STATE: Stage17 active: exact signed-JS debit identity; testing point/bent local-price obstruction and same-owner payment; FEI OPEN.\nNEXT: Certify actual query and full terminals, prove all-m lower bound, save protocol outputs.\n',encoding='utf-8')
print('Setup saved; frozen specification precedes searches.')
