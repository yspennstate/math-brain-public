SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B13, 2026-09-22T22:26:22Z.
attacking: QFORM-SAME-EXTREME-DECONVOLUTION-v1 by testing whether same-product-set copy geometry can be pulled back uniformly, then switching to a one-copy derivative/slope-offset incidence mechanism.

# account02/B13 — no uniform same-set deconvolution and a support-free slope-offset density gate

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** `Extremal product laws`  
**Run:** `20260922T222622Z-account02-B13-extremal-741150`  
**Classification:** `MECHANISM_FALSIFIER / NEW SUPPORT-FREE DENSITY GATE / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Control/source boundary and first unpaid implication

Fresh owner control is revision `2026-09-22.15`; QFORM remains the sole active programme and account02/B13 is not paused. The prepublication brain head used below is `c8b35b4b6228731f833e2eaa0d8872e32c99cb32`. The protected controls were read from the fresh main lineage and a compare to the prepublication head showed only worker artifacts after that control read, not a protected-control change.

The full target remains OPEN: for arbitrary finite dimension, independent real original-coordinate variables with probability densities at most one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite bound for the density of `Q=X^TAX`, or produce a target-valid counterexample.

This slot's completed zero-loss extremal-product front end remains in force: every fixed quadratic slab has the same supremum over arbitrary cap-one product densities as over arbitrary unit-measure product indicator sets. No interval, centered-uniform, bounded-diameter, or bounded-fragment extremality is assumed.

The immediately preceding B13 run, canonical `yspennstate/math-open-problems@5d5c3da2cf6c16154b7272ae31b960dd0a7b1fa5`, proved a same-extreme Fourier-power reduction and converted the designated partner's endpoint `|phi_Q(t)|=O(|t|^{-1/2})` into a linear four-copy alternating-sum bound. Its first unpaid implication was

`QFORM-SAME-EXTREME-DECONVOLUTION-v1`:

use the fact that all copies may be chosen from the **same** product indicator geometry to pull a linear four-copy collision estimate back to a one-copy linear slab estimate.

This run tests that mechanism first. The answer is negative for any pullback that relies only on same-set additive/parallelogram abundance. A phase-specific one-copy replacement is then proved.

## 2. Named designated-partner input actually used

The designated completed partner is account03/B13 r17,

`yspennstate/math-open-problems@eac866b378f5c54411a55f7eb49f89336a4701ae`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260922T213118Z-account03-B13-qform-r17/REPORT.md`.

In the exact-rank-three hard residual it has one heavy original coordinate `i`, row `r_i=sqrt(c)u`, `c>3/10`, and two disjoint light banks `L_1,L_2`. Writing the physical cross-row coefficients from `i` into bank `L_a` as `(A_ij)_(j in L_a)`, the partner proves the uniform bankwise energy floor

`||(A_ij)_(j in L_a)||_2 >= r_*`,

where

`r_* = sqrt(3/10)[sqrt(7/800)sqrt(1-10^(-4))-10^(-2)]`
`    = 0.0457549664530082... .`                                (2.1)

Its proof preserves the original independent coordinates and does not divide by a single diffuse coefficient. It also gives the one-copy `O(|I|^(1/2))` endpoint. The new one-copy gate in Section 4 below applies (2.1) directly.

A fresh compatible result also consumed for mechanism discipline is account02/B01 r29, canonical math commit `c396b6e553f98ca1cd735ae10eb0e6ec24a96cc4`. It proves a two-zero-row/two-slope density theorem, but also gives an exact rank-two falsifier showing that an arbitrarily small nonzero mutual edge can resurrect a product singularity while the two outside slope currencies remain fixed. Its repaired target-valid family becomes bounded only after a genuinely independent third large square is spent. Thus row-energy alone is not a license to perturb a zero-edge theorem.

The fresh correction `QFORM-HYPERBOLIC-TWOSIDED-HALFRIESZ-UNIFORM-FALSE-v1` is also honored: arbitrary two-sided contamination can turn a hyperbolic term into `(U+V)^2`, so no standalone universal half-Riesz bound is used below.

