SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-24T10:05:03Z.
attacking: the punctured physical-pivot collar via a mixed L^3–L^{3/2} coarea receiver that spends an independent transverse square before any scalar half-Riesz peel.

# account01/B05 auto11 — mixed L3 receiver across the null-pivot interface

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea / equivalent interval bound preserving arbitrary product densities.  
**Status:** `NEW SUPPORTING ANALYTIC THEOREM / PUNCTURED SPLIT-SOURCE COLLAR PAID / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Immediate debt and mechanism change

The preceding B05 run proved that the standard scalar completion

`physical pivot -> one-sided square kernel -> half-Riesz Schur remainder`

necessarily loses `log(1/|a|)` on the exact target family

`Q=a H^2+2tHL+W^2`

as the physical pivot `a` tends to zero, although the true output density remains uniformly bounded. The missing operation is to spend the third curvature before taking the scalar half-Riesz majorant.

This run changes mechanism accordingly. Instead of estimating a pointwise square kernel, I first prove an `L^3` bound for the complete bilinear-plus-hub phase and pair it by Young with the `L^{3/2}` density of the independent square. The null-pivot interface disappears completely.

No rotation of the random coordinates is used. All independence below is literal source independence. No moment, support, log-concavity, connected-support, Gaussian, or pointwise oscillatory-decay assumption is used.

## 2. Bilinear-plus-arbitrary-hub L3 lemma

### Lemma 2.1 — `QFORM-BILINEAR-HUB-L3-v1`

Let `H,L` be independent real random variables with probability densities `f_H,f_L` satisfying

`||f_H||_infinity <= m_H`, `||f_L||_infinity <= m_L`.

Let `t != 0`, and let `q:R->R` be any Borel function. Then

`R=q(H)+2tHL`

has a density `p_R in L^3(R)` with

`boxed: ||p_R||_3 <= 3 |t|^(-2/3) (m_H m_L)^(2/3).`                 (2.1)

The constant is independent of `q`; in particular it is independent of an arbitrarily large or arbitrarily small quadratic pivot hidden in `q(H)`.

### Proof

Condition on `H=h`. For `h != 0`, the conditional density is

`k_h(r)= [1/(2|t h|)] f_L((r-q(h))/(2th)).`                         (2.2)

Translation by `q(h)` does not change an `L^3` norm, and scaling gives

`||k_h||_3=(2|t h|)^(-2/3)||f_L||_3`.                               (2.3)

Since `f_L<=m_L` and `int f_L=1`,

`||f_L||_3 <= m_L^(2/3)`.                                           (2.4)

Minkowski therefore gives

`||p_R||_3
 <=2^(-2/3)|t|^(-2/3)m_L^(2/3)
   int f_H(h)|h|^(-2/3) dh.`                                        (2.5)

The last weighted integral is maximized, subject to `0<=f_H<=m_H` and `int f_H=1`, by filling the interval centered at the origin. Hence

`int f_H(h)|h|^(-2/3)dh
 <=m_H int_{|h|<=1/(2m_H)} |h|^(-2/3)dh
 =6*2^(-1/3)m_H^(2/3).`                                             (2.6)

Multiplying (2.5) and (2.6) yields exactly

`2^(-2/3)*6*2^(-1/3)=3`,                                            (2.7)

which proves (2.1). The null set `h=0` is irrelevant. QED.

The point is structural: an arbitrary self-phase `q(H)` is harmless at the `L^3` level because it only translates the conditional `L` density. This is exactly the cancellation lost by a scalar half-Riesz peel.

## 3. Shifted square L3/2 lemma

### Lemma 3.1 — `QFORM-SHIFTED-SQUARE-L32-v1`

Let `W` have probability density `f_W` with `||f_W||_infinity<=m_W`. For every `lambda !=0` and every real shift `s`,

`S=lambda(W-s)^2`

has a density `p_S in L^(3/2)(R)` with

`boxed: ||p_S||_(3/2) <=2 m_W^(2/3)|lambda|^(-1/3).`                (3.1)

### Proof

Translations of `W` preserve the density cap, so take `s=0`; reflection handles `lambda<0`. For `lambda>0`, put

`F(r)=f_W(r)+f_W(-r)`, `r>0`.

Then `0<=F<=2m_W`, `int_0^infinity F(r)dr=1`, and

`p_S(y)=F(sqrt(y/lambda))/(2 lambda sqrt(y/lambda))`, `y>0`.          (3.2)

Using `y=lambda r^2`,

`int p_S(y)^(3/2)dy
 =2^(-1/2)lambda^(-1/2)
   int_0^infinity F(r)^(3/2)r^(-1/2)dr.`                             (3.3)

Since `F^(3/2)<=sqrt(2m_W)F`, and the weighted integral of `F` is maximized by `F=2m_W` on `[0,1/(2m_W)]`,

`int_0^infinity F(r)r^(-1/2)dr<=2sqrt(2m_W)`.                        (3.4)

Thus

`int p_S^(3/2)<=2sqrt(2)m_W lambda^(-1/2)`.                          (3.5)

Raising (3.5) to the power `2/3` gives (3.1). QED.

## 4. Main mixed-curvature receiver

### Theorem 4.1 — `QFORM-MIXED-L3-SQUARE-RECEIVER-v1`

Let `H,L,W` be mutually independent with density caps `m_H,m_L,m_W`. Let `t lambda !=0`, let `q` be arbitrary Borel, and let `s,c` be arbitrary reals. Then

`Q=q(H)+2tHL+lambda(W-s)^2+c`                                       (4.1)

has a bounded continuous density vanishing at infinity, and

`boxed:
 ||p_Q||_infinity
 <=6 |t|^(-2/3)|lambda|^(-1/3)
      (m_H m_L m_W)^(2/3).`                                         (4.2)

### Proof

Set `R=q(H)+2tHL` and `S=lambda(W-s)^2`. Literal source independence gives `R independent of S`, hence

`p_Q=p_R*p_S` up to translation by `c`.                              (4.3)

By Lemmas 2.1 and 3.1 and Young's conjugate-exponent inequality,

`||p_Q||_infinity
 <=||p_R||_3 ||p_S||_(3/2)
 <=3*2 |t|^(-2/3)|lambda|^(-1/3)
   (m_Hm_Lm_W)^(2/3)`,                                               (4.4)

which is (4.2).

Moreover `p_R in L^3` and `p_S in L^(3/2)`. Convolution of conjugate finite-`p` functions is continuous and vanishes at infinity: translation continuity in `L^(3/2)` and Holder give

`|(p_R*p_S)(x+h)-(p_R*p_S)(x)|
 <=||p_R||_3 ||tau_h p_S-p_S||_(3/2) ->0`.                           (4.5)

QED.

### Affine robustness

The theorem immediately covers

`aH^2+2tHL+bH+dL+lambda W^2+eW+c`                                  (4.6)

with exactly the same bound. Shift `H` by `d/(2t)` so that the `L`-term becomes `2tHL`, absorb the resulting one-variable polynomial into `q(H)`, and shift `W` by `e/(2lambda)`. These are coordinatewise translations and preserve both density caps and independence.

Thus the estimate is completely uniform in the physical pivot `a`, including `a=0`, `a->0+`, and `a->0-`.

## 5. Conditional original-coordinate corollary

The preceding theorem is useful inside a full ambient quadratic form without assuming the ambient remainder is independent.

Suppose three literal original coordinates `(H,L,W)` have principal quadratic block

`B=[[a,t,0],[t,0,0],[0,0,lambda]]`, `t lambda !=0`.                  (5.1)

Condition on **all other original coordinates**. Because the input law is a product law, `H,L,W` remain mutually independent with the same density caps. Every outside coupling becomes only an affine term in `(H,L,W)`, so the conditional form is exactly of type (4.6). Therefore the conditional output density is bounded by (4.2), uniformly in the conditioning variables. Averaging gives

`boxed:
 ||p_(X^T A X)||_infinity
 <=6 |t|^(-2/3)|lambda|^(-1/3)
      (m_Hm_Lm_W)^(2/3).`                                           (5.2)

For cap-one inputs,

`boxed: ||p_(X^T A X)||_infinity <=6 (|t|^2|lambda|)^(-1/3).`        (5.3)

Each conditional density is continuous and bounded by the same constant; dominated convergence therefore also gives a continuous density for the unconditional output in this branch.

This is a genuine product-preserving localized theorem. The zero on the second diagonal in (5.1) is an actual structural hypothesis; it is not silently inferred from the spectral assumptions.

## 6. The previous logarithmic stress family is now paid at constant 6

Take the exact-target family from the preceding B05 run,

`Q_(eps,sigma)=sigma eps H^2+2sqrt(1+eps) H L+W^2`,                  (6.1)

where `H,L,W` are independent cap-one variables, `0<=eps<=1/16`, and `sigma in {+1,-1}`. Its matrix spectrum is

- `sigma=+1`: `{1+eps,-1,1}`;
- `sigma=-1`: `{1,-(1+eps),1}`.

Hence every member satisfies the owner's three-large-eigenvalue target exactly.

Theorem 4.1 gives, for both signs and all `eps` including zero,

`boxed:
 ||p_Q||_infinity
 <=6(1+eps)^(-1/3)
 <=6.`                                                              (6.2)

The density is continuous. Compare this with the scalar-pivot half-Riesz certificate proved in the previous run, which grows at least like `c log(1/eps)`. Therefore the logarithmic barrier is removed exactly by the requested operation: retain the full bilinear hub in `L^3`, then spend the independent square in `L^(3/2)` before taking a supremum.

This improves the previous split-product bound `128(1+eps)^(-1/4)` on this family and, more importantly, explains the cancellation analytically rather than by a black-box rank-two bridge.

## 7. Designated account02/B05 theorem applied to an actual inequality

At the exact interface `eps=0`, (6.1) is

`Q_0=2HL+W^2`.                                                       (7.1)

Apply the completed designated-partner theorem account02/B05,
`QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1`, canonical source

`yspennstate/math-open-problems@e7a21ed67b943d7aded714ac17ca48bdab4a1349`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T200516Z-account02-B05-QFORM-auto11c/REPORT.md`.

