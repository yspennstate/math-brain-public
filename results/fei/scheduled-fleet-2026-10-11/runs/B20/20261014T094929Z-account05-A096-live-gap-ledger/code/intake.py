from pathlib import Path
import json,hashlib
run=Path(__file__).resolve().parents[1]
old=run.parent/'20261013T220343Z-account05-A096-live-gap-ledger/code/intake.py'
code=old.read_text(encoding='utf-8').replace('20261011T234252Z-account05-A096-live-gap-ledger/out/SOURCE_LEDGER.json','20261014T042803Z-account05-A096-live-gap-ledger/out/SOURCE_LEDGER.json').replace('stage2','stage5')
exec(compile(code,str(old),'exec'))
p=run/'out/SOURCE_LEDGER.json';ledger=json.loads(p.read_text(encoding='utf-8'))
ledger['schema']='a096-source-bound-adoption-delta/6'
ledger['adoption_actions']=[
 {'claim':'A096-NONFLAT-POINT-QUOTIENT-REMAINDER@1','action':'Adopt full-scope A081 acceptance; consume A082 acceptance with correction to review-only empty-mask mass sentence. Original source remains unchanged.'},
 {'claim':'A096-CHILD-BANK-PRICE-FIVE-OBSTRUCTION@1','action':'Consume A082 full-scope acceptance, confirmed by A081 at exact point-law section scope. No universal bank-price interpretation.'},
 {'claim':'A082 stage5 REVIEW section1 normalization','action':'Review says derivative empty-mask mass delta*a_i^2/E_i; correct mass a_i^2/E_i. A081 explicit witness 1/2 versus1/128. Original A096 complete mu and resulting L are correct. No author claim retraction or blocked dependent required.'},
 {'claim':'A001-NEUTRAL-CORE-ACTUAL-DATA-TRANSFER@1','action':'Consume A081 full-scope acceptance and separate 30 ordered second-query extension. Do not duplicate them or promote to arbitrary supplied Q.'},
 {'claim':'A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK@1','action':'Use as independently accepted source dependency via A098 full reconstruction. New continuation keeps its actual incoming Q; no fresh floor reset.'},
 {'claim':'A096-PAID-FLOOR-NO-RESET-HISTORY@1','action':'Scoped conditional application: any finite adaptive physical history spends erasures and full terminal CE from original paid A097 floor. Conditional-reference refunds nonnegative; independent terminal CE stays charged.'},
 {'claim':'A096-INHERITED-CONSTANT-TERMINAL-COST@1','action':'Actual three-bit point sign with matching original Q gives constant child inherited Q=(5/8,1/8,1/8,1/8), CE=log2(8/5)>0 at I=0. Obstructs descendant local-rate promotion only.'}]
ledger['gap_map']={
 'C018':{'paid':'Singleton and T12 independently accepted; root no-reset history conserves already paid CE','unpaid':'Universal higher-layer erasure/root reference construction; no universal constant improvement'},
 'C019':{'paid_this_stage':'For A097 paid floor, all finite adaptive histories have erasure plus full terminal CE <= same original floor CE; executed debits kept','unpaid':'Find universal initial O(I) reference or selected policy with paid terminal conversions'},
 'C020':{'paid_this_stage':'Inherited complete references normalized by marginalization; independent full terminal cost coefficient one','unpaid':'Construct cheap complete reference for arbitrary Boolean source'},
 'C024':{'paid_this_stage':'No-reset transport arbitrary depth on a paid supplied reference, with exact conditional-KL refund and signed child amplitudes','unpaid':'Prescribed canonical descendant reset/local influence bank; false for unchanged inherited constant-terminal reference'}}
ledger['next_action']='Price the actual signed reset from inherited marginalized Q to admissible descendant references after an active query, jointly with complementary terminal and old debit; first witness has zero-influence terminal with log2(8/5) incoming debt.'
ledger['source_helper']={'path':str(old),'sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'purpose':'Reuse own read-only source-complete intake into new run only'}
p.write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
