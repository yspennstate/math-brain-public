SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T00:38:46Z.
attacking: projection-product interaction at a nonzero near-null spectral coloop, preserving the one genuinely independent physical scalar while using the two-dimensional product projection only through a proved marginal cap.

# account01/B16 r12 — cross-transverse smoothing closes the exact spectral-coloop interpolation

**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM`; full QFORM remains `OPEN / NOT PROVED`; full continuity remains open. Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source pins

The target is: for independent real `X_i` with probability densities at most one and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove one dimension-independent finite constant bounding the density of `X^T A X`. No moment, identical-law, support, sign, or log-concavity assumptions are available.


Required newest-Claude source read and used: `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371:proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`, with the underlying later Claude route `2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926`. In particular I preserve the determinant-only physical-pair theorem and the reduction to the still-open strict no-pivot problem `N3`; neither is treated as the full solution.

The fractional estimate used below is the completed `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` at
`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`:
for an invertible symmetric two-dimensional quadratic coefficient `K`, independent cap-one scalar inputs, and arbitrary affine terms,

`sup_t E |Z^T K Z + linear - t|^(-1/2) <= 16 sqrt(30) |det K|^(-1/4)`

when the affine term lies in the two-dimensional range (in particular for an actual two-variable quadratic). The general arbitrary-original-affine version has constant 128, but the sharper constant is valid in the two-variable use below.

The newest completed designated partner result actually consumed is account02/B16 run `20260923T003232Z-account02-B16-QFORM-r21`, canonical mathematics
`yspennstate/math-open-problems@45bff099504543528c3c7c78fba03f1b8cafeb16:proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T003232Z-account02-B16-QFORM-r21/REPORT.md`.
It proves, using the newest mixed-Fresnel theorem and full original-leaf product factorization, that the strict-N3 family

`Q_{m,delta}=delta X_0^2 + 2 sqrt(1+|delta|) X_0 Y + Z^2`

with the balanced same-bank projections described there has

`||p_Q||_infinity <= 3*2^(4/3)(1+|delta|)^(-1/3) <= 7.55952629937`.

Fresh correction consumed and preserved: account03/B16 `QFORM-PROJECTION-CAP-NONZERO-PIVOT-BARRIER-v1`, canonical mathematics `bf4ea19e3c7e327cd53615128f4daaeee0e53811`. A bounded two-dimensional receiver density, even with bounded one-dimensional marginals, does NOT by itself control an arbitrary nonzero-pivot quadratic trace: there are cap-one dependent `(U,V)` for which `X^2+2UV` has arbitrarily large density. The theorem below therefore contains an additional nonzero **cross-transverse determinant resource**. It does not assert the refuted cap-only statement.

## 2. New analytic lemma — cross-transverse projection-product smoothing

### Theorem 2.1 (`QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1`)

Let `X` be a real random variable of density at most one. Let `Y=(U,V)` be an independent two-dimensional random vector with joint density `rho_Y` satisfying

`||rho_Y||_infinity <= M`.

Let `B` be an invertible real symmetric `3x3` matrix. Relative to the splitting `R e_0 direct_sum R^2`, write

`B = [[a, b^T],[b,C]]`.

Assume `b != 0`. Rotate only inside the two-dimensional `Y`-plane so that `b=(beta,0)`, `beta=||b||>0`, and write

`C=[[c,d],[d,e]]`.

Define

`D=|det B|`,
`P=beta^2 |e|`.

If `P>0`, then the homogeneous quadratic form

`Q=(X,Y)^T B (X,Y)`

has an essentially bounded density and

`||p_Q||_infinity <= C_* M^(2/3) (D P)^(-1/6),`                 (2.1)

where

`C_* = 103680^(1/3) = 46.9784116940...`.

The same estimate remains valid with arbitrary deterministic affine terms, because the rank-two fractional estimate used below allows arbitrary affine terms in its two actual variables.

### Proof

The rotation is performed only in the receiver `Y`-plane; it does not mix `X` with `Y`. Hence `X` remains independent of the transformed `Y`, and the joint density cap of `Y` remains `M`.

Because `e !=0`, shear the receiver plane by

`W=V+(d/e)U`.

This change has determinant one, so the joint density of `(U,W)` is still at most `M`. Put

`sigma=c-d^2/e`.

Then

`Q = a X^2 + 2 beta X U + sigma U^2 + e W^2`.                 (2.2)

Fix an output value `t` and a parameter `delta>0`. Introduce the physical scalar slope coordinate

`r=aX+beta U`.

Split the density contribution into the region `|r|>=delta` and the region `|r|<delta`.

#### Far-slope part

Condition on `(U,W)`. As a function of `x`, the derivative of (2.2) is

`2(a x+beta U)=2r`.

There are at most two inverse branches. On `|r|>=delta`, each branch contributes at most `1/(2 delta)` because `f_X<=1`. Thus the total far-slope density is bounded by

`p_far(t) <= delta^(-1)`.                                    (2.3)

This uses the actual independent physical scalar `X`; no conditional receiver-density assertion is made.

#### Near-slope part

For fixed `x`, change variables from `u` to `r=a x+beta u`, so `du=dr/beta`. Integrating the `W` variable on the two roots of `eW^2=H_t(r,x)` gives the bound

`p_near(t)
 <= M/(beta sqrt(|e|))
    integral f_X(x) integral_{|r|<delta} |H_t(r,x)|^(-1/2) dr dx`,     (2.4)

where

`H_t(r,x)=t-2rx+a x^2-(sigma/beta^2)(r-a x)^2`                    (2.5)

(up to harmless affine terms if they were present initially).

The quadratic coefficient matrix of `H_t` in `(r,x)` is

`K=[[-s, as-1],[as-1,a-a^2s]],    s=sigma/beta^2`,                 (2.6)

and a direct determinant computation gives

`det K = as-1`.                                                   (2.7)

On the other hand the determinant of (2.2) is

`det B = e(a sigma-beta^2)=e beta^2(as-1)`,                       (2.8)

so

`|det K| = D/P`.                                                  (2.9)

Let `R_delta` be uniform on `[-delta,delta]`, independent of `X`. Its density cap is `(2delta)^(-1)`. Rescaling the first variable in `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` therefore yields

`E |H_t(R_delta,X)|^(-1/2)
 <= 16 sqrt(30) (2delta)^(-1/2) |det K|^(-1/4)`.                  (2.10)

Multiplying by the interval length `2delta` and using (2.9) in (2.4),

`p_near(t)
 <= 16 sqrt(60) M delta^(1/2) (D P)^(-1/4)`.                     (2.11)

Combining (2.3) and (2.11),

`p_Q(t) <= delta^(-1) + B_0 delta^(1/2),`

`B_0=16 sqrt(60) M(DP)^(-1/4)`.                                 (2.12)

The minimum occurs at `delta=(2/B_0)^(2/3)` and equals

`3*2^(-2/3) B_0^(2/3)
 =103680^(1/3) M^(2/3)(DP)^(-1/6)`.                              (2.13)

The bound is uniform in `t`, proving (2.1) and absolute continuity. QED.

## 3. Spectral geometry forces the missing transverse resource at a near-null coloop

The preceding theorem deliberately does **not** claim that a two-dimensional projection cap alone suffices. The key point is that at an exact spectral coloop with a small scalar diagonal, the three-large-eigenvalue hypothesis itself forces `P` to be comparable to `D`.

### Lemma 3.1 (`QFORM-NEAR-NULL-SPECTRAL-CROSS-RESOURCE-v1`)

Let `B=[[a,b^T],[b,C]]` be real symmetric `3x3` and suppose every eigenvalue of `B` has absolute value at least one. Put `D=|det B|`. If

`|a| <= tau <1`,                                                   (3.1)

then `b!=0`; after rotating the receiver plane so `b=(beta,0)` and writing `C=[[c,d],[d,e]]`,

`P=beta^2|e| >= (1-tau)D`.                                        (3.2)

### Proof

The determinant identity is

`det B = a det C - beta^2 e`.                                      (3.3)

If `det C=0`, (3.3) gives `P=D`, so (3.2) follows.

Assume `det C!=0`. The scalar Schur complement is

`s=a-b^T C^(-1)b`,

and `(B^(-1))_00=s^(-1)`. Since `B` is symmetric and every eigenvalue has absolute value at least one,

`||B^(-1)||_op <=1`.

Therefore `|s^(-1)|<=1`, so `|s|>=1`. Since `det B=(det C)s`,

`|det C| <= D`.                                                    (3.4)

Now (3.3) and the reverse triangle inequality give

`P=|beta^2e|
 =|a det C-det B|
 >=D-|a||det C|
 >=(1-tau)D`.                                                      (3.5)

If `b=0`, then `s=a`; (3.1) would contradict `|s|>=1`, so `b!=0`. QED.

This is exactly the extra information absent from the receiver-only counterexample `X^2+2UV`: there the scalar coefficient is `a=1`, so the near-null hypothesis (3.1) fails and no transverse scalar-leaf coupling is forced.

## 4. Corollary — every exact spectral coloop is now uniformly paid

Let

`A=U Lambda U^T`, `U^T U=I_3`, `|lambda_j|>=1`,                    (4.1)

be an exact-rank-three target. Suppose some original physical coordinate `i` has spectral leverage exactly one:

`||U^T e_i||^2=1`.                                                  (4.2)

Then the other physical rows lie in the orthogonal two-dimensional spectral plane. Choose the spectral basis so the coloop row is `e_1`. The remaining product source projects to a two-dimensional vector `Y`; the sharp bounded-density product-projection theorem gives

`||p_Y||_infinity <=2`.                                            (4.3)

The coloop scalar `X_i` is genuinely independent of `Y`. In coordinates `(X_i,Y)`, the coefficient matrix `B` is orthogonally congruent to `Lambda`, hence

`D=|det B|=|det Lambda|>=1`.                                       (4.4)

Let `a=A_ii`.

### Near-null half: `|a|<=1/2`

Lemma 3.1 gives `P>=D/2`. Theorem 2.1 with `M<=2` gives

`||p_Q||_infinity
 <= C_* 2^(2/3)(D^2/2)^(-1/6)
 = C_* 2^(5/6) D^(-1/3)
 <83.707`.                                                         (4.5)

This includes every nonzero near-null coloop and the exact null endpoint. It is two-sided: no one-sheet restriction is used.

### Non-small half: `|a|>1/2`

Apply the completed exact-rank-three Schur consequence (1.2) of `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`. Here the coloop leverage is `c_i=1`, so

`||p_Q||_infinity
 <=128 (|a|D)^(-1/4)
 <=128*2^(1/4)
 <152.219`.                                                        (4.6)

Thus every exact spectral-coloop target satisfies

`boxed(||p_Q||_infinity <153)`.                                    (4.7)

This closes the formerly unpaid interpolation between the exact-null coloop theorem and the nonzero scalar-pivot estimate. It does **not** claim that every exact-rank-three frame has a coloop, and it does not control arbitrary higher-rank extra spectrum.

## 5. Required designated-partner application to an actual inequality

The newest account02/B16 family has, in its orthonormal three-dimensional core,

`B_delta=[[delta,c_delta,0],[c_delta,0,0],[0,0,1]],`
`c_delta=sqrt(1+|delta|)`.                                         (5.1)

For this matrix

`D=|det B_delta|=c_delta^2=1+|delta|`,
`P=c_delta^2=D`,                                                   (5.2)

and the genuine same-bank two-dimensional leaf projection has density cap `M<=2`.

Therefore Theorem 2.1 itself gives the source-valid receiver bound

`||p_Q||_infinity
 <= C_* 2^(2/3) D^(-1/3)
 <74.574(1+|delta|)^(-1/3)`.                                      (5.3)

Now apply the **completed designated-partner result** `QFORM-SAME-BANK-NULL-HUB-MIXED-FRESNEL-v1` to the same form. Because its augmented Gram matrix is exactly `diag(c_delta^2,1)` with row leverage `2/m<=1/2`, the partner obtains the substantially sharper actual inequality

`||p_Q||_infinity
 <=3*2^(4/3) D^(-1/3)
 <=7.55952629937`.                                                 (5.4)

Thus the partner's full-product mixed-Fresnel theorem improves the cap-only cross-transverse estimate by a factor of about `9.87` on this model, but both remain uniform through `delta=0`. More importantly, (5.3) shows that in the exact-coloop near-null geometry the projection cap is sufficient **once the forced transverse determinant resource `P>=D/2` is retained**. This does not contradict the account03/B16 projection-cap barrier, whose adversarial example has `P=0` and `a=1`.

## 6. Interaction with the previous account02/B16 Pluecker theorem

The preceding completed account02/B16 theorem `QFORM-DISJOINT-PLUECKER-TWO-BANK-v1`, canonical `math-open-problems@229bfc27cc54adbfdc259c822d11f078483cedee`, gives for exact rank three

`||p_Q||_infinity <=6e |det Lambda|^(-1/3) D_disj^(-1/6)`           (6.1)

whenever the disjoint Pluecker mass `D_disj>0`, with continuity on that branch. In its `D_disj=0` base-packing complement, the rank-two witness leaves an exact spectral coloop; the prior B16 analysis had paid the exact-null point but not the nonzero near-null interpolation. Corollary (4.7) now pays that coloop endpoint for every value of its scalar diagonal. The rank-zero/rank-one base-packing witnesses remain paid by the completed finite-line-bank compression theorem as recorded in the previous B16 handoff.

Consequently, the **entire exact `D_disj=0` endpoint of that Pluecker route is now paid**. This is still not the full exact-rank-three theorem: quantitatively tiny but nonzero `D_disj` can make (6.1) arbitrarily large, and a frame in that collar need not contain an exact coloop.

## 7. What remains unpaid

The first remaining implication for this slot is now

`QFORM-APPROXIMATE-COLOOP-CROSS-TRANSVERSE-v1`:

replace the exact leverage-one coloop by an **approximate** high-leverage row in strict `N3`, retaining the original-product provenance of the residual leaf plane and proving that either

1. a quantitative cross-transverse resource survives and the argument above can be stabilized;
2. the newest mixed-Fresnel augmented Gram packet applies;
3. or a determinant-pair / D' / D5 / finite-core / grouped-bank exit is quantitatively available.

The difficulty is that an approximate coloop no longer makes the physical scalar independent of the full two-dimensional residual spectral projection; a naive spectral rotation or conditional projection cap would reintroduce the refuted dependence interfaces. Arbitrary additional nonzero spectrum remains a separate global obstacle.

No full-solution status is promoted. Continuity is proved only on previously Fourier-integrable branches, not by Theorem 2.1 in general.
