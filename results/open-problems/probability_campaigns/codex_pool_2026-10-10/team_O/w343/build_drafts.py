"""Build reviewer-ready data only. Never mutates the live store or inbox."""
import datetime
import difflib
import json
import pathlib
import re
import sqlite3

ROOT = pathlib.Path(__file__).resolve().parent
PIDS = ['P0340','C0036','P0013','P0150','C0003','C0060','C0085','C0131','P0016','P0046']
cards = json.loads((ROOT/'store_card_quotes_report.json').read_text(encoding='utf-8'))
store = sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True)
# The first limited query did not select the P0016 question, so select it by its exact title.
row = store.execute('SELECT id,kind,title,body,metadata_json FROM nodes WHERE title=? LIMIT 1',
                    ('Open problem: Worst square-submatrix conditioning in a Gaussian frame',)).fetchone()
assert row
cards['P0016'].append(dict(zip(['id','kind','title','body','metadata_json'],row)))
selected={}
for pid in PIDS:
    matches=[c for c in cards[pid] if ':open-problem-'+pid.lower()+'-' in json.loads(c['metadata_json']).get('logical_id','')]
    assert len(matches)==1,(pid,len(matches))
    selected[pid]=matches[0]
(ROOT/'selected_cards_report.json').write_text(json.dumps(selected,indent=2),encoding='utf-8')
entries=[]
info={}

def add(key,pid,namespace,name,kind,title,statement,proof_file,assumptions=(),label='proof'):
    proof=(ROOT/proof_file).read_text(encoding='utf-8') if kind in ('lemma','theorem') else None
    if proof:
        proof=proof.split('\n',1)[1].strip()
        if key=='p0340-tree':
            proof=proof.split('Checks to run:',1)[0].strip()
        elif key in ('p0340-height','p0340-linear'):
            proof=proof.split('## Linear-expectation argument checked against the earlier proof',1)[1]
            proof=proof.split('This is an author-checked proof candidate',1)[0].strip()
        elif key=='p0150-whisker':
            proof=proof.split('Useful sufficient input.',1)[0].strip()
        elif key=='c0131-pathwise':
            proof=proof.split('Uniform ellipticity alone is insufficient',1)[0].strip()
    source={'source_id':'owner-probability-campaign-w343:'+key,
            'url':'file:///~/brain_workers/w343/'+proof_file,
            'revision':'author-checked-2026-10-10-pending-w347',
            'license':'owner-own-work (campaign proof or status note)', 'excerpt':None}
    entry={'key':key,'namespace':namespace,'logical_name':name,'kind':kind,'title':title,
           'statement':statement,'proof_text':proof,'assumptions':list(assumptions),
           'domain':'probability theory','source':source}
    entries.append(entry)
    info[key]={'problem_id':pid,'label':label,'proof_file':proof_file,'audit_status':'PENDING',
               'claim_status':'candidate; no independent KEEP recorded'}
    return entry

add('p0340-tree','P0340','probability.randomtrees','full-binary-tree-drawn-length-height-identity','lemma',
    'Drawn length of a full binary tree: exact identity and depth bounds',
    'For a finite rooted full binary tree T with n leaves and edge height h(T), define l(leaf)=0 and '
    'l(T)=l(L)+l(R)+2+|h(L)-h(R)|. If D(T) is the sum of leaf depths, then '
    'l(T)=sum over internal vertices v of h(T_v)+h(T), and 2(n-1)<=l(T)<=D(T). '
    'This is a deterministic lemma; independent audit is pending.', 'P0340_proof.md',
    ['The tree is full binary, and the height of a leaf is zero.'])
