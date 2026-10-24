from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
old=R.parents[0]/'20261014T023633Z-account05-A083-formal-core/code/check_lean.py'
s=old.read_text(encoding='utf-8')
a=s.index('spec=');b=s.index("(R/'out/FROZEN_SPEC.json')")
spec={'helper_version':'reference-only row kernel check v1','family':'arbitrary rational normalized binary fallback; point-posterior matching','domain':'rational g,k0,k1 with k0+k1=1; rational u,g with u+g nonzero','case_count':'three universal rational identities','symmetry':'none','arithmetic':'Lean kernel Rat','memory_estimate_MB':550,'memory_hard_cap_MB':1400,'maximum_runtime_seconds':120,'imports':['Init.Data.Rat.Lemmas']}
s=s[:a]+'spec='+repr(spec)+'\n'+s[b:]
s=s.replace('BayesOccupancy.lean','ReferenceOnlyRows.lean').replace("out/FROZEN_SPEC.json","out/FROZEN_LEAN_SPEC.json").replace('p.wait(timeout=60)','p.wait(timeout=120)')
(R/'code/check_lean.py').write_text(s,encoding='utf-8')
dump={'source':str(old),'sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'adaptation':'source target and frozen scope only; resource guard unchanged'}
(R/'out/LEAN_HELPER_SOURCE.json').write_text(json.dumps(dump,indent=2),encoding='utf-8')
