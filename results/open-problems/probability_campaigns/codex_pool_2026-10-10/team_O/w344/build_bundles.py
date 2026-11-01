"""Create reviewable draft bundles and unified diffs, only inside w344."""
import difflib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
PROOFS = (HERE/'PROOFS.md').read_text(encoding='utf-8')
REFS = json.loads((HERE/'store_refs.json').read_text(encoding='utf-8'))
SECTIONS = {}
for part in PROOFS.split('\n## ')[1:]:
    name, _, body = part.partition('\n')
    SECTIONS[name.split(':')[0].strip()] = body.strip()
ENTRIES = []
def add(pid, key, kind, namespace, title, statement, assumptions, label, measure, edge_kind='cites'):
    ENTRIES.append({'problem_id':pid, 'key':key, 'kind':kind, 'namespace':namespace, 'title':title, 'statement':statement, 'assumptions':assumptions, 'label':label, 'measure':measure, 'edge_kind':edge_kind})

add('P0341','fixed-trim-divergent-occupation-counterexample','lemma','probability.harmonic_descent','Fixed-width trimming fails for sparse harmonic-descent occupation tests',
    'Let a(n,j) be the probability that the strictly descending chain with transitions q(n,j)=1/((n-j)H_(n-1)), 1<=j<n, visits j, where H_k=sum_(r=1)^k 1/r. Put a(j)=6H_(j-1)/(pi^2(j-1)) and g(j)=j when j=2^r for some r>=1, zero otherwise. For every fixed integer L>=0, along n=2^K+L+1 the ratio [sum_(j=2)^(n-L-1) a(n,j)g(j)]/[sum_(j=2)^n a(j)g(j)] tends to infinity. The same holds with the denominator stopped at n-L-1. Thus deleting any fixed-width near-root band does not repair the divergent-series occupation ansatz for polynomially bounded weights.',
    ['L is fixed as K tends to infinity','The chain uses the displayed harmonic-descent transition probabilities'], 'proof','p0341_measurements.json')
add('P0341','weighted-tail-criterion-for-occupation-convergence','lemma','probability.harmonic_descent','Weighted tail criterion for convergence of occupation sums',
    'Suppose b_n(j)>=0, b_n(j)=0 for j>n, and b_n(j)->b(j) for every fixed positive integer j. Let f(j)>=0 be finite and S=sum_(j>=1)b(j)f(j)<infinity. Then sum_j b_n(j)f(j)->S if and only if lim_(M->infinity) limsup_(n->infinity) sum_(j>M)b_n(j)f(j)=0. This criterion requires an actual weighted tail estimate; pointwise convergence alone does not supply it.',
    ['Nonnegative arrays and weights','Finite limiting weighted sum','Finite support of each row'], 'proof','PROOFS.md')
add('P0341','archival-sparse-ansatz-refutation-scope','concept','probability.harmonic_descent','Scope of the archived sparse-test refutation of Ansatz 20',
    'The campaign archived on 7-8 September 2026 refutes both clauses of Aldous-Janson Ansatz 20 using powers-of-two weights and a(n,n)=1. This is a partial answer to P0341: it refutes the unrestricted auxiliary ansatz while leaving general quantitative occupation error bounds and regular-weight repairs unresolved. A ranking label candidate_pa does not mean that no substantive prior result exists. This row records archival scope and claims no new priority.',
    [], 'source-backed scope audit','packet_sources.json')

add('C0039','s3-noncommuting-dpp-linear-distance-experiment','concept','probability.determinantal','Twelve finite S3 tests of the noncommuting determinantal distance bound',
    'Numerical evidence only: for twelve seeded real symmetric S3-equivariant kernel pairs with spectra in [0.1,0.9], the optimal expected normalized Hamming coupling distance divided by trace|Q-Qprime|/6 had maximum 0.6934876897518668, with no violation found. The 4096-variable transport LP was checked against DPP normalization, one-site marginals, equivariance, primal residuals and dual objectives; a .3I/.7I commuting control gave ratio 1. Finite-group averaging makes the unrestricted LP optimum an invariant coupling optimum. These finite observations do not prove the general linear bound.',
    ['Seed 344','Finite group S3','Strictly interior real symmetric positive contractions'], 'numerical evidence','c0039_summary.json','analogous_to')