add('p0340-height','P0340','probability.randomtrees','critical-beta-splitting-height-geometric-moment-bound','lemma',
    'An explicit expected maximum-height bound for critical beta-splitting trees',
    'Let T_n be the independent recursive binary splitting tree with q_m(i)=m/[2H_(m-1)i(m-i)], '
    'where H_k=sum_(j=1)^k 1/j. For n>=2 put p=1/(2H_(n-1)), b=ceil(log_2 n), '
    'and theta=-log(1-p/2). Its expected edge height is at most (log n+b log 2)/theta '
    '<=4H_(n-1)(2 log n+log 2). Each tagged leaf depth is bounded by a sum of b geometric(p) '
    'waiting times, whose exponential moment at theta is 2^b. No independence among leaf depths '
    'is required. Author proof; independent audit pending.', 'P0340_proof.md',
    ['Independent recursive subtrees conditional on split sizes.', 'Leaf height zero; natural logarithms except log_2.'])
add('p0340-linear','P0340','probability.randomtrees','critical-beta-splitting-linear-expected-drawn-length','theorem',
    'Candidate linear expectation asymptotic for minimal drawn length',
    'For T_n with independent recursive splits q_m(i)=m/[2H_(m-1)i(m-i)] and drawn-length '
    'recursion l(T)=l(L)+l(R)+2+|h(L)-h(R)|, with leaf height and length zero, put h_m=E h(T_m). '
    'Then E l(T_n)/n tends to c=(6/pi^2) sum_(m=2)^infinity H_(m-1)h_m/[m(m-1)], '
    'where 2<=c<infinity. The proof uses the published tagged-clade occupation limit '
    'a(n,m)->6H_(m-1)/[pi^2(m-1)] and the uniform block estimate '
    'sum_(j=b+1)^(2b) a(n,j)<=2H_(2b-1). This is an author-checked proof candidate; '
    'no independently certified open-problem solution or law of large numbers is claimed.',
    'P0340_proof.md', ['The stated pointwise occupation limit from Aldous-Janson Theorem 18.'])
m0340=json.loads((ROOT/'measurement_p0340.json').read_text(encoding='utf-8'))
b128=next(x for x in m0340['height_bound_comparison'] if x['n']==128)
add('p0340-numeric','P0340','probability.randomtrees','critical-beta-splitting-finite-drawn-length-recursion-check','concept',
    'Finite checks for drawn-length and height bounds',
    f"The local check_p0340.py run checked {m0340['trees_checked']} ordered full binary trees through ten leaves "
    'with no tree-identity or depth-bound failures. A float64 height-distribution recursion agrees with '
    'weighted tree enumeration through n=10 and gives E l(T_128)/128=4.496140445692661. '
    f"At n=128 the earlier proof's height upper bound is {b128['prior_proof_bound']:.6f} and the "
    f"tightened upper bound is {b128['tightened_bound']:.6f}, a {b128['bound_reduction_percent']:.2f}% reduction "
    'in that bound. These are finite numerical checks, not a proof of the limiting constant. '
    'Current Lean setup was refused by the compute governor; no new Lean verification is claimed.',
    'measurement_p0340.json',label='numerical evidence')
add('c0036-two','C0036','probability.determinantal','two-site-equivariant-determinantal-sharp-product-domination','lemma',
    'Sharp product domination for two-site equivariant determinantal kernels',
    'For a Hermitian positive contraction Q=[[a,z],[conj(z),a]], put p=sqrt(a^2-|z|^2) '
    'and q=1-sqrt((1-a)^2-|z|^2). Its determinantal law stochastically dominates iid '
    'Bernoulli(p) and is stochastically dominated by iid Bernoulli(q). Both parameters '
    'are optimal, including when Q or I-Q is singular. This proves only the two-site case '
    'of the general equivariant conjecture; independent audit pending.', 'C0036_proof.md',
    ['0<=a-|z|<=a+|z|<=1.'])
add('c0036-necessary','C0036','probability.determinantal','finite-determinantal-product-domination-determinant-necessity','lemma',
    'Necessary finite determinant bounds for iid domination',
    'For a determinantal probability law with positive-contraction kernel Q on N>=1 sites, '
    'iid lower stochastic domination at density b implies b<=det(Q)^(1/N); iid upper '
    'stochastic domination at density c implies c>=1-det(I-Q)^(1/N). The all-present '
    'and all-absent events prove these inequalities. For a finite transitive equivariant '
    'kernel these roots are the normalized Fuglede-Kadison determinants. Necessity does '
    'not imply the conjectured general sufficiency; independent audit pending.', 'C0036_proof.md')
