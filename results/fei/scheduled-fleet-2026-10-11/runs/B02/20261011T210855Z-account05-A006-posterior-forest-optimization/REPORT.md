# A006 posterior forest optimization

## exact target, quantifiers, hypotheses and units

All entropies and logarithms below are in bits except the rank discrepancies F, which use natural logarithms. The universal target G-J-COST remains open. This run solves the finite posterior optimization for one explicit unbounded-read representation, and supplies certified computable bounds for other finite collections.

For every integer m>=1, take uniform signs x0,...,xm and let

    f_m = 2*1[x0=1]*1[there is an i>=1 with xi=1]-1.

Represent f_m as the union of the m gates h_i=(x0 AND xi). These are distinct actual functions on supports R_i={0,i}, not repeated descriptions. Order each support as (0,i), set M_i=1, pi_i=1/4, lambda_i=1/m, and gamma=6/5. This is one fixed generator for each fixed function, independent of the sampled Fourier set. The incidence sum is 1 at coordinate 0 and 1/m at every private coordinate.

Write a=2^(-6/5), D=(1+1/(4m))^m-1, Lambda=m log(1+1/(4m)), and Z=1-2^(-Lambda). Thus Lambda+log Z=log D, without dropping either normalization term.

The optimized residual over **all distinct actual partition-forest runs** in this representation obeys

    R_m <= (43/10) I(f_m).

An explicitly paid prior over admissible scaled complete references gives residual plus scale-selection charge <=(53/10) I(f_m). Independently, the exact conditioned run-cost optimum has spectral expectation <=(23/2) I(f_m), or <=(25/2) I(f_m) including that same prior charge. All are upper bounds for a particular representation, not assertions about the optimal universal representation.

This family is already a read-once Boolean formula and a weighted threshold (weight m on x0, weight 1 on each xi). Its FEI status was therefore already covered by baseline results. The contribution is the **complete posterior cost and deterministic-witness obstruction for its given DNF with read number m**, not a new Boolean FEI class or a novelty claim.

## sources actually read, revisions and theorem locators

The execution protocol was read in full: fei-execution-protocol/2, revision 2026-10-11-execution-v2. The board snapshot is 2026-10-11 21:04 UTC. B02/STREAM_NOTES.md was absent when checked; no direction was inferred from that absence. A006 had no previous run output. No B02 prior run exists in the provided reports tree.

The reports README, CURRENT_STATUS, claim/obstruction registries, packet index and stream next actions were inspected. The research plan's Endpoint J, equations forest/residual, and A006 acceptance contract fix the target. The actual complete proof source is source_material/reductions/paper/forests.tex, Section `sec:forests`, definitions `eq:forestpacking`, `eq:forestconditioning`, `eq:forestcost`, and theorem `thm:posteriorforest`. Its generator uses probability lambda_child for each child gate, with remaining mass failure. This differs from the uniform-neighbor generator in the public threshold paper; the difference is retained here.

The supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, NATIVE_MAPPING, and SEED_LEMMAS were consulted; SEED_LEMMAS Section 2 supplies the normalized mixture interface, with every selected complete law and scale charge retained. The baseline current-threshold-paper.tex Sections 5.2, 5.6 and Proposition `prop:joint-witness`, and its exact forest checker were read. Context threshold_paper_38pp.txt Section 5.6 is the corresponding public interface; the percolation paper Section 2 gives a different hierarchical set codec and is not used as a proof premise. Earlier paper versions were inspected for context, not imported as dependencies. Source scopes and SHA256 pins are saved in out/SOURCES.json. No external theorem beyond these source-complete coding interfaces and elementary finite entropy identities is required.

## complete derivation or exact first unsupported line

### 1. Optimization and computable truncation certificates

For a finite set Omega of actual runs and any finite cost b(r), put S=sum_{r in Omega} 2^(-b(r)). If S>0, then

    inf_p [sum_r p(r)b(r)-H(p)] = -log S,
    p_*(r)=2^(-b(r))/S.

