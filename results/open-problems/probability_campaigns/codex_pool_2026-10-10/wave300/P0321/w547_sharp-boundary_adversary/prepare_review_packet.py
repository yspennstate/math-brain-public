"""Create only worker artifacts and the explicitly authorized w547 DRAFT inbox."""
from __future__ import annotations
import json
from pathlib import Path
import re
import time

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w547')

def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def main():
    measurements = json.loads((ROOT / 'MEASUREMENTS.json').read_text(encoding='utf-8-sig'))
    if measurements['status'] in ['RUNNING', 'FAIL', 'STOPPED_AT_NUMERIC_TIME_GATE']:
        raise RuntimeError('Resolve numerical run before creating the completed review packet')
    source_status = {
        'target': 'P0321', 'title': 'Existence of a hexatic phase for two-dimensional Riesz gases',
        'as_of': '2026-10-10', 'current_openness': 'UNKNOWN',
        'exact_catalogue_statement_recovered': True,
        'exact_catalogue_statement': 'Prove or refute the intermediate hexatic phase predicted in two-dimensional Riesz-gas phase diagrams, distinguished by orientational order and absence of crystalline positional order.',
        'fully_quantified_source_theorem_recovered': False,
        'reason': 'The cited survey supplies a qualitative phase prediction; it does not fix exact microscopic observables, rate quantifiers, or a universal exponent range.',
        'ranking': {'path': '~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv',
                    'line': 556, 'status': 'unsolved', 'status_date': '2026-09-07'},
        'primary_source': {'author': 'Mathieu Lewin', 'title': 'Coulomb and Riesz gases: The known and the unknown',
                           'url': 'https://arxiv.org/pdf/2202.09240v2', 'version': 'v2, 30 April 2022; PDF dated 3 May 2022',
                           'locator': 'VI.B, printed pp.66-67, PDF zero-based pages 65-66',
                           'short_exact_excerpt': 'fast decay of translational correlations and slow decay of (six-fold) orientational correlations',
                           'scope': 'Short-range s>2 and numerical discussion of neutralized long-range s=0,1; no assertion for every Riesz exponent.',
                           'model': 'd=2, density rho>0, beta>0; |x|^-s for s>0 and -log|x| for s=0; long range requires its neutralized/renormalized Gibbs specification.',
                           'source_hash_receipt': 'Not performed; source verification is not a mathematical proof.'},
        'local_prior': [
            {'path': '~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/brain_bundle_C006p02.json',
             'key': 'op-p0321', 'status': 'Concept; source says open, current status unverified.'},
            {'path': '~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/brain_bundle_C006a05.json',
             'key': 'at-p0321', 'status': 'Author-checked concept, no independent review; contains the same rotational-mixture example as C001.'},
            {'path': '~/math-brain-build/export/population/nodes.jsonl',
             'lines': [3643, 8627], 'status': 'Both exact logical entries located by targeted grep; no store export read wholesale.'}],
        'owner_solved_retired_check': {
            'attempts_H_20260912': 'No matching P0321/hexatic proof record located in targeted textual search.',
            'attempts_I_20260914': 'No matching P0321/hexatic proof record located in targeted textual search.',
            'lean_20260908': 'Only the annotated ranking row located; no actual target theorem located.',
            'team_O': 'No P0321 row in targeted TEAM_BOARD search.',
            'conclusion': 'No solved/retired certificate found in the named checked material; this is not an exhaustive openness certificate.'},
        'literature_verification': {
            'date': '2026-10-10', 'queries': ['hexatic Riesz gas arxiv', 'two-dimensional Riesz hexatic',
                                           'Coulomb and Riesz gases: The known and the unknown', 'Riesz hexatic 2025 OR 2026'],
            'conclusion': 'Primary survey verified. Bounded public search did not locate a rigorous resolution; current openness UNKNOWN.'},
        'brain_recall': {'status': 'TIMEOUT_60S', 'fallback_index_result': 'No relevant P0321/hexatic/Riesz or requested scar entry matched MEMORY.md.',
                         'explicit_required_scar': 'perceptron_proof_open_gaps_fleet_2026_07_12',
                         'lesson_applied': 'Successful auxiliary checks cannot close the hardest microscopic/defect proof gap.'},
        'independence': {'frozen_before_peer_read': ['C001', 'C002', 'C003'], 'peer_original_read': 'w546 LEMMA_L01.md',
                         'peer_verdict': 'KEEP within stated L1 stationary real Gaussian assumptions, AUDIT_W546_L01.md',
                         'review_of_review': False},
        'brain_output_states': {'prepared': True, 'submitted': True, 'reviewed': False,
                                'reviewed_detail': 'w548 requested for C002/C003; no independent receipt incorporated yet.',
                                'ingested': 'UNKNOWN / not performed by w547', 'retrievable': 'UNVERIFIED for the new bundle'},
        'hardest_open_piece': 'Construct a microscopic positive-temperature defect/correlation comparison that disorders translation and retains the required slow sixfold order on a genuine temperature interval.',
    }
    write_json(ROOT / 'SOURCE_STATUS.json', source_status)

    claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    for claim in claims:
        if claim['id'].endswith('C001'):
            claim['prior_work_status'] = 'Independent reproduction of at-p0321; not new and not included in the new brain draft.'
        claim['novelty'] = 'UNVERIFIED; no novelty claim'
    if not any(c['id'].endswith('A001') for c in claims):
        claims.append({'id': 'S1.P0321.w547.A001', 'kind': 'independent_original_proof_audit',
                       'status': 'independently checked proof',
                       'exact_statement': 'w546 L01 is correct for a centered stationary real Gaussian field with even nonnegative L1 spectral density and real nonzero m: its exponential increment correlation tends to exp(-m^2 R(0))>0.',
                       'assumptions': ['Exactly the L1 stationary Gaussian assumptions in AUDIT_W546_L01.md; m real nonzero.'],
                       'source': {'original': '~/brain_workers/w546/LEMMA_L01.md', 'audit': 'AUDIT_W546_L01.md'},
                       'proof': 'Exact Gaussian increment variance and characteristic function, followed by the Riemann-Lebesgue lemma. Independent curl special case saved before peer proof was read.',
                       'independent_reviewer': 'w547, for original w546 L01 only',
                       'remaining_gap': 'No microscopic Riesz/defect comparison; this audit is not an independent check of w547 C002/C003.',
                       'verdict': 'KEEP auxiliary lemma; clarify m real nonzero; no P0321 theorem verdict.'})
    (ROOT / 'CLAIMS.jsonl').write_text(''.join(json.dumps(c, ensure_ascii=False) + '\n' for c in claims), encoding='utf-8')

    source = {'source_id': 'owner-own-work:w547:p0321-gaussian-boundary-20261010',
              'url': 'urn:owner-work:w547:p0321-gaussian-boundary:20261010',
              'revision': 'draft-author-derivation-20261010-independent-referee-pending',
              'license': 'owner-own-work', 'excerpt': None}
    assumptions = ['T,mu,a,Lambda>0; nonzero G in R^2; fixed unit direction e; Fourier measure d^2k/(2*pi)^2.',
                   'Only the specified Gaussian proxy; no microscopic Riesz Gibbs measure or bond-observable comparison is established.',
                   'Independent mathematical referee for author-derived claims is pending; concept/draft material only.']
    bundle = {
        'spec': 'mathbrain-draft-v1', 'author_agent': 'w547',
        'bundle_slug': 'p0321-gaussian-stiffness-endpoint-obstruction-20261010',
        'entries': [
            {'key': 'gaussian-model', 'namespace': 'probability.gaussian',
             'logical_name': 'two-dimensional-cutoff-longitudinal-transverse-displacement-proxy',
             'kind': 'definition', 'title': 'Cutoff Gaussian displacement proxy for a Riesz phase route',
             'statement': 'For T,mu,a,Lambda>0 and 0<=p<=2, define a centered real Gaussian displacement u on R^2 modulo an additive constant by spectral covariance S_p(k)=T*(P_T(k)/(mu*|k|^2)+P_L(k)/(a*|k|^p))*1_{0<|k|<Lambda}, with Fourier measure d^2k/(2*pi)^2, P_L(k)=k*k^t/|k|^2 and P_T=I-P_L. The infrared limit is taken on anchored increments u(x)-u(0). For G!=0 define C_G,p(x)=E exp(i*G.(u(x)-u(0))); define theta=curl(u)/2 and C_6(x)=E exp(6*i*(theta(x)-theta(0))). These are defined elastic proxies, not identified with microscopic particle or bond correlations; p is a stipulated stiffness exponent, not an asserted Riesz exponent.',
             'proof_text': None, 'assumptions': assumptions[:2], 'domain': 'probability theory', 'source': dict(source)},
            {'key': 'proxy-asymptotics', 'namespace': 'probability.gaussian',
             'logical_name': 'draft-cutoff-gaussian-elastic-proxy-correlation-asymptotics',
             'kind': 'concept', 'title': 'DRAFT: Gaussian proxy exponents and persistent curl orientation',
             'statement': 'AUTHOR DERIVATION, INDEPENDENT REFEREE PENDING. Fix T,mu,a,Lambda>0, nonzero G in R^2, unit e and 0<=p<=2. For a centered real Gaussian displacement with spectral covariance T*(P_T/(mu*|k|^2)+P_L/(a*|k|^p))*1_{0<|k|<Lambda} and Fourier measure d^2k/(2*pi)^2, let C_G,p(x)=E exp(i*G.(u(x)-u(0))), interpreting u by anchored increments. For each fixed p<2, C_G,p(r*e)=A_p(G,e)*r^{-eta_T}*(1+o(1)), with A_p finite positive and eta_T=T*|G|^2/(4*pi*mu). At p=2 the exponent is eta_T+T*|G|^2/(4*pi*a), also with a finite positive prefactor. For theta=curl(u)/2, E exp(6*i*(theta(x)-theta(0))) tends to exp(-9*T*Lambda^2/(4*pi*mu))>0. These proxies therefore have neither exponential positional decay nor sixfold correlations decaying to zero. This calculation does not settle a microscopic Riesz hexatic phase.',
             'proof_text': None, 'assumptions': assumptions, 'domain': 'probability theory', 'source': dict(source)},
            {'key': 'endpoint-obstruction', 'namespace': 'probability.gaussian',
             'logical_name': 'draft-gaussian-stiffness-endpoint-and-distance-limits-do-not-commute',
             'kind': 'concept', 'title': 'DRAFT: noncommuting Gaussian stiffness endpoint and distance limits',
             'statement': 'AUTHOR DERIVATION, INDEPENDENT REFEREE PENDING. Fix T,mu,a,Lambda>0, G!=0 in R^2 and unit e. For the centered real Gaussian displacement increment model with spectral covariance T*(P_T/(mu*|k|^2)+P_L/(a*|k|^p))*1_{0<|k|<Lambda}, 0<=p<=2, and Fourier measure d^2k/(2*pi)^2, put C_G,p(x)=E exp(i*G.(u(x)-u(0))) and L(p,r)=-log(C_G,p(r*e))/log(r), r>1. Then lim_{p->2-}lim_{r->infinity} L(p,r)=T*|G|^2/(4*pi*mu), while lim_{r->infinity}lim_{p->2-} L(p,r)=T*|G|^2/(4*pi*mu)+T*|G|^2/(4*pi*a). Thus the fixed-p asymptotic exponent is not uniform over p<2. At finite r the covariance integral is continuous at p=2, but its fixed-p longitudinal large-distance contribution diverges like 1/(2-p). This is an obstruction to an auxiliary limit interchange; p has not been identified with a microscopic Riesz exponent and no P0321 refutation follows.',
             'proof_text': None, 'assumptions': assumptions, 'domain': 'probability theory', 'source': dict(source)},
        ],
        'relations': [
            {'from_key': 'proxy-asymptotics', 'to_key': 'gaussian-model', 'kind': 'depends_on',
             'rationale': 'The asymptotic calculation uses exactly the defined anchored displacement covariance and cutoff curl proxy.'},
            {'from_key': 'endpoint-obstruction', 'to_key': 'proxy-asymptotics', 'kind': 'depends_on',
             'rationale': 'The two different distance-limit exponents, combined with finite-distance continuity, yield the noncommuting iterated limits.'},
            {'from_key': 'endpoint-obstruction',
             'to_existing_logical': 'math:probability.core:open-problem-p0321-existence-of-a-hexatic-phase-for-two-dimensional-riesz-gases',
             'kind': 'semantic_association',
             'rationale': 'P0321 concerns correlations across a hexatic phase; this auxiliary elasticity-route calculation identifies a specific nonuniform-limit pitfall, without claiming a microscopic result. Target logical entry verified at export/population/nodes.jsonl:3643.'},
        ],
    }
    keys = {entry['key'] for entry in bundle['entries']}
    assert len(keys) == len(bundle['entries'])
    for entry in bundle['entries']:
        assert entry['kind'] in ['definition', 'concept'] and entry['proof_text'] is None
        assert entry['source']['license'].startswith('owner-own-work')
        assert entry['statement'] and entry['assumptions']
    for relation in bundle['relations']:
        assert relation['from_key'] in keys
        assert 'to_key' not in relation or relation['to_key'] in keys
        assert relation['kind'] in ['depends_on', 'semantic_association']
    write_json(ROOT / 'bundle_001.json', bundle)
    INBOX.mkdir(parents=True, exist_ok=True)
    destination = INBOX / 'bundle_001.json'
    if destination.exists():
        if json.loads(destination.read_text(encoding='utf-8-sig')) != bundle:
            raise RuntimeError('Existing inbox artifact differs; do not overwrite another or revised artifact')
    else:
        temporary = INBOX / 'bundle_001.json.part'
        if temporary.exists():
            raise RuntimeError('Existing part file needs inspection; do not overwrite')
        write_json(temporary, bundle)
        temporary.rename(destination)

    hook = {'id': 'gaussian-endpoint-w547-01', 'area': 'math', 'event': 'stage-start',
            'cue': '(?i)(?:uniform|interchang|commut|endpoint).*(?:asymptotic|limit|infrared)|(?:asymptotic|limit|infrared).*(?:uniform|interchang|commut|endpoint)',
            'fire_when': 'Interchange the p->2 endpoint limit with the large-distance asymptotic uniformly.',
            'silent_when': 'Compute the covariance at p=1 fixed and finite distance.',
            'text': 'Before interchanging a parameter endpoint and a distance limit, check uniformity. A finite fixed-parameter correction can diverge at the endpoint; keep the order of limits explicit. This is a prompt to check the proof, not a verdict.',
            'evidence': '~/brain_workers/w547/GAUSSIAN_BOUNDARY.md C003; perceptron_proof_open_gaps_fleet_2026_07_12',
            'proposer': 'w547'}
    assert len(hook['text']) <= 300
    assert re.search(hook['cue'], hook['fire_when'])
    assert not re.search(hook['cue'], hook['silent_when'])
    (ROOT / 'HOOK_PROPOSALS.jsonl').write_text(json.dumps(hook) + '\n', encoding='utf-8')
    write_json(ROOT / 'DRAFT_RECEIPT.json', {
        'prepared': True, 'submitted': True, 'inbox_path': str(destination),
        'submitted_at_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'entries': len(bundle['entries']), 'relations': len(bundle['relations']),
        'reviewed': False, 'ingested': 'UNKNOWN / not performed by w547', 'retrievable': 'UNVERIFIED',
        'local_validation': 'Required entry fields, concept/definition kinds, source tags and relation ends checked; not an integrator or mathematical-proof receipt.',
        'hook_controls': {'fire': True, 'silent': True},
        'promotion': 'No unreviewed theorem/lemma kind, no source manifests/digests, no live-store or global recall changes.'})
    print(json.dumps({'draft': str(destination), 'entries': len(bundle['entries']),
                      'relations': len(bundle['relations']), 'measurement_status': measurements['status'],
                      'hook_fire_and_silent_controls': 'PASS'}, indent=2))

if __name__ == '__main__':
    main()
