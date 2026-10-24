# A009 fractional incidence optimization

## exact target, quantifiers, hypotheses and units

This packet certifies one global incidence vector for a complete fixed-posterior forest residual, and derives its convex optimization dual. It supplies continuation/verification evidence for the existing A006/A007 mechanism, not a third broad B02 candidate. Independent acceptance is pending; full FEI remains OPEN.

For every finite nonconstant gate union with nonempty relevant supports R_l and pi_l>0, fix probability laws eta_A on distinct actual finite partition-forest runs. All logarithms in the residual are base two; natural units are used only to formulate the convex program. Put v=sum_{A nonempty} P_f(A), c_l=sum_A P_f(A) Pr_eta_A(l visited), and let d collect every lambda-independent cost and minus the actual-run posterior entropy. Remove gates with c_l=0 if desired: no selected run uses them, so their removal preserves these runs and decreases the normalizer. For the retained gates c_l>0. With D(lambda)=product_l(1+pi_l lambda_l)-1, the exact residual for these fixed laws is

    R(lambda)=d+[v ln D(lambda)-sum_l c_l ln lambda_l]/ln 2.

The requirements are lambda_l>0 and sum_{l:j in R_l}lambda_l<=1 for every physical coordinate. The generator and its weights are fixed across output sets. This does not assert that the posterior selected here is the posterior optimal for every lambda.

For all r,m>=1, take r common fair core coordinates and m private fair coordinates. Let A_r be their core conjunction, B_m the OR of the private positive literals, and f=2 A_r B_m-1. Its m distinct gates are core conjunction AND private_l. A single ordered cover lists all core coordinates first, then that gate's private coordinate; M_l=1. The certificate lambda_l=1/m satisfies every incidence constraint, including common-coordinate sum 1 and private-coordinate sum 1/m. The complete residual of the explicit actual-run laws below satisfies R<=8 I(f), and R plus a paid complete-reference scale prior is <=10 I(f), uniformly in both r and m. This is beyond bounded-read *representations*: maximum read is m. The Boolean functions themselves are already read-once formulas and weighted thresholds; no new Boolean FEI class or novelty is claimed.

## sources actually read, revisions and theorem locators

Execution protocol fei-execution-protocol/2, revision 2026-10-11-execution-v2, was read in full. Board snapshot 2026-10-11 22:26 UTC was read at stage start. The specified claude/B02/STREAM_NOTES.md was absent. Reports README, CURRENT_STATUS, claim/obstruction registries, packet index, stream actions, and the plan were inspected, specifically Endpoint J eq:residual and A009's acceptance contract. Earlier B05/B09/B19 run reports were read for their obstruction/review scopes; none supplies a proof premise.

The proof premise is the complete local source source_material/reductions/paper/forests.tex, read in full: eq:forestpacking, eq:forestconditioning, eq:forestcost, thm:posteriorforest and the actual queue definition. Its child draw probabilities are lambda_l, not uniform-neighbor probabilities. A006's 20261011T210855Z posterior-forest report and A007's 20261011T215236Z root-normalization report were read. The present proof reconstructs their needed algebra and extends their proposed shared-r-core calculation; their pending bounds are not assumed as accepted premises.

The supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were read/inspected. SEED_LEMMAS Section 2 supplies the normalized complete-reference prior. The sources inventory and LOG_ALLOCATION_CURATED/OVERLAPPING_PRODUCT_NOTE were inspected for scope guards. Both threshold text versions and both percolation versions were read for introductions and coding locators; threshold_paper_38pp Section 5.6 supplies the public unconditioned interface, while the percolation hierarchical codec has different spatial hypotheses and is not used. The text encodings require replacement decoding for some extracted bytes. Exact byte SHA256 and intake details are in out/SOURCES.json.

## complete derivation or exact first unsupported line

### Convexity for fixed actual-run laws

Write t_l=ln lambda_l and A_{jl}=1_{j in R_l}. Expansion gives

    D(e^t)=sum_{empty != R subset [N]} exp(sum_{l in R}(t_l+ln pi_l)).

