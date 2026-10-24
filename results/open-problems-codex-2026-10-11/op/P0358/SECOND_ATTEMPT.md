# P0358 — second serious attempt, 12 October 2026

**Conclusion:** PARTIAL, with strictly improved lower and upper bounds

    2sqrt(m(alpha1-1)/t*) <= a1 <= 2sqrt(m(alpha2-1)/t*).

The full proofs, the alternative Poisson recursion, referee checks and the remaining exact-value gap are recorded below. The stages preceding the final bracket are retained to show which assertions were preliminary and subsequently proved.

## Gap reread and two approaches not previously tried

The first attempt used a single fixed lower floor for extinction and a fixed-time one-jump reset construction for survival. It left sqrt(m(p-1)/t)<=a1<=2sqrt(mq/t), with p=alpha1, q=alpha2, t=t*. It also showed that t and m alone do not determine a1.

**Approach A: iterative moving-corridor exclusion (chosen).** Instead of keeping the lower floor at zero, first prove that every upper-barrier ray eventually lies above a positive multiple of sqrt(n log n). Repeat inside the narrower corridor. This is a new reduction from a single finite-horizon first moment to a finite sequence of almost-sure lower-envelope improvements. It resembles the lower-barrier differential inequalities in absorbed branching processes, but every step will be proved directly using the first attempt's elementary deviation lemma. A quadratic obstruction suggests a factor-two stronger lower bound.

**Approach B: exact Poisson survival recursion and frozen-strip spectral asymptotics.** In the admissible Poisson-Pareto family, finite-horizon survival probabilities have an exact nonlinear recursion, 1-exp(-integral q_next(x+y)mu(dy)). A neighboring linear problem is the spectral radius of the tilted walk killed outside [0,L]. Proving the asymptotic strip cost and then a time-dependent adiabatic theorem could give an exact special-case a1. This is distinct from the first attempt's deterministic coefficient checks and final-generation reset construction. It carries harder uniformity and nonlinear-survival obligations; it is the alternative rather than the main approach.

## Gap-directed brain query

Read-only command on 12 October:

    python -X utf8 ~/.claude/dreaming/math_recall.py "branching random walk heavy tail infinite ray barrier survival sharp constant reset polynomial tilted tail Aidekon Hu Shi"

The returned cards included the old P0358 scaling attempt (claim_cd28bba7285585a915789b0992abe86b6f23abb75cc8dbc38fa77f3c42ef4504), the problem card, a general BRW card, regular variation and a generic sharp-tail-bounds paper. None supplied a sharp corridor survival criterion. They are hints only. The new moving-floor argument below is derived independently.

## Working lemma: late low endpoints inside a corridor

Write f(n)=sqrt(n log n), n>=2. Let a>c>=0 and b>=0. Suppose

    t b (a-c) < m(p-1).                                   (C)

For every fixed integer n0>=2, almost surely there are only finitely many vertices u such that |u|=n>=n0,

    c f(k)<=V(u_k)<=a f(k) for n0<=k<n,
    V(u)<=b f(n).                                          (E)

This lemma, if established, permits a lower-floor bootstrap: all rays eventually in [cf,af] must eventually lie above bf. Endpoint b need not lie within [c,a]. The important strengthening over the first attempt is summability over every generation n, not just extinction at a sampled subsequence.

**Complete proof.** Choose beta in (0,p-1) such that tb(a-c)<m beta; this is possible by (C). Choose C0>0 such that

    (a-c)/sqrt(2C0)<m,     tb<beta/sqrt(2C0).

For b>0 these require C0 to lie strictly between (a-c)^2/(2m^2) and beta^2/(2t^2b^2), a nonempty interval. For b=0 there is only the lower restriction. Let r_i=floor(C0 i^2 log i) for sufficiently large integers i. Floor errors are bounded, and elementary differentiation/asymptotics give

    Delta_i=r_i-r_{i-1}~2C0 i log i,
    f(r_i)~sqrt(2C0) i log i,
    f(r_{i-1})/f(r_i)->1,
    [a f(r_i)-c f(r_{i-1})]/Delta_i
        ->(a-c)/sqrt(2C0)<m.                              (A)

