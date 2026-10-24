SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-24T10:57:16Z.
attacking: literature-to-proof transfer from sharp projection-density and quadratic-form results into the latest account02/B18 structural survivor.

# account01/B18 r53 — a one-sided overlapping-tail moving-square closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** literature-to-proof transfer  
**Status:** **PROVED SUPPORTING TARGET-LEVEL CHAMBER / LATEST ACCOUNT02-B18 PARTNER APPLIED / FULL QFORM OPEN**  
**Continuity:** not asserted by the new generic theorem; full-target continuity remains open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh boundary and exact gap attacked

Fresh main controls still mark the unrestricted theorem OPEN. The live corrections used here are decisive: no independence is inferred after an orthogonal projection, an unconditional pair-density cap is not replaced by a conditional cap, no small nonzero cross term is discarded, and no arbitrary-joint rank-three coarea theorem is used.

The latest completed designated partner is account02/B18 run `account02-B18-20260924T100529Z-r11`. Its main mathematical conclusion is that a small second cross direction is harmless when its whole random contribution is carried by source coordinates disjoint from a paid rank-one-cross/transverse-curvature core: it is then an exact independent convolution. It leaves the **overlapping-tail** case, where the small cross term shares source variables with the curved core.

This run closes a genuine one-sided-overlap subcase: the second cross term may share the **right** projected source with the curvature and therefore is not an independent additive remainder; its left coefficient is allowed to come from a separate original-coordinate bank. The mechanism is an exact moving-square shear, not a perturbative deletion.

## 2. Primary literature audit at exact hypotheses

### 2.1 Rudelson--Vershynin

Primary source: Mark Rudelson and Roman Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492, Theorem 1.2.

If `X_i` are independent real random variables with one-dimensional densities bounded by `K`, and `sum_i a_i^2=1`, then the density of `sum_i a_i X_i` is bounded by `sqrt(2) K` almost everywhere. The theorem assumes no iid structure, moments, bounded support, centering, symmetry, smoothness or log-concavity. I use it only on a genuine original-coordinate product bank.

### 2.2 Livshyts--Paouris--Pivovarov

Primary source: Galyna Livshyts, Grigoris Paouris and Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1.

For a genuine product probability density `f(x)=prod_i f_i(x_i)` with `||f_i||_infinity<=1`, every `k`-dimensional orthogonal marginal has density cap at most `2^(k/2)`. In particular a two-dimensional orthogonal projection has **joint** density cap at most `2`; its two coordinates are not asserted independent. If the source bank itself has dimension two, the same use is even simpler: an orthogonal change has Jacobian one, so the joint cap is at most one.

### 2.3 Banks--Garza Vargas--Kulkarni--Srivastava

Primary source: Jess Banks, Jorge Garza Vargas, Archit Kulkarni and Nikhil Srivastava, *Overlaps, Eigenvalue Gaps, and Pseudospectrum under real Ginibre and Absolutely Continuous Perturbations*, arXiv:2005.08930, Theorem 2.1 and Corollary 2.4 (`Density of Quadratic Forms`). Their theorem treats the bilinear-affine packet `X^T ZY + X^T U + V^T Y + W` for independent-entry bounded-density banks, and its scalar corollary pays geometric means of singular values. It does not literally state the same-bank moving square `gamma D^2 + 2 h(R,C)D` used below. Thus it supplies relevant prior provenance for the bilinear mechanism but not an exact published solution of the present curved overlapping-tail implication.

A bounded repository search did not locate the exact moving-square statement below. That search miss is not a novelty claim.

## 3. Source-valid analytic theorem

### Theorem `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-MOVING-SQUARE-v1`

Let `S` be a real random variable with density cap

`||p_S||_infinity <= K < infinity`.

Let `(C,D)` be independent of `S`, have a joint probability density `g`, and satisfy

`||g||_infinity <= M < infinity`.

Let `R` be an arbitrary random element independent of the entire triple `(S,C,D)`. No density, moment or regularity assumption is imposed on `R`. Let `beta,gamma` be nonzero real numbers and let `F(r,c), h(r,c)` be arbitrary measurable real functions. Define

`T = 2 beta S C + F(R,C) + 2 h(R,C)D + gamma D^2`.                 (3.1)

Then `T` has an essentially bounded density and

`boxed: ||p_T||_infinity
 <= 3 (2 M K)^(2/3) |beta^2 gamma|^(-1/3).`                         (3.2)

This keeps an arbitrary moving square shift depending jointly on an independent source `R` and on the same projected coordinate `C`; it does not require `C,D` to be independent.

### Proof

Condition first on `R=r`. Because `R` is genuinely independent of `(S,C,D)`, the law of `S` and the joint law of `(C,D)` are unchanged. Make the triangular change

`D' = D + h(r,C)/gamma`.                                            (3.3)

For each fixed `r`, the map `(c,d)->(c,d')` has Jacobian one, so the transformed pair still has a joint density bounded by `M`. Moreover

`gamma D^2 + 2 h(r,C)D
 = gamma D'^2 - h(r,C)^2/gamma`.                                    (3.4)

