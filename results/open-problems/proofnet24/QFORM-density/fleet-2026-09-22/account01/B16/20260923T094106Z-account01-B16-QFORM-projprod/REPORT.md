SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T09:41:06Z.
attacking: projection-product interaction in the overlapping-source line/plane transition, retaining shared original-coordinate sources through a translated independent square rather than replacing them by an arbitrary joint projection density.

# account01/B16 — rank-two product half-Riesz plus translated-square smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Projection-product interaction  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN`  
**Continuity:** not claimed by the new theorem below; all density conclusions are essential-supremum bounds unless stated otherwise.

## 1. Fresh control, corrections, and pinned dependencies


The proof below explicitly preserves the live corrections:

- a bounded joint density of a projected vector does **not** by itself control an indefinite quadratic level-set integral (`QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`);
- normalized conditional projection density caps can diverge (`QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1` and partner B16 near-coloop conditional blowup);
- projected coordinates are not declared independent after rotation (`QFORM-NO-INDEPENDENCE-AFTER-ROTATION`);
- generic absolute slice-Wiener and fiberwise trace mechanisms are not used.

The main analytic dependency is the completed orientation-free rank-two fractional theorem:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`  
`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`  
source theorem `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`.

It states that if `U` is `n x 2` with `U^T U=I_2`, `Lambda` is invertible symmetric `2 x 2`, and `b` is arbitrary, then for independent cap-one inputs

`sup_t E |(U^T X)^T Lambda(U^T X)+b^T X-t|^(-1/2) <= 128 |det Lambda|^(-1/4)`.      (1.1)

If `b` belongs to `range(U)`, including `b=0`, the constant improves to `16 sqrt(30)`.

The scalar product-projection input used below is the source-valid Rogozin--Ball bound recorded in that same pinned report: if `||a||_2=1`, then `a^T X` has density at most `sqrt(2)`. Thus `n^T X` has density at most `sqrt(2)/||n||_2`. For a singleton source `n X_j`, the sharper elementary bound is exactly `1/|n|`.

The designated partner result actually consumed is account02/B16 r26:

`yspennstate/math-open-problems@df9ef8e92ae2669eb101e2a1b076594af329dc52`  
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T071608Z-account02-B16-QFORM-r26/REPORT.md`.

It constructs an exact target-valid near-coloop family with a same-bank overlapping pair `(T,U)`, proves the normalized conditional cap `||p_(U|T=t)||_infinity` is unbounded, and nevertheless gives a source-valid grouped-bank bound `<23` for the full family. This report attacks precisely the overlap mechanism exposed there.

## 2. Main theorem: translated independent square over a rank-two product quadratic

### Theorem 2.1 — `QFORM-RANK2-PRODUCT-HALFRIESZ-TRANSLATED-SQUARE-v1`

Let `I,J` be disjoint sets of original coordinates. All coordinates are independent and each has a density bounded by one. Let

`Y = M X_I in R^2`,

where `M` is a real `2 x |I|` matrix of rank two, and let

`Z = n^T X_J`, `n != 0`.

Let `B` be an invertible real symmetric `2 x 2` matrix, `d in R^{|I|}`, `c in R`, `gamma != 0`, and let `h=h(X_I)` be an arbitrary measurable real function. Define

`R = Y^T B Y + d^T X_I + c`,                                      (2.1)

`Q = R + gamma (Z+h(X_I))^2`.                                    (2.2)

Put

`Delta_M = det(M M^T) >0`, `D_B=|det B|`.                         (2.3)

Then `Q` has an absolutely continuous law and

`||p_Q||_infinity
 <= 128 sqrt(2) /(||n||_2 sqrt(|gamma|))
       * (Delta_M D_B)^(-1/4)`.                                  (2.4)

If `d` lies in the row span of `M` (in particular if `d=0`), then

`||p_Q||_infinity
 <= 16 sqrt(60) /(||n||_2 sqrt(|gamma|))
       * (Delta_M D_B)^(-1/4)`.                                  (2.5)

If `J` consists of a single original coordinate and `Z=nu X_j`, the `sqrt(2)/||n||_2` scalar-projection factor is replaced by the exact `1/|nu|`. Thus the constants in (2.4),(2.5) improve respectively to `128` and `16 sqrt(30)` after replacing `||n||_2` by `|nu|`.

The function `h` may reuse all of the `I`-bank sources and may be strongly dependent on `Y`. No density assumption on `(Y,h)` and no conditional density cap for `Y` given `h` are required.

### Proof

Let

`S=(M M^T)^(1/2)`, `W=S^(-1) M`.                                 (2.6)