The subtraction in (A) is valid for fixed a>c: write its numerator as (a-c)f(r_i)+c[f(r_i)-f(r_{i-1})], with the latter difference o(f(r_i)). Pick h strictly between this limit and m. Choose i0 sufficiently large that r_{i0-1}>=n0, all sampled times thereafter increase strictly, and the numerator in (A) is at most h Delta_i for i>=i0.

Lemma 1 of ATTEMPT.md, with its full truncated-Laplace proof, gives for all sufficiently large i

    P(S_{Delta_i}<=h Delta_i)<=Delta_i^(-beta).

Increase i0 to meet its finite threshold. For a random-walk path in the ancestor corridor, its value at r_{i-1} is at least c f(r_{i-1}) and its value at r_i is at most a f(r_i). Its increment between those times therefore obeys that lower-deviation constraint. Independent increments (equivalently successive conditioning) imply that for L>=i0

    P(c f(k)<=S_k<=a f(k) for n0<=k<n)
        <=product_{i=i0}^L Delta_i^(-beta),                (P)

provided r_L<n. The constraint at r_{i0-1} is retained to justify the first transition, but its probability is bounded by one. Thus no conditioning on an unconstrained starting sample is used.

For each n let L=L(n) be the largest index with r_L<n, and let Z_n count the vertices satisfying (E). The many-to-one formula and the endpoint constraint yield

    E Z_n <=exp(tb f(n)) product_{i=i0}^{L(n)} Delta_i^(-beta). (F)

The sample sequence has r_{L+1}/r_L->1, so n/r_L->1 uniformly for r_L<n<=r_{L+1}. Thus

    L(n) log L(n)/f(n)->1/sqrt(2C0),
    sum_{i=i0}^{L(n)}log Delta_i / [L(n)log L(n)]->1.

For the second assertion, log Delta_i=log i+log log i+log(2C0)+o(1); sum log i~L log L, whereas sum log log i=O(L log log L)=o(L log L). Hence the log of the right side of (F), divided by f(n), tends to

    tb-beta/sqrt(2C0)<0.

There is gamma>0 such that E Z_n<=exp(-gamma f(n)) for all sufficiently large n. This is summable: for n>=3, f(n)>=sqrt(n), and grouping n in [j^2,(j+1)^2) gives a bound by sum_j(2j+1)exp(-gamma j)<infinity. The finitely many earlier E Z_n are finite as well, since E Z_n<=exp(tb f(n)). Tonelli's theorem gives E sum_n Z_n<infinity, and a nonnegative extended random variable with finite expectation is finite almost surely. This proves the lemma, including its endpoint count assertion. QED.

## A finite moving-floor bootstrap

Define

    K_source=m(p-1)/t>0.

Fix 0<a<2sqrt(K_source). Choose a deterministic K with a^2/4<K<K_source. Set c0=0. Whenever cj<a, put

    c_{j+1}=min(a, K/(a-cj)).                             (R)

This procedure reaches a after finitely many steps. Here is the full algebraic argument. For any real c,

    c(a-c)<=a^2/4,

because a^2/4-c(a-c)=(c-a/2)^2. If 0<=c<a and the minimum in (R) is not a, then

    c_{j+1}-c = [K-c(a-c)]/(a-c)
                  >=[K-a^2/4]/a=:delta>0.               (D)

The first inequality uses K-c(a-c)>=K-a^2/4>0 and 0<a-c<=a. Thus, unless a has already been reached, after j steps cj>=j delta. If the procedure never reached a, this would contradict cj<a as soon as an integer j satisfies j delta>=a. Such an integer exists by the Archimedean property. All preterminal cj lie in [0,a), and the terminal value is exactly a. Moreover every step satisfies

    c_{j+1}(a-cj)<=K<K_source.                            (S)

If the minimum is K/(a-cj), its product is K; if it is a, that minimum condition implies a(a-cj)<=K. This also covers equality at the threshold.

## Theorem: improved lower bound under the original hypotheses

    a1 >= 2sqrt(m(alpha1-1)/t*).                           (NEW-L)