Indeed, the expression equals -log S + KL(p || p_*). Infinite-cost/zero-weight runs must have p=0 at any finite optimum; if all weights vanish the value is +infinity. Unsuccessful or infinite queue paths are not in Omega. The actual partition-forest set is finite. For a countable successful-run collection and b=-log q, increasing finite collections converges to -log sum q whenever this sum is positive; finite-support posteriors suffice to establish the infimum even if the full conditional entropy is infinite.

This identity is baseline bookkeeping. Its computational use is as follows. For a deduplicated enumerated subcollection E, S_E gives an upper bound -log S_E on the full infimum. If every omitted run has cost >=b0 and their number is <=N, then

    -log(S_E+N*2^(-b0)) <= full infimum <= -log S_E.

More generally an upper bound U on the omitted weight replaces N*2^(-b0). Interval bounds on S_E and U yield rigorous logarithm intervals with their directions preserved. In the forest residual b=B; for the exact complete run cost b=-log q, S is actual conditioned output mass of the selected runs. These are different optimizers: p_B need not equal the true posterior p_q.

If a description map d->r has multiplicities n_r, summing descriptions would wrongly insert n_r in S. Either canonicalize to the actual queue key (initial root set, chronological visited-gate/subset/ordered-child trace), or use H(description)-H(description|run)=H(run). The correction follows directly from the entropy chain rule since run is a function of description. Child-label draws in different occurrence slots at the same attachment variable really are different random events; permutations of the written edge list which leave those draws unchanged are not.

For rational incidence weights and gamma=6/5, each 2^(-B) is algebraic: rank and congestion factors are rational quantities raised to rational powers. Rational bisection for fifth roots, products and finite sums gives explicit rational intervals for S; logarithms can then be bounded by a convergent rational series. No assertion of efficient enumeration in arbitrary dimension is made.

### 2. Exact Boolean law and influence

Let b=prod_{i=1}^m (1-xi)/2. Then

    f_m=x0-(1+x0)b.

Consequently P(empty)=4^(-m), P({0})=(1-2^(-m))^2, and P(T)=P({0} union T)=4^(-m) for every nonempty private T. Parseval gives v=1-4^(-m). Direct pivotal probabilities are I_0=1-2^(-m) and I_i=2^(-m) for private i. Hence

    I(f_m)=1+(m-1)2^(-m) >=1.

### 3. Exhaustion of actual partition forests

For A={0}, exactly m runs exist: choose root r, subset {0}, and zero children. Each has B=log m+2. They differ in the activated gate, so posterior H=log m is justified.

For A=T nonempty private, every coordinate is forced to its own gate, no incidence edges exist, all t=|T| gates are roots, and there is exactly one run. Its cost is

    B_private=t(log m+16/5).

Here F_i^i=ln 2 since the common predecessor is absent.

For A={0} union T, assignment of coordinate 0 determines a unique source gate. All other used gates own only their private variable, and have no outgoing edge. Thus the forest is forced to be a star. There are two possibilities:

* Inside root: r in T owns {0,r}, other gates own their private singleton. There are t choices of r and (t-1)! distinct ordered child-label sequences, for t! runs. Every such run has B_in=t log m+2+(6/5)(t-1).
* Outside root: r outside T owns {0}, with t private leaves. There are m-t root choices and t! ordered child-label sequences, for (m-t)t! runs. Each has B_out=(t+1)log m+2+(6/5)t.

In both cases every child attaches at coordinate 0. The chronological child draws are part of the run; selected subsets are disjoint and every used gate is visited once. This exhausts all assignments, root choices, parents, attachments and permitted child orders, with no duplicated descriptions.

The complete residual partition weights are therefore

    S_B({0})=1/4,
    S_B(T)=m^(-t)*(a/4)^t,
    S_B({0} union T)= t! * a^(t-1)/(4*m^t) * [1+(1-t/m)*a].

Together with p_B(r) proportional to 2^(-B(r)), these determine the exact finite optimizer for every spectral set. In the last display, individual runs inside each root type have equal weight, but the two root types have different weights.

### 4. Dimension-independent residual payment

Using the preceding exact optima,

    R_m = v log D + 2(1-2^(-m))^2
      + 4^(-m) sum_{t=1}^m binom(m,t) *
        [2t log m +(22/5)t +4/5 -log(t!)
         -log(1+(1-t/m)*a)].