Thus F(t)=v ln D(e^t)-c dot t is convex, being a log-sum-exp minus a linear function. Each g_j(t)=sum_l A_{jl}exp(t_l)-1 is convex. This statement does not require a convex objective in lambda coordinates. Strict feasibility holds by taking all lambda small and positive. Duplicate supports give distinct columns/draw labels and remain subject to the same coordinate rows; they must not be silently combined in a cost calculation. Every nonconstant gate has nonempty relevant support. Constant-false gates are removed; a constant-true gate makes f constant and H=I=0. Uncovered coordinates have the empty incidence sum zero. If a retained gate has c_l>0, its weight cannot be set to zero with finite fixed-posterior cost except in a simultaneous common-scaling limit where the normalizer cancels; see the boundary discussion below.

Here is a dual lower certificate without a solver. Choose a probability law nu on nonempty root sets, with marginals r_l=Pr_nu(l in R), and coordinate prices y_j>=0. Define q_l=sum_j A_{jl}y_j and b_l=c_l-v r_l. Require b_l>=0, and q_l>0 when b_l>0. With H_nat(nu)=-sum nu ln nu, define

    L(nu,y)=v[H_nat(nu)+sum_l r_l ln pi_l]-sum_j y_j
             +sum_{l:b_l>0} b_l[1+ln(q_l/b_l)].

Then inf_feasible F >= L. To prove this, the elementary finite Gibbs identity gives ln D(e^t)>=H_nat(nu)+sum_l r_l(t_l+ln pi_l). Add sum_j y_j g_j(t), which is <=0 on feasible points. Its infimum over unconstrained t separates into inf_t[-b_l t+q_l exp(t)]. For b_l,q_l>0 the value is b_l[1+ln(q_l/b_l)], attained at exp(t)=b_l/q_l. If b_l=0 the infimum is zero (also when q_l=0). If b_l<0 or b_l>0=q_l it is -infinity, hence those choices give no useful certificate. This proves weak duality directly; no unjustified interchange of supremum and infimum is used.

For a feasible positive lambda, take nu_*(R)=product_{l in R}(pi_l lambda_l)/D(lambda). Its marginals are rational for rational lambda and pi:

    r_l=pi_l lambda_l product_{k!=l}(1+pi_k lambda_k)/D.

If nonnegative rational prices satisfy

    c_l-v r_l=lambda_l q_l,
    y_j(sum_l A_{jl}lambda_l-1)=0,

the displayed dual bound equals F(ln lambda) exactly. Gibbs equality, scalar minimizer equality (including b_l=q_l=0), and complementary slackness prove the equality and global optimality. Equivalently the gradient of the convex Lagrangian vanishes, which also proves sufficiency directly. This is the claimed verifiable duality assertion: any such certificate is exact. Only the proved sufficient certificate and weak duality are asserted and used here. No necessity theorem, minimax interchange, or assertion that every instance has a finite optimizer is needed.

In particular the actual family member (r,m)=(1,2) with the fixed posterior below has v=15/16, c_l=17/32, pi_l=1/4, lambda_l=1/2, r_l=9/17. The common coordinate price y=19/272 and private prices zero give

    (15/16)(9/17)-17/32+(1/2)(19/272)=0.

This certifies a global optimum for that actual fixed-posterior instance. Three other heterogeneous examples in WEIGHT_CERTIFICATE.json certify abstract program inputs only; their c values are not asserted to be Boolean-realizable run marginals.

For the symmetric r,m family below c_l=c_total/m. Permuting t preserves feasibility and F; convex averaging therefore shows the infimum can be taken at equal weights, even if it is not attained. Set lambda_l=z/m, 0<z<=1. The scalar derivative with respect to ln z is v E_nu K-c_total, where K is root count. For m>=2 its derivative again is v Var_nu K>0, since both singleton and double root sets have positive mass. Hence there is at most one stationary scale; otherwise the upper boundary is optimal. For m>=2 our laws have c_total>v, so the objective tends to +infinity as z decreases to zero and a finite equal-weight minimizer exists. For m=1, c_total=v and the scale-dependent expression is constant. For general fixed laws, c_total=v can instead produce an unattained boundary infimum: if every output uses exactly one among several eligible gates, scaling all weights down cancels the leading ln scale. Consequently zero weights/boundary limits cannot simply be excluded when claiming the variational infimum.

