SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-22T22:18:30Z.
attacking: the many-small-pair heavy-star residual via a diffuse hub-Fresnel-Brascamp-Lieb compiler, then robustness to dense self-couplings.

# fleet02/B11 QFORM r16 — diffuse hub Fresnel compiler and full orthogonal hub-square subclass

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Indefinite signatures; complementary constructions/source-valid counterexamples  
Run: `20260922T221830Z-fleet02-B11-QFORM-r16`  
Outcome: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

## 1. First unpaid implication and what changed

The preceding B11 run left `QFORM-TWO-BANK-WEDGE-TRACE-v1`: after extracting two disjoint original-coordinate banks with constant transverse wedge mass, pay the parabolic trace without collapsing the banks to arbitrary joint densities. The newest assigned-partner result fleet03/B11 r17 sharpens the same obstruction: if neither a quantitative original-coordinate indefinite pair nor a diffuse rank-three ridge cut is present, the zero-diagonal/null-frame residue is a many-small-pair heavy star.

This run pays a nontrivial canonical part of that residue. It proves a sharp-Hausdorff--Young hub/Fresnel estimate which treats one genuine original-coordinate hub and an arbitrary finite-rank leaf curvature jointly, and then combines it with the partner pair compiler and the existing exact-rank-three scalar-pivot theorem to remove the diffuse-leverage hypothesis completely for the orthogonal hub-plus-one-square family. A harmonic family shows this subclass can escape both partner r17 branches at every fixed scale while remaining uniformly bounded here.

The remaining full-target debt is now the **robust dense self-coupling step**: retain this product-preserving mechanism when the leaf block contains an arbitrary small dense quadratic self-coupling. Such a term cannot be deleted perturbatively under the owner's moment/support-free hypotheses.

## 2. Source-pinned dependencies and correction status

1. Latest completed assigned partner fleet03/B11 r17: `yspennstate/math-open-problems@c869a82e52e46664d5bf299c3b210de02a02fc50`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260922T215136Z-fleet03-B11-QFORM-r17/REPORT.md`. Its `QFORM-INDEFINITE-PAIR-OR-DIFFUSE-RIDGE-COMPILER-v1` gives the physical-pair bound used in Section 5 and identifies the many-small-pair heavy-star residue.
2. Rank-two affine half-Riesz / exact-rank-three scalar-pivot theorem: `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, path `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`. For a full exact-rank-three matrix with all nonzero eigenvalues of magnitude at least one, every nonzero physical diagonal entry `A_ii` gives `||p_Q||_infinity <=128/sqrt(|A_ii|)`.
3. Claude-attributed Fresnel/Brascamp--Lieb package: `yspennstate/math-open-problems@7359c982f3fa85f61b99e8768b915cce6e596d36`, path `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`. Its Theorem H proves the general one-hub/low-rank-plus-diagonal mechanism with a coarser Fourier norm. The calculation below is a sharp-Hausdorff--Young specialization/strengthening with an explicit constant; no novelty claim is made.
4. Sharp Hausdorff--Young and geometric Brascamp--Lieb normalization is also fully written in the preceding rank-two-fusion source and in B11's earlier report `yspennstate/math-open-problems@245a4e2a4414294fbb20b9dd4f292f6b001e5aa2`.

Binding corrections were enforced: no independence after spectral rotation; no arbitrary-joint rank-three coarea; no conjugate-variable conditional density cap; no fixed-good-minor/cross-rank-three exhaustive dichotomy; no moment/support assumption; and no small-coefficient perturbative deletion under unbounded inputs.

## 3. A sharp hub-Fresnel-Brascamp--Lieb theorem

Let `X_0,(X_j)_{j in I},X_J` be independent real random variables with probability densities bounded by one. Condition on the outside coordinates `X_J`; all terms involving them become affine terms in the remaining original coordinates.

Let `b in R^m`, let `U` be an `m x r` real matrix (`r>=1`), and write the row vectors

`w_j=(b_j,U_{j,1},...,U_{j,r}) in R^(r+1)`.

Assume the Gram matrix