The root normalizer is well controlled in both directions:

    1/4 <= D < e^(1/4)-1 < 1/3.

The lower bound is the linear binomial term; (1+u)^m<=e^(mu) proves the middle bound. Since exp(x)<1/(1-x) for 0<x<1 by termwise comparison of its series with the geometric series, exp(1/4)<4/3. In particular log D<0, but the exact formula retains it before this bound.

Drop the two nonpositive posterior terms only for the upper estimate. The identities sum binom(m,t)t=m2^(m-1) and log m<=m give the rare-set contribution at most

    2^(-m) [m log m +(11/5)m +(4/5)(1-2^(-m))]
    <= 2^(-m) [m^2 +(11/5)m +4/5] <=23/10.

For the last inequality the values at m=1,2 are 2 and 23/10. If P(m)=m^2+(11/5)m+4/5, then 2P(m)-P(m+1)=m^2+(1/5)m-12/5>=0 for m>=2; induction proves the bound for all integers. The dominant term is <=2. Thus R_m<=43/10<= (43/10)I(f_m).

Posterior credit is indispensable for this representation. For point-mass posteriors, every singleton-common witness costs log m+2; every other B is nonnegative. Since log D>=-2,

    R_deterministic >= (1-2^(-m))^2*(log m+2)-2v.

The right side diverges while I(f_m)->1. This is an all-m obstruction to deterministic forest residual payment in this fixed DNF, **not** an obstruction to other representations or to FEI.

### 5. Exact complete run costs, beyond the residual bound

The actual subset sampler has weights theta_1(0)=1, theta_1(i)=a and theta_2=1. With nonempty roots conditioned, a prescribed root set of size k has mass (1/(4m))^k/D. Multiplying every prescribed draw gives total masses of all partition runs:

    W({0})=1/[16(1+a)D],
    W(T)=D^(-1) * [a/(16m(1+a))]^t,
    W_in({0} union T)= t!/[24 D t^2(t+1)m^t]
                          * [a/(4(1+a))]^(t-1),
    W_out({0} union T)= (m-t)t!/[8 D m^(t+1)(1+a)(t+1)(t+2)]
                           * [a/(4(1+a))]^t.

For inside roots the root subset-size probability is 1/6, the child-count probability is 1/[t(t+1)], and the attachment multiset probability is 1/t. For outside roots those factors are 1/[2(1+a)], 1/[(t+1)(t+2)], and 1. Every leaf costs a/[4(1+a)], and each prescribed child-gate label has probability 1/m. Summing all distinct sequences gives the factorials. Thus W_common=W_in+W_out. The exact optimized whole-cost expectation C_m is

    C_m=(1-2^(-m))^2 * log(1/W({0}))
        +4^(-m) sum_{t=1}^m binom(m,t)
           [log(1/W(T))+log(1/(W_in+W_out))].

This optimizes over all partition forests, not over successful runs with repeat visits or overlapping subsets. The latter may improve the reference output mass further and are not needed here.

For an elementary uniform bound, a<1 and 1/a<4 imply (1+a)/a<5. Since D<1/3, the dominant cost is <log(32/3)<4. Private-set cost is at most t log(80m)<=t(m+7). For common sets use only W_in, drop -log(t!), and bound log 24<5, log 20<5 and log(m+1)<=m. This gives

    log(1/W_common) <= 5+3m+t(m+5).

Adding the two rare costs and using the binomial identities bounds their full spectral expectation by

    2^(-m)(m^2+9m+5) <=15/2.

The initial value is 15/2 at m=1, and for Q(m)=m^2+9m+5 one has 2Q(m)-Q(m+1)=m^2+7m-5>=0 for m>=1. Hence C_m<=23/2<= (23/2)I(f_m). No K_ref component, terminal cost or hidden label was omitted: this calculation uses actual complete probabilities.

### 6. A paid normalized prior

For k>=0, build the entire conditioned forest reference using lambda_i^(k)=2^(-k)/m, and assign the fixed prior

    w_k=1/[(k+1)(k+2)].