add('c0036-conditioning','C0036','probability.determinantal','two-site-harmonic-geometric-conditioning-gap','lemma',
    'Full-rest conditionals need not reach the sharp geometric-mean density',
    'For Q=[[1/2,1/4],[1/4,1/2]], the minimum presence probability conditioned on the other '
    'site is 3/8, while the sharp iid lower domination density is sqrt(3)/4. Thus a '
    'worst-full-rest-conditional lower-bound method does not certify the geometric-mean '
    'density. The relevant Schur complement is odds s; its presence probability is s/(1+s), '
    'not s. Independent audit pending.', 'C0036_proof.md')
add('p0013-defects','P0013','probability.randomgraphs','complement-invariant-lovasz-theta-two-defect-reduction','lemma',
    'Two nonnegative defects in expected Lovasz theta',
    'For a complement-invariant random graph G on n>=1 vertices, let '
    'X=theta(G)/sqrt(n), Y=theta(complement G)/sqrt(n), R=sqrt(XY), and '
    'Z=(log X-log Y)/2. Using theta(G)theta(complement G)>=n, '
    'E theta(G)/sqrt(n)-1=E(R-1)+E[R(cosh Z-1)], with both terms nonnegative. '
    'Therefore the expectation asymptotic at sqrt(n) is equivalent to both defect '
    'expectations tending to zero. No defect estimate for G(n,1/2) is proved here. '
    'Independent audit pending.', 'P0013_proof.md', ['The standard Lovasz theta product inequality.'])
add('p0150-whisker','P0150','probability.metric','uniform-star-whisker-gromov-weak-nontightness','lemma',
    'Uniform finite graphs can hide a diverging pendant diameter',
    'Attach floor(sqrt(m)) new path vertices to the center of an m-vertex star, give all '
    'vertices uniform probability mass, and rescale graph distance by m^(-1/4). Every fixed '
    'iid sampled distance matrix tends in probability to zero, since the path mass tends '
    'to zero and star distances are at most 2m^(-1/4). The rescaled diameter is '
    '(floor(sqrt(m))+1)m^(-1/4), which diverges. Thus Gromov-weak convergence to a point '
    'need not imply GH tightness even for uniform full-support finite graphs. This family '
    'is not a heavy-tailed critical configuration model; independent audit pending.', 'P0150_proof.md')
add('p0150-mass','P0150','probability.metric','critical-metric-convergence-lower-mass-route-scope','concept',
    'The missing lower-mass input in a weak-to-metric convergence route',
    'Finite sampled distance matrices can miss low-mass appendages. A route to compact '
    'metric convergence must separately control the mass of every fixed-radius ball '
    '(or obtain an equivalent tightness estimate). The star-plus-path construction '
    'illustrates this requirement; it does not show that the requested critical '
    'configuration-model degree assumptions are insufficient. Their minimal-assumption '
    'lower-mass estimate remains unproved in this pass.', 'P0150_proof.md',label='scope guard')
add('c0003-tail','C0003','probability.extremes','moment-threshold-does-not-fix-logarithmic-laplace-tail','lemma',
    'Equal moment thresholds permit different Laplace corrections',
    'For a in [0,1], let W_a>=0 have survival probability 1/e on [0,e) and '
    '1/[t(log t)^a] for t>=e. For s>0, E W_a^s is finite exactly when s<1. '
    'As lambda decreases to zero, 1-E exp(-lambda W_a) is asymptotic to '
    'lambda[log(1/lambda)]^(1-a)/(1-a) for a<1, and to lambda log log(1/lambda) '
    'for a=1. Thus the moment threshold alone does not imply a positive finite '
    'lambda log(1/lambda) coefficient. These scalar laws are not asserted to satisfy '
    'the DGFF Gibbs-Markov or conformal axioms; independent audit pending.', 'C0003_proof.md')