## 3. Exact falsifier for support-only same-extreme deconvolution

### Theorem 3.1 — `QFORM-SAME-SET-ADDITIVE-ENERGY-NOUNIFORM-v1`

For every integer `N>=2` there is a compact finite union `E_N subset R` of exactly `N` intervals, total measure one, whose additive self-overlap energy

`A(E):= integral_R |E intersect (E+h)|^2 dh`                  (3.1)

is exactly

`boxed: A(E_N)=(4N-2)/(3N^2) -> 0.`                           (3.2)

Consequently there is no positive support-free lower bound on same-set parallelogram/collision multiplicity even inside the finite-fragment extreme-product class. For the product set `E_N^d`, the corresponding coordinatewise energy is

`A(E_N^d)=A(E_N)^d`.                                          (3.3)

#### Proof

Put `ell=1/N` and choose the Sidon-separated centers

`c_k=4*2^k`, `1<=k<=N`,

and

`E_N= union_(k=1)^N [c_k,c_k+ell]`.                           (3.4)

Every nonzero ordered difference `c_l-c_k` is distinct. Indeed, for a positive equality

`2^l-2^k=2^(l')-2^(k')`,

the 2-adic valuation gives `k=k'`, then the odd factors give `l=l'`; negative differences are analogous. Distinct nonzero difference centers are separated by at least four, whereas every correlation bump below has radius `ell<=1/2`, so all nonzero bumps are disjoint from each other and from the central bump.

Let

`g_N(h)=|E_N intersect (E_N+h)|`.

For one ordered pair of distinct component intervals the contribution is the triangle

`(ell-|h-h_0|)_+`.

At `h_0=0`, the `N` diagonal ordered pairs coincide, giving the single central triangle

`N(ell-|h|)_+`.

Since

`integral_(-ell)^ell (ell-|s|)^2 ds = 2 ell^3/3`,              (3.5)

the central contribution to `||g_N||_2^2` is

`N^2 * 2ell^3/3 = 2/(3N)`,                                    (3.6)

while the `N(N-1)` disjoint nonzero ordered differences contribute

`N(N-1)*2ell^3/3 = 2(N-1)/(3N^2)`.                            (3.7)

Adding gives (3.2). Tensor factorization of correlations gives (3.3). QED.

### Consequence for the preceding copy mechanism

If a one-copy slab set `A subset E` has measure `alpha`, then merely putting all four copies in `A` gives

`alpha^4 <= P(Q_1-Q_2+Q_3-Q_4 in [-2ell,2ell])`.               (3.8)

A four-copy linear bound therefore yields only the generic `alpha=O(ell^(1/4))` without extra geometry. The natural attempt to improve (3.8) by thickening the quadratic parallelogram identity requires a positive supply of same-set shifts, measured by quantities of the form (3.1). The sets (3.4) make that supply arbitrarily small while remaining legal finite-fragment extremizers. Hence **same-product support by itself cannot be the missing deconvolution resource**.

This is a mechanism counterexample, not a QFORM counterexample. It does not say that the four-copy theorem is useless; it says any successful pullback must spend phase-specific quadratic/product information rather than a support-only additive-energy lower bound.

## 4. New one-copy replacement: a slope-offset rectangle density theorem

The preceding falsifier motivates staying in one physical copy and using the actual derivative of the quadratic phase.

### Theorem 4.1 — `QFORM-SLOPE-OFFSET-LINF-v1`

Let `X` be independent of a real random pair `(S,C)`. Assume

`||p_X||_infinity <= L`,
`||p_(S,C)||_infinity <= M`,                                  (4.1)

with `L,M<infinity`. Let `a,b` be arbitrary real numbers and let `lambda != 0`. Define

`T = a X^2 + b X + lambda S X + C`.                            (4.2)

Then `T` has a density and

