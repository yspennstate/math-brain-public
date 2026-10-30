from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]; TEAM=ROOT.parents[3]
campaign=Path('~/mop_fei100/reports/fei-2026-10-11')
paths=[TEAM/'BOARD.md',TEAM/'claude/B01/STREAM_NOTES.md',TEAM/'claude/B20/SYNTHESIS.md',ROOT.parents[1]/'STATUS.md',ROOT.parents[1]/'LEARNED.md',campaign/'EXECUTION_PROTOCOL.json']
paths+=list((TEAM/'claude/B01/runs').glob('*/CLAIMS.json'))
for agent in ['A002','A003','A027','A028','A030','A051','A075']:
    runs=sorted((TEAM/'agents'/agent/'runs').glob('*'))
    if runs:
        paths += [p for p in runs[-1].glob('*') if p.name in ['REPORT.md','DERIVATION.md','ERASURE_LEDGER.md','CLAIMS.json']]
base=ROOT.parents[0]/'20261011T225209Z-fleet05-A005-noncircular-endpoint-referee/code/check.py'
paths+=[base]
records=[]
for p in paths:
    b=p.read_bytes();records.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
(ROOT/'out/SOURCE_MANIFEST.json').write_text(json.dumps(records,indent=2))
spec={'helper_version':'A005-stage2-v1','family':'all labelled Boolean signs through n=3 and tensor powers of three-bit point defect',
      'domain':'C in {0,5/2,8/3,3}; all n=0..3 truth tables; tensor m=1..4; one additional seed baseline at C=8/3',
      'case_count_full':1129,'case_count_pilot':97,'pilot_domain':'n<=2 all tables; tensor m=1,2',
      'symmetry':'none for truth-table checker; analytic tensor identity uses copy/seed permutation symmetry',
      'arithmetic':'integer FWHT, Fraction log-prime vectors, direct physical edge counts, rational intervals',
      'estimated_memory_MB':80,'maximum_runtime_seconds':60,'maximum_dimension_full':12,'maximum_dimension_pilot':6,
      'reused_arithmetic_helper':str(base),'reused_helper_sha256':hashlib.sha256(base.read_bytes()).hexdigest(),
      'no_automatic_dimension_escalation':True}
(ROOT/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2))
print(json.dumps({'source_count':len(records),'frozen_full_cases':1129,'frozen_pilot_cases':97}))
