import difflib
import hashlib
import json
from pathlib import Path
from time import perf_counter

ROOT = Path(__file__).resolve().parent
INTAKE = Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl')
INBOX = Path('~/math-brain-inbox/w496')

def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

start = perf_counter()
matches = []
with INTAKE.open(encoding='utf-8') as f:
    for line_no, line in enumerate(f, 1):
        if 'C0120' in line:
            row = json.loads(line)
            if row.get('problem_id') == 'C0120':
                matches.append((line_no, line.rstrip('\n'), row))
assert len(matches) == 1
line_no, original_line, before = matches[0]
after = dict(before)
after['statement'] = ('For independent standard Gaussian vertex weights on Z^2, let M_n be the maximum total weight over paths with n vertices starting at (0,0), with each step right or up and the endpoint free. Prove that there exist epsilon in (0,1) and C<infinity independent of n such that Var(M_n)<=C n^(1-epsilon) for all n>=2, improving the n/log n bound in Theorem 8.1 of the cited source.')
after['locator'] = 'Section 8, Theorem 8.1, pp. 37-39; Section 12, problem (3), p. 59'
after['status_search'] = ('Source-scope correction drafted 2026-10-10. The 2008 citation concerns a Gaussian free-endpoint ground-state maximum in Z^2. Positive-temperature log Z_n and higher-dimensional/general-disorder statements require separate sources. Current openness is UNKNOWN: scoped recent-literature and owner-artifact checks are not a complete novelty/status certification. No power improvement is established in this packet.')
after['verification'] = 'unreviewed'
save(ROOT / 'source_row_before.json', before)
save(ROOT / 'source_row_after.json', after)
after_line = json.dumps(after, ensure_ascii=False)
live_relative = INTAKE.relative_to(Path('~')).as_posix()
diff = ''.join(difflib.unified_diff([original_line+'\n'], [after_line+'\n'], fromfile='a/'+live_relative, tofile='b/'+live_relative))
diff = diff.replace('@@ -1 +1 @@', f'@@ -{line_no} +{line_no} @@')
patch = ROOT / 'patches/01_c0120_source_scope.diff'
patch.parent.mkdir(exist_ok=True)
patch.write_text(diff, encoding='utf-8')

# Reproducible source-coverage measurement, not a mathematical proof or recall benchmark.
def coverage(text):
    return {
        'ground_state_observable': 'M_n' in text and 'maximum' in text,
        'iid_standard_gaussian_disorder': 'independent standard Gaussian' in text,
        'two_dimensional_source_model': 'Z^2' in text and 'general dimension' not in text,
    }
checks_before = coverage(before['statement'])
checks_after = coverage(after['statement'])
assert all(checks_after.values())
assert original_line != after_line

claims_path = ROOT / 'CLAIMS.jsonl'
claims = [json.loads(s) for s in claims_path.read_text(encoding='utf-8').splitlines() if s.strip()]
for row in claims:
    if row['id'] == 'w496-C0120-006':
        row['proof'] = ('Independent root Gaussian plus sqrt(n-1) times a maximum of n Gaussians; separated quantile events and Mills bounds give a c/log n variance lower bound for that maximum; a bivariate Gaussian tail union bound gives the vanishing-noise overlap estimate.')
claims_path.write_text(''.join(json.dumps(c, ensure_ascii=False)+'\n' for c in claims), encoding='utf-8')

def concept(key, logical, title, statement, assumptions, artifact):
    return {
        'key':key, 'namespace':'probability.polymers', 'logical_name':logical,
        'kind':'concept', 'title':title, 'statement':statement,
        'proof_text':None, 'assumptions':assumptions, 'domain':'probability theory',
        'source':{
            'source_id':'owner:w496:C0120:'+key,
            'url':str(ROOT / artifact).replace('\\','/'),
            'revision':'draft-as-written-2026-10-10',
            'license':'owner-own-work (campaign draft; independent review pending)',
            'excerpt':None,
        },
    }

