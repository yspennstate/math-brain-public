# Second serious attempt at F0118 — 12 October 2026

## Two previously untried approaches

1. **Binary-experiment Blackwell comparison using the copy-cluster representation.** Regard the root as a binary hypothesis (label 1 versus label 2), while retaining the full q-state boundary observation. The copy-edge partition is independent of q; only accidental equalities between independently colored clusters change with q. Try to compare the resulting binary experiments in Blackwell order, a substantially stronger property than the previously studied total variation. For a symmetric binary experiment this amounts to comparison of every stop-loss transform of the absolute posterior bias, not just its mean. Such an order at all depths would immediately settle F0118. Test the proposed comparison exactly before attempting an induction; a counterexample to this stronger order would identify why a binary channel argument fails without refuting F0118.

2. **Population dynamics followed by a rigorous invariant-neighborhood reduction.** Work directly with the conditional-root distributional posterior recursion, starting from a perfectly revealing boundary. Look for a source q and a larger target r whose nonlinear fixed points order incorrectly, especially q=5,r=6 and b lambda^2<1. If numerical evidence suggests a separation, attempt to certify one side by an explicit recursive estimator and the other by a Lyapunov or strong-data-processing inequality. Numerical convergence alone would not be a counterexample. This differs from the first attempt's small exact leaf enumerations and independent recoloring obstruction.

Approach 1 is pursued first because its finite checks are exact, its proposed induction target is explicit, and failure can be certified without estimating an infinite-depth limit.

## Precise proposed stronger statement
Let E_q(T,lambda) be the observation experiment consisting of the whole boundary of a finite rooted tree, with equally likely root hypotheses 1 and 2 and q-state Potts edge channels. Is E_r a Blackwell improvement of E_q whenever r>q at the same positive lambda? This is stronger than F0118. It is not assumed to hold.

For a boundary word y set a=P(y|root=1), d=P(y|root=2). Its marginal mass is (a+d)/2 and its absolute posterior bias is z=|a-d|/(a+d). Swapping root labels makes the signed posterior bias symmetric. Define H_q(t)=E[(z-t)_+] for 0<=t<=1. All these transforms being ordered is equivalent to convex ordering of the symmetric posterior biases, hence to binary Blackwell ordering. H_q(0) is precisely pairwise root total variation. A negative H_r(t)-H_q(t) at any single t disproves the proposed stronger comparison.

The finite computation below directly evaluates

    H_q(t) = (1/2) sum_y (|P_1(y)-P_2(y)|-t(P_1(y)+P_2(y)))_+.

Exact rational likelihoods and rational thresholds make every returned witness exact. Checking all combined posterior-bias knots suffices: the difference of the two H functions is affine between consecutive knots.

## Brain queries and caution
Read-only math-store queries were made for (i) "Potts reconstruction symmetric posterior laws Blackwell comparison alphabet monotonicity Mossel Peres", (ii) "Blackwell order symmetric binary experiments convex order posterior bias Potts reconstruction", and (iii) "Strassen martingale coupling convex order Blackwell Sherman Stein comparison experiments". The first two returned no directly useful theorem. The third returned Strassen's **ordinary stochastic-order** coupling theorem and the bibliographic card for Strassen (1965), DOI 10.1214/aoms/1177700153. The card does not state the martingale/convex-order theorem needed here; substituting ordinary stochastic order would be incorrect. The finite convex-order/garbling argument is therefore proved below, rather than taken from the card.

## Exact obstruction: arbitrary rooted-partition coloring is insufficient

This is a counterexample to a stronger proposed comparison, **not** to F0118.

Consider root 0 and four observed vertices 1,2,3,4. Select a random partition independently of the root state, with the following probabilities (block codes are in order 0,1,2,3,4):

| partition code | blocks in words | probability |
|---|---|---|
| (0,0,1,1,0) | root with 1,4; 2 with 3 | 1/27 |
| (0,0,1,2,2) | root with 1; 2 singleton; 3 with 4 | 9/27 |
| (0,1,0,2,1) | root with 2; 3 singleton; 1 with 4 | 8/27 |
| (0,1,1,0,2) | root with 3; 4 singleton; 1 with 2 | 5/27 |
| (0,1,2,3,4) | all five vertices singleton | 4/27 |

