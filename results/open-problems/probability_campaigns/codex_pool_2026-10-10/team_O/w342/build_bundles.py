"""Prepare draft bundles and unified diffs; write only within the worker folder."""
import difflib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
ORDER=['P0289','C0035','P0001','P0133','C0002','C0059','C0083','C0128','P0015','P0044']
cards=json.loads((ROOT/'store_cards.json').read_text(encoding='utf-8'))
parents={p:next(c for c in cards if c['query']==p and ':open-problem-' in c['metadata'].get('logical_id','')) for p in ORDER}
bundles={p:{'spec':'mathbrain-draft-v1','author_agent':'w342','bundle_slug':'w342-'+p.lower()+'-partial-results','entries':[],'relations':[]} for p in ORDER}


def add(p,key,kind,title,statement,assumptions=(),namespace='probability.research.attempts'):
    proof=(ROOT/'proofs'/f'{p}.md')
    entry={'key':key,'namespace':namespace,'logical_name':key,'kind':kind,'title':title,'statement':statement,
           'proof_text':None if kind=='concept' else proof.read_text(encoding='utf-8'),
           'assumptions':list(assumptions),'domain':'probability theory and related mathematics',
           'source':{'source_id':'owner:w342:'+p+':'+key,'url':proof.as_uri(),
                     'revision':'author-proof-pending-w346-2026-10-10','license':'owner-own-work','excerpt':None}}
    bundles[p]['entries'].append(entry)
    return key


def quote(statement):
    short=statement[:260]
    if len(statement)>260:
        short=short.rsplit(' ',1)[0]
    return short.replace('\n',' ')


def relate(p,from_key,to_key,kind,reason,existing=None):
    entries={e['key']:e for e in bundles[p]['entries']}
    source=entries[from_key]['statement']
    target=existing['body'] if existing else entries[to_key]['statement']
    rationale='FROM "'+quote(source)+'"; TO "'+quote(target)+'"; '+reason
    relation={'from_key':from_key,'kind':kind,'rationale':rationale}
    if existing:
        relation['to_existing_logical']=existing['metadata']['logical_id']
    else:
        relation['to_key']=to_key
    bundles[p]['relations'].append(relation)


scopes={
 'P0289':'The cached Ross problem asks for universal decrease of stationary Cox/GI/1 mean workload with modulation speed and a necessary-and-sufficient criterion. The second-order coefficient sign criterion and prior-source scope correction have w346 KEEP on rows S1.w342.001 and .002. The bounded unit-service expansion and cyclic counterexample still await full proof review and address universal monotonicity only. The complete criterion remains unresolved here. Novelty and October 2026 literature status are unverified.',
 'C0035':'For a degree-m trigonometric symbol f:T->[0,1], the cached question asks whether its stationary determinantal process is an (m+1)-block iid factor. The phase-sensitive triple and conditional sublattice reduction below do not establish general existence. Degree one is recorded as known in the cached source. All new proofs await w346 KEEP.',
 'P0001':'The uniform-forest question asks for nonpositive covariance of every distinct edge pair on every finite simple graph. The w342 proof establishes this for graphs whose blocks are bridges or generalized theta graphs, including arbitrary positive fugacities. Arbitrary graphs and general negative association are not settled here. The proof awaits w346 KEEP.',
 'P0133':'The cached torus problem asks for the distribution of three noncontractible loop homotopy classes in a spanning-tree dual complement. A unimodular winding constraint is proved for a theta core; it does not provide limiting probabilities. The 3x3 square-grid enumeration also has bouquet cores, which are not covered by the three-loop assertion. Proofs await w346 KEEP.',
 'C0002':'The cached DGFF problem asks for convergence rates, fluctuation laws and rare deviations of intermediate level sets. A bulk one-point Gaussian tail expansion improves the first-moment calculation only; it establishes neither the joint fluctuation law nor large deviations. Its proof awaits w346 KEEP.',
 'C0059':'The cached Curien problem asks whether the dual infinite Boltzmann map is transient for type a in [2,5/2). The constructed recurrent and transient quartic-growth trees refute a volume-growth inference; neither is claimed to have the Boltzmann-map law. The original question is unresolved here. Proofs await w346 KEEP.',
 'C0083':'The cached Hamming-graph problem asks for the asymptotic critical-value expansion. Exact local cycle counts and the susceptibility Taylor series at p=0 do not establish a new critical-value coefficient. Critical control through exploration or a lace expansion is still required. Proofs await w346 KEEP.',
 'C0128':'The cached excited-walk problem asks for conditions giving directional zero-one laws. The sublinear adverse-drift budget supplies an explicit sufficient condition and includes finite adverse-cookie perturbations of uniform bias. It does not classify general stationary ergodic cookie environments. Proofs await w346 KEEP.',
 'P0015':'For N=4M-5 complex Gaussian measurements, the cached conjecture asks both p_M<1 and p_M->0. The explicit transverse-frame proof candidate establishes the first clause for every M>=2 and gives p_2=p_3=0. It supplies no uniform probability bound in M, so the asymptotic clause remains unresolved. No solution is reported before w346 KEEP and full proof audit; novelty is unverified.',
 'P0044':'The cached uniform-spanning-forest question asks for an automorphism-invariant inclusion coupling on arbitrary networks. The canonical tree-network coupling and the equal-edge-marginal reduction establish special cases only. The cached 2026 book already cites Lyons-Thom invariant couplings on sofic groups. Arbitrary networks remain unresolved here. Proofs await w346 KEEP.',
}
for p in ORDER:
    add(p,p.lower()+'-w342-result-scope','concept','Result scope and audit status for '+p,scopes[p])

