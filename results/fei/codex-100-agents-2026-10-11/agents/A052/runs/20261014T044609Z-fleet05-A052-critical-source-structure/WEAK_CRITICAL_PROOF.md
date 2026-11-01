# Critical weak-influence localization and the exact singleton Gibbs bank

All cubes are finite and uniform; f is a Boolean sign; entropy is in bits. Write kappa=2/ln(2). A physical singleton i has influence d_i, decrement L_i=H(f)-E H(f restricted at i), and minority Fourier mass beta_i. Its Fourier pairs are (a_t,b_t), q_t=a_t^2+b_t^2, e_t=min(a_t^2,b_t^2)/q_t, and c_t=4e_t(1-e_t); zero rows omitted. Put O_i=d_i-beta_i. The actual physical row transfer is j(c_t), and

    L_i=sum_t q_t[h2(e_t)+j(c_t)],
    j(c_t)<=kappa e_t, beta_i=sum_t q_t e_t.

The latter scalar inequality is independently reconstructed in the previous stage's A055 review. It does not require FEI or criticality.

## 1. Restriction forced by physical descendant ratio criticality

Suppose every physical child has ratio at most R=H(f)/I(f), with constants treated by zero deficit. Then the exact child identity implies R d_i<=L_i for every coordinate. This hypothesis is weaker than least-dimension threshold criticality: it needs no permission to use virtual Boolean phases.

Conditional entropy is at most the marginal entropy, so B_i<=h2(d_i). Also J_i<=kappa beta_i<=kappa d_i. For d_i>0,

    R<=h2(d_i)/d_i+kappa
      <log2(1/d_i)+1/ln(2)+kappa.

The strict inequality follows from -(1-d)ln(1-d)<d for 0<d<1, by integrating 1/(1-x) or differentiating. At d=1, L_i=0, so positive R is impossible under criticality. Since kappa+1/ln(2)=3/ln(2),

    max_i Inf_i(f)< exp(3) * 2^(-R)                 (1)

for every positive-ratio physically descendant-critical source. Only relevant coordinates need be considered. For a least-essential-dimension FEI(K) violation, D=H-KI>0, actual S_i=-E D_K(child)>=0, and

    K d_i+D+S_i=L_i.

The same argument yields d_i<exp(3)*2^-K. In particular a candidate with a healthy coordinate d_i>=tau cannot be minimal at K>=log2(exp(3)/tau). This applies to every source, not merely near-code perturbations. It explains why root-only weak-influence admissions still require child eligibility; they do not satisfy the premise automatically.

For K>kappa an exact sharper implicit endpoint d_K is the unique d in(0,1) satisfying h2(d)/d=K-kappa. The ratio h2(d)/d is strictly decreasing, because its derivative is log2(1-d)/d^2<0, and ranges from infinity to0. Hence d_i<=d_K, with strictness at a threshold violation. Equation(1) is a convenient explicit relaxation, not a claimed sharp Boolean constant.

## 2. Exact Gibbs decomposition of the retained bank

Fix any real K and any lambda>=kappa. Set

    rho=(1+2^(K-lambda))^-1, r=log2(1+2^(lambda-K)),
    Lambda_i=sum_t q_t KL_2(Ber(e_t)||Ber(rho)),
    A_i=sum_t q_t[lambda e_t-j(c_t)].

Both Lambda_i and A_i are nonnegative. The scalar Gibbs identity is exactly

    h2(e)-(K-lambda)e=r-KL_2(Ber(e)||Ber(rho)).

Multiply by q_t and sum; retain D_K(f) and the ACTUAL signed child reserve S_i=-E D_K(child). Then

    D_K(f)+S_i+K O_i+Lambda_i+A_i=r.              (2)

This identity holds on arbitrary roots, whose S_i need not be nonnegative. At lambda=kappa it restores the two discarded costs in A055's reviewed scalar bank: minority-row heterogeneity and the row recentring slack. It introduces no new influence budget. On a genuine minimal K-violation, K>=0,

    Lambda_i+A_i <= r-D-S_i-K O_i < r.           (3)

For actual ratio-critical sources use K=R, D=0, S_i>=0. Every child is retained in the same identity.

For u>=rho, binary KL(e||rho) is increasing in e on[u,1]. Thus the q-weighted mass m_i(u) of rows e_t>=u obeys

    m_i(u)[r+(K-lambda)u-h2(u)]
        <= Lambda_i <= r-D-S_i-K O_i.           (4)

Use (4) only where u>rho so its bracket is positive; the case u=rho gives no nontrivial tail bound. For fixed u>0 and large K, r=O(2^-K) and the bracket grows linearly in K. This forces genuinely ambiguous singleton rows to have weighted mass O(2^-K/K). Counting nonzero spectral support is not a substitute for this weighted restriction.