The root block has the root's label (equally likely 1 or 2), and every other block receives an independent uniform q-state label. The partition prior is identical for q=4 and q=5.

Let y be a boundary word. In common denominator 27q^4 its two root likelihoods have the form

    P_1(y)=(4+S_1(y))/(27q^4), P_2(y)=(4+S_2(y))/(27q^4).

For root h, the first four rows contribute respectively q^3,9q^2,8q^2,5q^2 when their root-block and equality constraints are satisfied. The last row always contributes 4 under either root.

Two distinct rows among the first four cannot both satisfy their constraints under the same root h unless all four boundary labels equal h. Check the six pairs directly: rows 1 and 2 impose y1=y4=h, y2=y3, and y3=y4, hence all h; rows 1 and 3 impose y2=h and y2=y3; rows 1 and 4 impose y3=h and y1=y2; rows 2 and 3 impose y1=y2=h, y1=y4, y3=y4; rows 2 and 4 impose y1=y3=h, y3=y4, y1=y2; rows 3 and 4 impose y2=y3=h, y1=y2, y1=y4. In every case all four labels are h.

Consequently a nonconstant word has at most one signal term for each root. For q=4 or 5 this gives S_h<=9q^2, because q^3<=9q^2. Its absolute posterior bias obeys

    |S_1-S_2|/(S_1+S_2+8) <= 9q^2/(9q^2+8).

The bound is 18/19 for q=4 and 225/233 for q=5. Constant words other than all-1 and all-2 have zero bias. The two constant signal words have

    z_q=(q^3+22q^2)/(q^3+22q^2+8),
    combined marginal mass w_q=(q^3+22q^2+8)/(27q^4).

For example for all-1, every first-four-row constraint is satisfied under root 1 and none under root 2, giving these formulas; all-2 is the swapped case.

At threshold t=225/233, which is above 18/19, only these two signal words contribute a positive stop-loss for either alphabet. Thus

    H_4(t) = 191/201312 = 4775/5032800,
    H_5(t) = 16/17475 = 4608/5032800,
    H_5(t)-H_4(t) = -167/5032800 < 0.

Therefore increasing the number of cluster colors from 4 to 5 can make a high-confidence binary decision payoff worse, despite leaving the random partition prior unchanged. The enumerated total variation nevertheless increases: TV_4=3/4 and TV_5=529/675. This distinction is central: the counterexample disproves a proposed Blackwell shortcut, not the requested reconstruction monotonicity or even finite-depth TV monotonicity.

Why it is not a Potts-tree counterexample: for a finite connected tree with every copy probability strictly positive, the event that every edge copies has positive probability and puts root and all four observed vertices in one block. This partition has probability zero in the above prior. Hence the displayed prior cannot be the copy-cluster partition of the source's finite Potts broadcast. Its failure does show that any cluster-coloring proof must use more than an arbitrary q-independent partition distribution.

`partition_search.py` found the prior in a bounded search (seed 11802, about six seconds), then evaluated the witness exactly. The proof above independently derives the witness without relying on the search or full histogram enumeration. `partition_witness.json` retains all rational posterior masses and likelihood checks.

## Finite binary Blackwell criterion, proved rather than assumed

For a finite binary experiment with equal root priors, put B=P(root=1|Y)-P(root=2|Y). If its marginal observation masses are m_y, its conditional laws are m_y(1+B_y) and m_y(1-B_y). Thus observing B itself is sufficient: once B is known, an observation with that value can be resampled from its marginal conditional law, which is independent of the hypothesis.

If an experiment is garbled by a stochastic kernel independent of the root, its new posterior bias X is E[B|garbled observation]. Jensen implies convex ordering: E phi(X)<=E phi(B) for every convex phi.

Conversely let two finitely supported, centered posterior-bias laws be X=x_i with masses p_i (the weaker candidate) and Y=y_j with masses r_j. Assume E phi(X)<=E phi(Y) for all convex phi. Seek nonnegative numbers a_ij with row sums p_i, column sums r_j, and sum_j a_ij y_j=p_i x_i. They are a finite linear feasibility problem. By the finite Farkas separation lemma, infeasibility would give numbers u_i,v_j,w_i with

    u_i+v_j+w_i y_j>=0 for all i,j,
    sum_i p_i u_i+sum_j r_j v_j+sum_i p_i w_i x_i<0.

