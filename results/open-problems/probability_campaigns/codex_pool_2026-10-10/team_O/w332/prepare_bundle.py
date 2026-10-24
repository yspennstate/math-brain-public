"""Build typed, independently unreviewed mathematical drafts, without ingestion."""
import difflib
import json
from pathlib import Path

root=Path(__file__).resolve().parent
entries=[]
relations=[]
catalog=[]

def add(pid,name,title,kind,statement,assumptions,proof=None):
    key=pid.lower()+'-'+name
    if kind in ['lemma','theorem'] and not proof:
        raise ValueError('Missing proof: '+key)
    entry={'key':key,'namespace':'probability.open-problems','logical_name':key,
        'kind':kind,'title':title,'statement':statement,'proof_text':proof,
        'assumptions':assumptions,'domain':'probability and mathematical proof auditing',
        'source':{'source_id':'owner-w332-20261010:'+key,
        'url':'urn:mathbrain:owner:campaign:20261010:w332:'+key,
        'revision':'author-checked-2026-10-10; independent w346 audit pending',
        'license':'owner-own-work',
        'excerpt':'Original worker derivation; see '+str(root/'reports'/f'{pid}_attempt.md')}}
    entries.append(entry)
    catalog.append((pid,entry))
    return key

p174mom=add('P0174','centered-diameter-moment-inequality','Centered second and fourth moments under a diameter bound','lemma',
    'If a real random variable X has mean zero and support in an interval of length D, with a=E X^2 and b=E X^4, then a<=D^2/4 and b+3a^2<=D^2 a.',
    ['X has mean zero','X is supported in an interval of finite length D'],
    'For support [l,h], E[(X-l)(h-X)]>=0 gives a<=-lh<=(h-l)^2/4. For an independent copy X-prime, (X-X-prime)^4<=D^2(X-X-prime)^2 pointwise. Centering gives E(X-X-prime)^4=2b+6a^2 and E(X-X-prime)^2=2a; divide by 2.')
p174profile=add('P0174','strict-cauchy-profile-minimum-bound','Strict lower bound for a separating Cauchy-profile minimum','lemma',
    'Let mu be a probability law with compact support of diameter at most D>0 and let R>0. Every local minimum of F(u)=integral ((x-u)^2+R^2)^(-1)dmu(x) has F(u)>1/D^2.',
    ['mu is a compactly supported probability law','D>0 bounds its support diameter','R>0'],
    'At a stationary point set y=R^2, Z=integral ((x-u)^2+y)^(-2)dmu, and reweight dQ=Z^(-1)((x-u)^2+y)^(-2)dmu. Under Q, X=x-u is centered; let a=E X^2,b=E X^4. Normalization gives 1/F=(b+2ay+y^2)/(a+y). Differentiation gives F-second/(2Z)=3-4y E_Q[1/(X^2+y)]. If F-second>=0, Jensen gives y<=3a. The moment bounds then imply 1/F-D^2<=((y-3a)(y+a)+(4a-D^2)y)/(a+y)<=0. Equality requires y=3a,4a=D^2 and the symmetric endpoint law. For that law F(u)-F(0)=-u^4/[4a(16a^2+4au^2+u^4)]<0 away from zero, so equality is a strict maximum and cannot be a local minimum.')
p174candidate=add('P0174','unimodality-constant-one-reconstruction','P0174 candidate constant one with endpoint check','concept',
    'AUTHOR-CHECKED FULL CANDIDATE, not an independently audited solution: for compactly supported initial probability laws with support diameter D>0, the strict Cauchy-profile minimum bound rules out more than two roots at every level 1/t<=1/D^2. The sufficient Hasebe-Ueda Lemma 3.1 was checked in the cached primary text with semicircle variance t and yields the candidate conclusion of unimodality for t>=D^2. A point mass handles D=0. The symmetric endpoint law fails just below D^2, giving candidate sharp constant C=1. Independent blind KEEP, full proof check, and literature novelty remain outstanding.',
    ['Compactly supported initial probability law','Semicircle variance t','Cached Lemma 3.1 is used only in its sufficient direction'])

