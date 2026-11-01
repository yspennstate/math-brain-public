"""Build reviewable math-only drafts; never invoke a live-store integrator."""
from pathlib import Path
import datetime as dt
import json

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w391')
STAMP = dt.datetime.now(dt.timezone.utc).isoformat()

def save(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def entry(key, logical, kind, title, statement, assumptions):
    return {'key':key,'namespace':'probability.fpp','logical_name':logical,'kind':kind,'title':title,'statement':statement,'proof_text':None,'assumptions':assumptions,'domain':'probability theory','source':{'source_id':f'owner-own-work:fpp-boundary-notes-20261010:{key}','url':'urn:math-work:fpp-boundary-notes:2026-10-10','revision':'draft-2026-10-10-pending-independent-review','license':'owner-own-work','excerpt':None}}

def main():
    audits = [json.loads(line) for line in (ROOT/'AUDIT_W390.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
    claims = [json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
    geometry = json.loads((ROOT/'GEOMETRY_RESULT.json').read_text(encoding='utf-8'))
    rows = json.loads((ROOT/'STORE_EXACT_ROWS.json').read_text(encoding='utf-8'))
    existing = {}
    for row in rows:
        record = row['record']
        if row['table']=='nodes':
            metadata = json.loads(record['metadata_json'])
            existing[metadata['logical_id']] = record['body']
    target = 'math:probability.core:open-problem-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp'
    prior = 'math:probability.core:attempt-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp'
    assert target in existing and prior in existing
    entries = [
        entry('def-bigeodesic','ambient-fpp-bi-infinite-geodesic-definition','definition','Global bi-infinite FPP geodesic',
              'Give each unoriented nearest-neighbor edge of Z^2 a finite nonnegative weight t_e, and let T(u,v) be the infimum of the weights of all finite walks from u to v, charging every edge traversal. A global bi-infinite geodesic is an injective adjacent-vertex sequence (v_k) indexed by all integers such that sum_{k=i}^{j-1} t_{v_k,v_{k+1}}=T(v_i,v_j) for every i<j. Competitors may leave any strip or region containing the sequence.',
              ['Undirected nearest-neighbor Z^2','Finite nonnegative edge weights']),
        entry('draft-atomic','draft-fpp-minimum-atom-bigeodesics-under-directed-survival','concept','DRAFT: minimum-atom bigeodesics under directed survival',
              'DRAFT author derivation, independent review pending. For iid weights equal to a>0 with probability p in (0,1) and b>a otherwise, suppose northeast directed bond percolation on the a-edges has positive forward survival probability theta(p). Then almost surely some global bi-infinite FPP geodesic exists. At the origin, forward and backward surviving-ray events depend on disjoint edge time levels and intersect with probability theta(p)^2. Their concatenation is monotone and every finite segment has Manhattan distance many a-edges, the minimum possible cost. Translation ergodicity upgrades positive probability of existence to probability one. This is a boundary obstruction to dropping nonatomicity, not a counterexample to the nonatomic-law target.',
              ['Independent identically distributed weights on undirected nearest-neighbor Z^2','Two-point law with 0<a<b<infinity and 0<p<1','Positive northeast directed open-ray survival probability theta(p)']),
        entry('draft-direction','draft-fpp-axis-direction-with-unbounded-strip-wandering','concept','DRAFT: axial direction with unbounded strip wandering',
              'DRAFT author derivation, independent review pending. In the constant weight-1 FPP environment, put f(k)=sign(k) floor(sqrt(abs(k))) for integers k, with f(0)=0. Join (k,f(k)) to (k+1,f(k)) horizontally and then move vertically at column k+1 to f(k+1). The resulting doubly infinite monotone staircase is a global geodesic: each finite segment has Manhattan-optimal length. Its two end directions are +e1 and -e1 because f(k)/abs(k) tends to zero, but neither tail lies eventually in any finite horizontal strip because f is unbounded at both ends. End directions alone therefore give no geometric finite-strip confinement. This example uses a constant law and does not refute a nonatomic iid theorem.',
              ['Undirected nearest-neighbor Z^2','Every edge has weight 1','The proposed bridge uses end directions alone']),
        entry('gap-confinement','fpp-thin-tube-obstruction-requires-bigeodesic-confinement-bridge','concept','Confinement gap in FPP thin-tube obstruction routes',
              'An absence theorem restricted to bigeodesic tails in deterministic thin horizontal or vertical tubes requires a further confinement theorem, or an obstruction for wider and adaptive wandering, before it can establish unrestricted absence. Countable intersections over fixed finite widths do not cover a path whose transverse displacement is unbounded. A directional limit permits unbounded sublinear transverse displacement. The separate compactness route, taking limits of geodesics between opposite distant endpoints, likewise needs anchoring near a bounded region; endpoints on opposite sides alone allow the connecting paths to escape every fixed ball. These are missing bridge premises, not refutations of absence for nonatomic iid planar FPP.',
              ['Ambient nearest-neighbor Z^2 FPP','The available absence theorem covers only specified deterministic tubes','No additional bigeodesic confinement or tightness premise is assumed']),
    ]
    relations = [
        {'from_key':'draft-atomic','to_key':'def-bigeodesic','kind':'depends_on','rationale':'The minimum-atom construction checks every finite segment against the ambient metric.'},
        {'from_key':'draft-direction','to_key':'def-bigeodesic','kind':'depends_on','rationale':'The staircase is a global bigeodesic by the Manhattan lower bound.'},
        {'from_key':'gap-confinement','to_key':'def-bigeodesic','kind':'depends_on','rationale':'The unrestricted path quantifier refers to global bigeodesics.'},
        {'from_key':'gap-confinement','to_key':'draft-atomic','kind':'semantic_association','rationale':'A local tube obstruction does not establish absence for all nonconstant atomic laws; the directed-survival example identifies that scope boundary.'},
        {'from_key':'gap-confinement','to_key':'draft-direction','kind':'semantic_association','rationale':'An axial end direction can coexist with unbounded transverse displacement in the stated constant-law example.'},
        {'from_key':'gap-confinement','to_existing_logical':target,'kind':'cites','rationale':'The stored P0117 target is the nonatomic iid planar absence question; the boundary examples and partial routes leave its unrestricted quantifier unresolved here.'},
        {'from_key':'gap-confinement','to_existing_logical':prior,'kind':'cites','rationale':'The exact prior-attempt card records the separate anchoring/tightness obstruction in a finite-geodesic compactness route.'},
    ]
    bundle = {'spec':'mathbrain-draft-v1','author_agent':'w391','bundle_slug':'fpp-boundary-obstructions-20261010','entries':entries,'relations':relations}
    by_key = {e['key']:e for e in entries}
    allowed = {'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
    evidence = []
    for relation in relations:
        assert relation['from_key'] in by_key and relation['kind'] in allowed
        to_quote = by_key[relation['to_key']]['statement'] if 'to_key' in relation else existing[relation['to_existing_logical']]
        evidence.append({'relation':relation,'from_quote':by_key[relation['from_key']]['statement'],'to_quote':to_quote,'status':'draft relation; mathematical acceptance pending'})
    for e in entries:
        assert e['kind'] in {'definition','concept'} and e['proof_text'] is None
        assert e['source']['license'].startswith('owner-own-work')
        text = json.dumps(e)
        assert 'C:/' not in text and 'C:\\' not in text and 'w391' not in text
    # All dependency arrows end at the definition, so the dependency graph is acyclic.
    assert all(r['to_key']=='def-bigeodesic' for r in relations if r['kind']=='depends_on')
    (ROOT/'bundles').mkdir(exist_ok=True)
    own = ROOT/'bundles'/'bundle_001.json'
    save(own,bundle)
    (ROOT/'RELATION_EVIDENCE.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in evidence),encoding='utf-8')
    INBOX.mkdir(parents=True,exist_ok=True)
    destination = INBOX/'bundle_001.json'
    complete = own.read_bytes()
    if destination.exists():
        if destination.read_bytes()!=complete:
            raise RuntimeError('Existing inbox draft differs; refusing to overwrite')
    else:
        part = INBOX/'bundle_001.part'
        part.write_bytes(complete)
        part.rename(destination)
    submission = {'at_utc':STAMP,'draft_path':destination.as_posix(),'entries':len(entries),'relations':len(relations),'submitted':True,'reviewed':False,'ingested':False,'retrievable':False,'state_meaning':'Flags mean separately verified receipts. Review pending; ingestion and new-card retrieval not verified. No live integrator invoked.'}
    save(ROOT/'SUBMISSION_STATUS.json',submission)
    summary = {'audited_claims':len(audits),'KEEP':sum(r['verdict']=='KEEP' for r in audits),'FIX':0,'DROP':0,'auditor':'w391','second_auditor':'w392 pending','full_target_established':False}
    save(ROOT/'AUDIT_W390.summary.json',summary)
    hook = {'id':'math-w391-01','area':'math','event':'stage-start','cue':'An argument concludes unrestricted FPP bigeodesic absence from fixed-strip barriers or end directions without a confinement premise.','fire_when':'The conclusion says all bigeodesics are absent while the proved lemma covers only fixed strips or deterministic thin tubes.','silent_when':'The conclusion states only the logarithmically thin-tube special case and explicitly records unrestricted wandering as the gap, as in the audited paired proof.','text':'A thin-tube obstruction needs a confinement bridge before excluding every bigeodesic. Check widths and trap probabilities. An end direction permits unbounded sublinear wandering; preserve the nonatomic-law hypothesis.','evidence':'perceptron_proof_open_gaps_fleet_2026_07_12; AUDIT_W390.jsonl w390-T3 and w390-C4; GEOMETRIC_BRIDGE_COUNTEREXAMPLE.md','proposer':'w391'}
    assert len(hook['text'])<=300
    (ROOT/'hooks').mkdir(exist_ok=True)
    hook_text = json.dumps(hook,ensure_ascii=False)+'\n'
    (ROOT/'hooks'/'math-w391.jsonl').write_text(hook_text,encoding='utf-8')
    (ROOT/'patches').mkdir(exist_ok=True)
    live = '~/primary_directive/hooks1000/proposals/math-w391.jsonl'
    (ROOT/'patches'/'01_math_scope_hook.diff').write_text(f'--- a/{live}\n+++ b/{live}\n@@ -0,0 +1 @@\n+{hook_text}',encoding='utf-8')
    status = json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    status['sources'].append({'role':'canonical math-store target and prior attempt','path':'~/math-brain-build/local/population/brain.sqlite3','access':'sqlite mode=ro','evidence':'STORE_EXACT_ROWS.json','exact_logical_cards':len(existing),'matching_sql_rows':len(rows),'status':'Read only exact IDs in nodes/claims; no store writes'})
    save(ROOT/'SOURCE_STATUS.json',status)
    measure = {'at_utc':STAMP,'peer_audit':summary,'own_author_proof_claims':len(claims),'draft_entries':len(entries),'draft_relations':len(relations),'relation_endpoints_resolved':len(evidence),'exact_existing_logical_cards':len(existing),'geometry':geometry,'is_math_proof_receipt':False,'live_store_changes':0}
    save(ROOT/'VALIDATION.json',measure)
    geometry_note = f"Finite geometry checks: {geometry['state']}; {geometry['endpoint_cases']} endpoint cases. "
    if geometry['state'].startswith('NOT_RUN'):
        geometry_note += 'The fresh resource gate declined; no finite-test PASS is claimed.'
    else:
        geometry_note += f"{geometry['pairwise_support_checks']} disjoint-support checks passed. These finite checks do not prove the infinite-volume claims."
    packet = f'''# P0117 boundary review packet

Five adversarial KEEP verdicts for the paired thin-tube proof are in AUDIT_W390.jsonl. The independent derivation was saved before reading that proof. This is one independent audit; a second account's acceptance remains separate.

The paired result assumes finite nonnegative nonconstant iid weights on ambient nearest-neighbor Z^2. Choose 0<=l<h with p_l=P(t<=l)>0 and p_h=P(t>=h)>0. Put K=1+4l/(h-l) and C=2K log(1/p_h)+(K+4)log(1/p_l). It excludes every geodesic ray tail in a deterministic nondecreasing tube w(n) with limsup w(n)/sqrt(log n)<1/sqrt(C), and yields the simultaneous transverse lower bound. The cut, connector, disjoint-support, dyadic and countable-quantifier obligations all survived this audit. No optimal coefficient or scale is established.

Own exact claims and proofs are in CLAIMS.jsonl, INDEPENDENT_DERIVATION.md and GEOMETRIC_BRIDGE_COUNTEREXAMPLE.md. Please independently check these four claims:

1. C01: a constant finite law c>=0 admits a horizontal bigeodesic, by the Manhattan edge-count bound.
2. C02: the separately derived finite-strip estimate has L=floor(a(4w+2)/(b-a))+1 and q=P(t>=b)^((2w+1)L) P(t<=a)^(L+4w+2). The column-0 to column-n strip-crossing probability is <=(1-q)^floor((n+1)/(L+1)); eventual confinement in any finite axis-aligned strip is excluded simultaneously. No moment or nonatomicity assumption is used.
3. C03: a nondegenerate two-point law with 0<a<b and positive directed survival theta(p) admits bigeodesics almost surely. Check forward/backward edge-set independence, monotonicity of every finite segment, and translation ergodicity. The positive-survival premise is explicit; no numerical oriented-percolation threshold is asserted.
4. C04: the constant-weight staircase f(k)=sign(k) floor(sqrt(abs(k))) has axial end directions and unbounded transverse displacement at both ends. This refutes a geometric direction-to-finite-strip bridge, not a model-specific nonatomic theorem.

The single hardest full-target gap is confinement: nothing here forces a candidate bigeodesic to have a tail in the covered tubes, or supplies obstructions for wider/adaptively wandering candidates. Atomic and constant-law examples violate nonatomicity and therefore do not refute P0117. The earlier compactness route separately lacked anchoring near a fixed bounded region.

SOURCE_STATUS.json recovers the exact historical question and the explicit working moment version. A September 24, 2026 primary manuscript claims the full standard-moment target. Its first two pages were read, but its full proof and independent acceptance were not audited. Current openness and novelty remain UNKNOWN; do not advertise P0117 as currently open from the old ranking alone.

{geometry_note}

Structural validation: {len(entries)} draft entries, {len(relations)} allowed relations with exact supporting ends, {len(existing)} existing logical cards verified by exact-ID read-only SQL. All new results are concepts marked DRAFT with independent review pending. No theorem promotion, live-store integration, formal verification, admitted placeholder or hash-as-proof claim is made. Submitted, reviewed, ingested and retrievable receipts are separate in SUBMISSION_STATUS.json.

Brain draft: {destination.as_posix()}. Local identical draft: bundles/bundle_001.json. One hook is staged in hooks/math-w391.jsonl and patches/01_math_scope_hook.diff within the worker boundary.

Reviewer: w392 for own new results; any result originated by that referee needs w395's independent check.

NEXT: Independently check C03's directed-survival construction and C04's geometric scope, then decide the draft concepts and the paired proof within their exact assumptions.
'''
    (ROOT/'REVIEW_PACKET.md').write_text(packet,encoding='utf-8')
    report = f'''Saved five scoped KEEP verdicts for the paired thin-tube proof. Its detour, independence, dyadic limit and simultaneous-ray quantifiers are sound within the stated deterministic tube scope. The full-target confinement bridge remains missing. Independent constant-law, conditional minimum-atom, finite-strip and axial-staircase derivations are saved for w392.

Measurements from `python -X utf8 package_results.py`: {len(audits)} audited claims, {summary['KEEP']} KEEP; {len(claims)} own author-proof claims; {len(entries)} submitted DRAFT entries; {len(relations)} allowed relations with supporting ends; {len(existing)} exact canonical logical cards recovered through read-only SQL. {geometry_note} Reproduce the fresh gate/check with `python -X utf8 geometry_check.py`; the receipt is GEOMETRY_RESULT.json. Structural receipts are not mathematical proof or a recall-quality benchmark. No measured recall improvement is claimed: brain changes remain draft proposals.

The recent primary manuscript claims the full moment-version target; it was not fully audited, so current openness and novelty are UNKNOWN. Own claims are pending independent review. The bundle uses concept/draft labels and owner-own-work sources. Ingestion and retrieval of new cards have not been verified.

Apply: the validating coordinator reviews C01-C04 and the draft at ~/math-brain-inbox/w391/bundle_001.json before ingestion; append the single staged hook line using patches/01_math_scope_hook.diff at its named live proposal path. No live code or store was edited by this worker.

NEXT: w392 independently checks C03 and C04 and returns exact-scope verdicts; coordinator records later ingestion and retrieval receipts separately.
'''
    (ROOT/'REPORT.md').write_text(report,encoding='utf-8')
    print(json.dumps(measure,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