add('C0039','finite-rank-one-dpp-linear-hamming-bound','lemma','probability.determinantal','Linear trace-norm coupling bound for rank-one determinantal kernels',
    'For unit vectors v,w in C^n, let P=vv* and Q=ww*. Their determinantal laws are single-site laws with probabilities |v_i|^2 and |w_i|^2. The optimal coupling cost for normalized Hamming distance on subsets of {1,...,n} equals (1/n)sum_i ||v_i|^2-|w_i|^2| and is at most trace|P-Q|/n. If both laws are invariant under a finite permutation group, averaging yields an invariant coupling of the same cost. This is a finite rank-one result, with no general equivariant approximation theorem asserted.',
    ['Unit vectors','Finite dimension','Normalized Hamming cost'], 'proof','PROOFS.md','analogous_to')

add('P0023','symmetric-triangle-mirror-start-efficient-coupling','lemma','probability.reflected_brownian','Efficient reflected Brownian coupling for mirror starting pairs in a symmetric triangle',
    'Let D be a bounded triangle invariant under reflection R across an axis, and let lambda_1 be the first positive Neumann eigenvalue of -Delta/2 on D. For starting points x and Rx with x off the axis, there is a coalescent coupling of reflected Brownian motions with generator Delta/2 whose meeting time T satisfies P(T>t)<=C_(x,gamma) exp(-gamma t) for every 0<gamma<lambda_1. The coupling reflects one path across the axis until it hits that axis, then uses the same path. The killed half-domain principal eigenvalue is at least lambda_1 by odd extension and the Neumann Rayleigh principle. In particular, the result covers mirror starting pairs in reflection-symmetric acute triangles, not arbitrary pairs or scalene triangles.',
    ['A global reflection symmetry of the triangle','Starting points are mirror images','Generator Delta/2'], 'proof','special_case_measurements.jsonl','specializes')

add('P0177','finite-variance-free-brownian-unique-global-mode','lemma','probability.free_brownian','A unique large-time global free Brownian mode under finite variance',
    'Let X have a probability law on R with mean m and finite variance sigma^2, and let mu_t be its free convolution with a semicircle law of variance t. For every t>0 with t>=1024(7+4sqrt(2))sigma^2, the continuous density of mu_t has a unique global maximizer M(t), and M(t)->m as t tends to infinity. If M3=E|X-m|^3 is finite, put B=(sqrt(2)+2)sigma, A=B^2+sigma^2 and K=A(B+sigma)+4(B^3+M3); then |M(t)-m|<=36K/t at those times. For sigma=0 the mode is exactly m. These are sufficient large-time bounds for a global density maximizer, without a compact-support assumption or a claimed optimal transition threshold.',
    ['Finite variance','Semicircle variance is t','Mode means the global maximizer of the continuous density','Finite third absolute central moment only for the stated explicit rate'], 'proof','unbounded_mode_measurements.json')
add('P0177','finite-seventh-moment-free-brownian-global-mode-expansion','lemma','probability.free_brownian','Second-order global free Brownian mode expansion under a finite seventh moment',
    'Let X have a probability law on R with E|X|^7<infinity, mean m, and central moments mu_k=E[(X-m)^k]. Normalize free Brownian motion as convolution with a semicircle law of variance t. Its unique sufficiently-large-time global density maximizer obeys m-3mu_3/t+(5mu_5-22mu_2mu_3)/t^2+O_mu(t^-3). With epsilon=1/t, the equations E[1/(r+epsilon(u-X)^2)]=1 and E[(u-X)/(r+epsilon(u-X)^2)^2]=0 have a C^3 branch at the limiting point (epsilon,u,r)=(0,m,1); finite seventh moment justifies one-sided derivatives and a C^3 extension in epsilon, and the global-mode lemma identifies the branch. An exponential quadratic moment implies this hypothesis. The remainder is law dependent and no originality certificate is asserted.',
    ['Finite seventh absolute moment','Semicircle variance is t','Global density maximizer','Law-dependent asymptotic remainder'], 'proof','unbounded_mode_measurements.json')

add('C0004','dgff-maximum-joint-density-source-scope','concept','probability.gaussian_fields','DGFF Problem 16.4 concerns joint maximum position and height density',
    'Source correction: Biskup arXiv:1712.09972v4, Theorem 12.19, equation (12.86), and Problem 16.4 concern the joint density rho^D(x,t) in maximizer position x and centered maximum height t. At fixed t its measure in position is A -> exp(-alpha t) E[Z^D(A)exp(-alpha^-1 exp(-alpha t)Z^D(D))]. Integrating over t gives the related marginal E[Z^D(A)/Z^D(D)] when the total mass is almost surely finite and positive. A marginal-only intake statement narrows the primary target; neither explicit joint nor marginal density is resolved by this correction.',
    ['Positive finite total extremal mass for the marginal integration identity'], 'source-backed scope correction','source_followup.json')
