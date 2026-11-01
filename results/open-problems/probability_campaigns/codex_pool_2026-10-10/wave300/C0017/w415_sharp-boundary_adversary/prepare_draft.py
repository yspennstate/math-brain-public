"""Validate locally, publish only the explicitly permitted worker draft, and save receipts."""
from datetime import datetime, timezone
import difflib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w415').resolve()

def source(key):
    return {'source_id': 'owner-own-work:w415:' + key,
            'url': 'file:///~/brain_workers/w415/ATTEMPT.md',
            'revision': '2026-10-10-draft-referee-pending',
            'license': 'owner-own-work', 'excerpt': None}

def entry(key, logical, title, statement, assumptions):
    return {'key': key, 'namespace': 'probability.percolation', 'logical_name': logical,
            'kind': 'concept', 'title': title, 'statement': statement,
            'proof_text': None, 'assumptions': assumptions,
            'domain': 'critical planar percolation; boundary approximation', 'source': source(key)}

bundle = {
    'spec': 'mathbrain-draft-v1', 'author_agent': 'w415',
    'bundle_slug': 'c0017-boundary-quantifiers-w415-001',
    'entries': [
        entry('uniform-bridge', 'unrestricted-uniform-cardy-domain-bridge',
              'Unrestricted uniform Cardy approximation: refuted draft auxiliary bridge',
              'DRAFT AUXILIARY PROPOSAL, REFEREE CHECK PENDING: for free critical bond percolation on the graph induced by delta Z^2 in the closure of each marked Jordan rectangle Q, the proposed bound sup_Q |P_delta(H_Q)-Cardy(Q)| -> 0 as delta -> 0 ranges over all positive-size Q, including Q that shrink with delta. This is stronger than convergence for each fixed marked domain. The two-bond boundary construction contradicts this proposed bound under the stated discretization. This auxiliary proposal is not the fixed-domain C0017 target.',
              ['Independent Bernoulli(1/2) bonds and free boundary conditions.',
               'Boundary contacts are induced-graph vertices on the two designated opposite sides.',
               'Q may depend on delta and no relative-mesh condition is imposed.']),
        entry('two-bond-witness', 'two-bond-obstruction-to-uniform-cardy-approximation',
              'Two-bond rectangle obstruction to uniform Cardy approximation: draft',
              'DRAFT AUTHOR DERIVATION; INDEPENDENT REVIEW BY w416 PENDING. Let delta>0 and take Q_delta=(0,2 delta) x (-delta/2,delta/2), marked at its corners. Its closed-rectangle induced delta Z^2 graph has exactly three vertices and two bonds, so free Bernoulli(1/2) left-to-right crossing probability is exactly 1/4. For horizontal aspect ratio 2, Cardy has cross ratio x=(sqrt(2)-1)^4 and value C(x)=B_x(1/3,1/3)/B(1/3,1/3). Since x<1/32, the beta-integral bounds give C(x)<(8/961)^(1/3)<1/4. Thus the approximation error exceeds 1/4-(8/961)^(1/3)>0 at every delta. This refutes only an unrestricted uniform-domain auxiliary assertion. The relative mesh delta/height(Q_delta)=1; no fixed-domain Cardy limit or C0017 solution is refuted or proved.',
              ['Induced graph includes boundary vertices in the closed rectangle.',
               'The two distinct bonds are independent; no conditional-product estimate is used.',
               'Horizontal Cardy aspect is width/height=K(1-x)/K(x), with K the elliptic parameter integral.',
               'Cardy is a comparison function here; its square-bond scaling-limit identification is not assumed.']),
        entry('quantifier-guard', 'cardy-limit-fixed-domain-and-relative-mesh-guard',
              'Quantifier guard for Cardy boundary-limit arguments: draft concept',
              'DRAFT SCOPE GUARD FOR C0017: pointwise convergence in mesh for each fixed marked Jordan domain does not provide a supremum bound over arbitrary domains that vary with the mesh. The two-bond rectangle has a persistent positive crossing discrepancy because the mesh never becomes fine relative to its height. Keep the marked domain fixed or state and prove suitable quantitative family hypotheses. For more general varying domains, unmarked interior convergence and Euclidean boundary-mark convergence do not automatically preserve marked prime ends. These are necessary scope checks, not a theorem asserting that any proposed list of conditions suffices. Correctly marked square-bond Cardy/SLE(6) limit identification remains the hardest unresolved step in this packet.',
              ['The counterexample concerns the explicitly stated free induced-graph convention.',
               'No sufficiency claim for diameter normalization or boundary regularity is made.',
               'Author result is not independently checked or promoted to theorem status.'])],
    'relations': [
        {'from_key': 'two-bond-witness', 'to_key': 'uniform-bridge', 'kind': 'refutes',
         'rationale': 'Draft relation pending referee check. The source end gives an error exceeding the positive constant 1/4-(8/961)^(1/3) for Q_delta at every delta. The target end proposes sup_Q |P_delta(H_Q)-Cardy(Q)| -> 0 over all sizes, which includes Q_delta. This relation targets that auxiliary supremum, never C0017 itself.'},
        {'from_key': 'quantifier-guard', 'to_key': 'two-bond-witness', 'kind': 'depends_on',
         'rationale': 'The guard distinguishes each fixed domain from arbitrary mesh-dependent domains. Its explicit supporting example is the two-bond rectangle with delta/height=1 and a persistent positive discrepancy.'}]
}