p389mass=add('P0389','fixed-mass-complement-variance','Fixed-mass complement variance identity','lemma',
    'For binary occupations on N sites with deterministic total k, S_B=k-S_(B-complement), so Var(S_B)=Var(S_(B-complement))<=min(|B|,N-|B|)^2/4. For a translation-invariant law and a one-site complement, the variance is (k/N)(1-k/N).',
    ['Binary occupations','Deterministic total k','Translation invariance only for the final equality'],
    'The complement identity holds for every configuration. A sum over m binary sites has range in [0,m], giving variance at most m^2/4; apply to each complement. Under translation invariance the omitted occupation is Bernoulli with mean k/N.')
p389subset=add('P0389','uniform-subset-mesoscopic-variance','Fixed mass permits ordinary mesoscopic variance','lemma',
    'Under the uniform k-subset law on N>=2 sites, a window of m sites has variance m*rho*(1-rho)*(N-m)/(N-1), where rho=k/N. If rho tends to rho_0 in (0,1), m tends to infinity and m/N tends to zero, its variance divided by m tends to rho_0(1-rho_0)>0. This comparison measure is not identified with the ARW free-chain law.',
    ['Uniform k-subset law','N>=2','The mesoscopic conclusion uses m/N -> 0'],
    'Each occupation has mean rho and variance rho(1-rho). Two distinct sites are both occupied with probability k(k-1)/(N(N-1)), giving covariance -rho(1-rho)/(N-1). Summing m variances and m(m-1) covariances gives the formula and its stated limit.')

c89zero=add('C0089','zero-intensity-vacant-walk-invariance','Zero-intensity vacant-set walk boundary case','lemma',
    'At interlacement intensity u=0 the vacant set is Z^d. For d>=1, simple random walk on it has n^(-1/2) X_(floor(nt)) converging to Brownian motion with covariance t I_d/d. This zero-intensity boundary case does not establish the quenched theorem at positive u.',
    ['u=0','Discrete-time simple random walk','d>=1','The standard functional CLT for i.i.d. increments'],
    'The increments are independent, uniformly distributed on the 2d signed coordinate vectors. Their mean is zero and covariance is I_d/d. The i.i.d.-increment functional central limit theorem gives the claimed covariance and path limit; the environment at u=0 is deterministic.')
c89map=add('C0089','full-phase-hypothesis-matching-gap','C0089 full-phase literature lead needs hypothesis matching','concept',
    'UNVERIFIED literature lead: the local intake suggests combining Procaccia-Rosenthal-Sapozhnikov (2016) with the 2023 vacant-set sharpness theorem. Equality of critical thresholds alone does not verify every stationarity, sprinkling, density-continuity and walk-normalization hypothesis in the invariance-principle framework. For a framework whose occupancy parameter must increase, vacant-set intensity may require reparametrization by v=1/u. Constants may depend on a compact interval below u-star; no uniformity at u-star is asserted.',
    ['No exact matched PRS and sharpness theorem quotes were inspected'])

p30splice=add('P0030','independent-brownian-splice-sufficient-condition','Common-time and independent finite-bridge Brownian splices','lemma',
    'If for a possibly random T the two path processes X(T+t)-X(T) and X(T-t)-X(T), t>=0, are independent standard Brownian motions, the centered shifted path is standard two-sided Brownian motion. A deterministic finite Brownian bridge segment independent of the two Brownian tails also gives a two-sided Brownian path when concatenated continuously.',
    ['Both entire half-paths have Brownian marginal laws at the proposed splice','The path pieces are independent','The bridge length, if used, is deterministic'],
    'For the common splice define Y(s)=B-plus(s) for s>=0 and Y(s)=B-minus(-s) for s<=0. Split any family of disjoint increments at zero. Each increment is a sum of independent centered Gaussian Brownian increments, with variance the original interval length, and disjoint increments remain independent. The same splitting at both 0 and a deterministic L proves the three-piece version Y(s)=B-mid(s) on [0,L] and Y(s)=B-mid(L)+B-plus(s-L) above L. Continuity and the Gaussian increment laws identify the two-sided Brownian law.')
