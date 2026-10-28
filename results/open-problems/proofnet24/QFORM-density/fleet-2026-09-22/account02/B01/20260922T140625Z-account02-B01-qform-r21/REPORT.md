# QFORM B01 r21 — product-preserving rank-two randomization plus transverse quadratic gate

Status: ESSENTIAL_STEP_APPLIED / supporting theorem / full target OPEN.

## Target and source pins

Programme: QFORM-DENSITY-3EIG-20260922, owner control revision 2026-09-22.5.
Fresh brain control initially resolved at `20dcc298195e75e8dab67da3c1efcca69490ed73`; pre-publication refresh observed `b1f7c74f88742b541c02dc9bd71a0c335b014382` with no later owner stop found at that point.
Consumed corrections include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`, and `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`.
Own prior dependency: account02/B01 r19, math-open-problems commit `fedbec07e3e8b2f9fcd2b1a65b0bb2a0137c212f`, proving the uniform scalar gate `int |F(t)|^3 dt <= 16 pi/|a|` for probability densities bounded by one.
Named partner consumed: account03/B01 run `account03-B01-20260922T123142Z-qform-r11`, math-open-problems report commit `d54e3a5d40a1d9837d39a1e525781fcf44ec0d9d`, which identifies the rank-two averaged `L^3` endpoint and the need to couple it to a third curvature direction without post-rotation independence.

## New theorem

Let `X_1,...,X_n` be independent real variables with probability densities `0<=f_i<=1`, and let `A` be real symmetric. Choose disjoint original-coordinate sets `I,K` with `|I|=3`, `|K|=2`. Put

`M=A[I,K]`.

Assume `rank M=2`. Let `nu` be a unit vector spanning `ker(M^T)` in `R^I`, and define

`a = nu^T A[I,I] nu`,
`Delta = sqrt(det(M^T M))`,

so `Delta` is the product of the two nonzero singular values of `M`. If `a != 0`, then `Q=X^T A X` has a bounded continuous density. Quantitatively,

`||p_Q||_infinity <= 1/pi + 4 pi^(1/3) Delta^(-1/2) max(3^(1/4), |a|^(-1/4)).`

This keeps every outside coupling and does not assume independence after any spectral rotation. It is a genuine coupled `2+1` smoothing mechanism: two directions come from original-coordinate linear randomization through the `3 x 2` cross block, while the third comes from quadratic curvature in the left-null direction of that same cross block.

## Proof

Write the three coordinates in `I` as a vector `x`. Choose an orthogonal matrix `O=[P,nu]`, where the two columns of `P` span `nu^perp`, and set

`x = P u + nu w`,  with `u in R^2`, `w in R`.

Because `nu^T M=0`, the two coordinates in `K`, denoted `v in R^2`, couple only to `u`. More precisely,

`N=P^T M`

is an invertible `2 x 2` matrix and

`|det N| = sqrt(det(M^T M)) = Delta`.

The transformed joint density on `(u,w)` is

`G(u,w)=prod_{i in I} f_i((P u+nu w)_i)`.

Orthogonality gives `int G=1`, and `0<=G<=1`. Define the slice mass

`m(u)=int_R G(u,w) dw`.

Since some coordinate of the unit vector `nu` has magnitude at least `1/sqrt(3)`, say `|nu_j|>=1/sqrt(3)`, and all other factors are at most one,

`m(u) <= int f_j((P u)_j+nu_j w) dw = 1/|nu_j| <= sqrt(3)`.

Also `int m(u)du=1`.

Let `R` denote all coordinates outside `I union K`, and condition on `R=r`. The phase involving `(u,w,v)` has the form

`u^T H u + 2 c^T u w + a w^2 + 2 u^T N v + linear terms in (u,w) + terms independent of (u,w)`.

The key point is that the `v`-variables do not occur in the linear coefficient of `w`, because `nu^T M=0`.

For fixed `r,t`, define

`Psi_{r,t}(z) = int exp(i t [u^T H u + 2c^T u w + a w^2 + 2 u^T z + ell_r(u,w)]) G(u,w) du dw`,

where `ell_r` is affine in `(u,w)`. Since the product density of the two `K`-variables is at most one, Jensen followed by the change of variables `z=Nv` gives

`|phi_Q(t)|^2 <= Delta^(-1) E_r int_{R^2} |Psi_{r,t}(z)|^2 dz`.          (1)

For fixed `u,r`, let

`F_{u,r}(t)=int exp(i t [a w^2+b_{u,r} w]) G(u,w) dw`,

where `b_{u,r}` is real. Two-dimensional Plancherel in `u` yields exactly

`int |Psi_{r,t}(z)|^2 dz = pi^2 |t|^(-2) int |F_{u,r}(t)|^2 du`.       (2)

Combining (1)-(2),

`|phi_Q(t)| <= pi Delta^(-1/2) |t|^(-1) H(t)`,

where

`H(t) = ( E_r int |F_{u,r}(t)|^2 du )^(1/2)`.                         (3)

It remains to exploit the quadratic curvature `a` without destroying the original product provenance.

### Scalar weighted lemma for non-normalized slices

Let `0<=h<=1` have mass `m=int h`, and let

`F(t)=int exp(i t (a w^2+bw)) h(w)dw`,  `a!=0`.

The r19 scalar theorem for a probability density bounded by one rescales to

`int_R |F(t)|^3 dt <= 16 pi m/|a|`.                                  (4)

Indeed, for `m>0`, the function `h(m y)` is a probability density bounded by one and the quadratic coefficient becomes `a m^2`.

Also `|F(t)|<=m`. For any `R0>=1`, Holder gives

`int_{R0}^infinity |F(t)|/t dt <= (64 pi m/(|a| R0))^(1/3)`.

Choose `R0=max(1,(|a|m^2)^(-1))`. Then

`int_1^infinity |F(t)|/t dt <= m [ c0 + log_+(1/(|a|m^2)) ]`,          (5)

with `c0=4 pi^(1/3)`.

Apply (5) to every slice `h(w)=G(u,w)`. Minkowski's integral inequality applied to the `L^2(du dP_R)` norm in (3) gives

`int_1^infinity |phi_Q(t)|dt
 <= pi Delta^(-1/2) || m(u)[c0+log_+(1/(|a|m(u)^2))] ||_{L^2(du)}`.    (6)

Because `int m=1` and `m<=sqrt(3)`, the final norm is dimension-free. Precisely,

`int m(u)^2 [c0+log_+(1/(|a|m(u)^2))]^2 du
 <= c0^2 max(sqrt(3), |a|^(-1/2)).`                                  (7)

To check (7), write `s=sqrt(|a|)m`. For `s>=1` the logarithm vanishes and `m<=sqrt(3)`. For `0<s<=1`, the function

`s [c0+2 log(1/s)]^2`

is maximized at `s=1` because `c0=4 pi^(1/3)>4`.

Thus

`int_1^infinity |phi_Q(t)|dt
 <= pi c0 Delta^(-1/2) max(3^(1/4), |a|^(-1/4)).`

The same estimate holds on `(-infinity,-1]`, while `|phi_Q(t)|<=1` on `[-1,1]`. Hence

`||phi_Q||_1 <= 2 + 2 pi c0 Delta^(-1/2) max(3^(1/4), |a|^(-1/4)).`

Fourier inversion proves the displayed density bound and gives a continuous density vanishing at infinity.

## What this pays and what remains

This proves a source-valid nonindependent `rank-two + third-curvature` bridge, directly addressing the coupling debt highlighted by the named partner's averaged `L^3` endpoint. The product assumption is used in an essential and transparent place: the one-dimensional slice mass bound `m(u)<=sqrt(3)`. Replacing the rotated three-coordinate law by an arbitrary bounded joint density would lose this control, consistent with the previously recorded projection-only counterexample.

The theorem does NOT finish the three-large-eigenvalue conjecture. To turn it into a universal proof one would need a dimension-free structural/aggregate implication ensuring a gate with controlled `Delta` and transverse `|a|`, or a many-column version in which small physical couplings are paid collectively. The source-valid family

`A_m = [1] direct_sum J_m/m direct_sum (-J_m/m)`

has spectrum `{1,1,-1}` but defeats any fixed-size uniformly good minor/cross-rank extraction: its useful couplings are spread over coordinate banks. Therefore the next unpaid implication is an aggregated version of the theorem, not selection of one uniformly large `3 x 2` minor.

## Partner application and comparison

The completed account03/B01 result `account03-B01-20260922T123142Z-qform-r11` proves a rank-two averaged endpoint and closes the independent-third-square branch by the exponent arithmetic `L^3 * L^(3/2) -> L^infinity`. The theorem above applies the same `2+1` philosophy in a genuinely coupled configuration: the two randomizing directions and the transverse square share the same three physical coordinates, and all remaining couplings are retained. Thus the partner's identified coupling debt is paid on this new cross-minor/transverse-curvature branch, while its diffuse branch remains separately available.

## Honest status

ESSENTIAL_STEP_APPLIED. Full QFORM remains OPEN. No claim is made that the three-large-eigenvalue hypothesis forces the quantitative gate above. No fixed-size-minor extraction is assumed. No post-rotation independence is used.
