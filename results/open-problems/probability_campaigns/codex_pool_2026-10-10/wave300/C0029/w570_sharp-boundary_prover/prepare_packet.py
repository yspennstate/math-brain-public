"""Prepare review-only math-brain drafts and a scoped source correction."""
from datetime import datetime, timezone
import difflib
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w570')
HOOKS = Path('~/primary_directive/hooks1000/proposals/math-w570.jsonl')
ATTEMPTS = Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl')


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


attempt = (ROOT / 'ATTEMPT.md').read_text(encoding='utf-8')
claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
names = {
    'P1': 'bernoulli-projective-row-column-partition-count',
    'P2': 'bernoulli-projective-row-column-collision-probability',
    'P3': 'bernoulli-collision-atom-forbids-fixed-two-power-remainder',
    'P4': 'bernoulli-corank-one-without-projective-pair-collisions'
}
titles = {
    'P1': 'DRAFT: exact simultaneous projective collision constraints',
    'P2': 'DRAFT: exact probability of projective row or column collision',
    'P3': 'DRAFT: collision atom and an impossible exponential endpoint',
    'P4': 'DRAFT: a corank-one sign matrix without pair collisions'
}


def source(key):
    return {'source_id': 'owner-probability-campaign-w570:' + key,
            'url': None, 'revision': 'author-proof-20261010-review-pending',
            'license': 'owner-own-work', 'excerpt': None}


def concept(key, logical, title, statement):
    return {'key': key, 'namespace': 'probability.random-matrices', 'logical_name': logical,
            'kind': 'concept', 'title': title, 'statement': statement, 'proof_text': None,
            'assumptions': [], 'domain': 'probability theory', 'source': source(key)}


entries = [concept('exact-target', 'spielman-teng-exact-one-bernoulli-target-scope',
                   'CONJECTURE: exact-one Spielman-Teng target and scope',
                   'For a real n by n matrix B_n with mutually independent uniform {-1,1} entries, the exact-one target asks for one c in (0,1) such that P(s_min(B_n)<=epsilon/sqrt(n))<=epsilon+c^n for every n>=1 and epsilon>=0. Current openness is UNKNOWN. Sah-Sahasrabudhe-Sawhney, arXiv:2405.20308v2 Theorem 1.1, prove a coefficient 1+O((log n)^(-1/16)), which does not by itself prove exact one. The original source is Spielman-Teng ICM 2002 Conjecture 2, p.605. These results do not extend an exact-one assertion to arbitrary entry laws or deterministic shifts.'),
           concept('collision-event', 'bernoulli-projective-pair-collision-event',
                   'Projective pair collision event for a sign matrix',
                   'For a sign matrix B_n, E_n means that some two distinct rows or some two distinct columns agree up to a global sign. E_n implies singularity by a left or right kernel vector supported on two coordinates. The converse is false; E_n is a specified subset of singularity, not all singularity.'),
           concept('sparse-bridge', 'rejected-two-coordinate-witness-bridge-for-sign-matrices',
                   'REJECTED bridge: every singular sign matrix has a two-coordinate witness',
                   'The proposed universal bridge is: every singular real sign matrix has a left or right nonzero kernel vector supported on at most two coordinates. This bridge is false even for corank-one matrices of every dimension n>=5. A counterexample to this bridge is not a refutation of the Spielman-Teng conjecture.')]

for key in ('P1', 'P2', 'P3', 'P4'):
    c = next(c for c in claims if c['id'].endswith('-' + key))
    section = attempt.split('## ' + key + ':', 1)[1].split('\n## ', 1)[0]
    statement = c['statement']
    if key in ('P1', 'P2', 'P3'):
        statement = 'Let B_n be n by n with mutually independent uniform {-1,1} entries. Let E_n mean that some two rows or some two columns agree up to sign. ' + statement
    if key == 'P4':
        statement = statement.replace('uniform-sign-support matrix', 'real {-1,1} matrix')
    entries.append({'key': key, 'namespace': 'probability.random-matrices',
                    'logical_name': names[key], 'kind': 'lemma', 'title': titles[key],
                    'statement': 'AUTHOR PROOF; INDEPENDENT REVIEW PENDING. ' + statement,
                    'proof_text': section.strip(), 'assumptions': [c['assumptions']],
                    'domain': 'probability theory', 'source': source(key)})