add('c0060-fiber','C0060','probability.percolation','finite-cut-vertex-fiber-hits-product-bypass','lemma',
    'Finite cut-vertex fiber hits do not separate a product graph',
    'Let c be a cut vertex of a connected graph G and let a,b lie on opposite sides. '
    'Any finite set F contained in {c} x Z can be bypassed in G x Z by moving to a height '
    'not used by F, crossing via c there, and returning along the other side. For the '
    'three-vertex path a-c-b, removing (c,z) for |z|<=H leaves a shortest a_0-to-b_0 '
    'path of length 2H+4. Hitting a corner region alone is not a proof of separation. '
    'This does not determine the vacant-set threshold of an infinite interlacement trace; '
    'independent audit pending.', 'C0060_proof.md', ['F is finite and lies only on the specified fiber.'])
add('c0085-sublevel','C0085','probability.percolation','invasion-explores-finite-root-sublevel-cluster','lemma',
    'Invasion explores a finite root sublevel cluster before exiting it',
    'On a connected countable locally finite infinite weighted graph, invasion starts at '
    'o and repeatedly adds the other endpoint of a minimum-weight boundary edge. If the '
    'ordinary weight-at-most-p root cluster C_p(o) is finite, invasion explores all of it '
    'before selecting its first edge with weight greater than p. Hence, under iid uniform '
    'weights and almost-sure finiteness of C_pc(o), P(x in IPC)>=P_pc(o connected to x). '
    'This compares with an ordinary critical cluster, not the incipient infinite cluster; '
    'it does not yield the target invasion exponent d-4. Independent audit pending.', 'C0085_proof.md')
add('c0131-pathwise','C0131','probability.randomenvironment','uniform-elliptic-adapted-walk-pathwise-site-dichotomy','lemma',
    'Uniform ellipticity gives a pathwise all-or-none recurrence alternative',
    'For an adapted nearest-neighbor walk on a connected countable graph, suppose each '
    'neighbor transition has conditional probability at least kappa>0 given the complete '
    'past. Almost surely, either every vertex is visited infinitely often or every vertex '
    'is visited only finitely often. If u has infinitely many visits, the chance of missing '
    'a fixed neighbor at k successive opportunities is at most (1-kappa)^k; propagation '
    'along finite paths proves the claim. On Z^d the second alternative leaves every finite '
    'ball eventually. This does not make the first alternative\'s annealed probability '
    'zero or one. Independent audit pending.', 'C0131_proof.md')
add('c0131-mixture','C0131','probability.randomenvironment','uniform-elliptic-global-mixture-with-nontrivial-recurrence-probability','lemma',
    'A global mixture distinguishes pathwise and annealed dichotomies',
    'A fair global coin selecting either simple random walk on Z^2 or a constant-kernel '
    'walk with directional probabilities (3/8,1/8,1/4,1/4) yields a uniformly elliptic '
    'walk with recurrent-alternative probability 1/2. The simple-random-walk branch '
    'is recurrent; the biased branch has drift 1/4 and is transient by the strong law. '
    'This global mixture is not an iid cookie environment and is not a counterexample '
    'to the iid excited-walk question. Independent audit pending.', 'C0131_proof.md',
    ['Classical recurrence of simple random walk on Z^2.'])
add('p0016-literature','P0016','probability.randommatrix','gaussian-phase-retrieval-extreme-submatrix-literature-answer','concept',
    'Cached literature answer for the Gaussian worst-subframe problem',
    'The cached LITERATURE_P2.md receipt attributes an answer to Yitzchak Shmalo, '
    'Extreme least singular values of Gaussian row submatrices and a phase retrieval '
    'stability problem, arXiv:2607.06249 (7 July 2026), Theorem 1.1 and Corollary 1.2. '
    'For standard real Gaussian (2m-1)-by-m frames it reports omega(A_m)=4^(-m+o_P(m)), '
    'equivalently m^(-1)log omega(A_m)->-log 4 in probability. This matches '
    'Randomstrasse101 Open Problem 21; the old attempted_unsolved ranking is stale '
    'according to that receipt. The primary paper and its full proof were not newly '
    'checked here; confirm the citation and normalization before admitting the status '
    'correction. This is a literature record, not an original solution.', 'P0016_literature.md',label='literature answer from cached receipt')