But phi(y)=max_i(-u_i-w_i y) is convex. The first inequality gives v_j>=phi(y_j), and phi(x_i)>=-u_i-w_i x_i gives u_i+w_i x_i>=-phi(x_i). The supposedly negative expression is therefore at least E phi(Y)-E phi(X)>=0, contradiction. A feasible coupling exists. Send y_j to x_i with probability a_ij/r_j (discard zero r_j). Conditional on either root hypothesis, the resulting mass at x_i is

    sum_j a_ij(1 +/- y_j)=p_i(1 +/- x_i),

exactly the weaker experiment's conditional law. Its original observation can then be resampled using sufficiency. This proves finite binary Blackwell dominance from convex ordering. Only the elementary finite linear-program separation theorem is used here; no recalled Strassen card is substituted for this proof.

For root-label-symmetric experiments the signed bias distribution is symmetric. Given a convex phi on [-1,1], g(z)=(phi(z)+phi(-z))/2 is convex and nondecreasing for 0<=z<=1. Nondecreasing follows from evenness and convexity: for 0<=x<=y, x is a convex combination of y and -y. Interpolate g linearly between the finitely many absolute-bias values from both laws. The interpolation is convex, has nonnegative initial slope, and is g(0)+a z+sum_k b_k(z-t_k)_+ with a,b_k>=0. Thus comparison of H(t)=E[(|B|-t)_+] at every t>=0 implies comparison for every convex phi; H(0) supplies the linear z term. The reverse follows by applying convex ordering to (|B|-t)_+. This establishes the stop-loss criterion used in the checks.

## Stronger proved finite-tree result: binary Blackwell order on two-leaf branches

### Statement
Fix a root with finitely many children. Each child has two observed leaves. For each branch, fix a parent-to-child parameter alpha in (0,1) and a child-to-leaf parameter beta in (0,1), the same beta on the two edges of that pair. Different branches may use different parameters. All parameters are held fixed as the alphabet size changes. For any integers 2<=q<r, the full r-state leaf observation, restricted to root hypotheses 1 versus 2, Blackwell-dominates the q-state leaf observation. In particular every binary decision problem becomes no harder, and pairwise root TV is nondecreasing. This includes depth two on a homogeneous binary tree and extends the previous TV-only result.

### Proof for one branch
Put s=1-beta, c=s/q, a=alpha beta, h=(1-alpha)beta^2/s, and k=1+2beta(1-alpha)/s. Then a,h,k>0 and k beta=beta+2h. Integrating out the unobserved child gives the same seven categories as in the earlier ATTEMPT.md table, now with

    A=h c+k c^2, B=k c^2, u=a(beta+2c), v=a c.

Indeed a pair of equal leaf labels has child-state likelihood (beta+c)^2 for that label and c^2 otherwise. Averaging this through the parent edge gives base

    ((1-alpha)/q)[beta^2+2beta c+q c^2]+alpha c^2=A,

and increment alpha[(beta+c)^2-c^2]=u. A distinct pair has child-state likelihood c(beta+c) on the two labels and c^2 otherwise, giving base ((1-alpha)/q)[2beta c+q c^2]+alpha c^2=B and increment alpha beta c=v. Substitute 1/q=c/s and qc=s to obtain the displayed formulas.

Under the binary root prior the two equal-signal categories E1,E2 together have marginal mass w_E=2A+u and absolute bias z_E=u/w_E. The distinct-signal categories D1,D2 have multiplicity m=2(q-2)=2s/c-4 on each side, so together have mass m w_D, where w_D=2B+v, and bias z_D=v/w_D=a/(a+2kc). The neutral categories have bias zero and play no role in stop-loss payoffs. The mass factors follow by averaging the two root likelihoods before pairing the symmetric categories; they are not q-uniform-root posterior masses.

Also

    uB-vA=a c^2(k beta-h+kc)=a c^2(beta+h+kc)>0,

