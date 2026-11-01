"""Prepare and validate an unreviewed concept-only draft. Never ingest a store."""
from datetime import datetime, timezone
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
source = {
    'source_id': 'owner-own-work:w414:C0017:20261010',
    'url': (ROOT / 'ATTEMPT.md').as_uri(),
    'revision': 'author-proof-20261010-unreviewed-v1',
    'license': 'owner-own-work',
    'excerpt': None,
}


def entry(key, logical, title, statement, assumptions):
    return {
        'key': key, 'namespace': 'probability.percolation',
        'logical_name': logical, 'kind': 'concept', 'title': title,
        'statement': 'DRAFT; author proof, independent mathematical review pending. ' + statement,
        'proof_text': None, 'assumptions': assumptions,
        'domain': 'probability theory', 'source': source,
    }


def main():
    entries = [
        entry('series-corridor', 'square-bond-series-corridor-factorization-draft',
              'Draft: exact crossing factorization through a series corridor',
              'Let two disjoint finite chamber graphs L and R be joined only by a simple k-edge path from u in L to v in R. Its interior vertices have degree two. Under independent Bernoulli(p) bonds, 0<p<1, and without external or cross-chamber identifications, terminals S in L and T in R satisfy P(S connects T)=p^k P_L(S connects u) P_R(v connects T)<=p^k. The bound is attained when S={u} and T={v}. Every path edge is a separating bridge; the three necessary and sufficient events use disjoint independent edge families. This is an auxiliary finite-graph result and does not solve square-lattice conformal invariance.',
              ['Finite graph', '0<p<1', 'Only the stated corridor joins the chambers',
               'Product bond law; no external connectivity']),
        entry('boundary-neck', 'boundary-hausdorff-kernel-square-percolation-neck-counterexample-draft',
              'Draft counterexample: unmarked geometric convergence does not preserve crossings',
              'For n>=81 put t=floor(sqrt(n)), a=t, b=2t+1, k=t+1, and m=floor(n/2). Let D_n be the interior of the union of the rectangles [0,a/n]x[0,1], [b/n,1]x[0,1], and [a/n,b/n]x[(m-1/2)/n,(m+1/2)/n]. Each D_n is a simply connected Jordan polygon with fixed corner marks A=(0,1), B=(0,0), C=(1,0), D=(1,1). Its closure Hausdorff distance from the closed unit square is <=k/(2n), its boundary Hausdorff distance is <=b/n, its area loss is k(n-1)/n^2, and its unmarked Caratheodory kernel at (1/2,1/2) is the open unit square. Yet in the induced nearest-neighbor graph on mesh-1/n vertices in its closure, independent bonds p=1/2 give P(AB connects CD)<=2^-k, tending to zero: only the row y=m/n joins the chambers. Canonical square crossings are uniformly positive by classical RSW. The missing marked-prime-end convergence is essential; this example refutes an overstrong approximation bridge, not the properly marked C0017 target.',
              ['Induced graph on closure vertices', 'Independent square-lattice bonds p=1/2',
               'Source AB is x=0; sink CD is x=1', 'No external wiring',
               'Geometric convergence is unmarked; marked prime ends need not converge']),
        entry('prime-end-collapse', 'square-neck-euclidean-marks-conformal-preimage-collapse-draft',
              'Draft: distinct Euclidean corner marks can collapse conformally',
              'For n>=81 put t=floor(sqrt(n)), a=t, b=2t+1, m=floor(n/2) and form the Jordan domain D_n from [0,a/n]x[0,1], [b/n,1]x[0,1], and the corridor [a/n,b/n]x[(m-1/2)/n,(m+1/2)/n], taking the interior of their union. Normalize the disk Riemann map f_n by f_n(0)=(1/2,1/2), f_n\'(0)>0. Its Jordan boundary extension satisfies |f_n^{-1}(0,1)-f_n^{-1}(0,0)|<=8/n. The boundary arc containing both corners lies behind a height-1/n gate at x=b/n. Brownian motion must hit this gate before exiting on that arc. The half-plane Poisson kernel bounds its harmonic measure by 1/[pi*n*(1/2-b/n)]<=4/(pi*n); the preimage arc has angular length <=8/n. Thus Euclidean corner convergence, even with unmarked kernel and boundary Hausdorff convergence, does not imply marked-prime-end convergence.',
              ['Jordan boundary extension', 'Normalized interior basepoint',
               'Brownian harmonic measure and its conformal invariance', 'n>=81']),
        entry('refuted-bridge', 'unmarked-domain-convergence-crossing-preservation-refuted-bridge-draft',
              'Draft warning: refuted unmarked crossing-preservation bridge',
              'The following auxiliary assertion is refuted by the boundary-neck construction: closure Hausdorff convergence, boundary Hausdorff convergence, area convergence, unmarked Caratheodory convergence to a fixed Jordan domain, and Euclidean convergence of four distinct boundary marks are sufficient to preserve critical square-lattice crossing probabilities of the marked arcs. These conditions alone do not control marked prime ends. This is a record of a false proposed bridge, not a theorem and not a refutation of conformal invariance for correctly marked approximations.',
              ['This entry describes a refuted auxiliary assertion',
               'No promotion to a theorem or a parent-problem solution']),
    ]
    relations = [
        {'from_key': 'boundary-neck', 'to_key': 'series-corridor', 'kind': 'depends_on',
         'rationale': 'The construction has exactly k mandatory corridor edges; its probability bound uses the exact series factorization.'},
        {'from_key': 'boundary-neck', 'to_key': 'refuted-bridge', 'kind': 'refutes',
         'rationale': 'It meets all five geometric and Euclidean-mark conditions while crossing tends to zero instead of the canonical square lower bound.'},
        {'from_key': 'prime-end-collapse', 'to_key': 'boundary-neck', 'kind': 'depends_on',
         'rationale': 'The gate and the trapped boundary arc are exactly those of the explicit Jordan neck family.'},
        {'from_key': 'prime-end-collapse', 'to_key': 'refuted-bridge', 'kind': 'semantic_association',
         'rationale': 'The 8/n boundary-preimage estimate identifies the omitted marked-prime-end hypothesis in the false bridge.'},
    ]
    bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w414',
              'bundle_slug': 'c0017-boundary-prime-end-collapse-w414-001',
              'entries': entries, 'relations': relations}
    required = {'key', 'namespace', 'logical_name', 'kind', 'title', 'statement',
                'proof_text', 'assumptions', 'domain', 'source'}
    keys = {e['key'] for e in entries}
    assert len(keys) == len(entries) <= 200
    for e in entries:
        assert required <= set(e)
        assert e['kind'] == 'concept' and e['proof_text'] is None
        assert e['statement'].startswith('DRAFT;')
        assert e['source']['license'].startswith('owner-own-work')
        assert 'pending' in e['statement']
    allowed = {'depends_on', 'defines', 'proves', 'refutes', 'generalizes',
               'specializes', 'analogous_to', 'cites', 'semantic_association'}
    for relation in relations:
        assert relation['from_key'] in keys and relation['to_key'] in keys
        assert relation['kind'] in allowed
        assert relation['from_key'] != relation['to_key']
    dependencies = {key: [] for key in keys}
    for r in relations:
        if r['kind'] == 'depends_on':
            dependencies[r['from_key']].append(r['to_key'])
    visited, active = set(), set()
    def visit(key):
        if key in visited:
            return
        assert key not in active, 'Dependency cycle'
        active.add(key)
        for dependency in dependencies[key]:
            visit(dependency)
        active.remove(key)
        visited.add(key)
    for key in keys:
        visit(key)
    text = json.dumps(bundle, ensure_ascii=False, indent=2) + '\n'
    destination = ROOT / 'bundle_001.json'
    destination.write_text(text, encoding='utf-8')
    receipt = {
        'recorded_at': datetime.now(timezone.utc).isoformat(),
        'local_bundle': str(destination), 'entries': len(entries),
        'relations': len(relations), 'concept_only': True,
        'dependency_graph_acyclic': True, 'local_validation': 'PASS',
        'validation_scope': 'Local shape/status/license/relation checks, not live integrator acceptance or mathematical review',
        'submitted': False, 'reviewed': False, 'ingested': False, 'retrievable': False,
        'cryptographic_manifest': 'Reserved for validating coordinator; no worker-generated manifests or source digests',
    }
    (ROOT / 'BUNDLE_STATE.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
