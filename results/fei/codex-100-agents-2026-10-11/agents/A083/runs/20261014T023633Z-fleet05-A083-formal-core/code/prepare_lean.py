from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
old=R.parents[0]/'20261013T234228Z-fleet05-A083-formal-core/code/check_lean.py'
s=old.read_text(encoding='utf-8')
start=s.index("spec={'helper_version'")
end=s.index("(R/'out/FROZEN_SPEC.json')")
spec={'helper_version':'Bayes occupancy kernel check v1','family':'physical weighted binary mixtures and occupied-prefix posterior factorization','domain':'rational masses with stated normalization, nonzero occupied group and nonnegative empty-prefix atoms','case_count':'three universally quantified theorems','symmetry':'none','arithmetic':'Lean core Rat','memory_estimate_MB':550,'memory_hard_cap_MB':1400,'maximum_runtime_seconds':60,'imports':['Init.Data.Rat.Lemmas']}
s=s[:start]+'spec='+repr(spec)+'\n'+s[end:]
s=s.replace('CoherentTransport.lean','BayesOccupancy.lean')
(R/'code/check_lean.py').write_text(s,encoding='utf-8')
(R/'out/LEAN_HELPER_SOURCE.json').write_text(json.dumps({'source':str(old),'sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'adaptation':'source target and frozen domain; resource guard unchanged'},indent=2),encoding='utf-8')
