# Target 1 working route: near-conserved balancedness

Route check exited 0. This is work in progress, not a GD convergence claim.

## Exact discrete identity

Let G_i(t)=partial loss/partial W_i, and D_i=W_(i+1)^T W_(i+1)-W_i W_i^T. The deep-linear gradient identities give

    W_(i+1)^T G_(i+1)=G_i W_i^T,
    G_(i+1)^T W_(i+1)=W_i G_i^T.

Expanding W_i^+=W_i-eta G_i therefore cancels the first-order terms:

    D_i(t+1)-D_i(t)
       =eta^2 [G_(i+1)^T G_(i+1)-G_i G_i^T].             (B1)

If a run has the sufficient-descent inequality
loss_(t+1)<=loss_t-(eta/2)sum_j ||G_j(t)||_F^2,
then for every T,

    ||D_i(T)-D_i(0)|| <=2 eta loss_0.                    (B2)

The descent assumption is explicit, and not proved for the full trajectory here. It can be enforced over any already-controlled region by an appropriate step. Formula (B2) is not being used circularly to claim global convergence. Continuous gradient flow conserves D_i exactly.

## Gaussian boundary margin: a polynomial witness

At the first hidden boundary write H=W_2^T W_2 and V=W_1, so D_1=H-VV^T. Assume d_x=q fixed, m grows, L>=3. H is square Wishart and independent of V. Put Q=H/m and X=(I-Q/4)V. Fixed-order Wishart moments and conditional Gaussian quadratic-form concentration give, with the exact coefficients independently checked below,

    V^T Q^k V /m -> C_k I_q,  k=0,1,2,3,
    (C_0,C_1,C_2,C_3)=(1,1,2,5).

Thus

    X^T X /m -> (1-1/2+2/16) I=(5/8)I,
    X^T H X /m^2 -> (1-4/4+5/16) I=(5/16)I,
    X^T V V^T X /m^2 -> (1-1/4)^2 I=(9/16)I,
    X^T D_1 X /m^2 -> -(1/4)I.

The limiting Rayleigh quotient on this q-dimensional subspace is -(2/5)m, so in particular D_1 has q eigenvalues <=-m/4 with probability tending to one. This requires a proof of the stated moment concentration, not a simulation or an appeal to a trained Gaussian law.

By transposition the final boundary D_(L-1)=W_L^T W_L-W_(L-1)W_(L-1)^T has d_y eigenvalues >=m/4 with probability tending to one. The two events need not be independent.

If these initial margins and (B2) hold, then Loewner order gives for all times covered by the descent assumption

    sigma_min(W_1(t))^2 >=m/4-2eta loss_0,
    sigma_min(W_L(t))^2 >=m/4-2eta loss_0.                (B3)

Indeed W_1 W_1^T=W_2^T W_2-D_1 >=-D_1 and W_L^T W_L=D_(L-1)+W_(L-1)W_(L-1)^T >=D_(L-1), followed by eigenvalue monotonicity. These are boundary layer bounds, not bounds on long prefixes or suffixes.

## Moment concentration proof

For Q=G^T G/m:
E tr H=m^2; E tr H^2=2m^3+m^2; E tr H^3=5m^4+6m^3+4m^2. These coefficients are verified by exact Wick pairing enumeration in scripts/check_balancedness.py, without random draws.

For fixed k, E tr Q^k=O(m): in a cyclic trace expansion each Wick pairing has at most k+1 free row/column indices (its quotient graph is connected with at most k edges). There are (2k-1)!! pairings.

For f_k=(1/m)tr Q^k, Gaussian Poincare and
||grad_G f_k||_F^2=(4k^2/m^3)tr Q^(2k-1)
give Var(f_k)=O(m^-2). Gaussian Poincare for polynomials follows from Hermite expansion: Var(f)=sum_(alpha!=0) c_alpha^2 alpha!, while E||grad f||^2=sum |alpha| c_alpha^2 alpha!.

Conditional on Q,
E ||V^T Q^k V/m - [(tr Q^k)/m] I_q||_F^2
  =q(q+1)tr Q^(2k)/m^2.
The fixed-order moment bound makes its expectation O(m^-1). The exact leading moments and witness algebra have been independently checked, so this proves the required convergence in probability. Thus the boundary singular-value margin statement above is proved under its explicit descent assumption. The balancedness identity itself is classical; no novelty is asserted for that identity.

## Remaining target-1 gap

Even hard bounds on W_1 and W_L do not protect W_i...W_1 X and W_L...W_(i+1) for interior i. Establishing a lower bound for the full trained output kernel requires more structure of the conserved imbalance tuple or the GD trajectory. Do not turn (B3) alone into a convergence claim.

Arithmetic audit completed: scripts/check_balancedness.py passes; logs/balancedness_check.json records all Wick coefficients, witness constants, and exact discrete identity at three boundaries. The concentration proof above now supplies the claimed convergence-in-probability boundary margin. No global sufficient-descent or long-product guarantee has been proved.

## Exact obstruction to retaining only coarse imbalance and boundary bounds

This concerns a universal auxiliary implication, NOT the Gaussian target and NOT the full conserved imbalance tuple. Fix L>=4 and any m>=2 (including m=floor(cL) for large L). In normalized coordinates B_i=W_i/sqrt(m), take e=e_1 and P=diag(0,1,...,1). Set

    B_1=2e, B_2=B_3=P,
    B_i=I_m for 4<=i<=L-1, B_L=2e^T.

Use scalar X=Y=1. Then B_L...B_1=0 and the loss is 1/2. For a layer i<=2 the backward suffix contains P killing e; for i>=3 the forward prefix contains P killing e. Therefore EVERY layer gradient is exactly zero. GD and gradient flow stay at this nonglobal stationary point.

Nevertheless the first and last layer squared singular values are 4m; every hidden block has operator norm <=1 in B coordinates; and every imbalance D_i has operator norm <=4m and is exactly conserved. Indeed D_1/m=diag(-4,1,...,1), D_2=0, and for L=4, D_3/m=diag(4,-1,...,-1). For L>=5 the next nonzero imbalance is I-P=diag(1,0,...,0), and the final D_(L-1)/m=diag(3,-1,...,-1); intervening imbalances vanish.

Thus bounds only on ||D_i|| and boundary singular values cannot imply a positive trained kernel lower bound or propagate noncollapse through long products. This chain has zero probability under Gaussian initialization and violates the good initial long endpoint-Gram event. It does not refute a theorem using that event plus the full conserved tuple, or a theorem about the actual Gaussian GD trajectory. The next proof must retain more than those coarse conditions.
