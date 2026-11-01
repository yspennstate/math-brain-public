"""Save receipts and submit only the specifically authorized per-worker draft/hook."""
import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
now=datetime.now(timezone.utc).isoformat()
status=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
status.update({
    'target_statement':'For static site-iid strictly elliptic nearest-neighbor RWRE on Z^d, d>=3, and every fixed deterministic nonzero real direction l, P_0(X_n dot l -> +infinity) belongs to {0,1}.',
    'assumptions':['site-iid transition vectors','static retained environment','strict positivity of all nearest-neighbor transitions','d>=3','fixed deterministic nonzero direction'],
    'uniform_ellipticity_required_by_original_question':False,
    'primary_statement_recovered':True,
    'current_openness':'UNKNOWN',
    'external_resolution':'Primary preprint claims full resolution; statement checked, proof not independently checked here.',
    'formal_check':{'status':'NOT_PERFORMED','theorem':'OAI.DirectionalZeroOne.directional_zero_one','comparator_contains_admitted_placeholder':True,'trusted_axiom_receipt':None,'caveat':'Comparator is a target skeleton; no assertion about a separate implementation is inferred from its sorry.'},
    'primary_sources':[
        {'title':'Selected Topics in Random Walks in Random Environment','authors':['Alexander Drewitz','Alejandro F. Ramirez'],'url':'https://arxiv.org/pdf/1309.2589','version':'1309.2589v1','question_locator':'Open question 3.2, PDF page 42, printed page 40, equation (3.2)','assumption_locator':'Definition 2.3, PDF page 7, equation (2.6): strict ellipticity','statement_quote':'P_0[A_l] in {0,1}?','verification':'Question and E/UE distinction read directly from primary source'},
        {'title':'The zero-one law for planar random walks in iid random environments revisited','author':'Martin P. W. Zerner','url':'https://arxiv.org/pdf/0706.0745','version':'0706.0745v1','scope':'Planar d=2 result only; not a higher-dimensional deduction'},
        {'title':'A directional zero-one law under strict ellipticity','author':'OpenAI','date':'2026-09-23','url':'https://raw.githubusercontent.com/openai/math/main/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf','locator':'Theorem 1.1, PDF page 2','local_file':str(ROOT/'sources'/'directional_zero_one_20260923.pdf'),'sha256':'245e917113b3545b311c4c9eab739227d530f527081c1b0be4a92ea904559683','verification':'Theorem statement and full hypotheses checked; proof audit pending'},
        {'title':'DirectionalWalk comparator target','url':'https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/DirectionalWalk.lean','local_file':str(ROOT/'sources'/'DirectionalWalk.lean'),'sha256':'8ad4588537c02fac9d123a9ba7fd780e9eda1575b48f674320733fad3938da11','locator':'Lines 78-81 one-based; theorem closes by sorry','verification':'Not a formal proof receipt'}],
    'prior_attempts':['C0044-A001 superseded by C0044-A002; latter corrects disjointness versus zero-one confusion'],
    'exact_id_checks_without_C0044_record':['probability_1000_intake_F_20260908/problems.jsonl and attempts.jsonl','probability_1000_attempts_H_20260912/problems.jsonl and attempts.jsonl when present','probability_1000_attempts_I_20260914/problems.jsonl and attempts.jsonl when present'],
    'updated_at':now,
})
(ROOT/'SOURCE_STATUS.json').write_text(json.dumps(status,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
result={'row_id':'S1.w585.003','type':'measured_retrieval_repair','statement':'A single draft density/UI criterion card changes hypothesis-bearing bridge retrieval in a scoped 14-card lexical replay from 0/3 to 3/3 top-three hits.','evidence':str(ROOT/'RETRIEVAL_MEASUREMENT.json'),'status':'local measured proposal; independent review and global validation pending','independent_reviewer':'w587 pending','remaining_gap':'Additional UI assumption is unproved under C0044 hypotheses; local retrieval is not global improvement.'}
with (ROOT/'RESULTS.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(result,ensure_ascii=False)+'\n')
draft=(ROOT/'bundle_001.json').read_bytes()
inbox=Path('~/math-brain-inbox/w585')
inbox.mkdir(exist_ok=True)
target=inbox/'bundle_001.json'
if target.exists():
    if target.read_bytes()!=draft: raise RuntimeError('Existing inbox draft differs; refusing overwrite')
else:
    part=inbox/'bundle_001.part'
    if part.exists() and part.read_bytes()!=draft: raise RuntimeError('Existing part differs; refusing overwrite')
    part.write_bytes(draft)
    part.rename(target)
hook={'id':'rwre-density-bridge-w585-01','area':'math','event':'PreToolUse','cue':'C0044 or directional zero-one proof using quenched positivity, an invariant environment law, or normalized incoming densities','fire_when':'A proof step infers directional probability one from q>0, or assumes density UI from first-moment normalization alone.','silent_when':'A conditional statement explicitly assumes density UI or invariant-law existence and keeps the parent result unresolved.','text':'For directional zero-one, q>0 is weaker than q=1. An invariant law or density UI needs its own hypothesis and proof. E f_n=1 alone does not give UI. State the missing bridge before using the retrieved theorem.','evidence':'~/brain_workers/w585/ATTEMPT.md Lemmas 2-4 and refuted route; RETRIEVAL_MEASUREMENT.json 0/3 to 3/3; memory prob1000_ranking_hour_555_problems_and_the_unread_inbox_corrections_2026_09_07','proposer':'w585'}
assert len(hook['text'])<=300
proposal=Path('~/primary_directive/hooks1000/proposals/math-w585.jsonl')
line=json.dumps(hook,ensure_ascii=False)
existing=proposal.read_text(encoding='utf-8') if proposal.exists() else ''
if hook['id'] not in existing:
    with proposal.open('a',encoding='utf-8') as f: f.write(line+'\n')
(ROOT/'HOOK_PROPOSAL.json').write_text(json.dumps(hook,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
delivery={'submitted':{'at':now,'path':str(target),'draft_only':True},'reviewed':False,'ingested':False,'live_retrievable':False,'local_replay_retrievable':True,'adversary_statement_message_id':'msg-abb7a486ff','referee_boundary_message_id':'msg-1edd69d235','peer_delivery_channel':'Existing direct agent_mesh; team_comm failed due to absent team registration','hook_proposal':str(proposal)}
(ROOT/'DELIVERY_STATUS.json').write_text(json.dumps(delivery,indent=2)+'\n',encoding='utf-8')
files=['STATEMENT_FOR_ADVERSARY.md','SOURCE_STATUS.json','ATTEMPT.md','CLAIMS.jsonl','bundle_001.json','BRAIN_REPAIR.md','REPORT.md','VALIDATION.json','RETRIEVAL_MEASUREMENT.json','patches/01_c0044_density_bridge.diff','verify_packet.py','measure_retrieval.py','COMPUTE_GATE.json','DELIVERY_STATUS.json']
hashes=[{'path':str(ROOT/name),'bytes':(ROOT/name).stat().st_size,'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()} for name in files]
review={'candidate_id':'C0044','author':'w585','referee':'w587','referee_new_result_reviewer':'w590','novelty_claim':False,'parent_solved':False,'scoped_keep_requested':['conditional UI criterion and concentration proof subject to review','finite-time density identity','positivity-versus-one distinction','normalization counterexample and explicit missing gap'],
        'hardest_gap':'Derive subsequential UI of incoming densities or Cesaro densities from iid strict ellipticity, or replace that over-strong bridge.','external_status':'Resolution claimed by a 2026-09-23 primary preprint; not independently verified here.','author_served_model_evidence':'Unavailable from response-side metadata; requested settings and worker identity are insufficient.','referee_served_model_evidence':'Pending; referee must provide response-side evidence if a different-model gate is asserted.','mathematical_review':'pending','checks':'Exact finite quotient algebra/schema and task-scoped retrieval only; no formal-check receipt','files':hashes}
(ROOT/'REVIEW_PACKET.json').write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'submitted_draft':str(target),'draft_entries':7,'review_packet':str(ROOT/'REVIEW_PACKET.json'),'review_packet_sha256':hashlib.sha256((ROOT/'REVIEW_PACKET.json').read_bytes()).hexdigest(),'hook_proposal':str(proposal),'ingested':False}))