add('C0004','zero-covariance-normalized-random-measure-criterion','lemma','probability.random_measures','Zero covariance rather than independence characterizes normalized-average equality',
    'Let Z be a random finite measure on D with total mass T>0 almost surely and 0<E[T]<infinity. Put U_A=Z(A)/T. Then E[Z(A)]/E[T]-E[U_A]=Cov(T,U_A)/E[T] for each measurable A. Consequently mean normalized measure equals normalized mean measure exactly when Cov(T,U_A)=0 for every A. Independence of total mass and normalized measure is sufficient but unnecessary: three equally likely outcomes T=(1,2,3), U_first=(1,0,1) on two sites give both averages (2/3,1/3), yet T and the normalized measure are dependent. No integrability or independence claim for DGFF extremal mass is inferred from this finite example.',
    ['Positive total mass','Finite positive mean total mass','0<=U_A<=1'], 'proof; Lean unavailable','special_case_measurements.jsonl','analogous_to')

add('C0063','regular-tree-percolation-linear-critical-amplitude','lemma','probability.percolation','Exact near-critical percolation amplitude on a regular tree',
    'For independent bond percolation on the infinite d-regular tree with d>=3, p_c=1/(d-1), theta(p)=0 for p<=p_c, and theta(p)=[2d(d-1)/(d-2)](p-p_c)+O((p-p_c)^2) as p decreases to p_c from above. The positive descendant-survival solution u obeys 1-u=(1-pu)^(d-1); division by u and the implicit-function theorem give the expansion, and theta=1-(1-pu)^d. This is an exact tree analogue, not a high-dimensional lattice solution.',
    ['Independent bond percolation','Infinite d-regular tree','d>=3'], 'proof','special_case_measurements.jsonl','analogous_to')
add('C0063','monotone-bounded-ratio-exponent-without-amplitude-limit','lemma','probability.critical_scaling','Monotonicity and exponent one do not force a limiting amplitude',
    'On 0<epsilon<1/4, F(epsilon)=epsilon(2+sin(log epsilon)) is strictly increasing, lies between epsilon and 3epsilon, and satisfies log F(epsilon)/log epsilon ->1 as epsilon tends to zero. Nevertheless F(epsilon)/epsilon has no limit. Thus monotonicity plus bounded-ratio beta=1 alone cannot establish asymptotic equivalence to c epsilon. This analytic counterexample is a refuted inference, not a percolation counterexample.',
    ['epsilon tends to zero through positive values'], 'proof','PROOFS.md','analogous_to')
add('C0063','archival-critical-exponent-subtraction-route-audit','concept','probability.critical_scaling','The archived beta equals gamma minus Delta route does not establish beta one',
    'The C0063-A001 intake attempt displays beta=gamma-Delta with gamma=1 and Delta=2 and claims that this gives beta=1. The displayed arithmetic instead gives -1. This records a route failure in that attempt and does not assert a replacement scaling theorem or equivalence of unresolved amplitude statements. Singular-limit differentiation and a right derivative at criticality still require proof for the requested lattice model.',
    [], 'source-backed route audit','packet_sources.json')

add('C0087','kruskal-sublevel-intrinsic-diameter-lower-transfer','lemma','probability.minimum_spanning_trees','Sublevel component intrinsic diameter is a lower bound for MST diameter',
    'Let G be a finite connected graph with distinct edge weights, T its minimum spanning tree, and G_p its subgraph of edges of weight at most p. For each component C of G_p, the restriction T to C is a spanning tree and the T path between vertices of C stays in C. Therefore max_C diam_intrinsic(C)<=diam(T). A probabilistic lower bound on sublevel intrinsic component diameter transfers directly to the MST; this gives no MST upper bound or high-dimensional cluster estimate by itself.',
    ['Finite connected graph','Distinct edge weights','Graph distance counts edges'], 'proof','special_case_measurements.jsonl')