p30bias=add('P0030','future-selected-time-brownian-bias','A future-selected splice can lose Brownian marginals','lemma',
    'Let B be standard Brownian motion. Define T=0 when B(1)>0 and T=1 otherwise. Then E[B(T+1)-B(T)]=1/sqrt(2*pi)>0, so the selected one-step increment is not a standard Brownian increment. This T is not assumed to be a stopping time.',
    ['B is standard Brownian motion','T uses the stated future-dependent selection rule'],
    'The expectation is E[B(1) 1_(B(1)>0)] + E[(B(2)-B(1)) 1_(B(1)<=0)]. The second term is zero by independent centered increments. The first is integral_0^infinity z exp(-z^2/2)/sqrt(2*pi) dz=1/sqrt(2*pi).')

p234margin=add('P0234','uniform-net-margin-negative-moments','Conditional safe-margin tail and inverse moments','lemma',
    'Let K be a deterministic nonempty compact set and F a random closed set in Euclidean space. Suppose for 0<delta<=delta_0 that K has a delta-net with at most C delta^(-d_0) centers in K, and sup_(x in K) P(dist(x,F)<=2delta)<=C-prime delta^alpha with alpha>d_0. For R=dist(K,F), gamma=alpha-d_0 and A=C*C-prime, P(R<=delta)<=A delta^gamma and R>0 almost surely. For 0<p<gamma, E[R^(-p)]<=delta_0^(-p)+A*p*delta_0^(gamma-p)/(gamma-p), taking infinity^(-p)=0.',
    ['K is deterministic and compact','F is random closed','Uniform bound over K','alpha>d_0','delta_0>0'],
    'If R<=delta, a closest point of K is within delta of F. A delta-net center is within 2delta of F, so a union bound proves the tail inequality. Letting delta decrease to zero excludes R=0. Compactness of K and closedness of F make disjointness equivalent to positive separation. Apply the layer-cake identity p integral_0^infinity delta^(-p-1)P(R<delta) ddelta, using the tail bound below delta_0 and probability at most one above it. Both integrals give the stated bound. The comparison tail delta^gamma on (0,1) has divergent gamma-th inverse moment, so the endpoint is not guaranteed.')

c10scale=add('C0010','dirichlet-dgff-constant-conductance-scaling','Exact DGFF scaling under constant conductance multiplication','lemma',
    'On a finite conductance network with Dirichlet boundary and positive-definite unnormalized Dirichlet Laplacian L, a DGFF has covariance L^(-1). Multiplying all conductances by a>0 divides the covariance by a and gives the field law h/sqrt(a).',
    ['Finite network','Every interior component reaches the Dirichlet boundary','Unnormalized conductance Laplacian','a>0'],
    'The conductance energy and its Laplacian both multiply by a. The inverse becomes L^(-1)/a. Centered Gaussian laws are determined by their covariances, which equals the covariance of h/sqrt(a).')
c10energy=add('C0010','dirichlet-dgff-ellipticity-covariance-comparison','Uniform-ellipticity comparison of DGFF covariance forms','lemma',
    'For a finite network as above with lambda<=c_e<=Lambda, 0<lambda<=Lambda, and unit-conductance Dirichlet Laplacian L_0, its DGFF covariance G_c obeys G_0/Lambda<=G_c<=G_0/lambda in quadratic-form order. This controls linear-functional variances and by itself asserts no universal extremal-process law.',
    ['Finite network with Dirichlet boundary','Positive definite Dirichlet Laplacians','0<lambda<=c_e<=Lambda','Unnormalized energy convention'],
    'The edge-energy representation gives lambda L_0<=L_c<=Lambda L_0. For any positive-definite L, f^T L^(-1)f=sup_v(2f^Tv-v^TLv). Increasing L decreases this supremum, so inversion reverses quadratic-form order and proves the sandwich.')
c10rate=add('C0010','ergodic-limit-does-not-supply-summable-scale-errors','A qualitative scale limit does not supply bounded cumulative error','concept',
    'The stored C0010 route has not verified a theorem giving the uniform O(1) Green-function remainder needed by its multiscale argument under arbitrary stationary ergodic conductances. Errors e_j=1/j tend to zero while their accumulated sum diverges, so a qualitative limiting estimate alone is insufficient. This is a gap in that route, not a counterexample to the random-conductance DGFF theorem.',
    ['This warning concerns the cited route, not impossibility of another proof'])