**Complete proof.** Fix a<2sqrt(K_source), and take the finite floors c0,...,cJ=a just constructed. For each j<J and each integer n0>=2, apply the corridor lemma with lower coefficient cj, upper coefficient a, and endpoint coefficient b=c_{j+1}. Its strict condition follows from (S). There are only finitely many j and countably many n0. Their almost-sure conclusions hold simultaneously on an event E of probability one.

Intersect E with the almost-sure, on-survival event that min_{|u|=n}V(u)->infinity. On this intersection, assume an infinite ray xi eventually satisfies V(xi_n)<=a f(n). The global-minimum divergence implies that V(xi_n)>=0=c0 f(n) eventually. Suppose inductively that V(xi_n)>=cj f(n) eventually. Choose an integer n0, depending on this ray, from which both the upper and lower corridor constraints hold. E includes the corridor-lemma conclusion for this particular n0. The ray can supply only finitely many endpoints with V(xi_n)<=c_{j+1}f(n). Thus eventually V(xi_n)>c_{j+1}f(n), establishing the next lower floor. In the final step cJ=a, this contradicts the assumed eventual upper bound V(xi_n)<=a f(n).

This proves simultaneously that there is no ray eventually below the upper barrier a f(n), almost surely on survival. It does not interchange an infimum with a limit or use a choice of a random n0 outside the countable probability-one event.

If Theta<a, the definition of an infimum over rays gives a ray with limsup V(xi_n)/f(n)<a. That ray lies below a f(n) eventually, which has just been excluded. Therefore Theta>=a almost surely on survival. Take a countable sequence increasing to 2sqrt(K_source) to obtain (NEW-L). QED.

Together with the already proved upper bound, the new result is

    2sqrt(m(alpha1-1)/t*) <= a1 <= 2sqrt(m alpha2/t*).      (NEW-B)

For the Poisson-Pareto family with tilted negative-tail index p0>1, taking the admissible moment order up to p0 and raw-tail exponent down to p0+1 gives

    2sqrt(m(p0-1)) <= a1 <= 2sqrt(m(p0+1)).                (PP)

The endpoint witnesses are limits of strict admissible witnesses, not a claim that the p0-th tilted moment is finite. At p0=5/2, m=49/30, this raises the previous lower bound from about 1.56525 to about 3.13050; the upper bound stays about 4.78191.

## Hostile-referee checks on the new argument

* **The endpoint lemma counts all generations.** An estimate only on the r_i subsequence would not prove eventual avoidance of a moving floor. The use of L(n), with r_L<n, supplies the missing summability.
* **The first sampled transition retains its starting constraint.** r_{i0-1}>=n0 and the path is constrained there. Earlier path constraints have probability at most one, not a magically independent starting point.
* **Endpoint constraints are separate.** The corridor is imposed for k<n; the potentially low endpoint at time n is allowed outside it. The many-to-one bound uses exp(tb f(n)), not the upper corridor height exp(ta f(n)).
* **All coefficients are deterministic.** The finite floors are chosen before probability-one events are intersected. Random ray-dependent starting times are handled by countably many deterministic n0.
* **Strictness has a buffer.** The auxiliary K is strictly less than K_source. It prevents accidental equality in the corridor cost condition, even when the recurrence clips to a.
* **Global floor zero is justified.** It follows from the source's minimum-divergence conclusion on survival, not from a positive speed, which is unavailable here.
* **No independence of different rays is needed.** Finite total expected endpoint counts controls every ray simultaneously. Shared ancestry does not invalidate that first-moment argument.
* **The gap still exists.** alpha1 and alpha2 cannot be identified; the argument improves only extinction. It does not construct survival at the new lower threshold.

## Gap after the moving-floor proof, before the subsequent refinement

The old factor-two mismatch in the coefficient is removed from the lower bound. The remaining gap is the difference between the tilted moment exponent alpha1-1 and the raw one-child reset exponent alpha2. For the regular Poisson-Pareto examples it is p0-1 versus p0+1. Closing it requires either a stronger multi-time survival construction with matching cost, or a proof that a different law statistic determines the exact threshold. The new corridor exclusion is a complete lower-bound proof, not a proof of any proposed exact formula.

## Further direction discovered during the audit: variable-time reset lines