entries.append(concept('gaussian-scope-correction', 'gaussian-hard-edge-limit-is-not-finite-size-cdf',
                       'CORRECTION: Gaussian hard-edge limit versus finite-size CDF',
                       'For G_1=[Z] with Z standard normal, P(s_min(G_1)<=t)=erf(t/sqrt(2)) for t>=0; its derivative at zero is sqrt(2/pi). Thus 1-exp(-t-t^2/2) is not the exact finite-n Gaussian least-singular-value CDF. It is the limiting CDF as n tends to infinity (Rudelson-Vershynin ICM 2010 survey). The finite-n bound P(s_min(G_n)<=t/sqrt(n))<=t is a separate statement. This corrects only the exact-law sentence in the 2026-09-07 C0029 attempt record.'))

relations = [
    {'from_key': 'P2', 'to_key': 'P1', 'kind': 'depends_on', 'rationale': 'P2 sums P1 joint partition probabilities with signed Stirling weights.'},
    {'from_key': 'P3', 'to_key': 'P1', 'kind': 'depends_on', 'rationale': 'P3 uses P1 one- and two-pair intersection probabilities in Bonferroni bounds.'},
    {'from_key': 'P2', 'to_key': 'collision-event', 'kind': 'cites', 'rationale': 'The probability in P2 is exactly the event E_n defined here.'},
    {'from_key': 'P3', 'to_key': 'collision-event', 'kind': 'cites', 'rationale': 'The lower singular atom comes from E_n, a subset of singularity.'},
    {'from_key': 'P4', 'to_key': 'sparse-bridge', 'kind': 'refutes', 'rationale': 'P4 constructs singular sign matrices of rank n-1 with no two-coordinate left or right witness; it refutes this bridge only.'},
    {'from_key': 'P4', 'to_key': 'collision-event', 'kind': 'cites', 'rationale': 'P4 lies outside E_n and verifies why E_n is not all singularity.'},
    {'from_key': 'gaussian-scope-correction', 'to_existing_logical': 'math:probability.random-matrices:attempt-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr', 'kind': 'refutes', 'rationale': 'Scope: refutes only the asserted exact finite-n Gaussian CDF sentence; the prior attempt itself remains an attempted-unsolved record.'}
]
bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w570',
          'bundle_slug': 'probability-bernoulli-c0029-sharp-boundary-w570-20261010',
          'entries': entries, 'relations': relations}
required = {'key', 'namespace', 'logical_name', 'kind', 'title', 'statement', 'proof_text', 'assumptions', 'domain', 'source'}
assert all(required <= e.keys() for e in entries)
assert all(e['proof_text'] if e['kind'] in {'lemma', 'theorem'} else e['proof_text'] is None for e in entries)
assert len({e['key'] for e in entries}) == len(entries)
keys = {e['key'] for e in entries}
assert all(r['from_key'] in keys and (r.get('to_key') in keys or 'to_existing_logical' in r) for r in relations)
INBOX.mkdir(parents=True, exist_ok=True)
final = INBOX / 'bundle_001.json'
payload = json.dumps(bundle, indent=2, ensure_ascii=False) + '\n'
existing = json.loads(final.read_text(encoding='utf-8')) if final.exists() else None
if existing is not None:
    assert existing['author_agent'] == 'w570' and existing['bundle_slug'] == bundle['bundle_slug'], 'Refusing to overwrite another artifact'
if existing != bundle:
    part = INBOX / 'bundle_001.part'
    assert not part.exists(), 'Preserving an existing unfinished draft'
    part.write_text(payload, encoding='utf-8')
    part.replace(final)
