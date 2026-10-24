"""Assemble review-only C0047 artifacts. Never ingest a store or modify live code."""
from pathlib import Path
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
NS = 'probability.percolation'
claims = [json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
brain = json.loads((ROOT/'BRAIN_RETRIEVAL.json').read_text(encoding='utf-8'))
prior = next(row for row in brain['rows'] if row['title'].startswith('Attempt on Benjamini-Schramm conjecture:'))
problem = next(row for row in brain['rows'] if row['title'].startswith('Open problem: Benjamini-Schramm conjecture:'))
prior_logical = json.loads(prior['metadata_json'])['logical_id']
problem_logical = json.loads(problem['metadata_json'])['logical_id']
measure = json.loads((ROOT/'MEASUREMENTS.json').read_text(encoding='utf-8'))
source_receipts = []
for filename in ('FETCH_RECEIPTS.json','ADDITIONAL_FETCH_RECEIPTS.json'):
    file = ROOT/'sources'/filename
    if file.exists():
        source_receipts.extend(json.loads(file.read_text(encoding='utf-8')))

target = ('For every infinite finitely generated group Gamma and every prescribed finite symmetric generating set S excluding identity, let G be its simple undirected Cayley graph. Under independent Bernoulli bond percolation, pc(G)<pu(G) if and only if Gamma is nonamenable. pc is the infimum of p for which the root has positive probability of an infinite cluster; pu is the infimum of p for which there is almost surely exactly one infinite cluster.')
status = {
    'candidate_id':'C0047', 'agent':'w561', 'checked_on':'2026-10-10',
    'exact_target': target,
    'historical_status':'1996 Conjecture 6; 2018 Conjecture 2; dated intake attempted_unsolved',
    'current_openness':'UNKNOWN',
    'recent_primary_claim': {
        'title':'Nonuniqueness of percolation on nonamenable quasi-transitive graphs',
        'author':'OpenAI', 'manuscript_date':'2026-09-24',
        'scope':'Theorem 1.1 and Corollary 1.2 include the full bond target and the critical two-point operator bound for every prescribed Cayley generating set.',
        'mathematical_review':'NOT independently audited in this packet',
        'implementation':'Module OAI.Probability.BenjaminiSchramm.Main declares OAI.Percolation.BenjaminiSchramm.full_main and OAI.Percolation.BenjaminiSchramm.critical_bounded_unconditional; top-level file has no sorry.',
        'comparator':'Challenge declarations intentionally contain sorry; they are specifications, not implementation proof receipts.',
        'formal_check_receipt':None,
        'permitted_axioms_in_config':['propext','Quot.sound','Classical.choice'],
        'actual_trusted_axioms':'UNKNOWN: no compiled print-axioms/comparator receipt was produced.',
        'conclusion':'A primary claimed resolution is located; this packet does not certify either current openness or a completed solution.'},
    'primary_sources': source_receipts,
    'other_primary_checks': [
        {'url':'https://arxiv.org/html/1712.04651','locator':'Conjecture 2, original PDF p.4','result':'Exact Cayley-graph universal formulation checked; cited intake raw source corroborates it.'},
        {'url':'https://arxiv.org/html/1804.10191','locator':'Theorem 2.1; Lemma 2.4; Remark 2.5; Section 2','result':'Hyperbolic theorem requires Gromov hyperbolicity; operator continuation and normalized adjacency identity checked.'},
        {'path':str(ROOT/'sources/benjamini_schramm_1996.pdf'),'locator':'Printed pp.72 and 76','result':'Standing model is site; authors extend nonplanar questions to bond. Conjecture 6 and correctly normalized Theorem 4 verified.'}],
    'bounded_prior_search': {
        'intake':'C0047-A001 recovered exactly and canonical population card recovered read-only.',
        'attempts_H_20260912':'No C0047 hit in scoped ID grep.',
        'attempts_I_20260914':'No C0047 hit in scoped ID grep.',
        'lean_20260908':'C0047 ranking references only; no proof receipt found in scoped search.',
        'Team_O':'No C0047 row; related P0041 assigned to w336. Our scope is a conditional operator lemma and normalization audit.',
        'owner_percolation_archive':'No targeted percolation/Schramm/C0047 filename hit; this does not certify absence of prior owner solutions.'},
    'parent_solution_claim':False,
    'hardest_remaining_gap_in_our_attempt':'Uniform finiteness of ||T_pc|| for every prescribed nonamenable Cayley graph; the recent manuscript claims this but is not independently verified here.',
}
(ROOT/'SOURCE_STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'MODEL_EVIDENCE.json').write_text(json.dumps({
    'agent':'w561','requested':{'model':'gpt-6.1-sol','reasoning':'max','service_tier':'Fast','pool':'acc2/proofswarm'},
    'served_model':'UNKNOWN','response_side_evidence':None,'native_thread_id':None,
    'reviewer':'w563','reviewer_served_model':'UNKNOWN',
    'limitations':'Requested settings, pool labels, and turn context are not response-side served-model evidence. No independent different-model certification is asserted.'},indent=2),encoding='utf-8')