The finite checker uses lambda=3, justified by ln2>2/3 and kappa<3. At integer K all rho,r and KL log arguments are rational, so the exact bank and its tail bound are checked without approximating a transcendental exponent. The sharper lambda=kappa formula is analytic.

## 3. Compatible whole-pair reference and one reserve owner

Use the SAME rho and lambda on coordinates i,j. For retained index t avoiding both, let nu_t be the actual four-atom squared Fourier law on the pair. Define

    G_ij=sum_t q_t KL_2(nu_t || Ber(rho) tensor Ber(rho)),
    Z_ij=I(S_i;S_j | S_rest)>=0.

These are normalized complete references, including all four atoms. No unknown row-dependent normalizer is omitted. When a singleton conditional row has inclusion probability p>1/2, replacing p by its minority e=1-p changes KL to Ber(rho) by

    KL(Ber(p)||Ber(rho))-KL(Ber(1-p)||Ber(rho))
        =(2p-1) log2((1-rho)/rho)=(K-lambda)(2p-1).

Its weighted excess is exactly O_i. The conditional KL chain rule on the four-atom row therefore gives

    Lambda_i+Lambda_j+(K-lambda)(O_i+O_j)
        =G_ij+Z_ij.                              (5)

For clarity the sum of the two actual conditional KLs equals the joint KL plus mutual information: expand each entropy and use H(i|j)+H(j|i)=H(i,j)-I(i;j). Weight by retained row masses. There is no hypothesis of zero orientation and no inconsistent choice of conditional reflections.

Add the two exact singleton banks and substitute(5):

    2D+S_i+S_j+lambda(O_i+O_j)
        +G_ij+Z_ij+A_i+A_j=2r.                  (6)

On a minimal K-witness with K>=0 and lambda>=kappa, every term displayed in(6) is nonnegative. In particular G_ij+Z_ij<=2r-2D-S_i-S_j, a reserve-relative row statement. This is an exact allocation identity, not permission to spend r separately at both singleton nodes.

The whole-pair physical bank has a second exact form. The normalized Gibbs identity gives

    G_ij=2r-B_ij+(K-lambda)I_ij.

Use D+S_ij=B_ij+J_ij-KI_ij to obtain

    D+S_ij+G_ij+(lambda I_ij-J_ij)=2r.           (7)

The final term is nonnegative by the actual block log-Sobolev bound J_ij<=kappa I_ij<=lambda I_ij. This bank uses the pair queried influence once, preserves ALL four physical children, and retains the full product-reference KL. More generally (7) holds for a queried block of a coordinates with 2r replaced by ar and its product reference on all 2^a atoms. Selecting a block where the signed collision remainder is affordable relative to this exact bank remains unproved.

For completeness the block bound has an elementary reconstruction. With natural-log Ent(g)=E[g ln(g/Eg)], product entropy tensorization gives Ent(g)<=sum_i E Ent_i(g). Normalize Eg=1 and view 2^-a g as a probability law; the inequality is H(P)>=sum_i H_P(X_i|X_others), which follows by conditioning each chain-rule term on additional coordinates. On one bit, Ent((s,t)^2)<=(s-t)^2/2. Replace s,t by absolute values, normalize their mean square to1 and write the squares as1+u,1-u. The difference of the right side and left side has derivative u/sqrt(1-u^2)-artanh(u), nonnegative because its derivative is (1-u^2)^(-3/2)-(1-u^2)^(-1)>=0; endpoints follow by continuity. Tensorize this estimate on each real physical Fourier row w_t and use Walsh Parseval to obtain (ln2)J_A<=2sum_t sum_i E(D_i w_t)^2=2I_A. Thus the all-block assertion does not depend on an unreviewed semigroup theorem.

## 4. Consequences for all pair channels

The previous signed-pair proof and reviewed A051 bound give C_ij<=6(Inf_i+Inf_j), where C is weighted squared-density collision. Therefore every proper pair of a minimal high-K violation satisfies

    C_ij<12 exp(3)*2^-K.                        (8)

This is absolute smallness derived from genuine criticality, not a cheap-root embedding. It locates all candidate pairs in a near-isospectral regime at high K, but D and all child reserves can also be exponentially small. Equations(2)--(4) give the missing conditional-row weights explicitly and should be retained when comparing the signed parity-minus-refund bill with D+S_pair and the phase margin.

No uniform selected-pair contradiction follows from(1) or(8). Arbitrary weak-influence functions remain FEI-hard through activation, but the new premise is actual descendant criticality. Conversely this premise has not been proved to make the available budgets sufficient. The first unsupported line is an inequality comparing a selected joint signed residual with the SAME positive root/child bank after its Gibbs costs have been retained, rather than upper bounding both by an absolute exponential scale.
