"""Stage author proofs, quoted edges and per-item receipts without ingesting."""
import difflib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDS = ['P0208','P0458','C0129','P0087','P0294','C0020','C0074','C0116','P0007','P0034']

SPECS = {
 'P0208': ('probability.markov-chains', [
  ('q-fold-cycle-hitting-times-and-relaxation','lemma','Exact walk parameters of q-fold cycles',
   'For m>=5 and q>=2, the arc-transitive graph C_m[empty_q] has mq vertices and degree 2q. Its mean hitting time from a target twin is mq, and from fiber j!=0 is j(m-j)+m(q-1). Its maximal commute time is 2 floor(m^2/4)+2m(q-1), its stationary mean hitting time is (m^2-1)/6+m(q-1), and its rate-one continuous-time relaxation time is 1/(1-cos(2*pi/m)). For fixed q their maximal-commute to twice stationary-hitting ratio tends to 3/2.'),
  ('q-fold-cycle-commute-and-relaxation-conventions','concept','Conventions for the q-fold cycle calculation',
   'In the q-fold cycle calculation, tau_star denotes the maximum of E_x T_y+E_y T_x; it is twice the maximum one-way hitting time because the hitting times are symmetric. Tau_2 denotes the relaxation time of the rate-one continuous-time generator P-I. For even m the discrete-time absolute spectral gap is zero and is a different quantity.')]),
 'P0458': ('probability.distributions', [
  ('standard-normal-positive-part-transform-density','lemma','Distribution of the normal positive-part transform',
   'Let Z be standard normal, g(z)=phi(z)+z Phi(z), a=1/sqrt(pi), and v=1/3+(sqrt(3)-2)/(2*pi). Then E[g(Z)]=a and Var(g(Z))=v. W=(a-g(Z))/sqrt(v) has support (-infinity,a/sqrt(v)] and no atom at its finite endpoint. For w<a/sqrt(v), with z=g^{-1}(a-sqrt(v)w), its CDF is 1-Phi(z) and its density is sqrt(v)*phi(z)/Phi(z). This non-Gaussian law is the standardized-degree limit only conditional on the earlier degree/moment convergence being established in a stated regime.')]),
 'C0129': ('probability.randomenvironment', [
  ('finite-cookie-prefix-failure-mean-and-variance','lemma','Exact failure moments beyond the cookie prefix',
   'For independent Bernoulli trials with probabilities p_1,...,p_M followed by fair trials, let F_m count failures before the m-th success. For m>=M and m>=1, s=sum p_i, t=sum p_i(1-p_i), and delta=sum(2p_i-1), E F_m=m-delta and Var F_m=2(m-s)+4t. This is a quenched single-stack identity; it assumes no independence between stacks. It does not settle the stationary-ergodic excited-walk recurrence criterion.'),
  ('cookie-branching-log-mean-route-warning','concept','Critical offspring warning for the cookie branching route',
   'With a finite cookie prefix and a fair tail, the large-population expectation of F_(k+1) is k+1-delta once k+1>=M. Its linear coefficient is one at every site. A nontrivial Lyapunov exponent of site-dependent offspring means is therefore not obtained by this calculation; migration and small-population behavior remain relevant. The general stationary-ergodic criterion and the prior periodic-case assertion are not proved by this local identity.')]),
 'P0087': ('probability.reinforcement', [
  ('forced-network-urn-stationary-beta-law-quadratic-forcing','lemma','Stationary beta law for quadratically forced network urns',
   'Fix a finite irreducible row-stochastic Q with stationary probability pi, p in [0,1]^d, c>0, f=cr^2 and 0<r with r+f<=1. Given Z, let X_i be conditionally independent Bernoulli((QZ)_i), and update Z prime=(1-r-f)Z+rX+fp. Put pbar=pi.p and K=sum pi_i^2. For 0<pbar<1, as r->0 the unique joint stationary law converges weakly to Y times the all-ones vector, where Y has Beta(2c*pbar/K,2c*(1-pbar)/K) law. At pbar=0 or 1 the stationary law is the corresponding point mass. This concerns stationary laws only; a functional diffusion limit and initial-layer analysis are not asserted.'),
  ('forced-network-urn-stationary-covariance-quadratic-forcing','lemma','Stationary covariance under quadratic urn forcing',
   'Fix a finite irreducible row-stochastic Q with stationary probability pi, p in [0,1]^d, c>0, f=cr^2 and 0<r with r+f<=1. Given Z, let X_i be conditionally independent Bernoulli((QZ)_i), and update Z prime=(1-r-f)Z+rX+fp. The stationary law is unique, has mean f*((r+f)I-rQ)^(-1)p, and Cov(Z) tends as r->0 to K*pbar*(1-pbar)/(2c+K) times the all-ones matrix, where pbar=pi.p and K=sum pi_i^2. For Q=(1), its exact variance is p(1-p)/(1+2c-c^2*r^2). This is a stationary moment result, not a functional diffusion convergence theorem.'),
  ('scalar-forced-urn-wright-fisher-generator-limit','lemma','Scalar forced-urn generator convergence',
   'For the scalar update Z prime=Z+r(X-Z)+cr^2(p-Z), X given Z=z being Bernoulli(z), c>0 and r+cr^2<=1, the one-step generator divided by r^2 converges uniformly on each h in C^3([0,1]) to c(p-z)h prime(z)+(1/2)z(1-z)h double-prime(z). The Taylor remainder divided by r^2 is at most ||h triple-prime|| infinity*r*(1+cr)^3/6 plus ||h double-prime|| infinity*c^2*r^2/2. This identifies a candidate Wright-Fisher generator without proving path convergence.')]),
 'P0294': ('probability.queueing', [
  ('random-routing-workload-exact-zero-finite-population-bias','lemma','Zero finite-N bias for random-routing workloads',
   'For N unit-speed servers with Poisson input N*lambda, independent uniformly chosen destinations, and independent nonnegative job sizes S with rho=lambda*E S<1 and E S^2 finite, the product stationary workload law consists of N independent M/G/1 workloads. The stationary mean workload per server is exactly lambda*E S^2/(2*(1-rho)) for every N. Its first-order 1/N bias and remainder are zero, and off-diagonal covariances are zero. This is the d=1 random-routing case; no zero-bias claim is made for workload-dependent least-of-d routing.')]),
 'C0020': ('probability.boolean-functions', [
  ('query-cost-does-not-bound-revealment-uniformly','lemma','Expected query cost does not bound each revealment by its average',
   'For exact algorithms on N bits, expected distinct query cost equals the sum of coordinate revealments, but no universal K bounds every revealment by K times cost/N. Fixed-order OR on fair bits has first revealment 1 and cost 2*(1-2^(-N)). Also any exact algorithm of cost o(N) can be padded by querying a fixed bit first, retaining cost at most the original cost plus one and revealment 1 at that bit. Thus a sublinear crossing query budget alone does not justify a uniform average-revealment premise.')]),
 'C0074': ('probability.scaling-limits', [
  ('tree-volume-and-resistance-orders-do-not-imply-walk-convergence','lemma','Uniform resistance orders do not imply a walk scaling limit',
   'On paths 0,...,n, put conductance c_n=1 for odd n and 2 for even n, normalized counting measure, and spatial scale 1/n. Graph metric-measure spaces converge and resistance is between half and all of graph distance. The stationary variable-speed walks accelerated by n^2 have no common limit of finite-dimensional laws: their cosine two-time covariance tends for t>0 to (1/2)exp(-pi^2*t) along odd n and (1/2)exp(-2*pi^2*t) along even n. This weighted-path example diagnoses the need for actual scaled resistance convergence; it is not a counterexample to an IIC scaling limit.')]),
 'C0116': ('probability.markov-chains', [
  ('visited-subset-exact-cover-time-recursion','lemma','Exact rational cover times by visited-subset recursion',
   'For a finite irreducible rational n-state transition matrix P, set V_full=0. For each nonempty proper visited set S, solve (I-P_SS)V_S=1+(sum_(v outside S)P_uv V_(S union {v})(v))_(u in S), in descending size of S. The killed matrix has spectral radius less than one. V_{ {u} }(u) is the exact cover time from u, and their maximum is the worst-start cover time. The method uses O(2^n*n^3) rational arithmetic operations and does not give a polynomial-time approximation algorithm.')]),
 'P0007': ('geometry.billiards', [
  ('unbounded-open-convex-domain-contains-ray-from-every-point','lemma','Convex vacant components have an escaping straight ray',
   'Every unbounded open convex set in finite-dimensional Euclidean space contains an infinite straight ray starting at each of its points. If such a set is a mirror-complement component, that ray never collides with a mirror and is an escaping launch direction. The assertion needs convexity and does not settle the general all-reflected-rays trapping problem.'),
  ('parabolic-open-corridor-contains-no-infinite-ray','lemma','An unbounded connected open corridor with no straight ray',
   'The planar set C={(x,y): x>0 and |y-x^2|<1} is open, connected and unbounded, but contains no straight ray with nonzero direction. A ray with negative x direction exits x>0, a vertical ray exits the bounded vertical strip at its fixed x, and a ray with positive x direction has y-x^2 tending to minus infinity quadratically. This is a geometric counterexample to an unbounded-component implies straight-visibility inference; no permitted mirror configuration or reflected-ray trapping is asserted.')]),
 'P0034': ('probability.self-interacting-walks', [
  ('horizontal-new-vertical-old-walk-both-clocks-diverge','lemma','Both clocks diverge in the horizontal-new vertical-old walk',
   'For the planar walk that chooses a fair horizontal step on a first visit and a fair vertical step on a repeat visit, its horizontal and vertical departure counts H_n and V_n both tend to infinity almost surely. The coordinates admit X_n=S^H_(H_n), Y_n=S^V_(V_n), where S^H and S^V are independent simple symmetric walks, and each clock visits every nonnegative integer. Consequently each coordinate is unbounded in both signs and hits zero infinitely often. The clocks depend jointly on the visited set; independence of the time-changed coordinates and infinitely many visits to a single planar site are not asserted.')])
}

