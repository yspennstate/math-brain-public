"""Build locally staged, audit-pending mathbrain-draft-v1 bundles and deployment diffs."""
from pathlib import Path
import json, sqlite3, difflib, re

ROOT=Path(__file__).resolve().parent
for directory in ['bundles','patches','hooks','audit']:
    (ROOT/directory).mkdir(exist_ok=True)

ENTRIES=[]
META={}
def entry(key,pid,namespace,title,statement,report,assumptions=(),kind='lemma',scope='author proof, pending blind audit'):
    e=dict(key=key,namespace=namespace,logical_name=key,kind=kind,title=title,
           statement=statement,proof_text=(ROOT/'reports'/report).read_text(encoding='utf-8') if kind in {'lemma','theorem'} else None,
           assumptions=list(assumptions),domain='probability theory and related mathematics',
           source=dict(source_id='owner-campaign:w330:'+key,url=(ROOT/'reports'/report).as_uri(),
                       revision='2026-10-10-author-proof-pending-w346',license='owner-own-work',excerpt=None))
    ENTRIES.append(e); META[key]=dict(problem_id=pid,label=scope,proof_path='reports/'+report,audit_status='PENDING_w346',novelty='unverified')

entry('randomized-forward-filling-invariant-mass-criterion','P0032','probability.measure',
      'Randomized forward filling: invariant component mass is the exact criterion',
      'Let T be an invertible measure-preserving transformation of a standard Borel probability space (E,P), I its invariant sigma-field modulo P-null sets, and Q=fP with f>=0 and integral f dP=1. On an extension with independent uniforms, there is an almost surely finite integer N>=0 and Z~P such that T^N Z~Q if and only if E[f|I]=1 almost surely. N need not be a path-filtration stopping time or have finite mean.',
      'P0032_invariant_criterion.md')
entry('critical-beta-splitting-joint-sackin-colless-polynomial','P0347','probability.trees',
      'Exact joint Sackin-Colless law at finite size in the critical beta-splitting model',
      'For n>=2 let q_n(i)=n/(2 H_{n-1} i(n-i)), 1<=i<n, where H_m=sum_{j=1}^m 1/j. Conditional on a split i,n-i assume independent daughter trees of their respective sizes. If S is external path length and C is the sum of the absolute differences of daughter leaf counts, then G_n(u,v)=E[u^S v^C] satisfies G_1=1 and G_n=sum_i q_n(i) u^n v^{abs(n-2i)} G_i G_{n-i}. This identifies each finite-n joint law; it does not identify a limiting law.',
      'P0347_joint_balance.md',['Critical beta=-1 Markov branching, including conditional daughter independence'])
entry('critical-beta-splitting-exact-minimum-child-toll','P0347','probability.trees',
      'Exact minimum-child and quadratic root tolls for a critical beta split',
      'For I with probabilities q_n(i)=n/(2 H_{n-1} i(n-i)), n>=2, E[min(I,n-I)]=(n/H_{n-1})(H_{n-1}-H_floor(n/2)+1_{n even}/n), E[abs(n-2I)]=n-2 E[min(I,n-I)], and E[(n-2I)^2]=n^2-2n(n-1)/H_{n-1}. The even central split is counted once.',
      'P0347_joint_balance.md')
entry('markov-branching-additive-index-covariance-recursion','P0347','probability.trees',
      'Total-variance and covariance recurrences for additive branching indices',
      'In a finite-leaf Markov branching tree with split probabilities q_n(i) and independent daughter trees conditional on i, an additive index A with deterministic root toll t^A_n(i) has mean mu^A_n=sum_i q_n(i)(t^A_n(i)+mu^A_i+mu^A_{n-i}). Put d^A_n(i)=t^A_n(i)+mu^A_i+mu^A_{n-i}-mu^A_n. For two finite-second-moment additive indices A,B, their covariance K_n=sum_i q_n(i)(K_i+K_{n-i}+d^A_n(i)d^B_n(i)). Setting B=A gives the variance recursion. Initial one-leaf values are deterministic.',
      'P0347_joint_balance.md',['Finite second moments','Deterministic one-leaf values','Conditional daughter independence'])
