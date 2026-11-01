"""Prepare local drafts and reviewer-applied diffs; never write outside this folder."""
from pathlib import Path
import difflib
import json
import shutil

ROOT = Path(__file__).resolve().parent
measurements = json.loads((ROOT / 'MEASUREMENTS.json').read_text(encoding='utf-8'))
assert measurements['failed'] == 0 and measurements['checks_passed'] == 46
card = json.loads((ROOT / 'CARD_EVIDENCE.json').read_text(encoding='utf-8'))['rows'][0]
existing = card['logical_id']

own_source = {
    'source_id': 'owner-own-work:w424:C0023-obstructions-20261010',
    'url': 'file:///~/brain_workers/w424/INDEPENDENT_DERIVATION.md',
    'revision': 'author-written-2026-10-10-draft-unreviewed',
    'license': 'owner-own-work',
    'excerpt': 'The counterexample is a nontransitive tree, not Z^d.'
}


def entry(key, name, title, statement, assumptions, source):
    return {'key': key, 'namespace': 'probability.percolation', 'logical_name': name,
            'kind': 'concept', 'title': title, 'statement': statement,
            'proof_text': None, 'assumptions': assumptions,
            'domain': 'probability theory', 'source': source}


tree = entry(
    'tree-jump', 'draft-dyadic-branching-bounded-degree-critical-jump',
    'DRAFT: a bounded-degree nontransitive tree can percolate at criticality',
    'DRAFT, author-written and not independently reviewed. Let T be the rooted tree '
    'where every generation k-1 vertex has 8 children if k is a power of 2 and 2 '
    'children otherwise, k>=1. For independent Bernoulli bond percolation on T, '
    'the maximum degree is 9, p_c(T)=1/2 and theta_T(1/2)>=4/5. Writing Z_n for '
    'root-connected generation-n vertices, E[Z_n]=(2p)^n 4^(1+floor(log_2 n)), '
    'and at p=1/2 the normalized second moment is at most 5/4. This explicitly '
    'refutes a general critical-nonpercolation inference based only on independence, '
    'finite energy, bounded degree and finite-event continuity. T is not '
    'quasi-transitive and this is not a counterexample to the Z^d conjecture.',
    ['The stated nontransitive rooted tree', 'Independent Bernoulli bonds',
     'No claim of critical uniqueness', 'Independent referee check pending'], own_source)

window = entry(
    'narrow-window', 'draft-dyadic-tree-narrow-backward-window-survival',
    'DRAFT: a shrinking subcritical window can preserve finite-generation survival',
    'DRAFT, author-written and not independently reviewed. For the explicit '
    'dyadic-branching tree with 8 children at power-of-two generations and 2 '
    'otherwise, let f_n(p)=P_p(Z_n>0). For 0<p_n=1/2-delta_n<1/2, '
    'f_n(p_n)>=4/5-delta_n n/p_n. Indeed open pivotal edges lie on any '
    'root-to-level-n path, so their number is at most n and finite-product '
    'differentiation gives f_n_prime(p)<=n/p. Therefore delta_n n->0 '
    'cannot also make f_n(p_n)->0. Finite-volume continuity and subcritical '
    'vanishing at each fixed parameter do not license exchanging these limits.',
    ['The same explicit tree', 'Finite increasing survival events',
     '0<p_n<1/2', 'Independent referee check pending'], own_source)

