"""Prepare a small concept-only draft; never invoke a live-store integrator."""
from pathlib import Path
import datetime
import difflib
import json

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w457')
SLUG = 'c0048-critical-gap-and-cubic-audit-w457-20261010'
PREFIX = 'DRAFT AUDIT CONCEPT; independent referee pending. '


def entry(key, logical, title, statement, assumptions, artifact):
    return {
        'key': key, 'namespace': 'probability.statmech', 'logical_name': logical,
        'kind': 'concept', 'title': 'Draft audit: '+title,
        'statement': PREFIX+statement, 'proof_text': None,
        'assumptions': assumptions, 'domain': 'probability theory',
        'source': {
            'source_id': 'owner-probability-proofswarm-w457-20261010:'+key,
            'url': 'urn:probability-research:20261010:w457:c0048:'+artifact,
            'revision': 'author-draft-20261010-v1; pending-independent-referee',
            'license': 'owner-own-work; private campaign derivation and audit, no theorem promotion',
            'excerpt': None,
        },
    }


def main():
    entries = [
        entry('critical-gap', 'critical-potts-magnetization-gap-proof-obligation',
              'C0048 uniform critical magnetization gap',
              'For integer q>=3,d>=3, C0048 asks theta_w(p_c)>0 for the zero-field nearest-neighbor FK/Potts model on Z^d. With delta-spin coupling p=1-exp(-beta), normalized color-1 magnetization equals theta_w(p). Wired theta_w is the decreasing finite-box limit of continuous increasing connection probabilities, hence right continuous in p. A lower bound delta>0 must be uniform as p decreases to p_c. Such a bound proves critical ordering; positivity with a p-dependent bound tending to zero does not. The uniform gap, particularly q=d=3, remains unproved in this packet; current general openness is UNKNOWN.',
              ['integer q>=3 and d>=3', 'nearest-neighbor Z^d, unit ferromagnetic coupling, zero field',
               'wired FK / monochromatic color-1 Potts boundary', '0<p_c<1'], 'ATTEMPT.md-I2'),
        entry('local-obstruction', 'critical-potts-local-to-global-fk-obstruction',
              'Positive FK edge conditionals do not imply percolation',
              'For q>=1 and 0<p<1, a finite FK edge conditional, given any subset of the other edges, lies between a=p/(p+q(1-p)) and p. The bounds follow from the open/closed component-count ratio and the tower property. For integer d>=1, in wired boxes [-N,N]^d, integer N>=1, connection of the origin to the boundary is at most 2d*p*((2d-1)*p)^(N-1), by sequential path conditioning and a union bound. At q=3,d=3,p=1/10 all local edge conditionals are at least 1/28, yet the one-arm bound is (3/5)*2^(-(N-1)) and tends to zero. The example is subcritical and does not refute C0048. Local positivity alone cannot supply the uniform critical gap.',
              ['FK weight p^open(1-p)^closed q^components', 'q>=1, 0<p<1',
               'only box boundary vertices are wired', 'integer d>=1 and N>=1'], 'ATTEMPT.md-I1'),
        entry('cumulant-audit', 'potts-free-cluster-fourth-cumulant-and-legendre-audit',
              'Fourth-cumulant mixing term and critical Legendre ratios',
              "For a finite free zero-field Potts graph with N vertices and integer q>=3, let S=sum_v(1{sigma_v=1}-1/q), H_j=sum_FK_components |C|^j, c2=(q-1)/q^2 and c4=(q-1)(q^2-6q+6)/q^4. Independent uniform cluster colors conditional on FK give kappa4(S)=c4*E H4+3*c2^2*Var(H2). At q=3 the omitted mixture term is (4/27)*Var(H2). For P(h)=N^-1 log E exp(hS), chi=P''(0)>0 and local Legendre I, I'''(0)=-P'''(0)/chi^3 and I''''(0)=3*(P'''(0))^2/chi^5-P''''(0)/chi^4. P'''(0)>0 alone does not provide a uniform magnetization cubic. Passing to criticality requires controlled ratios and a remainder on a fixed magnetization interval. The corresponding actual-lattice potential input is unproved.",
              ['finite nonempty free graph', 'zero external field', 'integer q>=3',
               'independent uniform FK colors conditional on all edges', 'local Legendre inverse with chi>0'],
              'CUBIC_OBSTRUCTION.md'),
        entry('cubic-toy', 'symmetric-cubic-potential-fractional-stabilization-obstruction',
              'An invariant cubic polynomial term with continuous onset',
              'For real t and z in C, set r=|z| and F_t(z)=-t*r^2+r^(5/2)-Re(z^3)+r^4. Rotation by 2pi/3 and conjugation preserve F_t, giving the standard S3 action. The cubic polynomial term has a fixed nonzero coefficient. Put c=1-2/(3sqrt(3))>0; 1-s+s^3>=c for s>=0 gives F_t>=-t*r^2+c*r^(5/2). Thus zero is the unique global minimizer for t<=0. For t>0, small positive real z has negative value, and coercivity gives nonzero minimizers with radius at most (t/c)^2. All minimizers approach zero as t decreases to zero. This is a toy variational counterexample to the bare invariant-cubic criterion, not a lattice Potts model. The fractional term prevents a uniform quartic Taylor remainder.',
              ['complex z and real t', 'toy scalar variational potential only',
               'no identification with the lattice constrained free energy'], 'CUBIC_OBSTRUCTION.md-S3'),
    ]
    relations = [
        {'from_key': 'local-obstruction', 'to_key': 'critical-gap', 'kind': 'semantic_association',
         'rationale': 'Supporting ends: local-obstruction says "Local positivity alone cannot supply the uniform critical gap"; critical-gap says "A lower bound delta>0 must be uniform as p decreases to p_c". The former prevents substituting local finite-energy positivity for the latter.'},
        {'from_key': 'cumulant-audit', 'to_key': 'critical-gap', 'kind': 'semantic_association',
         'rationale': 'Supporting ends: cumulant-audit says "P\'\'\'(0)>0 alone does not provide a uniform magnetization cubic"; critical-gap says "A lower bound delta>0 must be uniform as p decreases to p_c". Both identify the uniform input missing in the attempted lattice reduction.'},
        {'from_key': 'cubic-toy', 'to_key': 'cumulant-audit', 'kind': 'semantic_association',
         'rationale': 'Supporting ends: cubic-toy says "The fractional term prevents a uniform quartic Taylor remainder"; cumulant-audit says "Passing to criticality requires controlled ratios and a remainder on a fixed magnetization interval". The toy example demonstrates why the latter premise cannot be omitted.'},
        {'from_key': 'critical-gap',
         'to_existing_logical': 'math:probability.statmech:open-problem-c0048-discontinuity-of-the-potts-phase-transition-on-z-d-for-q-3-d-3',
         'kind': 'cites',
         'rationale': 'Existing export node claim_38c945c83e6d9f9dc77b20f936b660e811e528c284f76bd513990e6ed06ecc6a asks for a transition "discontinuous for every q >= 3" on Z^d,d>=3; this entry states "C0048 asks theta_w(p_c)>0" and records the unresolved uniform-gap route. Exact target source: arXiv:1707.00520, Conjecture 2, PDF page 93.'},
    ]
    bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w457', 'bundle_slug': SLUG,
              'entries': entries, 'relations': relations}
    allowed_relations = {'depends_on','defines','proves','refutes','generalizes','specializes',
                         'analogous_to','cites','semantic_association'}
    keys = {e['key'] for e in entries}
    assert len(entries) == len(keys) == 4
    for e in entries:
        assert e['kind'] == 'concept' and e['proof_text'] is None
        assert e['statement'].startswith(PREFIX)
        assert e['source']['license'].startswith('owner-own-work')
    for r in relations:
        assert r['from_key'] in keys and r['kind'] in allowed_relations
        assert ('to_key' in r) != ('to_existing_logical' in r)
        if 'to_key' in r:
            assert r['to_key'] in keys
    encoded = json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
    (ROOT/'draft_bundle.json').write_text(encoded,encoding='utf-8')
    hook = {
        'id': 'c0048-cumulant-mixture-w457-01', 'area': 'math', 'event': 'PostToolUse',
        'cue': 'A proof averages conditional fourth cumulants as the unconditional fourth cumulant, or infers a quartic sign after omitting cluster-moment variance.',
        'fire_when': 'The q=3 one-edge calculation uses only c4*E H4=-11/27, claiming the full kappa4; direct spin summation gives -8/27.',
        'silent_when': 'The proof includes 3*c2^2*Var(H2), or explicitly restricts its statement to a fixed FK configuration rather than the unconditional law.',
        'text': 'Check the mixture term before assigning a quartic sign: when E(S|FK)=0, kappa4(S)=E[kappa4(S|FK)]+3 Var(E[S^2|FK]). Conditional color independence does not remove random cluster-size fluctuations.',
        'evidence': '~/brain_workers/w457/cumulant_measurements.json: one-edge-q3-half and cycle4-q3-half; omitted formula fails 2/2, corrected formula fails 0/2. Scar: proof_steps_need_derived_joint_structure_2026_09_09.',
        'proposer': 'w457',
    }
    assert len(hook['text']) <= 300
    local_hooks = ROOT/'hooks'
    local_hooks.mkdir(exist_ok=True)
    hook_text = json.dumps(hook,ensure_ascii=False)+'\n'
    (local_hooks/'math-w457.jsonl').write_text(hook_text,encoding='utf-8')
    live_hook = Path('~/primary_directive/hooks1000/proposals/math-w457.jsonl')
    old_hook = live_hook.read_text(encoding='utf-8') if live_hook.exists() else ''
    assert hook['id'] not in old_hook
    patches = ROOT/'patches'
    patches.mkdir(exist_ok=True)
    patch = ''.join(difflib.unified_diff(old_hook.splitlines(keepends=True),(old_hook+hook_text).splitlines(keepends=True),
                                       fromfile='a/'+live_hook.as_posix(),tofile='b/'+live_hook.as_posix()))
    (patches/'01_cumulant_mixture_hook.diff').write_text(patch,encoding='utf-8')

    # The worker brief explicitly authorizes its own inbox. No other shared destination is written.
    INBOX.mkdir(exist_ok=True)
    dest = INBOX/'bundle_001.json'
    part = INBOX/'bundle_001.json.part'
    if dest.exists():
        assert dest.read_text(encoding='utf-8') == encoded, 'Preserve an existing distinct draft'
    else:
        if part.exists():
            assert part.read_text(encoding='utf-8') == encoded, 'Preserve an existing distinct partial draft'
        else:
            with part.open('x',encoding='utf-8') as f:
                f.write(encoded)
        part.rename(dest)
    states = {
        'bundle': str(dest), 'bundle_slug': SLUG, 'entry_count': len(entries),
        'relation_count': len(relations), 'submitted': {'state':'complete','at':datetime.datetime.now(datetime.timezone.utc).isoformat()},
        'reviewed': {'state':'pending','independent_reviewer':'w458'},
        'ingested': {'state':'not_observed','coordinator_only':True},
        'retrievable': {'state':'not_checked','requires_ingestion':True},
        'kind': 'concept-only draft', 'formal_check':None,
        'served_model_evidence': 'No response-side evidence available; no served-model identity is attested.',
        'local_validation': '4 complete concept entries, null proof fields, permitted license prefix and relation types, resolved internal ends; this is schema checking, not mathematical approval',
        'hook_proposal': {'state':'local_patch_prepared','path':str(local_hooks/'math-w457.jsonl'),
                          'deployment':'not_applied'},
    }
    (ROOT/'SUBMISSION_STATES.json').write_text(json.dumps(states,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(states))


if __name__ == '__main__':
    main()