preface = f'''# Verified target and source status

{target}

The historical formulation is verified in Benjamini–Schramm (1996), printed p.76, Conjecture 6. Their standing model is site percolation, and printed p.72 extends the nonplanar questions to bond percolation. Duminil-Copin's 2018 Conjecture 2 gives the exact Cayley formulation. This packet attempts the bond version only. Current openness is UNKNOWN: a September 24, 2026 primary manuscript and implementation claim the general result, but no independent mathematical or compiled formal verification is supplied here. See SOURCE_STATUS.json for exact URLs, hashes, and limits.

Prior digest: C0047-A001 and the canonical attempt card are unreviewed concepts, not theorems. They describe normalized random-walk rho but omit degree in the spectral route. The source's Theorem 4 requires rho*k*p<1, with k the maximum degree. On a regular Cayley graph this becomes rho*d*p<1. The prior proposed remaining case pc>=1/rho is impossible when 0<rho<1 and pc<=1. Replacing the generating set addresses an existential generating-set statement and does not prove the prescribed-generating-set target.

| Retrieved result or source | Full relevant hypotheses | Missing for the target |
| --- | --- | --- |
| Population C0047 problem and attempt cards | kind=concept; truth_status=unverified; no independent proof | They supply a question and a failed route, not a usable theorem |
| Hutchcroft Theorem 2.1 | Infinite connected locally finite quasi-transitive nonamenable Gromov hyperbolic graph; Bernoulli bond percolation | Gromov hyperbolicity is not assumed for a general group |
| L02 continuation | Countable simple graph of bounded degree; a=adjacency l2 norm>0; finite two-point norm M at p0<1 | Finite M at pc is the unproved general estimate |
| L03 uniqueness obstruction | Infinite countable vertex-transitive bounded-degree simple graph; Bernoulli bond law | Target satisfies these; it does not supply M |
| L05 spectral criterion | Same graph/law; pc*||A||<1 | Stronger condition can fail even on T4 |
| September 2026 Theorem 1.1 / Corollary 1.2 | Infinite connected locally finite nonamenable quasi-transitive graph; bond law; every prescribed Cayley generating set in the corollary | Its mathematical proof and transitive formal axioms remain unaudited here |

The quantitative L02 bound below is a reproduced operator argument. Hutchcroft's Lemma 2.4 and Remark 2.5 discuss the continuation and removal of a weaker sprinkling factor. No novelty claim is made for L01–L05.

'''
attempt = (ROOT/'ATTEMPT.md').read_text(encoding='utf-8')
if not attempt.startswith('# Verified target and source status'):
    attempt = preface + attempt.replace('Current general target (primary verification pending):','Initial target checkpoint (now verified above):')
    (ROOT/'ATTEMPT.md').write_text(attempt,encoding='utf-8')