`G=sum_j w_j w_j^T`

is positive definite and that every normalized row leverage

`c_j=w_j^T G^(-1) w_j`

satisfies `c_j<=1/2`. Let `C` be an invertible real symmetric `r x r` matrix and `kappa!=0`. Allow arbitrary diagonal leaf curvature `D=diag(d_j)`, arbitrary hub scalar curvature, arbitrary affine terms, and arbitrary outside coefficients/couplings. The conditioned quadratic polynomial has the structural part

`2 kappa X_0 <b,X_I> + (U^T X_I)^T C(U^T X_I) + X_I^T D X_I`.

### Theorem 3.1 — `QFORM-DIFFUSE-HUB-FRESNEL-BL-v1`

The full form has a continuous `C_0` density and

`||p_Q||_infinity <= ((r+2)/r) e^((r+1)/(r+2))`
`                      * |kappa|^(-2/(r+2))`
`                      * |det C|^(-1/(r+2))`
`                      * det(G)^(-1/(r+2)).`                 (3.1)

No sign condition on `C` is needed.

### Proof

Use the standard characteristic function `phi_i(s)=E exp(i s X_i)`. The exact `r`-dimensional Fresnel identity for invertible symmetric `C` gives, up to a unimodular phase,

`exp(i t z^T C z)`
` =(4 pi |t|)^(-r/2)|det C|^(-1/2)`
`   * integral exp(-i xi^T C^(-1)xi/(4t)) exp(i xi dot z) dxi.`

The hub scalar phase, leaf diagonal phases and all affine translations have modulus one. After conditioning outside, insert Fresnel in the `U`-quadratic term. Integrate the hub variable before taking the absolute value, use its density cap one, and set `v=2 kappa t x_0`. Independence of the **original leaf coordinates** then yields

`|phi_Q(t)| <= (4 pi |t|)^(-r/2)|det C|^(-1/2)`
`              * (2|kappa t|)^(-1) J`,                       (3.2)

where, allowing arbitrary argument translations `s_j`,

`J= integral_{R^(r+1)} prod_j |hat g_j(<w_j,y>+s_j)| dy`,     (3.3)

and `g_j(x)=f_j(x) exp(i times a real quadratic/affine phase)`, hence `|g_j|=f_j<=1` and `||g_j||_1=1`.

Put `u_j=G^(-1/2)w_j^T`, so `sum_j u_j u_j^T=I_(r+1)` and `c_j=||u_j||^2`. Changing variables by `G^(1/2)` contributes `det(G)^(-1/2)`. For `0<c_j<=1/2`, sharp Hausdorff--Young with exponent `1/c_j`, followed by geometric rank-one Brascamp--Lieb, gives exactly

`J <= det(G)^(-1/2) (2 pi)^(r+1)`
`       * product_j (1-c_j)^(-(1-c_j)/2)`
`   <= det(G)^(-1/2) (2 pi)^(r+1) exp((r+1)/2),`             (3.4)

because `-(1-c)log(1-c)<=c` and `sum c_j=r+1`. Zero rows are omitted. The argument translations do not affect the one-dimensional norms.

Combining (3.2)-(3.4) gives

`|phi_Q(t)| <= min(1, K |t|^(-(r+2)/2)),`                    (3.5)

with

`K=pi^(r/2+1) exp((r+1)/2)`
`   /( |kappa| sqrt(|det C|) sqrt(det G) ).`                  (3.6)

Let `alpha=(r+2)/2>1`. Direct integration gives

`int_R min(1,K|t|^-alpha) dt`
` =2 (r+2)/r * K^(2/(r+2)).`                                 (3.7)

Fourier inversion multiplies this by `1/(2pi)`. The power of `pi` in `K^(2/(r+2))` is exactly one and cancels, yielding (3.1). Since `phi_Q` is integrable, the density has a continuous representative vanishing at infinity. The bound was uniform in the outside conditioning, and equivalently the unconditional characteristic function satisfies the same envelope. QED.

### Rank-one leaf corollary

For `r=1`, if `b,d in R^m` are orthonormal and every row satisfies