keys = {item['key'] for item in bundle['entries']}
assert len(keys) == len(bundle['entries']) <= 200
required = {'key', 'namespace', 'logical_name', 'kind', 'title', 'statement',
            'proof_text', 'assumptions', 'domain', 'source'}
for item in bundle['entries']:
    assert required <= item.keys()
    assert item['kind'] == 'concept' and item['proof_text'] is None
    assert item['statement'].startswith('DRAFT')
    assert re.fullmatch(r'[a-z][a-z0-9-]*', item['logical_name'])
    assert re.fullmatch(r'[a-z]+(?:\.[a-z]+)+', item['namespace'])
    assert item['source']['license'].startswith('owner-own-work')
for relation in bundle['relations']:
    assert relation['from_key'] in keys and relation['to_key'] in keys
    assert relation['kind'] in ('refutes', 'depends_on')
# Only one depends_on edge, so the dependency graph is acyclic.
assert sum(relation['kind'] == 'depends_on' for relation in bundle['relations']) == 1

hook = {
    'id': 'cardy-boundary-w415-01', 'area': 'math', 'event': 'stage-start',
    'cue': '(?is)(uniform.{0,50}(domain|Jordan|crossing)|sup.{0,30}(domain|Jordan))',
    'fire_when': 'Claim a uniform crossing limit over all mesh-dependent Jordan domains.',
    'silent_when': 'Prove the crossing limit for one fixed regular marked domain.',
    'text': 'Before a uniform crossing-limit claim, state relative-mesh and marked-prime-end assumptions. A two-bond rectangle keeps probability 1/4 while the aspect-2 Cardy value is about .176. A fixed-domain limit cannot justify a supremum over all domains.',
    'evidence': '~/brain_workers/w415/ATTEMPT.md, boundary-002; MEASUREMENTS.json: 6 exact graph cases, discrepancy 0.0743531062; ADVERSE boundary scope independently derived.',
    'proposer': 'w415'}
assert len(hook['text']) <= 300
controls = {'fire': bool(re.search(hook['cue'], hook['fire_when'])),
            'silent': bool(re.search(hook['cue'], hook['silent_when']))}
assert controls == {'fire': True, 'silent': False}

draft_dir = ROOT / 'draft'
patch_dir = ROOT / 'patches'
draft_dir.mkdir(exist_ok=True)
patch_dir.mkdir(exist_ok=True)
body = json.dumps(bundle, indent=2, ensure_ascii=False) + '\n'
local_path = draft_dir / 'bundle_001.json'
local_path.write_text(body, encoding='utf-8')
hook_body = json.dumps(hook, ensure_ascii=False) + '\n'
(ROOT / 'HOOK_PROPOSAL.jsonl').write_text(hook_body, encoding='utf-8')
(ROOT / 'HOOK_CONTROLS.json').write_text(json.dumps(controls, indent=2), encoding='utf-8')

assert INBOX == Path('~/math-brain-inbox/w415').resolve()
INBOX.mkdir(exist_ok=True)
for index in range(1, 1000):
    final = (INBOX / f'bundle_{index:03d}.json').resolve()
    part = (INBOX / f'bundle_{index:03d}.json.part').resolve()
    assert final.parent == INBOX and part.parent == INBOX
    if not final.exists() and not part.exists():
        break
else:
    raise RuntimeError('No new draft filename available; nothing overwritten')
with part.open('x', encoding='utf-8', newline='\n') as stream:
    stream.write(body)
# Windows rename fails if another author created final meanwhile; never overwrite.
part.rename(final)
assert json.loads(final.read_text(encoding='utf-8')) == bundle

for filename, live_path, content in (
        ('01_C0017_boundary_bundle.diff', final.as_posix(), body),
        ('02_C0017_boundary_hook.diff',
         '~/primary_directive/hooks1000/proposals/math-boundary-w415.jsonl', hook_body)):
    patch = ''.join(difflib.unified_diff([], content.splitlines(keepends=True),
                                      fromfile='a/' + live_path, tofile='b/' + live_path))
    (patch_dir / filename).write_text(patch, encoding='utf-8')

receipt = {
    'submitted': True, 'submitted_at_utc': datetime.now(timezone.utc).isoformat(),
    'inbox_path': final.as_posix(), 'local_draft_path': local_path.as_posix(),
    'entry_count': len(bundle['entries']), 'relation_count': len(bundle['relations']),
    'theorem_or_lemma_entries': 0, 'local_schema_checks_passed': True,
    'coordinator_validator_run': False, 'reviewed': False, 'ingested': False,
    'retrievable': False, 'live_store_mutated': False,
    'hook_submitted': False, 'hook_local_path': (ROOT / 'HOOK_PROPOSAL.jsonl').as_posix(),
    'hook_control_results': controls,
    'note': 'Only draft submission is complete. Referee review and integration are separate states. Global hook proposal is staged locally under the worker write restriction.'}
(ROOT / 'BRAIN_SUBMISSION.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(receipt, indent=2))