entries = [
    concept('source-model','c0120-gaussian-ground-state-source-scope-draft',
        'C0120 primary-source model: draft scope correction',
        'Source-scope audit draft, awaiting independent review: the cited arXiv:0810.4221v2 Section 8 concerns M_n, the maximum sum of iid standard Gaussian weights over n-vertex up-right paths from the origin in Z^2 with a free endpoint. Its logarithmic variance bound is for M_n. The intake replacement by an arbitrary-dimensional log partition function needs a separate source. A power improvement for this precise M_n is not proved here; current openness is UNKNOWN.',
        ['Historical citation arXiv:0810.4221v2; not a current-openness certification'], 'SOURCE_STATUS.json'),
    concept('spectral-criterion','gaussian-directed-path-polynomial-chaos-cutoff-draft',
        'Polynomial chaos cutoff for Gaussian path variance: draft reduction',
        'Draft conditional reduction, not an independently certified theorem: let v_nk be the degree-k Gaussian chaos variance of the centered source-model M_n. The path-indicator gradient has squared norm n almost surely, giving sum k v_nk=n. Hence Var(M_n)<=sum_{k<=K}v_nk+n/(K+1). A bound sum_{k<=ceil(n^delta)}v_nk<=C n^(1-delta), for fixed 0<delta<1 uniformly in n, would give a power variance improvement. This low-chaos-mass input remains unproved.',
        ['Finite free-endpoint n-vertex up-right paths', 'iid standard Gaussian vertex environment', 'Gaussian first-order Sobolev Hermite identity'], 'INDEPENDENT_DERIVATION.md'),
    concept('layer-average','gaussian-directed-path-layer-average-split-draft',
        'Independent Gaussian layer averages: draft exact decomposition',
        'Draft lemma awaiting independent review: in the source model let A_t be the mean weight of the t+1 vertices on x+y=t, and R_v=g_v-A_t on that layer. Joint Gaussianity and zero cross covariance make the entire vector of A_t independent of the entire R vector. Every path visits one vertex per layer, so M_n(g)=sum_t A_t+M_n(R) and Var(M_n)=H_n+Var(M_n(R)), with H_n=sum_{j=1}^n 1/j. Residual weights within each layer are correlated; the split supplies no residual upper bound.',
        ['iid N(0,1) vertex weights', 'n vertices starting at the origin and moving up/right', 'Layers t=0,...,n-1'], 'INDEPENDENT_DERIVATION.md'),
    concept('hermite-control','fixed-degree-gaussian-chaos-suppression-no-power-control-draft',
        'Fixed-degree suppression alone: draft spectral counterexample',
        'Draft counterexample awaiting independent review: for k_n=ceil(log n), normalized probabilists Hermite polynomial H_k and G~N(0,1), F_n=sqrt(n/k_n) H_k_n(G) has variance n/k_n and Gaussian Dirichlet energy n. Every fixed chaos degree eventually vanishes, and normalized gradient covariance tends to zero at every fixed positive Ornstein-Uhlenbeck time, yet no fixed power variance bound follows. This example is not a convex or Lipschitz polymer maximum.',
        ['n>=2', 'Normalized Hermite polynomials', 'General Gaussian Sobolev functions; not the source lattice class'], 'INDEPENDENT_DERIVATION.md'),
    concept('fan-control','gaussian-fan-path-qualitative-chaos-no-power-control-draft',
        'Qualitative chaos without a power gain: draft Gaussian fan control',
        'Draft counterexample awaiting independent review: on the graph with a common root and n disjoint branches of n-1 vertices with iid standard Gaussian weights, the maximum n-vertex path sum is convex and sqrt(n)-Lipschitz, with path-indicator gradient of squared norm n. It has normalized expected overlap tending to zero at Ornstein-Uhlenbeck time u_n=16 log(log n)/log n, yet Var(M_n)>=c n/log n for all sufficiently large n and some c>0. Thus these structural facts alone do not yield a power bound. The growing-degree fan is not Z^2; fixed lattice geometry may provide the missing quantitative premise.',
        ['n large enough that u_n>0 and the Mills-bound quantile b_n>=1', 'A different fan graph for each n; root degree n', 'Not a counterexample to C0120 on Z^2'], 'GAUSSIAN_FAN_OBSTRUCTION.md'),
]
relations = [
    {'from_key':'spectral-criterion','to_key':'source-model','kind':'depends_on','rationale':'The spectral identity uses the Gaussian path maximum and its path-indicator gradient specified by the source-model concept.'},
    {'from_key':'layer-average','to_key':'source-model','kind':'depends_on','rationale':'The layer sizes t+1 and exactly one visited vertex per layer come from this two-dimensional up-right source model.'},
    {'from_key':'fan-control','to_key':'hermite-control','kind':'analogous_to','rationale':'Both give variance lower bounds of logarithmic rather than fixed-power scale while displaying qualitative Gaussian decorrelation; the fan also preserves convexity and a bounded path-indicator gradient.'},
    {'from_key':'fan-control','to_key':'spectral-criterion','kind':'semantic_association','rationale':'The fan control shows why a qualitative overlap statement cannot supply the quantitative polynomial cutoff required by the reduction; it does not disprove that cutoff for the lattice model.'},
]
bundle = {'spec':'mathbrain-draft-v1','author_agent':'w496','bundle_slug':'c0120-independent-spectral-fan-controls-001','entries':entries,'relations':relations}
allowed_relations = {'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
keys = {e['key'] for e in entries}
assert len(keys)==len(entries) and len(entries)<=200
for e in entries:
    assert e['kind']=='concept' and e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work')
    assert e['statement'] and e['assumptions']
for r in relations:
    assert r['kind'] in allowed_relations and r['from_key'] in keys and r['to_key'] in keys
save(ROOT / 'bundle_001.json', bundle)
INBOX.mkdir(parents=True, exist_ok=True)
destination = INBOX / 'bundle_001.json'
if not destination.exists():
    part = INBOX / 'bundle_001.json.part'
    save(part, bundle)
    part.rename(destination)
else:
    assert json.loads(destination.read_text(encoding='utf-8')) == bundle, 'Existing inbox bundle differs: do not overwrite.'

hook = {'id':'c0120-w496-01','area':'math','event':'stage-start',
    'cue':'source_id=chatterjee_chaos_2008 and its cited conclusion is stated for log Z or general dimension',
    'fire_when':'The C0120 intake row 120 cites Chatterjee Section 8 for Var(log Z_n) in general dimension.',
    'silent_when':'The argument states the Gaussian Z^2 ground-state maximum, or cites a separate positive-temperature theorem with its own assumptions.',
    'text':'Check the observable, dimension and temperature in the primary statement: the 2008 polymer theorem cited by C0120 concerns a Gaussian path maximum in Z^2. A log-partition or higher-dimensional extension needs its own source.',
    'evidence':'~/brain_workers/w496/SOURCE_STATUS.json; w496-C0120-002; source coverage 0/3 to 3/3.',
    'proposer':'w496'}
assert len(hook['text'])<=300
(ROOT / 'HOOK_PROPOSAL.jsonl').write_text(json.dumps(hook,ensure_ascii=False)+'\n',encoding='utf-8')

measurement = {
    'command':'python -X utf8 ~/brain_workers/w496/build_review_packet.py',
    'source_row_line':line_no, 'source_coverage_before':checks_before,'source_coverage_after':checks_after,
    'coverage_passes_before':sum(checks_before.values()),'coverage_passes_after':sum(checks_after.values()),
    'coverage_total':3,'claim_rows':len(claims),'audited_peer_claims':len([s for s in (ROOT/'AUDIT_w495.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]),
    'draft_entries':len(entries)+(len(json.loads((ROOT/'bundle_002.json').read_text(encoding='utf-8'))['entries']) if (ROOT/'bundle_002.json').exists() else 0),
    'draft_relations':len(relations)+(len(json.loads((ROOT/'bundle_002.json').read_text(encoding='utf-8'))['relations']) if (ROOT/'bundle_002.json').exists() else 0),
    'theorem_or_lemma_entries':0,'source_row_patch_hunks':1,
    'elapsed_seconds':round(perf_counter()-start,6),
    'meaning':'Source-assumption coverage and packet-format checks only; no stochastic experiment, proof certificate, deployed recall gain or live-store improvement claimed.',
}
save(ROOT / 'MEASUREMENTS.json',measurement)
save(ROOT / 'BRAIN_SUBMISSION.json',{
    'bundle_path':str(destination).replace('\\','/'),
    'bundle_paths':[str(destination).replace('\\','/'),str(INBOX/'bundle_002.json').replace('\\','/')] if (ROOT/'bundle_002.json').exists() else [str(destination).replace('\\','/')],
    'submitted':True, 'reviewed':False, 'ingested':'NOT_CONFIRMED','retrievable':'NOT_CONFIRMED',
    'independent_referee':'w497', 'promotion':'All entries are concepts/drafts; no theorem promotion.',
    'integration_owner':'Validating coordinator; this worker did not invoke the live-store integrator.',
})
artifacts = ['CLAIMS.jsonl','SOURCE_STATUS.json','INDEPENDENT_DERIVATION.md','GAUSSIAN_FAN_OBSTRUCTION.md','AUDIT_w495.jsonl','AUDIT_W495_PROOF.md','patches/01_c0120_source_scope.diff']
artifacts += [name for name in ['POLYNOMIAL_NOISE_QUANTIFIER.md','STORE_CORRECTION.json'] if (ROOT/name).exists()]
hashes = {name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in artifacts}
save(ROOT / 'review/ARTIFACT_HASHES.json',{'purpose':'Review snapshot hashes, not a store seal or bundle manifest','sha256':hashes,'served_model_evidence':'UNVERIFIED: requested settings do not attest served identity; no profile/credential file read.'})
print(json.dumps(measurement,ensure_ascii=False))
