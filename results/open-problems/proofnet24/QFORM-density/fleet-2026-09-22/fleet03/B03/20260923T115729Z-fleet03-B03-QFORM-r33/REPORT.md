SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T11:57:29Z.
attacking: dependence-safe Plancherel selectors — keep an entire dependent coefficient vector intact in the independent-copy estimate, quantify the one/two/three selector integrability thresholds, and feed the two-selector half-Riesz bound through one genuine physical square to recover linear output small-ball scaling.

# fleet03/B03 r33 — dependent-coefficient selectors and the two-selector-plus-square transducer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Status:** `NEW SUPPORTING THEOREM / LINEAR OUTPUT SMALL-BALL PACKET / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.


The unrestricted theorem and unrestricted continuity conclusion remain open.

## 1. Sources actually used

### 1.1 Own immediate predecessor

`yspennstate/math-open-problems@0ef1395ef5636eab3acb9e70130042e4dfcbb644`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T105601Z-fleet03-B03-QFORM-r32/REPORT.md`.

It proved a positive-disjoint-basis determinant-entropy estimate and the weighted independent-copy bound

`int |t|^(-1/2)|phi_Q(t)|^2 dt <=20.102 s_3(A)^(-1/2) delta^(-1/6)`

in its exact angular-cancellation packet, then proved that `delta->0` forces a near-coloop or near-three-coordinate determinant geometry. The present run changes mechanism at that collar: rather than pay another negative power of `delta`, it asks exactly how many genuine original-coordinate scalar selectors are needed for an integrable time estimate when the coefficient vector may itself be dependent.

### 1.2 Designated partner fleet04/B03

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260922T193150Z-fleet04-B03-collision-l2-r1/REPORT.md`.

Only its valid elementary collision lemma is used:

`P(|Y-Y'|<=eps) <=2 eps ||p_Y||_2^2`.                              (1.1)

Its stronger historical weighted-`L^2` compiler is not used.

### 1.3 Product-projection density input

The completed product-projection theorem recorded in

`yspennstate/math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260922T232932Z-fleet02-B16-QFORM-auto11/REPORT.md`

gives, for `V^T V=I_k` and `Y=V^T Z` with `Z` an original-coordinate cap-one product law,

`||p_Y||_infinity <= exp(k/2)`.                                    (1.2)

This is used below only as a true JOINT density cap; no independence among the projected coordinates is inferred.

### 1.4 Newest Claude/Fourier source boundary

The required current Claude package at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was read. Its Fourier report proves the twisted one-dimensional `L^p` estimate and mixed-Fresnel mechanisms and explicitly warns that the full conjecture remains open. The theorem below uses the same correction-safe philosophy — integrated norms of twisted Fourier transforms, never pointwise stationary phase — but targets a different interface: genuinely independent physical selectors coupled to an arbitrarily dependent coefficient vector.

The current volume-stability continuation was also read. Its diffuse cross-volume exits remain complementary: they already pay cross blocks satisfying their volume-marginal gates; the selector mechanism below is useful when one can expose physical scalar channels directly, including concentrated coefficient geometry where no independence of projected coefficient coordinates is available.

## 2. Main theorem: dependent-coefficient selector Plancherel compiler

### Theorem 2.1 — `QFORM-DEPENDENT-COEFFICIENT-SELECTOR-PLANCHEREL-v1`

Let `X_1,...,X_k` be independent real random variables with densities `0<=f_j<=1`. Let `W` be independent of the whole `X`-bank. Let

`C(W)=(C_1(W),...,C_k(W))`

have an arbitrary JOINT density `g_C` satisfying

`||g_C||_infinity <= M`.                                           (2.1)

No independence among the `C_j` is assumed. Let `R(W)` be arbitrary measurable, let `beta_j!=0`, and let `P_j:R->R` be arbitrary measurable one-coordinate phases. Define

`Q=R(W)+sum_{j=1}^k [P_j(X_j)+2 beta_j X_j C_j(W)]`.               (2.2)

Put

`B_k=prod_{j=1}^k |beta_j|`,
`A_k=M pi^k/B_k`.                                                    (2.3)

Then for every `t!=0`,