add('C0087','complete-graph-path-mst-reverses-no-diameter-upper-bound','lemma','probability.minimum_spanning_trees','Small sublevel graph diameter need not bound MST diameter',
    'For each n>=3 there is a distinct-weight assignment on K_n such that the MST is a Hamilton path of diameter n-1, while a sublevel including all edges has intrinsic diameter 1. Assign the n-1 path edges the smallest weights and every other edge larger weights. Hence a cluster intrinsic-diameter bound at one threshold does not imply the reverse MST-diameter inequality. This refutes that generic upper-bound route, not torus or hypercube scaling.',
    ['Complete graph K_n','Distinct weights with path edges first'], 'proof','special_case_measurements.jsonl')

add('C0139','isoperimetric-dimension-greater-than-one-percolation-goal','concept','probability.percolation','C0139: nontrivial percolation threshold under isoperimetric dimension greater than one',
    'Historical open-problem target, current status unverified: for an infinite connected bounded-degree graph G satisfying |boundary_E S|>=c|S|^((d-1)/d) for every finite nonempty S, for some c>0 and d>1, must independent bond percolation have p_c(G)<1? The local intake attributes this to the Benjamini-Schramm conjecture in Pete lecture notes, Conjecture 12.7. Positive-Cheeger expansion is a stronger sufficient hypothesis; it does not cover the entire finite-dimensional isoperimetric condition. This goal card fills an exact C0139 anchor absent from the read-only population snapshot and supplies no claimed resolution.',
    ['Infinite connected bounded-degree graph','Uniform isoperimetric constant and dimension d>1'], 'archival problem context','packet_sources.json')
add('C0139','positive-edge-cheeger-explicit-bond-percolation-threshold-bound','lemma','probability.percolation','Positive edge-Cheeger constant gives an explicit nontrivial bond threshold',
    'Let G be an infinite connected graph of maximum degree D<infinity and edge-Cheeger constant h=inf_(finite nonempty S)|boundary_E S|/|S|>0. For independent bond percolation, 1/(D-1)<=p_c<=1/(1+h)<1. A simple-path first moment proves the lower bound. During cluster exploration after s discoveries and f failures, at least h(s+1)-f boundary edges remain untested. For p>1/(1+h), the comparison walk h+hs-f has positive drift and positive probability to remain positive forever, forcing an infinite cluster. This proves a positive-Cheeger special case; the drift argument does not decide critical equality or the full finite-dimensional isoperimetric conjecture.',
    ['Independent bond percolation','Infinite connected graph','Finite maximum degree','Uniform positive edge-Cheeger constant'], 'proof','special_case_measurements.jsonl','specializes')
add('C0139','square-lattice-finite-isoperimetry-with-zero-cheeger','lemma','probability.percolation','Finite isoperimetric dimension does not imply a positive Cheeger constant',
    'Every finite nonempty S in the square lattice Z^2 has |boundary_E S|>=4sqrt(|S|), while the edge-Cheeger constant of Z^2 is zero. Indeed, if S occupies a columns and b rows then its edge boundary is at least 2a+2b>=4sqrt(ab)>=4sqrt(|S|); square boxes of side r have boundary/volume=4/r. Thus an IP_2 inequality cannot be substituted for the uniform positive-Cheeger hypothesis in the explicit threshold proof. This does not refute the conjecture that finite isoperimetric dimension greater than one ensures p_c<1.',
    ['Unweighted square lattice','Finite nonempty vertex sets'], 'proof','PROOFS.md')

add('P0018','single-edge-partition-graph-matrix-sharp-norm','lemma','probability.graph_matrices','Sharp expected norm for the valid single-edge graph-matrix shape',
    'Under the partition convention of Randomstrasse101 Definition 14.2, the shape with one edge uv, U={u} and V={v}, gives a symmetric n by n Rademacher matrix A with zero diagonal. Its expected operator norm is Theta(sqrt(n)), so this shape has exponents f=1/2 and g=0. Deterministically ||A||>=sqrt(n-1) by its Frobenius norm. For each unit real x, P(|x^T A x|>=r)<=2exp(-r^2/4); a 1/4 sphere net of size at most 9^n and integration give the O(sqrt(n)) expectation bound. This does not resolve the existence conjecture for every fixed shape.',
    ['Independent Rademacher variables for unordered distinct pairs','Single-edge shape','Injective labels','Disjoint left/right partition'], 'proof','valid_shape_measurements.json','specializes')
