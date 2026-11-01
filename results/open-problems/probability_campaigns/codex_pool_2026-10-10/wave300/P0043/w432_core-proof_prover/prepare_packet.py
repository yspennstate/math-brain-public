"""Build reviewable drafts locally; publication is a separate explicit step."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def save(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
receipt = json.loads((ROOT / 'INPUT_RECEIPT.json').read_text(encoding='utf-8'))
save('SOURCE_STATUS.json', {
    'target_id': 'P0043', 'date': '2026-10-10', 'exact_source_verified': True,
    'current_openness': 'UNKNOWN', 'novelty_claim': False, 'full_problem_solved_in_this_packet': False,
    'exact_target': 'Independent Bernoulli bond percolation on an infinite connected locally finite quasi-transitive graph G with p_c(G)<1 has no infinite cluster almost surely at p_c(G).',
    'ranking': {'date': '2026-09-07', 'tier': 5, 'status': 'attempted_un', 'caveat': 'Short reason omits the necessary p_c<1 restriction.'},
    'original_ledger_records': receipt['records'],
    'primary_sources': [
        {'source': 'Benjamini--Schramm (1996)', 'locator': 'Conjecture 4, printed p.75',
         'url': 'https://www.kurims.kyoto-u.ac.jp/EMIS/journals/EJP-ECP/article/download/978/1171.pdf',
         'verified': 'Exact conjecture and p_c<1 restriction; original exposition uses site percolation and discusses bond transfer.',
         'quote': 'Critical percolation dies in every almost transitive graph (assuming pc < 1).'},
        {'source': 'Hutchcroft (2016)', 'locator': 'Conjecture 1.1 and Theorem 1.2',
         'url': 'https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2016.07.013.pdf',
         'verified': 'Precise bond target with connectedness and local finiteness; exponential-growth subclass is proved.',
         'quote': 'has no infinite clusters almost surely.'},
        {'source': 'Cerf, arXiv:2608.23661', 'locator': 'Abstract, submitted 2026-08-24',
         'url': 'https://arxiv.org/abs/2608.23661',
         'verified': 'Partial result explicitly for Bernoulli site percolation on Z^d; does not by itself certify a bond extension.'},
        {'source': 'OpenAI math primary scope note 213',
         'url': 'https://raw.githubusercontent.com/openai/math/main/lean/docs/213.md',
         'paper_date': '2026-09-24', 'verified': 'Source claims the entire bond target, including multiplicities, and links comparator statements.',
         'proof_audit': 'NOT PERFORMED here; w434 is inspecting the associated paper. No kernel, theorem-type, or trusted-axiom receipt is claimed.'}
    ],
    'owner_status_check': {'scope': 'Named P0043/C0084 intake rows and prior attempts; Big Open project README identifies a different p_c<p_2-to-2 target; cited solved register targeted grep.',
                           'complete_worldwide_or_owner_search': False},
    'canonical_store_check': {'population': 'Read-only selected P0043/C0084 cards in INPUT_RECEIPT.json',
                              'math_research_brain_path': '~/math-research-brain',
                              'additional_store_receipt': 'CANONICAL_RECEIPT.json if present; no whole-store export read'},
    'independent_review': {'w433': 'Statement-first msg-35afdcf200 delivered; independent analysis predated proof exchange. Peer reports L02-L06 survive as scoped claims and supplies tightening 12 in place of 27; w432 independently rederived it as L08.',
                           'w434': 'Pending packet review'},
    'formal_check': {'run': False, 'theorem': None, 'assumptions': None, 'trusted_axioms': None, 'receipt': None},
    'single_remaining_proof_gap': 'G01: symmetry-dependent vanishing of the entire critical-window pivotal mass, including centres escaping in the mass-transport representation.'
})

descriptions = {
    'w432-L02': ('critical-percolation-pivotal-measure-atom-draft', 'Draft: critical survival as a pivotal-measure atom'),
    'w432-L03': ('critical-percolation-window-integrability-criterion-draft', 'Draft: exact critical-window integrability criterion'),
    'w432-L04': ('bounded-degree-critical-survival-tree-draft', 'Draft: degree-eight tree with positive critical survival'),
    'w432-L05': ('critical-percolation-pointwise-influence-limit-obstruction-draft', 'Draft: pointwise derivative limits can lose a critical atom'),
    'w432-L06': ('regular-tree-uniform-critical-pivotal-bound-draft', 'Draft: uniform finite-radius pivotal bound on regular trees'),
    'w432-L07': ('critical-percolation-pivotal-mass-transport-tail-draft', 'Draft: mass transport leaves the distant-centre tail'),
    'w432-L08': ('regular-tree-complete-subcritical-uniform-pivotal-bound-draft', 'Draft: strengthened regular-tree derivative bound 12'),
    'w432-G01': ('quasitransitive-critical-window-integrability-input-unproved', 'Unproved route input: quasi-transitive critical-window bound')
}
entries = []
for claim in claims:
    if claim['id'] not in descriptions:
        continue
    logical_name, title = descriptions[claim['id']]
    prefix = 'UNPROVED INPUT IN THIS PACKET; worldwide status UNKNOWN. ' if claim['id'] == 'w432-G01' else 'AUTHOR-PROVED DRAFT; independent mathematical review pending. '
    entries.append({
        'key': claim['id'], 'namespace': 'probability.percolation', 'logical_name': logical_name,
        'kind': 'concept', 'title': title, 'statement': prefix + claim['exact_statement'] + ' ' + claim['remaining_gap'],
        'proof_text': None, 'assumptions': claim['assumptions'], 'domain': 'probability theory',
        'source': {'source_id': 'owner-own-work:w432:P0043:' + claim['id'],
                   'url': str(ROOT / 'ATTEMPT.md'), 'revision': 'author-packet-2026-10-10-unreviewed',
                   'license': 'owner-own-work', 'excerpt': None}
    })
    if claim['id'] == 'w432-L08':
        entries[-1]['source']['source_id'] = 'owner-own-work:P0043:w433-tightening-w432-rederivation'
        entries[-1]['statement'] += ' Discovery credited to w433; w432 independently rederived the bound. Referee w434 pending.'
entries.append({
    'key': 'w432-R01', 'namespace': 'probability.percolation',
    'logical_name': 'quasitransitive-critical-extinction-lattice-specialization-scope-correction-draft',
    'kind': 'concept', 'title': 'Draft scope correction: the lattice is a special case of the graph target',
    'statement': 'DRAFT SOURCE CORRECTION, independent review pending. The assertion of critical Bernoulli bond extinction on every infinite connected locally finite quasi-transitive graph G with p_c(G)<1 includes the nearest-neighbour Z^d case under the same critical-parameter restriction. A proof only on Z^d does not by itself cover all polynomial-growth quasi-transitive graphs. The cited prior attempt supplies no converse reduction; retain the valid one-way specialization rather than an equivalence.',
    'proof_text': None, 'assumptions': ['The general graph target is read with its full stated hypotheses', 'No transfer theorem is assumed'],
    'domain': 'probability theory',
    'source': {'source_id': 'owner-own-work:w432:P0043:scope-correction',
               'url': str(ROOT / 'SOURCE_CORRECTIONS.jsonl'), 'revision': 'author-source-audit-2026-10-10-unreviewed',
               'license': 'owner-own-work', 'excerpt': None}
})
relations = [
    {'from_key': 'w432-L03', 'to_key': 'w432-L02', 'kind': 'depends_on', 'rationale': 'The limiting critical-window mass is the critical survival atom; the exact iff proof is in L03.'},
    {'from_key': 'w432-L05', 'to_key': 'w432-L04', 'kind': 'depends_on', 'rationale': 'The pointwise derivative obstruction uses the specified degree-eight tree and its positive critical survival.'},
    {'from_key': 'w432-L05', 'to_key': 'w432-L02', 'kind': 'semantic_association', 'rationale': 'The tree exhibits a nonzero critical atom despite pointwise subcritical derivative decay.'},
    {'from_key': 'w432-L04', 'to_key': 'w432-L03', 'kind': 'semantic_association', 'rationale': 'The counterexample fails quasi-transitivity and shows why independent bonds and bounded degree alone cannot prove the proposed critical-window estimate.'},
    {'from_key': 'w432-L06', 'to_key': 'w432-L03', 'kind': 'specializes', 'rationale': 'The proved regular-tree L-infinity influence bound verifies the sufficient integrability criterion for this subclass.'},
    {'from_key': 'w432-L07', 'to_key': 'w432-L03', 'kind': 'semantic_association', 'rationale': 'Under the explicitly assumed mass-transport principle, the critical-window mass equals the integrated incoming pivotal mass over all centres.'},
    {'from_key': 'w432-L08', 'to_key': 'w432-L06', 'kind': 'proves', 'rationale': 'The stronger D/c_b bound on the whole interval [0,1/b] implies the old D(1+2/c_b) bound on [1/(2b),1/b]. For D=3 the constants are 12 and 27 respectively.'},
    {'from_key': 'w432-G01', 'to_key': 'w432-L03', 'kind': 'depends_on', 'rationale': 'G01 is the unproved critical-window input identified by the exact target-equivalence criterion; the parent target is not proved.'},
    {'from_key': 'w432-R01', 'to_key': 'w432-G01', 'kind': 'semantic_association', 'rationale': 'Both concern the scope of the full quasi-transitive target; neither is a proof of that target.'}
]
bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w432', 'bundle_slug': 'critical-percolation-pivotal-concentration-w432-001',
          'entries': entries, 'relations': relations}
bundle_filename = 'bundle_002.json' if any(claim['id'] == 'w432-L08' for claim in claims) else 'bundle_001.json'
save(bundle_filename, bundle)

allowed = {'depends_on', 'defines', 'proves', 'refutes', 'generalizes', 'specializes', 'analogous_to', 'cites', 'semantic_association'}
keys = {entry['key'] for entry in entries}
assert len(keys) == len(entries) <= 200
for entry in entries:
    assert entry['kind'] == 'concept' and entry['proof_text'] is None
    assert re.fullmatch(r'[a-z0-9][a-z0-9.-]*', entry['logical_name'])
    assert entry['source']['license'].startswith('owner-own-work')
    assert all(isinstance(entry['source'][field], str) and entry['source'][field] for field in ('source_id', 'url', 'revision', 'license'))
    assert entry['statement'] and isinstance(entry['assumptions'], list)
for relation in relations:
    assert relation['from_key'] in keys and relation['to_key'] in keys and relation['kind'] in allowed
adjacency = {key: [] for key in keys}
for relation in relations:
    if relation['kind'] == 'depends_on':
        adjacency[relation['from_key']].append(relation['to_key'])


def check(key, trail):
    assert key not in trail
    for target in adjacency[key]:
        check(target, trail | {key})


for key in keys:
    check(key, set())
save('BUNDLE_VALIDATION.json', {'structural_status': 'PASS', 'entries': len(entries), 'relations': len(relations), 'local_bundle': bundle_filename,
                               'mathematical_review': 'PENDING; structural validation is not proof',
                               'live_store_writes': 0, 'all_entries_kind': 'concept'})
old_states = json.loads((ROOT / 'BUNDLE_STATES.json').read_text(encoding='utf-8')) if (ROOT / 'BUNDLE_STATES.json').exists() else {}
history = old_states.get('submission_history', [])
if old_states.get('submission_path') and old_states['submission_path'] not in history:
    history.append(old_states['submission_path'])
save('BUNDLE_STATES.json', {'prepared': True, 'submitted': False, 'reviewed': False, 'ingested': False, 'submission_history': history,
                           'retrievable': False, 'independent_reviewers': ['w433', 'w434'],
                           'note': 'Only the validating coordinator may integrate after independent mathematical review.'})
print(json.dumps({'prepared_entries': len(entries), 'relations': len(relations), 'structural_status': 'PASS',
                  'author_proved_partial_claims': sum(claim['id'].startswith('w432-L') for claim in claims),
                  'unproved_inputs': [claim['id'] for claim in claims if claim['status'] == 'conjecture']}))