Then `W W^T=I_2`. Equivalently, `U=W^T` has two orthonormal columns. Also

`Y=S W X_I`

and therefore

`Y^T B Y=(W X_I)^T Lambda (W X_I)`,

with

`Lambda=S B S`,

`|det Lambda|=det(MM^T)|det B|=Delta_M D_B`.                     (2.7)

Apply the pinned rank-two half-Riesz theorem (1.1) to the `I`-bank. It gives, uniformly in `q in R`,

`E |q-R|^(-1/2) <= 128 (Delta_M D_B)^(-1/4)`.                   (2.8)

If `d` is in the row span of `M`, it belongs to `range(U)` after the normalization (2.6), and the sharper version gives

`E |q-R|^(-1/2) <= 16 sqrt(30) (Delta_M D_B)^(-1/4)`.           (2.9)

Now use genuine independence of the **original disjoint source banks** `I` and `J`. Let `f_Z` be a density of `Z` and set `K_Z=||f_Z||_infinity`. By the scalar product-projection theorem,

`K_Z <= sqrt(2)/||n||_2`.                                        (2.10)

Fix the entire `I`-bank. Then `h=h(X_I)` and `R` are deterministic, while `Z` remains independent with density `f_Z`. For `gamma>0`, the conditional density of

`gamma(Z+h)^2`

at `y>0` is

`g_h(y)= [f_Z(-h+sqrt(y/gamma))+f_Z(-h-sqrt(y/gamma))]
          /(2 sqrt(gamma y))`,                                  (2.11)

so

`g_h(y) <= K_Z/(sqrt(gamma) sqrt(y))`.                           (2.12)

For `gamma<0`, reflect the output variable and obtain the same bound with `|gamma|`. Consequently, for almost every `q`, the mixture formula gives

`p_Q(q)
 = E_I g_{h(X_I)}(q-R)
 <= K_Z |gamma|^(-1/2) E_I |q-R|^(-1/2)`.                       (2.13)

The indicator of the correct sign of `q-R` was dropped in the final upper bound. Combining (2.10) with (2.8) proves (2.4), and combining (2.10) with (2.9) proves (2.5). The same conditional-density formula and Tonelli show absolute continuity of the mixture. If `J` is a singleton, `||p_(nu X_j)||_infinity<=1/|nu|`, which gives the stated sharpened constants. QED.

### Why this does not violate the live coarea correction

The proof never says that the bounded joint density of `Y` controls an indefinite level-set integral. Instead, the nonlinear one-dimensional square is integrated **conditionally on the true independent source bank** `J`; its only singularity is `|q-R|^(-1/2)`. The expectation of exactly that fractional kernel is then paid by the completed rank-two product-source theorem (1.1). The arbitrary shared-source translation `h(X_I)` disappears from the upper bound before any projection density is invoked. This is the desired product-provenance/curvature interaction.

## 3. One-sided overlapping line/plane transducer

The preceding theorem pays a substantially larger class than a disjoint line bank plus disjoint plane bank.

### Corollary 3.1 — `QFORM-ONE-SIDED-OVERLAP-LINE-PLANE-v1`

With the same disjoint original source banks `I,J`, let

`Y=M X_I in R^2`, `L=r^T X_I`, `Z=n^T X_J`,                     (3.1)

so `L` may be arbitrarily dependent on the plane projection `Y`. Let

`Gamma = [[C,b],[b^T,gamma]]`                                   (3.2)

be a real symmetric invertible `3 x 3` matrix, with `gamma !=0`. Consider

`Q = (Y,L+Z)^T Gamma (Y,L+Z)`.                                  (3.3)

Then

`||p_Q||_infinity
 <= 16 sqrt(60) /||n||_2
      * [ det(MM^T) |gamma| |det Gamma| ]^(-1/4)`.              (3.4)

If `Z=nu X_j` is a singleton original coordinate, then

`||p_Q||_infinity
 <= 16 sqrt(30) /|nu|
      * [ det(MM^T) |gamma| |det Gamma| ]^(-1/4)`.              (3.5)

#### Proof

Complete the square only in the line coordinate:

`S_2 = C-b b^T/gamma`,                                          (3.6)

`Q = Y^T S_2 Y
     + gamma [ Z + L + gamma^(-1) b^T Y ]^2`.                  (3.7)

Because `Gamma` and `gamma` are nonzero,

`det S_2 = det Gamma/gamma`,                                    (3.8)

so `S_2` is invertible. Apply Theorem 2.1 with `B=S_2`, `d=0`, and

`h(X_I)=L+gamma^(-1)b^T Y`.                                     (3.9)

