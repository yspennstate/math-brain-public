from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(exist_ok=True)
old=R.parent/'20261013T223410Z-fleet05-A028-stopping-tree-payment'/'code'/'exact.py'
(R/'code'/'exact.py').write_text(old.read_text(encoding='utf-8'),encoding='utf-8')
spec={'helper':'A028-shared-point-selector-v1','actual_family':'Point selectors between Boolean branches with a common k-bit block and disjoint private blocks; actual bent/one-point-flip branches',
'domain':{'pilot':'k1: all 4x4 no-private branches, r1,2; k2: all16x16 no-private branches,r2; bent k4,r1,2,4',
'full':'k1: all branches private dimension0 or1 (20x20),r1..4; k2: all16x16 no-private branches,r1..4; bent k4,6,r1,2,k'},
'case_count':{'pilot':291,'full':2630},'symmetry':'none; labeled exhaustive branch pairs within frozen small domains',
'arithmetic':'integer Walsh, exact Fraction/prime-log; rational outward atanh24 intervals',
'memory_estimate_MB':128,'maximum_runtime_seconds':{'pilot':55,'full':300},'max_actual_dimension':12,
'automatic_escalation':False,'heavy_job':False}
(R/'out'/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print('Frozen specification saved before computation.')
