from pathlib import Path
import datetime as dt
import difflib
import json

base=Path(__file__).resolve().parent
required=['ATTEMPT.md','CLAIMS.jsonl','SOURCE_STATUS.json','REVIEW_PACKET.md',
          'STATEMENT_FIRST.md','checks/exact_results.json','checks/compute_gate.json',
          'checks/bundle_validation.json','checks/submission.json','drafts/bundle_001.json']
assert all((base/f).is_file() for f in required)
submission=json.loads((base/'checks/submission.json').read_text(encoding='utf-8'))
results=json.loads((base/'checks/exact_results.json').read_text(encoding='utf-8'))
assert submission['submitted'] and results['status']=='PASS'
date=dt.datetime.now(dt.timezone.utc).isoformat()
review={
 'observed_at_utc':date,'reviewer':'w349',
 'source_file':'~/brain_workers/w349/PEER_AUDIT.md',
 'independent_precommitment':'~/brain_workers/w349/PEER_L1_INDEPENDENT.md',
 'verdicts':{'w348-L1':'KEEP','w348-L2':'KEEP','w348-L3':'KEEP',
             'w348-L4':'FIX: finite-fourth-moment derivative domain'},
 'repair_applied':'L4 defines U2 under finite fourth moments and identifies U2=T2 only if exponential moments exist near zero; current ATTEMPT, claims and submitted degree-two concept agree.',
 'repair_confirmation':'PENDING','final_referee':'w350','final_referee_verdict':'PENDING',
 'full_target_proof_verdict':'NOT_CLAIMED','account_provenance':'Different account provenance not verified by w348.'}
(base/'checks/independent_review_receipt.json').write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')

