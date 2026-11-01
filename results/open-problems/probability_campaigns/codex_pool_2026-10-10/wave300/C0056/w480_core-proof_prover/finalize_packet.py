"""Save remaining result rows, hook diff, proof artifact hashes, and direct peer handoff."""
import difflib
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLAIMS = ROOT / 'CLAIMS.jsonl'
rows = [json.loads(line) for line in CLAIMS.read_text(encoding='utf-8').splitlines() if line.strip()]
known = {row['claim_id'] for row in rows}
result = json.loads((ROOT / 'SCALAR_CHECK_RESULTS.json').read_text(encoding='utf-8'))
additions = [
    {'claim_id':'C0056-W480-S1','kind':'source_scope_correction','statement':'The C0056 source is Bourgade arXiv:1807.03031 Section 2.1: iid centered variance-one potentials, periodic finite-volume restrictions, and microscopic volume scaling. The target combines a spectral delocalization component and a separate GOE statistics component; no implication from spectral purity to GOE is established here. The uniform[-1,1] working law requires an explicit sqrt(3) variance normalization bridge.', 'assumptions':['Read the cited 2018 source as a historical source, not current status certification.'], 'source':{'url':'https://arxiv.org/pdf/1807.03031','locator':'Section 2.1, printed page 7','quote':'there is no clear understanding about how extended states imply GOE spectral statistics','sha256':'b8b15c02ac7b675471097e9c499a6d588cfd7b0c591c49b0135f2a42eaedddb0'}, 'proof_or_counterexample':'Direct primary source inspection; byte hash matches the intake receipt. This is a source correction, not a mathematical proof.', 'independent_reviewer':'w482, pending', 'remaining_gap':'Current openness UNKNOWN; recent primary proof claim not audited; GOE component unaddressed.', 'status':'sketch','parent_problem_solved':False},
    {'claim_id':'C0056-W480-N1','kind':'numerical_cross_check','statement':f"A bounded CPU scalar run passed {result['identity_cases']} entropy-identity cases and {result['conditional_density_cases']} conditional-density cases, maximum relative identity error {result['max_identity_relative_error']}. The finite cavity integral increased from 4.218525850462488 at eta=0.01 to 30.97238182141814 at eta=1e-8; this supports the proved finite-dimensional divergence formula but is not a proof of LG.", 'assumptions':['Python float arithmetic','Fresh scalar compute gate: at most 10 CPU seconds and 200000 function evaluations','Scalar and 3-by-3 diagonal-cavity diagnostics only'], 'source':{'path':str(ROOT / 'SCALAR_CHECK_RESULTS.json'),'command':result['command']}, 'proof_or_counterexample':'Adaptive Simpson quadrature versus the independently derived closed form, plus exact finite-dimensional spectral formulas. No formal checker used.', 'independent_reviewer':'w482, pending', 'remaining_gap':'Floating-point checks do not establish any infinite-volume spectral claim.', 'status':'numerical evidence','parent_problem_solved':False},
]
with CLAIMS.open('a',encoding='utf-8') as handle:
    for row in additions:
        if row['claim_id'] not in known:
            handle.write(json.dumps(row,ensure_ascii=False)+'\n')

hook = (ROOT / 'HOOK_PROPOSAL.jsonl').read_text(encoding='utf-8')
hook_obj = json.loads(hook)
assert len(hook_obj['text']) <= 300
patches = ROOT / 'patches'
patches.mkdir(exist_ok=True)
target = '~/primary_directive/hooks1000/proposals/probability-w480.jsonl'
(patches / '01_log_cavity_hook.diff').write_text(''.join(difflib.unified_diff([],hook.splitlines(keepends=True),fromfile='a/'+target,tofile='b/'+target)),encoding='utf-8')

source_status_path = ROOT / 'SOURCE_STATUS.json'
ss = json.loads(source_status_path.read_text(encoding='utf-8'))
ss['bundle_state'] = {'prepared':True,'submitted':True,'reviewed':False,'ingested':False,'retrievable':False}
ss['review_state'] = 'submitted_to_named_referee; independent verdict pending'
if (ROOT / 'sources' / 'canonical_store_c0056.json').exists():
    ss['canonical_store_check'] = 'Read-only exact C0056 IDs queried in the explicitly assigned active population DB; receipt in sources/canonical_store_c0056.json. A separate canonical path under math-research-brain/local was not located in targeted pilot directories. No writes or solved-status certification.'
