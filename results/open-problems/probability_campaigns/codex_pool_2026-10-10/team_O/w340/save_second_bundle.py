"""Publish the remaining scoped results and enrich per-result audit rows."""
import difflib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sources=json.loads((ROOT/'SOURCE_REPORT.json').read_text(encoding='utf-8'))
foundations=json.loads((ROOT/'FOUNDATION_REPORT.json').read_text(encoding='utf-8'))
entries=[]
relations=[]
rows=[]
audit_prefix='PROOF OF THE STATED SCOPED RESULT; independent audit pending. '

def add(problem,key,namespace,title,statement,proof,assumptions,measurement,op_kind='specializes',attempt_kind='cites',label='proof'):
    for filename in [proof,measurement]:
        assert (ROOT/filename).is_file(),filename
    entry={'key':key,'namespace':namespace,'logical_name':key,'kind':'lemma','title':title,'statement':audit_prefix+statement,'proof_text':(ROOT/proof).read_text(encoding='utf-8'),'assumptions':assumptions,'domain':'probability theory','source':{'source_id':'owner-own-work:w340:'+key,'url':'urn:owner-own-work:w340:'+key,'revision':'2026-10-10-draft-awaiting-w346','license':'owner-own-work (campaign proof and local check receipt)','excerpt':None}}
    entries.append(entry)
    endpoints=[]
    for prefix,kind in [('Open problem:',op_kind),('Attempt on',attempt_kind)]:
        candidates=[x for x in sources[problem]['store_nodes'] if x['title'].startswith(prefix)]
        assert candidates,(problem,prefix)
        node=candidates[-1]
        logical=json.loads(node['metadata_json'])['logical_id']
        body=node['body'].replace('\n',' ')
        if problem=='C0135' and attempt_kind=='refutes' and prefix=='Attempt on':
            start=max(0,body.index('equivalently')-60)
            quote=body[start:start+260]
            explanation='refutes only the clock-to-inverse scale equivalence in the previous attempt, not the ERW question.'
        else:
            start=body.find('Result:') if prefix=='Attempt on' else body.find(').')+2
            if start<0: start=0
            quote=body[start:start+260].strip()
            explanation='records the precise relationship of this scoped result to the existing card.'
        rationale='New end: "'+statement[:230]+'"; store end: "'+quote+'"; '+explanation
        relations.append({'from_key':key,'to_existing_logical':logical,'kind':kind,'rationale':rationale})
        endpoints.append({'kind':kind,'logical_id':logical,'store_node_id':node['id'],'source_quote':quote})
    rows.append({'problem_id':problem,'entry_key':key,'label':label,'statement':statement,'proof_path':str(ROOT/proof),'measurement_path':str(ROOT/measurement),'audit_status':'PENDING_W346','current_literature_status':'UNVERIFIED_OFFLINE','store_edges':endpoints})

add('C0033','finite-determinantal-entropy-concavity-implies-stationary-entropy-rate-concavity','probability.determinantal','Finite determinantal entropy concavity implies stationary entropy-rate concavity',
    'If Shannon entropy of finite determinantal measures is midpoint-concave in the positive-contraction kernel for every finite set, then the entropy rate of stationary determinantal processes on Z is midpoint-concave in their measurable [0,1]-valued circle symbols. Finite restrictions are linear in the symbol; dividing their inequalities by the interval length and taking the subadditive entropy-rate limit proves the implication. No converse is asserted, and the fixed-diagonal two-site lemma does not supply the premise for all sizes.',
    'c0033_entropy_rate_proof.md',['Finite-kernel concavity is assumed at every size','Stationary binary determinantal processes with symbols in [0,1]'],'CACHED_SOURCE_REPORT.json',op_kind='semantic_association')