claims=[json.loads(line) for line in (base/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
for c in claims:
    if c['claim_id'] in review['verdicts']:
        c['independent_reviewer']['adversary_verdict']=review['verdicts'][c['claim_id']]
        c['independent_reviewer']['adversary_receipt']=review['source_file']
        c['independent_reviewer']['referee_verdict']='PENDING'
        if c['claim_id']=='w348-L4': c['scope_repair_status']='APPLIED; independent confirmation pending'
if not any(c['claim_id']=='w348-review-001' for c in claims):
    claims.append({
     'claim_id':'w348-review-001','target':'P0017','record_type':'independent_review_receipt',
     'statement':'w349 independently kept L1-L3 and identified the finite-moment/tilt-domain distinction in L4; the current packet implements the U2 repair.',
     'assumptions':['Verdicts apply to the component statements, not full KLS','Final w350 review is pending'],
     'source':review['source_file'],'proof_or_counterexample':'Recorded verdicts and the current L4 statement; bounded moments do not imply a finite Laplace transform near zero.',
     'independent_reviewer':{'adversary':'w349','referee':'w350','final_verdict':'PENDING'},
     'remaining_gap':'Confirm corrected L4 and independently audit L1-L4; universal all-degree log-concave input remains unproved in this packet.',
     'status':'sketch','mathematical_proof':False})
(base/'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')

status=json.loads((base/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
status['independent_reviews']=review
status['brain_states']['submitted']=True
status['brain_states']['reviewed']=False
status['brain_states']['ingested']=False
status['brain_states']['retrievable']=False
status['brain_state_semantics']='False means no verified completion receipt in this packet, not proof that an external event did not occur. Adversarial component review is partial; final referee review is pending.'
(base/'SOURCE_STATUS.json').write_text(json.dumps(status,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
metrics=json.loads((base/'METRICS.json').read_text(encoding='utf-8'))
metrics['submitted']=True
metrics['claim_rows']=len(claims)
metrics['independent_adversary_keeps']=3
metrics['independently_accepted_results']=0
metrics['final_referee_verdict']='PENDING'
(base/'METRICS.json').write_text(json.dumps(metrics,indent=2)+'\n',encoding='utf-8')
validation=json.loads((base/'checks/bundle_validation.json').read_text(encoding='utf-8'))
validation['claim_rows']=len(claims)
validation['independent_adversary_keeps']=3
(base/'checks/bundle_validation.json').write_text(json.dumps(validation,indent=2)+'\n',encoding='utf-8')

patch_dir=base/'patches'
patch_dir.mkdir(exist_ok=True)
live='~/math-brain-inbox/w348/bundle_001.json'
raw=(base/'drafts/bundle_001.json').read_text(encoding='utf-8')
diff=''.join(difflib.unified_diff([],raw.splitlines(keepends=True),
                                fromfile='a/'+live,tofile='b/'+live))
(patch_dir/'01_p0017_brain_draft.diff').write_text(diff,encoding='utf-8')

report='''Prepared four exact component results for P0017: sharp binomial block-tensor recovery, its approximate-symmetry bound and kernel counterexample, the exact all-degree tilt operator norm for independent centered exponential products, and the degree-two quadratic-form duality. Complete proofs and exact assumptions are in ATTEMPT.md and CLAIMS.jsonl.

The main analytic result is ||T_d||=sqrt(binom(2d-2,d-1)), in every product dimension, with optimal all-degree base R=2. Its proof uses the product law to split orthogonal coordinate supports. It does not extend this independence to general log-concave measures. The single full-target gap is the universal all-degree Hilbert--Schmidt tilt bound for arbitrary regular log-concave measures; the cited reduction and general-measure approximation are external steps.

The exact original source is Randomstrasse101, arXiv:2603.29571v1, Entry 13, Conjecture 30. Existing brain cards record a Gaussian-only Hermite proof attempt. The old original campaign ledger path is missing, so its typed population-store cards supply that digest. October 4 primary papers 2610.05474v1 and 2610.01447v2 now claim full KLS. This packet makes no novelty or complete-proof verdict about those claims.

Measurements: python -B -X utf8 tests/gated_exact.py passed 287 incidence coefficient cases, 812 sharpness coordinate cases, 169 polynomial-moment cases, 45 support trace cases and 511 positive compositions in 0.0272442 seconds. The fresh governor-state receipt was 18.8 seconds old and the live GPU gate allowed this bounded CPU check. At d=8 the stated published recovery factor 65,536 becomes the sharp factor 12,870; the latter upper bound is already present in the published proof. This measures the constants and finite checks, not a recall-speed or novelty improvement.

w349 independently kept L1-L3 and caught a derivative-domain error in L4. L4 now defines the quadratic-moment operator U2 with finite fourth moments and identifies it with a tilt derivative only if exponential moments exist near zero. Corrected L4 confirmation and the final w350 review are pending. Finite arithmetic and structural validation are not formal proof receipts. All seven entries remain concept drafts, with six allowed relations and accepted owner-own-work source tags.

Submitted: ~/math-brain-inbox/w348/bundle_001.json. Local copy: drafts/bundle_001.json. Submitted, reviewed, ingested and retrievable are tracked separately in SOURCE_STATUS.json; only submission is complete. No live store, recall control or service was changed by w348. The tensor-assumption hook is saved locally in HOOK_PROPOSAL.jsonl for authorized relay; the worker-folder-only rule prevents direct placement in the shared hooks directory.

Apply: after independent KEEP, the validating coordinator integrates the reviewed draft from the named inbox folder. patches/01_p0017_brain_draft.diff is the unified creation diff naming that live draft path; it is already submitted and is an archive for review. Run the gated check again before integration under the then-current compute state.

NEXT: w350 audits L1-L4, prioritizing the L3 support-direct-sum and factorial normalization, then confirms the corrected L4 domain before coordinator integration.
'''
(base/'REPORT.md').write_text(report,encoding='utf-8')
packet=(base/'REVIEW_PACKET.md').read_text(encoding='utf-8')
packet=packet.replace('checks/exact_results.json (finite results when PASS)',
                      'checks/exact_results.json (PASS: 0.0272442 seconds)')
packet=packet.replace('drafts/bundle_001.json (concept drafts, once packaged)',
                      'drafts/bundle_001.json (seven submitted concept drafts, six relations)')
packet += '\n2026-10-10 review receipt: w349 KEEP L1-L3; L4 derivative-domain FIX applied in the current proof, claims and submitted concept. Final w350 review and corrected-L4 confirmation remain pending. See checks/independent_review_receipt.json.\n'
(base/'REVIEW_PACKET.md').write_text(packet,encoding='utf-8')
print(json.dumps({'packaged':True,'submitted':True,'entries':7,'relations':6,
                  'claim_rows':len(claims),'adversary_keeps':3,'referee':'PENDING',
                  'report':str(base/'REPORT.md')}))