entry('young-diagram-infinite-bad-top-corner-move-family','C0062','combinatorics.partitions',
      'An infinite family refutes the naive dimension-increasing top-corner move',
      'For a>=2 and b>=0, set lambda=(a,a-1,1^b) and mu=(a-1,a-1,1^{b+1}). Their standard Young tableau dimensions satisfy dim(mu)/dim(lambda)=a(a+b-1)/(2(a+b)(b+1)). In particular, for a=b+4 and b>=2 the diagram lambda has width minus number of rows equal to two, yet moving its top-right box to a new bottom row strictly decreases dimension. The ratio tends to 1/2. This refutes that specific move rule, not maximal-dimension uniqueness.',
      'C0062_corner_family.md',['Standard hook-length formula for tableau dimensions'])
entry('two-sided-brownian-concatenation-external-noniid-lengths','P0028','probability.stochastic',
      'Two-sided Brownian concatenation for externally chosen non-iid lengths',
      'Let (B^k)_{k in Z} be mutually independent standard Brownian drivers, and let the entire sequence of positive finite lengths (L_k) be independent of every driver, with partial sums diverging in both directions. Concatenate B^k restricted to [0,L_k] and pin the join between -1 and 0 at time and value zero. The resulting process has two-sided Wiener law at that origin. The lengths may have any joint law; no iid, uniform bound or finite-mean assumption is needed. Path-dependent Brownian stopping lengths are not covered.',
      'P0028_external_lengths.md')
entry('hammersley-rsk-stationary-mixture-certified-truncation','P0220','probability.interacting-particles',
      'Certified truncation error for the stationary Hammersley rank mixture',
      'Assume the ordered stationary drift-jump particle law has its consistent RSK rank representation: first-row labels B=(1=b_1<...<b_k) from uniform permutations restricted to their smallest M labels, and independent unit-rate Poisson arrival spacings, giving independent conditional gamma gaps of shapes b_i-b_{i-1}, with X_1 of shape one. Truncating the nonnegative mixture to b_k<=M omits exactly epsilon_{k,M}=(1/M!) sum_{lambda partition of M, lambda_1<k}(f^lambda)^2, where f^lambda is the number of standard Young tableaux of shape lambda. The density L1 error is epsilon_{k,M}; all event-probability errors and the total variation after normalization are at most epsilon_{k,M}, using sup-event total variation. For k=2 epsilon=1/M!.',
      'P0220_certified_series.md',['Established consistent stationary RSK representation','M>=k>=1'])
entry('hammersley-first-two-density-and-independent-gap','P0220','probability.interacting-particles',
      'First two Hammersley particles: explicit density and independence of the first gap',
      'Under the stationary RSK rank mixture for drift dX_i/dt=X_i and rate-one Poisson space-time left jumps, the first-row label pair is (1,b) with weight (b-1)/b!, b>=2. For 0<x_1<x_2, put g=x_2-x_1. Its joint density is exp(-x_2) F(g), where F(g)=sum_{r>=0}(r+1)g^r/(r!(r+2)!). Consequently X_1~Exp(1) is independent of X_2-X_1, whose density is exp(-g)F(g); F(0)=1/2. The marginal tail is P(X_2>x)=exp(-x) sum_{r>=0}x^r/(r!)^2.',
      'P0220_certified_series.md',['Established stationary RSK rank mixture'],scope='proof of a known-representation consequence, pending audit; no novelty claim')
entry('integer-monotone-exponential-count-real-pole-nonconvergence','C0006','analysis.tauberian',
      'An integer monotone count can have a simple real Laplace pole without a growth limit',
      'For h>=0 put F(h)=floor(exp(h)(1+sin(h)/4)). This is a finite integer-valued nondecreasing right-continuous counting function, realized by nonnegative deterministic heights. For L(beta)=integral_0^infinity exp(-beta h)F(h) dh, beta>1, (beta-1)L(beta)->1 as beta decreases to one, while exp(-h)F(h) has subsequential limits 5/4 and 3/4. Thus a real-axis pole residue and monotonicity do not alone imply the pointwise exponential-growth limit. This array is not a DGFF cluster.',
      'C0006_pole_obstruction.md')
