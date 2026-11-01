from pathlib import Path
from datetime import datetime, timezone
import json

ROOT=Path(__file__).resolve().parent
required=['SOURCE_STATUS.json','STATEMENT.md','ATTEMPT.md','INDEPENDENT_OBSTRUCTION.md','CLAIMS.jsonl','AUDIT.md','AUDIT_VERDICTS.jsonl','AUDIT_SNAPSHOT.json','MEASUREMENTS.json','DENSITY_MEASUREMENTS.json','BRAIN_TARGET_RECEIPT.json','ORIGINAL_RECORD.json','DRAFT_BUNDLE.json','BUNDLE_VALIDATION.json','RELATION_EVIDENCE.jsonl','SUBMISSION_STATUS.json','REVIEW_PACKET.md','REVIEW_OUTBOX.jsonl','PROGRESS_OUTBOX.jsonl','hooks/proposals/math-w544.jsonl','patches/01_p0321_density_draft.diff']
for filename in required:
    assert (ROOT/filename).is_file(),filename
measure=json.loads((ROOT/'MEASUREMENTS.json').read_text(encoding='utf-8'))
density=json.loads((ROOT/'DENSITY_MEASUREMENTS.json').read_text(encoding='utf-8'))
validation=json.loads((ROOT/'BUNDLE_VALIDATION.json').read_text(encoding='utf-8'))
submission=json.loads((ROOT/'SUBMISSION_STATUS.json').read_text(encoding='utf-8'))
assert measure['checks']['all_assertions_passed']
assert density['all_assertions_passed']
assert validation['all_schema_and_scope_assertions_passed']
assert submission['submitted'] and not submission['reviewed']
assert not submission['ingested'] and not submission['retrievable']
bundle=json.loads((ROOT/'DRAFT_BUNDLE.json').read_text(encoding='utf-8'))
assert len(bundle['entries'])==3 and len(bundle['relations'])==3
assert all(e['kind'] in {'definition','concept'} for e in bundle['entries'])
original=json.loads((ROOT/'ORIGINAL_RECORD.json').read_text(encoding='utf-8'))

claims=[]
for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines():
    row=json.loads(line)
    assert all(k in row for k in ['claim_id','statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap','status'])
    assert row['status']=='sketch'
    row['independent_reviewer']='w545 designated; review request staged in REVIEW_OUTBOX.jsonl, delivery not confirmed'
    if row['claim_id']=='P0321-S01':
        row['remaining_gap']='Primary locator and phase distinction recovered by P0321-S02. Microscopic Gibbs specification and exact decay quantifiers remain a declared formalization choice.'
    claims.append(row)