add('P0289','unit-service-workload-minus-parallel-residual-monotonicity','lemma','Monotonicity of workload minus parallel residual work',
    'For any locally finite set A of nonnegative arrival ages with finite unit-service workload, let V(A)=sup_{u>=0}(#{a in A:a<=u}-u)_+ and T(A)=sum_{a in A}(1-a)_+. Then V(A)>=T(A), and V(A)-T(A) does not decrease when ages are added, provided both compared workloads are finite.',
    ['Nonnegative arrival ages','Unit service and rate-one server','Finite compared workloads'],'probability.queueing')
add('P0289','bounded-cox-unit-service-uniform-light-traffic-expansion','lemma','Uniform light-traffic expansion for bounded Cox intensity',
    'Let M>0 be finite, eps>=0, and F be stationary, measurable and bounded between 0 and M, with a=E F(0), eps M<1 and c>0. Conditional on F, take Poisson arrivals of intensity eps F(ct), unit service and a rate-one server. The stationary workload satisfies E V_c=eps a/2+eps^2 integral_0^1(1-u)E[F(0)F(-cu)]du+R_c, uniformly in c, where 0<=R_c<=eps^3 M^3/[2(1-eps M)].',
    ['M>0 finite and eps>=0','Stationary measurable bounded nonnegative intensity','Unit deterministic service','eps M<1'],'probability.queueing')
add('P0289','ross-cyclic-environment-faster-modulation-workload-rise','theorem','Cyclic environment with increased workload under faster modulation',
    'Let X_t be the stationary clockwise CTMC on Z/1024Z with jump rate 1/sin(2pi/1024), and F(t)=2+cos(2pi X_t/1024). For conditional Poisson arrivals of intensity F(ct)/10000, unit service and rate-one service, both stationary queues are stable and E V_{3pi}-E V_{2pi}>2491/161280000000000>0. Thus universal mean-workload decrease with modulation speed fails for this stationary ergodic environment.',
    ['Uniform stationary initial law for the finite irreducible CTMC','Conditional Poisson Cox law','Unit deterministic service'],'probability.queueing')
add('P0289','light-traffic-integrated-correlation-sign-criterion','lemma','Sign criterion for an integrated second-order coefficient',
    'If R:[0,infinity)->R is continuous and Psi(c)=integral_0^1(1-u)R(cu)du for c>0, then Psi is continuously differentiable and Psi\'(c)=c^{-3}integral_0^c(2v-c)R(v)dv. Psi is nonincreasing iff the integral is nonpositive for every c>0. When Psi is a workload expansion coefficient this criterion alone does not order full workloads.',
    ['Continuity of R'],'probability.queueing')
