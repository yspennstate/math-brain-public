# QFORM-RANK2-HEAVY-ROW-SCHUR-SLOPE-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T120107Z-account02-B14-QFORM-r35`  
Status: supporting target-level theorem; full conjecture open.

## 1. Statement

Let an original-coordinate invertible indefinite physical pair have coefficient block `C`; put

`D=|det C|`, `kappa=sigma_min(C)>0`.

After exact completion of that pair and conditioning only on arbitrary outside original coordinates, suppose a remaining independent product bank `V=(V_1,...,V_d)` has quadratic coefficient

`S_VV = Delta + R G R^T`,                                         (1.1)

where

- `Delta` is an arbitrary real diagonal matrix;
- `R` is a real `d x 2` matrix with orthonormal columns (`R^T R=I_2`);
- `G` is an arbitrary real symmetric invertible `2 x 2` matrix with `sigma_min(G)>=s>0`.

All affine terms are arbitrary. The signs of the two eigenvalues of `G` are unrestricted.

Let `r_i in R^2` be the rows of `R`, let

`c=max_i ||r_i||_2^2`,

and suppose `0<c<1`. Then

`boxed:`
`||p_Q||_inf`
` <= 8 / ( sqrt(kappa s) [c(1-c)]^(1/4) ) + C_*/sqrt(D),`         (1.2)

where

`C_* = 2+log 2+sqrt(2 pi e) erfc(1/sqrt 2)=4.004506265397...`.

No support, moment, fragment-count/separation, or translation parameter occurs. The estimate is uniform in the arbitrary diagonal twist `Delta` and arbitrary conditioning-generated affine terms.

The result is useful precisely on the high-leverage side left complementary to the diffuse rank-two Fresnel branch: if `1/2<c<=1-delta`, then

`||p_Q||_inf <= 8(2/delta)^(1/4)/sqrt(kappa s)+C_*/sqrt(D).`      (1.3)

The only endpoint not controlled uniformly by this estimate is `c -> 1`.

## 2. Exact row-to-bank leakage identity

Choose an index `i` attaining `||r_i||^2=c`. Let `T=R G R^T`, and let `a` be the vector of the off-diagonal entries in row `i`:

`a_j=T_ij=r_i^T G r_j`, `j != i`.

Because the columns of `R` are orthonormal,

`sum_j r_j r_j^T=I_2`.

Therefore

`||a||_2^2`
` = sum_{j!=i} (r_i^T G r_j)^2`
` = r_i^T G (I_2-r_i r_i^T) G r_i`
` = ||G r_i||_2^2 - (r_i^T G r_i)^2.`                           (2.1)

Write `r_i=sqrt(c)e` with `||e||=1`. Then

`||a||_2^2`
` = c ||G e||_2^2 - c^2 (e^T G e)^2`
` >= c(1-c)||G e||_2^2`
` >= c(1-c)s^2,`                                                 (2.2)

because `(e^TGe)^2<=||Ge||^2` and `||Ge||>=sigma_min(G)>=s`. Thus

`boxed: ||a||_2 >= s sqrt(c(1-c)).`                              (2.3)

This identity is sign-free: it works for positive, negative, or indefinite rank-two curvature.

## 3. Reduction to the arbitrary-self random-slope compiler

Keep the physical bank coordinate `X=V_i` active. All diagonal twisting merely changes its self coefficient

`h=Delta_ii+T_ii`,

which is completely arbitrary. The exact bank polynomial can be written

`h X^2 + X[beta+2 a^T V_{-i}] + R_0(V_{-i}),`                    (3.1)

where `beta` contains every conditioning-generated affine contribution and `R_0` is otherwise arbitrary. In particular, no independence between the slope and the remainder is asserted or needed.

The previous account02/B14 r34 theorem `QFORM-ARBITRARY-SELF-RANDOM-SLOPE-MASS-v1` applies once the scalar slope in (3.1) has a density cap.

## 4. Required Claude L^p result gives the whole-slope cap

The required source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

proves the Fourier `L^p` lemma

`int |psi(t)|^p dt <=4 pi/sqrt(p),     p>=2`                     (4.1)

for the characteristic function of every cap-one density.

For completeness, (4.1) gives the following source-valid projection cap for the actual original-coordinate product bank:

`boxed: ||p_{a^T V_{-i}}||_inf <=2/||a||_2.`                     (4.2)

Indeed, if some `|a_j|>=||a||/sqrt(2)`, condition on all other coordinates and use the one-dimensional cap `1/|a_j|<=sqrt(2)/||a||<2/||a||`. Otherwise put `alpha_j=a_j^2/||a||^2<=1/2`, use generalized Holder with exponents `1/alpha_j`, apply (4.1), and obtain

`int |phi_{a^TV}(t)|dt <=4pi/||a||`,

hence (4.2) by Fourier inversion.

Consequently the slope `beta+2a^TV` has density cap

`H <=1/||a||_2 <=1/[s sqrt(c(1-c))].`                            (4.3)

Applying the r34 pair/random-slope compiler with bank mass one gives

`||p_Q||_inf <=8 sqrt(H/kappa)+C_*/sqrt(D),`

and (4.3) proves (1.2).

## 5. Protected second-stage localization

The r35 protected-anchor theorem gives an additional useful sharpening of the proof architecture. If the slope vector `a` has a physical coordinate `k` such that

`|a_k| >= ||a||_2/2,`                                            (5.1)

then keep only `V_k` whole and arbitrarily fragment/localize **every other** coordinate of `V_{-i}`. On every resulting subproduct cell of mass `m`, the unnormalised density of the slope `2a^TV` is at most

`m/(2|a_k|) <= m/||a||_2.`                                      (5.2)

Thus the exact same whole-slope value `H=1/||a||_2` used in Section 4 survives piecewise with a full factor of the cell mass. Summation therefore preserves the constant in (1.2) exactly.

In this heavy-second-stage branch, after the outer pair only the hub coordinate `i` and one slope anchor `k` need remain unfragmented; every other physical bank coordinate can be localized at zero tax. If (5.1) fails, the slope itself is genuinely diffuse and should be paid by the whole-bank Fourier/projection certificate before active fragmentation.

## 6. What this changes

Together with the already-completed diffuse rank-two Schur/Fresnel branch, this theorem reduces arbitrary-affine `diagonal + rank-two` Schur curvature to a near-coordinate endpoint: the only leverage regime not receiving a uniform constant from either the diffuse theorem or (1.2) is `c` arbitrarily close to one. The remaining endpoint must be sent to a whole-law volume/ridge/rank-one mechanism; it cannot be replaced by coefficient-to-output-law continuity under arbitrary unbounded inputs.
