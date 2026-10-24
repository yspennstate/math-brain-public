from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
S=Path(r'~\brain_workers\FEI100_20261011\agents\A096\runs\20261014T042803Z-account05-A096-live-gap-ledger')
P=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(P.read_text(encoding='utf-8-sig'))
check=json.loads((R/'out/CHECK.json').read_text());assert check['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
ids=['A096-NONFLAT-POINT-QUOTIENT-REMAINDER','A096-CHILD-BANK-PRICE-FIVE-OBSTRUCTION']
claims=[c for c in json.loads((S/'CLAIMS.json').read_text(encoding='utf-8-sig')) if c['claim_id'] in ids]
for c in claims:
 # Preserve the exact source statement and its original hash; independent reviews cannot silently alter scope.
 c['review_records'].append({'reviewer':'A082','timestamp':now,'verdict':'ACCEPT_AT_FULL_ORIGINAL_SCOPE_NO_REPAIR','reviewer_contributed_repair':False,'method':'Independent direct character spectra and physical edge counts; rational atanh logarithm intervals; analytic minimum-cut and actual entropy-surplus reconstruction','proof_source':str(R/'REVIEW.md'),'validation_source':str(R/'out/CHECK.json'),'source_claims_sha256':hashlib.sha256((S/'CLAIMS.json').read_bytes()).hexdigest()})
 c['status']='INDEPENDENTLY_ACCEPTED_BY_A082_LOCAL_ADOPTION_PENDING'
 assert set(c)==set(protocol['required_per_run']['claim_fields'])
def save(n,x): (R/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
save('CLAIMS.json',claims)
next_action='A096/A090: evaluate full retained reference price with the sufficient (V,beta_T) statistic against one unused actual child bank; keep both full terminal entropies and do not substitute a root quota.'
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B17',packet_id='A082',gap_id='C024-ACTUAL-CHILD-BANK',attempt_id='A082-A096-INDEPENDENT-BANK-AUDIT-01',method='Exact finite labeled audit plus independent all-dimensional proof reconstruction',mathematical_delta='Both A096 arbitrary-core quotient remainder and sharp loss-only child-bank threshold five independently accepted without repairs; 2760 exact Boolean fixtures and seven rational interval bank certificates. Universal available-bank transfer remains open.',deliverable_status='COMPLETE_LOCAL_SAVED',mathematical_status='TWO_SCOPED_CLAIMS_INDEPENDENTLY_ACCEPTED_FULL_FEI_OPEN',claim_versions_used=[dict(claim_id=i,version=1) for i in ids],claims_created_or_changed=[dict(claim_id=i,version=1,change='Independent A082 acceptance attached locally; source immutable') for i in ids],source_artifacts=['REVIEW.md','FROZEN_SPEC.json','code/audit.py','code/finalize.py','out/PILOT.json','out/CHECK.json','out/RECEIPTS.json'],next_consumers=['A096','A090','A001','A073','A085','A097','B20'],next_action=next_action,stagnant_substantive_attempts=0,blockers=['No theorem establishes availability of the root quotas after retained reference and terminal charges. Mirror and downstream adoption are not verified.'],packet_ids=['A082'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
report=f'''# A082: independent actual-bank certificates

## exact target, quantifiers, hypotheses and units

Review A096-NONFLAT-POINT-QUOTIENT-REMAINDER@1 and A096-CHILD-BANK-PRICE-FIVE-OBSTRUCTION@1 unchanged. All finite d,r>=1 for the remainder, d>=2 for the bank fixture, actual Boolean signs on uniform physical cubes, bits and physical flip influence. The bank threshold concerns the specified quotient loss alone.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision {protocol['revision']} read completely. BOARD.md snapshot 2026-10-14 04:50 UTC and B17 STREAM_NOTES.md v2 (2026-10-11 23:40 UTC), own STATUS and previous stage2 PROGRESS read. B17's K5 assignment is already completed and independently certified in own stage2; no repeat census. New dependency: A096 run {S.name}, DERIVATION Sections 1-3, CLAIMS.json and code/check.py. A073/A100 latest reports were inspected for overlap; their bent-only improvements are not reused as proof dependencies. Earlier campaign baseline sources remain recorded in previous runs; no claim that they were freshly reread this stage.

## complete derivation or exact first unsupported line

REVIEW.md independently reconstructs the complete conditional probability laws, summed arbitrary-core loss, cube cut bound, rational 9/8 coefficient, exact point-family entropy and actual child surplus, and the nonconstant-child tensor continuation. Both original claims accepted at full scope with no contributor repair. The first unsupported universal line is payment of full retained reference price plus loss from one actually unused certified child surplus.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec preceded computation. Command: python -X utf8 code/audit.py --pilot (20 cases), then python -X utf8 code/audit.py (2760 cases). Exact direct character sums, direct physical edge counts and Fraction probabilities; 24-term range-reduced atanh rational log intervals. Full result: {check['cases']} cases, {check['gate_rows']} relevant gate rows, {check['assertions']} assertions, PASS, runtime {check['runtime_seconds']:.3f}s. Symbolic interval certificates at d=2,3,4,8,16,32,64 saved in out/CHECK.json. Estimated memory 100MB, so the >300MB memok gate does not apply; no heavy job or dimension escalation. Pilot initially exposed a checker-only missing influence weight in the KL chain-rule replay; corrected before full validation. No source theorem repair was needed.

## proof dependencies and changed downstream conclusions

The reviewed source claims have no external proof dependencies. Both exact statement versions and hashes preserved in CLAIMS.json, with independent acceptance records added locally only. Rate C<5 same-price loss-only child payment fails even with actual C-certified children and a rate-four root, including nonconstant children. Root loss bounds remain valid but are not unspent bank certificates. No improvement in the universal FEI constant is claimed.

## one next mathematical action and independent reviewer

{next_action} A094 can audit this independent reconstruction; A096 should consume the acceptance and A090 should retain the sufficient statistic rather than inject an avoidable quotient loss.

## actual persistence receipts or precise save blocker

Four protocol files, frozen spec, review, code and rational outputs saved within this run; rolling STATUS/WORKLOG/LEARNED updated. out/RECEIPTS.json records SHA256 and size of all saved run files except itself. Exact schema keys, JSON readback, identical compatibility delta and file sizes checked by the finalizer. GitHub mirrors and downstream adoption not checked or asserted.

## Universal bridge

C024 history transfer advances by two independent scoped acceptances: arbitrary non-flat quotient loss has one original influence partition, and a genuine unused child bank cannot replace that partition at any price below five for the specified loss. Full retained reference and terminal payment remain open; universal constant improvement is zero. NEXT tests the actual sufficient signed-amplitude reference against genuinely unused child surplus, the shortest surviving route to the universal bridge because it avoids the now-certified artificial loss obstruction rather than extending another isolated finite class.
'''
for title in protocol['required_per_run']['report_fields']:assert '## '+title in report
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: Independent full-scope A096 non-flat remainder and price-five child-bank obstruction accepted; 2760 exact fixtures PASS; full FEI OPEN.\nNEXT: A096/A090 price sufficient (V,beta_T) reference against one unused actual child bank, keeping full terminal debt; A094 review; no n=6 census.\n',encoding='utf-8')
for file,entry in [('WORKLOG.md',f'\n{now}: Stage {R.name}: reconstructed A096 arbitrary-core conditional loss and sharp child-bank threshold-five, including nonconstant tensor continuation; 2760 direct-character/Fraction fixtures PASS. Initial pilot caught missing e in our interval replay, fixed. Both unchanged claims independently accepted; full retained cost unpaid.\n'),('LEARNED.md','\nStage 20261014T045125Z: The exact loss-only bank threshold five is a policy obstruction, not an FEI lower bound: point-sign roots already obey H<=4I. Arbitrary signed-core amplitudes plus gate mask form a sufficient KL statistic. A dedicated root influence allowance does not certify an unused terminal bank. The small exhaustive regression domain does not replace the all-dimensional cut/Parseval/derivative proof.\n')]:
 with (A/file).open('a',encoding='utf-8') as f:f.write(entry)
receipts={}
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  data=p.read_bytes();assert len(data)<20*1024*1024
  receipts[str(p.relative_to(R))]={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
save('out/RECEIPTS.json',receipts)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for p in R.rglob('*.json'):json.loads(p.read_text(encoding='utf-8-sig'))
print(json.dumps({'saved_files':len(receipts)+1,'claims':len(claims),'case_count':check['cases'],'status':'COMPLETE_LOCAL_SAVED'}))
