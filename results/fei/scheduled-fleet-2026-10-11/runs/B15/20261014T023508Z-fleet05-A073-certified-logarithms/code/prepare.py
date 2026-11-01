from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261013T234148Z-fleet05-A073-certified-logarithms/code/review.py'
prefix=old.read_text(encoding='utf-8').split('def named_witnesses():')[0]
(R/'code/exact.py').write_text(prefix,encoding='utf-8')
spec={'helper_version':'A073-spectator-audit/2; own exact helper prefix from prior run',
 'helper_sha256':hashlib.sha256(prefix.encode()).hexdigest(),
 'actual_Boolean_family':'All signs n=1,2 and each parity-duplication subset; n=3 majority, parity, point defect, AND and all duplication subsets; bent point-selector and bent AND point-gate d=2,4,6',
 'parameter_domain':{'exhaustive_n':[1,2],'named_n3':['majority','parity','point','AND'],'bent_d':[2,4,6]},
 'case_count':110,'pilot_case_count':6,'symmetry':'None; labeled functions and subsets, including empty subset',
 'arithmetic':'Integer FWHT, inverse and physical edge checks; Fraction complete row laws; exact prime-log identities; N=12 positive-tail rational log intervals, no refinement',
 'memory_estimate_bytes':80000000,'max_runtime_seconds_per_job':55,'maximum_physical_dimension':8,
 'analytic_extension':'Even d>=2 AND point-gate; conditional binary remainder exact formula and uniform <=1/2 bit bound before influence weighting',
 'stop_rule':'Stop each sign at first exact identity or fixed-N rational enclosure; no dimension escalation'}
(R/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print('Frozen spec and own helper saved before computation')