relate('P0289','bounded-cox-unit-service-uniform-light-traffic-expansion','unit-service-workload-minus-parallel-residual-monotonicity','depends_on','The nonnegative residual difference is monotone under the stated Poisson thinning coupling.')
relate('P0289','ross-cyclic-environment-faster-modulation-workload-rise','bounded-cox-unit-service-uniform-light-traffic-expansion','depends_on','The uniform remainder leaves a strictly positive rational lower bound for the workload difference.')
relate('P0289','light-traffic-integrated-correlation-sign-criterion','bounded-cox-unit-service-uniform-light-traffic-expansion','analogous_to','The integral sign test applies to the second-order term and carries no full-workload conclusion.')
sign=next(e for e in bundles['P0289']['entries'] if e['key']=='light-traffic-integrated-correlation-sign-criterion')
sign_proof=ROOT/'proofs/P0289_sign_criterion.md'
sign['proof_text']=sign_proof.read_text(encoding='utf-8')
sign['source']['url']=sign_proof.as_uri()
sign['source']['revision']='w346-keep-S1.w342.001-second-order-criterion-only-2026-10-10'

add('C0035','degree-two-determinantal-pair-laws-miss-triple-phase','lemma','Equal pair laws and different determinantal triple laws',
    'The two symbols f_+(theta)=1/2+(4/25)cos(theta)+(2/25)cos(2theta) and f_-(theta)=1/2+(4/25)cos(theta)-(2/25)cos(2theta) both lie in [13/50,37/50]. Their stationary determinantal binary processes have equal one- and two-point marginals at every lag, but their probabilities of X_0=X_1=X_2=1 differ by 16/15625. Pair-law matching therefore cannot certify a full block-factor representation.',namespace='probability.determinantal')
add('C0035','determinantal-sublattice-block-window-transfer','lemma','Conditional transfer of a block factor through sublattices',
    'Let g:T->[0,1] be a trigonometric polynomial and k,r positive integers. If its stationary determinantal process has an r-block representation Y_n=h(U_n,...,U_{n+r-1}) for iid U, then the symbol f(theta)=g(k theta) has the representation X_i=h(U_i,U_{i+k},...,U_{i+(r-1)k}), hence a block window of length 1+(r-1)k. The residue-class copies are independent because the Fourier kernel is block diagonal. This conditional transfer does not establish the unproved reduced-degree case.',
    ['An r-block representation of P_g is already established'],'probability.determinantal')

add('P0001','weighted-theta-block-forests-pairwise-negative-correlation','theorem','Pairwise negative correlation in weighted theta-block forests',
    'Let G be a finite graph whose blocks are bridges or unions of r>=2 internally vertex-disjoint paths between two distinct terminals. Give every edge a positive finite fugacity w_e and sample an acyclic edge set A with probability proportional to product_{e in A}w_e. For every distinct pair e,f, Cov(1_{e in A},1_{f in A})<=0. The assertion includes the uniform-forest law and makes no claim of full negative association.',
    ['Finite graph of the stated block form','Positive finite edge fugacities'],'probability.forests')

add('P0133','torus-dual-tree-complement-homology-unimodularity','lemma','Integral homology basis of a torus dual tree complement',
    'For a finite connected graph cellularly embedded in an oriented torus and a primal spanning tree T, the dual edges complementary to T form a connected one-face graph H. Inclusion H->torus induces an isomorphism H_1(H,Z)->H_1(torus,Z). Thus any integral cycle basis of H has two winding vectors with determinant +/-1 in any oriented torus-period basis.',
    ['Connected cellular embedding in an oriented torus','Primal spanning tree'],'probability.spanning-trees')
