SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B09, 2026-09-22T21:49:06Z.
attacking: the one-strong-cross full-curvature residual via a two-transverse-direction definite bank estimate that keeps conditional linear anti-concentration and avoids square-root decoupling.

# fleet03/B09 QFORM r18 — definite transverse two-curvature smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet03/B09` — Bilinear block mechanism  
Run: `20260922T214906Z-fleet03-B09-QFORM-r18`  
Outcome: **SUPPORTING_THEOREM_PROVED / DEFINITE TRANSVERSE-RANK-TWO BANK PAID / INDEFINITE JOINT-CAP EXTENSION REFUTED / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The full quadratic-form conjecture remains open. This run advances the current B09 one-strong-cross residual in two ways. First, it proves a direct `O(interval length)` estimate when the opposite bank supplies two same-sign transverse curvature directions, without taking a square-root small-ball loss. Second, it gives an explicit bounded-joint-density obstruction showing that the same proof interface cannot simply replace the definite two-dimensional curvature by an indefinite one. The latter is not a target counterexample because the constructed three-dimensional joint law is not asserted to arise as a product-measure projection.

## 1. Source-pinned dependency actually used

I use the completed fleet02/B06 theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical proof

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For any `k`-dimensional orthogonal projection of a product density with one-dimensional caps one, that theorem gives a joint density cap at most `exp(k/2)`. Therefore, for linearly independent vectors `v,w1,w2` in one original-coordinate bank and

`Z=(V,W1,W2)=(<v,X>,<w1,X>,<w2,X>)`,

we have

`||p_Z||_infinity <= e^(3/2) / ||v wedge w1 wedge w2||`.              (1.1)

The one-dimensional projection theorem already used in the preceding B09 run gives, for `U=<u,X>` on a disjoint original-coordinate bank,

`||p_U||_infinity <= sqrt(2)/||u||_2`.                                (1.2)

The designated partner `fleet04/B09` was checked again at the current canonical math-open-problems and brain handoff locations. No completed current-QFORM artifact was present. I therefore do not fabricate a partner theorem; work proceeds asynchronously with the completed compatible fleet02/B06 result above applied at the explicit inequality (4.2).

Corrections enforced: no post-rotation independence, no arbitrary-joint rank-three coarea, no positive conditional projection-density moment, no pointwise law-uniform Fresnel decay, no fixed tiny principal-minor inversion, and no square-root decoupling.

## 2. Analytic core

### Lemma 2.1 — `QFORM-SCALAR-THREEPROJ-DEFINITE-TRANSVERSE-v1`

Let `U` be independent of the random vector `Z=(V,W)` with `V in R`, `W in R^2`. Assume

`||p_U||_infinity <= N`,
`||p_Z||_infinity <= M`.                                             (2.1)

Let `a!=0`. Let `q(v,w)` be an arbitrary real quadratic polynomial in `(v,w)` whose quadratic `w`-block is a real symmetric definite `2x2` matrix `D`; thus

`q(v,w)=w^T D w + 2v h^T w + c v^2 + l^T w + beta v + delta`,        (2.2)

with `D` positive or negative definite. For arbitrary `alpha in R`, define

`T=2aUV + alpha U + q(V,W)`.                                         (2.3)

Then `T` has an essentially bounded density and

`boxed: ||p_T||_infinity
 <= 2 sqrt(pi M N / |a|) |det D|^(-1/4).`                            (2.4)

Consequently every interval `L` satisfies

`P{T in L} <= 2 sqrt(pi M N / |a|) |det D|^(-1/4) |L|`.             (2.5)

#### Proof

Translate `V` by `alpha/(2a)`. This removes `alpha U`, preserves independence of `U` from `Z`, preserves the joint density cap `M`, and leaves the quadratic `w`-block equal to `D`. Thus assume `alpha=0`.

Fix `t in R`, `epsilon>0`, and a threshold `r>0`. Split the event

`E={|T-t|<=epsilon}`

into `|V|>r` and `|V|<=r`.

**Large cross coefficient.** Conditional on `Z=(v,w)` with `|v|>r`, the admissible values of `u` form an interval of length

`epsilon/(|a v|)`                                                     (2.6)

because the slope in `u` is `2av`. Hence

`P(E, |V|>r) <= N epsilon/(|a|r)`.                                   (2.7)

**Small cross coefficient.** Condition on `U=u`. For each fixed `(u,v)`, the condition `|T-t|<=epsilon` is

`|w^T D w + b(u,v)^T w + d(u,v)-t|<=epsilon`                         (2.8)