The fixed-endpoint survival construction discards all but one possible reset time per block. A potentially stronger construction tests reset parents throughout the last fixed fraction of a block and retains successful children as an optional line (an antichain), rather than forcing them to have the same generation. This can gain one power of block length. The conditional successes across different generations are not independent, so the proposed argument uses a predictable Bernoulli compensator and an exponential supermartingale instead of an incorrect conditional-independent sum.

The target is an upper bound 2sqrt(m(alpha2-1)/t*). The complete argument below checks the tilted mass lost by pruning, uniformly positive aggregate candidate mass, the predictable compensator, and time conversion. The earlier save point treated this only as work in progress.

## Lemma: an adaptive Bernoulli compensator bound

Let I_l be {0,1}-valued variables explored sequentially, with predictable probabilities pi_l=E[I_l|F_{l-1}]. Let N=sum I_l and A=sum pi_l, where the number of actual trials is finite almost surely (possibly random). After exploration finishes, pad the sequence by I_l=pi_l=0. Then for R>0, integer K0>=1, and s>0,

    P(N<K0, A>=R)<=exp(s K0-(1-exp(-s))R).                (CB)

Proof. Put h=1-exp(-s) in (0,1). The process

    M_L=exp(-s sum_{l<=L}I_l+h sum_{l<=L}pi_l)

is a nonnegative supermartingale starting at 1. Indeed its one-step conditional factor is exp(h pi_l)(1-h pi_l)<=1, because 1-z<=exp(-z) for z>=0. Its expectation is at most one at every deterministic L. Since exploration is finite almost surely, M_L converges to exp(-s N+h A). Fatou yields E exp(-s N+h A)<=1. On {N<K0,A>=R} the limit is at least exp(-s K0+h R). Markov's inequality proves (CB). This proof does not condition on a random entire compensator and then falsely assert independence. QED.

## Theorem: improved upper bound by variable-time reset lines

    a1 <= 2sqrt(m(alpha2-1)/t*).                          (NEW-U)

**Complete proof.** Fix c>m, gamma in (0,1), lambda>0, and d>(q-1)/t. For each sufficiently large block index i let

    B_i=floor(2lambda i log i),  k_i=ceil(gamma B_i),
    H_i^reset=d log i.

Choose v with 0<v<m gamma. We first define a single-block exploration in a fresh subtree, with positions relative to its root (position zero). Explore only vertices whose paths satisfy V(w_l)<=c l for every l up to their depth. A parent w is eligible when

    k_i<=|w|<=B_i,    V(w)>=v B_i.

At every eligible parent reveal its offspring. If it has any child at relative position <=H_i^reset, count one success and choose one such child by its label. Retain that child as a terminal reset output. Explore no descendants of any child at position <=H_i^reset of this eligible parent, whether chosen or not. Continue exploration through all other children satisfying the path cap, up to parent depth B_i. At noneligible parents continue through all cap-admissible children as usual. Call the continuing, cap-admissible tree the bulk tree. All chosen terminal children form an antichain: their descendants are never explored within this block, so a later chosen terminal child cannot descend from an earlier one.

This exploration has finitely many nodes almost surely. At any depth k, the full weighted sum W_k is finite almost surely, since E W_k=1. Every cap-admissible vertex has V(w)<=c k and weight exp(-tV(w))>=exp(-tc k). Hence the number of such vertices at that depth is at most exp(tc k)W_k<infinity. The deterministic depth bound B_i+1 makes the entire explored set finite. This argument also handles an offspring process with infinitely many children at very large positive positions.

Define aggregate candidate mass

    H_i=(1/B_i) sum_{k=k_i}^{B_i}
                sum_{w in bulk, |w|=k, V(w)>=v B_i} exp(-tV(w)).  (HM)

For comparison let the inner sum in the full, unpruned cap tree be U_{i,k}. Many-to-one gives

    E U_{i,k}=P(S_l<=c l for l<=k, S_k>=v B_i).

Uniformly for k in [k_i,B_i], this tends to Q_c>0 from Lemma 3 of ATTEMPT.md. To see uniformity, the cap probabilities converge to Q_c as k->infinity, and

    P(some k>=gamma B_i has S_k/k < v/gamma)->0