add('P0133','torus-theta-core-loop-windings-farey-triangle','lemma','Farey-triangle constraint on torus theta-core windings',
    'Under the torus dual-tree-complement hypotheses, suppose pruning leaves and suppressing degree-two vertices gives a theta core. Orient its three paths between the branch vertices in the same direction. Their three loop windings, in units of the torus periods, are u,v,v-u for a Z^2 basis u,v with det(u,v)=+/-1. Every winding is primitive and every pair has determinant +/-1. This statement is conditional on a theta core and assigns no distributional probabilities.',
    ['The pruned core is theta'],'probability.spanning-trees')
relate('P0133','torus-theta-core-loop-windings-farey-triangle','torus-dual-tree-complement-homology-unimodularity','depends_on','The two path-difference graph cycles are an integral homology basis.')
add('P0133','torus-comb-tree-dual-four-edge-simple-trail-classes','lemma','Four edge-simple trail classes in a torus comb-tree dual',
    'For every L>=3, take the spanning tree on the L-by-L square torus grid consisting of all nonwrapping horizontal row edges and the nonwrapping vertical edges in column zero. Its pruned dual complement is two edge-disjoint loops meeting at one vertex. Under the convention that an edge-simple closed trail may repeat vertices but not edges, it contains four distinct noncontractible homotopy classes up to total reversal, with windings (1,0),(0,1),(1,1),(1,-1). This is a finite-grid convention check, not a scaling-limit distribution assertion.',
    ['L>=3 integer','Edge-simple means no repeated edges; repeated vertices allowed'],'probability.spanning-trees')

add('C0002','gaussian-intermediate-level-tail-relative-log-correction','lemma','Relative log correction in a Gaussian intermediate-level tail',
    'Fix g>0, lambda>0 and a bounded interval of B. For L=log N and H centered Gaussian with variance g(L+B), as L->infinity uniformly over B, P(H>=2sqrt(g)lambda L)=N^{-2lambda^2}exp(2lambda^2 B)/(2lambda sqrt(2pi L)) times [1+(B/2-2lambda^2 B^2-1/(4lambda^2))/L+O(L^{-2})]. The variance remainder B is its exact finite-N value. This is a one-point statement, not a level-set fluctuation theorem.',
    ['Fixed positive g and lambda','Bounded B','L sufficiently large for positive variance'],'probability.gaussian-fields')

add('C0059','binary-stretched-tree-quartic-growth-finite-energy','lemma','Finite-energy unit flow in a quartic-growth tree',
    'Replace each generation-n edge in a binary tree by a path of length 2^{floor(n/3)}, with unit resistances. The resulting degree-three planar tree has quartic volume growth. Equal splitting at each branch gives a unit flow to infinity with energy sum_{n>=0}2^{floor(n/3)}/2^{n+1}=7/6, hence the tree is transient.',
    ['Unit edge resistances'],'probability.random-walks')
add('C0059','quartic-volume-degree-three-trees-recurrence-undetermined','theorem','Quartic volume and bounded degree permit either recurrence behavior',
    'There exist two locally finite planar trees with maximum degree three and |B(o,R)|=Theta(R^4), one recurrent and one transient. The recurrent tree is a ray with finite binary trees of depth floor(3log_2 n) attached at spine vertex n>=2. The transient tree has each generation-n binary-tree edge stretched by 2^{floor(n/3)}. These examples refute volume-growth-only recurrence inferences; neither is asserted to be a Boltzmann map.',namespace='probability.random-walks')
relate('C0059','quartic-volume-degree-three-trees-recurrence-undetermined','binary-stretched-tree-quartic-growth-finite-energy','depends_on','The explicit finite-energy half of the two-graph construction gives transience.')

add('C0083','hamming-graph-local-triangle-and-four-cycle-counts','lemma','Triangles and four-cycles through a Hamming-graph vertex',
    'For integers n>=2,d>=1 in the Hamming graph K_n^d, each vertex has degree D=d(n-1), lies in d binom(n-1,2) triangles and in 3d binom(n-1,3)+binom(d,2)(n-1)^2 simple four-cycles. The two four-cycle terms count coordinate-clique cycles and two-coordinate rectangles, respectively.',
    ['n>=2 and d>=1 integers'],'probability.percolation')
