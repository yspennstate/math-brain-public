"""Write the ten-problem proof packet, result rows, and local draft bundle."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CARDS = json.loads((ROOT/'evidence/store_cards.json').read_text(encoding='utf-8'))
ORDER = ['P0189','P0390','C0100','P0031','P0242','C0011','C0070','C0105','C0153','P0025']
DATA = []

def add(pid, key, title, statement, proof, assumptions, relation='semantic_association', target='problem', label='proof; independent audit pending'):
    DATA.append(dict(pid=pid,key=key,title=title,statement=statement,proof=proof,assumptions=assumptions,relation=relation,target=target,label=label))

add('P0189','nilpotent-rotation-approximants','Nilpotent sums of primitive rotation matrices',
    'For q>=2, let omega be a primitive qth root of unity and c a complex number with c^q=-1. On C^q set U e_k=omega^k e_k and V e_k=c e_(k-1 mod q). Then det(zI-U-V)=z^q and (U+V)^q=0.',
    'Each nonzero determinant term uses either all diagonal entries or the entire cyclic permutation. Thus det(zI-U-V)=product_k(z-omega^k)-c^q=(z^q-1)+1=z^q. Cayley-Hamilton gives nilpotency. See the separate P0189 proof for the full construction and strong-convergence reduction.',
    ['q is an integer >=2','omega is a primitive qth root','c^q=-1'], 'specializes')
add('P0189','rotation-strong-convergence-reduction','Strong convergence of rational rotation approximants',
    'Fix an irrational theta and reduced rationals p_j/q_j tending to theta with q_j tending to infinity. The clock/shift pairs U_j,V_j from the nilpotent construction, with omega_j=exp(2*pi*i*p_j/q_j) and c_j=exp(pi*i/q_j), converge in all star-moments and in the norms of every fixed matrix-valued star-polynomial to the canonical irrational rotation pair u,v. This uses simplicity and the faithful canonical trace of the irrational rotation C*-algebra. Combining it with the cited Brown-measure theorem for u+v is a candidate counterexample to a universal Brown-measure convergence implication; the source dependency and full counterexample await independent review.',
    'In the product of matrix algebras modulo norm-null sequences, the classes of U_j,V_j satisfy the irrational rotation relation. Simplicity makes the universal homomorphism injective, hence completely isometric. The quotient norm is the limsup, for every subsequence and every fixed matrix amplification. Therefore polynomial norms converge. A fixed word reduces to a phase times U_j^a V_j^b. Its trace is eventually zero unless a=b=0, and the phases converge, proving canonical star-moment convergence. The Brown-measure assertion is a separate literature dependency, not certified by this algebraic proof.',
    ['theta irrational','q_j -> infinity','p_j/q_j -> theta','simplicity of the irrational rotation C*-algebra','canonical trace faithful'], 'specializes', label='proof of reduction; Brown-measure source dependency pending')

add('P0390','weighted-covariance-hyperuniformity-bound','A weighted covariance criterion for power-saving number variance',
    'Let (eta_x) be a real, stationary, square-integrable field on Z^d, d>=1, with covariance c(z)=Cov(eta_0,eta_z). Suppose sum_z |c(z)|<infinity, sum_z c(z)=0, and M_alpha=sum_z ||z||_infinity^alpha |c(z)|<infinity for some 0<alpha<=1. For every integer L>=1, Var(sum_(x in {1,...,L}^d) eta_x) <= d M_alpha L^(d-alpha). These assumptions on the infinite-volume covariance are sufficient for a power saving; they are not established here for ARW wake states.',
    'The variance equals sum_z n_L(z)c(z), where n_L(z)=product_i (L-|z_i|)_+. Subtract L^d sum_z c(z)=0. The overlap deficit satisfies 0<=L^d-n_L(z)<=d L^d min(1,||z||_infinity/L)<=d L^(d-alpha)||z||_infinity^alpha. Absolute summation proves the claim. A dyadic covariance estimate |c(z)|<=C(1+||z||_infinity)^(-d-beta), beta>alpha, supplies M_alpha<infinity by a geometric annulus sum. Finite-torus conservation alone does not supply the infinite-volume zero sum or a uniform weighted tail bound.',
    ['stationary square-integrable field on Z^d','absolute covariance summability','infinite-volume covariance sum zero','0<alpha<=1','M_alpha finite'], 'semantic_association')

add('C0100','sandpile-periodic-patch-frequency-reduction','Conditional patchwise criterion for sandpile height frequencies',
    'Let B be a bounded Jordan measurable set in R^2 of positive area. Let P_i be countably many disjoint open Jordan measurable patches covering B up to a null set. For every i fix a finite-period Z^2 pattern h_i and let f_i(j) be its fraction of height j in one period. Suppose a discrete configuration s_N on B intersect N^(-1)Z^2 differs from h_i(Nx) at o(N^2) sites in each fixed P_i intersect B. Then for every integer j its height-j frequency in B converges to (1/area(B)) sum_i area(B intersect P_i) f_i(j). This is a sufficient condition; the required patchwise agreement for the actual sandpile, and the sandpile identity-element limit, are not proved here.',
    'For a fixed finite collection of patches, periodic cell counting on Jordan sets gives the stated frequencies, and the o(N^2) mismatches change normalized counts by o(1). Choose finitely many patches covering all but epsilon area of B. Their union and its complement are Jordan measurable, so lattice counting bounds the omitted sites by epsilon N^2+o(N^2). Indicators of a fixed height lie in [0,1]. First let N tend to infinity, then epsilon tend to zero. This avoids an unsupported uniform claim about every small patch or a transition layer around an infinite gasket.',
    ['B bounded Jordan measurable with positive area','patches disjoint and Jordan measurable','patches cover B up to a null set','fixed finite-period pattern in each patch','o(N^2) mismatches in each fixed patch'], 'specializes')
add('C0100','weak-height-convergence-does-not-determine-frequencies','Weak height convergence alone does not determine height frequencies',
    'Weak-* convergence of bounded lattice height functions to a constant does not by itself imply convergence of each height frequency. Alternating arrays equal to 1 everywhere, or to a fine checkerboard of heights 0 and 2, both converge weak-* to 1, while the height-1 frequencies are respectively 1 and 0. A sequence alternating these two array types has a weak-* limit and no height-1 frequency limit. These are generic bounded arrays, not claimed to be stabilized sandpiles.',
    'On every fine checkerboard cell the height difference from 1 has mean zero. Against a continuous test function its integral is bounded by a constant times the modulus of continuity at the cell diameter, hence tends to zero. Boundedness extends the limit to L^1 test functions by density. The constant arrays have the same weak-* limit but a different exact height-1 fraction.',
    ['bounded arrays','weak-* convergence only','no sandpile dynamics assumed'], 'semantic_association')

add('P0031','sparse-first-passage-square-root-threshold','The square-root threshold for exceptional first-passage clock time',
    'Let tau_i be independent standard Brownian first hitting times of -1. For a deterministic exceptional-index set let m(N) count its first N indices and S_N=sum_(i=1 to m(N)) tau_i. For m(N)>0 and epsilon>0, P(S_N>epsilon N)=erf(m(N)/sqrt(2 epsilon N)). Thus S_N/N tends to zero in probability if and only if m(N)/sqrt(N) tends to zero. A zero density m(N)/N->0 alone is insufficient. If m(N)=O(N^(1/2-delta)) for some delta>0, then S_N/N->0 almost surely. These are clock statements, not a construction of a backward or two-sided Brownian law after a finite random shift.',
    'By the strong Markov property, the sum of m independent first hitting times of -1 has the law of a Brownian first hitting time of -m. Brownian scaling and the reflection principle give the displayed erf formula. It tends to zero exactly when m(N)/sqrt(N) does. For the almost-sure assertion, use erf(x)<=2x/sqrt(pi) at N=2^k. The probabilities are O(2^(-delta k)) and summable. Borel-Cantelli and monotonicity of S_N extend the limit from dyadic N to every N. The earlier geometric-index result is included as a special case; the exact in-probability threshold is stronger.',
    ['independent standard Brownian first-passage times','deterministic exceptional indices','m(N) counts the first N indices'], 'specializes')

family_proof=(ROOT/'proofs/P0242.md').read_text(encoding='utf-8')
add('P0242','stationary-flow-lumping-three-halves-lower-bound','Stationary-flow lumping amplification approaches three halves',
    'For finite irreducible reversible chains, any universal K satisfying t_stop(P_hat)<=K t_stop(P) for every stationary-flow lumping must obey K>=3/2. Here t_stop(P)=max_i inf_T E_i T for randomized stopping times with terminal law pi. A four-state family with symmetric weights W=[[0,0,1,0],[0,2s,1,2s],[1,1,0,s],[0,2s,s,4s^2]], P_ij=W_ij/sum_k W_ik, s>0, and blocks {0},{1},{2,3}, has t_stop(P)->2 and t_stop(P_hat)->3 as s->infinity. This proves a candidate lower bound only; existence or sharpness of a universal K is not settled here. Independent review is pending.',
    family_proof,
    ['s>0','P_ij=W_ij/w_i','stationary-flow lumping, not a Markov projection','standard optimal stationary-stopping identity t_stop=max_(i,j)(H_ij-E_pi H_.j)'], 'specializes', label='proof candidate; exact symbolic certificate; audit pending')

add('C0011','ray-knight-additive-square-correction','Ray-Knight local-time identity retains an additive independent square',
    'In the normalized second Ray-Knight identity on a finite symmetric network pinned at a base vertex, the field identity in law is {L_(tau(t))^x + phi_x^2/2}_x =_d {(phi_x+sqrt(2t))^2/2}_x, with the left Gaussian field independent of the walk. It does not assert L_(tau(t))^x =_d (phi_x+sqrt(2t))^2/2. When Var(phi_x)=g>0 and t>0, the local-time marginal has mean t and an atom exp(-t/g) at zero, whereas the shifted Gaussian square has mean t+g/2 and no atom at zero. The omitted term in the earlier C0011 attempt invalidates that transfer step. This correction does not decide present openness of the full planar level-set problem.',
    'For lambda>=0, independence on the left and the elementary Gaussian-square transform give E exp(-lambda L)=exp(-t lambda/(1+g lambda)). This is the Laplace transform of a compound Poisson sum with Poisson mean t/g and exponential jumps of mean g. It has mean t and zero atom exp(-t/g). Directly E[(phi+sqrt(2t))^2/2]=t+g/2, and a nondegenerate Gaussian hits a single value with probability zero. Thus the claimed equality after deleting the independent square is false.',
    ['finite symmetric network with normalized pinned Ray-Knight identity','g=Var(phi_x)>0','t>0','Gaussian field on the left independent of the walk'], 'refutes', 'attempt', label='proof of a correction to an earlier identity; audit pending')
add('C0011','inverse-local-time-square-root-chernoff-bound','Square-root Chernoff rate for inverse-local-time marginals',
    'Let L have Laplace transform E exp(-lambda L)=exp(-t lambda/(1+g lambda)), lambda>=0, where t>0 and g>0. For ell>=t, P(L>=ell)<=exp(-(sqrt(ell)-sqrt(t))^2/g). For 0<=ell<=t, P(L<=ell)<=exp(-(sqrt(ell)-sqrt(t))^2/g). At ell=0 the bound is exact: P(L=0)=exp(-t/g). This supplies a one-point rate, not joint spatial convergence of a local-time level set.',
    'The transform identifies a compound Poisson law with exponential jumps, whose moment generating function is exp(t lambda/(1-g lambda)) for lambda<1/g. For ell>0 choose lambda=(1-sqrt(t/ell))/g in Markov/Chernoff; positive lambda controls the upper tail and negative lambda controls the lower tail. Its optimized exponent is -(sqrt(ell)-sqrt(t))^2/g. Handle ell=0 by lambda tending to minus infinity, or by the compound-Poisson zero atom.',
    ['t>0','g>0','specified local-time/compound-Poisson Laplace transform'], 'semantic_association')

add('C0070','poisson-extinction-duality-rate-identity','Poisson branching extinction duality preserves the total-progeny rate',
    'Let a Poisson(lambda) Galton-Watson process have lambda>1 and extinction probability q in (0,1), satisfying q=exp(-lambda(1-q)). Conditional on extinction its offspring law is Poisson(lambda q). If I(a)=a-1-log a, then I(lambda q)=I(lambda) exactly. For lambda=1+epsilon with epsilon decreasing to zero, lambda q=1-epsilon+(2/3)epsilon^2+O(epsilon^3). This is a branching-process mechanism for discrete duality; it does not prove that hypercube clusters after deleting the giant have this law.',
    'If p_k is the original offspring law, conditioning the k independent descendant processes to become extinct gives p_k q^k/q. For Poisson(lambda), q=e^(lambda(q-1)) reduces this to Poisson(lambda q). Since log q=-lambda(1-q), I(lambda q)=lambda q-1-log lambda-log q=lambda-1-log lambda. Expanding the extinction equation gives 1-q=2epsilon-(8/3)epsilon^2+O(epsilon^3), hence the claimed dual mean. By Stirling, the Borel total-progeny mass has exponential rate I(a). A hypercube proof still needs uniform exploration and dependence estimates; the existing subcritical result must not be replaced by an unverified claim that its matching lower bound is missing.',
    ['Poisson Galton-Watson offspring','lambda>1','q is the nontrivial extinction root'], 'analogous_to')

add('C0105','prime-phase-moment-averaging-bound','An explicit moment window for time-averaged prime phases',
    'Let tau be uniform on [T,2T], T>0, and let A and B be products of at most r prime factors each, all primes <=y, y>=2. For A=B, E exp(-i tau log(A/B))=1. For A!=B its modulus is at most min(1,2/(T |log(A/B)|))<=min(1,2 y^r/T). Independent Haar phases at the primes have the same expectation 1 when A=B and 0 otherwise. Thus for a finite polynomial in these phases and their conjugates with such monomials and coefficient absolute sum M, the time-average versus Haar moment error is at most 2 M y^r/T. This is a sufficient fixed-moment approximation window, not a necessary condition and not a decomposition theorem for log|zeta|.',
    'Integrate the single exponential exactly over [T,2T]. For distinct positive integers A,B, |log(A/B)|>=|A-B|/max(A,B)>=y^(-r). Unique factorization identifies A=B with matching prime exponents, exactly the Haar resonance condition. Sum the monomial errors against absolute coefficients. A growing moment order or prime cutoff requires a quantitative bound on M y^r/T; failure of this upper bound to vanish proves no failure of independence by itself. Controlling the zeta approximation remainder and spatial increments remains separate.',
    ['tau uniform on [T,2T]','T>0','each prime product has at most r factors <=y','finite polynomial with coefficient absolute sum M'], 'semantic_association')

add('C0153','random-cluster-finite-energy-boundary-obstruction','Finite energy obstructs full exterior wiring of every boundary vertex',
    'Consider a finite simple graph with an FK(p,q) law, 0<p<1 and q>=1, with no imposed identification of vertices outside a chosen subgraph H. Suppose H has at least two distinct boundary vertices and boundary vertex v has k incident edges outside H. If xi is the partition of the boundary induced by open paths using only exterior edges, then P(xi is not the one-block wired partition)>=(1-p)^k. In a family of maximum degree D this is at least (1-p)^D>0. Therefore uniqueness of a giant component alone cannot justify an assertion that every fixed boundary vertex is wired together with probability tending to one.',
    'An FK edge conditional open probability is p when its endpoints are already connected and p/(p+q(1-p)) otherwise. Both are <=p for q>=1. Exposing the k exterior edges incident to v in turn gives probability at least (1-p)^k that all are closed. On that event no exterior open path leaves v, so v cannot be identified with another boundary vertex. The domain Markov property gives an interior FK law with the random exterior partition xi, not automatically the fully wired finite-volume law. A correct limit proof must compare the induced exterior partitions or their effects on a smaller ball.',
    ['0<p<1','q>=1','finite simple graph','no deterministic exterior identifications','at least two distinct boundary vertices'], 'semantic_association')

add('P0025','exterior-disk-log-distance-occupation-identity','An exact boundary-occupation functional for synchronous reflection outside a disk',
    'Let X,Y solve the synchronous Skorokhod equations in {|x|>=R}, R>0, with the same continuous driving path and inward-to-domain normal X/R or Y/R on the boundary. Write r=|X-Y| and let L_X,L_Y be their boundary regulators. Before r reaches zero, d log r = (1/(2R))(1-(|Y|^2-R^2)/r^2) dL_X + (1/(2R))(1-(|X|^2-R^2)/r^2) dL_Y. For reflected Brownian motions the same identity holds pathwise because the common Brownian increments cancel in X-Y. Thus coalescence at infinity is equivalent to this signed occupation functional tending to minus infinity. No sign or long-time behavior of that functional is proved here.',
    'The difference X-Y is a continuous finite-variation path. Apply the ordinary chain rule to its squared norm and then its logarithm, localized away from zero. On dL_X support |X|=R and (X-Y).X/R=(r^2+R^2-|Y|^2)/(2R); use the analogous formula for dL_Y. This gives the identity. Integrating it yields log r_t=log r_0 plus the displayed functional, so r_t->0 exactly when that functional tends to -infinity, unless the paths have already met. For R=1 and drive (-t,0), X_0=(1,0) has X_t=(1,0), L_X=t. Starting Y_0=(-2,0) gives r_t=3+t; starting Y_0=(2,0) gives r_t=1-t for 0<=t<1. These deterministic Skorokhod examples confirm both signs; they do not give a positive-probability Brownian asymptotic event.',
    ['R>0','same continuous driving path','normal reflection into the exterior domain','boundary regulators supported on |X|=R or |Y|=R','identity localized before meeting'], 'specializes')

entries=[]
relations=[]
edge_rows=[]
result_rows=[]
for pid in ORDER:
    subset=[item for item in DATA if item['pid']==pid]
    if pid not in ['P0189','P0242']:
        parts=[f'# {pid}: bounded attempt and checked reductions\n\nCurrent-literature status: not certified by this offline pass. Historical source says open; every result below is a partial result or a correction, pending w347.\n']
        for item in subset:
            parts += [f'## {item["title"]}\n\nLabel: {item["label"]}.\n\n{item["statement"]}\n\nProof: {item["proof"]}\n']
        parts += ['\nNEXT: independently audit the stated hypotheses and proof; retain the original problem as unverified rather than promoting a partial result to a solution.\n']
        (ROOT/'proofs'/f'{pid}.md').write_text('\n'.join(parts),encoding='utf-8')
    for item in subset:
        path=ROOT/'proofs'/f'{pid}.md'
        entry={'key':item['key'],'namespace':'probability.open-problems','logical_name':item['key'],'kind':'lemma','title':item['title'],'statement':item['statement'],'proof_text':item['proof'],'assumptions':item['assumptions'],'domain':'probability','source':{'source_id':f'owner:w333:{pid}:{item["key"]}','url':path.as_uri(),'revision':'2026-10-10-unreviewed','license':'owner-own-work','excerpt':None}}
        entries.append(entry)
        targets=[c for c in CARDS.get(pid,[]) if (c['title'].startswith('Attempt on') if item['target']=='attempt' else c['title'].startswith('Open problem:'))]
        targets=[c for c in targets if c['metadata'].get('logical_id') and (pid not in ['P0031','P0025'] or ('Sparse first-passage' in c['title'] if pid=='P0031' else 'Synchronous reflection' in c['title']))]
        for card in targets[:1]:
            quote=card['body'].split('\n')[0][:500]
            rationale=f'New end: "{item["statement"]}" Existing end: "{quote}" Relation applies to the stated reduction or quoted step only; no complete open-problem solution is asserted.'
            relations.append({'from_key':item['key'],'to_existing_logical':card['metadata']['logical_id'],'kind':item['relation'],'rationale':rationale})
            edge_rows.append({'from_key':item['key'],'to_existing_logical':card['metadata']['logical_id'],'kind':item['relation'],'new_end_quote':item['statement'],'existing_end_quote':quote,'existing_node_id':card['id'],'audit_status':'PENDING w347'})
        result_rows.append({'row_id':'S1.O.w333.'+item['key'],'problem_id':pid,'result_type':'lemma','label':item['label'],'statement':item['statement'],'proof_path':path.as_posix(),'entry_key':item['key'],'audit_status':'PENDING w347'})

for from_key,to_key in [('rotation-strong-convergence-reduction','nilpotent-rotation-approximants'),('inverse-local-time-square-root-chernoff-bound','ray-knight-additive-square-correction')]:
    a=next(e for e in entries if e['key']==from_key)
    b=next(e for e in entries if e['key']==to_key)
    relations.append({'from_key':from_key,'to_key':to_key,'kind':'depends_on','rationale':f'New end: "{a["statement"]}" Dependency end: "{b["statement"]}"'})
bundle={'spec':'mathbrain-draft-v1','author_agent':'w333','bundle_slug':'team-o-ten-problems-reductions-w333-20261010','entries':entries,'relations':relations}
(ROOT/'bundles').mkdir(exist_ok=True)
part=ROOT/'bundles/bundle_001.part'
part.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
part.replace(ROOT/'bundles/bundle_001.json')
with (ROOT/'results.jsonl').open('a',encoding='utf-8') as f:
    for row in result_rows:
        f.write(json.dumps(row,ensure_ascii=False)+'\n')
(ROOT/'edges.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in edge_rows),encoding='utf-8')
print(json.dumps({'problems':len(ORDER),'entries':len(entries),'relations':len(relations),'quoted_existing_edges':len(edge_rows),'audit':'PENDING w347'}))