### Joint posterior/weight optimization is not convex

Take the actual Boolean function f=x_1 represented by two identical dictator gates. There are two actual partition runs for its singleton spectral set, one rooted at each gate, and pi_1=pi_2=1/2. After optimizing the posterior, S_B=(lambda_1+lambda_2)/2 and the natural-unit residual is

    ln[D/S_B]=ln[1+lambda_1 lambda_2/(2(lambda_1+lambda_2))].

Put lambda_1=exp(t+s), lambda_2=exp(t-s). This becomes ln[1+exp(t)/(4 cosh s)]. At t=ln(1/4), s=0 the incidence inequality has strict slack and the second derivative in s is -1/17. Thus the full posterior-optimized objective is not convex in log weights, even for an actual Boolean example. The fixed-law convex program and its dual must not be transferred to that broader objective.

### Full shared-core residual certificate

Put p=2^-r, q=2^-m, b=1-q, gamma=6/5. For core U and private T, every nonempty set has coefficient 2p Bhat(T). Bhat(empty)=b; every nonempty private T has |Bhat(T)|=q. Therefore

    P(U union T)=4p^2 b^2 if T empty and U nonempty,
    P(U union T)=4p^2 q^2 if T nonempty (including U empty),
    v=4pb(1-pb), I_core=2rp b, I_data=2pmq.

These also follow directly from physical pivotal probabilities. Choose the following laws, fixed independently of lambda:

* If U nonempty and T empty: one gate owns U; average uniformly over all m root gates, giving H(eta)=log m.
* If U nonempty and T nonempty, t=|T|: select one of the t private gates as root, assign all U to it along with its private coordinate, and attach the other t-1 private gates through the first selected core coordinate. Average uniformly over the t root choices and (t-1)! ordered child-label sequences. There are exactly t! distinct actual queue runs, so H(eta)=log(t!).
* If U empty: each of the t private coordinates is assigned to its own gate; all t gates are roots. The source components are singleton gates, and the root queue's fixed order gives one actual run, with entropy zero.

Every run visits each used gate once, uses disjoint assigned subsets, and terminates. The root reaches every other used gate when U is nonempty, so the star is a permitted spanning forest with one source component. Ordered child draws are distinct actual random outcomes, not permutations of an abstract written edge list. The selected common attachment has positive probability under the uniform multiset draw. Every prescribed label draw is positive with lambda=1/m.

Let E denote spectral-weighted expectation on nonempty sets and these laws, K the root count, and V the used-gate count. Direct tensor summation gives

    E K-v=4p^2 q(m/2-b),
    E |T|=I_data,
    E V-v=2p q[m-2(1-q)]>0 for m>=2.

For the last identity, E V=core-only mass + E|T|, and core-only mass=4p(1-p)b^2. The difference is zero for m=1 and any r; it is positive for m>=2 because m>=2>2b.

The root rarity is r+1, and D=(1+p/(2m))^m-1. Expansion and exp(a)-1<=a exp(a), a=p/2, give

    log D=-(r+1)+delta, 0<=delta<=(p/2)log e.

Hence normalization plus rarity is exactly v delta+(r+1)(E K-v). Since K-1<=|T| on the empty-core exceptional sets,

    E K-v<=p I_data,
    (r+1)(E K-v)<=I_data,
    v delta <=(log e) I_core.

Here (r+1)2^-r<=1 and v<=4pb. Both Lambda and log Z were retained through log D; neither is silently dropped.

Write G(U)=gamma sum_{j selected in U} log(j/position_U(j)), using ranks j=1..r. Every selected core coordinate contributes this same term, regardless of root. Conditional on selection of rank j, its predecessor count is Bin(j-1,1/2). Direct binomial summation gives E[1/(1+Bin)]=2(1-2^-j)/j. Jensen for the concave log therefore gives expected log(j/(1+Bin))<=1, so the uniform-U average of G is <=gamma r/2. Also sum_T Bhat(T)^2=b (B is an indicator). Consequently

    E G(U)<=4p^2 b 2^r gamma r/2=gamma I_core.

