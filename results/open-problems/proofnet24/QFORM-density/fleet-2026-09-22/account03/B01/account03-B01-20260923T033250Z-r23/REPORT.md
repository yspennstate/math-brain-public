SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-23T03:32:50Z.
attacking: the concentrated-volume two-sided-core receiver — aggregate a full two-dimensional original-coordinate cross bank before paying the bilinear singularity, then pass the result through signed Fejer.

# account03/B01 r23 — two-dimensional grouped bilinear receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Oscillatory replacement  
**Classification:** `SUPPORTING TARGET-LEVEL ANALYTIC THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not proved by the new general branch; tracked separately.

## 1. Source boundary and first missing implication


This run starts from the newest physical-core reductions rather than another scalar pivot split. In particular:

* account03/B16 r23, `yspennstate/math-open-problems@bbb01a983ce6478003ccf8422198c87f44f52cea`, proves a dominant mixed-Pluecker star and reduces one surviving exact-rank-three branch to a near-null heavy star with transverse leverage at most `1/2`;
* account03/B07 r22, `yspennstate/math-open-problems@ac54330d3df42a48098ef7c704ac268382accd7c`, proves the four-bank low-tail / paid / two-sided-core alternative and explicitly leaves a product-provenance receiver for the concentrated two-sided core;
* account04/B01, `yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`, proves the exact signed-Fejer equivalence used in Section 6 below.

The analytic obstruction is that a scalar bilinear product has a logarithmic singularity. The replacement proved here is to aggregate TWO physical directions on one side before inversion. The resulting inverse-radius singularity is integrable against a bounded planar product projection. This is an averaged/product-geometry mechanism; no pointwise scalar Fresnel estimate is used.

The following live corrections are retained: bounded one-dimensional density does not imply law-uniform pointwise quadratic-phase decay; spectral rotation does not preserve independence; a bounded projection density alone does not control an arbitrary indefinite quadratic pushforward; arbitrary joint coarea and worst conditional-height substitutes remain forbidden; and no local minor is selected before the relevant grouped mass is formed.

## 2. Two source-valid product-projection inputs

The current QFORM fleet has source-validated the following two consequences of bounded product marginals.

1. If `X=(X_j)` has independent coordinate densities bounded by one and `v` is a deterministic coefficient vector, then

   `||p_(v^T X)||_infinity <= sqrt(2)/||v||_2`.                 (2.1)

2. If `M` is a real `2 x m` rank-two matrix and `U=M X`, then

   `||p_U||_infinity <= 2/sqrt(det(M M^T))`.                    (2.2)

Translations do not change either cap. Equation (2.1) is used by the completed account04/B01 grouped-square handoff; (2.2) is the two-dimensional product-marginal input already used in account03/B01 r22.

Write

`Delta_M := det(MM^T)>0`,
`Delta_N := det(NN^T)>0`,
`s_M := sigma_min(M)>0`,
`s_N := sigma_min(N)>0`.                                       (2.3)

## 3. Exact inverse-radius lemma

### Lemma 3.1 — planar cap implies an inverse-radius moment

Let `U` be any random vector in `R^2` with probability density `g` satisfying `0<=g<=K`. Then, for every deterministic translation `a in R^2`,

`boxed: E |U-a|^(-1) <= 2 sqrt(pi K).`                          (3.1)

#### Proof

Translation lets us take `a=0`. By layer cake,

`E |U|^(-1)
 = int_0^infinity P(|U|^(-1)>s) ds
 = int_0^infinity P(|U|<1/s) ds.`                              (3.2)

The probability inside a radius `1/s` is bounded both by one and by density cap times area:

`P(|U|<1/s) <= min(1, K pi s^(-2)).`                            (3.3)

Put `s_0=sqrt(pi K)`. Then

`int_0^s0 1 ds + int_s0^infinity K pi s^(-2) ds
 =s_0 + K pi/s_0
 =2 sqrt(pi K).`                                                (3.4)

This proves (3.1). The constant is the bathtub value corresponding to filling a disk at density `K`. QED.

The point is dimensional: in one dimension the analogous `E|L|^(-1)` can diverge logarithmically. In two dimensions the `1/r` singularity is integrable. This is the exact mechanism exploited below.

## 4. Main theorem: grouped two-dimensional bilinear receiver

Partition the ORIGINAL independent coordinates into mutually disjoint banks

`I, J, D, W`.                                                   (4.1)

Let `M` be `2 x |I|` of rank two and `N` be `2 x |J|` of rank two. Allow arbitrary measurable translations `a(X_W), b(X_W) in R^2`, and define

`U = M X_I + a(X_W)`,
`V = N X_J + b(X_W)`.                                          (4.2)

Let `H=H(X_I,X_D,X_W)` be an arbitrary measurable real random variable, finite almost surely. Thus ALL curvature and nonlinear dependence on the `I,D,W` banks may be retained; the only structural requirement is that the `J` bank enters the displayed active part linearly through the two-dimensional grouped variable `V`.

Set

`Q = 2 U^T V + H.`                                              (4.3)

### Theorem 4.1 — `QFORM-GROUPED-BILINEAR-2D-RECEIVER-v1`

Under (4.1)-(4.3), `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(pi) Delta_M^(-1/4) s_N^(-1).`                       (4.4)

No moment, support, connectedness, log-concavity, Gaussianity, or independence after rotation is used. The term `H` may contain arbitrary same-side quadratic curvature in the entire `I` bank and arbitrary quadratic/remainder terms in the disjoint `D,W` banks.

If instead the arbitrary nonlinear remainder depends on `J,D,W` but not on `I`, the symmetric estimate holds:

`||p_Q||_infinity
 <= 2 sqrt(pi) Delta_N^(-1/4) s_M^(-1).`                       (4.5)

If the additive remainder is independent of both active banks (or otherwise both conditioning orientations are source-valid), then

`boxed:
 ||p_Q||_infinity
 <=2sqrt(pi) min{
   Delta_M^(-1/4) s_N^(-1),
   Delta_N^(-1/4) s_M^(-1)
 }.`                                                            (4.6)

#### Proof

Condition on `(X_I,X_D,X_W)`. Then `U=u` and `H=h` are deterministic, while the untouched `X_J` coordinates remain independent with their original cap-one densities. For `u!=0`,

`2 u^T V + h
 =2 (N^T u)^T X_J + constant.`                                 (4.7)

By (2.1), its conditional density is bounded by

`sqrt(2)/||2N^T u||_2
 =1/(sqrt(2)||N^T u||_2)
 <=1/(sqrt(2) s_N |u|).`                                       (4.8)

The event `u=0` has probability zero because, conditional on `X_W`, the planar law of `U` is absolutely continuous. Averaging (4.8) over the conditioned variables gives

`||p_Q||_infinity
 <=(1/(sqrt(2)s_N)) E |U|^(-1).`                               (4.9)

Conditional on `X_W=w`, (2.2) gives

`||p_(U|X_W=w)||_infinity <= K_M:=2/sqrt(Delta_M),`             (4.10)

uniformly in the translation `a(w)`. Lemma 3.1 therefore yields

`E(|U|^(-1)|X_W=w)
 <=2sqrt(pi K_M)
 =2sqrt(2pi) Delta_M^(-1/4).`                                  (4.11)

Insert (4.11) into (4.9):

`||p_Q||_infinity
 <=[2sqrt(2pi)/(sqrt(2))]
   Delta_M^(-1/4)s_N^(-1)
 =2sqrt(pi)Delta_M^(-1/4)s_N^(-1).`                            (4.12)

This proves (4.4). Swapping the two active banks proves (4.5); when both orientations are valid, take the minimum. QED.

### Why arbitrary same-side curvature is genuinely retained

The proof conditions on the whole `I` bank, not merely on `U`. Therefore `H` may be `X_I^T C X_I`, a fragmented-support-dependent measurable term, an affine term generated by outside conditioning, or any combination with the `D,W` variables. It is just a translation in (4.7). What remains unpaid is nonlinear curvature involving the still-random `J` bank itself. That is the exact boundary of this theorem and should not be silently crossed.

## 5. Aggregate-before-inversion form and a target-valid control family

Since the singular values of `M` are `m_1>=m_2>0`,

`Delta_M^(1/4)=sqrt(m_1 m_2).`                                 (5.1)

Thus (4.4) spends the full two-dimensional grouped area before inversion:

`||p_Q||_infinity
 <=2sqrt(pi)/[sqrt(m_1m_2) s_N].`                              (5.2)

No single physical entry or `2x2` physical minor is selected.

In particular, if

`MM^T=NN^T=I_2`,                                                (5.3)

then

`boxed: ||p_Q||_infinity <=2sqrt(pi)=3.5449077018... .`         (5.4)

For the pure grouped cross form `Q=2(MX_I)^T(NX_J)`, the active symmetric matrix on `I union J` is

`A_cross=[[0,M^TN],[N^TM,0]]`.                                 (5.5)

Under (5.3) its nonzero eigenvalues are exactly `+1,+1,-1,-1`; hence this is an actual target-valid family with at least three eigenvalues of modulus one. The theorem controls every cap-one product input law uniformly in the bank dimensions. An arbitrary INDEPENDENT additive quadratic form on a disjoint bank may be convolved afterward without increasing the bound.

This family is a control/application, not a claim that the bare three-eigenvalue hypothesis always forces (4.3).

## 6. Designated account04/B01 result applied to the new inequality

Account04/B01 proves the exact signed-Fejer equivalence. For a law `mu` with characteristic function `muhat`, define

`D_T mu(y)
 =(1/(2pi)) int_{-T}^T (1-|t|/T)
   Re(e^(-ity) muhat(t)) dt.`                                  (6.1)

Its theorem gives

`||p_mu||_infinity = sup_(T>0,y in R) D_T mu(y)`                (6.2)

whenever the bounded density exists, with the converse implication as well.

Applying (6.2) to Theorem 4.1 gives the ACTUAL averaged-frequency inequality

`boxed:
 sup_(T>0,y) D_T law(Q)(y)
 <=2sqrt(pi) Delta_M^(-1/4)s_N^(-1).`                          (6.3)

If both conditioning orientations are valid, replace the right side by the minimum in (4.6). This is exactly the requested oscillatory replacement: it is a signed Fejer bound obtained from grouped original-coordinate product geometry, not from a false law-uniform pointwise Fresnel estimate or from absolute Fourier `L^1` integrability.

## 7. Phase-aligned counterexample remains preserved

For every prescribed nonzero frequency `s` and every small `delta>0`, the set

`E_s(delta)={x: dist(sx^2,2pi Z)<=delta}`                       (7.1)

has infinite Lebesgue measure. Choose a measurable finite union of pieces inside it of total measure one and set `f=1_E`. Then `0<=f<=1`, `int f=1`, and

`Re int e^(isx^2)f(x)dx >=cos(delta).`                         (7.2)

Hence no positive law-uniform pointwise power decay in `|s|` can hold for scalar quadratic phases. Theorem 4.1 never invokes such a statement. It instead turns a two-dimensional grouped linear projection into the integrable inverse-radius factor (3.1).

## 8. Relation to the current concentrated-volume debt

The newest B07 reduction shows that failure of its paid diffuse-tail branch can force a two-sided bounded-rank physical core with heavy ORIGINAL row and column coordinates. The present theorem supplies a clean analytic endpoint whenever that core can be product-preservingly arranged so that one two-dimensional grouped bank enters linearly across the cross interaction, while all same-side curvature is placed on the conditioned bank. It therefore removes the reciprocal-single-entry obstruction in that subcase.

What it does NOT yet prove is the structural/analytic splice needed when BOTH grouped banks retain arbitrary self-curvature. Nor does it show that every strict-N3 concentrated-volume state contains a source-disjoint rank-two grouped receiver with `Delta_M` and `s_N` bounded below. Those are the first unpaid implications.

A concrete successor is:

`QFORM-TWO-SIDED-CURVED-BICORE-RECEIVER-v1` — starting from the B07 two-sided bounded-rank physical core, either orient the core so that one side is linear and apply (4.4), route to an already-paid grouped-square/pair-log/hub endpoint, or prove an extension of (4.4) that tolerates self-curvature on BOTH active grouped banks without replacing product provenance by a generic bounded joint density.

Arbitrary additional spectrum remains a separate global splice debt. Full continuity remains open.

## 9. Status

`QFORM-GROUPED-BILINEAR-2D-RECEIVER-v1`: PROVED as a supporting target-level analytic theorem.

Full QFORM: OPEN / NOT PROVED / NOT DISPROVED.

Continuous density in the full target: OPEN. The new theorem establishes absolute continuity and essential boundedness in its stated scope; it does not assert a continuous representative.
