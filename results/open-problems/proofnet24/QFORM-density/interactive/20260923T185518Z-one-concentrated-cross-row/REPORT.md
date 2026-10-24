# One concentrated cross row with a diffuse rank-two remainder

**Status:** Complete conditional theorem. The unrestricted three-eigenvalue conjecture remains open. This note uses only independent original coordinates; no projected variables are declared independent. It permits arbitrary quadratic self blocks, affine terms, and conditioning on all coordinates outside the selected physical cut.

## Theorem

Let `I,J` be disjoint sets of original coordinate indices, let `M=A[I,J]`, and fix `h in I`. Write `M0=M[I\{h},J]`. For `k=2,3` and a rectangular matrix `B`, set

`Z_k(B)=e_k(B^T B)=sum_{|S|=|T|=k}det(B[S,T])^2`.

When `Z_k(B)>0`, assign each pair `(S,T)` of row and column `k`-subsets probability `det(B[S,T])^2/Z_k(B)`. Let `alpha_i^(k)(B)` denote the resulting row-inclusion probability. Suppose

1. `Z_3(M)>0` and `alpha_i^(3)(M)<=1/2` for every `i in I\{h}`; no restriction is imposed on `alpha_h^(3)(M)`;
2. `Z_2(M0)>0` and `alpha_i^(2)(M0)<=1/2` for every row of `M0`.

For independent real `X_i` with probability densities bounded by one and every real quadratic-plus-affine form `Q(X)=X^TAX+b^TX+c`, the law of `Q` has a continuous density vanishing at infinity and

`||p_Q||_infinity <= 10 sqrt(e) [Z_3(M) Z_2(M0)]^(-1/10).`         (1)

The same result holds for any `F(X_I)+2 X_I^T M X_J+G(X_J)` with arbitrary measurable real phases `F,G`; coordinates outside `I∪J` may be conditioned on if their conditional contributions have this form.

## Product-source decoupling

Condition on the outside coordinates and absorb their contributions into `F,G`. Write `Y=X_J`. If `psi_i` is the characteristic function of `X_i`, Cauchy–Schwarz in the independent vector `X_I` gives

`|phi_Q(t)|^2 <= E_{D=Y-Y'} prod_{i in I}|psi_i(2t(MD)_i)|`.     (2)

Indeed the `F` phase disappears after Cauchy–Schwarz, and expanding the square over independent `Y,Y'` makes the `G(Y)-G(Y')` factor have modulus one. Each `D_j` is independent and has probability density `g_j=f_j*tilde f_j<=1`. No conditional law of a transformed coordinate is used.

Set `H(D)=|psi_h(2t(MD)_h)|` and `L(D)=prod_{i≠h}|psi_i(2t(MD)_i)|`. Weighted Cauchy–Schwarz in the same `D` law yields

`E(HL) <= [E(H^2 L)]^(1/2)[E L]^(1/2)`.                    (3)

The factors on the right use, respectively, all three cross dimensions with the concentrated row squared, and two cross dimensions after that row is deleted.

## Mixed Fourier-power volume bound

For an `r×d` matrix `B` and `Z_k(B)>0`, let `alpha_i,beta_j` be the row and column marginals of its squared-`k`-minor weights. Thus `sum alpha_i=sum beta_j=k`. For nonnegative row multiplicities `m_i>=1` such that `alpha_i<=m_i/2`,

`E_D prod_i |psi_i(2t(BD)_i)|^{m_i}
 <= e^{k/2}(2pi)^k |t|^{-k} Z_k(B)^(-1/2),   t≠0`.            (4)

Here the coordinate laws defining the `psi_i` and the independent difference variables `D_j` may come from different groups of cap-one original coordinates.

To prove (4), let `d_i,e_j>0` be Gaussian parameters. Expanding the determinant in principal minors, then applying Cauchy–Binet and weighted AM–GM with weights `det(B[S,T])^2/Z_k`, gives

`det(diag(e)+B^T diag(d) B)
 >= sum_{|S|=|T|=k}det(B[S,T])^2 prod_{i in S}d_i prod_{j notin T}e_j
 >= Z_k(B) prod_i d_i^{alpha_i} prod_j e_j^{1-beta_j}`.    (5)

Lieb's Gaussian characterization of the Brascamp–Lieb constant for the row maps `y↦(By)_i` with exponents `alpha_i` and column maps `y↦y_j` with exponents `1-beta_j` therefore bounds it by

`Z_k(B)^(-1/2) prod_i alpha_i^(-alpha_i/2)
                  prod_j (1-beta_j)^(-(1-beta_j)/2)`.       (6)

Terms with zero exponent are omitted; endpoints follow by continuity of the Gaussian parameters. The one-dimensional Fourier estimate for a probability density `f<=1` is

`int_R |hat f(u)|^p du <= 4pi/sqrt(p),    p>=2`.              (7)

For completeness, this follows directly from the sharp Hausdorff–Young inequality of Beckner (`Inequalities in Fourier analysis`, *Ann. of Math.* 102 (1975), 159–182): with `r=p/(p-1)`, `||f||_r<=1` because `f<=1` and `int f=1`, and the sharp inequality in the present Fourier convention gives

`int |hat f|^p <= 2pi r^((p-1)/2) p^(-1/2)
                 <= 2pi sqrt(e/p) < 4pi/sqrt(p)`.

Apply (7) with `p=m_i/alpha_i>=2`. For a row input `u↦|psi_i(2tu)|^{m_i}`, its `L^{1/alpha_i}` norm is at most