(ROOT/'CLAIMS.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in claims),encoding='utf-8')

source=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source['primary_source_candidate']['verification']='Primary PDF text and exact printed-page locators checked; screenshots requested.'
source['paired_proof_read']=True
source['independent_route_saved_before_paired_proof']=True
source['route_adjustment']='Independent positive-shear calculation agrees with w543 H1-H2; disjoint extension is the correlated-Gaussian positivity obstruction in INDEPENDENT_OBSTRUCTION.md.'
source['upstream_ledger_recovery']={'receipt':'ORIGINAL_RECORD.json','problems_file_present':not original.get('problems_missing',False),'attempts_file_present':not original.get('attempts_missing',False),'result':'The old worktree paths cited by the intake builder are absent. Recovered migrated exact target and attempt cards instead; no claim that a missing ledger was checked.'}
source['bounded_owner_status_check']={'receipt':'BRAIN_TARGET_RECEIPT.json','population_target_cards':2,'result':'The two exact legacy target cards retain unsolved/unverified or unreviewed statuses. This bounded check is not a complete unpublished solved/retired-work audit; novelty and current openness remain UNKNOWN.'}
source['canonical_checkout_store_present']=(Path('~/math-research-brain/local/population/brain.sqlite3').is_file())
source['recent_primary_search']={'date':'2026-10-10','queries':['site:arxiv.org Riesz hexatic 2025','site:arxiv.org Riesz hexatic 2026','Riesz gases hexatic rigorous'],'result':'No verified present-day resolution recovered; absence of search hits is not evidence of openness.'}
(ROOT/'SOURCE_STATUS.json').write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

tail=density['negative_density_tails'][1]
row=measure['rows'][-1]
report=f'''# P0321: review-ready auxiliary obstruction

The new deliverable is a positivity guard for an exact Gaussian particle-density identification. A nondegenerate additive Gaussian density has a negative tail; with stationary covariance decay it is negative infinitely often along a ray, without assuming independent cells. It cannot itself be a finite nonnegative smoothing of a point configuration. The full proof is in INDEPENDENT_OBSTRUCTION.md. Approximate fluctuation laws and nonlinear positive observables remain possible.

P0321 is not solved by this packet. Current openness and novelty are UNKNOWN. The source survey gives a descriptive phase diagram, and the missing microscopic Gibbs/defect/correlation transfer on an open temperature interval remains the hardest piece. STATEMENT.md labels the stronger benchmark choices explicitly. The old upstream ledger path is missing; the migrated exact target cards and Lewin's primary VI.B passage were recovered.

The independent harmonic derivation was saved before reading w543. It agrees with the peer's positive-shear result. AUDIT.md and three verdict rows KEEP H1-H4 under their Gaussian hypotheses, with no admission of P0321. A precision note separates raw correlation limits from normalized decay rates. The new ray argument is a disjoint probabilistic extension and awaits w545's independent review; all own claim rows remain sketches.

Measured model comparison: {measure['checks']['covariance_contractions']:,} covariance contractions passed in {measure['elapsed_seconds']:.3f} s, with maximum error {max(measure['checks']['max_absolute_theta_contraction_error'],measure['checks']['max_absolute_density_contraction_error']):.3g}. At distance {row['distance']:.0f}, compatible C6={row['compatible_C6']:.6f}, against continuum limit {row['continuum_C6_limit']:.6f} (relative error {row['relative_error_to_limit']:.3%}); the independent-angle shortcut gives {row['independent_angle_GFF_C6']:.3g}. The exact beta=1 linear-density variance is {tail['variance']:.8f}, and its negative-tail probability is {tail['negative_probability']:.9g}. Nine H4 angular checks passed with maximum error {density['max_absolute_angular_error']:.3g}. Commands: python -X utf8 verify_elasticity.py; python -X utf8 collect_receipts.py, both from this folder and with separate fresh CPU gates.

Before preparation, the targeted read-only store query returned two legacy P0321 cards. The submitted draft adds one definition, two concepts, and three supported relations, including the exact existing problem end. Schema checks passed; no theorem or lemma was submitted. This is a measured, reviewable addition, not a claim of deployed recall improvement. SUBMISSION_STATUS.json separately records submitted=true, reviewed=false, ingested=false, retrievable=false; the latter flags mean no confirming receipt has been observed.

Apply (coordinator only, after independent mathematical review): use the submitted math-brain-inbox/w544/bundle_001.json with python -X utf8 ~/math-brain-build/tools/integrate_drafts.py --only w544. patches/01_p0321_density_draft.diff records the same proposed inbox addition. No live research-store writes, integration, or deployment were run by this worker.

Risks and limits: the Gaussian observables are not microscopic Delaunay bonds or a Gibbs particle density. The probability proof gives no finite-box tail rate. Different-login provenance is unverified, and no formal-check receipt is claimed. An actual correlation transfer requires a nonlinear/local approximation and errors small relative to correlations tending to zero.

Outbound team messages failed because no team was registered for w544. A later read received w543's source-only note. REVIEW_OUTBOX.jsonl preserves the narrow requests; PROGRESS_OUTBOX.jsonl and hooks/proposals/math-w544.jsonl are staged under the worker write boundary. The hook has explicit exact-density fire and fluctuation-law silent cases.

NEXT: w545 independently checks P0321-N01/N02; then derive a positive microscopic observable or local good-event comparison with scale-relative correlation errors.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
packet=(ROOT/'REVIEW_PACKET.md').read_text(encoding='utf-8')
packet=packet.replace('Mesh communication failed (no registered team; first read also saw a lock)', 'Outbound mesh communication failed (no registered team; first read also saw a lock); a later read received w543\'s source-only message')
(ROOT/'REVIEW_PACKET.md').write_text(packet,encoding='utf-8')
audit_rows=[json.loads(line) for line in (ROOT/'AUDIT_VERDICTS.jsonl').read_text(encoding='utf-8').splitlines()]
hook_rows=[json.loads(line) for line in (ROOT/'hooks/proposals/math-w544.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(audit_rows)==3 and all(r['verdict']=='KEEP' for r in audit_rows)
assert len(hook_rows)==1 and len(hook_rows[0]['text'])<=300
final_receipt={'checked_utc':datetime.now(timezone.utc).isoformat(),'required_files':len(required)+1,'own_claim_rows':len(claims),'audit_rows':len(audit_rows),'draft_entries':3,'draft_relations':3,'staged_hooks':1,'numeric_checks_passed':True,'schema_checks_passed':True,'independent_acceptance_of_own_results':False,'all_required_artifacts_present':True,'submission_receipt':'SUBMISSION_STATUS.json','next':'Independent w545 review of P0321-N01/N02; nonlinear/local correlation transfer remains open.'}
(ROOT/'FINAL_CHECK.json').write_text(json.dumps(final_receipt,indent=2)+'\n',encoding='utf-8')
status=(ROOT/'STATUS.md').read_text(encoding='utf-8').splitlines()
status[0]='STATE: NEEDS_REVIEW'
status[1]='NEXT: w545 checks P0321-N01/N02, then the coordinator reviews the concept-only submitted draft; microscopic correlation transfer remains open.'
status.append('2026-10-10: Review packet complete. Saved 8 own claim rows, 3 scoped peer audit verdicts, all measurement receipts, exact relation ends, and 3 validated draft entries submitted atomically to the named inbox. Own results remain unreviewed sketches; no live research-store ingestion or P0321 solution claimed. Outbound peer/progress/hook requests are staged locally. FINAL_CHECK.json passed.')
(ROOT/'STATUS.md').write_text('\n'.join(status)+'\n',encoding='utf-8')
print(json.dumps(final_receipt))
print('STATE: NEEDS_REVIEW')