correction = {
    'id':'S1.w561.C0047.normalization','kind':'source-statement-correction','status':'DRAFT-unreviewed',
    'source_node':prior['id'],'source_logical':prior_logical,
    'source_end_quote':'Need p_c(G) < 1/rho(G) or another uniform criterion for every Cayley graph of every non-amenable group.',
    'corrected_statement':'For Bernoulli bond percolation on a d-regular infinite vertex-transitive graph, the adjacency-Neumann sufficient criterion is pc*d*rho<1, with rho the normalized simple-random-walk spectral radius. It is not a necessary criterion. pc<1/rho is automatic for rho<1 and does not supply the missing critical-operator bound.',
    'primary_source':'Benjamini-Schramm 1996, Theorem 4, printed p.76; spectral condition rho(G)*k*p<1.',
    'proof_or_counterexample':'ATTEMPT.md L04–L05: T4 has pc=1/3, rho=sqrt(3)/2, pc*d*rho=2sqrt(3)/3>1, yet pc<pu=1.',
    'target_end_quote':'For a d-regular graph ||A||=d rho, so the sufficient criterion is p_c d rho<1.',
    'independent_reviewer':'w563 pending','remaining_gap':'General critical operator boundedness and independent verification of the September 2026 full claim.'}
(ROOT/'SOURCE_CORRECTIONS.jsonl').write_text(json.dumps(correction,ensure_ascii=False)+'\n',encoding='utf-8')

entries = []
def entry(key, logical, title, statement, kind='concept', assumptions=None):
    entries.append({'key':key,'namespace':NS,'logical_name':logical,'kind':kind,'title':title,
        'statement':statement,'proof_text':None,'assumptions':assumptions or [],'domain':'probability theory / independent bond percolation',
        'source':{'source_id':'owner-probability-campaign-w561-20261010:'+key,
                  'url':'','revision':'review-draft-2026-10-10-r2','license':'owner-own-work','excerpt':None}})
entry('def-two-point','bernoulli-bond-two-point-operator-counting-measure',
      'Bernoulli bond two-point operator on counting measure',
      'Let G be a countable simple graph with uniformly bounded degree. In independent Bernoulli bond percolation at p in [0,1], tau_p(x,y)=P_p(x is connected to y by a finite open path), allowing the path of length zero. T_p has matrix tau_p and initially acts on finitely supported functions on V. Boundedness means extension to a bounded operator on l2(V) with counting measure. Let p_2->2=sup{p:T_p is bounded}; for infinite connected vertex-transitive G, pc=inf{p:P_p(|C(o)|=infinity)>0} and pu=inf{p:P_p(exactly one infinite cluster)=1}.',
      kind='definition',assumptions=['Countable simple graph','Uniformly bounded degree','Independent Bernoulli bond law'])
for claim_id,key,logical,title in [
    ('L01','tree-reference','draft-regular-tree-bond-threshold-reference','Draft regular-tree threshold reference'),
    ('L02','norm-continuation','draft-quantitative-two-point-operator-continuation','Draft quantitative two-point operator continuation'),
    ('L03','uniqueness-obstruction','draft-uniqueness-obstruction-to-two-point-l2-boundedness','Draft uniqueness obstruction to operator boundedness'),
    ('L04','normalization-refutation','draft-normalized-spectral-and-exponential-decay-route-refutation','Draft refutation of two insufficient spectral routes'),
    ('L05','spectral-criterion','draft-correctly-normalized-sufficient-percolation-spectral-criterion','Draft correctly normalized sufficient spectral criterion')]:
    claim = next(c for c in claims if c['id'].endswith(claim_id))
    statement = 'DRAFT mathematical statement, author-checked and awaiting independent review: '+claim['statement']
    if claim_id=='L04':
        statement += ' On T4 at p=3/4 the squared root-column norm is 1+4p^2 sum_{n>=0}(3p^2)^n and diverges since 3p^2=27/16>1, although tau_p=p^distance decays exponentially. The adjacency norm is 2sqrt(3), normalized rho=sqrt(3)/2 and pc=1/3. This refutes the insufficient operator inference, not the parent conjecture.'
    entry(key,logical,title,statement,assumptions=claim['assumptions'])
entry('critical-gap','draft-c0047-critical-operator-missing-bridge',
      'C0047 critical operator estimate remains an unverified bridge',
      'For each prescribed finite symmetric generating set of each infinite finitely generated nonamenable group, finiteness of ||T_pc|| on counting-measure l2, together with pc<1, would imply pc<p_2->2<=pu by the draft continuation and uniqueness lemmas. This packet has not established that finite critical norm in general. Hyperbolicity and pc*||A||<1 are additional sufficient hypotheses, not assumptions of the original target. A September 2026 primary source claims the general critical estimate; independent mathematical verification and a compiled trusted-axiom receipt remain absent here.',
      assumptions=['Infinite finitely generated nonamenable group','Prescribed finite symmetric generating set','Independent Bernoulli bond law'])
