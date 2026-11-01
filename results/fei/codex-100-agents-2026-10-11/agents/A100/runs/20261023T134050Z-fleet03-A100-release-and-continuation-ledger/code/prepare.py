from pathlib import Path
import json, hashlib
R=Path(__file__).resolve().parents[1]; A=R.parent.parent
old=A/'runs/20261023T112759Z-fleet03-A100-release-and-continuation-ledger'
# These are new files in this run, not rewrites of source artifacts.
s=(old/'code/check_ghost.py').read_text(encoding='utf-8')
prefix=s.split('\nctrl=')[0]
(R/'code/exact.py').write_text(prefix,encoding='utf-8',newline='\n')
p=R/'code/ledger.py'
s=p.read_text(encoding='utf-8').replace("cid=='A079-ZERO-SINGLETON-GHOST-CREDIT-SHARP'", "cid=='A097-NECESSARY-FLOOR-ADMISSION-SAME-ORIGINAL-OWNER'")
s=s.replace('accepted=[]; partial=[];', "full_verdicts.add('HOLDS_AT_EXACT_STATED_SCOPE_WITHOUT_REPAIR')\naccepted=[]; partial=[];")
p.write_text(s,encoding='utf-8',newline='\n')
spec={'helper_version':'A100-floor-review-1','family':'literal original 4-bit complementary controller and 3 equal-sign core on disjoint L-bit parity blocks; both signs; ALL first-block histories and both next physical children', 'domain':{'pilot_L':[1],'full_L':[1,2,3],'general_floor_cases':27},'case_count':'50 prefix nodes, 28 complete admission terminals, 56 post-admission children; 27 rational floor profiles','symmetry':'none; all labelled prefix outcomes and both signs','arithmetic':'integer Walsh; Fraction references; exact prime-log linear forms; analytic log-sum for continuum','memory_estimate_MB':140,'pilot_max_seconds':55,'max_runtime_seconds':55,'automatic_escalation':False,'helper_sha256':hashlib.sha256((R/'code/exact.py').read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256((R/'code/review_floor.py').read_bytes()).hexdigest(),'audit_sha256':hashlib.sha256((R/'code/audit_floor.py').read_bytes()).hexdigest(),'audit_domain':'direct characters for L=1 both signs, direct physical pivots L=1..3, rational chain-rule factorization','audit_memory_MB':40}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8',newline='\n')
(A/'STATUS.md').write_text('STATE: A100 stage20 active: independent A097 declared-floor/same-original-owner review; full FEI OPEN.\nNEXT: Check minimum-cost floor, all physical prefixes and installed-reference continuation; refresh release and continuation ledger.\n',encoding='utf-8',newline='\n')
print('FROZEN_SPEC saved; hashes bound; no mathematical search executed by prepare.py')