For a private leaf the subset congestion gamma log(|U|+1) cancels its negative private rank term, leaving exactly gamma log(r+1). For the inside root the private rank cost is gamma log((r+1)/(|U|+1)) and congestion is zero. Empty-core roots also cost gamma log(r+1). Thus all private rank/congestion terms together are <=gamma log(r+1) I_data<=gamma I_core: use log(r+1)<=r, m 2^-m<=1/2 and b>=1/2.

Core-only labels cancel against log m actual-root entropy. On every other set, the remaining label cost minus posterior entropy is at most |T| log m; the -log(t!) saving stays nonpositive. Therefore it is <=I_data log m=2p m q log m<=4p<=4 I_core. For the middle bound log m<=m and m^2/2^m<=2 suffice: verify m=1,2,3 and use the ratio ((m+1)/m)^2/2<1 for m>=3. I_core>=rp>=p.

The complete residual, including all subset congestion, M=1 order costs, ranks, root labels, rarity and actual-run entropy, thus obeys

    R <= (4+2gamma+log e) I_core+I_data < 8 I(f).

The strict numerical comparison requires no floating point: ln 2>5/8 follows already from the first term 2/3 of its positive atanh series; hence log e<8/5 and 4+12/5+log e<8. For m=1 the same bound is valid without any multiple-root or label charge.

For a paid scale prior choose lambda_l^(j)=2^-j/m and w_j=1/[(j+1)(j+2)] for j>=0. These weights telescope to one; each whole conditioned generator is a subprobability. Selecting j=0 pays exactly v bits because w_0=1/2, and v<=2I_core/r<=2I. The complete residual plus this explicit prior is <=10I. This is an upper certificate at a feasible global vector, not a claim that uniform weights are optimal in every r,m case.

### New lead direction: geometric sunflower weights and the affine-plane obstruction

The B02 notes appeared at 2026-10-11 22:45 UTC, after this stage began, and were read in full before final persistence. They identify PI-J (prime-implicant whole-set coding) as the stream target and direct A009 to the outer fractional expression eq:outerfractional. The following is a source-bound test of that existing mechanism, not a new broad candidate. A008's finished dictionary report was also read: its sunflower quotient uses a different generator, so its bound neither replaces nor contradicts this residual.

For the r=1 sunflower, assign a common-coordinate pivotal input to the first positive private literal. Then alpha_0=b=1-2^-m, q_{0,l}=2^-l/b for l=1..m; a private-coordinate derivative has alpha_l=2^-m and only gate l eligible, so q_{l,l}=1. Choose the global rational weights lambda_l=2^-l. The common incidence sum is 1-2^-m<1, and each private row is 2^-l<=1. Put a=11/48. The outer sum satisfies

    S_0=b^(-1/2) sum_{l=1}^m 2^(-13l/48)
        <=sqrt(2)/(2^(13/48)-1)<9,
    log S_l=(11/48)l.

The last strict bound is elementary: 13/48>1/4, (7/6)^4<2, and sqrt(2)<3/2. Thus the pressure P=(48/5)sum_j alpha_j log S_j is at most (192/5)b+(11/5)2^-m m(m+1)/2 <41 I, using m(m+1)2^-m<=3/2 and I>=1. The latter bound follows from m=1,2,3 and the recurrence ratio (m+2)/(2m)<=1 for m>=2. This removes the uniform-weight (11/48)log m contribution inside every log S_j. The source's C_0<41 and v log Z<=0 yield a coarse H<82I, already known for this Boolean class; the new directional fact is the bounded fractional pressure with one explicit global vector and a specified tie rule. No entropy H is an input to the weights.