write_json(ROOT / 'DRAFT_STATUS.json', {'bundle': str(final), 'entries': len(entries), 'relations': len(relations),
                                       'submitted': True, 'reviewed': False, 'ingested': False, 'retrievable': False,
                                       'independent_reviewer': 'w572', 'served_model_gate': 'UNKNOWN / not met',
                                       'integration': 'Coordinator only; do not run integrator before proof/model gates.'})
write_json(ROOT / 'RELATION_EVIDENCE.json', [{'relation': r,
              'from_statement': next(e['statement'] for e in entries if e['key'] == r['from_key']),
              'to_statement': next((e['statement'] for e in entries if e['key'] == r.get('to_key')), 'Existing attempt node: false exact finite-n law; see ATTEMPT.md prior digest.'),
              'review_status': 'PENDING'} for r in relations])

old_line = None
line_number = None
with ATTEMPTS.open(encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'C0029-A001' in line:
            old_line, line_number = line, i
            break
assert old_line is not None
old = json.loads(old_line)
old['scope_correction_w570_20261010'] = (
    'The stated equality 1-exp(-t-t^2/2) is the n->infinity Gaussian hard-edge limit, not an exact finite-n law. '
    'At n=1 the exact CDF is erf(t/sqrt(2)), with slope sqrt(2/pi). '
    'SSS arXiv:2405.20308v2 Theorem 1.1 now gives 1+O((log n)^(-1/16)) uniformly over epsilon>=0; exact one is not concluded. '
    'Historical author result preserved verbatim; correction pending independent review.')
new_line = json.dumps(old, ensure_ascii=False) + '\n'
header = str(ATTEMPTS).replace('\\', '/')
diff = ''.join(difflib.unified_diff([old_line], [new_line], fromfile='a/' + header, tofile='b/' + header, n=0))
diff = diff.replace('@@ -1 +1 @@', f'@@ -{line_number} +{line_number} @@')
(ROOT / 'patches').mkdir(exist_ok=True)
(ROOT / 'patches/01_C0029_gaussian_scope.diff').write_text(diff, encoding='utf-8')
write_json(ROOT / 'STORE_CORRECTION.json', {'target_claim_id': 'claim_cbd6e1bc44ea67c88a3ad2112abab63bbfcf63f991be2eeccb063fdba514f1fa',
    'target_logical_id': 'math:probability.random-matrices:attempt-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr',
    'correction': old['scope_correction_w570_20261010'], 'review_status': 'PENDING', 'live_store_changed': False,
    'source_record_patch': str(ROOT / 'patches/01_C0029_gaussian_scope.diff')})

hook = {'id': 'C0029-w570-01', 'area': 'math', 'event': 'PreToolUse',
        'cue': 'An argument uses a limiting distribution as an exact finite-size probability law',
        'fire_when': 'C0029-A001 calls 1-exp(-t-t^2/2) the exact Gaussian finite-n CDF',
        'silent_when': 'The argument explicitly takes n to infinity before using the limiting CDF',
        'text': 'When importing a limiting law into a finite-size proof, check n=1 or another explicit boundary. Preserve the order of limits and distinguish an exact finite-n bound from an asymptotic CDF.',
        'evidence': str(ROOT / 'ATTEMPT.md') + ' prior-attempt digest; n=1 CDF erf(t/sqrt(2))', 'proposer': 'w570'}
assert len(hook['text']) <= 300
HOOKS.parent.mkdir(parents=True, exist_ok=True)
already = HOOKS.read_text(encoding='utf-8') if HOOKS.exists() else ''
if hook['id'] not in already:
    with HOOKS.open('a', encoding='utf-8') as f:
        f.write(json.dumps(hook, ensure_ascii=False) + '\n')

print(json.dumps({'draft': str(final), 'entries': len(entries), 'relations': len(relations),
                  'integrated': False, 'hook': hook['id'], 'patch_line': line_number}))