add('C0135','inverse-clock-m-squared-log-m-asymptotic','probability.randomenvironment','The inverse of a clock asymptotic to m squared log m',
    'For an increasing deterministic sequence T_m asymptotic to m^2 log(m), the generalized inverse max{m:T_m<=t} is asymptotic to sqrt(2t/log(t)). It is not asymptotic to sqrt(t)/log(t). This corrects an arithmetic implication in C0135-A001; it does not assert that the excited-walk clock has the assumed asymptotic behavior.',
    'c0135_proof.md',['Deterministic increasing clock','T_m/(m^2 log(m)) tends to one'],'c0135_checks.json',op_kind='analogous_to',attempt_kind='refutes',label='proof; refuted route')

add('C0135','uniform-backtracking-gate-for-running-maximum-process-limit','probability.randomenvironment','Uniform backtracking transfers a running-maximum process limit',
    'Let S_k=max_{j<=k} X_j and a_n=sqrt(n) log(n). If for every finite T, max_{k<=floor(nT)} |S_k-X_k|/a_n tends to zero in probability, and S_floor(nt)/a_n converges in the Skorokhod J1 topology to a continuous process Y, then X_floor(nt)/a_n also converges to Y. The identity time change bounds their J1 distance by the displayed uniform norm. A uniform O_P(sqrt(n)) backtracking estimate suffices; a fixed-time estimate alone does not establish this hypothesis. No such estimate under the weaker ERW cookie assumptions is claimed.',
    'c0135_proof.md',['Uniform backtracking hypothesis on every compact time interval','Continuous J1 limit of the rescaled maximum'],'CACHED_SOURCE_REPORT.json',op_kind='semantic_association')

add('P0109','iid-first-passage-geodesics-laplace-nonexplosion-criterion','probability.firstpassage','A Laplace criterion for finite iid FPP geodesics without moments',
    'Let G be a countable connected graph of maximum degree Delta>=2 with iid finite nonnegative edge weights W. If for some theta>0, (Delta-1) E exp(-theta W)<1, then almost surely every vertex pair has a finite path attaining its passage-time infimum. Counting simple paths, exponential Markov bounds and Borel-Cantelli make all bounded-cost competitors have bounded lengths. In particular (Delta-1)P(W=0)<1 suffices, even without a positive lower bound or a finite mean. On Z^d this gives the known sufficient subrange P(W=0)<1/(2d-1), leaving the arbitrary-law question unresolved.',
    'p0109_proof.md',['Countable connected locally finite graph of maximum degree Delta>=2','Iid finite nonnegative weights','Strict Laplace criterion'],'p0109_checks.json')

queue_assumptions=['One FCFS server','Poisson arrival rate lambda>0','Independent exponential service rate mu>lambda','Deterministic nonnegative setup tau and grace g','Setup is never cancelled; setup arrivals queue']
add('P0441','mm1-deterministic-delayedoff-stationary-waiting-power-curve','probability.queueing','Exact M/M/1 deterministic DelayedOff waiting-power curve',
    'For the specified stable one-server DelayedOff queue, put p=exp(-lambda g), x=lambda tau, rho=lambda/mu and y=p/(1+xp), with p=0 at g=infinity. The stationary mean queueing wait is lambda/[mu(mu-lambda)] + tau(1+x/2)y. If busy, on-idle, off and setup powers are B,I,O,U, average power is rho B+(1-rho)I+(1-rho)[O+xU-(1+x)I]y. Hence varying the grace period traces an affine waiting-power curve. The formula includes arrivals during setup and the subsequent busy period. It addresses k=1 and does not claim the many-server frontier or optimality among other policies.',
    'p0441_proof.md',queue_assumptions,'p0441_checks.json')

add('P0441','mm1-delayedoff-regenerative-state-fractions','probability.queueing','M/M/1 DelayedOff regenerative state fractions',
    'In the stable one-server deterministic DelayedOff model, set p=exp(-lambda g), x=lambda tau and rho=lambda/mu. Busy, on-idle, off and setup occupy fractions rho, (1-rho)(1-p)/(1+xp), (1-rho)p/(1+xp), and (1-rho)xp/(1+xp). A cycle from one empty epoch to the next has expected duration mu/[lambda(mu-lambda)](1+xp). These fractions sum to one and include all setup arrivals.',
    'p0441_proof.md',queue_assumptions,'p0441_checks.json')

