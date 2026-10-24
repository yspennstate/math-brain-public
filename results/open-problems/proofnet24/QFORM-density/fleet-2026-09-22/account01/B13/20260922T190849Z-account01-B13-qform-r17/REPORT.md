SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B13, 2026-09-22T19:08:49Z.
attacking: mixed exact-rank-three one-heavy/two-diffuse geometry via aggregate Pluecker mass before any reciprocal-minor step.

# Mixed rank-three geometry: a forced transverse plane and a paid-pair / two-bank dichotomy

**Run:** `20260922T190849Z-account01-B13-qform-r17`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_REDUCTION / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full QFORM conjecture remains **OPEN / NOT PROVED**. This report attacks the sole exact-rank-three Gram regime left by the designated partner's latest heavy/light trichotomy. It does not use the false arbitrary-joint coarea bound, the false conditional positive-moment gate, pointwise law-uniform quadratic Fourier decay, post-rotation independence, bounded-diameter localization, fixed fragment count, or a single-good-minor hypothesis.

## 1. Exact source dependencies

Fresh owner/control source at the beginning of this run: `yspennstate/math-research-brain@1f5dcf1bc0b184b5d6a18ebcfe88c574328c7127`, OWNER CONTROL revision `2026-09-22.11`.

The designated partner result actually used is account02/B13 run `20260922T182158Z-account02-B13-qform-4ebdd821`, canonical report