entry('bounded-critical-branching-variance-oscillating-survival-constant','C0066','probability.branching',
      'Critical branching with bounded generation variances can lack a survival constant',
      'Consider independent offspring in generation j with pgf f_{a_j}(s)=1-(1-s)/(1+a_j(1-s)), a_j in {1,2}. Each generation has mean one and variance 2a_j. Survival to generation n from one ancestor has probability p_n=1/(1+sum_{j=1}^n a_j). Alternating a_j=1 and 2 in blocks of lengths 10^(2^(k+1)), k>=0, yields order-1/n survival but n p_n has subsequential limits one and one-half. This refutes a generic inference from bounded critical branching comparisons to an exact constant, not a percolation conjecture.',
      'C0066_varying_environment.md')
entry('finite-asymptotic-series-prefix-does-not-identify-radius','C0097','analysis.series',
      'A finite coefficient prefix cannot identify a formal series radius of convergence',
      'For arbitrary real coefficients a_0,...,a_m, the polynomial P(z)=sum_{j<=m}a_j z^j and the formal series P(z)+sum_{n>m}n! z^n have identical supplied coefficients, but radii of convergence infinity and zero respectively. Alternating factorial signs still give zero radius. A factorial upper bound alone is compatible with either alternative. This gives no divergence result for actual self-avoiding-walk coefficients.',
      'C0097_finite_coefficients.md')
entry('factorial-coefficient-subsequence-sufficient-zero-radius','C0097','analysis.series',
      'A factorial lower bound on an unbounded coefficient subsequence forces zero radius',
      'If a formal power series sum_n a_n z^n has constants c,K>0 and an unbounded sequence n_j such that abs(a_{n_j})>=c K^{n_j} n_j!, then its radius of convergence is zero by Cauchy-Hadamard. Counting unsigned lace diagrams or bounding remainders above does not supply this signed coefficient lower bound.',
      'C0097_finite_coefficients.md')
entry('connected-nested-folner-dumbbells-corridor-obstruction','C0144','probability.percolation',
      'A connected nested Folner exhaustion can retain exponentially unreliable corridors',
      'In nearest-neighbor Z^2, for L=8^j join squares [-L,L-1]^2 and [3L,5L-1] x [-L,L-1] by {(x,-L):L<=x<3L}. The induced sets are connected, nested and exhausting, have volume 8L^2+2L and edge boundary 20L-2, hence form a Folner exhaustion. Any internal path between their squares uses all 2L+1 corridor edges. In iid bond percolation with p<1, its probability is at most p^(2L+1). This does not disprove existence of a different good Folner sequence.',
      'C0144_connected_dumbbells.md')
entry('folner-dumbbell-two-giants-conditional-consequence','C0144','probability.percolation',
      'Conditional two-giant consequence for a connected Folner dumbbell',
      'For the two-square Folner exhaustion with side 2L and a width-one corridor of length 2L, assume under fixed iid bond percolation p<1 that each square restricted to the ambient infinite cluster has one component of size (theta+o_P(1))4L^2, theta>0, and all its other components are o_P(L^2). Then with probability tending to one the two giants are separate within the exhaustion. The second-largest/largest ratio tends to one in probability, and the largest density tends to theta/2. The conclusion is conditional on those finite-square giant assumptions.',
      'C0144_connected_dumbbells.md',['The two stated finite-square giant hypotheses','Fixed p<1 and theta>0'])
entry('planar-finite-crossing-arcs-accessible-adjacency-equivalence','P0020','topology.planar',
      'Finite-crossing arcs are equivalent to finite accessible component chains',
      'For a closed K subset of R^2, call a boundary point z accessible from a component U of R^2 minus K if a continuous path starts at z and lies in U at every positive parameter. Join two complement components in a graph when some point of K is accessible from both. Two distinct points outside K can be joined by an arc meeting K finitely many times exactly when their components are joined by a finite graph path. Thus the simultaneous all-pairs property is equivalent to connectivity of this countable graph. Closure contact alone is insufficient.',
      'P0020_accessible_graph.md',['Arc extraction for a continuous path image in a metric space'])