so z_E>z_D>0. For any fixed threshold t in [0,1],

    H_c(t)=(u-t w_E)_+ + m(v-t w_D)_+.

We show it is nonincreasing in c on 0<c<=s/2. On t>=z_E it is zero. On z_D<=t<z_E only the E term contributes and

    dH_c(t)/dc = 2a-t(2h+2a+4kc)
                <= 2a-[a/(a+2kc)](2h+2a+4kc)
                = -2ah/(a+2kc)<0.

On 0<=t<z_D both terms contribute. Their first moment and combined informative mass simplify to

    u+mv=a(2-beta-2c),
    w_E+m w_D=a(2-beta)+(2h-2a+4sk)c-6kc^2.

Thus

    dH_c(t)/dc=-2a-t(2h-2a+4sk-12kc).

Put D=a+2kc and eta=tD/a, so 0<=eta<=1. Its negative, multiplied by D/(2a)>0, is

    D-eta(a-h-2ks+6kc)
      =(1-eta)D+eta[h+2k(s-2c)]>0.

Here D>0, h>0 and s-2c>=0; the two nonnegative weights sum to one. Hence the derivative is strictly negative also in this region.

The expressions meet continuously at t=z_D and t=z_E, because the relevant positive-part term is then zero. For fixed t, the transitions occur only finitely many times: z_D is strictly decreasing in c, and z_E is a nonconstant rational function, so an equation z_E=t has at most finitely many roots unless it is identically true, which it is not (at c down to zero z_E tends to 1 and at positive c it is less than 1). Piecewise differentiability and the nonpositive derivative therefore give global nonincrease in c. Increasing q decreases c, proving H_r(t)>=H_q(t) for every t. The finite criterion above proves binary Blackwell dominance for the branch.

The derivative argument uses a rational extension in c (equivalently real q>=2) only to compare the integer endpoints. Only integer q is interpreted as an alphabet size. No probability model at a noninteger number of states is required.

### Combining branches
The branch observations are independent conditional on the **root** hypothesis; integrating out separate child states preserves this independence. For each branch use the binary garbling kernel just proved to convert its r-state observation law into its q-state law under both root labels. Apply these kernels independently across branches. The conditional product law becomes exactly the q-state root experiment. This is a whole-branch transformation, not independent recoloring at every vertex, so it is consistent with the earlier divisibility obstruction. It proves the statement for any finite number of branches and for the specified heterogeneous parameters.

### Limitation
This does not permit induction to arbitrary depth. The branch garbling is certified only for child input hypotheses 1 and 2. When a branch is preceded by another Potts edge, the child's true label may be any other state, and the common reset contribution involves all q conditional observation laws. Binary comparison alone does not preserve that contribution. The next explicit counterexample shows the closure issue remains even for symmetric posterior laws.

## Exact obstruction: pairwise binary Blackwell order is not closed under a Potts edge

Again this is a counterexample to an induction principle, **not** to F0118. Both experiments here use the same q=3.

For a posterior vector p, let O(p) be the uniform law over all its coordinate permutations. Every such law has barycenter (1/3,1/3,1/3). It defines a valid symmetric three-input experiment: the observation is a posterior vector sampled with marginal law mu, and its conditional law given input i has density 3p_i against mu. These laws integrate to one, and Bayes returns p. Mixtures of the orbits remain symmetric valid experiments.

Define the candidate stronger and weaker posterior laws by

    mu = (2/5)O(0,1/6,5/6)+(1/25)O(0,1/3,2/3)
         +(2/5)O(0,1/2,1/2)+(4/25)O(1/6,1/3,1/2),
    nu = (2/5)O(0,0,1)+(2/5)O(1/6,1/6,2/3)
         +(1/5)O(1/3,1/3,1/3).

Restrict either experiment to equally likely input hypotheses 1 and 2. For any three-coordinate orbit its absolute-bias stop-loss is exactly

    H_{O(p)}(t)=(1/2) sum_{i<j} (|p_i-p_j|-t(p_i+p_j))_+.

