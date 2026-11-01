from pathlib import Path
import json,hashlib
run=Path(__file__).resolve().parent.parent
old=run.parent/'20261013T220343Z-fleet05-A096-live-gap-ledger/code/intake.py'
code=old.read_text(encoding='utf-8').replace('20261011T234252Z-fleet05-A096-live-gap-ledger/out/SOURCE_LEDGER.json','20261013T220343Z-fleet05-A096-live-gap-ledger/out/SOURCE_LEDGER.json').replace('stage2','stage3')
exec(compile(code,str(old),'exec'))
p=run/'out/SOURCE_LEDGER.json';ledger=json.loads(p.read_text(encoding='utf-8'))
ledger['schema']='a096-source-bound-adoption-delta/4'
ledger['adoption_actions'] += [
    {'claim':'A096-TERMINAL-KL-REFUND-AUDIT@1','action':'Adopt A073 and A001 independent full-scope acceptances; source-complete records in A001 stage4 CLAIMS.json; no universal payment accepted'},
    {'claim':'A001-BOUNDED-DEGREE-REFUND-LOSS@1','action':'Consume exact within-tail loss and full-support vanishing-I objection; remains author-proved pending independent review'},
    {'claim':'A090-DEGREE-COARSENED-REFUND-OBSTRUCTION@1','action':'Consume within-degree tribes obstruction; not a refutation of full conditional reference; pending independent review'},
    {'claim':'A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1','action':'New exact partial duplication and sufficient-partner binary quotient; one-bit local influence payment refuted by bounded-ratio actual Boolean witness; independent review pending'}]
ledger['gap_map']['C018']['new_audit']='A correlated non-product row can preserve complete KL via its informative binary partner; deleting that partner loses the exact terminal M_i, locally unbounded per erased-pair influence'
ledger['gap_map']['C018']['controls'] += ['A001: bounded prefix plus undifferentiated tail loses unbounded refund even at full support and I->0','A090: retaining exact degree alone loses unbounded within-degree tribes refund','A096: one correlated bit can carry d bits of KL; retain complete reference mass outside derivative support']
ledger['next_action']='Construct a likelihood-ratio-preserving conditional partition for a nonzero-erasure shared-coordinate row, or debit its exact remainder once to a certified terminal-core reserve'
ledger['source_helper']={'path':str(old),'sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'purpose':'Prior source-complete intake code reused inside current run only'}
p.write_text(json.dumps(ledger,indent=2,ensure_ascii=False),encoding='utf-8')
