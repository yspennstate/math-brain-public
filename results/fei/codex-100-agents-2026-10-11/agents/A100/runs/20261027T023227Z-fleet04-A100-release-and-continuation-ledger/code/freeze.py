from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
spec={'helper_version':'A100-query-account-v1','family':'ALL labelled Boolean tables n=0,1,2,3; actual queries and complete reference resets, plus exact multiplicity model of A011 M1/a1/b12..16 allowed edit','domain':'278 tables; masses1,1/2; true/uniform mixture coefficient1,1/2; two-level full physical query trees; reset1/3; matched no-reset controls','case_count':'1112 general transactions; 5 exact grouped in-family witnesses','symmetry':'none for general tables; grouped witnesses use proved equal Fourier coefficients and literal multiplicities','arithmetic':'integer characters/Fraction; exact rational combinations of prime logarithms; analytic log-sum/Jensen outside finite test domain','memory_estimate_MB':70,'pilot_max_seconds':55,'max_runtime_seconds':55,'no_automatic_escalation':True,'checker_sha256':hashlib.sha256((R/'code/check_account.py').read_bytes()).hexdigest()}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print('Frozen specification saved before pilot.')