c10status=add('C0010','unverified-resolved-card-status-conflict','C0010 resolved title has no inspected resolving reference','concept',
    'The inspected store contains both an open C0010 card and a card titled Resolved whose body says unverified and provides no resolving reference. The matching cached campaign alias P0475 has result_status held. Neither title nor that held record certifies a resolving theorem. Full level-set and extremal-process resolution, and the claim that the cluster law must be random, remain unverified in this packet.',
    ['Status only of the inspected local source cards'])

c68scale=add('C0068','critical-window-crossover-scale-reversal','Correct torus crossover comparison and explicit gap sequence','lemma',
    'For d>6 and V tending to infinity, V^(-1/3)<<V^(-2/d). With beta=(1/3+2/d)/2 and eps=V^(-beta), eps/V^(-1/3) tends to infinity but eps/V^(-2/d) tends to zero. Thus the entire window-above regime is not above the V^(-2/d) crossover; the stored opposite implication is false.',
    ['d>6','V>0 tends to infinity','The symbol << means the ratio tends to zero'],
    'Since 2/d<1/3, V^(-2/d)/V^(-1/3)=V^(1/3-2/d) tends to infinity. The midpoint exponent satisfies 2/d<beta<1/3, so the two eps ratios have respectively positive and negative exponents. Under xi~eps^(-1/2), xi/V^(1/d)=V^(beta/2-1/d) grows along this sequence; that heuristic cannot supply the earlier crossover justification.')

c101quad=add('C0101','integer-binomial-quadratic-laplacian-witness','Integer binomial quadratics have exact trace Laplacian','lemma',
    'For every symmetric integer matrix A in dimension d, g_A(x)=sum_i A_ii*x_i*(x_i-1)/2+sum_(i<j) A_ij*x_i*x_j is integer valued on Z^d, differs from x^T A x/2 by a linear term, and has unnormalized nearest-neighbor Laplacian Delta g_A=tr(A). It is a witness for a threshold Delta g<=K when tr(A)<=K, after matching the intended growth convention; no general maximality claim is made.',
    ['A is a symmetric integer matrix','Nearest-neighbor unnormalized Laplacian','K is an explicitly stated threshold'],
    'Every x_i(x_i-1) is even. The diagonal binomial term has second difference A_ii in direction i, and each cross term is affine in each coordinate and has zero second difference. Sum over directions to obtain tr(A). Expanding the binomial diagonal terms gives the specified quadratic plus linear term.')
c101round=add('C0101','ceil-quadratic-curvature-counterexample','Counterexample to the stored ceiling-curvature bound','lemma',
    'For g(x)=ceil(a*x^2/2) on Z, the stored bound Delta g<=a+1 is false: a=1/2 gives Delta g(0)=2>3/2. The universally valid rounding estimate is Delta g(x)<a+2 for every real a and integer x.',
    ['Nearest-neighbor one-dimensional Laplacian','a is real and x is integer'],
    'At a=1/2 the values at -1,0,1 are 1,0,1. In general write g(x)=a*x^2/2+e(x) with 0<=e(x)<1. Then Delta g=a+e(x+1)+e(x-1)-2e(x)<a+2.')

c148finite=add('C0148','residually-finite-cayley-local-quotients','Exact finite-quotient approximations for residually finite groups','lemma',
    'Every Cayley graph of a finitely generated residually finite group with a finite symmetric generating set is a local weak limit of finite quotient Cayley graphs, with generator labels preserved. For a prescribed radius R, choose a finite-index normal subgroup containing no nonidentity word of length at most 2R+1; every quotient root then has the exact radius-R labelled ball.',
    ['G is finitely generated and residually finite','S is a finite symmetric generating set','Cayley graph/diagram conventions are matched'],
    'Residual finiteness separates each of the finitely many nonidentity elements in the word ball of radius 2R+1 in a finite quotient. Intersect these kernels. A collision between two radius-R words would give a kernel word of length <=2R, and an extra edge between them would give one of length <=2R+1; both are excluded. Quotient transitivity makes every root exact. Letting R grow proves uniform-rooted local weak convergence. The labels are inherited from the quotient, so this is the labelled sofic special case.')