entry('compact-nested-circles-infinite-crossing-obstruction','P0020','topology.planar',
      'A compact union of nested circles can force infinitely many arc contacts',
      'Let K be the unit circle together with all circles of radii 1+1/n, n>=1. K is compact. Every continuous path from the origin to a point of radius three intersects each of those circles by the intermediate value theorem, so no such path has finitely many K-contacts. The inner disk is isolated in the accessible adjacency graph. This is a deterministic compact-set example, not Brownian-trace evidence.',
      'P0020_accessible_graph.md')

entry('p0032-candidate-proof-provenance-note','P0032','probability.open-problems',
      'P0032 proof provenance: raw titles do not establish the active audited status',
      'The inspected store contains PROVED and CANDIDATE titles for one P0032 logical ID, while the cited 2026-09-06 construction explicitly says no independent review and no novelty claim. Raw nodes may be historical revisions; this observation does not establish a current serving defect or refute the construction. Before counting a new full solution, check the active revision, an independent KEEP and the full proof, including permitted prefix randomness and time dependence.',
      'REVIEW_LIMITS.md',kind='concept',scope='source-supported provenance note')
entry('c0144-cached-source-locator-unverified','C0144','probability.open-problems',
      'C0144 cached locator needs a source-version check',
      'The assigned C0144 ledger cites Question 12.34, p.170 in Pete notes for a Folner giant-component question. The inspected cached notes instead locate Exercise 12.34 at PDF page 140, concerning invariant percolation with finite clusters, and a targeted search did not locate the giant question. Keep this source locator and current global status unverified until the matching source version is supplied. This is not an absence claim about all versions.',
      'REVIEW_LIMITS.md',kind='concept',scope='cached source mismatch, pending paired audit')

ROUTES=[
 ('refuted-route-width-gap-forces-top-corner-improvement','C0062','combinatorics.partitions','REFUTED ROUTE: width at least height plus two always makes the move from the top-right box to a new row increase tableau dimension. An infinite family disproves this specific rule.','C0062_corner_family.md','young-diagram-infinite-bad-top-corner-move-family'),
 ('refuted-route-real-laplace-pole-and-monotonicity-force-count-limit','C0006','analysis.tauberian','REFUTED ROUTE: a monotone integer count with a real-axis simple exponential Laplace pole must have a pointwise normalized limit. An explicit oscillating counting function disproves this generic implication.','C0006_pole_obstruction.md','integer-monotone-exponential-count-real-pole-nonconvergence'),
 ('refuted-route-bounded-branching-variance-forces-arm-constant','C0066','probability.branching','REFUTED ROUTE: critical offspring means and uniformly positive bounded variances, without time homogeneity or variance averaging, force convergence of n times survival probability. A varying-environment example disproves this implication.','C0066_varying_environment.md','bounded-critical-branching-variance-oscillating-survival-constant'),
 ('refuted-route-finite-coefficient-growth-certifies-series-divergence','C0097','analysis.series','REFUTED ROUTE: rapid growth of an arbitrary finite coefficient prefix certifies zero convergence radius. Entire and zero-radius tails can share every supplied coefficient. Actual coefficient non-cancellation still needs proof.','C0097_finite_coefficients.md','finite-asymptotic-series-prefix-does-not-identify-radius')]
for key,pid,ns,s,report,_ in ROUTES:
    entry(key,pid,ns,key.replace('-',' ').capitalize(),s,report,kind='concept',scope='refuted proof route')

cards=[]
for name in ['matched_store_cards.json','assigned_store_cards_full.json']:
    cards.extend(json.loads((ROOT/'reports'/name).read_text(encoding='utf-8')))
c=sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True)
for pid in ['P0032','P0347','C0062','P0028','P0220','C0006','C0066','C0097','C0144','P0020']:
    for row in c.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE metadata_json LIKE ? AND title LIKE 'Open problem:%' LIMIT 2",('%open-problem-'+pid.lower()+'%',)):
        cards.append(dict(zip(['id','kind','title','body','metadata'],row)))