relations = [
    {'from_key':key,'to_key':'def-two-point','kind':'depends_on','rationale':'The draft statement uses the explicitly defined counting-measure two-point operator or percolation thresholds.'}
    for key in ('norm-continuation','uniqueness-obstruction','spectral-criterion')]
relations += [
    {'from_key':'spectral-criterion','to_key':'uniqueness-obstruction','kind':'depends_on','rationale':'The positive Neumann-series bound rules out uniqueness through the bounded-kernel obstruction.'},
    {'from_key':'critical-gap','to_key':'norm-continuation','kind':'depends_on','rationale':'A finite norm at pc would yield a strictly larger bounded parameter.'},
    {'from_key':'critical-gap','to_key':'uniqueness-obstruction','kind':'depends_on','rationale':'The operator threshold cannot exceed the uniqueness threshold.'},
    {'from_key':'normalization-refutation','to_existing_logical':prior_logical,'kind':'refutes','rationale':'Refutes only the prior normalized-rho obstruction and its adjacency normalization: the old route omits degree, while the corrected condition is pc*d*rho<1. No edge claims to refute the parent conjecture.'},
    {'from_key':'spectral-criterion','to_existing_logical':problem_logical,'kind':'semantic_association','rationale':'A sufficient criterion for the historical target, requiring an extra quantitative assumption; not a proof of the full target.'},
    {'from_key':'critical-gap','to_existing_logical':problem_logical,'kind':'semantic_association','rationale':'Isolates the additional unverified estimate needed by this proof route.'},
]
bundle = {'spec':'mathbrain-draft-v1','author_agent':'w561','bundle_slug':'c0047-operator-continuation-normalization-review-draft','entries':entries,'relations':relations}
keys={e['key'] for e in entries}
assert len(keys)==len(entries)<200
assert all(e['kind'] in ('concept','definition') and e['proof_text'] is None for e in entries)
assert all(e['source']['license'].startswith('owner-own-work') for e in entries)
assert all(r['from_key'] in keys and (r.get('to_key') in keys or r.get('to_existing_logical') in (prior_logical,problem_logical)) for r in relations)
graph={k:[] for k in keys}
for r in relations:
    if r['kind']=='depends_on' and 'to_key' in r: graph[r['from_key']].append(r['to_key'])
def visit(k, stack, seen):
    assert k not in stack, 'depends_on cycle'
    if k in seen:return
    for child in graph[k]: visit(child,stack|{k},seen)
    seen.add(k)
seen=set()
for k in keys: visit(k,set(),seen)
draft_dir=ROOT/'drafts'; draft_dir.mkdir(exist_ok=True)
blob=json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
(draft_dir/'bundle_001.json').write_text(blob,encoding='utf-8')
inbox=Path('~/math-brain-inbox/w561'); inbox.mkdir(exist_ok=True)
same=next((p for p in inbox.glob('bundle_*.json') if p.read_text(encoding='utf-8')==blob),None)
if same is None:
    number=1
    while (inbox/f'bundle_{number:03d}.json').exists() or (inbox/f'bundle_{number:03d}.part').exists():number+=1
    same=inbox/f'bundle_{number:03d}.json'
    part=inbox/f'bundle_{number:03d}.part'; part.write_text(blob,encoding='utf-8'); part.rename(same)
older=[str(p) for p in inbox.glob('bundle_*.json') if p!=same and json.loads(p.read_text(encoding='utf-8')).get('bundle_slug')==bundle['bundle_slug']]
(ROOT/'BUNDLE_STATES.json').write_text(json.dumps({'bundle':str(same),'superseded_review_drafts':older,'exclusive_claim':'clm-6dd287802b',
    'submitted':True,'reviewed':False,'ingested':False,'retrievable':False,
    'schema_validation':'passed locally; source-family/live integrator validation pending',
    'state_basis':'Submitted observed by file write; reviewed/ingested/retrievable false means no confirming receipt has been observed, not a claim about asynchronous external state.',
    'reason_no_ingest':'Only the validating coordinator integrates; all mathematical entries are review-only concept drafts.'},indent=2),encoding='utf-8')

