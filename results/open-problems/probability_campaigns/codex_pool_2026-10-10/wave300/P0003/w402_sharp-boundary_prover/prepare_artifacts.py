"""Prepare reviewable local drafts. Publishing is a separate authorized action."""
from pathlib import Path
import difflib
import json

ROOT = Path(__file__).resolve().parent
assert ROOT.as_posix().lower().endswith('/brain_workers/w402')
M = json.loads((ROOT / 'MEASUREMENTS.json').read_text(encoding='utf-8'))
assert M['status'] == 'PASS' and not M['formal_proof']


def write_json(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


proofs = {
 'kernel': 'Orient internal edges e=(u,v), put d_e=v-u and J_e=d_e F(p_e)/2. The vertex equations become B J=-b, where B has +1 at the tail and -1 at the head and b is the prescribed boundary contribution. Each component has one row dependency. A spanning-tree incidence minor with a root row removed has determinant +/-1 by leaf elimination, so rank B=|V|-c. Its image consists precisely of vectors with zero sum on each component. This proves the compatibility condition and affine dimension |E|-|V|+c. Euler gives the bounded-face count in the connected plane case.',
 'mode': 'On a complete interior hexagon v_0,...,v_5, define H at side midpoints by delta/(v_{j+1}-v_j) and zero at all other midpoints. At v_j the outgoing contribution is delta/2 and the incoming contribution is -delta/2; the third is zero. Other vertices see zero. Since side lengths are delta, the six nonzero values have modulus one. Every prescribed boundary value is unchanged by adding H.',
 'obstruction': 'The constant field 1 satisfies the vertex identity because the three displacement vectors sum to zero. Add the six-edge field H from the preceding lemma. Then F=1+H has full boundary trace 1 and sup norm at most 2. A face-side midpoint p and the midpoint q of the third edge at the same vertex have separation sqrt(3)delta/2 and value difference of modulus 1. Center the chosen face near a fixed interior point while delta tends to zero. Locally uniform convergence to any continuous f would make the difference at p,q tend to zero, a contradiction. This argument uses arbitrary complex fields; it does not say the actual SAW observable has these modes.',
 'minimal': 'The oriented boundaries of the f bounded faces give real cycle vectors c_i. They are independent: zero edge coefficients force neighboring face coefficients to agree, and exterior coefficient zero propagates through the connected dual. Their number f=|E|-|V|+1 equals dim ker B, so C=[c_i] spans the homogeneous kernel. If J=C a and C^T J=0 then C^T C a=0; positive definiteness gives a=0, including complex a. For an inhomogeneous solution J_0, use a=-(C^T C)^(-1)C^T J_0 to satisfy the extra conditions. Fewer than f linear constraints leave a nonzero kernel by rank-nullity. These are algebraic constraints, not conditions proved for the SAW path sum.'
}

statements = {
 'assigned': 'Historical conjecture, current openness UNKNOWN: Grimmett Question 2.2 asks whether the uniform n-step self-avoiding walk on the honeycomb lattice, starting at the origin with free endpoint, converges weakly after a suitable rescaling to an SLE(8/3) random curve. The source does not specify rescaling, SLE geometry or stopping, parametrization, or topology. The critical-fugacity boundary-to-boundary chordal conjecture is a related formulation; equivalence to this fixed-length question is not established here.',
 'bridge': 'Proposed observable compactness bridge (false for arbitrary complex midpoint fields): on honeycomb domains with mesh tending to zero, the vertex relation sum_{p adjacent to v}(p-v)F(p)=0, a uniform sup bound, and a fixed full boundary trace would force a locally uniform continuous holomorphic subsequential limit. This proposed implication needs extra hypotheses excluding lattice cycle modes. Its failure does not refute SAW-to-SLE convergence.',
 'kernel': 'Let V be a finite honeycomb vertex set, E the edges with both endpoints in V, H the boundary mid-edges with exactly one endpoint in V, and c the number of components of (V,E). Prescribe complex g on H and b_v=sum_{h in H incident to v}(h-v)g(h). Arbitrary complex interior midpoint values F satisfying sum_{p adjacent to v}(p-v)F(p)=0 exist iff sum_{v in C}b_v=0 on every component C. If solvable, their complex affine dimension is |E|-|V|+c. For a connected plane graph this equals the number of bounded faces. This is an author-proved auxiliary result, pending full independent review.',
 'mode': 'On a honeycomb mesh of side length delta, choose a complete interior hexagonal face with counterclockwise vertices v_0,...,v_5. The complex midpoint field H((v_j+v_{j+1})/2)=delta/(v_{j+1}-v_j), with indices modulo 6 and H=0 elsewhere, satisfies every vertex relation sum_p(p-v)H(p)=0, has six support points of modulus 1, and vanishes at every boundary midpoint. Adding H to a solution preserves every boundary value. This is an author-proved auxiliary result, pending full independent review.',
 'obstruction': 'There exist simply connected honeycomb patches tending to a fixed hexagonal domain, with mesh delta_n tending to zero, and arbitrary complex midpoint fields F_n with full boundary trace identically 1, sup norm at most 2, and sum_{p adjacent to v}(p-v)F_n(p)=0 at every vertex, but no subsequence converges locally uniformly to a continuous function near a fixed interior point. One may take F_n=1+H_delta_n on a central face; two midpoints at distance sqrt(3)delta_n/2 have value difference of modulus 1. These fields are not asserted to be SAW observables. This is an author-proved auxiliary result, pending full independent review.',
 'minimal': 'For a connected finite plane honeycomb graph with f bounded faces and compatible prescribed boundary midpoint values, the homogeneous vertex-relation kernel has complex dimension f. Fewer than f additional complex linear conditions cannot determine interior midpoint values uniquely. Exactly f suffice: orient each internal edge, put J_e=(v-u)F(p_e)/2, and impose c_i^T J=0 on the real signed cycle vectors of the bounded faces. These constraints give a unique solution to the algebraic boundary problem; they are not claimed to hold for the actual SAW observable or to prove a scaling limit. This is an author-proved auxiliary result, pending full independent review.'
}

status = json.loads((ROOT / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
status['primary_source'] = {
 'url': 'https://arxiv.org/pdf/2205.07318', 'version': '2205.07318v1, 2022-05-15',
 'target': 'Question 2.2, printed/PDF page 3',
 'source_quote': 'Does a uniformly distributed n-step SAW from the origin of H converge weakly, when suitably rescaled, to the Schramm-Loewner random curve SLE8/3?',
 'statement_validation': 'PRIMARY_SOURCE_READ', 'ensemble': 'uniform fixed n, origin start, free endpoint',
 'unspecified': ['rescaling', 'SLE geometry and stopping', 'parametrization', 'topology']}
status['related_observable_source'] = {
 'url': 'https://arxiv.org/pdf/1007.0575', 'version': '1007.0575v2, 2011-06-27',
 'target': 'Section 4, Conjecture 1', 'local_identity': 'Lemma 1, equation (1)',
 'warning': 'Section 4, pages 9-10: the local identity alone does not give compactness',
 'ensemble': 'critical fugacity; two distinct boundary marks', 'equivalence_to_assigned_target': 'NOT_PROVED'}
status['prior_attempt_check'] = {
 'exact_intake_record': 'Older original P0003 ledger not recovered from the named intake problems.jsonl files.',
 'secondary_record': 'export/population/nodes.jsonl:1176, math:probability.core:open-problem-p0003-hexagonal-self-avoiding-walk-scaling-limit',
 'H_I_direct_P0003_hits': 0,
 'lean_direct_P0003_hits': 'Annotated historical ranking only; no actual theorem or formal receipt recovered.',
 'related_attempt': 'C0096-A001, intake_claude_20260907/attempts.jsonl:84; historical and unreviewed, not imported as proof.',
 'owner_solved_retired_check': 'Targeted named records and SAW memory hints contain no closure certificate. Complete authoritative retirement/status register not recovered; current openness stays UNKNOWN.'}
status['status_check_limits'] = 'Assigned primary question read and matched to the secondary record. Historical and bounded recent primary-literature searches do not establish current openness or a solution. No repeated status search is needed to continue the precise auxiliary mathematics.'
status['hardest_target_gap'] = 'Prove mesh-independent regularity and orientation consistency for the actual normalized observable; justify all curve-limit steps and any passage to the assigned fixed-length, free-endpoint ensemble separately.'
write_json('SOURCE_STATUS.json', status)

claims = [json.loads(x) for x in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if x]
claims[1]['source'] = 'owner-own-work; local-relation background verified in arXiv:1007.0575v2, Lemma 1, equation (1)'
for number, key in [(3, 'kernel'), (4, 'mode'), (5, 'obstruction'), (6, 'minimal')]:
    claims.append({'id': f'S1.P0003.w402.{number:03}', 'kind': 'auxiliary mathematical result',
                   'statement': statements[key], 'assumptions': 'All hypotheses are included in the statement; arbitrary complex midpoint fields, not the actual SAW path sum.',
                   'source': 'owner-own-work; ATTEMPT.md; local equation from arXiv:1007.0575v2',
                   'proof_or_counterexample': proofs[key], 'independent_reviewer': 'w404; full-packet verdict pending',
                   'remaining_gap': 'Actual SAW regularity, curve convergence, and fixed-length ensemble passage remain open in this packet.',
                   'status': 'proved special case'})
claims.append({'id': 'S1.P0003.w402.007', 'kind': 'source-scope correction', 'statement': statements['assigned'],
               'assumptions': 'Do not assume equivalence of uniform fixed-length and critical-fugacity chordal ensembles.',
               'source': 'https://arxiv.org/pdf/2205.07318, Question 2.2, printed/PDF page 3',
               'source_quote': status['primary_source']['source_quote'],
               'proof_or_counterexample': 'The primary question has fixed length and origin start; the related observable conjecture explicitly has critical weights and two marked boundary endpoints. Their asymptotic equivalence is not supplied by either quoted formulation.',
               'independent_reviewer': 'w404; source-scope review requested',
               'remaining_gap': 'The fixed-length question needs a precise limiting-law convention before any target-proof claim.',
               'status': 'conjecture'})
seen = set()
dedup = []
for row in claims:
    if row['id'] not in seen:
        seen.add(row['id'])
        dedup.append(row)
(ROOT / 'CLAIMS.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in dedup), encoding='utf-8')

titles = {'assigned': 'P0003: fixed-length source scope and unverified current status',
          'bridge': 'Proposed honeycomb observable compactness bridge',
          'kernel': 'Exact boundary solvability and cycle freedom of the honeycomb vertex relation',
          'mode': 'Six-edge boundary-preserving mode of the honeycomb vertex relation',
          'obstruction': 'Bounded fixed-boundary honeycomb midpoint fields can fail compactness',
          'minimal': 'Minimal linear constraints for the honeycomb midpoint boundary kernel'}
names = {'assigned': 'p0003-fixed-length-source-scope', 'bridge': 'honeycomb-local-identity-compactness-bridge',
         'kernel': 'honeycomb-midpoint-identity-boundary-kernel', 'mode': 'honeycomb-midpoint-six-edge-mode',
         'obstruction': 'honeycomb-midpoint-bounded-boundary-compactness-obstruction',
         'minimal': 'honeycomb-midpoint-kernel-minimal-linear-constraints'}
entries = []
for key in statements:
    source = {'source_id': f'owner-probability-campaign-w402-20261010:{key}',
              'url': (ROOT / 'ATTEMPT.md').as_uri(), 'revision': 'author-proof-20261010-review-pending',
              'license': 'owner-own-work', 'excerpt': None}
    if key == 'assigned':
        source = {'source_id': 'arxiv:2205.07318v1:question-2-2', 'url': 'https://arxiv.org/pdf/2205.07318',
                  'revision': 'as-read-2026-10-10', 'license': 'arxiv-nonexclusive (mathematical statement paraphrased)', 'excerpt': None}
    entries.append({'key': key, 'namespace': 'probability.self_avoiding_walk', 'logical_name': names[key],
                    'kind': 'lemma' if key in proofs else 'concept', 'title': titles[key],
                    'statement': statements[key], 'proof_text': proofs.get(key),
                    'assumptions': ['Finite honeycomb graph; arbitrary complex midpoint fields'] if key in proofs else [],
                    'domain': 'probability; self-avoiding walk; discrete complex analysis', 'source': source})
relations = [
 {'from_key': 'mode', 'to_key': 'kernel', 'kind': 'specializes', 'rationale': 'The six-edge face circulation is a nonzero element of the classified homogeneous boundary kernel.'},
 {'from_key': 'obstruction', 'to_key': 'mode', 'kind': 'depends_on', 'rationale': 'Adding the explicitly proved six-edge field to the constant field gives the persistent unit oscillation.'},
 {'from_key': 'obstruction', 'to_key': 'bridge', 'kind': 'refutes', 'rationale': 'The fields meet the proposed local equation, bound and full boundary trace, but have no continuous locally uniform subsequential limit.'},
 {'from_key': 'minimal', 'to_key': 'kernel', 'kind': 'depends_on', 'rationale': 'Rank-nullity and the exact face count prove the necessary number of extra independent linear conditions.'},
 {'from_key': 'kernel', 'to_key': 'bridge', 'kind': 'semantic_association', 'rationale': 'A face-dimensional kernel explains why the boundary trace plus vertex relation leaves interior ambiguity.'},
 {'from_key': 'bridge', 'to_key': 'assigned', 'kind': 'semantic_association', 'rationale': 'The observable bridge is a related SAW-to-SLE route; no equivalence to the fixed-length free-endpoint target is asserted.'},
 {'from_key': 'assigned', 'to_existing_logical': 'math:probability.core:open-problem-p0003-hexagonal-self-avoiding-walk-scaling-limit', 'kind': 'cites', 'rationale': 'The new source-scope note identifies the original source of this exact existing P0003 concept; it does not certify present openness.'}
]
bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w402',
          'bundle_slug': 'p0003-local-observable-boundary-obstruction-20261010', 'entries': entries, 'relations': relations}
write_json('bundle_001.json', bundle)
rows = []
by_key = {e['key']: e for e in entries}
for i, rel in enumerate(relations, 1):
    rows.append({'id': f'S1.P0003.w402.EDGE.{i:03}', **rel,
                 'from_quote': by_key[rel['from_key']]['statement'],
                 'to_quote': by_key[rel['to_key']]['statement'] if 'to_key' in rel else 'OPEN PROBLEM from the Codex campaign ledger (source_says_open; current status unverified; result status attempted_unsolved). Does the rescaled uniform n-step hexagonal-lattice self-avoiding walk converge to SLE_(8/3)?',
                 'reviewer': 'w404; pending', 'status': 'DRAFT'})
(ROOT / 'RELATIONS.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
hook = {'id': 'math-w402-01', 'area': 'math', 'event': 'stage-start',
        'cue': 'honeycomb/parafermionic observable AND local vertex identity is proposed as sufficient for compactness or boundary uniqueness',
        'fire_when': 'Claiming local relation + sup bound + fixed boundary trace imply a holomorphic scaling limit.',
        'silent_when': 'Using the local identity only to compute the connective constant, with no compactness or uniqueness claim.',
        'text': 'Honeycomb vertex identities leave one mode per bounded face. A six-edge perturbation preserves the full boundary trace but oscillates by 1 at O(delta). Name the extra estimate excluding these modes before claiming compactness; this does not refute SAW-to-SLE.',
        'evidence': '~/brain_workers/w402/MEASUREMENTS.json: five meshes, 2448 exact vertex equations, 216 boundary values, oscillation 1; ATTEMPT.md Lemmas 1-2 and Proposition 3',
        'proposer': 'w402'}
assert len(hook['text']) <= 300
(ROOT / 'HOOK_PROPOSAL.jsonl').write_text(json.dumps(hook) + '\n', encoding='utf-8')
patch_dir = ROOT / 'patches'
patch_dir.mkdir(exist_ok=True)
for name, local, live in [('01_brain_draft.diff', 'bundle_001.json', 'math-brain-inbox/w402/bundle_001.json'),
                          ('02_math_hook.diff', 'HOOK_PROPOSAL.jsonl', 'primary_directive/hooks1000/proposals/math-w402.jsonl')]:
    diff = ''.join(difflib.unified_diff([], (ROOT / local).read_text(encoding='utf-8').splitlines(True),
                                      fromfile='a/' + live, tofile='b/' + live))
    (patch_dir / name).write_text(diff, encoding='utf-8')
write_json('BRAIN_LIFECYCLE.json', {'draft': 'prepared', 'submitted': False, 'reviewed': 'partial verdicts to be read; full packet pending',
                                  'ingested': False, 'retrievable': False, 'bundle': '~/math-brain-inbox/w402/bundle_001.json'})
print(json.dumps({'prepared': True, 'claim_rows': len(dedup), 'draft_entries': len(entries), 'draft_relations': len(relations),
                  'patches': 2, 'hook_characters': len(hook['text'])}))