def begin(pid):
    (ROOT/'STATUS.md').write_text(f'STATE: WORKING\nNEXT: Check and save {pid}; its independent audit remains pending.\n\n2026-10-10: Sequential checks of the assigned ten problems; all mathematical drafts require w346 KEEP.\n', encoding='utf-8')

def save(pid, metrics, record=True):
    (ROOT/'measurements').mkdir(exist_ok=True)
    (ROOT/'measurements'/f'{pid}.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
    namespace, specs = SPECS[pid]
    proof = (ROOT/'proofs'/f'{pid}.md').read_text(encoding='utf-8')
    entries = []
    for logical, kind, title, statement in specs:
        if pid=='P0087':
            statement=statement.replace('Given Z, let', 'For Z in the state space [0,1]^d, let')
        entries.append(dict(key=logical, namespace=namespace, logical_name=logical,
          kind=kind, title=title, statement=statement,
          proof_text=proof if kind=='lemma' else None,
          assumptions=['All hypotheses and scope restrictions in the statement apply.'],
          domain='probability theory' if namespace.startswith('probability') else 'Euclidean geometry and billiards',
          source=dict(source_id=f'owner:campaign:w336:{pid}:{logical}',
                      url=str(ROOT/'proofs'/f'{pid}.md'), revision='author-proof-2026-10-10; independent audit w346 pending',
                      license='owner-own-work; campaign proof, no novelty claim',
                      excerpt=statement[:110])))
    cards=json.loads((ROOT/'store_cards.json').read_text(encoding='utf-8'))
    problem_cards=json.loads((ROOT/'problem_cards.json').read_text(encoding='utf-8'))
    relations=[]
    for e in entries:
        for card,kind in [(problem_cards[pid][0],'cites'),(cards[pid][0], 'generalizes' if pid=='P0208' else 'cites')]:
            logical_id=json.loads(card['metadata_json'])['logical_id']
            body=card['body']
            if 'Result: ' in body:
                old_quote=body.split('Result: ',1)[1][:240]
                if pid=='C0129' and 'whose survival criterion' in body:
                    old_quote=body[body.index('whose survival criterion'):][:240]
                elif pid=='P0458' and 'g(z)=' in body:
                    at=body.index('g(z)=')
                    old_quote=body[max(0,at-60):at+180]
            elif '). ' in body:
                old_quote=body.split('). ',1)[1].split(' Source:',1)[0][:240]
            else:
                old_quote=body[:240]
            relations.append(dict(from_key=e['key'],to_existing_logical=logical_id,kind=kind,
                rationale=f'New: "{e["statement"][:180]}"; existing: "{old_quote}". The new result addresses the stated problem or continues the recorded route within its explicit scope.'))
    if pid=='P0208':
        relations.append(dict(from_key=entries[0]['key'],to_key=entries[1]['key'],kind='depends_on',
            rationale=f'New: "{entries[0]["statement"][:150]}"; convention: "{entries[1]["statement"][:150]}". The displayed parameters use these definitions.'))
    bundle=dict(spec='mathbrain-draft-v1',author_agent='w336',bundle_slug=f'w336-{pid.lower()}-checked-attempt-20261010',
                audit_status='PENDING_W346_KEEP; do not promote to audited or solved',entries=entries,relations=relations)
    (ROOT/'bundles').mkdir(exist_ok=True)
    filename=f'bundle_{IDS.index(pid)+1:03d}.json'
    local=ROOT/'bundles'/filename
    data=json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
    local.write_text(data,encoding='utf-8')
    # Explicit task destination; this is a new draft, not a live-store edit.
    inbox=Path('~/math-brain-inbox/w336')
    inbox.mkdir(exist_ok=True)
    part=inbox/(filename+'.part')
    final=inbox/filename
    if final.exists():
        previous=json.loads(final.read_text(encoding='utf-8'))
        if previous.get('author_agent')!='w336' or previous.get('bundle_slug')!=bundle['bundle_slug']:
            raise RuntimeError('Refuse to overwrite a draft not owned by this result: '+str(final))
    part.write_text(data,encoding='utf-8')
    part.replace(final)
    (ROOT/'patches').mkdir(exist_ok=True)
    patch=''.join(difflib.unified_diff([],data.splitlines(keepends=True),
        fromfile=f'a/~/math-brain-inbox/w336/{filename}',
        tofile=f'b/~/math-brain-inbox/w336/{filename}'))
    (ROOT/'patches'/f'{IDS.index(pid)+1:02d}_{pid.lower()}.diff').write_text(patch,encoding='utf-8')
    row=dict(row_id=f'w336.{pid}.result',problem_id=pid,kind='checked-proof-bundle',label='proof',
             proof_path=f'proofs/{pid}.md',measurement_path=f'measurements/{pid}.json',bundle_path=str(final),
             entries=len(entries),relations=len(relations),checks=metrics,audit_status='pending-w346')
    if record:
        with (ROOT/'results.jsonl').open('a',encoding='utf-8') as handle:
            handle.write(json.dumps(row,ensure_ascii=False)+'\n')
        with (ROOT/'progress_rows.jsonl').open('a',encoding='utf-8') as handle:
            handle.write(json.dumps(dict(agent='w336',row=row['row_id'],event=f'{pid}: {len(entries)} proof/concept drafts, {len(relations)} quoted edges; independent audit pending',evidence=str(local)))+'\n')
    next_pid=IDS[IDS.index(pid)+1] if pid!=IDS[-1] else 'validate all bundles and prepare w346 handoff'
    (ROOT/'STATUS.md').write_text(f'STATE: WORKING\nNEXT: {next_pid}.\n\n2026-10-10: Saved {pid} proof, measurement and draft bundle; independent audit pending.\n',encoding='utf-8')
    print(json.dumps(dict(problem=pid,entries=len(entries),relations=len(relations),metrics=metrics)),flush=True)
    return bundle