add('p0016-numeric','P0016','probability.randommatrix','gaussian-worst-row-subframe-small-dimension-reproduction','concept',
    'Finite reproduction of worst Gaussian row-subframe scaling',
    'With NumPy RNG seed 343, the local check minimizes the smallest singular value '
    'over every m-row subset of 64 standard real Gaussian frames for each m=1,...,6: '
    '384 frames and 40,768 minors. At m=6 the median of 4^m omega is '
    '2.5933238602603175. At m=1 the exact omega law is |N(0,1)|. These finite samples '
    'check the row-subframe convention and provide numerical evidence only; they '
    'do not establish the asymptotic or an exponential limit law.', 'measurement_p0016.json',label='numerical evidence')
add('p0046-interfaces','P0046','probability.spanningforests','infinite-component-interfaces-suffice-for-sparse-invariant-connection','lemma',
    'Infinite interfaces suffice for arbitrarily sparse independent connection',
    'Let F be a random spanning forest on a connected countable locally finite graph G. '
    'Join F-components when infinitely many G-edges run between them. If this component '
    'graph is almost surely connected, then F united with independent Bernoulli(delta) '
    'G-edges is almost surely connected for every 0<delta<1. If F is invariant, the union '
    'is invariant and P(e in union minus F)<=delta for each edge. Each infinite interface '
    'receives an edge almost surely, and countably many such assertions hold simultaneously. '
    'The interface assumption is not proved for a general FUSF; independent audit pending.', 'P0046_proof.md')
add('p0046-columns','P0046','probability.spanningforests','vertical-line-forest-sprinkling-window-connectivity','lemma',
    'A vertical-line forest admits every positive horizontal sprinkling',
    'In Z^2 let F consist of all vertical edges. Every 0<delta<1 independent edge '
    'sprinkling connects its columns almost surely. In a rectangular window of q>=1 '
    'columns and r>=1 horizontal levels, retaining its vertical forest, the exact '
    'connectivity probability is [1-(1-delta)^r]^(q-1). Adjacent column pairs have '
    'disjoint r-edge interfaces. This example is a spanning forest, not an assertion '
    'about the FUSF law; independent audit pending.', 'P0046_proof.md')

relations=[]
quote_rows=[]
def excerpt(text, words=27):
    return ' '.join(text.split()[:words])
def connect(key, target, kind, why, existing=False):
    source=next(e for e in entries if e['key']==key)
    if existing:
        c=target;logical=json.loads(c['metadata_json'])['logical_id']
        body=c['body']
        clean=re.sub(r'^OPEN PROBLEM.*?\. ','',body,count=1,flags=re.S)
        target_quote=excerpt(clean)
        assert target_quote in ' '.join(body.split())
        edge={'from_key':key,'to_existing_logical':logical,'kind':kind}
        target_id=c['id']
    else:
        other=next(e for e in entries if e['key']==target)
        target_quote=excerpt(other['statement']);target_id=target
        edge={'from_key':key,'to_key':target,'kind':kind}
    source_quote=excerpt(source['statement'])
    edge['rationale']=f'FROM "{source_quote}"; TO "{target_quote}". {why}'
    relations.append(edge)
    quote_rows.append({'from_key':key,'target':target_id,'kind':kind,
                       'from_quote':source_quote,'to_quote':target_quote,'rationale':why})
for entry in entries:
    key=entry['key'];pid=info[key]['problem_id']
    kind='specializes' if key=='c0036-two' else 'semantic_association'
    connect(key,selected[pid],kind,'Precise result or scope guard attached to the assigned question; no general solution inferred.',True)
