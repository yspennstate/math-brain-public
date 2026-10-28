from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
s=json.loads((R/'out/FROZEN_SPEC_v1.json').read_text(encoding='utf-8'))
s['helper']='check_tree.py v2; same main family/domain/cap, corrected negative-reserve guard'
s['guards']='One additional three-bit point-defect K=1 singleton; all main K>=2 proper children have nonnegative reserve'
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(s,indent=2),encoding='utf-8')
(R/'out/ATTEMPT_V1.json').write_text(json.dumps({'status':'FAILED_HARNESS_GUARD','assertions_before_failure':757055,'first_failure':'final negative>0 guard, not a ledger inequality','cause':'All proper children in n<=3 main K>=2 domain have at most two bits and satisfy FEI(2); a negative reserve is impossible there','repair':'Use explicit noncritical K1 three-bit point-defect singleton guard; preserve complete v1 source; same main domain, arithmetic and runtime cap','excluded_from_final_pass_total':True},indent=2),encoding='utf-8')
print('v2 frozen; v1 failure preserved')