by the strong law, since v/gamma<m. In particular S_k>=v B_i throughout this window with probability tending to one. Therefore

    (1/B_i)sum_{k=k_i}^{B_i}E U_{i,k}->(1-gamma)Q_c.      (M1)

The weighted mass lost by pruning is negligible. If a tilted spine child is pruned, its parent has position at least v B_i and that child has position <=d log i. For sufficiently large i its displacement is thus <=-v B_i/2. The many-to-one representation of the bulk sum is the random-walk probability of the cap and endpoint constraint, with no previously pruned spine edge. The union bound over at most B_i edges gives, uniformly in the window,

    0<=E U_{i,k}-E[bulk candidate mass at k]
       <=B_i P(X<=-v B_i/2)
       <=C B_i^(1-p)->0.                                (M2)

Here C is finite from the original tilted p-moment; the constant v is fixed. The pruning event is determined by spine positions, not by a condition on unchosen siblings. A spine edge is pruned exactly when its own position is low and its parent is eligible. Thus this many-to-one identity does not introduce a sibling-bias assumption.

Combining (M1) and (M2) gives

    E H_i->(1-gamma)Q_c=:Q>0.                             (M3)

Also H_i<=(1/B_i)sum_{k=k_i}^{B_i}W_k. This family is uniformly integrable because {W_k} is uniformly integrable. Explicitly, for any convex average Y of nonnegative W_k (adding a zero term if its weights sum to less than one),

    Y 1_{Y>M} <=2 sum_k weights_k W_k 1_{W_k>M/2}.

Indeed Y<=M/2+sum weights_k(W_k-M/2)_+, and on {Y>M} the second term is at least Y/2. The expectation on the right tends uniformly to zero as M->infinity. Domination then proves uniform integrability of H_i. As in the first attempt's positive-mass argument, there exist eta,rho>0 with

    P(H_i>=eta)>=rho                                     (M4)

for every sufficiently large i. For completeness, choose M such that sup_i E[H_i 1_{H_i>M}]<Q/8, use E H_i>=Q/2, and eta=Q/8. Then Q/2<=eta+M P(H_i>=eta)+Q/8, so rho=Q/(4M) works after enlarging M if needed.

Order the eligible parent tests by increasing generation and label, revealing each parent's offspring only when it is tested. A parent's presence, position and eligibility are determined before revealing its reproduction. Conditionally on this history, its success indicator is Bernoulli with probability

    pi_w=theta(V(w)-d log i).

Parents' indicators across different generations need not be independent. They nevertheless satisfy the predictable-probability framework of (CB). Eligible parents have v B_i<=V(w)<=c B_i, so their y=V(w)-d log i tends uniformly to infinity and is at most c B_i. The source tail bound gives

    pi_w >=i^(td)(c B_i)^(-q)exp(-tV(w)).

Writing A_i for the full predictable compensator, and nu_i for the number of successes/terminal reset outputs, we obtain the pathwise inequality

    A_i >=c^(-q)i^(td)B_i^(1-q) H_i=:G_i H_i,
    G_i->infinity,                                      (G)

since td>q-1 and B_i~2lambda i log i. Apply (CB) with s=1. For any fixed integer K0,

    P(nu_i<K0,H_i>=eta)
       <=exp(K0-(1-exp(-1))G_i eta)->0.

Together with (M4), this yields P(nu_i>=K0)>=rho/2 for all sufficiently large i. Pick K0 large enough that K0 rho/2>1. Thus every sufficiently late block reproduction law dominates the fixed supercritical law with K0 children with probability rho/2 and zero otherwise.

Retained terminal children have unexplored descendant subtrees. The standard branching property applies to this explicitly constructed stopping line: independence of the point processes assigned to distinct vertices implies that, conditional on the block exploration, all future subtrees below these incomparable children are independent fresh copies of the original branching random walk. Selection used their labels/positions, not their own reproduction. Inductively performing block i+1 below each terminal output therefore gives an inhomogeneous Galton–Watson process with offspring law nu_i at block i, regardless of the terminal children's possibly different depths. Independent quantile coupling embeds the fixed supercritical process. Starting at the root with any sufficiently late block index gives survival with positive probability. Every block has finitely many outputs; the surviving embedded tree supplies an infinite ray.