source_status_path.write_text(json.dumps(ss,indent=2)+'\n',encoding='utf-8')

names = ['ATTEMPT.md','STATEMENT_FOR_ADVERSARY.md','SOURCE_STATUS.json','CLAIMS.jsonl','REVIEW_PACKET.md','REPORT.md','SCALAR_CHECK_RESULTS.json','check_scalar.py','bundle_001.json','RELATION_SUPPORT.jsonl','BUNDLE_VALIDATION.json','HOOK_PROPOSAL.jsonl','patches/01_log_cavity_hook.diff','sources/SOURCE_RECEIPTS.json']
hashes = {name:{'path':str(ROOT / name),'sha256':hashlib.sha256((ROOT / name).read_bytes()).hexdigest()} for name in names}
(ROOT / 'FILE_HASHES.json').write_text(json.dumps({'purpose':'Frozen proof artifact receipt for review; not an integrator source manifest or live-store seal','files':hashes},indent=2)+'\n',encoding='utf-8')

mesh = '~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
common = f"C0056 scoped packet: {ROOT / 'REVIEW_PACKET.md'}; proof {ROOT / 'ATTEMPT.md'} sha256={hashes['ATTEMPT.md']['sha256']}; exact artifact paths/hashes {ROOT / 'FILE_HASHES.json'}. L1-L5/C1 author proofs; LG UNPROVED; no GOE or parent solved claim; current openness UNKNOWN. Author served-model evidence unavailable; do not substitute requested settings."
messages = [
    ('w482',common+' Please audit exact statements L1-L5/C1 and keep LG an explicit input. Independent verdict pending; any new referee result goes to w485.'),
    ('w481',common+' The isolated statement was sent first by direct mesh msg-eaad154505; your independent first-moment obstruction is acknowledged. Attack the entropy reduction and boundary-limit gap.'),
    ('w474','C0056 boundary claim: w480 developed logarithmic cavity/entropy purity criterion, scalar identity and finite-cavity obstruction. '+str(ROOT / 'ATTEMPT.md')+' . No certificate construction, GOE or parent solution claimed.'),
    ('w477','C0056 boundary claim: w480 developed logarithmic cavity/entropy purity criterion and finite-cavity obstruction. '+str(ROOT / 'ATTEMPT.md')+' . No certificate construction or GOE claimed.'),
    ('w483','C0056 boundary claim: w480 developed logarithmic cavity/entropy purity criterion and finite-cavity obstruction. '+str(ROOT / 'ATTEMPT.md')+' . No certificate construction or GOE claimed.'),
    ('codex-01a12190',common+f" Concept-only DRAFT ~/math-brain-inbox/w480/bundle_001.json sha256={hashes['bundle_001.json']['sha256']}, seven entries/six relations, local schema PASS. Scoped KEEP is requested, not yet received. Reviewed=false, ingested=false, retrievable=false. No integrator run or theorem promotion. Source receipts include the primary PDF exact matching hash. Hook proposal patch remains local."),
]
receipts = []
for recipient, body in messages:
    p = subprocess.run(['python','-X','utf8',mesh,'send','--agent','w480','--to',recipient,'--topic','probability300-C0056','--kind','message','--body',body],capture_output=True,text=True,encoding='utf-8',errors='replace')
    receipt = {'to':recipient,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    receipts.append(receipt)
    (ROOT / 'HANDOFF_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'to':recipient,'returncode':p.returncode,'stdout':p.stdout[:450]},ensure_ascii=False),flush=True)
assert all(r['returncode']==0 for r in receipts), 'One or more mesh handoffs failed; inspect HANDOFF_RECEIPTS.json'
assert len([json.loads(line) for line in CLAIMS.read_text(encoding='utf-8').splitlines()]) == 10
print(json.dumps({'claims':10,'draft_entries':7,'relations':6,'messages_delivered':len(receipts),'store_changed':False}))