c.close()
cards=list({x['id']:x for x in cards}.values())
(ROOT/'reports'/'resolved_edge_cards.json').write_text(json.dumps(cards,ensure_ascii=False,indent=2),encoding='utf-8')

targets={}
for card in cards:
    logical=json.loads(card['metadata']).get('logical_id')
    if not logical: continue
    for pid in ['P0032','P0347','C0062','P0028','P0220','C0006','C0066','C0097','C0144','P0020']:
        if ('open-problem-'+pid.lower()) in logical and card['title'].lower().startswith('open problem:'):
            targets[pid]=card
    if logical=='math:probability.stochastic:candidate-brownian-equivalent-suffix-finite-prefix-embedding': targets['P0032']=card
    if logical=='math:probability.measure:randomized-nonnegative-shift-to-absolutely-continuous-ergodic-law': targets['filling']=card
if 'C0144' not in targets:
    key='c0144-folner-single-giant-question-source-unverified'
    entry(key,'C0144','probability.open-problems','C0144: the Folner single-giant question, source locator unverified',
          'Recorded open question: for an amenable transitive graph under supercritical iid percolation, with its unique infinite cluster C_infinity and density theta(p), is there a connected Folner sequence F_n such that almost surely the largest component of F_n intersect C_infinity has density theta(p) in F_n and the second-largest/largest size ratio tends to zero? Folner means edge boundary divided by volume tends to zero. This is a question, not a theorem. The cached primary locator and current global resolution status are unverified.',
          'REVIEW_LIMITS.md',kind='concept',scope='problem node from assigned ledger, source locator unverified')
    e=ENTRIES[-1]
    targets['C0144']=dict(id='draft:w330:'+key,title=e['title'],body=e['statement'],draft_key=key,
                          metadata=json.dumps(dict(logical_id='math:'+e['namespace']+':'+key)))
assert set(targets)>={'P0032','P0347','C0062','P0028','P0220','C0006','C0066','C0097','C0144','P0020','filling'}, targets.keys()

bykey={x['key']:x for x in ENTRIES}
relations=[]; edge_evidence=[]
def existing_link(e,card,kind):
    logical=json.loads(card['metadata'])['logical_id']
    sq=e['statement']; tq=card['body'][:280]
    why='Source: "'+sq+'" Target: "'+tq+'"'
    target=dict(to_key=card['draft_key']) if 'draft_key' in card else dict(to_existing_logical=logical,to_node_id=card['id'])
    relation_target={k:v for k,v in target.items() if k!='to_node_id'}
    relations.append(dict(from_key=e['key'],**relation_target,kind=kind,rationale=why))
    edge_evidence.append(dict(from_key=e['key'],**target,kind=kind,source_quote=sq,target_quote=tq,audit_status='PENDING_paired_Codex'))
for e in ENTRIES:
    target=targets[META[e['key']]['problem_id']]
    if target.get('draft_key')!=e['key']: existing_link(e,target,'cites')
existing_link(bykey['randomized-forward-filling-invariant-mass-criterion'],targets['filling'],'generalizes')
for route,*_,prover in ROUTES:
    s=bykey[prover]['statement']; t=bykey[route]['statement']
    relations.append(dict(from_key=prover,to_key=route,kind='refutes',rationale='Source: "'+s+'" Target: "'+t+'"'))
    edge_evidence.append(dict(from_key=prover,to_key=route,kind='refutes',source_quote=s,target_quote=t,audit_status='PENDING_paired_Codex'))
prover='folner-dumbbell-two-giants-conditional-consequence';target='connected-nested-folner-dumbbells-corridor-obstruction'
relations.append(dict(from_key=prover,to_key=target,kind='depends_on',rationale='Source: "'+bykey[prover]['statement']+'" Target: "'+bykey[target]['statement']+'"'))
edge_evidence.append(dict(from_key=prover,to_key=target,kind='depends_on',source_quote=bykey[prover]['statement'],target_quote=bykey[target]['statement'],audit_status='PENDING_paired_Codex'))