For each prime power Q>=16, let the coordinates be the Q^2 points of the affine plane over F_Q. Define f_Q=1 iff some affine line has all its Q point bits positive; otherwise f_Q=-1. There are N=Q(Q+1) genuine conjunction gates and k=Q+1 gates incident to each point. All are prime implicants: if a positive pattern contains a line, its minimal positive subset is that entire line; a set of fewer than Q points cannot contain any line. Conversely every line is minimal positive. All gate supports are nonempty and distinct, each cover has M_l=1, and each pi_l=2^-Q.

Fix a point j and a line l through it. Conditional on all Q-1 other points of l being positive, an alternative incident line is ready with probability 2^(-(Q-1)), since its other points are disjoint from l. A nonincident line has at most one forced positive point, so its probability of being fully positive at the j-negative endpoint is at most the same quantity. A union bound over N-1 other lines gives probability at least 1-epsilon_Q that no such alternative occurs, where

    epsilon_Q=Q(Q+1)2^(-(Q-1))<1/2 for every integer Q>=16.

These clean events for different lines through j are disjoint and make j pivotal. Therefore

    alpha_j >= k 2^(-(Q-1))(1-epsilon_Q)>0.

For ANY fixed disjoint pointwise tie decomposition of this derivative among pivotal line gates, each piece's squared norm is at most 2^(-(Q-1)). Hence its normalized mass obeys q_{j,l}<=1/[k(1-epsilon_Q)]<=2/k. These are precisely the disjoint signed pieces with masses summing to one required by the source outerfractional formula.

Every feasible global lambda has sum_{l incident j}lambda_l<=1. With a=11/48 and beta=1/[2(1+a)]=24/59, Holder gives the local relaxation bound

    S_j=sum_l sqrt(q_{j,l})lambda_l^-a
        >=(sum_l q_{j,l}^beta)^(1+a)
        >=(k/2)^(35/48).

The first inequality follows by applying Holder to q_l^beta=(sqrt(q_l)lambda_l^-a)^(1/(1+a)) lambda_l^(a/(1+a)). The second uses sum q=1 and q_l<=2/k, so sum q_l^beta>= (2/k)^(beta-1). This uses only the coordinate row, and thus holds for ALL simultaneous global incidence vectors; zeros with positive piece mass give infinite S_j rather than evade the bound. Consequently

    (48/5)sum_j alpha_j log S_j >= 7 I(f_Q) log((Q+1)/2).

Uniform lambda_l=1/k is feasible. Since sum sqrt(q_{j,l})<=sqrt k, it also gives pressure <=7I log k. Thus the optimized positive pressure grows logarithmically, between these two explicit bounds. No global weight choice repairs it. In addition v log Z cannot cancel that divergence: D=product_l(1+pi_l lambda_l)-1, log Z alone may diverge if weights shrink, but the positive pressure then rises; for the statement here only the nonnegative pressure requested by the lead is being bounded below. No claim about the infimum of the FULL expression with v log Z is inferred from this pressure lower bound. Its exact remaining cancellation is an additional question if one attempts to use this outer theorem rather than the whole-set forest mechanism.

This resolves the lead's requested O(I) pressure test negatively for the affine-plane DNF. The obstruction is the almost uniform distribution of genuinely pivotal line witnesses at each point, producing at least (35/48)log((Q+1)/2) in log S_j even after a local fractional relaxation. It does not disprove FEI, PI-J, or the posterior forest cost bound: all retain whole-set label sharing absent from this coordinatewise coarsening. Analytic finite-geometry incidence and a union bound establish the all-Q obstruction; no exponentially large truth-table computation is claimed.

### Exact remaining bridge

The full expectation is paid for this representation family. No claim that every Boolean function has such a representation is made. For arbitrary overlapping base gates in a shared core activation, the root component still cancels, but the base label/rank/congestion expectation need not have the binomial/private-singleton law used above. That is the first unsupported line for a universal whole-set cost theorem. The optimization dual pays no such missing structural expectation by itself.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was written before execution. Domain r,m=1..5, 25 actual Boolean functions, maximum n=10; no automatic increase and no symmetry omissions. Integer FWHT and Fraction verify every coefficient, Parseval, influences, root excess and label-count derivatives. Rational atanh-series intervals certify the complete residual upper endpoint below 8I and the paid-prior endpoint below 10I in all 25 cases. The logarithm error is bounded by 2 z^(2L+1)/[(2L+1)(1-z^2)] after L=60 terms and dyadic range reduction; division takes all four endpoint combinations, including negative numerators.