add('C0083','regular-graph-percolation-susceptibility-cubic-coefficient','lemma','Cubic susceptibility coefficient in a regular graph',
    'For independent bond percolation with parameter p on a finite simple D-regular graph, let T_v be the number of triangles through v and chi_v(p)=E_p|C(v)|. Then chi_v(p)=1+Dp+D(D-1)p^2+[D(D-1)^2-4T_v]p^3+O(p^4) as p->0. A finite Taylor series at zero does not determine a critical-value expansion.',
    ['Finite simple D-regular graph','Independent bond percolation'],'probability.percolation')
relate('C0083','regular-graph-percolation-susceptibility-cubic-coefficient','hamming-graph-local-triangle-and-four-cycle-counts','analogous_to','The general cubic coefficient specializes to Hamming graphs using their triangle count; four-cycles enter later.')

add('C0128','nearest-neighbor-walk-sublinear-adverse-drift-transience','theorem','Directional transience from a sublinear adverse-drift budget',
    'Let X_0=0 and X_{n+1}-X_n be +/-1 with history-conditional right probability p_n. If p_*>1/2 and sum_{k<n}(p_*-p_k)_+=o(n) almost surely, then liminf X_n/n>=2p_*-1 almost surely. In particular X_n->+infinity and sup_n X_n=+infinity have probability one; inf_n X_n=-infinity and X_n->-infinity have probability zero.',
    ['Predictable history-conditional probabilities','Almost-sure sublinear adverse-drift budget'],'probability.excited-walks')
add('C0128','finite-adverse-cookie-perturbation-preserves-rightward-speed','lemma','Finite adverse-cookie debt preserves directional transience',
    'For a one-dimensional nearest-neighbor cookie walk, suppose p_*>1/2 and sum_{z in Z,j>=1}(p_*-omega(z,j))_+ is finite almost surely, after conditioning on the environment. Each cookie is used at most once, so liminf X_n/n>=2p_*-1 almost surely. This includes finitely many arbitrary adverse cookies in an otherwise uniformly right-biased environment, including cookies of right probability zero.',
    ['Finite total adverse-cookie debt'],'probability.excited-walks')
relate('C0128','finite-adverse-cookie-perturbation-preserves-rightward-speed','nearest-neighbor-walk-sublinear-adverse-drift-transience','depends_on','The full cookie debt bounds every trajectory\'s accumulated adverse drift.')

add('P0015','complex-four-m-minus-five-open-noninjective-frame-set','theorem','Open sets of noninjective complex frames at 4M-5 measurements',
    'For every integer M>=2 and N=4M-5, a nonempty open subset of complex N-by-M measurement frames fails phaseless injectivity modulo global phase. At H_0=diag(1,-1,0,...,0), the explicit isotropic frame in the proof has a rank-two Hermitian chart Jacobian of determinant 8*64^{M-2}. The implicit function theorem preserves an indefinite rank-two kernel witness under all sufficiently small frame perturbations. Therefore a full-support complex Gaussian frame has failure probability strictly greater than zero, so p_M<1. No bound uniform in M or conclusion p_M->0 is asserted.',
    ['M>=2 integer','Complex Gaussian law has positive density everywhere'],'probability.phase-retrieval')
add('P0015','complex-three-and-seven-measurement-deterministic-noninjectivity','lemma','Deterministic noninjectivity in complex dimensions two and three',
    'Every complex frame with M=2,N=3 or M=3,N=7 fails phaseless injectivity modulo global phase. If the vectors span, a nonzero Hermitian kernel matrix cannot be semidefinite. In dimension two a nonzero kernel matrix exists and has rank two. In dimension three a two-dimensional kernel contains a nonzero singular matrix by the odd cubic determinant and the intermediate value theorem; this matrix is indefinite of rank two. If the vectors do not span, a nonzero blind vector already gives failure. Thus p_2=p_3=0.',namespace='probability.phase-retrieval')