c148gap=add('C0148','unlabelled-approximants-label-recovery-gap','The finite-quotient case does not resolve unlabelled label recovery','concept',
    'C0148 in the cached Pete notes asks about unlabelled local weak approximations. The residually finite construction supplies labels from actual finite quotients; it does not show that arbitrary unlabelled approximating graphs admit globally compatible generator labels on almost every root. The earlier locally rigid picture has no inspected theorem establishing that compatibility for general groups.',
    ['The general question concerns unlabelled graphs'])

p22subarc=add('P0022','self-similar-jordan-subarc-dimension','Self-similar Jordan arcs can force every subarc to have full dimension','lemma',
    'Let f:[0,1]->K be a homeomorphism onto a Jordan arc. Suppose for every n and 0<=j<4^n the subarc f([j/4^n,(j+1)/4^n]) is a similarity copy of K, and dim_H K=q. Then every nontrivial Jordan arc A contained in K has Hausdorff dimension q.',
    ['f is a homeomorphism onto a Jordan arc','All canonical base-four subarcs are similarity copies of K'],
    'The compact connected nontrivial set f^(-1)(A) is a nondegenerate closed interval [a,b]. Some base-four subdivision interval is contained in [a,b]. Its image is a similarity copy of K and hence has dimension q. It lies in A, while A lies in K; monotonicity of Hausdorff dimension gives q<=dim_H A<=q.')
p22route=add('P0022','polygonal-approximation-does-not-build-thin-internal-arcs','Polygonal approximation does not construct thin arcs inside a trace','concept',
    'A continuous planar path and its one-dimensional polygonal approximations do not by themselves produce a one-dimensional Jordan arc contained in the path image. For the standard Koch arc, the similarity dimension is log(4)/log(3)>1 and every nontrivial internal Jordan arc has that dimension. This deterministic obstruction refutes the generic polygonal-approximation route; it asserts no dimension above one for a Brownian trace.',
    ['The standard Koch arc satisfies the stated self-similar Jordan-arc hypotheses','The usual open-set self-similar dimension theorem is an input'])

def dep(fromkey,tokey,kind,reason):
    source=next(e for e in entries if e['key']==fromkey)
    target=next(e for e in entries if e['key']==tokey)
    relations.append({'from_key':fromkey,'to_key':tokey,'kind':kind,
        'rationale':reason+' FROM: "'+source['statement'][:200]+'" TO: "'+target['statement'][:200]+'"'})
dep(p174profile,p174mom,'depends_on','The profile proof uses the centered diameter moment inequalities.')
dep(p174candidate,p174profile,'depends_on','The candidate uses the strict minimum bound; cached Lemma 3.1 supplies the sufficient criterion.')
dep(p389subset,p389mass,'specializes','The uniform subset law is a specified law with fixed total mass.')
dep(c89map,c89zero,'analogous_to','The zero-intensity boundary check isolates the unresolved positive-intensity input.')
dep(p30bias,p30splice,'semantic_association','The biased selection shows why the Brownian marginal hypothesis at the splice matters.')
dep(c10energy,c10scale,'generalizes','The covariance comparison extends exact constant scaling to bounded varying conductances.')
dep(c148gap,c148finite,'semantic_association','The residual finite result already has labels; general unlabelled recovery remains separate.')
dep(p22route,p22subarc,'depends_on','The self-similar subarc fact supplies the deterministic route obstruction.')

context148=add('C0148','unlabelled-local-weak-approximation-question-context','C0148 local ledger question context','concept',
    'Historical question in Pete, Probability and geometry on groups, Question 14.3, p.200: does unlabelled local weak approximability transfer between Cayley generating sets, and does approximability for all finitely generated Cayley graphs imply soficity? Present status is unverified in the inspected local ledger.',
    ['Historical source question; no current-open certification'])

for pid,entry in list(catalog):
    if entry['key']==context148:
        continue
    packet=json.loads((root/'reports'/f'{pid}_sources.json').read_text(encoding='utf-8'))
    cards=packet['store_cards']
    problem=next((c for c in cards if c['title'].startswith('Open problem:')),None)
    if problem:
        logical=json.loads(problem['metadata_json'])['logical_id']
        quote=problem['body'][:210]
        relations.append({'from_key':entry['key'],'to_existing_logical':logical,'kind':'semantic_association',
            'rationale':'Result touches the cited problem, with independent review pending. FROM: "'+entry['statement'][:210]+'" TO: "'+quote+'"',
            })
    elif pid=='C0148':
        dep(entry['key'],context148,'cites','The named local ledger supplies the exact unlabelled question.')