add('P0441','mm1-killed-busy-period-duration-and-queue-area','probability.queueing','M/M/1 busy-period duration and queue area from k customers',
    'For a continuous-time birth-death queue with birth rate lambda, death rate mu>lambda, killed on hitting zero, the expected busy duration from k>=0 is k/(mu-lambda) and the expected integral of queue length before extinction is k^2/[2(mu-lambda)]+(lambda+mu)k/[2(mu-lambda)^2]. The quadratic function has generator equal to minus k; negative drift gives exponential jump-count tails, which justify stopping and passage to the limit. These identities also average over a Poisson initial queue.',
    'p0441_proof.md',['Constant birth and death rates','0<lambda<mu','Integer starting queue k>=0','Kill the process on hitting zero'],'algebra_checks.json',op_kind='semantic_association')

add('C0045','homogeneous-positive-drift-exponential-box-exit-bound','probability.randomenvironment','Homogeneous positive drift gives exponential backward and transverse exit bounds',
    'For a nearest-neighbour walk on Z^d with iid increments and mean e1 drift u>0, starting at zero, stop at longitudinal +/-L or transverse distance L^3. For some theta>0 and all sufficiently large integer L, the chance of exiting anywhere but the +L face is at most exp(-theta L)+exp(-u^2(L^3-1)/8), and hence below L^(-M) for every fixed M at large L. An exponential supermartingale handles backward exit; bounded iid increments and Hoeffding handle the delayed forward hit. The proof requires iid increments and does not infer the analogous bound from annealed velocity in a general random environment.',
    'c0045_proof.md',['Homogeneous nearest-neighbour iid increments','Strictly positive e1 drift','Start at zero; boxes and stopping rule as stated'],'c0045_checks.json')

add('C0081','all-orders-compact-asymptotics-do-not-locate-critical-pole','probability.percolation','An exponentially small residue can move a critical pole by order 1/d',
    'For integer d>=2 let a_d=1-1/d and F_d(z)=[(1-z)^(-1)+exp(-d)(1-z/a_d)^(-1)]/[1+exp(-d)]. Its Taylor coefficients are nonnegative, F_d(0)=1, and its first pole is a_d. On every fixed [0,1-epsilon], |F_d(z)-(1-z)^(-1)|<=3 exp(-d)/epsilon for all large d, giving the same asymptotic expansion to every order in 1/d, yet its first pole is shifted by 1/d. Thus compact subcritical expansions alone cannot locate a critical point; the lace-free susceptibility route requires additional control near criticality or exclusion of small-residue poles. This is an analytic countermodel to an inference, not a percolation counterexample.',
    'c0081_proof.md',['Specified analytic family, not an asserted susceptibility law','Fixed compact intervals strictly below one'],'c0081_checks.json',op_kind='analogous_to',label='proof; refuted route')

add('C0123','paired-block-nk-exact-bridge-deficit-threshold','probability.gaussian','Exact bridge threshold for a deterministic paired-block NK landscape',
    'For a deterministic K=1 NK-form landscape on 2m bits with F(x)=sum_i J_i 1{x_(2i-1)=x_(2i)}, J_i>0, there are 2^m strict single-bit local maxima, all global. Two peaks differing on pair set D connect by a single-bit path inside {F>=max F-delta} exactly when delta>=max_{i in D} J_i. Every level-set component contains a peak and the component count is 2^(number of J_i>delta). For J_i=1, all peaks are isolated below deficit one and the whole level set is connected at deficit one. This is a deterministic block model, not the typical iid Gaussian NK model with overlapping neighborhoods.',
    'c0123_proof.md',['Disjoint paired neighborhoods','Positive deterministic block weights','Single-bit graph adjacency','Unnormalized summed fitness as stated'],'c0123_checks.json',op_kind='analogous_to')