for some vector `b(u,v)` and scalar `d(u,v)`. Completing the square in `w` translates the ellipse (or reflected ellipse) without changing its area. Diagonalizing `D` orthogonally and then scaling by `|D|^(1/2)` shows

`Leb_2{w: |w^T D w + b^T w + d-t|<=epsilon}
 <= 2 pi epsilon / sqrt(|det D|)`.                                   (2.9)

Indeed, after these transformations the set is an annulus strip

`{y: ||y|^2-s|<=epsilon}`,

whose area is at most `2pi epsilon`; negative-definite `D` is reduced by multiplying the quadratic by `-1`.

For `|v|<=r`, the available `v`-length is `2r`. Since `Z` has joint density at most `M`, uniformly in `u`,

`P(E, |V|<=r | U=u)
 <= 4 pi M r epsilon / sqrt(|det D|)`.                               (2.10)

Averaging in `u` leaves the same bound. Combining (2.7) and (2.10),

`P(E) <= epsilon [ A/r + B r ]`,                                    (2.11)

where

`A=N/|a|`,
`B=4 pi M / sqrt(|det D|)`.                                         (2.12)

The minimum over `r>0` is attained at `r=sqrt(A/B)` and equals

`2 epsilon sqrt(A B)`.                                                (2.13)

The centered interval in (2.11) has length `2epsilon`, so the law is dominated by Lebesgue measure with density cap

`sqrt(A B)=2 sqrt(pi M N / |a|)|det D|^(-1/4)`,                      (2.14)

which is (2.4). `QED`

The important feature is that the interval length remains linear throughout. The large-`|V|` branch uses conditional linear anti-concentration; the small-`|V|` branch uses the constant area of a two-dimensional definite quadratic shell. No `sqrt(epsilon)` loss is introduced.

## 3. Why definiteness cannot be dropped at the joint-cap interface

### Proposition 3.1 — `QFORM-INDEFINITE-TRANSVERSE-JOINTCAP-FALSE-v1`

There is no bound depending only on `N`, `M`, `|a|`, and `|det D|` in Lemma 2.1 if `D` is allowed to be indefinite, even with `N=M=|a|=1` and `|det D|=1/4` fixed.

#### Construction

Fix `0<delta<1/4`, set

`R=exp(1/(4 delta^2))`,

and let `Z=(V,W1,W2)` have density equal to the indicator of

`E_delta={|v|<=delta, 1<=w1<=R, |w2|<=delta/w1}`.                    (3.1)

Its volume is exactly

`(2delta) int_1^R (2delta/w1) dw1
 =4 delta^2 log R
 =1`,                                                                  (3.2)

so this is a probability density with cap one. Let `U` be independent and uniform on `[-1/2,1/2]`, also cap one. Put

`T_delta=2 U V + W1 W2`.                                              (3.3)

The transverse quadratic matrix is

`D=[[0,1/2],[1/2,0]]`,

so `det D=-1/4`, uniformly nondegenerate and indefinite. Yet on the support,

`|2UV|<=delta`,
`|W1W2|<=delta`,

hence

`|T_delta|<=2delta` almost surely.                                    (3.4)

The law is absolutely continuous because conditional on `(V,W1,W2)` with `V!=0` it is the affine image of the absolutely continuous variable `U`, while `P(V=0)=0`. Since all mass lies in an interval of length `4delta`,

`||p_(T_delta)||_infinity >= 1/(4delta) -> infinity`.                 (3.5)

Thus the bounded joint-density information supplied by a projection theorem is by itself insufficient for indefinite transverse curvature. A successful indefinite-bank theorem must retain more of the original product provenance than the single number `||p_Z||_infinity`. This proposition is **not** a counterexample to the QFORM conjecture because the joint density (3.1) is not asserted to be a linear projection of independent cap-one coordinates.

## 4. Product-bank theorem

### Theorem 4.1 — `QFORM-TWO-BANK-DEFINITE-TRANSVERSE-RANK2-v1`

Let `I,J,R` be disjoint sets of original independent coordinates. Choose nonzero `u in R^I` and linearly independent `v,w1,w2 in R^J`. Define

`U=<u,X_I>`,
`V=<v,X_J>`,
`Wk=<wk,X_J>`, `k=1,2`.

Conditioning on `X_R` is permitted provided the active conditional form depends on `X_J` only through `(V,W1,W2)` and can be written

`F=Z_R + 2aUV + alpha U + q(V,W1,W2)`,                               (4.1)

