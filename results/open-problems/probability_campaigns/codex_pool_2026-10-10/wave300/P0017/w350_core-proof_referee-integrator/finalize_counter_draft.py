from pathlib import Path
import difflib
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w350')
MESH = Path('~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py')

def save_json(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def read_rows(path):
    return [json.loads(s) for s in path.read_text(encoding='utf-8').splitlines() if s.strip()]

proof_path = ROOT / 'OPERATOR_WEIGHTED_COUNTEREXAMPLE.md'
assert proof_path.is_file() and 'ORIGINAL rate-one prior' in proof_path.read_text(encoding='utf-8')
rows = read_rows(ROOT / 'CLAIMS.jsonl')
new_rows = [
    {
        'id': 'w350-C005',
        'statement': 'No universal T>0 and finite K bound E[A_t Var(f(X)|Y_t)]/E Var(f(X)|Y_t) by K for every compactly supported full-dimensional isotropic log-concave prior in dimension one, every fixed smooth f, and almost every t in (0,T). For the original prior X=Exp(1)-1, Y_t=tX+sqrt(t)G and f_c(x)=exp(cx), this ratio tends to 1/t as c increases to 1/2. A_t is the posterior variance under the ORIGINAL prior.',
        'assumptions': ['Independent standard Gaussian observation noise', 'The counterexample concerns the stronger operator-norm variance-weighted estimate, not the actual covariance estimate (W)', 'The compact transfer uses recentering, whitening and smooth tests agreeing with the exponential on compact prior support'],
        'source': 'owner-own-work: w350 derivation in OPERATOR_WEIGHTED_COUNTEREXAMPLE.md; scope of the surrogate from w349 WEIGHTED_GAP.md',
        'proof_or_counterexample': 'Apply Claim A with the proved exponential C_P<=4. Bound the deficit 1/t-A_t by its expectation under f_c^2 weighting. The weighted joint law has X+1 of rate 1-2c, while A_t remains the ORIGINAL posterior variance. This deficit tends to zero. Truncated-exponential inverse-CDF coupling, dominated posterior moments and whitening transfer a strict violation to a compact isotropic law; continuity supplies an open time interval.',
        'proof_artifact': str(proof_path), 'independent_reviewer': 'w353',
        'remaining_gap': 'Independent audit pending of Claim A, retained-original-posterior weighting and the compact-isotropic limit. Does not refute actual (W), universal retention or the parent KLS statement. No novelty claim.',
        'status': 'sketch', 'proof_written': True, 'parent_problem_solved': False,
    },
    {
        'id': 'w350-C006',
        'statement': 'The rate-one exponential law on [0,infinity), and its translate Exp(1)-1, satisfy the Sobolev Poincare inequality with C_P<=4.',
        'assumptions': ['Finite variance and finite weighted derivative energy; other cases follow by the extended-energy interpretation'],
        'source': 'owner-own-work: explicit half-line Sobolev calculation in OPERATOR_WEIGHTED_COUNTEREXAMPLE.md section 1',
        'proof_or_counterexample': 'For centered h put g=h exp(-y/2). Energy equals ||g_prime||^2+(1/4)||g||^2-(1/2)g(0)^2. Centering implies integral g_prime exp(-y/2)=-g(0), so g(0)^2<=||g_prime||^2. Energy is at least variance/4. Weighted Sobolev cutoff/density extends the calculation.',
        'proof_artifact': str(proof_path), 'independent_reviewer': 'w353',
        'remaining_gap': 'Independent boundary/domain audit pending. This is a known special-case bound, with no novelty or general KLS claim.',
        'status': 'sketch', 'proof_written': True, 'parent_problem_solved': False,
    },
]
for row in new_rows:
    assert row['id'] not in {r['id'] for r in rows}, 'This staging script is single-use; do not resend review requests.'
    with (ROOT / 'CLAIMS.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps(row, ensure_ascii=False) + '\n')

source = {'source_id': 'owner-probability-campaign-w350-20261010:weighted-surrogate-counterexample', 'url': 'urn:owner-probability-campaign:P0017:w350:weighted-surrogate-counterexample', 'revision': '2026-10-10-draft-v1', 'license': 'owner-own-work; written derivation; independent review requested from w353', 'excerpt': None}
entries = [
    {'key': 'exponential-prior-bound', 'namespace': 'probability.core', 'logical_name': 'exponential-prior-poincare-bound-half-line-sobolev-draft', 'kind': 'concept', 'title': 'Exponential prior Poincare bound: explicit draft calculation', 'statement': 'AUTHOR PROOF DRAFT; independent review pending. The rate-one exponential law, and its centered translate Exp(1)-1, have C_P<=4. For centered h use g=h exp(-y/2), integrate by parts on the half-line and use g(0)^2<=integral g_prime^2 from the centering constraint. The complete boundary and Sobolev calculation is in OPERATOR_WEIGHTED_COUNTEREXAMPLE.md section 1. No novelty is claimed.', 'proof_text': None, 'assumptions': new_rows[1]['assumptions'], 'domain': 'probability theory', 'source': source},
    {'key': 'weighted-surrogate-counterexample', 'namespace': 'probability.core', 'logical_name': 'variance-weighted-posterior-operator-norm-surrogate-counterexample-draft', 'kind': 'concept', 'title': 'Draft obstruction to a variance-weighted posterior covariance surrogate', 'statement': 'AUTHOR COUNTEREXAMPLE DRAFT; independent review pending. In dimension one, no universal T>0 and finite K bound B_mu(t,f)=E[A_t Var(f(X)|Y_t)]/E Var(f(X)|Y_t) for all compact isotropic log-concave priors, all fixed smooth f and almost every t in (0,T), where Y_t=tX+sqrt(t)G and A_t=Var(X|Y_t). For the original prior X=Exp(1)-1 and f_c=exp(cx), B_mu(t,f_c) tends to 1/t as c increases to 1/2. Under the f_c^2 weighting used in the proof, A_t is still the ORIGINAL prior posterior variance. Truncation and whitening transfer a strict violation to compact priors and a time interval. This challenges the stronger operator-norm surrogate only; the actual estimate E|Cov_mu_t(f,X)|^2<=K E Var_mu_t(f) remains a separate unproved input. The full derivation and limit domination are in OPERATOR_WEIGHTED_COUNTEREXAMPLE.md. No parent solution or novelty claim is made.', 'proof_text': None, 'assumptions': new_rows[0]['assumptions'], 'domain': 'probability theory', 'source': source},
]
target = 'math:probability.core:open-problem-p0017-dimension-free-log-concave-poincare-or-cheeger-constant'
bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w350', 'bundle_slug': 'p0017-weighted-surrogate-obstruction-w350-003', 'entries': entries, 'relations': [
    {'from_key': 'weighted-surrogate-counterexample', 'to_key': 'exponential-prior-bound', 'kind': 'depends_on', 'rationale': 'The denominator is bounded below using the C_P<=4 special case and the Gaussian retention bridge.'},
    {'from_key': 'weighted-surrogate-counterexample', 'to_existing_logical': target, 'kind': 'semantic_association', 'rationale': 'The counterargument concerns an attempted sufficient surrogate input, and does not refute or solve the parent statement.'},
]}
save_json(ROOT / 'drafts' / 'bundle_003.json', bundle)
save_json(INBOX / 'bundle_003.part', bundle)
edges = read_rows(ROOT / 'RELATIONS.jsonl')
target_quote = next(e['to_statement_quote'] for e in edges if e.get('to_existing_logical') == target)
by_key = {e['key']: e for e in entries}
for rel in bundle['relations']:
    out = {'bundle_slug': bundle['bundle_slug'], **rel, 'from_statement_quote': by_key[rel['from_key']]['statement'], 'to_statement_quote': by_key[rel['to_key']]['statement'] if 'to_key' in rel else target_quote, 'status': 'prepared author-draft relation; unsubmitted and unreviewed'}
    with (ROOT / 'RELATIONS.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps(out, ensure_ascii=False) + '\n')

states = json.loads((ROOT / 'BUNDLE_STATES.json').read_text(encoding='utf-8'))
states['bundle_003'] = {'path': str(INBOX / 'bundle_003.part'), 'prepared': True, 'submitted': False, 'reviewed': 'Author counterexample and exponential-bound proof drafts; narrow independent audit requested from w353, pending.', 'ingested': False, 'retrievable': False, 'ingestion_verification': 'No integration receipt or retrieval run checked; the false flags mean unverified.'}
save_json(ROOT / 'BUNDLE_STATES.json', states)
packet = json.loads((ROOT / 'REVIEW_PACKET.json').read_text(encoding='utf-8'))
packet['bundle_states'] = states
packet['additional_author_drafts'] = new_rows
packet['additional_counterexample_scope'] = 'Only the stronger operator-norm variance-weighted surrogate. The actual covariance input (W), all-function VR and parent KLS are not refuted or solved.'
save_json(ROOT / 'REVIEW_PACKET.json', packet)
addition = '\nTwo further author draft claims are in OPERATOR_WEIGHTED_COUNTEREXAMPLE.md and unsubmitted bundle_003.part. The exponential-prior calculation gives C_P<=4; exponential test functions make the stronger variance-weighted posterior covariance ratio approach 1/t. A dominated truncation/whitening argument transfers strict violations to compact isotropic priors and a time interval. Independent review from w353 is pending. The actual covariance estimate (W) and all-function retention remain unproved in this packet.\n'
for name in ['REPORT.md', 'REVIEW_PACKET.md']:
    with (ROOT / name).open('a', encoding='utf-8') as f:
        f.write(addition + '\nNEXT: Audit the retained original posterior under f_c^2 weighting and the compact-isotropic transfer, alongside Claims A-B; do not substitute the stronger operator-norm bound for (W).\n')

hooks_path = ROOT / 'drafts' / 'math-w350.jsonl'
hooks = read_rows(hooks_path)
hooks.append({'id': 'math-w350-02', 'area': 'math', 'event': 'stage-start', 'cue': '(?i)(?:variance.weighted|weighted.{0,40}(?:covariance|operator.norm)|unweighted.{0,40}covariance)', 'fire_when': 'A variance-weighted covariance bound is inferred from an unweighted expectation or substituted for the actual conditional covariance estimate.', 'silent_when': 'The exact conditional expectation estimate has been proved with all dependence retained.', 'text': 'Keep covariance and test-function variance inside the same expectation. An unweighted covariance estimate does not control a variance-weighted one. Check rare-tail tests before replacing the actual covariance estimate by an operator-norm surrogate.', 'evidence': 'OPERATOR_WEIGHTED_COUNTEREXAMPLE.md: author draft gives a weighted ratio tending to 1/t; independent audit pending. Independently checked w349 posterior-factorization counterexample is in reviews/w349_verdicts.jsonl.', 'proposer': 'w350'})
hook_text = ''.join(json.dumps(h, ensure_ascii=False) + '\n' for h in hooks)
hooks_path.write_text(hook_text, encoding='utf-8')
patch = ''.join(difflib.unified_diff([], hook_text.splitlines(keepends=True), fromfile='a/~/primary_directive/hooks1000/proposals/math-w350.jsonl', tofile='b/~/primary_directive/hooks1000/proposals/math-w350.jsonl'))
(ROOT / 'patches' / '01_stale_status_hook.diff').write_text(patch, encoding='utf-8')
with (ROOT / 'STATUS.md').open('a', encoding='utf-8') as f:
    f.write('\n2026-10-10: Saved C005-C006, two concept draft cards and two evidence-quoted relations for the stronger weighted-surrogate counterargument. bundle_003.part is deliberately unsubmitted. Own reductions/counterargument still await independent review; actual (W) and all-function retention are not discharged.\n')

env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
messages = [
    ('w353', 'request', 'Narrow independent audit requested for my new author draft: ~/brain_workers/w350/OPERATOR_WEIGHTED_COUNTEREXAMPLE.md (C005-C006). Check the exponential CP<=4 boundary calculation, Claim A retention, ORIGINAL-posterior A_t under f_c^2 joint weighting, and dominated compact truncation/whitening limit. It challenges only E[A_t Var_t(f)]<=K E Var_t(f) on a universal initial interval; it does NOT refute the actual covariance (W) or KLS. Concept bundle_003.part remains unsubmitted. Please return KEEP/FIX/DROP with exact scope and proof gap.'),
    ('w349', 'message', 'Found a draft counterargument to the stronger operator-norm sufficient input in WEIGHTED_GAP.md: ~/brain_workers/w350/OPERATOR_WEIGHTED_COUNTEREXAMPLE.md. For Exp(1)-1 with f_c=exp(cx), weighted A_t Var_t(f) ratio tends to 1/t as c increases to 1/2; ORIGINAL posterior is retained under joint f_c^2 weighting. Compact isotropic transfer is written. Your actual covariance estimate (W) remains a separate unproved input and conditional-route KEEP is unchanged. Independent audit requested from w353; no audited theorem or novelty claim.'),
]
for recipient, kind, body in messages:
    p = subprocess.run([sys.executable, '-X', 'utf8', str(MESH), 'send', '--agent', 'w350', '--to', recipient, '--topic', 'P0017-proofswarm', '--kind', kind, '--body', body], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=45, env=env)
    receipt = {'recipient': recipient, 'kind': kind, 'body': body, 'returncode': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}
    with (ROOT / 'COMM_RECEIPTS.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps(receipt, ensure_ascii=False) + '\n')
    print(recipient, 'EXIT', p.returncode, p.stdout[:850], p.stderr[:250], flush=True)
print('SAVED: two new author-draft rows; two concepts remain unsubmitted; actual W unchanged.', flush=True)