add('P0044','tree-network-canonical-invariant-wired-free-forest-coupling','lemma','Canonical invariant forest coupling on tree networks',
    'On every countable connected locally finite infinite tree network with positive finite conductances, FUSF is the deterministic full edge set E. Sampling W with the WUSF law and setting F=E gives both required marginals, W subset F for every outcome, and a joint law invariant under every conductance-preserving network automorphism. This includes nonamenable regular trees and does not require Folner averaging.',
    ['Countable connected locally finite tree network','Positive finite conductances'],'probability.forests')
add('P0044','inclusion-coupling-equal-edge-marginals-is-diagonal','lemma','Equal edge marginals force an inclusion coupling to be diagonal',
    'For probability laws on subsets of a countable edge set, suppose a coupling (W,F) has W subset F almost surely and P(e in W)=P(e in F) for every edge e. Then W=F almost surely and the two laws coincide. If this common marginal is invariant under a group action, its diagonal coupling is invariant. Countability is used to take the union of the zero-probability edge discrepancies.',
    ['Countable edge set','An inclusion coupling exists','Equal one-edge probabilities'],'probability.forests')

for p in ORDER:
    measurement=ROOT/(p.lower()+'_measurements.json')
    observed=json.loads(measurement.read_text(encoding='utf-8'))
    statement='Measured validation evidence for '+p+': '+json.dumps(observed,ensure_ascii=False,sort_keys=True)+'. These finite checks support the written proof and do not replace its independent audit or establish the full open problem.'
    key=add(p,p.lower()+'-w342-validation-evidence','concept','Finite validation evidence for '+p,statement)
    bundles[p]['entries'][-1]['source']['url']=measurement.as_uri()

# Every new node quotes both its own statement and the existing target card.
for p in ORDER:
    scope=p.lower()+'-w342-result-scope'
    for entry in bundles[p]['entries']:
        relate(p,entry['key'],None,'cites','This result touches the cached problem; no full solution or independent KEEP is implied.',existing=parents[p])
        if entry['key']!=scope:
            relate(p,entry['key'],scope,'cites','The scope card states the unresolved part and the pending independent audit.')

manifest=[]
edges=[]
(ROOT/'bundles').mkdir(exist_ok=True)
(ROOT/'patches').mkdir(exist_ok=True)
for number,p in enumerate(ORDER,1):
    filename=f'bundle_{number:03d}.json'
    path=ROOT/'bundles'/filename
    text=json.dumps(bundles[p],ensure_ascii=False,indent=2)+'\n'
    part=path.with_suffix('.part')
    part.write_text(text,encoding='utf-8')
    part.replace(path)
    live=f'~/math-brain-inbox/w342/{filename}'
    patch=''.join(difflib.unified_diff([],text.splitlines(keepends=True),fromfile='a/'+live,tofile='b/'+live))
    patchfile=f'patches/{number:02d}_{p.lower()}_bundle.diff'
    (ROOT/patchfile).write_text(patch,encoding='utf-8')
    manifest.append({'problem_id':p,'bundle_file':'bundles/'+filename,'patch_file':patchfile,'intended_live_path':live,'entries':len(bundles[p]['entries']),'relations':len(bundles[p]['relations']),'audit_status':'PENDING_w346','full_problem_solved':False})
    edges.extend({'problem_id':p,**edge} for edge in bundles[p]['relations'])
(ROOT/'bundle_handoff.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
(ROOT/'edge_rows.jsonl').write_text(''.join(json.dumps(edge,ensure_ascii=False)+'\n' for edge in edges),encoding='utf-8')
with (ROOT/'results.jsonl').open('a',encoding='utf-8') as handle:
    existing={json.loads(line)['row_id'] for line in (ROOT/'results.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()}
    for path in sorted((ROOT/'results').glob('*.json')):
        row=json.loads(path.read_text(encoding='utf-8'))
        if row['row_id'] not in existing:
            handle.write(json.dumps(row,ensure_ascii=False)+'\n')
print(json.dumps({'bundles':len(manifest),'entries':sum(x['entries'] for x in manifest),'relations':len(edges),'live_writes':0}))