tensor_assumptions=['Diagonal real order-r tensors, r>=2','p in [2,infinity]','Independent standard coefficient Gaussians; coordinate Gaussians may be correlated','Use the stated multilinear or polynomial norm convention']
add('P0012','diagonal-gaussian-tensor-type-two-all-p','probability.gaussian','Diagonal Gaussian tensor type-2 bounds for every p>=2',
    'For diagonal real order-r multilinear tensors T_i and independent standard g_i, if p<=r then E||sum g_i T_i||_(I_p)<=sqrt(2 log(2d)) sqrt(sum ||T_i||_(I_p)^2). For p>r set q=p/(p-r), q=1 at p=infinity. If q>=2 the same bound holds with constant c_q=(E|g|^q)^(1/q) and no dimension factor; if 1<=q<2 it holds with factor d^(1/q-1/2)=d^(1/2-r/p). These bounds also hold for diagonal homogeneous polynomial norms, multiplying by at most 2^(1/q) for even r and p>r. They imply the proposed d^(1/2-1/p) scale on this diagonal family, up to the stated logarithm and constants. Off-diagonal tensors remain unresolved.',
    'p0012_proof.md',tensor_assumptions,'p0012_checks.json')

add('P0012','diagonal-tensor-multilinear-and-polynomial-norm-identities','probability.gaussian','Diagonal tensor norm identities and the even-degree sign split',
    'Let T_a(x1,...,xr)=sum_j a_j product_k xk_j, with every xk in the l_p unit ball. Its multilinear norm is ||a||_infinity for p<=r and ||a||_q for p>r, q=p/(p-r), with q=1 at p=infinity. For the homogeneous polynomial using one repeated vector, the same identities hold for p<=r and for odd r. For even r and p>r the polynomial norm is max(||a_+||_q,||a_-||_q), so it is within factor 2^(1/q) of the multilinear norm. Explicit Holder optimizers prove all identities; the mixed-sign example r=2,p=infinity,a=(1,-1) has norms two and one.',
    'p0012_proof.md',tensor_assumptions[:-1]+['Norms are explicitly distinguished'],'algebra_checks.json',op_kind='semantic_association')

add('P0038','finite-energy-flow-lift-through-tree-corridors','probability.percolation','A finite-energy gate for a transient graph embedded through corridors',
    'Let an infinite connected locally finite unit-conductance graph C contain a subdivision of a locally finite graph H, replacing each edge e by an internally vertex-disjoint path of length ell_e. If H has a unit flow f from a root to infinity with sum_e ell_e f(e)^2 finite, then C is transient. Lift the constant current along each replacement path; its energy is exactly that sum and its divergence is inherited at branch vertices. Uniformly bounded corridor lengths suffice whenever H is transient. A percolation argument must establish this quantitative energy condition, not only branching topology.',
    'p0038_proof.md',['Connected locally finite unit-conductance graphs','An actual subdivision with disjoint path interiors','A specified root-to-infinity unit flow with finite weighted energy'],'p0038_checks.json',op_kind='semantic_association')

add('P0038','level-subdivided-binary-tree-resistance-criterion','probability.percolation','Exact resistance criterion for a binary tree stretched by levels',
    'In a rooted binary tree whose edges between levels k-1 and k are replaced by paths of integer length ell_k>=1 and unit conductance, resistance from the root to infinity equals sum_{k>=1} ell_k/2^k. Equal current splitting attains this energy and Cauchy-Schwarz on each level gives the matching lower bound. Thus ell_k=k is transient with resistance two, while ell_k=2^k is recurrent. An infinite binary branching topology alone does not guarantee transience after stretching.',
    'p0038_proof.md',['Exactly a level-subdivided rooted binary tree','Integer positive corridor lengths','Unit edge conductances'],'p0038_checks.json',op_kind='analogous_to',label='proof; refuted route')

by_key={e['key']:e for e in entries}
def internal(left,right):
    a,b=by_key[left],by_key[right]
    relations.append({'from_key':left,'to_key':right,'kind':'depends_on','rationale':'From end: "'+a['statement'][len(audit_prefix):len(audit_prefix)+200]+'"; to end: "'+b['statement'][len(audit_prefix):len(audit_prefix)+200]+'"; this calculation supplies a step in the proof.'})