hook={'id':'spectral-normalization-w561-01','area':'math','event':'PostToolUse',
      'cue':r'(?is)(?=.*(?:p_c|pc))(?=.*1\s*/\s*(?:rho|ρ))(?=.*(?:random.walk|normalized))',
      'fire_when':'A recalled C0047 attempt uses pc<1/rho with rho defined as normalized simple-random-walk spectral radius.',
      'silent_when':'A source explicitly uses pc*d*rho<1 or an adjacency operator norm with all hypotheses supplied.',
      'text':'If rho is the normalized random-walk spectral radius on a d-regular graph, the adjacency bound uses d*rho. Check normalization: pc<1/rho is automatic when rho<1 and cannot be the missing estimate.',
      'evidence':str(ROOT/'SOURCE_CORRECTIONS.jsonl')+' row S1.w561.C0047.normalization; canonical source node '+prior['id']+'; scar perceptron_proof_open_gaps_fleet_2026_07_12',
      'proposer':'w561'}
assert len(hook['text'])<=300
assert re.search(hook['cue'],prior['body'])
assert not re.search(hook['cue'],'Normalized random-walk rho; the source criterion is pc*d*rho<1.')
(ROOT/'HOOK_PROPOSAL.jsonl').write_text(json.dumps(hook,ensure_ascii=False)+'\n',encoding='utf-8')
hook_path=Path('~/primary_directive/hooks1000/proposals/math-w561.jsonl')
hook_path.parent.mkdir(exist_ok=True)
existing=hook_path.read_text(encoding='utf-8') if hook_path.exists() else ''
if hook['id'] not in existing:
    with hook_path.open('a',encoding='utf-8') as f:f.write(json.dumps(hook,ensure_ascii=False)+'\n')

patches=ROOT/'patches';patches.mkdir(exist_ok=True)
code=(ROOT/'spectral_bridge_guard.py').read_text(encoding='utf-8')
diff=''.join(difflib.unified_diff([],code.splitlines(keepends=True),fromfile='a/12_cognitive_architecture/brain_improvement/c0047_spectral_guard.py',tofile='b/12_cognitive_architecture/brain_improvement/c0047_spectral_guard.py'))
(patches/'01_c0047_spectral_guard.diff').write_text(diff,encoding='utf-8')

measurement_text = (f"Exact finite-volume microchecks passed: {measure['exact_Russo_BK_entry_checks']} entry inequalities; unsupported spectral transfers 3 to 0 on four self-authored fixtures, preserving one valid sufficient case. These are regression checks, not proof of the parent conjecture." if measure['state']=='passed' else 'The guard and exact microchecks were not run: two fresh CPU samples, 88.1% and 86.0%, exceeded the unchanged 85% gate. The code remains an unmeasured proposal. Analytic proofs and source correction do not depend on these experiments.')
peer_review_text='w562 reported a scoped KEEP of L01–L05 in AUDIT_W561.md, after saving an independent obstruction before reading this proof. Their message reports 123 exact finite pivotal inequalities. These are their independent checks, not a run by w561. The named referee w563 and response-side different-model evidence remain pending; no claim is promoted.'
report=f'''The canonical C0047 attempt card drops degree from a normalized spectral-radius criterion. The original source requires rho*k*p<1. The omitted degree turns pc<1/rho into an automatic inequality for nonamenable Cayley graphs, so the old proposed obstruction cannot be the missing case.

ATTEMPT.md supplies five author-checked results: the regular-tree reference, quantitative bounded-operator continuation, the uniqueness obstruction, exact counterexamples to insufficient spectral inferences, and the correctly normalized sufficient criterion. The single general gap is finite critical two-point norm on every prescribed nonamenable Cayley graph. The recent primary manuscript claims that estimate in full; its proof and compiled trusted axioms remain unchecked here. Current openness is UNKNOWN and there is no parent-solution or novelty claim.

The required general recall timed out at 60 seconds with zero completed results. Command: python -X utf8 ~/.claude/dreaming/brain.py recall "C0047 nonamenable Cayley percolation bridge mistakes", bounded by subprocess timeout=60. The targeted read-only SQLite command saved in BRAIN_RETRIEVAL.json returned the exact canonical C0047 problem and attempt cards in {brain['seconds']:.6f} seconds (plus two unrelated title matches). This is a bounded fallback measurement, not a like-for-like throughput or general recall-improvement claim.

{measurement_text}

{peer_review_text}

Apply proposal: reviewer may run git -C ~/<private-repo> apply ~/brain_workers/w561/patches/01_c0047_spectral_guard.diff after review. It adds a standalone numeric/hypothesis guard and does not connect itself to global recall. Tests: python -X utf8 ~/brain_workers/w561/measure_bridge.py, under its fresh compute gate. A bound supplied to the helper must have independent mathematical provenance; a failed sufficient criterion must not be described as a counterexample to the conjecture.

The active review-only bundle is {same}; older review drafts {older} are superseded and preserved. Integrate only the active revision after review. Submitted is observed; reviewed/ingested/retrievable have no confirming receipt. The local schema and dependency check passed. Only the validating coordinator should integrate after scoped review. A narrow normalization hook is proposed at {hook_path}; its canonical-card fire and corrected-criterion silence controls passed, with no live hook activation.

NEXT: w563 audit L02's pivotal-edge bound and infinite-volume passage, L04/L05 normalization, and the unproved general critical-norm estimate; route any new result of the referee to w566, then send kept rows and verified model evidence to codex-01a12190 for integration.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
review=ROOT/'review';review.mkdir(exist_ok=True)
packet=f'''# C0047 review packet — w561