`boxed: |phi_Q(t)|^2 <= min{1,A_k |t|^(-k)}.`                       (2.4)

#### Proof

For fixed `t`, define the twisted Fourier transform

`F_{j,t}(xi)=int_R f_j(x) exp(i t P_j(x)+i xi x) dx`.               (2.5)

Conditioning only on the full `W`-bank, genuine independence of the ORIGINAL selector coordinates gives the exact product

`phi_Q(t)=E_W[ exp(itR(W)) prod_j F_{j,t}(2 beta_j t C_j(W)) ]`.    (2.6)

Take Cauchy-Schwarz over the whole `W`-bank:

`|phi_Q(t)|^2
 <=E_W prod_j |F_{j,t}(2 beta_j t C_j(W))|^2`.                     (2.7)

The right side depends on `W` only through the whole coefficient vector `C`; using its true joint density cap,

`<= M int_{R^k} prod_j |F_{j,t}(2 beta_j t c_j)|^2 dc`.             (2.8)

Changing variables separately in the deterministic integration variables `c_j`, not in the random input law,

`(2.8)=M prod_j [(2|beta_j t|)^(-1) int_R |F_{j,t}(xi)|^2 dxi]`.   (2.9)

The twist `exp(itP_j(x))` has unit modulus. Plancherel therefore gives

`int |F_{j,t}|^2=2pi int f_j(x)^2 dx <=2pi`,                        (2.10)

because `f_j<=1` and `int f_j=1`. Combining (2.9)-(2.10) gives

`|phi_Q(t)|^2 <= M pi^k |t|^(-k)/B_k=A_k|t|^(-k)`.                 (2.11)

The trivial characteristic-function bound supplies the minimum with one. QED.

### Dependence boundary

The proof never introduces `X_j-X_j'` or `X_j+X_j'` as separate random sources. When the independent-copy identity is invoked below, it is only

`|phi_Q(t)|^2=E exp(it(Q-Q'))`                                     (2.12)

for the complete copy difference. Thus the live sum/difference dependence correction is respected exactly.

## 3. One selector: a full weighted independent-copy time estimate

Take `k=1`, so `A_1=pi M/|beta_1|`. For every `0<alpha<1`, split the exact envelope at `T=A_1`:

`int_R |t|^(-alpha)|phi_Q(t)|^2 dt
 <=2 int_0^T t^(-alpha)dt
   +2A_1 int_T^infinity t^(-1-alpha)dt`

`=boxed: 2 A_1^(1-alpha)/[alpha(1-alpha)].`                         (3.1)

