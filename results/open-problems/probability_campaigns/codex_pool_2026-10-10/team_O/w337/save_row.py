"""Save one result and rebuild the local draft; never touch a live store or inbox."""
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parent
STATEMENTS={
 'P0209':('probability.markov-chains','rare-state-four-state-uniform-clt-counterexample',
 'For every integer s>=2 let A=1-s^(-2), epsilon=(1-A^2)/(5-4A), B=(5-4A)/(2-A), R=s^4. Take independent stationary chains Y in {0,1}, with rates epsilon and 1-epsilon, and Z in {-1,1}, flipping at rate R/2. The observable g=AZ+B(Y-epsilon) has mean zero, variance one and sup norm two, and the product chain has relaxation time one. At time t=s its integral normalized by its asymptotic standard deviation times sqrt(s) tends to zero in probability, has second moment tending to one, and has normal Kolmogorov distance tending to 1/2. Thus the cached chain-independent CLT bound using only sup norm and t/relaxation time is false.'),
 'P0459':('probability.random-graphs','bilateral-preference-mean-deficit-and-simultaneous-bound',
 'Let LK(n,k) retain edges of K_n chosen among the k cheapest incident costs at both endpoints, where edge costs are iid and continuous, n>=2 and 1<=k<=n-1. If D_v is degree and mu=E D_v, then 0<=k-mu<=sqrt(k(n-1-k)/(2n)). For 0<eta<1, P(max_v |D_v-mu|>2 sqrt(2k log(2n/eta)))<=eta. For k<n-1 the exact mean is (n-1) times the integral on [0,1] of P(Bin(n-2,u)<=k-1)^2. In particular k/log n tending to infinity suffices for relative simultaneous concentration around mu.'),
 'C0130':('probability.random-walks','bounded-cookie-finite-interval-escape-upper-bounds',
 'For a deterministic nearest-neighbor excited walk on Z with at most M cookies per site, then fair transitions, assume every transition probability lies in [epsilon,1-epsilon] for fixed epsilon>0. Starting at 1 with positive-site cookies unused, q_L=P_1(T_L<T_0) decreases to P_1(T_0=infinity). Each q_L is the absorption probability of a finite chain with at most (L-1)(M+1)^(L-1) transient states (position and capped visit counts). This state bound grows with L; bounded cookies per site do not give a finite-state representation on the whole half-line. Finite truncations provide upper bounds, not certified lower bounds on escape.'),
 'P0088':('probability.random-graphs','marked-bernoulli-poisson-adaptive-coupling',
 'For a finite family of probabilities p_i in [0,1], let B_i be independent Bernoulli(p_i) and N_i independent Poisson(p_i), retaining the target label i. Under total variation defined as the supremum of event-probability differences, d_TV(Law((B_i)_i),Law((N_i)_i))<=sum_i p_i(1-exp(-p_i))<=sum_i p_i^2. Any target-marked point measure obtained from these vectors satisfies the same bound. For at most m adaptive exposure steps in countable history and exposure spaces whose conditional kernels, whenever histories agree, satisfy corresponding bounds epsilon_j, a sequential maximal coupling fails with probability at most sum_j epsilon_j. This requires control of the actual conditional marked kernels; count approximation alone proves no local graph limit.'),
 'P0336':('probability.optimal-transport','separated-rectangles-opposite-vanishing-tilts',
 'For uniform probability marginals on [0,1]^2 and [2,3]x[0,1], write d=y_1-x_1 in [1,3] and h=y_2-x_2. The minimum mean Euclidean cost is 2 and every optimal coupling preserves the vertical coordinate. For every epsilon>0, the cost sqrt(d^2+h^2)+epsilon d^2 uniquely selects y=(x_1+2,x_2). The cost sqrt(d^2+h^2)-epsilon d^2 uniquely selects y=(3-x_1,x_2). Both costs converge uniformly to Euclidean distance as epsilon decreases to zero, but their optimizing plans have distinct limits. Thus convergence of costs and marginals by itself cannot select the empirical optimizer of the original unperturbed problem.'),
 'C0022':('probability.percolation','summable-separators-for-random-set-law-singularity',
 'Let P and Q be probability laws on the same measurable space of random compact sets. If measurable events A_j satisfy sum_j[P(A_j^c)+Q(A_j)]<infinity, then the measurable event liminf_j A_j has P-probability one and Q-probability zero, hence P and Q are mutually singular. A difference of any finite moments alone does not imply singularity. If both laws have positive mass at the empty set, their full unconditioned laws are not mutually singular; any intended singularity claim must remove that common atom or condition on nonemptiness.'),
 'C0076':('probability.percolation','intrinsic-one-arm-normalization-and-tightness-obstruction',
 'If c/n<=P(A_n)<=C/n for constants 0<c<=C<infinity and n^gamma P(A_n) tends to a finite strictly positive limit, then gamma=1. This necessary one-arm normalization does not prove path tightness. On [1,2], for n>=8 let U be uniform on [5/4,7/4] and Y_n(t)=1+max(1-n|t-U|,0). These continuous processes converge in every fixed finite-dimensional distribution to the constant-one process, yet their laws are not tight in the uniform path topology. Activating these processes independently with probability 1/n and setting them to zero otherwise gives exactly 1/n survival probabilities with the same obstruction under the n-scaled, survival-restricted measures. This is a general counterexample to that inference, not a percolation counterexample.'),
 'C0117':('probability.random-walks','complete-graph-cover-variance-and-exponential-tail',
 'For simple random walk on K_n from a fixed vertex, put m=n-1. In discrete time the cover time is a sum of independent geometric(k/m) variables on {1,2,...}; its mean is m H_m and variance m^2 H_m^(2)-m H_m. In continuous time with independent mean-one exponential holding times the gaps are Exp(k/m), giving variance m^2 H_m^(2) and the same mean. Maximal expected hitting time is m in both conventions. Discrete K_6 has Var(tau_cov)/t_hit^2=145/144>1; continuous K_3 has ratio 5/4>1. These refute only a unit-constant standard-deviation bound. In both conventions P(|tau_cov-E tau_cov|>=s m)<=2 exp(1/4-s/4) for s>=0. This proves the scale and tail for complete graphs, not the all-graph universal-constant conjecture.'),
 'P0009':('probability.random-walks','manhattan-pinball-localization-not-pathwise-monotone',
 'Orient even horizontal rows east and odd rows west; even vertical columns north and odd columns south. A mirror switches the outgoing axis and an empty vertex keeps it. With mirrors exactly at (-3,0),(0,0),(-3,3),(0,3), the trajectory starting in incoming horizontal state at (0,0) has period 12. Adding one mirror at (0,1) makes it escape indefinitely west along row 1. Thus localization is not an increasing event under pointwise addition of mirrors. This deterministic configuration does not refute almost-sure localization in an iid positive-density mirror environment.'),
 'P0035':('probability.random-walks','inward-biased-speed-on-products-of-regular-trees',
 'Let G be the Cartesian product of m infinite (b_i+1)-regular trees, each rooted, with integers b_i>=2. A nearest-neighbor lambda-biased walk gives weight lambda to each neighbor closer to the product root and weight one to each farther neighbor. If 0<lambda<min_i b_i, then its distance from the root divided by time converges almost surely to (sum_i b_i-m lambda)/(sum_i b_i+m lambda)>0. In the balanced case b_i=b this is (b-lambda)/(b+lambda), and the graph has exponential growth rate b. Thus products of equal-degree tree Cayley graphs satisfy the cached speed claim throughout 1<lambda<b; arbitrary Cayley graphs are not covered.')}