Along this ray, the duration ell_i of block i lies in

    gamma B_i <=ell_i<=B_i+1,

and its endpoint displacement is at most d log i. Up to the endpoint, its displacement at any local step l is at most c l: every parent path satisfies the cap, and the final child position <=d log i is also <=c ell_i for large i. If T_j is the cumulative generation after block j (with an arbitrary fixed initial index), then

    T_j>= (gamma lambda+o(1))j^2 log j,
    V(xi_{T_j})<= (d+o(1))j log j.

These follow from sum_{i<=j}B_i~lambda j^2 log j and sum_{i<=j}log i~j log j. If T_j<=n<T_{j+1}, then

    V(xi_n)<=V(xi_{T_j})+c(B_{j+1}+1)
             <=(d+2c lambda+o(1))j log j,
    f(n)>=f(T_j)>=(sqrt(2gamma lambda)+o(1))j log j.

Thus with positive probability an infinite original ray has

    limsup_n V(xi_n)/f(n)
      <=(d+2c lambda)/sqrt(2gamma lambda).

The source's deterministic-on-survival theorem promotes this positive-probability construction to the same upper bound for a1. Choose lambda=d/(2c), obtaining 2sqrt(cd/gamma). Finally let c decrease to m, d decrease to (q-1)/t and gamma increase to one along countable deterministic sequences. Q_c,eta,rho may depend on these fixed choices; no uniformity in those limits is assumed. The resulting deterministic bound is (NEW-U). QED.

## Updated two-sided conclusion

The complete proofs in this file establish

    2sqrt(m(alpha1-1)/t*) <= a1 <= 2sqrt(m(alpha2-1)/t*).  (FINAL-B)

The gap is smaller than both earlier brackets. In the Poisson-Pareto family,

    2sqrt(m(p0-1)) <= a1 <= 2sqrt(m p0).                  (FINAL-PP)

For p0=5/2 and m=49/30, these bounds are approximately 3.13050 and 4.04145. This still does not identify the constant.

## Additional hypothesis consistency check

The source's two polynomial witnesses necessarily satisfy alpha2>alpha1+1 (a stronger restriction than the displayed alpha1<=alpha2). Let mu_- be the negative-displacement intensity in terms of z=-x>0. Its tail F(y)=mu_-([y,infinity)) is at least theta(y), and hence at least exp(-ty)y^(-q) for all sufficiently large y. Tonelli gives

    integral exp(tz)z^p mu_-(dz)
      >=t integral_{y0}^infinity exp(ty)y^p F(y)dy
      >=t integral_{y0}^infinity y^(p-q)dy.

For the first inequality use, pointwise for z>=y0,

    exp(tz)z^p >=t integral_{y0}^z exp(ty)y^p dy,

since y^p<=z^p and integral_{y0}^z t exp(ty)dy<=exp(tz). The left side is finite by the tilted p-moment. The last integral is finite only when p-q<-1, proving q>p+1. In particular q>2. This check prevents an apparent false exact solution obtained by setting alpha1=alpha2; such witnesses cannot occur under the full assumptions.

## Canonical law parameters (a bound, not an identification)

Let

    p_- =sup{r>1:E[(X^-)^r]<infinity},
    q_* =limsup_{y->infinity}[-log theta(y)-ty]/log y.

Under the source assumptions, 1<alpha1<=p_-<infinity and 2<q_*<=alpha2, with q_*>=p_-+1. Here is a complete justification. The tail hypothesis bounds q_* above by alpha2. For any q'>q_*, the definition of limsup supplies theta(y)>=exp(-ty)y^(-q') eventually. For any r with a finite negative tilted r-moment, the preceding Tonelli argument with r,q' forces q'>r+1. Let q' decrease to q_* and take the supremum over r to obtain q_*>=p_-+1>2, which also bounds p_- finitely.