To verify the factor, average over all six coordinate permutations, with repetitions if coordinates agree; each unordered coordinate pair appears twice. Its binary marginal weight is (3/2)(p_1+p_2), and the positive-part bias term divides by p_1+p_2. Hence the total factor is (3/2)*(2/6)=1/2. Repeated permutations induce exactly the same uniform law on the unique orbit points because each unique permutation has the same multiplicity.

All pre-edge breakpoints from these orbits are 0,1/5,1/3,1/2,3/5,2/3,1. Direct substitution in the displayed formula gives:

| t | H_mu(t)-H_nu(t) |
|---|---|
| 0 | 1/75 |
| 1/5 | 0 |
| 1/3 | 0 |
| 1/2 | 1/100 |
| 3/5 | 8/375 |
| 2/3 | 1/150 |
| 1 | 0 |

The difference is affine between consecutive breakpoints, so it is nonnegative everywhere in [0,1]. The finite criterion proves mu's restricted binary experiment Blackwell-dominates nu's. By full coordinate symmetry the same holds for every pair of distinct input symbols.

Now precede each experiment by the **same** three-state Potts edge of eigenvalue 1/2. Since the input is uniform and the channel is symmetric, the new posterior vector is p'=u+(p-u)/2=(1/6,1/6,1/6)+p/2, with the same marginal posterior-orbit mixing probabilities. At threshold t=1/5 the orbit payoff is

    H'_{O(p)}(1/5)=(1/4)sum_{i<j}
       (|p_i-p_j|-(1/5)(2/3+p_i+p_j))_+.

The seven orbit values, in the order (0,0,1), (0,1/6,5/6), (0,1/3,2/3), (0,1/2,1/2), (1/6,1/6,2/3), (1/6,1/3,1/2), uniform, are respectively

    1/3, 13/60, 2/15, 2/15, 1/10, 1/60, 0.

Consequently

    H'_mu(1/5)=(2/5)(13/60)+(1/25)(2/15)
                +(2/5)(2/15)+(4/25)(1/60)=37/250,
    H'_nu(1/5)=(2/5)(1/3)+(2/5)(1/10)=13/75,
    H'_mu(1/5)-H'_nu(1/5)=-19/750<0.

The binary Blackwell ordering is therefore destroyed by a common positive Potts edge, despite full symmetry and despite the fact that the pre-edge ordering held for every pair of states. This rules out the naive induction on pairwise binary Blackwell dominance in the class of all symmetric posterior experiments. It does not rule out a stronger order involving the complete q-state experiment, nor an order restricted to the smaller family actually generated by Potts broadcast trees. Some of the constructed posterior vectors have zero coordinates; finite positive-channel descendant observations have positive likelihood for every root label, so these mixtures are not being claimed to be finite pure Potts descendant experiments.

`edge_order_search.py` used a small linear program to propose weights on seven rational orbits, then independently checked all pre-edge inequalities and the negative post-edge payoff using exact Fractions. The proof above supplies the full analytical certificate; `edge_order_witness.json` preserves the data. The floating-point LP is used only for discovery, never as proof.

## Verification and hostile-referee audit

