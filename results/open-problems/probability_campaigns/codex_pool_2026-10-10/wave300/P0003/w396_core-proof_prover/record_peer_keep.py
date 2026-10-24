from pathlib import Path
import difflib
import json

root=Path(__file__).resolve().parent
peer_path='~/brain_workers/w397/REVIEW_w396_proof.md'
review={'reviewer':'w397','verdict':'KEEP','scope':['L0','L0prime','L1','L2','L3 under condition (C)','first-entrance injection (U)'],'citation_fix':'LSW Lemma 3.2 for uniqueness; Theorem 6.1 for the SLE avoidance values','source':peer_path,'assigned_referee':'w398','assigned_referee_verdict':'pending','different_login_verified':False,'full_target_proved':False}
(root/'PEER_REVIEW_RECEIPT.json').write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')
claims=[json.loads(s) for s in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
kept={'w396-S1.2':'L1','w396-S1.3':'L2','w396-S1.4':'L3 under (C)','w396-S1.8':'L0prime','w396-S1.10':'(U)'}
for c in claims:
    if c['id'] in kept:
        c['peer_review']={'reviewer':'w397','verdict':'KEEP','scope':kept[c['id']],'source':peer_path,'different_login_verified':False}
        c['review_state']='one peer KEEP; assigned referee w398 pending'
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')
state=json.loads((root/'DRAFT_STATE.json').read_text(encoding='utf-8'))
local=Path(state['draft_path'])
before=local.read_text(encoding='utf-8')
bundle=json.loads(before)
e=next(e for e in bundle['entries'] if e['key']=='maximal-collar')
e['proof_text']=e['proof_text'].replace('E D_tau=D_0=r(A)-r(B)','E D_tau=E D_0=r(A)-r(B)')
after=json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
local.write_text(after,encoding='utf-8')
target=Path(state['submitted_path']).as_posix()
patch=root/'patches/02_initial_filtration_expectation.diff'
patch.write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/'+target,tofile='b/'+target)),encoding='utf-8')
state.update({'mathematical_review_received':True,'peer_review_source':peer_path,'assigned_referee_review_received':False,'submitted_revision_has_pending_clarification':True,'clarification_patch':str(patch),'ingested':False,'retrievable':False})
(root/'DRAFT_STATE.json').write_text(json.dumps(state,indent=2)+'\n',encoding='utf-8')
src=json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
for s in src['sources']:
    if s['id']=='lsw-chordal-restriction':s['locator']='Lemma 3.2 (uniqueness); Theorem 6.1 (SLE avoidance formula)'
src.update({'peer_review_received':True,'peer_review_source':peer_path,'reviewed':True,'review_status':'One peer KEEP on finite lemmas; assigned referee and cross-login admission pending','assigned_referee_review_received':False})
(root/'SOURCE_STATUS.json').write_text(json.dumps(src,indent=2)+'\n',encoding='utf-8')
for name in ['measurements.json','ARTIFACT_VALIDATION.json']:
    obj=json.loads((root/name).read_text(encoding='utf-8'))
    obj.update({'mathematical_peer_reviews':1,'assigned_referee_reviews':0,'cross_login_admission_verified':False})
    (root/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
receipt=json.loads((root/'FINITE_CHECKS.json').read_text(encoding='utf-8'))
report='Saved a P0003 proof attempt centered on one result: a static collar deficit controls all SAW exploration prefixes without a path-length factor. The fixed-length version retains n-k in its continuation count. The packet also proves the exact conditioning cost, a conditional weak-limit bridge and a first-entrance counting bound. H_disk, the concrete collar-count estimate attempted here, remains unproved; this does not solve P0003.\n\nRun measurements: seven locally valid draft cards, seven relations and ten claim rows; no live changes. Exact finite regression was deferred by a fresh distress/throttle gate (zero mathematical assertions). Artifact syntax/schema checks passed; they are not mathematical proof or evidence of improved recall. This remains a proposal pending final review and integration. See measurements.json and ARTIFACT_VALIDATION.json.\n\nSubmitted draft: '+state['submitted_path']+'. w398 received the full packet as msg-13de88a071. w397 independently kept L0/L0prime, L1--L3 under their assumptions and (U); no different-login admission or w398 verdict is recorded. The original fixed-length catalog source and the distinct all-length chordal route are separated explicitly.\n\nApply: before normal coordinator integration, apply patches/02_initial_filtration_expectation.diff to the submitted draft (or use the clarified local copy). It writes E[D_0] for a general initial filtration; the fixed-start SAW proof is unchanged. The draft addition is patches/01_saw_collar_draft.diff. No live store integration was run.\n\nRisks: H_disk is open; tightness, continuum normalization and conformal identification are also unproved. Geometric edge deletion and literal collar hypotheses must be preserved. Progress and hook proposals are staged locally under the worker write boundary.\n\nNEXT: w398 audit the packet and clarification; then bound mutually avoiding fixed-length prefix/suffix counts for H_disk.\n'
(root/'REPORT.md').write_text(report,encoding='utf-8')
with (root/'review_packet/REVIEW.md').open('a',encoding='utf-8') as f:
    f.write('\nPeer audit received: w397 KEEP on L0/L0prime, L1--L3 under (C), and (U); source '+peer_path+'. Citation correction applied in ATTEMPT.md and SOURCE_STATUS.json. One draft proof clarification is ready in patches/02_initial_filtration_expectation.diff: E D_0 replaces D_0 when the abstract F_0 is nontrivial. The local draft includes this clarification; the submitted draft is left for the reviewer to patch before integration. No cross-login admission or assigned-referee verdict is claimed.\n\nNEXT: w398 audit the corrected packet and apply the draft clarification before integration.\n')
with (root/'STATUS.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-10: Incorporated w397 full-snapshot KEEP on L0/L0prime, L1--L3 and (U). Verified and fixed LSW citation: Lemma 3.2 uniqueness, Theorem 6.1 avoidance values. Prepared clarification diff for the abstract E[D_0] proof; did not edit the submitted/live file. w398 and cross-login admission remain pending. STATE stays NEEDS_REVIEW.\n')
print(json.dumps({'peer_keep_received':True,'reviewer':'w397','assigned_referee_pending':True,'claim_rows':len(claims),'draft_clarification_patch':str(patch),'numerical_status':receipt['status'],'full_target_proved':False}),flush=True)
