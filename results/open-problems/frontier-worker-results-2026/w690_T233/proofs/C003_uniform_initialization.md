# C003 working: uniform Gaussian initialization at width proportional to depth

Kind bound, target 1. Initialization component only; NOT a GD convergence theorem. Author codex-w690. Two checked routes: endpoint Gram martingales, and interval conditional expectations with two Doob inequalities. The first is proved in T1_endpoint_gram_working.md; this file derives the all-block estimate and locates the remaining training gap.

## Uniform hidden-block bound without a depth union bound

Let B_1,...,B_n be independent m by m matrices with iid N(0,1/m) entries. They represent just the hidden square layers (n=L-2). Put Z=||B_n ... B_1||_F^2. For every 1<=i<=j<=n,

    E[Z | B_i,...,B_j] = ||B_j ... B_i||_F^2.                 (1)

Indeed integrating the outer left factors uses E[B^T B]=I; integrating outer right factors uses E[B B^T]=I. The independence makes both integrations valid even conditional on the middle block.

Let A_j be conditional expectation on B_1,...,B_j and C_i conditional expectation on B_i,...,B_n. These expectation operators commute: for independent coordinates their composition is expectation on the common coordinates, namely the interval i,...,j when i<=j (and the trivial sigma field otherwise). Thus (1) is A_j C_i Z.

Let M=max_i C_i Z. Positivity gives A_j C_i Z<=A_j M, so

    max_(i<=j) ||B_j ... B_i||_F^2 <= max_j A_j M.
    ||max_j A_j M||_(L^2) <= 2||M||_(L^2) <= 4||Z||_(L^2).  (2)

Both inequalities are ordinary finite-horizon Doob L^2 maximal inequalities: C_i exposes the coordinates backwards and A_j exposes them forwards. They do not require the two filtrations to be independent, only the commuting identity used above. The general probability space can include other independent layers without changing the calculation.

For a deterministic positive semidefinite Q, independent Gaussian B=G/sqrt(m) gives

    E[(tr BQB^T)^2 | Q]=(tr Q)^2+(2/m)tr(Q^2).              (3)

This follows by writing tr BQB^T as m independent Gaussian quadratic forms divided by m. Their means are tr Q and variances 2tr(Q^2). Since tr(Q^2)<=(tr Q)^2, iteration from Q_0=I_m yields

    E[Z^2] <= m^2 (1+2/m)^n <= m^2 exp(2n/m).              (4)

Combining (2)-(4) with Markov, for any 0<delta_b<1, with probability >=1-delta_b,

    max_(i<=j) ||B_j ... B_i||_F^2
        <= 4m exp(n/m)/sqrt(delta_b).

Consequently every hidden block, simultaneously, has operator norm at most

    K=2 sqrt(m) exp(n/(2m)) delta_b^(-1/4).                 (5)

No factor counting the blocks or depth appears in the probability. Include empty blocks by increasing K to at least 1 (the displayed K already is >=2). For n=0 there is no nonempty block.

At m=cL, K=O_(c,delta_b)(sqrt(L)). This is an upper bound, not a claim that every block is close to an isometry.

## Initialization package

Combine (5), with delta_b=delta/2, and the endpoint lemma with zeta=delta/8. With probability >=1-delta, all endpoint Grams have constant lower/upper bounds depending only on c,r,d_y,delta and every hidden block has operator norm O_(c,delta)(sqrt(L)). The initial output kernel consequently has spectrum between positive c-dependent multiples of L sigma_min(X)^2 and L||X||^2/d_y, as stated precisely in the endpoint note.

This recovers the types of initialization inputs in Du-Hu Eq. (12) at every fixed m=cL, with c-dependent distortion instead of their fixed near-isometry constants and with no union bound costing log L. It does not establish their induction B(t) at t>0.

## Reading Du-Hu at the actual trajectory failure

Source inspected directly: https://arxiv.org/pdf/1901.08572, printed pp.7-8, Section 7.1 and 7.2, Claims 7.1 and 7.2, especially Eqs. (15)-(19). Their C(t) is

    max_i ||W_i(t)-W_i(0)||_F <= R_W = D/L,

where D=24sqrt(B d_y)||X||/sigma_min(X)^2 under their original near-isometry constants. The residual geometric series in Claim 7.1 cancels eta exactly.

The same issue remains with arbitrary fixed endpoint constants. Suppose, conditionally on a proposed induction, all normalized prefix/suffix singular values are in [s,M], s>0. Then the initial-style kernel lower coefficient is gamma=s^4 sigma_min(X)^2/d_y. A geometric loss bound loss_t<=B(1-eta gamma L)^t and 0<eta gamma L<=1 imply

    ||grad_(W_i) loss_t||_F <= g sqrt(loss_t),
    g=M^2 ||X|| sqrt(2/d_y),
    sum_t eta ||grad_(W_i) loss_t||_F
        <= 2g sqrt(B)/(gamma L) = D/L.                    (6)

Use 1-sqrt(1-x)>=x/2. Again eta disappears, so reducing eta alone does not improve this full-run drift certificate.

Set delta_A=R_W/sqrt(m), since B_i=W_i/sqrt(m). The product expansion in their Claim 7.2 has budget

    theta=L K delta_A=K D/sqrt(m).                         (7)

For the valid all-block bound (5), this certificate becomes

    theta <= 2D exp(n/(2m)) delta_b^(-1/4).                (8)

Here theta using the actual maximum block norm might be smaller; (8) is an upper certificate, not a lower bound on actual movement or a Gaussian counterexample. It has no vanishing factor in L or eta at m=cL. Endpoint perturbations can be bounded by M_0[(1+K delta_A)^L-1]<=M_0(exp(theta)-1), where M_0 bounds the relevant initial endpoint factors. This only preserves a positive singular-value margin when the constants meet an additional smallness inequality. Neither increasing L nor decreasing eta forces that inequality.

Thus this route removes an initialization union bound, but cannot assert arbitrary-c convergence by transplanting Du-Hu's deterministic neighborhood induction. The needed new statement concerns the actual GD trajectory or sharper structure of its perturbations. No alleged impossibility for GD, no repeated width experiment, and no target-1 solution are claimed.

## Independent checks

The q=1 inverse-Gram identity in the endpoint note reduces to the product of inverse chi-square means m/(m-2), agreeing with its rho_q. The full-block moment calculation can also be checked via the exact coupled recurrences a_(k+1)=a_k+2b_k/m and b_(k+1)=(1+1/m)b_k+a_k/m, where a=E(tr Q)^2 and b=E tr(Q^2), initially a=m^2,b=m. A short arithmetic check accompanies the final claim. No training simulation is used.

## Self-contained L2 maximal inequality used above

For a nonnegative finite martingale with terminal Y and maximum M*, stopping at its first crossing of lambda gives lambda Pr(M*>=lambda)<=E[Y 1_(M*>=lambda)]. Integrate 2 times this inequality over lambda to get E[(M*)^2]<=2 E[Y M*]<=2||Y||_2||M*||_2. Hence ||M*||_2<=2||Y||_2. Finite Gaussian moments justify all uses here.

Review status: C003v1 all-block lemma independently ACCEPTED by an agent; endpoint note was not re-derived in that review and is separately pending as C004v1. No acceptance of a trajectory or convergence claim is implied.
