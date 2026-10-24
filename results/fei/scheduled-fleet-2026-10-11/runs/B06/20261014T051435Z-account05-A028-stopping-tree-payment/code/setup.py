from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(exist_ok=True)
old=R.parent/'20261014T022306Z-account05-A028-stopping-tree-payment'/'code'/'exact.py'
(R/'code'/'exact.py').write_text(old.read_text(encoding='utf-8'),encoding='utf-8')
spec={'helper':'A028-general-controller-reserve-v1','actual_family':'arbitrary sign controller a on fresh cube; two Boolean branches with full shared data, or one shared plus disjoint one-bit private blocks',
'domain':{'pilot':'all controllers dimensions0..1; all full-overlap data dimensions0..1; four selected two-bit branches for each partially shared child',
'full':'all controllers dimensions0..2; all full-overlap data dimensions0..2; all16 two-bit branches for each partially shared child'},
'case_count':{'pilot':216,'full':11704},'symmetry':'none, all labeled truth tables in stated domains',
'arithmetic':'integer Walsh/Fraction/canonical prime-log and outward rational atanh24 enclosures',
'memory_estimate_MB':160,'maximum_runtime_seconds':{'pilot':55,'full':600},'max_dimension':5,
'automatic_dimension_escalation':False,'heavy_job':False,'reference_laws':'true calibrated shared atoms plus uniform conditional private law, all off-target private fibers retained'}
(R/'out'/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print('Frozen specification and exact arithmetic helper saved.')