Here the literal hub has cap one, `(L,W)` has joint density cap one because they are independent original coordinates, and the square coefficient is one. The partner theorem yields the actual endpoint inequality

`boxed: ||p_(Q_0)||_(infinity,ess) <=7.761982175235.`                (7.2)

The new mixed-`L^p` theorem sharpens the same equation to `<=6`, but (7.2) is retained as an independent partner-sourced endpoint certificate and confirms compatibility with the existing fleet chain.

I also consumed the newer account02/B05 theorem `QFORM-WITT-DISJOINT-PLUCKER-CROSSING-v1` at

`yspennstate/math-open-problems@8b902bf20457a12c8ad394ece3808c9a0130a95b`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260924T075515Z-account02-B05-QFORM-r12/REPORT.md`.

That theorem handles a source-sharing zero-pivot Witt branch by aggregate Pluecker crossing. The present theorem does **not** extend it automatically to shared-source nonzero pivots; it supplies the exact stable receiver when the transverse square carrier is genuinely source-disjoint.

## 8. Exact next missing implication

The calculation exposes a stronger natural target than another scalar-pivot estimate.

### `QFORM-INDEFINITE-PAIR-L3-v1`

For independent cap-one `H,L`, symmetric invertible indefinite

`B=[[a,t],[t,b]]`,

and arbitrary affine terms, prove a universal bound of the scale-correct form

`||p_([H,L]B[H,L]^T+affine)||_3
 <=C_2 |det B|^(-1/3).`                                             (8.1)

Theorem 2.1 proves (8.1) with `C_2=3` whenever one physical diagonal is zero. A uniform theorem for both nonzero diagonals would combine with Lemma 3.1 to give

`||p_(rank-two indefinite pair + independent square)||_infinity
 <=2 C_2 (|det B| |lambda|)^(-1/3)`,                                (8.2)

uniformly through the punctured-pivot collar and without any scalar half-Riesz logarithm.

This is the first essential missing implication after the current run. It keeps the correct original-coordinate product provenance and asks only for an `L^3` density norm, which is compatible with the unavoidable logarithmic point singularity of a rank-two indefinite quadratic form.

A proof of (8.1) must not replace the invertible linear image of the product law by an arbitrary bounded joint density: the live arbitrary-joint curved-tube counterexamples rule out that shortcut.

## 9. Scope and status

**Proved this run:** the uniform `L^3` bilinear-hub lemma with arbitrary self-phase; the uniform `L^(3/2)` shifted-square lemma; the mixed receiver (4.2) with a continuous `C_0` density; the conditional ambient principal-block corollary; and the exact target stress family bound `<=6` uniformly across both signs and the null interface.

**Not proved:** (8.1) for a general physical indefinite pair with two nonzero diagonals; a receiver when the square carrier shares original-coordinate sources with the bilinear pair; the arbitrary-rank reduction; the full QFORM conjecture; or full-target continuity.

No counterexample to the owner conjecture is produced.

## 10. Sources actually used

2. Previous account01/B05 scalar-pivot obstruction: `yspennstate/math-open-problems@b2459adaa430f8a8df8c703544128b283e49a3c4:proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260924T085700Z-account01-B05-QFORM-auto11/REPORT.md`.
3. Designated partner endpoint: `yspennstate/math-open-problems@e7a21ed67b943d7aded714ac17ca48bdab4a1349:proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T200516Z-account02-B05-QFORM-auto11c/REPORT.md`.
4. Newest compatible account02/B05 crossing compiler: `yspennstate/math-open-problems@8b902bf20457a12c8ad394ece3808c9a0130a95b:proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260924T075515Z-account02-B05-QFORM-r12/REPORT.md`.

No schedule, task-state, notification, permission, repository-visibility, public-release, cross-account authentication, or paid-model/API setting is changed by this report.