add('P0018','graph-matrix-partition-convention-excludes-diagonal-internal-vertex-example','concept','probability.graph_matrices','Exclude an overlapping diagonal example from the cited graph-matrix convention',
    'Definition 14.2 in the cached Randomstrasse101 paper partitions all shape vertices into left and right sets. The diagonal signed-degree construction using the same vertex on both sides and an unindexed leaf requires a broader graph-matrix convention. Its finite norm experiment therefore supplies no special-case answer under this literal definition. The valid one-edge example uses distinct left and right vertices. Exact indexing conventions must be fixed before assigning shape exponents.',
    [], 'source-backed scope correction','source_followup.json')

add('P0047','tail-trivial-forest-infinite-component-count-dichotomy','lemma','probability.uniform_spanning_forests','The finite-versus-infinite component dichotomy is a tail event',
    'For any random spanning forest on a countable graph with trivial edge-tail sigma-field, the event that it has infinitely many components has probability zero or one. Finitely many edge changes alter a finite component count by at most finitely much and cannot change finiteness. For every finite edge set K, the infinite-count event can therefore be computed after making all edges in K absent, so it is measurable outside K. In particular FUSF on an infinite connected locally finite network has either infinitely many components almost surely or finitely many almost surely. In the finite case the argument does not make the component count constant.',
    ['Countable underlying graph','Tail-trivial forest law','For the FUSF corollary use Lyons-Peres Theorem 10.18'], 'proof','source_followup.json','specializes')
add('P0047','free-uniform-spanning-forest-on-tree-is-connected','lemma','probability.uniform_spanning_forests','FUSF on a tree is the whole connected tree',
    'On an infinite connected locally finite network whose underlying graph is a tree and whose edge conductances are positive, the free uniform spanning forest contains every edge almost surely and has exactly one component. Every finite connected induced exhaustion is itself a tree with a unique spanning tree; the free weak limit therefore fixes every edge as present. This is a boundary case of component-count determinism, not an argument for arbitrary networks.',
    ['Tree underlying graph','Positive conductances','Free connected exhaustion'], 'proof','PROOFS.md','specializes')

def quote(text):
    return ' '.join(text.split()[:18])
def target_quote(text):
    if text.startswith('OPEN PROBLEM') and '). ' in text:
        text=text.split('). ',1)[1]
    return quote(text)
bundle_dir=HERE/'drafts'
patch_dir=HERE/'patches'
bundle_dir.mkdir(exist_ok=True)
patch_dir.mkdir(exist_ok=True)
patch=[]
manifest=[]
order=['P0341','C0039','P0023','P0177','C0004','C0063','C0087','C0139','P0018','P0047']
row_counter=3
with (HERE/'result_nodes.jsonl').open('w',encoding='utf-8') as rows:
    for number,pid in enumerate(order,1):
        candidates=[entry for entry in ENTRIES if entry['problem_id']==pid]
        assert len(REFS.get(pid,[]))==1, f'Missing or ambiguous exact store anchor: {pid}'
        target=REFS[pid][0]
        logical=target['metadata']['logical_id']
        entries=[]
        relations=[]
        for item in candidates:
            key=item['key']
            entry={'key':key,'namespace':item['namespace'],'logical_name':key,'kind':item['kind'],'title':item['title'],'statement':item['statement'],'proof_text':SECTIONS[pid] if item['kind']=='lemma' else None,'assumptions':item['assumptions'],'domain':'probability theory','source':{'source_id':f'owner-w344-open-problems-20261010:{key}','url':(HERE/'PROOFS.md').as_uri(),'revision':f'2026-10-10 worker result; {item["label"]}; independent audit pending w346; novelty unverified','license':'owner-own-work (campaign proof and attributed mathematical source audit)','excerpt':quote(item['statement'])}}
            entries.append(entry)
            relations.append({'from_key':key,'to_existing_logical':logical,'kind':item['edge_kind'] if pid!='C0139' else 'cites','rationale':f'New end: "{quote(item["statement"])}"; existing end: "{target_quote(target["body"])}". This result addresses or audits {pid}; the cited card identifies its mathematical context and is not used as a proof or a current openness certificate.'})
            rows.write(json.dumps({'row_id':f'S1.w344.{row_counter:03d}','problem_id':pid,'node_key':key,'label':item['label'],'statement':item['statement'],'proof_file':'PROOFS.md','measurement':item['measure'],'auditor':'w346','audit_status':'PENDING','full_problem_solved':False,'bundle':f'drafts/bundle_{number:03d}.json'},ensure_ascii=False)+'\n')
            rows.flush()
            row_counter+=1
        if pid=='P0177':
            parent,child=entries
            relations.append({'from_key':child['key'],'to_key':parent['key'],'kind':'depends_on','rationale':f'New end: "{quote(child["statement"])}"; goal end: "{quote(parent["statement"])}". The finite-variance global-mode result identifies the stationary implicit-function branch with the unique global density maximizer.'})
        if pid=='C0139':
            goal=entries[0]
            for entry in entries[1:]:
                relations.append({'from_key':entry['key'],'to_key':goal['key'],'kind':'cites','rationale':f'New end: "{quote(entry["statement"])}"; goal end: "{quote(goal["statement"])}". The positive-Cheeger result and the zero-Cheeger IP_2 example identify the proved special case and its remaining hypothesis gap.'})
        bundle={'spec':'mathbrain-draft-v1','author_agent':'w344','bundle_slug':f'w344-open-problem-{pid.lower()}-checked-partials-20261010','entries':entries,'relations':relations}
        filename=f'bundle_{number:03d}.json'
        serialized=json.dumps(bundle,indent=2,ensure_ascii=False)+'\n'
        (bundle_dir/filename).write_text(serialized,encoding='utf-8')
        live=f'math-brain-inbox/w344/{filename}'
        patch.extend(difflib.unified_diff([],serialized.splitlines(keepends=True),fromfile='a/'+live,tofile='b/'+live))
        manifest.append({'problem_id':pid,'bundle':str(bundle_dir/filename),'live_path':'~/'+live,'nodes':len(entries),'relations':len(relations),'existing_anchor_id':target['id'],'existing_logical':logical,'review_status':'PENDING_W346','measurement_files':sorted(set(item['measure'] for item in candidates))})