def main():
    pid=sys.argv[1]
    namespace,name,statement=STATEMENTS[pid]
    proof=ROOT/(pid+'.md')
    if not proof.is_file():
        raise SystemExit('Missing finished proof report: '+str(proof))
    data={'row_id':'S1.w337.'+pid,'problem_id':pid,'label':'proof',
          'statement':statement,'proof_path':proof.as_posix(),'auditor':'w347','audit_state':'PENDING',
          'solution_counted':False,'literature_status':'offline cached status only; current status and novelty unverified'}
    with (ROOT/'results.jsonl').open('a',encoding='utf-8') as f:
        f.write(json.dumps(data,ensure_ascii=False)+'\n')
    cards=json.loads((ROOT/'evidence'/'store_cards.json').read_text(encoding='utf-8'))
    completed={}
    for line in (ROOT/'results.jsonl').read_text(encoding='utf-8').splitlines():
        row=json.loads(line)
        if row.get('proof_path'):
            completed[row['problem_id']]=row
    entries=[]
    relations=[]
    for key,row in completed.items():
        ns,logical,stmt=STATEMENTS[key]
        entry={'key':'result-'+key.lower(),'namespace':ns,'logical_name':logical,'kind':'lemma',
               'title':'[Blind audit pending] '+logical.replace('-',' '), 'statement':stmt,
               'proof_text':(ROOT/(key+'.md')).read_text(encoding='utf-8'),
               'assumptions':['Exact hypotheses are stated in the complete statement; author proof, independent blind audit pending'],
               'domain':'probability theory',
               'source':{'source_id':'owner-campaign:w337:'+key+':20261010',
                         'url':(ROOT/(key+'.md')).as_uri(),'revision':'author-check-2026-10-10',
                         'license':'owner-own-work (campaign proof; blind audit pending)','excerpt':None}}
        entries.append(entry)
        anchors=[c for c in cards if c['problem_id']==key and c['title'].startswith(('Open problem:','Attempt on '))]
        for card in anchors:
            target=card['metadata'].get('logical_id')
            if not target:
                continue
            relations.append({'from_key':entry['key'],'to_existing_logical':target,'kind':'cites',
                'rationale':'Source end: "'+stmt[:220]+'"; target end ('+card['id']+'): "'+card['body'][:260]+'". The new result addresses this cached question or continues its attempt; it does not promote the full problem to solved.'})
    draft={'spec':'mathbrain-draft-v1','author_agent':'w337','bundle_slug':'team-o-ten-problem-checks-w337-20261010',
           'entries':entries,'relations':relations}
    (ROOT/'bundles').mkdir(exist_ok=True)
    part=ROOT/'bundles'/'bundle_001.part'
    part.write_text(json.dumps(draft,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    part.replace(ROOT/'bundles'/'bundle_001.json')
    print(json.dumps({'saved_problem':pid,'result_rows':len(completed),'draft_entries':len(entries),'quoted_relations':len(relations),'audit':'PENDING'}))

if __name__=='__main__':
    main()
