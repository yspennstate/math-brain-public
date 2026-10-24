"""Build the worker's draft mathematics and review packet, without live ingestion."""
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent

def save(name, value):
    (BASE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def source(key):
    return {'source_id': 'owner:probability-campaign:C0056:w489:' + key,
            'url': (BASE / 'ATTEMPT.md').as_uri(), 'revision': 'draft-2026-10-10-independent-review-pending',
            'license': 'owner-own-work', 'excerpt': None}

def main():
    attempt = (BASE / 'ATTEMPT.md').read_text(encoding='utf-8')
    parts = {}
    for n in range(1, 6):
        start = attempt.index('## L' + str(n) + ':')
        end = attempt.find('\n## ', start + 1)
        parts['l' + str(n)] = attempt[start:end if end >= 0 else len(attempt)].strip()

    items = [
        ('l1', 'atomic-poisson-first-moment-counterexample',
         'DRAFT: a bounded first Poisson moment permits an atom',
         'For the positive probability measure mu=delta_0 and P_eta(E)=eta/(E^2+eta^2), integral_R P_eta(E)dE=pi for every eta>0 although mu is purely atomic; integral_R P_eta(E)^2 dE=pi/(2 eta). A uniform first energy moment does not imply absolute continuity.',
         ['eta>0', 'P_eta is the unnormalised Poisson transform of mu=delta_0']),
        ('l2', 'annealed-spectral-density-does-not-imply-quenched-absolute-continuity',
         'DRAFT: an annealed density can conceal atomic sample measures',
         'If S is Uniform[-1,1] and H_S is the scalar self-adjoint operator S, its sample spectral measure is mu_S=delta_S, but E mu_S has density (1/2)1_[-1,1]. For every real E and eta>0, E Im(S-E-i eta)^(-1)<=pi/2. Thus uniform expected first resolvent imaginary parts do not imply samplewise absolute continuity.',
         ['S is Uniform[-1,1]', 'H_S acts on a one-dimensional Hilbert space', 'E is real and eta>0']),
        ('l3', 'uniform-expected-higher-poisson-moments-imply-local-absolute-continuity',
         'DRAFT: higher Poisson moments imply almost-sure absolute continuity',
         'Let mu_omega be random positive Borel measures on R of mass at most one, I a bounded open interval, p>1, and eta_n a deterministic positive sequence decreasing to zero. Put P_omega,eta(E)=integral eta/((t-E)^2+eta^2)dmu_omega(t). If sup_n E integral_I P_omega,eta_n(E)^p dE<=C<infinity, then almost surely mu_omega restricted to I has an Lp density f_omega, and E integral_I |f_omega(E)|^p dE<=C/pi^p.',
         ['random positive Borel measures with measurable integrals and mass at most one', 'I is bounded and open', 'p>1', 'eta_n decreases deterministically to zero', 'uniform expected pth energy moment is finite']),
        ('l4', 'inverse-cavity-width-moments-imply-quenched-spectral-absolute-continuity',
         'DRAFT: inverse cavity-width moments give quenched spectral absolute continuity',
         'Let H be bounded self-adjoint on l2(Z^3), with bounded deterministic hopping and iid real site variables of bounded support and bounded probability density rho, scaled by a fixed lambda>0. Delete x to obtain H^x and its hopping vector b_x, and put Gamma_x(E,eta)=eta+Im<b_x,(H^x-E-i eta)^(-1)b_x>. Fix 0<q<1 and an open interval I. If for each x and each compact interval J contained in I, sup_{0<eta<1} E integral_J Gamma_x(E,eta)^(-q)dE<infinity, then almost surely all site spectral measures restricted to I are absolutely continuous, with locally L^(1+q) densities, and chi_I(H)l2(Z^3) is contained in the absolutely continuous subspace. This is a conditional criterion; the moment bound is not established for the lattice Anderson model here. Nonzero spectral weight is a separate requirement.',
         ['bounded self-adjoint H on the countable lattice', 'bounded deterministic hopping', 'bounded-support iid site law with rho in L-infinity', 'fixed lambda>0', 'own-site variable independent of the entire complement', '0<q<1', 'uniform inverse cavity-width energy moment on each compact interval J contained in I']),
        ('l5', 'bounded-potential-resolvent-perturbation-leaves-the-zero-height-gap',
         'DRAFT: bounded-potential perturbation stops at positive height',
         'For the six-neighbour lattice, H_lambda^x=H_0^x+lambda V^x with ||V^x||<=1, lambda>0 and z=E+i eta with eta>0, ||(H_lambda^x-z)^(-1)-(H_0^x-z)^(-1)||<=lambda/eta^2. With ||b_x||^2=6, the corresponding cavity escape widths differ by at most 6 lambda/eta^2. A free lower bound Gamma_0,x>=c>0 yields Gamma_lambda,x>=c/2 by this estimate only under the sufficient restriction eta^2>=12 lambda/c. This estimate supplies no uniform control as eta tends to zero at fixed positive lambda.',
         ['six-neighbour deterministic hopping of magnitude one', 'bounded site potential of norm at most one', 'lambda>0 and eta>0', 'the lower-bound consequence additionally assumes Gamma_0,x>=c>0']),
    ]
    entries = []
    claims = []
    for key, logical, title, statement, assumptions in items:
        remaining = ('Establish the height-uniform inverse cavity-width moment for the actual weak-disorder cyclic lattice, with nonzero spectral weight; GOE statistics require a separate argument.'
                     if key in ('l3', 'l4', 'l5') else
                     'This counterexample only refutes an inference, not weak-disorder Anderson delocalisation.')
        entries.append({'key': key, 'namespace': 'analysis.spectral', 'logical_name': logical,
                        'kind': 'lemma', 'title': title, 'statement': statement,
                        'proof_text': parts[key], 'assumptions': assumptions,
                        'domain': 'spectral theory / random Schrodinger operators', 'source': source(key)})
        claims.append({'id': 'C0056-W489-' + key.upper(), 'statement': statement,
                       'assumptions': assumptions, 'source': source(key), 'proof': parts[key],
                       'independent_reviewer': 'w491; requested, no mathematical verdict received',
                       'remaining_gap': remaining, 'status': 'proved special case',
                       'scope_note': 'Author-derived generic or conditional lemma; not a proof of the parent problem.',
                       'novelty_claim': False, 'formal_check': None,
                       'submitted': False, 'reviewed': False, 'ingested': False, 'retrievable': False})

    for key, logical, title, statement in [
        ('invalid-first-moment-route', 'invalid-first-moment-route-to-sample-spectral-absolute-continuity',
         'DRAFT: rejected first-moment route to sample spectral absolute continuity',
         'Rejected inference: a uniform first energy moment of a scalar Poisson transform, or a bounded density of the disorder-averaged spectral measure, implies almost-sure absolute continuity of the sample measures. This implication is false: delta_0 and the random scalar operator with uniform eigenvalue give exact counterexamples. A higher moment or another argument excluding sample singular mass is required.'),
        ('cavity-moment-gap', 'weak-disorder-cubic-lattice-inverse-cavity-width-moment-gap',
         'DRAFT OPEN GAP: inverse cavity-width moments on the cyclic cubic lattice',
         'Proposed sufficient-condition research target, not an established theorem: for H=-A+lambda V on l2(Z^3), V_x iid Uniform[-1,1], find q in (0,1), lambda_0>0 and a deterministic nonempty bounded open interval I of nonzero spectral weight such that for each fixed 0<lambda<lambda_0, each site x and each compact interval J contained in I, sup_{0<eta<1} E integral_J [eta+Im<b_x,(H^x-E-i eta)^(-1)b_x>]^(-q)dE<infinity. H^x is the compression deleting x and b_x has the six hopping coefficients. This bound would supply a conditional spectral route; it would not prove GOE microscopic statistics. No proof of this bound is supplied.'),
    ]:
        entries.append({'key': key, 'namespace': 'analysis.spectral', 'logical_name': logical,
                        'kind': 'concept', 'title': title, 'statement': statement,
                        'proof_text': None, 'assumptions': [],
                        'domain': 'spectral theory / proof obstructions', 'source': source(key)})

    gap = next(e for e in entries if e['key'] == 'cavity-moment-gap')
    claims.append({'id': 'C0056-W489-GAP', 'statement': gap['statement'],
                   'assumptions': ['actual iid uniform Anderson operator on Z^3', 'fixed positive lambda before eta tends to zero'],
                   'source': gap['source'], 'proof': None,
                   'independent_reviewer': 'w491; pending', 'remaining_gap': 'The entire proposed inverse cavity-width bound is unproved.',
                   'status': 'conjecture', 'novelty_claim': False,
                   'submitted': False, 'reviewed': False, 'ingested': False, 'retrievable': False})

    existing_lp = 'math:analysis.functional:lp-lq-duality-with-its-sigma-finiteness-hypothesis'
    existing_st = 'math:probability.random-matrices:stieltjes-inversion-formula-density-from-the-boundary-imaginary-part'
    existing_attempt = 'math:probability.random-matrices:attempt-c0056-extended-states-for-the-three-dimensional-anderson-model-at-weak-disor'
    relations = [
        {'from_key': 'l4', 'to_key': 'l3', 'kind': 'depends_on', 'rationale': 'Own-site conditioning yields the higher Poisson moment to which the pathwise Lp compactness criterion is applied.'},
        {'from_key': 'l1', 'to_key': 'invalid-first-moment-route', 'kind': 'refutes', 'rationale': 'The atom has uniformly bounded first Poisson energy moment but is singular.'},
        {'from_key': 'l2', 'to_key': 'invalid-first-moment-route', 'kind': 'refutes', 'rationale': 'An absolutely continuous expected spectral measure coexists with purely atomic measures in every sample.'},
        {'from_key': 'l4', 'to_key': 'cavity-moment-gap', 'kind': 'semantic_association', 'rationale': 'The conditional theorem identifies exactly the still-unproved lattice hypothesis required by this route.'},
        {'from_key': 'l5', 'to_key': 'cavity-moment-gap', 'kind': 'semantic_association', 'rationale': 'The deterministic perturbation estimate loses its lower bound as eta tends to zero and does not close the gap.'},
        {'from_key': 'l3', 'to_existing_logical': existing_lp, 'kind': 'depends_on', 'rationale': 'Uses Lp reflexivity with 1<p<infinity on the finite Lebesgue interval; excludes the p=1 endpoint.'},
        {'from_key': 'l3', 'to_existing_logical': existing_st, 'kind': 'cites', 'rationale': 'The Poisson approximate-identity representation is compatible with inversion; the returned pointwise density clause already assumes absolute continuity and is not used to prove it.'},
        {'from_key': 'cavity-moment-gap', 'to_existing_logical': existing_attempt, 'kind': 'cites', 'rationale': 'Continues the recorded closed-recursion and fixed-coupling limit obstruction without reusing a spanning-tree transfer.'},
    ]
    bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w489',
              'bundle_slug': 'c0056-cavity-poisson-bridge-w489-001',
              'entries': entries, 'relations': relations}
    save('DRAFT_bundle_001.json', bundle)
    (BASE / 'CLAIMS.jsonl').write_text(''.join(json.dumps(c, ensure_ascii=False) + '\n' for c in claims), encoding='utf-8')

    live = json.loads((BASE / 'BRAIN_SELECTED_LIVE.json').read_text(encoding='utf-8'))
    existing = {json.loads(r['live_row'][4])['logical_id']: r['live_row'][3] for r in live['rows'] if r['live_row']}
    bykey = {e['key']: e for e in entries}
    edge_rows = []
    for relation in relations:
        to = relation.get('to_key') or relation['to_existing_logical']
        ends = {'from_statement': bykey[relation['from_key']]['statement'],
                'to_statement': bykey[to]['statement'] if to in bykey else existing[to]}
        edge_rows.append({**relation, **ends, 'status': 'DRAFT pending independent review', 'author': 'w489'})
    (BASE / 'EDGES.jsonl').write_text(''.join(json.dumps(e, ensure_ascii=False) + '\n' for e in edge_rows), encoding='utf-8')

    state = json.loads((BASE / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    state['exact_target_status'] = 'Original primary Section 2.1 checked; both spectral and finite-volume GOE demands retained; a uniform-law spectral specialisation is explicitly chosen.'
    state['primary_source'] = {'author': 'Paul Bourgade', 'title': 'Random band matrices',
                               'url': 'https://math.nyu.edu/~bourgade/papers/ICMProceedings.pdf',
                               'arxiv': '1807.03031', 'locator': 'Section 2.1, printed page 7 (PDF page index 6)',
                               'assumptions': 'H=Delta+lambda V; iid real centred variance-one sites; periodic finite-volume boxes for the statistics discussion.',
                               'source_quote': 'there is no clear understanding about how extended states imply GOE spectral statistics.',
                               'law_conversion': 'Our V is Uniform[-1,1], variance 1/3. Set W=sqrt(3)V, alpha=lambda/sqrt(3) to obtain variance-one sites with the same diagonal alpha W=lambda V.',
                               'hash_check': 'SOURCE_HASH_CHECK.json; both archived PDF and text match the intake hashes. This is provenance, not a proof.'}
    state['owner_solved_retired_check'] = {'status': 'No C0056 solved/retired finding in the scoped intake, H/I attempt searches, memory-index terms or direct root status-index filename check. New September primary claim located; referee source audit pending.',
                                         'conclusion': 'UNKNOWN, not certified open and not certified solved'}
    state['brain_memory_recall']['fallback'] = 'Exact required scar perceptron_proof_open_gaps_fleet_2026_07_12.md read; memory-index term search had no matching entry.'
    state['mathematics'] = {'claim_rows': len(claims), 'author_proved_lemmas': 5,
                            'parent_target_solved': False, 'independently_checked_claims': 0,
                            'single_hardest_spectral_gap': gap['statement'],
                            'GOE_branch': 'not established; no implication from absolute continuity asserted'}
    state['adversary_feedback'] = {'agent': 'w490', 'event': 'Independent joint-UI criterion sealed before reading the proof (reported prefix 3e357c12); conditional L3--L5 algebra supported in peer message.',
                                   'scope_boundary': 'w490 owns joint-UI equivalence and ac/no-Lp separation; w489 owns cavity negative-moment to Lp and deterministic height cutoff.',
                                   'counted_as_completed_referee_verdict': False, 'served_identity_receipt': None}
    save('SOURCE_STATUS.json', state)

    measurements = json.loads((BASE / 'FILTER_MEASUREMENT.json').read_text(encoding='utf-8'))
    receipts = {
        'worker': 'w489', 'target': 'C0056', 'date': '2026-10-10',
        'reviewer': 'w491', 'adversary': 'w490',
        'served_model_response_receipt': None, 'served_identity_status': 'unavailable; requested settings are not evidence',
        'author_math_status': 'draft generic/conditional results; no parent solution',
        'independent_review_status': 'pending', 'formal_receipt': None,
        'source_hash_check': 'SOURCE_HASH_CHECK.json', 'retrieval_measurement': measurements,
        'files': [{'path': str(BASE / n), 'sha256': hashlib.file_digest((BASE / n).open('rb'), 'sha256').hexdigest()}
                  for n in ('TARGET.md', 'ATTEMPT.md', 'CLAIMS.jsonl', 'EDGES.jsonl', 'SOURCE_STATUS.json', 'BRAIN_HYPOTHESIS_COMPARISON.md', 'FILTER_MEASUREMENT.json')],
        'bundle': str(BASE / 'DRAFT_bundle_001.json'),
        'integration_digest_or_manifest': 'not computed; reserved for the coordinator',
        'promotion_gate': 'Mathematical review plus required different-model and served-identity evidence; none claimed passed here',
        'submitted': False, 'reviewed': False, 'ingested': False, 'retrievable': False,
    }
    save('REVIEW_PACKET.json', receipts)
    print(json.dumps({'claim_rows': len(claims), 'draft_entries': len(entries), 'exact_edges': len(edge_rows),
                      'local_filter_precision': [measurements['before_precision'], measurements['after_precision']],
                      'live_store_mutation': False}))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
