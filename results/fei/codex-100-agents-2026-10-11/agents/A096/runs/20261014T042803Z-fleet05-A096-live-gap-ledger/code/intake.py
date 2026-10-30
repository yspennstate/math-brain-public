from pathlib import Path
import json,hashlib
run=Path(__file__).resolve().parent.parent
old=run.parent/'20261013T220343Z-fleet05-A096-live-gap-ledger/code/intake.py'
code=old.read_text(encoding='utf-8').replace('20261011T234252Z-fleet05-A096-live-gap-ledger/out/SOURCE_LEDGER.json','20261014T013836Z-fleet05-A096-live-gap-ledger/out/SOURCE_LEDGER.json').replace('stage2','stage4')
exec(compile(code,str(old),'exec'))
p=run/'out/SOURCE_LEDGER.json';ledger=json.loads(p.read_text(encoding='utf-8'))
ledger['schema']='a096-source-bound-adoption-delta/5'
ledger['adoption_actions'] += [
    {'claim':'A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1','action':'Adopt A073 full-scope acceptance saved in stage4 CLAIMS; A004 also reports full acceptance, not independently re-reviewed here'},
    {'claim':'A073-NONZERO-ERASURE-BINARY-REMAINDER@1','action':'Consume A098/A085 independent acceptance provenance; no claim of arbitrary-core or retained-price payment'},
    {'claim':'A090-ARBITRARY-GATE-SIGNED-REFUND-PARTITION@1','action':'A096 independently reconstructs full original scope in current DERIVATION and exact checker; add acceptance record'},
    {'claim':'A001 repeated-owner/four-cell fixture','action':'Consume complete saved stage5 report: paid enlarged root ledger <=7/2 I, explicitly not unused certified terminal surplus'},
    {'claim':'A096-NONFLAT-POINT-QUOTIENT-REMAINDER@1','action':'New universal point-attachment remainder bound 2I_Y+9/8 I_X (I_Y/2 in nonconstant-child case); terminal charge retained'},
    {'claim':'A096-CHILD-BANK-PRICE-FIVE-OBSTRUCTION@1','action':'For exact nonflat point/dictator fixture and 4<=C<5, no constant query allowance covers L from actual S_C; C=5 covers L. Actual family H/I<=4.'}]
ledger['gap_map']['C018']['new_audit']='Arbitrary non-flat point-core quotient loss paid from one root influence partition; actual child surplus remains distinct, with a sharp price-five obstruction for the lossy quotient'
ledger['gap_map']['C018']['controls'] += ['A096: near-cancelling non-flat Fourier amplitudes covered by direct reference floor, no nonzero-coefficient lower bound assumed','A096: child bank S_C is not a fresh root quota; L-S_C>=e[(5-C)d-7] at C in [4,5) despite genuine child/root FEI price four']
ledger['next_action']='Use a sufficient signed/amplitude partition or a complete-reference price avoiding the injected quotient cost; prove its retained bill fits a single actual unused child surplus, with full core/gate terminals'
ledger['source_helper']={'path':str(old),'sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'purpose':'Reuse own source-complete intake into current run only'}
p.write_text(json.dumps(ledger,indent=2,ensure_ascii=False),encoding='utf-8')