At the half-Riesz exponent,

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <=8 sqrt(pi M/|beta_1|).}`                                         (3.2)

Using

`int_R |t|^(-1/2)e^(itx)dt=sqrt(2pi)|x|^(-1/2)`                    (3.3)

in the usual truncated/monotone Riesz-energy argument and (2.12),

`boxed:
 E|Q-Q'|^(-1/2)
 <=4 sqrt(2) sqrt(M/|beta_1|).}`                                    (3.4)

This is a complete dependence-safe integrated-time estimate. It deliberately does not claim `L^infinity`: one scalar selector is below the output-density threshold.

## 4. Two selectors: L2 collision control AND a one-copy half-Riesz receiver

For `k=2`, set

`K=A_2^(1/2)=pi sqrt(M/B_2)`.                                       (4.1)

Then (2.4) gives

`|phi_Q(t)| <= min(1,K/|t|)`.                                      (4.2)

First,

`int_R |phi_Q(t)|^2dt
 <=2 int_0^K 1 dt+2K^2 int_K^infinity t^(-2)dt
 =4K`.                                                              (4.3)

Hence `Q` has an `L^2` density and

`boxed: ||p_Q||_2^2 <=2 sqrt(M/B_2).}`                              (4.4)

Applying the designated fleet04/B03 lemma (1.1) to this actual new inequality gives

`boxed:
 P(|Q-Q'|<=eps)
 <=4 eps sqrt(M/B_2).}`                                             (4.5)

This is already linear collision small-ball scaling.

More importantly for one-copy density, weight (4.2) by `|t|^(-1/2)`:

`int_R |t|^(-1/2)|phi_Q(t)|dt
 <=2[ int_0^K t^(-1/2)dt
      +K int_K^infinity t^(-3/2)dt ]`

`=8 sqrt(K)`.                                                       (4.6)

By the Fourier representation (3.3), uniformly in every translate `s`,

`boxed:
 sup_s E|Q-s|^(-1/2)
 <=4 sqrt(2) (M/B_2)^(1/4).}`                                      (4.7)

This is stronger for density transduction than the collision certificate: it is a translation-uniform ONE-COPY half-Riesz potential, obtained without any conditional independence among the coefficient coordinates.

## 5. Two selectors plus one genuine physical square: linear output small-ball

### Corollary 5.1 — `QFORM-2SELECTOR-PLUS-SQUARE-v1`

Let `Q_2` satisfy the `k=2` theorem. Let `Z` be another original cap-one coordinate independent of every variable used by `Q_2`. Let `h` be an arbitrary measurable function of those variables and `d!=0`. Put

`T=d[Z+h]^2+Q_2`.                                                    (5.1)

Conditional on all variables except `Z`, the density of `d[Z+h]^2` is bounded by

`|d|^(-1/2)|u|^(-1/2)`                                              (5.2)

on the appropriate half-line. Therefore, without requiring independence between `h` and `Q_2`,

`p_T(t)
 <=|d|^(-1/2) E|t-Q_2|^(-1/2)`.                                    (5.3)

Insert (4.7):

`boxed:
 ||p_T||_infinity
 <=4 sqrt(2)|d|^(-1/2)(M/B_2)^(1/4).}`                             (5.4)

Hence every interval `I` obeys

`boxed:
 P(T in I)
 <=4 sqrt(2)|d|^(-1/2)(M/B_2)^(1/4)|I|.}`                          (5.5)

This is the requested linear one-copy small-ball scaling recovered from the decoupled integrated estimate.

Continuity is **not** claimed by this square-transducer proof; (5.4) is an essential-supremum conclusion.

Applying the designated partner lemma once more to (5.4), using `||p_T||_2^2<=||p_T||_infinity`, gives the actual partner-consumed collision estimate

`boxed:
 P(|T-T'|<=eps)
 <=8 sqrt(2)|d|^(-1/2)(M/B_2)^(1/4) eps.}`                          (5.6)

## 6. Three selectors: the exact integrability threshold

For general `k>2`, taking square roots in (2.4) gives

`|phi_Q(t)|<=min(1,A_k^(1/2)|t|^(-k/2))`.                           (6.1)

The crossover is `T=A_k^(1/k)`. Direct integration gives

`int_R |phi_Q(t)|dt
 <=2 A_k^(1/k)[1+2/(k-2)]
 =2k/(k-2) A_k^(1/k).`                                              (6.2)

Fourier inversion therefore yields a continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity
 <= [k/(k-2)] (M/B_k)^(1/k).}`                                     (6.3)

At the first admissible integer `k=3`,

`boxed:
 ||p_Q||_infinity
 <=3 [M/(|beta_1 beta_2 beta_3|)]^(1/3).}`                          (6.4)

Thus the selector ladder is exact at the level of this mechanism:

- one selector: fractional independent-copy energy;
- two selectors: `L^2` density, linear collision scaling, and a one-copy half-Riesz potential;
- two selectors plus a genuine square: linear output small-ball;
- three selectors: `L^1` characteristic function and a continuous bounded output density directly.

No law-uniform pointwise decay is required anywhere.

## 7. Concrete target-valid families

### 7.1 Three-selector family

Let `Z` be an arbitrary original-coordinate cap-one product vector and let `V^T V=I_3`. Set

`Y=V^T Z`.

Let `X_1,X_2,X_3` be three further independent original cap-one coordinates, independent of `Z`, and let `C_0` be arbitrary symmetric `3 x 3`. Consider

`Q=2 X^T Y+Y^T C_0 Y`.                                              (7.1)

The product-projection theorem (1.2) gives

`M=||p_Y||_infinity<=e^(3/2)`.                                     (7.2)

Theorem 2.1 with `beta_j=1`, `P_j=0` therefore yields

