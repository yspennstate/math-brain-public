from pathlib import Path
import json
R=Path(__file__).resolve().parents[1];A=R.parents[1]
for d in ['code','out']:(R/d).mkdir(exist_ok=True)
old=A/'runs/20261026T232430Z-account04-A089-repair-specialist/code'
for name in ['prior.py','arithmetic.py']:(R/'code'/name).write_bytes((old/name).read_bytes())
spec={'version':'A089-correlated-summary-repair-v1','family':'arbitrary Boolean row dictionaries with deterministic correlated state map; radius-one prime edits for source review','domain':'all81 maps {0,1}^2->{0,1,2} and64 triples of1-bit rows; fixed weight-state map on2 bits with4096 triples of2-bit rows;56 seed/padding source cases','case_count':{'summary_circuits':9280,'prime_edit_cases':56},'symmetry':'none; source n3 seeds are an explicitly selected list, not exhaustive','arithmetic':'Fraction, direct characters/FWHT/edges, prime-log vectors and outward192-bit log enclosures','memory_estimate_mb':120,'maximum_runtime_seconds':55,'pilot':'64 small summary circuits and8 selected large circuits; under55s','no_automatic_dimension_escalation':True}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A089 stage22 ACTIVE: audit A092 summary-only obstruction; derive retained-row entropy replacement and exact correlated-state influence; FEI OPEN.\nNEXT: Validate coefficient-one row source and original edge ledger; preserve summary-only counterfamily; initial original-source payment remains unpaid.\n',encoding='utf-8')
print('spec and checkpoint saved')