Command: `python -X utf8 runs/20261011T223308Z-account05-A009-fractional-incidence-optimization/code/check.py`. Initial execution passed 4,083 assertions in 1.97 seconds. Before the second execution the frozen spec was extended to add the actual (1,2) KKT and duplicate-dictator Hessian checks without changing the family domain. Final output and observed assertion count are in out/CHECK.json. Abstract KKT witnesses check stationarity and root-law normalization exactly, with realizability explicitly excluded. Memory estimate 30 MB; no heavy job, GPU, background process or memory-gate exemption was used. Analytic arguments, not finite checks, supply the all-r,m bound. Independent reconstruction of the new derivation has not occurred.

The lead-directed analytic checks were frozen separately in LEAD_FROZEN_SPEC.json before execution: m=1..12 sunflower geometric-mass identities (algebra only), and Q=16,32,64,128,256 affine-plane incidence/union-bound constants (algebra only; no high-dimensional Boolean enumeration). Command: `python -X utf8 runs/20261011T223308Z-account05-A009-fractional-incidence-optimization/code/lead_check.py`. It passed 87 exact rational assertions in under 0.002 seconds. Together the two checkers passed 4,173 assertions. The all-Q geometric proof and Holder lower bound are analytic; these finite checks only certify the stated rational constants and exponents.

## proof dependencies and changed downstream conclusions

Source-complete conditioned forest theorem and eq:outerfractional, elementary finite Gibbs identity, binomial identity, Jensen, Holder, affine-plane incidence, and the supplement's complete-reference prior are the premises. The outer theorem's use here is a scoped test of its already derived pressure expression; the lower bound does not assume its FEI conclusion. Effective-piece rank bounds are not used, so no disjoint-physical-piece or fiber-antichain hypothesis is being assumed. No unreviewed B09 theorem or solver output is used. A006/A007's proposed shared-r-core singleton continuation now has an explicit whole residual ledger with bounded ratio; the fixed-law weight optimization has exact rational price certificates. A010 must distinguish the nonconvex posterior-optimized problem from the convex fixed-law subproblem.

B02 already had two pending broad candidates at stage start. This run is continuation/verification evidence and is queued as provisional evidence for their review, with CLAIMS.json empty rather than opening a third registry candidate. This does not amount to adoption or independent acceptance of this new extension.

## one next mathematical action and independent reviewer

Next: A086/A094 reconstruct the exact dual and residual continuation, then reconstruct the affine-plane local mass lower bound. Following the newly available lead, test the actual prime-implicant whole-set forest on the affine-plane DNF to see whether posterior sharing removes its proven coordinatewise logarithmic pressure. Do not repeat the singleton family or try another coordinatewise weight solver on the same affine-plane pressure.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, INCIDENCE_OPTIMIZATION.tex, WEIGHT_CERTIFICATE.json, frozen spec, code and exact output are saved locally. out/RECEIPTS.json records sizes and SHA256, excluding itself. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. All writes are inside A009. Supervisor copying, mirrors and independent review remain pending and are not claimed complete.

## Universal bridge

C020 whole-set witness cost / G-J-COST advances from common-core root cancellation to a full R<=8I certificate for every shared-r-core singleton-petal representation, with a paid prior costing at most another 2I. The fixed-law dual is exact; the fully posterior-optimized objective remains nonconvex. In the lead's PI-J direction, geometric weights remove sunflower fractional pressure, while the affine-plane prime-implicant DNF has optimized coordinatewise positive pressure at least 7I log((Q+1)/2). The remaining universal obligation is a whole-set actual-run law whose base labels/ranks/congestion expectation is influence-paid. The shortest next route is its posterior forest on the affine-plane family, where the weight-only coarsening has now failed uniformly over every feasible vector; this tests whole-set sharing on a family with growing genuine overlap rather than adding another calibrated read-once FEI result.