Thus it suffices to prove (3.2) for

`T_r = 2 beta S C + A_r(C) + gamma D^2`,                             (3.5)

where `A_r` is arbitrary measurable.

Fix an output value `t`. Since `C` has an absolutely continuous marginal, the null set `C=0` may be ignored. Integrating first in the independent scalar `S`, an output-density kernel is

`K_t(c,d)
 = [1/(2|beta c|)]
   p_S( [t-A_r(c)-gamma d^2]/[2 beta c] ).`                          (3.6)

For `z>0`, if `K_t(c,d)>z`, then

`p_S(x_t(c,d)) > 2|beta| z |c|`.                                   (3.7)

Since `p_S<=K`, necessarily

`|c| < K/(2|beta|z).`                                               (3.8)

For a fixed nonzero `c`, put `m=2|beta|z|c|` and

`E_m={x:p_S(x)>m}`.

Probability normalization gives `|E_m|<=1/m`. The map

`d -> x_t(c,d)
 = [t-A_r(c)-gamma d^2]/[2 beta c]`                                 (3.9)

is a quadratic whose leading coefficient has magnitude

`|gamma|/(2|beta c|)`.

For every quadratic `A(d-d0)^2+v` and every measurable set `E` of length `L`, the two inverse branches give

`|{d:A(d-d0)^2+v in E}| <= 2 sqrt(L/|A|).`                          (3.10)

Applying (3.10) with `L<=1/m` yields, for each allowed `c`,

`|{d:K_t(c,d)>z}| <= 2/(sqrt(|gamma|) sqrt(z)).`                    (3.11)

The `c`-interval in (3.8) has total length `K/(|beta|z)`, hence

`|{(c,d):K_t(c,d)>z}|
 <= [2K/(|beta|sqrt(|gamma|))] z^(-3/2).`                            (3.12)

The transformed pair density has cap `M` and total mass one. Therefore

`int_{K_t>z} g_r'(c,d) dc dd
 <= min{1, A z^(-3/2)},
 A = 2 M K/(|beta|sqrt(|gamma|)).`                                  (3.13)

Layer cake now gives uniformly in `t,r`

`p_{T_r}(t)
 <= int_0^infinity min{1,A z^(-3/2)} dz
 = 3 A^(2/3)
 = 3(2MK)^(2/3)|beta^2 gamma|^(-1/3).`                              (3.14)

Averaging over `R` gives the same bound for `T`. QED.

### Correction discipline

The proof conditions on a genuinely independent original-source object `R`. The nonlinear shear (3.3) is performed only inside the already-joint `(C,D)` pair and is used through its Jacobian-one density cap; it does **not** assert independence of `C,D`. The nonzero term `h(R,C)D` is retained exactly. This is therefore distinct from the refuted conditional-cap-as-independence interface.

## 4. Product-law corollary: one-sided overlapping cross tails

Take three pairwise-disjoint ORIGINAL-coordinate banks `I0, I1, J`. Let

`S=u^T X_I0`,  `R=r^T X_I1`,
`C=v^T X_J`,   `D=w^T X_J`,                                        (4.1)

where `u,r` are unit vectors and `v,w` are orthonormal. Then `S`, `R`, and the pair `(C,D)` have the genuine source separation needed in Theorem 3, while `C,D` may be dependent.

Rudelson--Vershynin gives

`K<=sqrt(2)`,                                                       (4.2)

and Livshyts--Paouris--Pivovarov gives

`M<=2`.                                                             (4.3)

Hence for arbitrary real `c,delta`, `d1!=0`, `gamma!=0`, and arbitrary `d2`,

`Q = 2 d1 S C + 2 d2 R D
    + c C^2 + 2 delta C D + gamma D^2`                              (4.4)

has

`boxed: ||p_Q||_infinity
 <= 3*2^(5/3) |d1^2 gamma|^(-1/3)
 = 9.524406311809198... |d1^2 gamma|^(-1/3).`                       (4.5)

Indeed (4.4) is (3.1) with

`beta=d1`, `F(R,C)=cC^2`, `h(R,C)=d2 R+delta C`.

The crucial point is that (4.5) is **independent of `d2`**. The tail `2d2RD` may be arbitrarily small or large; it shares the right variable `D` with `gamma D^2`, so it is not an independent additive remainder, but the moving square absorbs it exactly.

If `S` is one literal original coordinate, `K<=1` and (4.5) improves to

`3*4^(2/3)|d1^2 gamma|^(-1/3)
 =7.559526299369239... |d1^2 gamma|^(-1/3).`                        (4.6)

## 5. Direct application to the designated partner's collar

Use the preceding completed account02/B18 structural funnel. In the SVD-aligned two-right-direction chamber, the active matrix in the orthonormal deterministic frame `(u,r,v,w)` is

`H = [[0,0,d1,0],
      [0,0,0,d2],
      [d1,0,c,delta],
      [0,d2,delta,gamma]],`                                         (5.1)

with `d1>=d2>=0`, and put `s=s3(H)>0`.