internal('mm1-deterministic-delayedoff-stationary-waiting-power-curve','mm1-delayedoff-regenerative-state-fractions')
internal('mm1-deterministic-delayedoff-stationary-waiting-power-curve','mm1-killed-busy-period-duration-and-queue-area')
internal('mm1-delayedoff-regenerative-state-fractions','mm1-killed-busy-period-duration-and-queue-area')
internal('diagonal-gaussian-tensor-type-two-all-p','diagonal-tensor-multilinear-and-polynomial-norm-identities')
internal('level-subdivided-binary-tree-resistance-criterion','finite-energy-flow-lift-through-tree-corridors')

def foundation(key,topic,logical,kind='depends_on'):
    nodes=[n for n in foundations[topic] if json.loads(n['metadata_json']).get('logical_id')==logical]
    assert nodes,logical
    node=nodes[-1]
    relations.append({'from_key':key,'to_existing_logical':logical,'kind':kind,'rationale':'New end: "'+by_key[key]['statement'][len(audit_prefix):len(audit_prefix)+220]+'"; store end: "'+node['body'].replace('\n',' ')[:220]+'"; uses the named inequality or the indicated convergence analogy.'})
foundation('iid-first-passage-geodesics-laplace-nonexplosion-criterion','markov','math:probability.concentration:markov-inequality')
foundation('homogeneous-positive-drift-exponential-box-exit-bound','hoeffding','math:probability.concentration:hoeffding-inequality')
foundation('diagonal-tensor-multilinear-and-polynomial-norm-identities','holder','math:analysis.lp.inequalities:holder-inequality-lp-exact')
foundation('uniform-backtracking-gate-for-running-maximum-process-limit','slutsky','math:probability.core:slutsky-theorem',kind='analogous_to')

payload={'spec':'mathbrain-draft-v1','author_agent':'w340','bundle_slug':'w340-ten-problem-scoped-progress-20261010','entries':entries,'relations':relations}
local=ROOT/'bundle_002.json'
local.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
inbox=Path('~/math-brain-inbox/w340')
final=inbox/'bundle_002.json'
part=inbox/'bundle_002.part'
assert not final.exists() and not part.exists(),'Do not overwrite any previous draft'
part.write_bytes(local.read_bytes())
part.rename(final)

result_path=ROOT/'results.jsonl'
prior=[json.loads(x) for x in result_path.read_text(encoding='utf-8').splitlines() if x.strip()]
existing={row['row_id']:row for row in prior}
counters={'C0033':1}
for row in rows:
    pid=row['problem_id']
    counters[pid]=counters.get(pid,0)+1
    row['row_id']='w340.'+pid+'.'+str(counters[pid]).zfill(3)
    row['draft_path']=str(final)
    row['command']='python -X utf8 '+('check_algebra.py' if row['measurement_path'].endswith('algebra_checks.json') else 'cached_scopes.py' if row['measurement_path'].endswith('CACHED_SOURCE_REPORT.json') else 'check_remaining.py')
    existing[row['row_id']]=row
ordered=[existing[x['row_id']] for x in prior]
old_ids={x['row_id'] for x in prior}
ordered.extend(row for key,row in existing.items() if key not in old_ids)
result_path.write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in ordered),encoding='utf-8')

patches=ROOT/'patches'
live='~/math-brain-inbox/w340/bundle_002.json'
patch=''.join(difflib.unified_diff([],local.read_text(encoding='utf-8').splitlines(keepends=True),fromfile='a/'+live,tofile='b/'+live))
(patches/'02_remaining_research_bundle.diff').write_text(patch,encoding='utf-8')
print(json.dumps({'draft':str(final),'entries':len(entries),'relations':len(relations),'new_mathematical_rows':len(rows),'total_mathematical_entries':len(entries)+2,'audit_status':'PENDING_W346'},ensure_ascii=False))
