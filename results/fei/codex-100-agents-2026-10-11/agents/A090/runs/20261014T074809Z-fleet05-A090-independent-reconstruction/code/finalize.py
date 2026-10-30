import json, hashlib
from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]; agent=root.parents[1]
src=Path(r'~\brain_workers\FEI100_20261011\agents\A001\runs\20261014T035113Z-fleet05-A001-quantifier-audit')
src96=Path(r'~\brain_workers\FEI100_20261011\agents\A096\runs\20261014T042803Z-fleet05-A096-live-gap-ledger')
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def write(name,obj): (root/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
claim=next(c for c in read(src/'CLAIMS.json') if c['claim_id']=='A001-SHARED-CORE-FOUR-CELL-OWNERSHIP')
digest=hashlib.sha256(claim['exact_statement'].encode()).hexdigest()
source_digest=claim['statement_sha256']
claim['statement_sha256']=digest
claim['review_records'].append({'reviewer':'A090','timestamp':datetime.now(timezone.utc).isoformat(),'verdict':'ACCEPT_AT_FULL_ORIGINAL_STATED_SCOPE_NO_REPAIR','method':'Reconstructed from theorem statement before reading source derivation; independent complete cell sums, likelihood fibers, joint extra-debit bound and conditional entropy bound; separate integer Walsh/physical flip/Fraction implementation','proof_source':str(root/'RECONSTRUCTION.md'),'validation_source':str(root/'out'/'check.json'),'source_statement_sha256':source_digest,'recomputed_exact_statement_utf8_sha256':digest,'hash_metadata_note':'Source supplied hash differs from UTF8 exact_statement hash; exact statement preserved verbatim, local hash corrected, source untouched; no mathematical repair.','reviewer_contributed_repair':False,'scope':'Every original clause, all even d>=2 and r>=1; enlarged complete root bill, all-selector loss counterexample, positive atoms and H<=4I. No hereditary child surplus or full FEI accepted.'})
claim['status']='INDEPENDENTLY_ACCEPTED_AT_FULL_ORIGINAL_SCOPE_BY_A090_LOCAL_ADOPTION_PENDING'
own=next(c for c in read(src96/'CLAIMS.json') if c['claim_id']=='A090-ARBITRARY-GATE-SIGNED-REFUND-PARTITION')
assert own['statement_sha256']==hashlib.sha256(own['exact_statement'].encode()).hexdigest()
write('CLAIMS.json',[claim,own])
result=read(root/'out'/'check.json')
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B18','packet_id':'A090',
 'gap_id':'OPEN-C018-TERMINAL-KL','attempt_id':5,
 'method':'Independent theorem-statement reconstruction of complete four-cell root reference and single-owner payment; exact Walsh/flip/rational certificate validation',
 'mathematical_delta':'Accepted A001 four-cell ownership at full stated scope: retained selector quotient plus all discarded KL/lower-edge costs paid once in a <=7/2 I root ledger. Consumed A096 full-scope acceptance of A090 signed partition. First missing implication is hereditary unused child surplus after a mixed core query.',
 'deliverable_status':'COMPLETE_LOCAL_SAVE_VERIFIED','mathematical_status':'SCOPED_SOURCE_CLAIM_INDEPENDENTLY_ACCEPTED_FULL_FEI_OPEN',
 'claim_versions_used':['A001-SHARED-CORE-FOUR-CELL-OWNERSHIP@1','A090-ARBITRARY-GATE-SIGNED-REFUND-PARTITION@1','A096-NONFLAT-POINT-QUOTIENT-REMAINDER@1 (statement consumed as frontier context only)','A096-CHILD-BANK-PRICE-FIVE-OBSTRUCTION@1 (statement consumed as frontier context only)'],
 'claims_created_or_changed':['A001-SHARED-CORE-FOUR-CELL-OWNERSHIP@1 independent review appended locally','A090-ARBITRARY-GATE-SIGNED-REFUND-PARTITION@1 A096 acceptance consumed locally'],
 'source_artifacts':[str(src/'CLAIMS.json'),str(src/'DERIVATION.md'),str(src96/'CLAIMS.json'),str(root/'RECONSTRUCTION.md'),str(root/'out'/'check.json')],
 'next_consumers':['A001','A096','A073','A086','A094','A099','B18','B20'],
 'next_action':'Audit one actual core-data restriction of the four-cell fixture using the SAME incoming complete reference and old single-owner debit; certify any child slack before spending it, with both terminal spectra retained.',
 'stagnant_substantive_attempts':0,
 'blockers':['Root physical allowance is not certified hereditary unused child entropy surplus; arbitrary non-flat complete reference plus full terminal/history payment still absent.'],
 'packet_ids':['A090']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
fields={
 'exact target, quantifiers, hypotheses and units':
 'Independent reconstruction of A001-SHARED-CORE-FOUR-CELL-OWNERSHIP@1, for every even d>=2 and integer r>=1. Actual uniform physical Boolean signs, base-two entropy/KL, canonical bent core with point-attached product of r two-bit negative-at-11 gates. Verdict HOLDS at full original scope, without repair. This is a complete root-row fixture, not a universal FEI proof or a hereditary child-bank theorem. Full FEI remains OPEN.',
 'sources actually read, revisions and theorem locators':
 f'Read BOARD.md dated 2026-10-14 07:47 UTC, own STATUS.md and B18 STREAM_NOTES.md v2 (still the initial baseline direction). Productive dispatch consumes the new root payment rather than repeats the completed baseline. Read full EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2. Read {src}/CLAIMS.json, the exact A001 four-cell statement, and {src96}/CLAIMS.json, including the A096 independent acceptance of our signed partition and its non-flat remainder/price-five frontier statements. RECONSTRUCTION.md was saved from the statement before reading A001 DERIVATION.md; that source was subsequently read for comparison. No new external paper theorem is invoked. A081 acceptance on the board and the precise A096 acceptance record retire the previous scoped partition as a live unreviewed candidate. No other agent files were changed.',
 'complete derivation or exact first unsupported line':
 'Full independent reconstruction is in RECONSTRUCTION.md. Exact four-cell probabilities and the exceptional-cell likelihood ratio yield M_C/e=1+(w/2)[d+2r-1+log A], L_C=e w D_y/2. The polynomial identity 3R_+-A>=0 gives D_y<=log3<2. Summing all selector extras once gives E<(r delta w/2)(d+2r+1)<=5/8<3a/2, so a single named core coordinate owns the combined extras. Core erasure <=2I_core and lower halves <=J/ln2 complete the <=7/2 I audit. Independent conditioning on selector emptiness gives H<=d+1+2r delta<=4I. The binary quotient loses at least r delta(3d/8-1/2), divergent against one specified core influence at r=2^d. All original source clauses reconstruct. First unsupported UNIVERSAL implication: the same root allowance survives an actual mixed core-data query as genuinely unused child entropy surplus with incoming complete reference, both terminal spectra and all old debits intact. Root price is not such a certificate. No general finite K for the universal retained-KL lower bound is proved.',
 'executed validation with domain, arithmetic, commands and outputs':
 f'FROZEN_SPEC.json preceded computation. Pilot physical (d,r)=(2,1),(2,2): 2 cases, 320 assertions, 0.0015 s. Main physical (2,1),(2,2),(2,3),(4,1),(4,2),(4,3),(6,1),(6,2): 8 cases, every selector queried, maximum physical dimension 10. Symbolic grid: every even d=2..32, r=1..64, 1024 cases. Total {result["exact_assertions"]} exact assertions PASS in {result["elapsed_seconds"]:.3f} s. Integer truth-table Walsh and physical flip counts independently verify every coefficient, atom positivity, influences, complete row and quotient normalizers, four-cell and binary laws, exceptional conditional laws, common likelihoods elsewhere and entropy-upper sufficient certificates. Fraction arithmetic certifies the polynomial KL bound, nonrenewed summed allowance and binary-loss lower bounds. No floating-point sign claims; logarithmic constants follow from proved rational likelihood inequalities. Commands: python -X utf8 runs\\{root.name}\\code\\check.py --pilot and the same command without --pilot. Outputs: out/pilot.json, out/check.json. Analytic quantifiers are proved separately; grid is validation, not extrapolation. Estimated memory <80 MB; no job expected above 300 MB, so memok not triggered. No heavy/background job or dimension escalation.',
 'proof dependencies and changed downstream conclusions':
 'This is an independent acceptance of the unchanged A001 claim statement/version, not a contributor repair. The reconstruction uses elementary coefficient expansion, KL chain rule, Parseval, binary entropy and actual physical edge counting. The source enlarged audit bills M_C+L_C, which conservatively dominates full M=M_C-L_C; it must not be represented as equality. CLAIMS.json also preserves A096 independent acceptance of A090 signed partition at its original scope. It is now justified to use the four-cell root ledger downstream; it remains unjustified to treat its core quota as a free recurrent child surplus. No shared registry, old immutable run, other agent folder, mirror, or brain was modified.',
 'one next mathematical action and independent reviewer':
 'A001/A096 should expose one actual core-data coordinate in the four-cell fixture, keeping the SAME incoming reference and previously booked root-owner debit, then identify exactly what genuinely unused signed child surplus remains. A086/A094 should audit that next mixed-query transfer with both terminal spectra retained. This directly tests the missing hereditary implication. No messages were sent; handoff is in the saved source-bound artifacts.',
 'actual persistence receipts or precise save blocker':
 'Four protocol files, reconstruction, frozen spec, code and outputs are locally saved inside the assigned A090 run; STATUS.md is current and WORKLOG.md/LEARNED.md appended. out/schema.json validates exact protocol field sets, unchanged claim hashes and compatibility copy identity; out/manifest.json gives local sizes and SHA256 receipts. Local save only: no mirror adoption/publication is asserted. No save blocker.'}
report='\n\n'.join('# '+k+'\n\n'+v for k,v in fields.items())
report+='\n\nSource metadata receipt: A001 supplied statement_sha256 '+source_digest+' differs from the exact_statement UTF8 digest '+digest+'. The exact statement is preserved verbatim and the local hash recomputed; both hashes are in the review record. This is a metadata discrepancy, not a proof repair. Source files remain untouched.'
report+='\n\n**Universal bridge:** This stage moves C018/C024 from an isolated quotient-loss reserve to an independently reconstructed complete four-cell root-row payment, including retained quotient price and all selector remainders, with one original physical owner and total bill <=(7/2)I. What remains is reference and budget transport through actual mixed restrictions: the paid root allowance has not become unused hereditary child surplus. NEXT tests that precise transport with both terminals and every old debit retained, the shortest direct step toward the universal bridge rather than another isolated class bound.\n'
(root/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: Stage 5 complete: A001 full four-cell root ownership independently HOLDS; retained quotient plus all remainders paid once at <=7/2 I; 24082 exact checks PASS; A096 acceptance of signed partition consumed; FEI OPEN.\nNEXT: A001/A096 expose one actual core-data query with SAME incoming reference and old root debit; certify genuinely unused child surplus and both terminal debts; A086/A094 review.\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp} Stage 5 {root.name}: reconstructed A001 four-cell claim from statement before source derivation comparison. All clauses HOLDS without repair; complete root payment preserves one owner. 8 physical and 1024 symbolic cases, 24082 exact assertions PASS in 0.199 s. Consumed A096 independent acceptance of previous arbitrary-gate claim. First open implication: mixed-query hereditary unused surplus, not root feasibility.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage 5 durable fact: A001 four-cell quotient for a bent core point-attached to r two-bit gate products jointly pays selector M_C+L_C beyond J with extra E<rw delta(d+2r+1)/2<=5/8<3a/2, one named owner only. Full M=M_C-L_C, so the source audit conservatively overpays 2L_C. Root B<=7I/2 and H<=4I are proved at fixture scope. Binary-only quotient total loss >=r delta(3d/8-1/2) cannot be assigned repeatedly to one core coordinate at r=2^d. A root physical quota is not hereditary unused child entropy surplus; retain reference and all debits when testing actual mixed queries.\n')
protocol=read(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
cf=protocol['required_per_run']['claim_fields'];pf=[s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(pf)
for c in [claim,own]:
    assert set(c)==set(cf)
    assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode()).hexdigest()
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()
assert all(s in fields for s in protocol['required_per_run']['report_fields'])
write('out/schema.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,'exact_statement_hashes_verified':True,'source_hash_discrepancy_preserved_in_review':True,'compatibility_copy_identical':True,'report_fields_complete':True})
manifest=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='manifest.json':
        raw=p.read_bytes();assert len(raw)<20*1024*1024
        manifest.append({'path':str(p.relative_to(root)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
for p in [agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md']:
    raw=p.read_bytes();manifest.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
write('out/manifest.json',manifest)
print(json.dumps({'status':'SAVED_SCHEMA_PASS','run':str(root),'review':'A001 full original stated scope; no repair','files_hashed':len(manifest)}))