`b_j^2+d_j^2<=1/2`,

then for

`Q=2 kappa X_0 <b,X> + lambda <d,X>^2`

(and arbitrary affine terms),

`||p_Q||_infinity <= 3 e^(2/3)|kappa|^(-2/3)|lambda|^(-1/3).` (3.8)

At `|kappa|,|lambda|>=1`, the constant is

`3 e^(2/3)=5.843202123164...`.

This is genuinely rotated when `b,d` are diffuse and overlapping in the original coordinates.

## 4. Exactly how the third direction removes the rank-two logarithm

The rank-two opposite-sign control is retained. For two independent centered unit uniforms, the density of `2XY` is logarithmically divergent at zero. More generally, a product of two independent variables whose densities are bounded below near zero has the same logarithmic lower-bound mechanism.

In (3.2), the hub bilinear variable supplies exactly `|t|^-1`: the change of variable `v=2 kappa t x_0` costs `1/|t|`. With no transverse quadratic direction (`r=0`) this is the critical nonintegrable endpoint, matching the rank-two logarithm. One genuine leaf quadratic direction contributes an additional Fresnel factor `|t|^-1/2`; the joint original-coordinate Brascamp--Lieb integral stays uniformly finite under the leverage gate, producing `|t|^-3/2`. Thus the third direction removes the logarithm by moving the time exponent strictly above one, not by making rotated variables independent and not by pretending the rank-two density is bounded. Each further exact low-rank leaf direction adds another half power.

## 5. Removing the diffuse gate for the full orthogonal hub-square subclass

The preceding theorem can be combined with two completed source-pinned results to cover **every** orthogonal hub-square frame, including heavy rows.

### Theorem 5.1 — `QFORM-ORTHOGONAL-HUB-SQUARE-FULL-v1`

Let `b,d in R^m` be orthonormal, let `|kappa|>=1` and `|lambda|>=1`, and let all `X_0,...,X_m` be independent with densities bounded by one. Then

`Q=2 kappa X_0 <b,X> + lambda <d,X>^2`                         (5.1)

has an essentially bounded density satisfying the universal estimate

`||p_Q||_infinity <=256.`                                    (5.2)

For `lambda>0` the three nonzero eigenvalues have signature `(+,+,-)`; for `lambda<0` they have signature `(+,-,-)`. They are exactly `|kappa|,-|kappa|,lambda`, so this is a genuine exact-rank-three target subclass.

### Proof

If every `b_j^2+d_j^2<=1/2`, use (3.8), giving `<5.844`.

Otherwise choose `j` with `b_j^2+d_j^2>1/2`.

**Square-dominant subcase.** If

`|A_jj|=|lambda| d_j^2 >=1/4`,

apply the exact-rank-three scalar-pivot theorem from the rank-two-fusion source. Since all three nonzero eigenvalues have magnitude at least one,

`||p_Q||_infinity <=128/sqrt(|A_jj|)<=256.`                  (5.3)

**Saddle-dominant subcase.** Suppose instead `|lambda|d_j^2<1/4`. Then `d_j^2<1/4`, hence `b_j^2>1/4` and the original-coordinate principal pair on `{0,j}` is

`B_j=[[0,a],[a,q]],  a=kappa b_j, q=lambda d_j^2`,

with `|a|>1/2`, `|q|<1/4`. It is indefinite. Its determinant magnitude is `D=a^2>=1/4`; its smallest singular value obeys

`kappa_B >= kappa_0 := (sqrt(17)-1)/8 =0.3903882032...`.

Therefore the partner's pair scale satisfies

`(D^2 kappa_B)^(1/5) >= delta_0 := (kappa_0/16)^(1/5)`
` =0.4758557709... .`                                         (5.4)

Apply fleet03/B11 r17 with the valid global spectral scale `s=1` and `delta=delta_0`. It gives

`||p_Q||_infinity <=3*400^(1/3)*delta_0^(-5/6)`
` <41.044.`                                                    (5.5)

The maximum of the three subcase constants is 256. QED.