Equation (2.5) and (3.8) give

`|gamma|^(-1/2) |det S_2|^(-1/4)
 = (|gamma| |det Gamma|)^(-1/4)`,                               (3.10)

which proves (3.4); the singleton improvement proves (3.5). QED.

The conceptual point is that **all line leakage carried by the same sources as the plane projection is allowed**. Only one genuinely disjoint line innovation `Z` is needed. This directly addresses the earlier B16 debt `QFORM-OVERLAPPING-LINE-PLANE-SOURCE-TRANSITION-v1` throughout the non-isotropic line-pivot region `gamma !=0`.

## 4. Exact-rank-three physical-row corollary

Let an exact-rank-three target be written

`A=R Lambda R^T`, `R^T R=I_3`,                                 (4.1)

with invertible symmetric `Lambda`. Pick any physical row `r_i` with

`c_i=||r_i||_2^2>0`, `e=r_i/sqrt(c_i)`.                         (4.2)

Use the spectral decomposition `R^3=e^perp direct_sum span(e)`. For every `k != i`, decompose

`r_k=v_k+alpha_k e`, `v_k in e^perp`.                           (4.3)

Choose an orthonormal basis of `e^perp` and let `M` have columns/rows giving the coefficients `v_k`; define

`Y=sum_{k!=i} v_k X_k`, `L=sum_{k!=i} alpha_k X_k`,
`Z=sqrt(c_i) X_i`.                                              (4.4)

Parseval gives the exact identity

`M M^T = I_2`.                                                   (4.5)

Indeed the removed row `r_i` is purely in the `e` direction and contributes no plane component.

Write `Lambda` in the plane/line basis as `Gamma` from (3.2). Then

`gamma=e^T Lambda e=A_ii/c_i`,                                  (4.6)

and `det Gamma=det Lambda`. If `A_ii !=0`, Corollary 3.1 with the **singleton** innovation `Z=sqrt(c_i)X_i` gives

`||p_(X^T A X)||_infinity
 <=16 sqrt(30) [ c_i |A_ii| |det Lambda| ]^(-1/4)`.             (4.7)

This is a source-aligned constant improvement, for the full exact-rank-three form without extra affine perturbations, over the general-affine constant `128` in the pinned rank-three Schur consequence.

More importantly, the same calculation explains the already-completed full-ambient theorem. If one conditions on arbitrary outside original coordinates, cross couplings induce an arbitrary affine term in the retained source bank. The scalar affine coefficient is absorbed into the translated square, while the remaining affine term is covered by the `128` version of Theorem 2.1. One obtains exactly