gap_source = dict(own_source)
gap_source['source_id'] = 'owner-own-work:w424:C0023-w423-quantifier-audit-20261010'
gap_source['url'] = 'file:///~/brain_workers/w424/ADVERSARIAL_REVIEW.md'
gap_source['excerpt'] = 'A bound at p_c alone, or a different a_n for every n, does not suffice.'
gap = entry(
    'interval-gap', 'draft-critical-percolation-fixed-backward-interval-proof-obligation',
    'DRAFT: the fixed backward interval is the open proof obligation',
    'DRAFT audit concept, not a proof of critical nonpercolation. For independent '
    'nearest-neighbour Bernoulli bonds on Z^d, define A_n as origin-to-boundary '
    'connection inside [-n,n]^d, f_n(p)=P_p(A_n), and lambda_n(p) as the '
    'conditional expected number of open pivotal edges given A_n. For '
    '0<a<b<1, log(f_n(b)/f_n(a))=integral_a^b lambda_n(s)/s ds. Under a '
    'hypothetical theta(p_c)>0, ruling out a critical jump via this identity '
    'requires a finite liminf of that integral on one fixed [a,p_c] with '
    'a<p_c, or another rigorously derived geometric mechanism. Endpoint '
    'bounds and intervals shrinking with n do not establish this premise. '
    'w423 states the premise explicitly and has not proved it for the lattice.',
    ['Independent nearest-neighbour Bernoulli bond model',
     'Finite increasing connection events', '0<a<p_c<1',
     'The claimed lattice estimate is unproved'], gap_source)

bundle = {
    'spec': 'mathbrain-draft-v1', 'author_agent': 'w424',
    'bundle_slug': 'w424-c0023-critical-jump-obstructions-draft-001',
    'entries': [tree, window, gap],
    'relations': [
        {'from_key': 'narrow-window', 'to_key': 'tree-jump', 'kind': 'depends_on',
         'rationale': 'The narrow-window survival lower bound uses the explicit tree and its critical 4/5 lower bound.'},
        {'from_key': 'interval-gap', 'to_key': 'narrow-window', 'kind': 'analogous_to',
         'rationale': 'The tree exhibits failure of exchanging parameter and scale limits; the lattice criterion requires a fixed interval. This is an analogy, not a proof transfer.'},
        {'from_key': 'tree-jump', 'to_existing_logical': existing, 'kind': 'semantic_association',
         'rationale': 'The bounded-degree nontransitive counterexample tests unrestricted inferences used when approaching C0023; it neither refutes nor proves the Z^d claim.'},
        {'from_key': 'interval-gap', 'to_existing_logical': existing, 'kind': 'semantic_association',
         'rationale': 'The exact missing fixed-interval premise concerns attempts to prove the C0023 critical bond statement; its validity on Z^d remains open in this packet.'}
    ]
}

hook = {
    'id': 'critical-limit-w424-01', 'area': 'math', 'event': 'stage-start',
    'cue': 'A proposed critical-nonpercolation proof uses continuity of finite-volume probabilities to exchange the parameter and infinite-volume limits without a uniform estimate.',
    'fire_when': 'A proposed inference says finite-scale continuity plus vanishing below p_c implies theta(p_c)=0; h_n(p)=min(1,(2p)^n) is a saved counterexample to that inference.',
    'silent_when': 'w423 L2 explicitly leaves the fixed-interval domination unproved; or a proof supplies and verifies the required uniform estimate.',
    'text': 'Write the order of limits and fix the parameter interval. Finite-volume continuity does not exclude a critical jump. Check the uniform estimate and all graph hypotheses before concluding theta(p_c)=0.',
    'evidence': 'w424/INDEPENDENT_DERIVATION.md; w424/MEASUREMENTS.json (46 checks); brain scar proof_steps_need_derived_joint_structure_2026_09_09',
    'proposer': 'w424'
}
assert len(hook['text']) <= 300

