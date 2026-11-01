"""Validate and checkpoint research artifacts; optionally submit the authorized DRAFT."""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SUBMIT = '--submit' in sys.argv
def write(name, obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

claims = [json.loads(s) for s in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s]
proof_sha = hashlib.sha256((ROOT/'ATTEMPT.md').read_bytes()).hexdigest()
peer_path = Path('~/brain_workers/w475/AUDIT_ROWS.jsonl')
peer_rows = [json.loads(s) for s in peer_path.read_text(encoding='utf-8').splitlines() if s and 'w474-' in s] if peer_path.exists() else []
write('PEER_VERDICTS.json', {'source':str(peer_path),'rows':peer_rows,
      'author_attempt_sha256':proof_sha,'served_model_account_gate':'UNKNOWN',
      'note':'Receipt of scoped mathematical verdicts; no audit of the audit or served-identity inference.'})

evidence = json.loads((ROOT/'STORE_EVIDENCE.json').read_text(encoding='utf-8'))
evidence = [r for r in evidence if re.search(r'\bIsing\b',r['title'],re.I)]
write('STORE_EVIDENCE.json',evidence)
card = next(r for r in evidence if r['id']=='claim_db355f188daf0592950298d6e3b23e5f2b7e6eb0f3a21694083ad47fdadd0048')
meta = json.loads(card['metadata_json'])
corrected = (
    'AUTHOR ATTEMPT; no unconditional reduction certified. In the zero-field nearest-neighbor '
    'ferromagnetic Ising model, for four distinct sites the switching identity is '
    'U4(x1,x2,x3,x4)=-2 G(x1,x2) G(x3,x4) times the probability that the four source vertices '
    'are connected in the union of two independent currents with source pairs {x1,x2} and {x3,x4}. '
    'The source coupling is the full sum of U4(0,x2,x3,x4) divided by chi(beta)^2 xi(beta)^3 '
    'as beta increases to beta_c from below. Its nontriviality means this signed quantity does '
    'not tend to zero; since it is nonpositive, a positive subsequential lower bound on its '
    'negative is sufficient and equivalent to that non-limit-zero statement. A uniform '
    'unweighted intersection bound at every scale is stronger and is not established by '
    'the stated identity alone. A second-moment route still needs a justified second moment '
    'of the correctly sourced, weighted connectivity observable; a two-point conjecture or '
    'a heuristic cluster dimension is not an unconditional reduction. Current openness and '
    'novelty are not certified by this attempt.'
)
audit = {'row_id':'w474.S1.3','verdict':'FIX','status':'proposal; referee pending',
    'card_id':card['id'],'logical_id':meta.get('logical_id'),
    'current':{'title':card['title'],'body':card['body']},
    'corrected':{'title':'3D Ising nontriviality: weighted current identity and unclosed lower-bound obligation','body':corrected},
    'why':'The current concept asserts an unspecified uniform-in-scale equivalence. The source defines a beta-limit of a normalized summed coupling. Preserve the conditional variance obligation and remove the uncertified equivalence.',
    'source':{'url':'https://arxiv.org/pdf/1707.00520','locator':'Section 7, equations 7.1-7.2, Conjecture 6; Exercise 61.1',
              'target_quote':'Prove that the three-dimensional Ising model is non-trivial'},
    'independent_reviewer':'w476 requested; pending for this card correction',
    'application':'Coordinator must create a validated corrected revision and preserve provenance; do not edit a content-addressed object, export digest, or SQLite row directly.',
    'remaining_gap':'A model-specific weighted lower bound or fully sourced equivalence is still required; this source-fidelity proposal is not a C0052 proof.'}
write('SOURCE_CARD_AUDIT.json',audit)
if not any(r['claim_id']=='w474-C2' for r in claims):
    claims.append({'claim_id':'w474-C2','status':'sketch',
        'exact_statement':'The stored private reduction should not present an unspecified uniform-scale current-intersection lower bound as a certified equivalent of the source coupling limit; the source supplies a weighted four-point identity and a beta-limit definition, with the second-moment gap still open.',
        'assumptions':['source-fidelity audit of the specified concept','no claim that every possible uniform-scale equivalence is mathematically false'],
        'source':{'url':'https://arxiv.org/pdf/1707.00520','locator':'Section 7 equations 7.1-7.2; Exercise 61.1','card_id':card['id']},
        'proof_or_counterexample':'Compare the complete current card quoted in SOURCE_CARD_AUDIT.json with the source coupling and source-current identity. The unspecified uniform infimum is absent from that source definition; no derived averaged-to-uniform bridge was proved.',
        'independent_reviewer':'w476 (pending for C2)',
        'remaining_gap':'Coordinator source review and a justified weighted lower-bound argument; no live revision applied.'})
for claim in claims:
    if claim['claim_id'] != 'w474-C2':
        claim['independent_reviewer'] = 'w475 scoped KEEP received; w476 formal referee pending; served model/account gate UNKNOWN'
        claim['review_receipt'] = 'PEER_VERDICTS.json'
    required = {'claim_id','status','exact_statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap'}
    assert required <= claim.keys()
    assert claim['status'] in {'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
(ROOT/'CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in claims),encoding='utf-8')

bundle = json.loads((ROOT/'DRAFT_BUNDLE.json').read_text(encoding='utf-8'))
if not any(e['key']=='anchored-contact-mass' for e in bundle['entries']):
    bundle['entries'].append({
        'key':'anchored-contact-mass','namespace':'probability.ising',
        'logical_name':'exact-anchored-fourth-cumulant-contact-mass',
        'kind':'concept','title':'DRAFT: exact contact mass in the renormalized Ising coupling (scoped peer KEEP)',
        'statement':'AUTHOR PROOF DRAFT; w475 scoped mathematical KEEP, served identity and formal referee gates pending. Let sigma be a translation-invariant mean-zero +/-1 field on Z^3 or a finite abelian group, with 0<=G(x)=E[sigma_0 sigma_x]<=1 and finite chi=sum_x G(x). Put B=sum_x G(x)^2. For the ordered triples D such that (0,x2,x3,x4) has at least two equal sites, sum_D[-U4(0,x2,x3,x4)]=12chi^2-16chi-6B+12, between 0 and 12chi^2. Here U4 is the mean-zero fourth cumulant. For any xi>0 the contact contribution normalized by chi^2 xi^3 is at most 12/xi^3, and therefore vanishes if xi diverges. Since B<=chi, the unnormalized contact mass divided by chi^2 tends to 12 when chi diverges. The coefficient is sharp over the stated class, as N perfectly correlated spins on a cyclic group give 12N^2-22N+12. Exact coincident tuples only are controlled; the distinct-site mass required for C0052 is not lower-bounded.',
        'proof_text':None,
        'assumptions':['translation invariance','mean-zero +/-1 spins','nonnegative two-point function','finite susceptibility','xi>0 for the normalized assertion','exact coincidences only','formal referee/model gates pending'],
        'domain':'probability and statistical mechanics',
        'source':{'source_id':'owner-own-work:w474:C0052-boundary-2026-10-10','url':'file:///~/brain_workers/w474/ATTEMPT.md','revision':'2026-10-10-author-draft','license':'owner-own-work','excerpt':None}})
    bundle['relations'].append({'from_key':'anchored-contact-mass','to_key':'false-two-point-bridge','kind':'semantic_association',
        'rationale':'The bridge treats a nonzero on-site cumulant as evidence of a non-Gaussian scaling limit. The contact identity quantifies the vanishing of exact coincidences under the Ising coupling normalization; no vanishing of all distinct-site terms is inferred.'})
keys = {e['key'] for e in bundle['entries']}
for entry in bundle['entries']:
    assert entry['kind']=='concept' and entry['proof_text'] is None
    assert entry['source']['license']=='owner-own-work'
for edge in bundle['relations']:
    assert edge['from_key'] in keys and edge['to_key'] in keys
    assert edge['kind'] in {'depends_on','refutes','semantic_association'}
write('DRAFT_BUNDLE.json',bundle)
lines = (ROOT/'DRAFT_BUNDLE.json').read_text(encoding='utf-8').splitlines()
patch_dir = ROOT/'patches'
patch_dir.mkdir(exist_ok=True)
target = 'math-brain-inbox/w474/bundle_001.json'
patch = f'diff --git a/{target} b/{target}\nnew file mode 100644\n--- a/{target}\n+++ b/{target}\n@@ -0,0 +1,{len(lines)} @@\n'
(patch_dir/'01_ising_boundary_draft.diff').write_text(patch+'\n'.join('+'+line for line in lines)+'\n',encoding='utf-8')

lifecycle = json.loads((ROOT/'BUNDLE_LIFECYCLE.json').read_text(encoding='utf-8'))
lifecycle['reviewed'] = {'state':'partial: w475 scoped KEEP; w476 and served-identity gates pending','referee':'w476','verdict_path':str(peer_path)}
lifecycle['duplicate_handling'] = 'w475 independently derived L3 and explicitly left its anchored card to w474; w475 publishes weighted-block and path-sprinkling concepts instead.'
if SUBMIT:
    inbox = Path('~/math-brain-inbox/w474').resolve()
    inbox.mkdir(parents=True,exist_ok=True)
    final = inbox/'bundle_001.json'
    part = inbox/'bundle_001.part'
    assert final.resolve().parent==inbox and part.resolve().parent==inbox
    payload = (ROOT/'DRAFT_BUNDLE.json').read_text(encoding='utf-8')
    if final.exists():
        assert final.read_text(encoding='utf-8')==payload, 'Existing draft differs; preserve it.'
    else:
        part.write_text(payload,encoding='utf-8')
        part.rename(final)
    lifecycle['submitted']={'state':'submitted as DRAFT','path':str(final),'entries':len(bundle['entries']),'relations':len(bundle['relations'])}
write('BUNDLE_LIFECYCLE.json',lifecycle)

hook = {'id':'math-w474-c0052-01','area':'math','event':'stage-start',
    'cue':'A C0052 attempt infers nontriviality from an unweighted uniform current intersection or only a two-point exponent/local cumulant.',
    'fire_when':'The stored C0052 reduction is invoked without the beta-limit normalization and an adequate weighted second-moment bound.',
    'silent_when':'The correctly normalized four-distinct-site sum has a sourced lower bound and its probability/variance obligations are explicitly proved.',
    'text':'For Ising nontriviality, retain the source limit quantifier and chi^2 xi^3 normalization. Exact contacts contribute at most 12/xi^3. A two-point exponent or first intersection moment does not close the weighted variance gap; a passed sublemma is not the parent proof.',
    'evidence':'~/brain_workers/w474/ATTEMPT.md L2-L3; SOURCE_CARD_AUDIT.json w474.S1.3; scar perceptron_proof_open_gaps_fleet_2026_07_12',
    'proposer':'w474'}
assert len(hook['text'])<=300
(ROOT/'HOOK_PROPOSAL.jsonl').write_text(json.dumps(hook)+'\n',encoding='utf-8')

measured = json.loads((ROOT/'MEASUREMENTS.json').read_text(encoding='utf-8'))
report = f'''C0052 sharp boundary packet: exact source target recovered; parent problem not solved.

L1 proves the sharp Gaussian-sign residual bound. L2 constructs positively associated bounded spins with power-law correlations, on-site cumulant -2, and Gaussian smeared FDD limits. L3 gives exact contact mass 12chi^2-16chi-6B+12 and normalized bound 12/xi^3. This refutes only the broader auxiliary bridge, not nearest-neighbor Ising.

Measured receipts: one live unverified concept has an unsupported uniform-scale equivalence; SOURCE_CARD_AUDIT.json proposes a scoped correction. The diagnostic command was python -X utf8 ~/brain_workers/w474/check_boundaries.py. Its fresh gate held the run: status distress, reason process_critical, physical headroom 3252 MB, commit headroom 6951 MB. Zero numerical checks ran; no numerical before/after improvement or test pass is claimed. The deterministic diagnostics are saved for a safe later run.

w475 supplied scoped KEEP for L1-L3/C1 after an independent initial contact derivation. w476's formal referee decision and served model/account evidence remain pending. Proof statuses stay author-level; no formal-check receipt is claimed. Validation here covers JSON/schema/scope and the attached mathematical derivations, not a proof checker.

Brain lifecycle: {lifecycle['submitted']['state']}; {len(bundle['entries'])} concept/DRAFT entries, {len(bundle['relations'])} supported relations; mathematical review partial; ingestion not performed; retrieval unverified. w475 explicitly leaves the anchored contact card to this bundle. No live-store improvement is asserted before reviewed ingestion and recall verification.

Apply: the reviewer may use patches/01_ising_boundary_draft.diff with ~ as the path root to stage the DRAFT if missing; the validating coordinator integrates only after the required gates. SOURCE_CARD_AUDIT.json is a proposed new corrected revision, not a direct SQLite/content-addressed-object patch.

Limits: FDD convergence alone does not give fourth-moment convergence; exact contacts exclude distinct near-diagonal sites; the Gaussian-sign field has no established nearest-neighbor Ising Gibbs or random-current structure. Current global openness and novelty are UNKNOWN/unclaimed.

NEXT: w476 checks the proofs and source-card proposal; the next parent proof step is a weighted second-moment bound for the four-distinct-source current connectivity observable.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
review_files = {}
for name in ('ATTEMPT.md','CLAIMS.jsonl','SOURCE_STATUS.json','SOURCE_CARD_AUDIT.json','check_boundaries.py','MEASUREMENTS.json','COMPUTE_GATES.jsonl','REVIEW_PACKET.md'):
    review_files[name]={'path':str(ROOT/name),'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()}
write('REVIEW_FILES.json',{'purpose':'Freeze authored review files; not a brain digest/source manifest/store seal','files':review_files})
result_rows = [
    {'row_id':'w474.S1.2','kind':'source-status','target':'C0052','statement':'Signed source g(beta) not tending to zero is a subsequential nonvanishing criterion, not a certified uniform infimum over unweighted scale events.','source_quote':'Prove that the three-dimensional Ising model is non-trivial','source':'https://arxiv.org/pdf/1707.00520, eq7.1-7.2 and Conj6','reviewer':'w476 pending'},
    {'row_id':'w474.S1.3','kind':'source-card-audit','verdict':'FIX proposal','card_id':card['id'],'card_quote':'non-triviality (nonvanishing renormalised coupling) is equivalent to inf over scales L of P(two independent random-current clusters at scale L intersect) > 0.','source_quote':'Prove that the three-dimensional Ising model is non-trivial','evidence':'SOURCE_CARD_AUDIT.json','remaining_gap':'Scoped referee source check; no live revision applied.'},
    {'row_id':'w474.S1.4','kind':'proof-packet','claim_ids':['w474-L1','w474-L2','w474-L3','w474-C1'],'evidence':'ATTEMPT.md and CLAIMS.jsonl','review':'w475 scoped KEEP; w476 formal referee and served gate pending','parent_problem_solved':False,'single_hardest_gap':'Normalized four-distinct-site weighted current lower bound.'},
    {'row_id':'w474.S1.5','kind':'draft-submission','evidence':lifecycle['submitted']['path'],'state':lifecycle['submitted']['state'],'entries':len(bundle['entries']),'relations':len(bundle['relations']),'ingested':False,'retrievable':'unverified','numerical_diagnostics':'DEFERRED by fresh process_critical gate'}
]
existing = (ROOT/'RESULTS.jsonl').read_text(encoding='utf-8')
with (ROOT/'RESULTS.jsonl').open('a',encoding='utf-8') as out:
    for row in result_rows:
        if row['row_id'] not in existing:
            out.write(json.dumps(row,ensure_ascii=False)+'\n')
print(json.dumps({'submitted':SUBMIT,'entries':len(bundle['entries']),'relations':len(bundle['relations']),
                  'claims':len(claims),'peer_verdicts':len(peer_rows),'author_attempt_sha256':proof_sha,
                  'numerical_diagnostics':'DEFERRED','source_card_fix':'proposal only'}))