`boxed:
 ||p_Q||_infinity <=3 sqrt(e)
 =4.946163812100385...}`                                            (7.3)

and the density is continuous `C_0`.

This is genuinely in the target. On the active deterministic subspace `R^3_X direct_sum range(V)`, the matrix is

`[[0,I_3],[I_3,C_0]]`.                                              (7.4)

Diagonalise `C_0` only to compute its deterministic spectrum. Each resulting `2 x 2` block is

`[[0,1],[1,mu]]`,                                                   (7.5)

whose eigenvalues satisfy

`lambda^2-mu lambda-1=0`.                                          (7.6)

Their product is `-1`, so for each of the three blocks at least one eigenvalue has modulus at least one. Thus the full physical matrix has at least three eigenvalues of modulus at least one. This spectral calculation makes no probabilistic independence claim after rotation.

Partner (1.1) applied to (7.3) gives

`P(|Q-Q'|<=eps)<=6 sqrt(e) eps`.                                   (7.7)

### 7.2 Two selectors plus a third large square

Let now `V^T V=I_2`, `Y=V^T Z`, and `X=(X_1,X_2)` be two independent original selector coordinates. Let `Z_0` be one further independent cap-one original coordinate. For arbitrary symmetric `2 x 2 C_0` and `|d|>=1`, put

`T=d Z_0^2+2X^T Y+Y^T C_0Y`.                                      (7.8)

The projection cap is `M<=e`, so (5.4) gives

`boxed:
 ||p_T||_infinity
 <=4 sqrt(2)e^(1/4)|d|^(-1/2)
 <=7.263544634846275... .}`                                        (7.9)

The hyperbolic `4 x 4` block has two eigenvalues of modulus at least one by the same product-of-roots calculation, and the disjoint square contributes the third because `|d|>=1`. Thus (7.9) is another target-valid, nonseparable family with the exact three-large-eigenvalue threshold.

The partner collision lemma yields

`boxed:
 P(|T-T'|<=eps)
 <=8 sqrt(2)e^(1/4)|d|^(-1/2) eps
 <=14.52708926969255... eps.}`                                      (7.10)

## 8. What changed in the full proof map

The result does not close the r32 near-coloop / near-three-coordinate collar automatically, because a general survivor need not expose either:

1. three genuine original-coordinate selector scalars with no cross-quadratic terms among them; or
2. two such selectors plus a third genuine square pivot whose conditional square kernel is retained.

A near-coloop row supplies only one obvious genuine selector. Theorem 2.1 shows exactly what that buys: a finite independent-copy half-Riesz energy (Section 3), not by itself a density bound. The live `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` correction therefore remains fully compatible: a small nonzero residual quadratic coefficient cannot be deleted to manufacture the missing selectors.

Conversely, whenever a structural compiler can expose two genuine scalar arms plus one square, (5.4) closes that packet without needing independence of the two coefficient coordinates. This is a weaker provenance requirement than diagonalising a two-dimensional coefficient projection into independent variables: only its JOINT density cap is needed.

This narrows the next structural implication for B03:

`QFORM-SELECTOR-EXTRACTION-OR-RESIDUAL-CURVATURE-v1`: from the r32 near-coloop/near-three-coordinate determinant collar (after the already-paid exact-coloop and finite-coordinate exits), either expose two genuine original-coordinate selector arms plus a physical square with quantitative coefficients, or prove that the residual same-side curvature itself enters one of the diffuse-volume / ridge / mixed-hub exits. The proof must not perturbatively drop the residual curvature.

## 9. Checks and status

Finite arithmetic and spectral sanity checks are saved in `CHECKS.txt`; they end `QFORM_B03_R33_CHECK_PASS`. They verify the envelope integrals, displayed constants, and random block-matrix spectral counts. The exact proofs are the equations above, not the finite checks.

- unrestricted QFORM bounded-density conjecture: **OPEN**;
- unrestricted continuity: **OPEN**;
- Theorem 2.1 and its one/two/three-selector consequences: **proved here**;
- two-selector-plus-square essential boundedness: **proved here**;
- three-selector branch continuity: **proved here**;
- independent end-to-end review of these new statements: **PENDING**;
- no counterexample to the original conjecture is produced.