The lower-deviation lemma can use any finite negative r-moment, without needing a positive r-moment. Retain the existing finite absolute alpha1-moment only for the Laplace remainder exponent s=min(alpha1,2)>1. Clipping X at -y still gives E|clip(X)|^s<=E|X|^s and E clip(X)>=m. The large-negative-jump union bound instead reads nP(X<-y)<=n E[(X^-)^r]/y^r. With y=n^(1-delta), this proves the deviation lemma for every beta<r-1. Every subsequent corridor/bootstrap step is unchanged. Let r increase to p_-; the moment spectrum is downward closed by the elementary inequality z^r<=1+z^{r'} for r<r'. This proves the canonical lower bound. The variable-time reset proof applies for each q'>q_* and uses only the original absolute moment for its lost-mass estimate; let q' decrease to q_*. Consequently,

    2sqrt(m(p_--1)/t*) <= a1 <= 2sqrt(m(q_*-1)/t*).       (LAW-B)

For Poisson-Pareto offspring, p_-=p0 and q_*=p0+1, exactly as computed in the first attempt. Thus these canonical parameters do not close even that special-case gap.

## Final gap at this save point

The extinction and variable-time survival constructions now have the same factor two. In the regular Poisson-Pareto family, their remaining squared-cost parameters are p0-1 versus p0; the earlier gap was p0-1 versus p0+1. A matching sharper survival construction or stronger extinction theorem is still missing. The general law-based bracket (LAW-B) cannot be declared an exact formula, and the full point-process hypotheses admit correlations not present in the Poisson example.

## Approach B: an exact finite-horizon reduction, without an exact asymptotic solution

For the finite-intensity Poisson offspring family let b_k be a deterministic upper barrier, with b_0,b_1 specified separately when later b_k=a sqrt(k log k). Let q_{k,N}(x) be the probability that a particle at absolute position x at generation k has some cap-admissible descendant at generation N, requiring the path to remain at or below b_l for k<=l<=N. Then exactly

    q_{N,N}(x)=1_{x<=b_N},
    q_{k,N}(x)=1_{x<=b_k}
       [1-exp(-integral q_{k+1,N}(x+y)mu(dy))].           (POIS)

Proof. If x>b_k, the particle is already killed. Otherwise its offspring form a Poisson point process of displacements with intensity mu. Conditional on their positions, the events that the offspring have a cap-admissible descendant at N are independent, by the branching property, with success probability q_{k+1,N}(x+y). The Poisson generating functional gives probability exp(-integral q_{k+1,N}(x+y)mu(dy)) that no offspring succeeds; equivalently this is independent thinning of the Poisson process. Subtracting from one proves the recursion. The integral is finite because 0<=q<=1 and mu(R)<infinity. All functions are measurable by induction. QED.

For each fixed k,x, q_{k,N}(x) decreases as N increases, since success at N+1 implies success at N. Its limit is the probability of an infinite cap-admissible ray: continuity of probability from above gives the probability of cap-admissible vertices at every finite depth, and the Poisson tree has finite offspring almost surely, so the finitely branching tree lemma converts that event to an infinite ray. The same argument works in a fresh subtree with shifted absolute position and time. Thus (POIS) is an exact reduction of fixed-start barrier survival in this special family.

The unproved step is an asymptotic analysis of this recursion at b_n=a sqrt(n log n), together with its relation to all eventually bounded rays under the source's infimum/limsup quantifiers. Linearizing (POIS) at zero or numerically iterating it at a finite N does not establish that step. This alternative was not substituted for the already proved moving-corridor and stopping-line results, and no finite-horizon number is called a1.

## Method limits and boundary cases

At a=2sqrt(K), the unclipped floor recurrence c_{j+1}=K/(a-cj), c0=0, has the exact solution

    cj=(a/2)j/(j+1).

Proof by induction: substituting this formula into K/(a-cj), with K=a^2/4, gives (a/2)(j+1)/(j+2). It never reaches a. For a>2sqrt(K), the smaller positive root r=(a-sqrt(a^2-4K))/2 of r(a-r)=K is a fixed point of the increasing map c->K/(a-c). Starting at zero, induction bounds all iterates by r<a. Thus the finite constant-floor bootstrap cannot improve its threshold merely by running additional iterations.

For the upper construction, gamma is sent to one only after a fixed positive-length time window was used. Setting gamma=1 before taking i->infinity eliminates the factor B_i and loses the improved exponent. At the endpoint td=q-1, G_i is proportional to (log i)^(1-q), which tends to zero; strict td>q-1 is essential, and equality is reached only by a final limit over d.

The canonical consistency relation q_*>=p_-+1 shows that even optimal choices of polynomial witnesses cannot make (LAW-B) match: the two squared-cost parameters differ by at least one in the Poisson-Pareto case and cannot become equal by choosing alpha1 and alpha2 differently. A new estimate or construction is required.

## Checks completed and their scope

* `corridor_checks.py` passed 250 exact-rational clipped recurrences. Each reaches a within the rigorously derived finite bound. It verified the critical identity cj=j/(j+1) for 1,000 steps at a=2,K=1. Five block indices through 10^6, each with three endpoint positions inside the next block, checked the all-generation normalization. The convergence is slow and need not be monotone; no finite sample is used in place of the limit proof.
* `reset_checks.py` passed 100 finite adaptive Bernoulli-tree enumerations, including 1,500 event inequalities, 1,000 optimized variable-duration coefficients and 1,000 convex-average UI inequalities. It explicitly tests adaptive, not independent, probabilities. These tests are numerical checks of auxiliary facts, not simulations of an infinite ray.
* In the example q=3.5,td=2.6, G_i initially decreases through i=10^6 because the small positive power i^0.1 is masked by (log i)^(-2.5). The exact log expression turns upward only after log i>25, and the large-log evaluations in reset_checks.json confirm eventual growth. The proof uses the exact power comparison and does not infer divergence from a short run.
* `CorridorBootstrap.lean` kernel-checks the quadratic corridor inequality, the bootstrap increment, the clipped-step cost and the finite-growth contradiction. Run via `lake env lean <absolute file path>` from ~/lean_verify, with a 3600-second timeout, one Lean process at a time. Final exit code 0; every printed axiom set is [propext, Classical.choice, Quot.sound]. No sorry or native_decide occurs in the checked file. Its imports are Mathlib.Data.Real.Basic plus the explicitly used Linarith and FieldSimp tactic files.
* The first Lean invocation failed because the real-number type had not been imported. That failure is saved in corridor_lean_failed1.txt and is never called a checked proof. Adding the specific Real.Basic import fixed the issue; corridor_lean_check.txt contains the successful final output.

## Additional referee audit of the upper construction

1. **Sibling dependence:** discard only a parent's low children, not all its children when it has a low sibling. The bulk spine event then depends on its own edges. Discarding all offspring of a successful parent would invalidate (M2).
2. **Adaptive trials:** a future candidate parent's existence can depend on previous successes. The compensator lemma, rather than a variance formula for a supposedly independent full-generation sum, handles this.
3. **A random trial count:** the depth-capped explored tree is finite almost surely. Pad with zeros and use deterministic-time supermartingales plus Fatou; no unsupported optional stopping expectation equality is asserted.
4. **Antichain outputs:** all low children at an eligible parent are pruned from the bulk. Retaining only one as an output preserves finite branching and leaves its reproduction unobserved. No retained output can be an ancestor of another output within the block.
5. **Fresh subtrees:** terminal selection uses positions and labels only. The output's own point process and all descendant point processes remain independent of the exploration. The different depths do not change the translated reproduction law.
6. **Lost weighted mass:** the original absolute p-moment with p>1 is exactly what makes B P(X<=-vB/2)=O(B^(1-p)) tend to zero; a raw probability estimate without the tilt would not prove this comparison.
7. **Count-to-time conversion:** offspring generation in the embedded process is the block index, not the original generation. The deterministic lower duration gamma B_i is required in the denominator. The gamma penalty is present until the final deterministic limit.
8. **Positive mass is not just positive expectation:** domination by UI averaged W_k is used to obtain a uniformly positive probability of H_i>=eta. This rules out an expectation carried entirely by rare gigantic families.
9. **No exact solution label:** all formal and numerical certificates cover finite/auxiliary steps. The open problem's exact a1 is not proved, and neither an optimality claim nor a publication/novelty claim is made.