The weights telescope to 1. Every component satisfies fractional incidence; each has its own Lambda_k, Z_k, and exact complete queue costs. Define Q_mix=sum_k w_k Q_{*,k}. This is a subprobability by nonnegative summation. No scale is chosen for free after observing A. Choosing k=0 for the displayed upper bound costs log(1/w_0)=1 bit under the normalized-prior lemma. Thus the whole-cost expectation is at most C_m+v<=(25/2)I(f_m); the K_ref form is at most K_ref I+R_m+v<=(K_ref+53/10)I. This uses the seed mixture interface on complete references and pays the selector, instead of adding a free adaptive scale to B.

The original two-sided dyadic prior from SEED_LEMMAS is unnecessary here; this one-sided prior is explicitly normalized and every component is admissible. Its scale is relative to the globally fixed base incidence vector, not an output-dependent incidence choice.

### 7. Boundary of the result

No line in the stated sunflower theorem remains unsupported by the derivation above. Independent acceptance is pending. The first unsupported line for full FEI is the existence, for every Boolean function, of a representation and globally fixed weights whose complete posterior residual is O(I) with one absolute constant. The sunflower calculation does not establish it. Nor does it settle shared-data collision classes with arbitrary Boolean cores.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json fixes the dimensions and resources before the search. Pilot V1 checked the inside-root collection in 1.206 seconds and is preserved as out/PILOT_V1.json. V2 adds the outside-root collection, without increasing m, to exhaust every partition forest. It passed 213,593 assertions in 1.861 seconds (the saved counter excludes the final runtime check; console includes it). Both are below the 60-second pilot limit, with no GPU, background job or dimension escalation.

Command: `python -X utf8 runs/20261011T210855Z-account05-A006-posterior-forest-optimization/code/check.py` from A006.

Truth tables for m=1,...,8: direct integer character sums and Fraction squared coefficients; Parseval, exact spectrum, v, and I checked against independent physical edge counts. Full trace enumeration for m=1,...,6 checks every listed actual partition forest, disjoint selected subsets, one visit per gate, output, uniqueness, sequential draw probability and closed-form total mass. It uses the two rational auxiliary theta values a=2/5 and 1/2. The actual a lies strictly between them by exact fifth-power comparison; these endpoint experiments are checks of the formulas, **not** certificates that the actual theta is rational. The analytic probability multiplication and the all-m inequalities above prove the actual result.

Exact rational checks also verify binomial aggregation and all initial/recurrence inequalities. No floating-point entropy signs establish a claim. The original baseline forest checker was inspected as a model for the queue key; it was not rerun or modified. This independent checker specializes to the sunflower family. Independent human/agent reconstruction is still required.

## proof dependencies and changed downstream conclusions

Dependencies: source-complete conditioned posterior forest theorem, the elementary finite Gibbs/KL identity, and the supplement's normalized complete-reference mixture argument. No unreviewed B09 claim is used. Hash-pinned sources appear in out/SOURCES.json.

Changed conclusion: the given sunflower DNF has unbounded read m and a diverging deterministic residual, but its true all-partition posterior residual and complete-cost expectation have absolute influence bounds. A coordinatewise label or deterministic-witness failure cannot be used to reject its posterior code. Consumers: A007 (normalization), A008 (label compression), A009 (incidence), A010 (residual falsification), A014 and A086. There is one combined mathematical candidate, keeping B02 below the two-unreviewed-candidate cap.

## one next mathematical action and independent reviewer

Next mathematical action: extend the forced-star enumeration to a shared conjunction of r variables with singleton private leaves and identify whether a paid normalized prior and posterior over assignments give O(I) uniformly in both r and m. This is a continuation target, not a claimed theorem. Independent reviewers: A086 for actual-run decoding/probabilities, A094 for the all-m expectation and the distinction between an existing FEI class and a new cost theorem.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, FROZEN_SPEC.json, code/check.py and exact outputs are saved in this agent's requested run directory. out/RECEIPTS.json binds sizes and SHA256 for persisted files, excluding the receipt itself. STATUS.md, WORKLOG.md and LEARNED.md are current. No shared tree was modified. GitHub/Brain upload and independent review are supervisor actions and are not claimed as completed here.