`[(2pi/|t|) sqrt(alpha_i/m_i)]^{alpha_i}`.                  (8)

The factors `alpha_i^{alpha_i/2}` cancel (6); `m_i^{-alpha_i/2}<=1`. The column inputs satisfy `||g_j||_{1/(1-beta_j)}<=1` because `g_j<=1` and `int g_j=1`. Finally `prod_j(1-beta_j)^(-(1-beta_j)/2)<=e^{k/2}` by `-(1-x)log(1-x)<=x`, proving (4). The case `alpha_i=0` simply drops that bounded row factor; the case `beta_j=1` drops the bounded column factor and takes the determinant limit with its Gaussian column parameter zero.

Use (4) for `B=M,k=3,m_h=2,m_i=1` otherwise. The hypotheses imply `m_i/alpha_i>=2`, including `alpha_h<=1`, so

`E(H^2 L) <= e^(3/2)(2pi)^3 |t|^-3 Z_3(M)^(-1/2)`.         (9)

Use (4) for `B=M0,k=2,m_i=1` to obtain

`E L <= e(2pi)^2 |t|^-2 Z_2(M0)^(-1/2)`.                     (10)

Equations (2), (3), (9), and (10) imply

`|phi_Q(t)| <= min{1, e^(5/8)(2pi)^(5/4)|t|^(-5/4)
                         [Z_3(M)Z_2(M0)]^(-1/8)}`.        (11)

The envelope is integrable. For `b=5/4`, `int_R min(1,K|t|^-b)dt=10K^(4/5)`. Fourier inversion turns (11) into (1), since `(10/(2pi))[e^(5/8)(2pi)^(5/4)]^(4/5)=10sqrt(e)`. Integrability also gives a continuous density vanishing at infinity. The conditional bound is uniform in the outside variables, so averaging proves the result for the full quadratic form.

## Exact rank-three no-pivot example

Fix `m>=2`. Take mutually disjoint physical sets `I={h}∪I_1∪I_2`, `J={j}∪J_1∪J_2` with each `I_l,J_l` of size `m`. Write `u_l,v_l` for normalized all-ones vectors on `I_l,J_l`, respectively. Let

`M=e_h v_1^T +u_1 e_j^T+u_2 v_2^T`.                         (12)

Its three nonzero singular values are exactly `1,1,1`, so `Z_3(M)=1`; deleting `h` leaves singular values `1,1`, so `Z_2(M0)=1`. The third-volume row marginal at `h` is `1`, while all other active row marginals are `1/m`; the second-volume row marginals of `M0` are also `1/m`. Hence (1) gives `||p_Q||∞<=10sqrt(e)` for arbitrary within-bank quadratic terms, despite both a concentrated row and a concentrated column.

For the pure cross matrix `A=[[0,M],[M^T,0]]`, the spectrum is `(+1,+1,+1,-1,-1,-1,0,...,0)`. Every physical diagonal is zero, and every `2×2` principal minor has magnitude at most `1/m`; choose `m` large to make all such pivots small. Swapping the cut fails the usual diffuse gate because the column `j` has volume marginal one. Thus (1) covers a target-valid, no-pivot configuration not certified by the single-side diffuse three-volume gate. The arbitrary same-bank terms in the theorem can couple the three channels and need no independence assumptions.

The theorem needs both nonzero volumes. A lone rank-one star has `Z_3=0` and is correctly outside its scope; its quadratic form `2HL` can have an unbounded density at zero. This note does not claim a structural reduction from three large eigenvalues to the theorem's hypotheses.

## Several concentrated rows: a general mixed-volume hierarchy

The same argument applies with a set `H` of `r` concentrated rows. Let `1<=r<k`, let `M0` result from deleting `H` from `M`, and suppose `Z_k(M)>0`, `Z_{k-r}(M0)>0`. Assume the `k`-volume row marginals of every row outside `H` are at most `1/2`, and the `(k-r)`-volume row marginals of every row of `M0` are at most `1/2`. The high rows have no leverage restriction. If `2k-r>4`, then

`||p_Q||_infinity
 <= [2sqrt(e)(2k-r)/(2k-r-4)]
    [Z_k(M) Z_{k-r}(M0)]^(-1/[2(2k-r)])`.                  (13)

The density is continuous and vanishes at infinity; arbitrary same-bank phases remain allowed. To see this, set `F=prod_{h in H}|psi_h(2t(MD)_h)|` and `G=prod_{i notin H}|psi_i(2t(MD)_i)|`. Equation (3) holds with this `F`. Apply (4) to `E F^2G` with full matrix `M`, row multiplicity two on `H`, one elsewhere, and to `E G` with `M0` and all row multiplicities one. Taking the two square roots as in (2) gives

`|phi_Q(t)| <= min{1,
 e^((2k-r)/8)(2pi)^((2k-r)/4) |t|^(-(2k-r)/4)
 [Z_k(M)Z_{k-r}(M0)]^(-1/8)}`.                          (14)

The decay exponent `(2k-r)/4` exceeds one exactly under the displayed condition. Integrating (14) gives (13). For `k=3,r=1`, this recovers (1). For `k=4,r=2`, it gives

`||p_Q||_infinity <=6sqrt(e)[Z_4(M)Z_2(M0)]^(-1/12)`.     (15)

For `k=3,r=2`, this particular Cauchy–Schwarz scheme yields only `|t|^-1`; it does not certify a bounded density in that case.