1. **Binary prior versus q-uniform prior.** The comparison uses equal priors on root labels 1 and 2. A q-uniform posterior orbit is converted to that binary prior using marginal factor (q/2)(p1+p2). Omitting this weighting gives incorrect Blackwell payoffs. The orbit formula and direct likelihood enumeration independently agree.
2. **Garbling versus TV.** A single negative convex payoff excludes binary Blackwell dominance even if total variation increases. Neither auxiliary counterexample is asserted to reverse reconstruction or finite-tree TV. For the edge-composition example, TV scales exactly by the edge eigenvalue, so its positive TV difference after the edge is expected and consistent with the failed Blackwell order.
3. **Finite criterion.** The coupling/garbling proof includes the finite linear separation argument and both conditional root laws; it does not infer a common kernel from agreement at t=0 alone. Full knot comparison is used.
4. **Changing q.** The q-independent partition prior in the first counterexample is an arbitrary distribution, and lacks the all-open event required by any positive-channel finite tree. The second counterexample uses the same q=3 on both sides. Neither is a source-model counterexample.
5. **Closure.** Coordinate symmetry of the orbit mixtures is explicitly proved, and the pre-edge comparison holds for every pair by permutation invariance. Thus merely adding pairwise symmetry does not repair the generic edge-closure problem. Whether the smaller family of actual broadcast-tree posterior laws admits a stable comparison remains open.
6. **Branch formula.** All nonneutral observation multiplicities are counted, and the root marginal factor 1/2 is included in w_E,w_D. For q=2 the D1/D2 multiplicity is zero. The neutral observations have zero payoff and are legitimately omitted, rather than discarded before normalization.
7. **Derivative signs and thresholds.** The low-tail certificate uses c<=s/2, equivalent to q>=2, and eta in [0,1], equivalent to t<=z_D. The high-tail estimate uses t>=z_D. The third region is identically zero. Continuity and finitely many crossings justify patching the derivative arguments. Both alpha and beta are restricted to (0,1), so h and the strict derivative denominators stay positive; no boundary extensions are claimed without a separate argument.
8. **Independent verification.** `validate_second.py` directly integrates each unobserved child state and checks 63 heterogeneous branch laws, 54 adjacent-alphabet full stop-loss comparisons, and one three-branch heterogeneous tree comparison. It independently generates cluster colors for the partition witness, reproducing -167/5032800 and its TV values, and uses the analytical orbit formula to reproduce all seven pre-edge checks and -19/750 after the edge. All checks use exact Fractions or exact symbolic identities. No LP tolerance or Monte Carlo result is promoted to a proof.
9. **Formal scope.** `BlackwellAlgebra.lean` contains four polynomial identity certificates: branch-ratio ordering numerator, informative mass, low-tail derivative decomposition, and high-tail derivative bound numerator. The complete file passed `lake env lean` from `~/lean_verify`, exit 0, in about 245 seconds. No sorry or native_decide is present. Convex-order existence, inequalities, probabilistic experiment statements and the full conjecture are not formalized.
10. **Finite tree search.** `blackwell_checks.py` additionally checked 43 adjacent-alphabet Blackwell comparisons for actual homogeneous finite trees: b=2,depth=2,q=2,...,8 at five lambda values; b=2,depth=3,q=2,...,5 at lambda=1/2,3/5,2/3; b=3,depth=2,q=2,3,4 at lambda=1/3,1/2. Every comparison checked all combined knots with exact arithmetic and all passed. This is numerical evidence for the proposed true-tree comparison, not a proof at arbitrary depths.

## Remaining gap and outcome

Approach 1 produced a stronger finite-tree comparison theorem and two exact obstructions to generalizing it by a generic cluster-coloring or pairwise-binary induction argument. It did not produce a proof or counterexample to F0118. Approach 2 was written down but was not pursued after the first route yielded these results.

The unclosed task is to compare the **actual Potts broadcast-generated** posterior experiments for arbitrary depths, or their limiting nontrivial posterior laws, for nondivisible alphabets in the below-KS range left in ATTEMPT.md. A successful induction must control the full conditional laws entering the uniform reset mixture, or prove an additional property of the BP-generated class that excludes the symmetric edge-order counterexample. Pairwise binary Blackwell dominance over the class of all symmetric experiments is not stable enough. The original infinite-depth remaining gap is otherwise unchanged. Verdict: PARTIAL. No novelty claim is made for the finite theorem or the auxiliary counterexamples.

Final targeted checks: `targeted_blackwell.py` additionally compared q=5 versus q=6 on the binary tree at depth three for lambda=13/20 and 7/10. Both complete exact stop-loss comparisons passed, giving 45 new true-tree comparisons in total. Both eigenvalues are strictly below 1/sqrt(2). These finite checks do not certify reconstruction or non-reconstruction.

Final TV-only follow-up: `partition_tv_search.py` sampled 40,000 random rational partition priors (seed 11803) with three to five observed vertices for q=3 to 4 and q=4 to 5. No pairwise-TV reversal was found. Every sign was computed by integer cross-multiplication. The soft 20-second sampling limit was exceeded by the final likelihood-matrix construction; actual wall time was about 53 seconds. This negative bounded search leaves the weaker arbitrary-partition TV comparison unresolved and does not turn the Blackwell counterexample into a TV counterexample.