`yspennstate/math-open-problems@d511859edaa636cdc00fcd64155ab07506875c3d`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T182158Z-account02-B13-qform-4ebdd821/REPORT.md`.

It proves the following exact-rank-three trichotomy. Write

`A=R Lambda R^T`, `R^T R=I_3`, `min |eig(Lambda)|>=1`,
`c_i=||r_i||^2`, `H={i:c_i>3/10}`, `L=H^c`,
`S=sum_{j in L} r_j r_j^T`, with eigenvalues `s_1>=s_2>=s_3`.

Then `|H|<=9`; the branches `s_3>=3/5` and `s_2<=3/5` are already paid by universal density bounds. The only remaining Gram regime is

`(MIXED)    s_3<3/5<s_2`.

The same partner report proves the compression lemma

`max(|A_ii|,|A_ij|,|A_jj|) >= ||r_i wedge r_j||^2/4`

for every pair in exact rank three, and records the two payment mechanisms used below: the orientation-free physical-pivot theorem

`||p_Q||_infinity <=128 (c_i |A_ii| |det Lambda|)^(-1/4)`

and the support-free near-null pair theorem

`||p_Q||_infinity <=43.323633263897 (|A_ij| |det Lambda| Delta_ij)^(-1/4)`

when `Delta_ij=||r_i wedge r_j||^2>0` and both diagonals have modulus at most `|A_ij|/2`.

I also apply account02/B13's exact bang-bang reduction

`yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T115714Z-account02-B13-qform-480ba28b/REPORT.md`:
for every fixed measurable slab kernel, the supremum over independent densities `0<=f_i<=1`, `int f_i=1`, equals the supremum over product indicators of arbitrary measurable sets `E_i` with `|E_i|=1`, with zero constant loss.

## 2. A forced heavy coordinate with a uniformly nondegenerate transverse light plane

For each heavy index `i`, let

`M_i = sum_{j<k, j,k in L} det(r_i,r_j,r_k)^2`,

and set `M_HLL=sum_{i in H} M_i`.

### Lemma 2.1 — exact mixed Pluecker identity

In the mixed regime,

`M_HLL = tr(adj(S)(I-S))`

and hence, in terms of the eigenvalues of `S`,

`M_HLL=(1-s_1)s_2s_3+(1-s_2)s_1s_3+(1-s_3)s_1s_2`
`      =s_1s_2+s_1s_3+s_2s_3-3s_1s_2s_3`.

Moreover

`boxed(M_HLL >= 9/25)`.

#### Proof

By Cauchy--Binet,

`det(S+t(I-S))`

is the sum of squared `3x3` row determinants, with a factor `t` for every selected heavy row. The coefficient of `t` is therefore exactly the sum over triples containing one heavy and two light rows, namely `M_HLL`. Differentiating the determinant at `t=0` gives `tr(adj(S)(I-S))`.

For the lower bound fix `s_1,s_2`. The displayed expression is affine in `s_3`, with derivative

`d=s_1+s_2-3s_1s_2`.

If `d>=0`, the minimum over `0<=s_3<3/5` is at `s_3=0`, and equals `s_1s_2>=(3/5)^2=9/25`.

If `d<0`, the infimum is attained as `s_3` approaches `3/5`, where the expression becomes

`F=(3/5)(s_1+s_2)-(4/5)s_1s_2`.

On `3/5<=s_2<=s_1<=1`, this bilinear expression is at least `2/5`, hence in particular at least `9/25`. Thus `M_HLL>=9/25`. QED.

Since `|H|<=9`, some heavy coordinate `i` satisfies

`boxed(M_i>=1/25)`.

Fix such an `i`. Put `c=||r_i||^2`, `u=r_i/sqrt(c)`, and let `P=I-u u^T` be orthogonal projection onto `u^perp`. For each light row set `p_j=P r_j`, and define the two-dimensional transverse Gram operator

`G=sum_{j in L} p_j p_j^T` on `u^perp`.

### Lemma 2.2 — quantitative transverse plane

For this heavy `i`,

`boxed(det G >=1/25)`

and in fact

`boxed((1/25) I_{u^perp} <= G <= I_{u^perp}}`.

#### Proof

In an oriented orthonormal basis with first vector `u`,

`det(r_i,r_j,r_k)=sqrt(c) det_2(p_j,p_k)`.

Two-dimensional Cauchy--Binet gives

`M_i=c sum_{j<k} det_2(p_j,p_k)^2=c det G`.

Since `c<=1`, `det G=M_i/c>=M_i>=1/25`.

Also `S<=I_3`, hence for every `v in u^perp`,

`v^T G v=v^T S v<=||v||^2`,

so both eigenvalues of `G` are at most one. Their product is at least `1/25`, therefore both are at least `1/25`. QED.

This is already stronger than the previous qualitative statement “the light set carries two directions”: one *specific heavy original coordinate* has a uniformly elliptic two-dimensional light Gram in its spectral transverse plane.

## 3. High normalized transverse leverage is already paid

Normalize the transverse light frame by

`z_j=G^(-1/2)p_j`, so `sum_{j in L} z_j z_j^T=I_2`.

Let

`ell_j=||z_j||^2`.

### Proposition 3.1 — a `1/32` leverage atom yields a universal density bound

If some light index `j` has `ell_j>=1/32`, then

`boxed(||p_Q||_infinity < 8228)`.

#### Proof

By Lemma 2.2,

`||p_j||^2=z_j^T G z_j >= (1/25) ell_j >=1/800`.

Thus the physical leverage of row `j` obeys `c_j=||r_j||^2>=1/800`. Since `r_i=sqrt(c)u`,

`Delta_ij=||r_i wedge r_j||^2=c ||p_j||^2
          >=(3/10)(1/800)=3/8000`.

Apply the partner compression lemma to the physical pair `(i,j)`. Write

`a=A_ii`, `b=A_ij`, `d=A_jj`, `Delta=Delta_ij`.

If `|a|>=Delta/8`, the physical-pivot theorem at the heavy coordinate gives

`||p_Q||_infinity
 <=128[(3/10)(3/64000)]^(-1/4)
 <2091`.

If `|d|>=Delta/8`, the same theorem at `j`, using `c_j>=1/800`, gives

`||p_Q||_infinity
 <=128[(1/800)(3/64000)]^(-1/4)
 <8228`.

Otherwise both diagonals have modulus below `Delta/8`. The compression lemma then forces `|b|>=Delta/4`, so `|a|,|d|<=|b|/2`. The partner near-null theorem gives

`||p_Q||_infinity
 <=43.323633263897 (Delta^2/4)^(-1/4)
 <=43.323633263897 sqrt(2) sqrt(8000/3)
 <3164`.

Hence all subcases are bounded by `8228`. QED.

By the partner's exact bang-bang theorem, the same statement is an actual geometric inequality: for every interval `J` and every family of arbitrary measure-one sets `E_k`,

`boxed(|{x in prod E_k : x^T A x in J}| <= 8228 |J|)`

throughout this high-normalized-leverage subbranch. No single-interval, finite-diameter, or fixed-fragment assumption is used.

## 4. Otherwise the light transverse plane splits into two independent banks

Assume now

`ell_j<1/32` for every `j in L`.

Apply the two-color Marcus--Spielman--Srivastava paving theorem to the Parseval frame `{z_j}` in dimension two. There is a partition

`L=L_1 disjoint_union L_2`

such that, for `a=1,2`,

`||sum_{j in L_a} z_j z_j^T|| <= (1/sqrt(2)+sqrt(1/32))^2 =25/32`.

Since the two partial sums add to `I_2`, each also has lower spectral bound `7/32`. Conjugating by `G^(1/2)`, define

`G_a=sum_{j in L_a} p_j p_j^T`.

Then

`boxed((7/32)G <= G_a <=(25/32)G)`

and therefore, using Lemma 2.2,

`boxed((7/800)I_{u^perp} <= G_a <=(25/32)I_{u^perp},  a=1,2}`.

In particular both light banks are quantitatively full rank in the same transverse plane, and because `L_1,L_2` are disjoint sets of original coordinates their underlying product sources remain independent. This is a product-preserving statement; no rotation of the independent coordinates has occurred.

Equivalently, after conditioning on the other heavy original coordinates `H\{i}`, every still-unpaid exact-rank-three mixed instance has the canonical structure

- one cap-one original scalar `X_i` with leverage `c_i>3/10`, and
- two independent light coordinate banks whose transverse spectral Grams are each at least `(7/800)I_2`.

This is the new reduction `QFORM-RANK3-MIXED-TRANSVERSE-TWOBANK-v1`.

## 5. What this does and does not prove

Combining the designated partner trichotomy with Propositions 3.1 and the two-bank reduction gives an exhaustive exact-rank-three decision tree:

1. `s_3>=3/5`: already paid by the partner diffuse theorem;
2. `s_2<=3/5`: already paid by the partner heavy-pair theorem;
3. `s_3<3/5<s_2`: choose the heavy coordinate forced by Lemmas 2.1--2.2;
   - if some normalized transverse light leverage is at least `1/32`, the full density is `<8228`;
   - otherwise the light coordinates split into two independent transverse banks, each with Gram at least `7/800 I_2`.

Thus the exact-rank-three obstruction has been reduced further from “one heavy direction / two diffuse directions” to a concrete **one original scalar + two disjoint quantitatively elliptic transverse product banks** geometry.

This does **not** yet give a universal density bound in the final two-bank subbranch. The live correction that a bounded two-dimensional projection density alone does not control an indefinite quadratic pushforward remains decisive. The next theorem must use the *product-linear provenance* of both transverse banks jointly with the heavy scalar, rather than replace either bank by an arbitrary two-dimensional density.

A promising exact endpoint is the near-null heavy pivot. In a spectral basis beginning with `u`, if the normalized heavy Rayleigh coefficient vanishes, the heavy scalar enters linearly through the transverse slope. The two-bank split above supplies two independent product-linear realizations of that transverse slope. The remaining analytic task is to average the rank-two logarithmic ridge over the second bank before taking any reciprocal coefficient. This is precisely the kind of group-before-condition operation demanded by the correction inbox.

Arbitrary additional spectral directions remain a separate full-QFORM bridge after exact rank three. Therefore the full conjecture stays **OPEN**.

## 6. First unpaid implication

`QFORM-RANK3-ONEHEAVY-TWOTRANSVERSE-BANK-CLOSURE-v1`:

> Given an exact-rank-three target in the final branch above, prove a universal density bound using one original cap-one heavy scalar and the two disjoint light product banks satisfying `G_1,G_2 >=7/800 I_2`, while preserving their product-linear provenance. In the near-null pivot regime, aggregate the logarithmic ridge against the second transverse bank before absolute values or reciprocal-minor payment.

This is strictly narrower than the partner's former `QFORM-RANK3-MIXED-ONEHEAVY-TWODIFFUSE-v1` debt, and the high-normalized-leverage portion of that debt is now completely paid.