This is an actual application of the newest assigned-partner theorem, not just a citation.

## 6. A genuinely diffuse family escaping both partner r17 certificates

For `m>=4` divisible by four, set

`b_j=sqrt(2/m) cos(2 pi j/m)`,
`d_j=sqrt(2/m) sin(2 pi j/m)`, `j=0,...,m-1`,                 (6.1)

and `kappa=lambda=1`. Then `b,d` are exactly orthonormal and every leaf row has leverage

`b_j^2+d_j^2=2/m`.

The physical matrix is

`A_m = [[0,b^T],[b,d d^T]]`,                                  (6.2)

with exact nonzero spectrum `{-1,1,1}`. Every leaf-leaf principal pair is singular, while every hub-leaf pair has partner pair scale at most `sqrt(2/m)`, so no fixed positive pair threshold survives as `m->infinity`.

Moreover every disjoint original-coordinate cross block `A_m[I,J]` has rank at most two. Indeed

`A_m=e_0 b^T+b e_0^T+d d^T`,

and for disjoint `I,J` at most one of `e_{0,I},e_{0,J}` is nonzero; hence at most two of the three displayed rank-one cross terms survive. Thus `s_3(A_m[I,J])=0` for every cut, so the partner diffuse-ridge branch never applies.

Nevertheless Theorem 3.1 gives

`||p_Q||_infinity <=3e^(2/3)<5.844`                            (6.3)

for all `m`. This is a concrete many-small-pair heavy-star/diffuse-leaf family that escapes both partner r17 certificates but is paid by joint hub-Fresnel aggregation before inversion. It is not a counterexample to QFORM.

At `m=4`, deleting the square term leaves `2X_0(X_1-X_3)/sqrt(2)`. For centered unit uniforms, both factors have densities positive near zero, so the product density diverges logarithmically. Restoring the orthogonal square `(X_2-X_4)^2/2` is the third direction. At larger `m`, the `b` and `d` projections genuinely overlap across original coordinates, and the proof above does not use independence of those projections.

## 7. A falsifier for the leverage-free absolute-BL shortcut

The leverage condition in Theorem 3.1 cannot simply be erased from this absolute-value proof. Let `b=e_1`, `d=e_2` and take centered unit-uniform leaf laws. The core Brascamp--Lieb majorant in (3.3) factorizes as

`J=(integral_R |sinc(v/2)| dv)(integral_R |sinc(xi/2)| dxi)=infinity`,

because the absolute integral of `sinc` diverges logarithmically. The actual three-variable output `2kappa X_0X_1+lambda X_2^2` is controlled by the existing parabolic/Abel mechanisms. Hence this is a counterexample only to the stronger leverage-free **absolute Fourier majorant**, not to QFORM. Heavy rows must be peeled by a physical pivot/pair mechanism, exactly as in Theorem 5.1.

## 8. First remaining implication

The owner proof-first continuation specifically asks B10/B11/B12 to handle a hub/star plus delocalized component with arbitrary small dense self-couplings. The theorem above now pays the complete unperturbed orthogonal hub-plus-square model, including both diffuse and heavy leaf rows, and it permits diagonal leaf phases inside the diffuse branch. The genuinely unpaid step is:

`QFORM-HUB-FRESNEL-ROBUST-SELFCOUPLING-v1`:

Given a paid hub/Fresnel frame, control

`2 kappa X_0<b,X> + lambda<d,X>^2 + X^T E X`                  (8.1)

for arbitrary dense symmetric `E` in the source-valid scale regime, **without** treating `X^TEX` as a small random perturbation and without moments/support assumptions; alternatively force a completed physical-pair/ridge/volume-sampling certificate or produce a genuine target counterexample.

The obstruction is structural, not merely a constant loss: a dense nonseparable phase destroys the coordinatewise product inside (3.3), while coefficient-smallness gives no uniform phase error on unbounded or fragmented admissible supports. This is the exact interface to the current Claude Theorem-H limitation and the newest owner proof-first request.

The full QFORM conjecture therefore remains **OPEN / NOT PROVED**.