for pid,key,needle in [
    ('C0068',c68scale,'d > 6 <=> V^{-2/d} << V^{-1/3}'),
    ('C0101',c101round,'the discrete Laplacian of x -> ceil(a x^2 / 2) in one dimension is at most a + 1')]:
    packet=json.loads((root/'reports'/f'{pid}_sources.json').read_text(encoding='utf-8'))
    old=next(c for c in packet['store_cards'] if needle in c['body'])
    statement=next(e for e in entries if e['key']==key)['statement']
    relations.append({'from_key':key,'to_existing_logical':json.loads(old['metadata_json'])['logical_id'],'kind':'refutes',
        'rationale':'Refutes this specific assertion in an author-only attempt, not the open problem. FROM: "'+statement+'" TO: "'+needle+'"'})

packet=json.loads((root/'reports/C0010_sources.json').read_text(encoding='utf-8'))
resolved=next(c for c in packet['store_cards'] if c['title'].startswith('Resolved:'))
relations.append({'from_key':c10status,'to_existing_logical':json.loads(resolved['metadata_json'])['logical_id'],'kind':'cites',
    'rationale':'Source-status warning. FROM: "'+next(e for e in entries if e['key']==c10status)['statement'][:190]+'" TO: "'+resolved['body'][:180]+'"'})

bundle={'spec':'mathbrain-draft-v1','author_agent':'w332','bundle_slug':'probability-open-problems-w332-20261010-001','entries':entries,'relations':relations}
drafts=root/'drafts';drafts.mkdir(exist_ok=True)
text=json.dumps(bundle,indent=2,ensure_ascii=False)+'\n'
part=drafts/'bundle_001.part';part.write_text(text,encoding='utf-8')
part.replace(drafts/'bundle_001.json')
patches=root/'patches';patches.mkdir(exist_ok=True)
patch=''.join(difflib.unified_diff([],text.splitlines(keepends=True),fromfile='a/~/math-brain-inbox/w332/bundle_001.json',tofile='b/~/math-brain-inbox/w332/bundle_001.json'))
(patches/'01_math_nodes.diff').write_text(patch,encoding='utf-8')
old_rows=[json.loads(line) for line in (root/'results.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
seen={row.get('entry_key') for row in old_rows}
latest={row['entry_key']:row for row in old_rows if row.get('entry_key')}
number=max(int(row['row_id'].rsplit('.',1)[1]) for row in old_rows)
with (root/'results.jsonl').open('a',encoding='utf-8') as stream:
    for pid,entry in catalog:
        current_relations=[r for r in relations if r['from_key']==entry['key']]
        if entry['key'] in seen and latest[entry['key']]['statement']==entry['statement'] and latest[entry['key']]['relations']==current_relations:
            continue
        number+=1
        row={'row_id':f'S1.w332.{number:03d}','problem_id':pid,'entry_key':entry['key'],
            'kind':entry['kind'],'epistemic_status':'proof_author_checked' if entry['kind']=='lemma' else 'unverified_concept_or_candidate',
            'statement':entry['statement'],'proof_text':entry['proof_text'],
            'report_path':str(root/'reports'/f'{pid}_attempt.md'),
            'relations':current_relations,
            'audit_status':'pending_w346','lean_status':'not Lean-checked; SETUP_UNVERIFIED'}
        if entry['key'] in latest:
            row['supersedes_row_id']=latest[entry['key']]['row_id']
        stream.write(json.dumps(row,ensure_ascii=False)+'\n');stream.flush()
metrics={'command':'python -X utf8 ~/brain_workers/w332/prepare_bundle.py','problem_ids':sorted({p for p,e in catalog}),
    'entries':len(entries),'relations':len(relations),'lemmas':sum(e['kind']=='lemma' for e in entries),
    'concepts':sum(e['kind']=='concept' for e in entries),'refutes_edges':sum(r['kind']=='refutes' for r in relations),
    'pending_independent_audits':len(entries),'solved_problem_claims':0,'live_store_writes':0}
(root/'bundle_metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
print(json.dumps(metrics,indent=2))