bundle=dict(spec='mathbrain-draft-v1',author_agent='w330',bundle_slug='w330-open-problems-ten-20261010',entries=ENTRIES,relations=relations)
text=json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
part=ROOT/'bundles'/'bundle_001.part'; final=ROOT/'bundles'/'bundle_001.json'
part.write_text(text,encoding='utf-8'); part.replace(final)
(ROOT/'EDGE_ROWS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in edge_evidence),encoding='utf-8')
initial=(ROOT/'RESULT_ROWS.jsonl').read_text(encoding='utf-8').splitlines()
initial=[line for line in initial if not json.loads(line).get('bundle_key')]
rows=[]
for e in ENTRIES:
    m=META[e['key']]; rows.append(dict(row_id='S1.O.w330.'+m['problem_id']+'.'+e['key'],
        bundle_key=e['key'],**m,statement=e['statement'],source_quote=e['statement'],
        source_path='bundles/bundle_001.json',source_json_key=e['key']))
(ROOT/'RESULT_ROWS.jsonl').write_text('\n'.join(initial+[json.dumps(r,ensure_ascii=False) for r in rows])+'\n',encoding='utf-8')

hook=dict(id='math-w330-01',area='math',event='PreToolUse',cue='candidate proof is about to be promoted to solved without an independent proof receipt',
    fire_when='Promote an author-checked candidate using only a ledger validator or a raw PROVED title.',
    silent_when='The result is explicitly pending audit, or an independent KEEP and full proof receipt are attached.',
    text='Before promoting a candidate to solved, check the active revision, independent KEEP and full proof receipt. Ledger validity and a raw title do not establish a proof audit.',
    evidence='burdzy_scheutzow_75_yes_by_a_filling_scheme_2026_09_08; reports/resolved_edge_cards.json; reports/REVIEW_LIMITS.md',proposer='w330')
hooktext=json.dumps(hook,ensure_ascii=False)+'\n'
(ROOT/'hooks'/'math-w330.jsonl').write_text(hooktext,encoding='utf-8')
def patch(destination,text,output):
    diff=''.join(difflib.unified_diff([],text.splitlines(keepends=True),fromfile='a/'+destination,tofile='b/'+destination))
    (ROOT/'patches'/output).write_text(diff,encoding='utf-8')
patch('~/math-brain-inbox/w330/bundle_001.json',text,'01_mathbrain_bundle.diff')
patch('~/primary_directive/hooks1000/proposals/math-w330.jsonl',hooktext,'02_provenance_hook.diff')

request=dict(auditor='w346',secondary_edge_auditor='w347 on a distinct account, or another distinct-account Codex peer',
    bundle_path=str(final),proofs_directory=str(ROOT/'reports'),claims=[dict(key=e['key'],**META[e['key']]) for e in ENTRIES],
    requested_verdict_path=str(ROOT/'audit'/'w346_verdict.jsonl'),
    instructions='Derive or check independently; record KEEP/FIX/DROP per key with mathematical reasons and account identity. Check scope and hypotheses. Full solutions are not requested or counted. Independent full proof review is required for any future solution promotion. Edges need paired distinct-account Codex KEEP. Do not deploy before required keeps.',
    current_keeps=0,delivery='Local file handoff; worker cannot use send commands or write outside w330')
(ROOT/'AUDIT_REQUEST.json').write_text(json.dumps(request,indent=2),encoding='utf-8')
event=dict(agent='w330',row='S1.O.w330.ten-problems',evidence=str(final),event=f'10 assigned problems: {len(ENTRIES)} draft nodes, {len(relations)} quoted edges, measured proof controls; pending w346 audit.')
(ROOT/'PROGRESS_PENDING.jsonl').write_text(json.dumps(event)+'\n',encoding='utf-8')
from write_cost_receipt import write_cost_receipt
write_cost_receipt()
print(json.dumps(dict(entries=len(ENTRIES),relations=len(relations),results=len(rows)+len(initial),paired_edge_rows=len(edge_evidence),keeps=0)))