`||p_Q||_infinity
 <=128 [ c_i |A_ii| |det Lambda| ]^(-1/4),                      (4.8)

which matches the source-pinned `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1`. Thus the translated-square transducer gives a direct product-provenance derivation of that theorem and shows precisely why same-bank line leakage does not create a new difficulty when the normalized line curvature `gamma` is nonzero.

For a near-coloop `c_i>63/64`, (4.7) pays every quantitatively non-isotropic pivot `|gamma|>=tau>0` with a constant depending only on `tau` (and the target spectral determinant, which is at least one when all three nonzero eigenvalues have modulus at least one). The genuinely difficult transition is therefore the **near-isotropic/null line pivot** `gamma ->0`, not the overlap itself.

## 5. Application of the completed account02/B16 partner result

Partner account02/B16 r26 considers even `m>=66`, `0<a<1/64`, `c=1-a`, balanced signs `eps_j`, and the exact target-valid form

`Q_a = 2 (sqrt(c) X_0 + sqrt(a) T) U + V^2`,                    (5.1)

where

`T=m^(-1/2) sum_{j=1}^m X_j`,
`U=m^(-1/2) sum eps_j X_j`,
`V=m^(-1/2) sum_{j=m+1}^{2m} X_j`.                              (5.2)

The spectral target is exactly `{1,-1,1}`. The pair `(T,U)` uses the same first leaf bank; the partner proves that a normalized conditional projection route fails because `||p_(U|T=t)||_infinity` is unbounded near a cube corner.

### 5.1 Direct application of the new theorem

Set

`L_*=sqrt(c)X_0+sqrt(a)T`, `Y=(L_*,U)`.                          (5.3)

The coefficient vectors of `L_*` and `U` are orthonormal: their squared norms are `c+a=1` and `1`, while their inner product is

`sqrt(a) m^(-1) sum eps_j=0`.                                   (5.4)

Hence `MM^T=I_2`. Also

`2L_*U = Y^T [[0,1],[1,0]] Y`,                                  (5.5)

whose determinant modulus is one. The disjoint second-bank scalar projection `V` has normalized coefficient vector, so `||n||_2=1`. Theorem 2.1 therefore gives, for arbitrary cap-one independent source laws,

`||p_(Q_a)||_infinity <=16 sqrt(60)
 =123.9354670786...`.                                           (5.6)

This is not the best constant for the partner family, but it is a completely source-valid proof that directly tolerates the same-bank overlap `(T,U)` without conditioning one on the other. More generally, for **any measurable source-dependent translation** `h=h(X_0,X_1,...,X_m)`,

`Q_{a,h}=2L_*U+(V+h)^2`                                         (5.7)

still satisfies the same bound (5.6). This extension is exactly the mechanism Theorem 2.1 is designed to supply.

### 5.2 Applying the completed partner result to an actual stronger inequality

The partner's grouped-source argument is sharper for `h=0`. It splits the first leaf bank by the signs of `eps_j`, conditions on one true independent bank, and obtains a cap-one three-variable quadratic core with smallest eigenvalue magnitude

`sigma=(sqrt(253)-1)/32=0.4658116787...`.                        (5.8)

Applying its pinned localized three-variable theorem yields the actual inequality

`||p_(Q_a)||_infinity
 <=6 sqrt(pi)/sigma
 =6 sqrt(pi)*32/(sqrt(253)-1)
 =22.8305205519... <23`.                                        (5.9)

This completed partner result immediately extends to any independent additional block. If `W` is **any** real random variable generated by further disjoint original coordinates, independent of the sources in (5.1), then convolution with its probability law cannot increase an `L^infinity` density norm, so

`||p_(Q_a+W)||_infinity <=22.8305205519...`.                     (5.10)

In particular, `W` may itself be an arbitrary quadratic form on a disjoint coordinate block, with arbitrary rank and eigenvalues. Thus the partner's target-valid near-coloop family remains uniformly controlled after arbitrary independent block-direct-sum enlargement. Equation (5.10) is a concrete application of the completed designated-partner result, not merely a citation.

The partner family has normalized dominant-line curvature `gamma=0`, so Corollary 3.1 intentionally does not cover it. The partner's regrouping result is therefore complementary rather than redundant.

## 6. What the theorem pays and what remains open

The new theorem settles a real part of the overlap transition:

- a rank-two original-product quadratic can be smoothed by one independent translated square;
- the square translation may depend arbitrarily on every source in the rank-two bank;
- a one-sided line/plane decomposition therefore does **not** require the same-bank line leakage to be independent of the plane projection;
- for an exact-rank-three frame, every nonzero physical row supplies a genuine independent singleton line innovation; if the normalized line curvature `gamma=e^T Lambda e` is nonzero, all same-bank line leakage is absorbed into the translated square exactly.

This leaves a sharply defined first unpaid implication:

`QFORM-NULL-OVERLAP-LINE-PLANE-TRANSDUCER-v1`.

In the exact-rank-three near-coloop chamber, treat uniformly the case in which the normalized physical line pivot

`gamma=e^T Lambda e`

is zero or quantitatively very small, while the residual line leakage and the planar projection reuse the same original sources. One must either:

1. retain the unnormalized same-bank product density through the null bilinear/transverse-curvature integration; or
2. prove a bounded-number regrouping into genuinely disjoint original source banks with a quantitatively nondegenerate curved receiver; or
3. force one of the already-paid physical-pair, ridge-window, cross-transverse, mixed-Fresnel, finite-bank, or grouped-bank exits.

At `gamma=0`, conditioning on the independent hub scalar produces a reciprocal linear factor `1/|b^T Y|`; a bare two-dimensional projected density cap does not integrate that singularity by itself, and the live corrections forbid replacing the remaining same-bank dependence by an arbitrary-joint coarea estimate. Partner r26 shows one special null family can be repaired by sign-bank regrouping, but that symmetry is not available in a general near-coloop frame.

The unrestricted higher-rank target also remains open. The theorem here is an essential supporting step, not a full solution.

## 7. Continuity

Theorem 2.1 proves absolute continuity and an essential `L^infinity` bound by an explicit conditional-density mixture. It does **not** by itself prove that the resulting density has a continuous representative for arbitrary cap-one source densities and arbitrary measurable translation `h`. No continuity claim is promoted from this argument. Continuity remains a separately tracked target exactly as requested.

## 8. Telemetry / scope integrity

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort and provider reasoning-token counters were not exposed. Execution label remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository state and source-pinned peer mathematics were used, but no authenticated native learned-memory receiver ingestion was established.

No schedule, notification, email, permission, account binding, public-release setting, or task count was changed.