Requested referee: w563. Independent adversary: w562; statement-first message msg-a9da9090c9. A reviewer must supply a real verdict and response-side served-model evidence before this packet can be described as independently checked. Any new result authored by w563 needs w566 as independent referee.

Scope: L01–L05 and SOURCE_CORRECTIONS.jsonl only. The packet does not claim the parent problem solved. No formal proof receipt is claimed. Current openness UNKNOWN; primary September 2026 full-result claim found. MODEL_EVIDENCE.json records that the requested gpt-6.1-sol/max/Fast settings do not establish served identity.

Check L02's Russo/BK pivotal inequality, absence of a spurious 1/(1-p) factor, uniform finite-volume norm inequality, and bilinear-form passage to infinite volume. Check L03's positive theta and FKG argument. Check L04's explicit geometric-series divergence and adjacency/random-walk normalization. Check that L05 is sufficient only and fails on T4. Do not infer general critical operator boundedness from any of these lemmas or from the existence of a source implementation file.

{measurement_text}

{peer_review_text}

Source receipts: sources/FETCH_RECEIPTS.json and sources/ADDITIONAL_FETCH_RECEIPTS.json. Workflow states: BUNDLE_STATES.json. Patch and prospective microchecks: patches/01_c0047_spectral_guard.diff and measure_bridge.py.

{attempt}
'''
(review/'REVIEW_PACKET.md').write_text(packet,encoding='utf-8')
artifacts=['ATTEMPT.md','CLAIMS.jsonl','SOURCE_STATUS.json','SOURCE_CORRECTIONS.jsonl','MODEL_EVIDENCE.json','BRAIN_RETRIEVAL.json','MEASUREMENTS.json','REPORT.md','review/REVIEW_PACKET.md','drafts/bundle_001.json','patches/01_c0047_spectral_guard.diff','measure_bridge.py','spectral_bridge_guard.py','BUNDLE_STATES.json']
(review/'ARTIFACT_HASHES.json').write_text(json.dumps({'purpose':'Review transport hashes only, not an integrator source manifest or proof certificate',
    'artifacts':[{'path':str(ROOT/name),'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()} for name in artifacts]},indent=2),encoding='utf-8')
print(json.dumps({'review_packet':str(review/'REVIEW_PACKET.md'),'bundle':str(same),'entries':len(entries),'relations':len(relations),
    'schema_and_dependency_checks':'passed','hook_fire_and_silent_controls':'passed','microcheck_state':measure['state'],'parent_solution_claim':False},indent=2))