required = {'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
keys = {x['key'] for x in bundle['entries']}
assert len(keys) == len(bundle['entries']) == 3
for x in bundle['entries']:
    assert required <= x.keys()
    assert x['kind'] == 'concept' and x['proof_text'] is None
    assert x['statement'].startswith('DRAFT')
    assert x['source']['license'].startswith('owner-own-work')
for rel in bundle['relations']:
    assert rel['from_key'] in keys
    assert rel['kind'] in {'depends_on', 'analogous_to', 'semantic_association'}
    assert rel.get('to_key') in keys or rel.get('to_existing_logical') == existing
# Only one depends_on edge, with distinct endpoints: there is no dependency cycle.
assert [(r['from_key'], r['to_key']) for r in bundle['relations'] if r['kind']=='depends_on'] == [('narrow-window', 'tree-jump')]

outdir = ROOT / 'drafts'
outdir.mkdir(exist_ok=True)
bundle_text = json.dumps(bundle, indent=2, ensure_ascii=False) + '\n'
hook_text = json.dumps(hook, ensure_ascii=False) + '\n'
(outdir / 'bundle_001.json').write_text(bundle_text, encoding='utf-8')
(outdir / 'critical-limit-w424.jsonl').write_text(hook_text, encoding='utf-8')

patchdir = ROOT / 'patches'
patchdir.mkdir(exist_ok=True)
patches = ''
for live_path, content in (
    ('math-brain-inbox/w424/bundle_001.json', bundle_text),
    ('primary_directive/hooks1000/proposals/critical-limit-w424.jsonl', hook_text)
):
    patches += ''.join(difflib.unified_diff([], content.splitlines(keepends=True),
                     fromfile='a/' + live_path, tofile='b/' + live_path))
(patchdir / '01_critical_limit_drafts.diff').write_text(patches, encoding='utf-8')

relations = []
entries_by_key = {x['key']: x for x in bundle['entries']}
for r in bundle['relations']:
    target = entries_by_key[r['to_key']] if 'to_key' in r else card
    relations.append({'relation': r, 'from_quote': entries_by_key[r['from_key']]['statement'],
                      'to_quote': target.get('statement', target.get('body')), 'status': 'DRAFT, review pending'})
(ROOT / 'RELATIONS.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in relations),encoding='utf-8')

verdicts = [
    {'claim_id': 'w423.S1.1', 'verdict': 'KEEP', 'scope': 'finite-event identity with all stated assumptions'},
    {'claim_id': 'w423.S1.2', 'verdict': 'KEEP', 'scope': 'conditional criterion only; the lattice premise remains unproved'},
    {'claim_id': 'w423.S1.3', 'verdict': 'KEEP', 'scope': 'the stated nontransitive unbounded-degree graph only'}
]
for v in verdicts:
    v.update({'auditor':'w424','proof_file':'~/brain_workers/w423/LEMMAS.md',
              'evidence':'ADVERSARIAL_REVIEW.md','C0023_proved':False})
(ROOT / 'AUDIT_VERDICTS.jsonl').write_text(''.join(json.dumps(v)+'\n' for v in verdicts),encoding='utf-8')

states = {'prepared': True, 'submitted': False, 'reviewed': False,
          'ingested': False, 'retrievable': False,
          'schema_checked_locally': True, 'integrator_run': False,
          'entries': 3, 'relations': 4, 'hook_proposals': 1,
          'integration_condition': 'w425 independently checks own new calculations; coordinator applies the diff and validates the draft without promoting unreviewed concepts to theorems.'}
(ROOT / 'SUBMISSION_STATE.json').write_text(json.dumps(states,indent=2)+'\n',encoding='utf-8')
(ROOT / 'PACKET_VALIDATION.json').write_text(json.dumps({
    'command':'python -X utf8 prepare_packet.py','required_fields':'pass','allowed_kinds':'pass',
    'draft_labels':'pass','accepted_source_tag':'owner-own-work','relation_endpoints':'pass',
    'dependency_cycle':'none','proof_checks':46,'independent_referee_receipt':None,
    'integrator_compatibility':'Not executed; local field validation only.'},indent=2)+'\n',encoding='utf-8')

progress = {'event':'w424 C0023: bounded-degree critical-jump obstruction and fixed-interval gap audit saved; 46 deterministic checks pass; drafts await review.',
            'agent':'w424','row':'S1.w424.2','evidence':str(ROOT / 'REPORT.md'),
            'posted':False,'reason':'The worker brief restricts writes to w424 and forbids live mesh sends; prepared for supervisor posting.'}
(ROOT / 'PROGRESS_EVENT.json').write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')

reviewdir = ROOT / 'review'
reviewdir.mkdir(exist_ok=True)
snapshot = reviewdir / 'w423_LEMMAS_snapshot.md'
if not snapshot.exists():
    shutil.copyfile(Path(r'~/brain_workers/w423/LEMMAS.md'), snapshot)
print(json.dumps({'entries':3,'relations':4,'proof_checks':46,'all_output_local':True,'submitted':False}))