`boxed: ||p_T||_infinity <= 4 sqrt(L M/|lambda|).`              (4.3)

The constant is uniform in the quadratic coefficient `a`, the affine coefficient `b`, all support locations, and all moments. No independence between `S` and `C` is assumed.

#### Proof

Let `I` be an interval of length `ell`. For a parameter `R>0`, split the joint integration according to the physical derivative

`D(x,s)=2ax+b+lambda s`.                                       (4.4)

**Small-derivative region.** For fixed `x`, the condition `|D(x,s)|<=R` restricts `s` to an interval of length exactly `2R/|lambda|`. For fixed `x,s`, the slab condition `T in I` restricts `c` to an interval of length `ell`. Hence, using the pair-density cap and then `integral p_X=1`,

`P(T in I, |D|<=R) <= 2 M R ell/|lambda|`.                     (4.5)

**Large-derivative region.** Fix `(s,c)`. The function

`q_(s,c)(x)=a x^2+(b+lambda s)x+c`

has at most two monotonic branches. On the part of either branch where `|q'|>R`, the preimage of an interval of length `ell` has Lebesgue length at most `ell/R`. Therefore the entire large-derivative preimage has length at most `2ell/R`. Since `p_X<=L`,

`P(T in I, |D|>R | S=s,C=c) <= 2L ell/R`.                      (4.6)

Average (4.6) over `(S,C)` and combine with (4.5):

`P(T in I) <= ell [ 2MR/|lambda| + 2L/R ].`                    (4.7)

Choose

`R=sqrt(L|lambda|/M)`

(with the zero/trivial cases interpreted by approximation). Both terms in (4.7) then equal `2 sqrt(LM/|lambda|)`, proving

`P(T in I) <= 4 sqrt(LM/|lambda|) ell`.                        (4.8)

Interval domination implies absolute continuity and (4.3). QED.

### Why this gate is source-safe

The proof never conditions on `S` and then normalizes a possibly singular conditional law. It never rotates original independent coordinates. It never requires moments or a bounded support diameter. A remote support changes neither (4.5) nor (4.6). The small-derivative region is paid in the **two-dimensional slope-offset plane before reciprocal derivative payment**, while the large-derivative region is paid by direct monotonicity in the untouched original coordinate `X`.

This is exactly the kind of joint product-space payment demanded by the newest corrections; it is also immune to the nonzero coefficient `a`, so it avoids an operator-norm perturbation around a null pivot.

## 5. Direct application of the designated partner's cross-row floor

Return to the account03/B13 r17 hard residual. Condition only on original coordinates outside the heavy coordinate `i` and the two disjoint banks `L_1 union L_2`. The remaining quadratic has the exact form

`Q = A_ii X_i^2 + b_0 X_i + 2 X_i U + C`,                    (5.1)

where `C` depends only on the two banks and `U` is the full variable heavy-to-bank slope. Let

`r_a=||(A_ij)_(j in L_a)||_2`,
`r=(r_1^2+r_2^2)^(1/2)`,
`S=U/r`.                                                       (5.2)

The banks are disjoint, so the coefficient norm adds in squares. By the designated partner (2.1),

`r >= sqrt(2) r_*`.                                            (5.3)

Thus (5.1) is (4.2) with `X=X_i`, `L=1`, and

`lambda=2r >= 2sqrt(2) r_*`.                                  (5.4)

Therefore **if** the normalized slope-offset pair `(S,C)` in this residual admits a dimension-free joint density cap `M`, Theorem 4.1 immediately yields

`boxed: ||p_Q||_infinity`
` <= 4 sqrt(M/(2r))`
` <= 4/sqrt(2sqrt(2)r_*) * sqrt(M)`
` = 11.1190676858... * sqrt(M).`                               (5.5)

This is a genuine use of the partner result: its aggregate row-energy floor supplies the denominator in a one-copy density theorem, with no selection of a single diffuse coefficient.