The account02/B18 funnel `s<=d2+||P_v C P_v||` specializes here to the actual scalar inequality

`boxed: |gamma| >= (s-d2)_+.`                                      (5.2)

Also, because the right curvature block has rank at most two, subtracting it from `H` and using the rank-two approximation characterization of `s3` yields

`s <= || [[0,D],[D^T,0]] ||_op = d1`,                              (5.3)

so `d1>=s`.

For `0<=d2<s`, write `eta=d2/s`. The new moving-square theorem gives

`||p_Q||_infinity
 <= [3*2^(5/3)]/[s(1-eta)^(1/3)].`                                 (5.4)

The completed rank-two cross theorem used throughout the partner chain gives, when `d2>0`,

`||p_Q||_infinity <= 2sqrt(pi)/sqrt(d1 d2)
                  <= 2sqrt(pi)/(s sqrt(eta)).`                       (5.5)

For `eta>=1`, (5.5) is at most `2sqrt(pi)/s`. On `(0,1)`, the first right side in (5.5) decreases and the right side of (5.4) increases. Their crossing is

`eta_* = 0.12657584480912131...`,                                  (5.6)

and the common value is

`9.963903543676045.../s`.                                          (5.7)

Therefore the whole chamber (5.1), under the stated source-separated left-bank provenance, obeys

`boxed: ||p_Q||_infinity < 9.964/s3(H).`                            (5.8)

This is an equation-level application of the completed partner funnel. It extends the earlier literal-two-hub planar result to two arbitrary projected left aggregates, provided their original source supports are disjoint.

## 6. Exact target-valid overlapping-tail family

For every `0<eps<1`, take the same source structure and set

`Q_eps = 2 S C + 2 eps R D + D^2.`                                 (6.1)

In the frame `(S,R,C,D)` the physical active matrix is

`H_eps=[[0,0,1,0],
        [0,0,0,eps],
        [1,0,0,0],
        [0,eps,0,1]].`                                              (6.2)

It decomposes into the blocks `[[0,1],[1,0]]` and `[[0,eps],[eps,1]]`, so its eigenvalues are

`-1, 1, (1+sqrt(1+4eps^2))/2, (1-sqrt(1+4eps^2))/2.`                (6.3)

For `0<eps<1` it therefore has **exactly three** eigenvalues of modulus at least one, and

`s3(H_eps)=1.`                                                      (6.4)

The term `2eps R D` shares the right source `D` with the square `D^2`; it is not the source-separated independent remainder covered by the latest account02/B18 run. Nevertheless (4.5) gives, for all admissible rough product laws,

`boxed: ||p_{Q_eps}||_infinity <= 3*2^(5/3)
       =9.524406311809198... ,  0<eps<1.`                           (6.5)

No limit or perturbation in `eps` is taken.

## 7. Literal use of the latest account02/B18 r11 remainder theorem

Let `Z` be **any** real random variable generated by a fourth original-coordinate bank disjoint from all sources in (4.1), independent of the displayed core. It may itself be an arbitrary quadratic form and need not have a density or moments. The latest account02/B18 result `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-PLUS-INDEPENDENT-REMAINDER-v1` applies to the already-paid core by exact convolution, giving

`boxed: ||p_{Q_eps+Z}||_infinity <= 9.524406311809198...}`           (7.1)

for the target-valid family (6.1), with the arbitrary source-separated remainder retained exactly. Thus the partner's completed result is applied to an actual inequality here, rather than only cited.

## 8. What is newly paid and what remains

This run pays one genuine part of the partner's overlapping-tail debt:

- the second cross direction may overlap the curved core on the **right** source bank;
- its coefficient may depend on an arbitrary separate left source `R`;
- the pair `(C,D)` can be dependent projected coordinates;
- all of the tail is retained exactly by a moving-square shear;
- arbitrary further source-separated remainder is then free by the latest account02/B18 convolution result.

The still-unpaid overlapping geometry is when the nominal rank-one cross carrier and the small second direction share source coordinates on **both** sides, so there is no independent `S` versus `(R,C,D)` split to condition on. Likewise the bare global hypothesis `s3(A)>=1` still does not force a zero-self original-coordinate packet or the two-right-direction chamber (5.1). Those are structural compiler gaps, so the unrestricted QFORM theorem remains OPEN.

Continuity is kept separate. The layer-cake proof establishes absolute continuity and an essential `L^infinity` bound. I do not assert a generic `C_0` representative for Theorem 3 or (5.8).

## 9. Finite checks

The constant optimization and exact spectra were independently checked numerically only as algebra audits:

- `3*2^(5/3)=9.524406311809198...`;
- the crossing of `2sqrt(pi)/sqrt(eta)` and `3*2^(5/3)/(1-eta)^(1/3)` is `eta_*=0.12657584480912131...` with value `9.963903543676045...`;
- for `eps=10^-6,0.1,0.5,0.999`, direct diagonalization of (6.2) agrees with (6.3) and gives exactly three absolute eigenvalues at least one.

The proof itself is analytic; these finite checks are not evidence for the full conjecture.