(patch_dir/'01_open_problem_nodes.diff').write_text(''.join(patch),encoding='utf-8')
(HERE/'BUNDLE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
hooks=[{'id':'occupation-w344-01','area':'math','event':'stage-start','cue':r'(?is)(?:Ansatz\s*20|P0341|harmonic[- ]descent).{0,180}(?:trim|remove.{0,16}root|weighted|polynomial)','fire_when':'P0341: repair the polynomial weighted ansatz by removing the root plus 64 states below it.','silent_when':'Harmonic-descent chain: compute the leaf absorption height.','text':'Before using the polynomial-test ansatz, check weights at moving states near the starting value. Removing a fixed-width boundary band can still fail. Prove weighted-tail control for the intended class.','evidence':'memory:aldous_janson_ansatz_20_is_false_in_both_parts_2026_09_08; ~/brain_workers/w344/p0341_measurements.json, K=18 L=64 lower-bound ratio 3.8824542231499803','proposer':'w344'},
 {'id':'normalization-w344-02','area':'math','event':'stage-start','cue':r'(?is)(?:normalized|normalisation|normalization|ratio of expectations).{0,160}(?:iff|only if|requires independence|independence is necessary)','fire_when':'Normalized averages coincide iff total mass is independent of the normalized random measure.','silent_when':'For finite mean total mass, independence is sufficient to exchange normalized averaging.','text':'For finite mean mass T, use Cov(T, normalized mass on each set)=0 as the equality criterion for normalized averages. Independence supplies a sufficient condition. Check integrability first.','evidence':'~/brain_workers/w344/special_case_measurements.jsonl, C0004 exact 2/3 equality with joint probability 0 versus product 2/9; PROOFS.md C0004','proposer':'w344'}]
hook_text=''.join(json.dumps(hook,ensure_ascii=False)+'\n' for hook in hooks)
(HERE/'math-w344.jsonl').write_text(hook_text,encoding='utf-8')
hook_live='primary_directive/hooks1000/proposals/math-w344.jsonl'
(patch_dir/'02_math_hooks.diff').write_text(''.join(difflib.unified_diff([],hook_text.splitlines(keepends=True),fromfile='a/'+hook_live,tofile='b/'+hook_live)),encoding='utf-8')
print(json.dumps({'bundles':len(manifest),'nodes':len(ENTRIES),'relations':sum(m['relations'] for m in manifest),'lemma_nodes':sum(e['kind']=='lemma' for e in ENTRIES),'concept_nodes':sum(e['kind']=='concept' for e in ENTRIES),'hook_proposals':len(hooks),'output':'BUNDLE_MANIFEST.json'}))