The statement (5.5) is **conditional**, not a claim that such an `M` has already been proved. Indeed a generic slope marginal cap is insufficient, and even a generic slope-offset joint cap is too strong to posit without proof: for independent cap-one `Y,Z`, the pair

`S=Y`, `C=Y^2+delta Z^2`

has a square-root singular joint density along `c=s^2` for every `delta>0`. The remaining argument must use the specific two-bank rank-three provenance, not only low-dimensional density caps.

## 6. What changed and the new first unpaid implication

### Target-level movement

Full exact-rank-three QFORM and full QFORM remain OPEN. No universal constant is claimed here.

The run nevertheless removes a false bridge and replaces it by a precise support-free one-copy gate:

1. finite-fragment extreme product sets can have arbitrarily small additive self-overlap energy, so a support-only same-set parallelogram pullback of the four-copy theorem has no dimension-free constant;
2. a genuine two-dimensional slope-offset payment gives a linear one-copy bound uniformly through a nonzero quadratic pivot;
3. the designated partner already supplies the required heavy-slope scale `r>=sqrt(2)r_*`.

### Mechanism-level movement

The mechanism has changed from copy deconvolution to derivative/slope-offset incidence on the **same physical copy**. This is materially different: it partitions by the actual derivative, pays the small-derivative region jointly in `(S,C)`, and pays the complement by monotonicity. It does not use additive energy, Fourier-power deconvolution, a fixed-depth KL argument, or coefficient continuity on remote supports.

### New first unpaid implication

`QFORM-NEARNULL-TWOBANK-SLOPE-OFFSET-PAYMENT-v1`:

> In the account03/B13 near-null one-heavy/two-transverse-bank residual, prove a dimension-free phase-adapted two-dimensional concentration estimate strong enough to substitute for the `M` in (4.5) for the actual pair `(S,C)` in (5.1), using the two banks' transverse curvature/residual leakage **before** any conditional normalization; or produce a genuine target-compatible falsifier showing that this slope-offset incidence route is insufficient.

A literal global `L^infinity` density bound for `(S,C)` is only a sufficient condition and is not asserted to be the right final formulation. The estimate actually needed by the proof is the rectangle/slanted-strip bound used in (4.5), uniformly over the derivative band. That weaker phase-adapted object is the recommended next target.

Fresh account02/B01 r29 clarifies why the third-direction input must appear here: two slope currencies alone survive an arbitrarily small nonzero-edge falsifier in rank two, while adding a genuine third large square restores a uniform target-valid bound. The B13 two-bank transverse curvature is the available third-direction resource and must be spent in the slope-offset payment, not discarded before reciprocal integration.

## 7. Correction discipline

This report does not use or revive:

- the false arbitrary-joint rank-three coarea inequality;
- positive moments of worst conditional projection heights;
- law-uniform scalar quadratic van der Corput;
- post-rotation independence;
- bounded-diameter or fixed-fragment localization;
- one-good-minor selection as a universal reduction;
- the false near-zero half-Riesz continuation;
- the fresh false two-sided hyperbolic half-Riesz claim;
- a perturbative continuation of a zero mutual edge.

The additive-energy construction is itself a finite-fragment extreme-product construction, so it respects the exact B13 extremal-law class. The slope-offset theorem works directly for arbitrary cap-one laws and hence transfers to indicator extremizers with zero loss.

## 8. Status

- `QFORM-SAME-SET-ADDITIVE-ENERGY-NOUNIFORM-v1`: **PROVED THIS RUN**.
- support-only same-extreme parallelogram deconvolution: **REFUTED AS A UNIFORM MECHANISM**.
- `QFORM-SLOPE-OFFSET-LINF-v1`: **PROVED THIS RUN**.
- designated account03/B13 r17 bankwise row-energy theorem: **APPLIED** through (5.3)-(5.5).
- `QFORM-NEARNULL-TWOBANK-SLOPE-OFFSET-PAYMENT-v1`: **OPEN**.
- exact-rank-three QFORM: **OPEN**.
- full owner QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
