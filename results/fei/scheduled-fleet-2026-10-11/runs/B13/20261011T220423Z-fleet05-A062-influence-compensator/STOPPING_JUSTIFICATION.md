# Stopping and dimension limits

The complete finite-tree proof is FAIR_TREE_INFLUENCE_PROCESS.tex. It gives the same physical stopping tree for entropy and influence, with the actual leaf terms. No external optional-stopping result is needed for the finite proof.

For one fixed finite-dimensional function, randomized selection is allowed only through randomness independent of the physical input and decisions measurable from already revealed history. Conditioning on the full auxiliary seed preserves the fair unrevealed cube. An infinite expected wall-clock stopping time is harmless: there are at most n fresh input reveals. Influence, entropy and their cumulative compensators have deterministic dimension-dependent bounds, so truncation followed by bounded convergence is valid. No all-dimensional inference follows from these bounds.

For a genuinely unbounded process with finite initial expected influence, nonnegative query costs imply that their cumulative sum is integrable by monotone convergence. Residual influence is a nonnegative supermartingale, so it converges almost surely. Without uniform integrability, Fatou proves only the inequality E(sum costs)+E(lim residual influence)<=E(initial influence). Equality requires a residual tail condition, such as lim_{K->infinity} sup_m E[I_{tau wedge m} 1_{I_{tau wedge m}>K}]=0. Entropy requires its own condition; paying influence does not prove entropy continuity without an additional theorem.

# Actual Boolean obstruction to dimension-uniform passage

Let k>=1, m=2^k+1, and use m independent data signs. Define

g_k(y)=y_0 product_{j=1}^{2^{k-1}} (-1)^{b_{2j-1} b_{2j}},

where b_i=(1-y_i)/2. The leading sign balances g_k. Each quadratic two-bit factor has four Fourier coefficients of magnitude 1/2; consequently H(g_k)=2^k and I(g_k)=2^{k-1}+1 exactly. Let A_k be the indicator that k independent control signs all equal +1 and let p_k=2^{-k}. The function F_k=1+A_k(g_k-1) is an actual Boolean function.

Reveal the controls in order and stop as soon as one is negative; after k positive controls, stop at g_k without revealing data. Every terminal leaf is either +1 or g_k. On the common probability space of an infinite fair control sequence,

I(leaf_k)=(2^{k-1}+1) 1_{A_k},
H(leaf_k)=2^k 1_{A_k}.

Both random variables converge to zero almost surely, since almost every control sequence has a first negative sign. Nevertheless E I(leaf_k)=1/2+2^{-k}->1/2 and E H(leaf_k)=1 for every k. These terminal families are not uniformly integrable: for every K, choose k so the positive value exceeds K; their expected tail masses stay at least 1/2 and 1.

The root influences are uniformly bounded and explicitly

I(F_k)=p_k[I(g_k)+k]=1/2+(k+1)2^{-k}<=3/2.

Each of the k controls has influence p_k at the root. At a node with r preceding positives it has influence 2^r p_k and reach probability 2^{-r}. Thus the total expected queried influence is k p_k. The exact finite identity is

I(F_k)=k p_k+(1/2+p_k).

The right terminal term cannot be replaced by the expectation of the almost-sure limit. In fact k p_k->0, while I(F_k)->1/2. Likewise the exact activation entropy is

H(F_k)=1+2 k p_k(2-p_k)+(1-p_k)^2 log_2[1/(1-p_k)^2],

which tends to 1. Its expected accumulated entropy drop tends to zero, and its terminal expected entropy is 1; replacing the latter by the entropy of the limiting constant leaf would lose one bit. This is a dimension-limit counterexample, not a failure of optional stopping for any fixed F_k. The functions even converge physically to +1 almost surely on the coupled cube. Neither influence nor spectral entropy is continuous under that convergence with only the stated bounded root budgets.

This example uses the threshold paper's balanced activation identities (38pp, Proposition 8.9) and also has a direct derivation: nonempty data coefficients are p_k times the coefficients of g_k in every control sector; empty-data nonempty-control coefficients are -p_k; the all-empty coefficient is 1-p_k. Summing their squared masses and degrees gives the displayed formulas. It is a stress test of interchange of limits, not an FEI counterfamily: its H/I tends to 2.

# Pathwise spending is different from expected spending

The three-bit function F(z,y_1,y_2)=1 when z=-1 and y_1 y_2 when z=+1 has I(F)=3/2. Its two children have influences 0 and 2. Thus the positive child already has more residual influence than the root. The cumulative influence compensator is a martingale in expectation; there is no claim that the influence decreases on every branch or that root influence is a deterministic pathwise wallet.

For A064's debt accounting, any tail argument must keep both the physical history weight and the terminal reserve. This family gives a small, exact obstruction to replacing expected terminal reserve by a pointwise limit across increasing dimensions.