for source,target,kind in [('p0340-linear','p0340-tree','depends_on'),
                            ('p0340-linear','p0340-height','depends_on'),
                            ('p0340-numeric','p0340-tree','cites'),
                            ('p0340-numeric','p0340-height','cites'),
                            ('c0036-two','c0036-necessary','depends_on'),
                            ('c0036-conditioning','c0036-two','specializes'),
                            ('p0150-mass','p0150-whisker','cites'),
                            ('p0016-numeric','p0016-literature','cites'),
                            ('p0046-columns','p0046-interfaces','specializes')]:
    connect(source,target,kind,'The endpoint statements explain the dependency or scope of the finite example.')
# The neighboring circulant card was returned by the original topic query, not newly searched.
circulant=next(c for c in cards['P0013'] if ':open-problem-p0014-' in json.loads(c['metadata_json']).get('logical_id',''))
connect('p0013-defects',circulant,'analogous_to','The circulant case has exact theta product, so its product defect is zero.',True)

bundle={'spec':'mathbrain-draft-v1','author_agent':'w343','bundle_slug':'team-o-ten-problem-refinements-20261010',
        'entries':entries,'relations':relations}
out=ROOT/'drafts';out.mkdir(exist_ok=True)
payload=json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
(out/'bundle_001.json').write_text(payload,encoding='utf-8')
(ROOT/'edge_quotes.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in quote_rows),encoding='utf-8')
baseline=[]
for e in entries:
    logical='math:'+e['namespace']+':'+e['logical_name']
    count=store.execute("SELECT COUNT(*) FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=?",(logical,)).fetchone()[0]
    baseline.append({'logical_id':logical,'live_matching_nodes_before':count})
cite_count=store.execute("SELECT COUNT(*) FROM nodes WHERE kind='claim' AND (body LIKE ? OR metadata_json LIKE ?)",
                         ('%2607.06249%','%2607.06249%')).fetchone()[0]
canonical_cite_count=store.execute("SELECT COUNT(*) FROM nodes WHERE kind='claim' AND "
    "json_extract(metadata_json,'$.logical_id') LIKE 'math:%' AND (body LIKE ? OR metadata_json LIKE ?)",
    ('%2607.06249%','%2607.06249%')).fetchone()[0]
store.close()
(ROOT/'baseline_report.json').write_text(json.dumps({'selected_problem_cards':len(selected),
    'raw_claim_citation_matches_before':cite_count,
    'canonical_math_citation_matches_before':canonical_cite_count,'candidate_logical_names':baseline,
    'staged_entries_after':len(entries),'staged_relations_after':len(relations),
    'live_store_modified':False},indent=2),encoding='utf-8')
audit={'auditor':'w347','manager':'claude-4a88bc43','bundle':'drafts/bundle_001.json',
       'method':'Independent check of statements, hypotheses and proof; no expected verdict supplied.',
       'result_packets':[dict(key=e['key'],problem_id=info[e['key']]['problem_id'],
                               statement=e['statement'],label=info[e['key']]['label'],
                               proof_file=info[e['key']]['proof_file'],audit_status='PENDING') for e in entries],
       'review_points':['P0340: check split-law size bias, conditional subtree law, dyadic tail, pointwise occupation source and geometric coupling.',
          'C0036: enumerate every increasing event, check complements and singular endpoints; distinguish odds from probability.',
          'P0013: use complement-invariant law and the inequality, not exact theta product for general graphs.',
          'P0150/C0003/C0060: distinguish generic route counterexamples from instances of the original stochastic hypotheses.',
          'C0085: require finite ordinary sublevel root cluster; do not silently substitute IIC.',
          'C0131: distinguish a pathwise alternative from annealed zero-one law; global mixture is not iid cookies.',
          'P0016: inspect the primary Shmalo paper and normalization; local receipt and numerics are not its proof.',
          'P0046: require connected infinite-interface graph; this has not been proved for arbitrary FUSF.',
          'No current Lean verification: lean_current_receipt.json records setup refusal.'],
       'verdict_schema':{'key':'entry key','verdict':'KEEP|FIX|DROP','why':'independent reasons',
                          'full_proof_check':'true only if the complete applicable proof and cited hypotheses were checked'},
       'new_solution_certified':False}
(ROOT/'W347_AUDIT_PACKET.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')

patches=ROOT/'patches';patches.mkdir(exist_ok=True)
def write_patch(name,live_path,text):
    # Both headers name the live path, as COMMON.md requests. The old file is empty.
    patch=''.join(difflib.unified_diff([],text.splitlines(keepends=True),
                                     fromfile='a/'+live_path,tofile='b/'+live_path))
    (patches/name).write_text(patch,encoding='utf-8')
    # Git requires /dev/null for a creation; keep a directly applyable variant.
    deploy='diff --git a/'+live_path+' b/'+live_path+'\nnew file mode 100644\n'+patch.replace('--- a/'+live_path+'\n','--- /dev/null\n',1)
    (patches/name.replace('.diff','.apply.diff')).write_text(deploy,encoding='utf-8')
write_patch('01_team_o_bundle.diff','math-brain-inbox/w343/bundle_001.json',payload)
hooks=[{'id':'math-w343-01','area':'math','event':'stage-start',
        'cue':'Starting an attack on P0016 or the worst Gaussian row-submatrix problem with an unsolved ranking',
        'fire_when':'The packet calls P0016 unsolved and the agent is about to start a new proof attempt.',
        'silent_when':'The Shmalo 2607.06249 answer is already cited or no open-problem attack is starting.',
        'text':'Before attacking a ranked open problem, compare its date with the cited local literature receipts and the owner\'s papers. P0016 had a saved July answer while its September ranking still said unsolved.',
        'evidence':'memory:p0016_was_already_solved_by_yitzchaks_own_paper_2026_09_13; P0016_literature.md',
        'proposer':'w343'},
       {'id':'math-w343-02','area':'math','event':'PostToolUse',
        'cue':'lean_check.py output says SETUP_UNVERIFIED, runtime unavailable or timed out',
        'fire_when':'The current Lean checker refuses setup under the compute governor, as in lean_current_receipt.json.',
        'silent_when':'A reviewed current receipt reports verified compilation and its target axiom inventory.',
        'text':'A refused or timed-out Lean setup is not a Lean check. Keep the current receipt separate from older compilations and label the mathematical proof by the evidence that actually ran.',
        'evidence':'~/brain_workers/w343/lean_current_receipt.json: exit 2, SETUP_UNVERIFIED',
        'proposer':'w343'}]
hook_text=''.join(json.dumps(h,ensure_ascii=False)+'\n' for h in hooks)
(ROOT/'hooks_proposals.jsonl').write_text(hook_text,encoding='utf-8')
write_patch('02_hooks_proposals.diff','primary_directive/hooks1000/proposals/math-w343.jsonl',hook_text)

existing_rows={json.loads(line)['row_id'] for line in (ROOT/'results.jsonl').read_text(encoding='utf-8').splitlines()}
with (ROOT/'results.jsonl').open('a',encoding='utf-8') as f:
    for i,e in enumerate(entries,20):
        rid=f'S1.O.w343.{i:03}'
        if rid not in existing_rows:
            f.write(json.dumps({'row_id':rid,'problem_id':info[e['key']]['problem_id'],'kind':e['kind'],
                                'label':info[e['key']]['label'],'entry_key':e['key'],'statement':e['statement'],
                                'bundle_file':'drafts/bundle_001.json','proof_file':info[e['key']]['proof_file'],
                                'audit_status':'pending-w347','new_solution_certified':False},ensure_ascii=False)+'\n')
(ROOT/'STATUS.md').write_text('STATE: WORKING\nNEXT: Validate the bundle, quoted endpoints and unified diffs; write REPORT.md and set NEEDS_REVIEW for w347.\n'
    +datetime.datetime.now().isoformat()+f' Staged {len(entries)} typed candidates and {len(relations)} relations for the ten assigned problems, '
    'with blind audit packet and two evidence-backed hook proposals. All files are inside w343; no live store writes or mesh sends.\n',encoding='utf-8')
print(json.dumps({'entries':len(entries),'relations':len(relations),'problems':len(PIDS),
                  'hook_proposals':len(hooks),'auditor':'w347','audit_keeps':0,'live_store_modified':False}))
