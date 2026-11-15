# C005 v1: Gaussian boundary margins and near-conserved GD balancedness

Kind: bound. Target: 1. Author codex-w690. Proposed for review.
This is a conditional trajectory component, not polynomial-time convergence.

## Statement

Use the dossier's Gaussian initialization, fixed input/output dimensions d_x,d_y, hidden width m, and L>=3. As m tends to infinity, with probability 1-o(1), simultaneously

    D_1(0) has d_x eigenvalues <=-m/4,
    D_(L-1)(0) has d_y eigenvalues >=m/4,

where D_i=W_(i+1)^T W_(i+1)-W_i W_i^T. The o(1) is uniform in L>=3: only the two boundary pairs are involved and a union bound needs no independence.

On this event, consider ANY constant-step GD run which satisfies, for every step under consideration,

    loss_(t+1) <= loss_t-(eta/2) sum_j ||grad_(W_j) loss_t||_F^2.    (C5.1)

Then simultaneously for every such time T,

    sigma_min(W_1(T))^2 >= m/4-2eta loss_0,
    sigma_min(W_L(T))^2 >= m/4-2eta loss_0.                        (C5.2)

Thus if eta loss_0<=m/16, both squared singular values are >=m/8. The first minimum is over d_x singular values and the last over d_y. For gradient flow the D_i are exactly conserved, so the m/4 boundary margins persist throughout its interval of existence.

The sufficient-descent condition (C5.1) is an explicit hypothesis, not a global conclusion proved here. These bounds do NOT protect long products or imply an output-kernel lower bound. No novelty is asserted for the classical balancedness identity.

## Exact discrete identity and its summation

Let G_i=grad_(W_i) loss. The chain gradient formula gives

    W_(i+1)^T G_(i+1)=G_i W_i^T,
    G_(i+1)^T W_(i+1)=W_i G_i^T.

Expanding W_i^+=W_i-eta G_i cancels the first-order terms, leaving exactly

    D_i(t+1)-D_i(t)=eta^2[G_(i+1)^T G_(i+1)-G_i G_i^T].            (C5.3)

Using (C5.1), nonnegative loss, and that each layer pair is a subset of all layers,

    ||D_i(T)-D_i(0)||
      <=eta^2 sum_(t<T)(||G_(i+1)||_F^2+||G_i||_F^2)
      <=eta^2 sum_(t<T)sum_j ||G_j||_F^2
      <=2eta loss_0.                                               (C5.4)

The same bound holds for every i, with no time or layer union bound. In continuous time the eta^2 term disappears.

## Gaussian boundary margin without a spectral-limit theorem

Consider D=H-VV^T with H=G^T G, where G is m by m iid standard Gaussian, V is an independent m by q iid standard Gaussian, and q is fixed. This has the distribution of D_1 for q=d_x. The negative of the final D has the same distribution after transposition, for q=d_y.

Put Q=H/m. For k=0,1,2,3 define A_k=V^T Q^k V/m. We first prove, in probability in fixed dimension q,

    A_0->I, A_1->I, A_2->2I, A_3->5I.                            (C5.5)

Exact Wick expansion gives

    E tr H=m^2,
    E tr H^2=2m^3+m^2,
    E tr H^3=5m^4+6m^3+4m^2.                                    (C5.6)

These coefficients were independently enumerated by all Gaussian pairings in scripts/check_balancedness.py; no random sampling was used. More generally, E tr Q^k<=(2k-1)!! m for any fixed positive integer k. In the cyclic trace expansion each pairing identifies a connected bipartite graph with at most k edges, hence at most k+1 free row/column indices; each summand is at most m^(k+1), before division by m^k.

For f_k=(1/m)tr Q^k, direct differentiation gives

    ||grad_G f_k||_F^2=(4k^2/m^3)tr Q^(2k-1).

Gaussian Poincare consequently gives Var(f_k)=O(m^-2). For completeness this inequality for the polynomial f follows from its finite multivariate Hermite expansion: Var(f)=sum_(a!=0)c_a^2 a!, whereas E||grad f||^2=sum_a |a|c_a^2 a!>=Var(f). Equations (C5.6) therefore imply f_k->1,2,5 for k=1,2,3.

Conditionally on Q, Gaussian second and fourth moments give

    E[||A_k-f_k I_q||_F^2 | Q]
       =q(q+1)tr Q^(2k)/m^2.

The fixed-order moment bound makes its expectation O(m^-1). This also handles k=0 with Q^0=I. Chebyshev/Markov establishes (C5.5).

Now choose the degree-one polynomial witness

    Z=(I-Q/4)V.

The preceding convergences give

    Z^T Z/m = A_0-A_1/2+A_2/16 -> (5/8)I,
    Z^T H Z/m^2 = A_1-A_2/2+A_3/16 -> (5/16)I,
    Z^T V V^T Z/m^2 = (A_0-A_1/4)^2 -> (9/16)I,
    Z^T D Z/m^2 -> -(1/4)I.

Thus Z is full rank with probability tending to one, and the largest Rayleigh quotient of D on col(Z), divided by m, tends to -2/5. In particular that entire q-dimensional subspace has quotient <=-m/4 with probability tending to one. Min-max gives the q negative eigenvalues claimed. Apply the transposed argument to the final boundary and use a union bound.

## From imbalance margins to boundary singular values

From (C5.4) and eigenvalue perturbation, D_1(T) retains d_x eigenvalues <=-m/4+2eta loss_0, and the final D retains d_y eigenvalues >=m/4-2eta loss_0. Since

    W_1 W_1^T = W_2^T W_2-D_1 >=-D_1,
    W_L^T W_L = D_(L-1)+W_(L-1)W_(L-1)^T >=D_(L-1),

Hermitian eigenvalue monotonicity gives (C5.2), including full boundary rank whenever the right side is positive.

## Why coarse imbalance bounds cannot finish target 1

Fix L>=4,m>=2, normalized B_i=W_i/sqrt(m), e=e_1 and P=diag(0,1,...,1). Take B_1=2e, B_2=B_3=P, B_i=I for 4<=i<=L-1, and B_L=2e^T. With scalar X=Y=1, the output is zero and loss is 1/2. Every gradient vanishes: for i<=2 the suffix kills e through B_3, while for i>=3 the prefix kills e through B_2.

Nevertheless both boundary squared singular values are 4m, every normalized hidden block has norm <=1, and all imbalances have norm <=4m and are exactly conserved by this stationary GD trajectory. Their diagonal entries are computed in T1_balancedness_working.md; exact finite-size checks are in logs/coarse_balance_witness_check.json.

This only refutes an auxiliary implication from conserved/bounded imbalance norms and full-rank boundary layers to a positive trained kernel. It is a deterministic zero-probability Gaussian initialization and violates the good initial long endpoint-Gram event. It does NOT refute target 1, nor a theorem using good Gaussian initialization plus the full conserved imbalance tuple.

The next actual trajectory argument must retain more joint information. Do not claim that (C5.2) alone proves GD convergence.