where `a!=0`, `Z_R` is the conditioned additive shift, and the `W=(W1,W2)` quadratic block of `q` is a definite matrix `D`.

Let

`Omega=||v wedge w1 wedge w2||`,
`Gamma=|a|^2 ||u||_2^2 Omega^2 |det D|`.                             (4.2)

Then

`boxed: ||p_F||_infinity <= C_def Gamma^(-1/4)`,                     (4.3)

where

`C_def=2^(5/4) sqrt(pi) e^(3/4)=8.9244876390... <8.925`.              (4.4)

Equivalently, for every interval `L`,

`P{F in L} <=8.925 Gamma^(-1/4)|L|`.                                 (4.5)

#### Proof

Because `I` and `J` are disjoint, `U` is genuinely independent of the triple `(V,W1,W2)`. The one-dimensional projection bound gives

`N<=sqrt(2)/||u||_2`.                                                  (4.6)

Apply the completed fleet02/B06 theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` to an orthonormal basis of `span{v,w1,w2}` and then transform to the stated coordinates. This is the promised actual application of a completed worker result:

`M<=e^(3/2)/Omega`.                                                    (4.7)

Insert (4.6)-(4.7) into Lemma 2.1:

`||p_F||_infinity
 <=2 sqrt(pi/|a|) [e^(3/2)sqrt(2)/(||u|| Omega)]^(1/2)|det D|^(-1/4)
 =2^(5/4)sqrt(pi)e^(3/4) Gamma^(-1/4)`.                               (4.8)

Conditioning on `X_R` changes only coefficients already allowed in `q` and the additive shift, so the bound is uniform in the conditioning and averages back. `QED`

The certificate `Gamma` is invariant under rescaling of the projection vectors and under invertible changes of basis in the two-dimensional `W`-plane: `Omega^2 det D` is the natural volume-curvature product.

## 5. Exact target-valid diffuse stress family

Let `m` be divisible by four. Take disjoint banks `I,J`, each of size `m`. Let `u` be the normalized constant vector on `I`, and let `v,w1,w2` be three orthonormal Walsh vectors on `J`, each with coordinates of magnitude `m^(-1/2)`. Define the symmetric matrix

`A = u v^T + v u^T + w1 w1^T + (1/2) w2 w2^T`.                       (5.1)

On the orthonormal span `{u,v,w1,w2}`, the compressed matrix is

`[[0,1,0,0],
  [1,0,0,0],
  [0,0,1,0],
  [0,0,0,1/2]]`.                                                      (5.2)

Therefore the nonzero spectrum is exactly

`{-1,1,1,1/2}`.                                                       (5.3)

Thus (5.1) has exactly three eigenvalues with modulus at least one and is a valid target matrix. Every physical matrix entry is `O(1/m)`, so fixed local-minor methods lose scale as `m` grows. In Theorem 4.1 we have

`a=1`, `||u||=1`, `Omega=1`, `D=diag(1,1/2)`,

hence `Gamma=1/2` and

`boxed: ||p_(X^T A X)||_infinity
 <=2^(3/2) sqrt(pi)e^(3/4)
 =10.6130641981... <10.614`                                          (5.4)

for every independent input law with coordinate densities at most one, uniformly in `m`.

This is an aggregate bank payment: all active physical entries tend to zero while the density bound remains dimension-free.

## 6. Remaining B09 debt

The current one-strong-cross residual is now narrower. The following branches are paid by existing B09 work:

1. two singular cross directions across one cut;
2. a three-disjoint-bank rank-one triangle;
3. one cross direction plus one transverse rank-one same-bank square;
4. one cross direction plus a **definite transverse rank-two bank**, by Theorem 4.1.

The first unpaid mechanism is now:

`QFORM-ONE-STRONG-CROSS-INDEFINITE-OR-OVERLAPPING-CURVATURE-v1`.

One must retain product provenance strongly enough to control either (i) an indefinite transverse two-curvature bank, for which Proposition 3.1 shows that a mere three-dimensional joint density cap is insufficient, or (ii) genuinely overlapping higher-rank residual curvature that cannot be conditioned onto disjoint original coordinates without destroying the bank aggregation. A plausible next route is a Brascamp--Lieb-weighted hyperbolic shell estimate that retains the individual original-coordinate factors instead of collapsing them to `||p_Z||_infinity`.

The unrestricted QFORM conjecture remains **OPEN**. The new theorem proves absolute continuity and an essential `L^infinity` bound in its stated scope; it does **not** prove a continuous representative.
