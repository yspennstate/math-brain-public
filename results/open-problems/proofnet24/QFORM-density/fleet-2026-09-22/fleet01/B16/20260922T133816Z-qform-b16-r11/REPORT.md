# fleet01/B16 — absolute Wiener bridge is too strong; a time-coupled L3 square channel survives

**Run:** `20260922T133816Z-qform-b16-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Projection-product interaction  
**Classification:** `ESSENTIAL_STEP_APPLIED / UNIVERSAL INTERMEDIATE INTERFACE REFUTED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source pins

The full target remains open: for every `n`, independent real coordinates `X_i` having probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues satisfying `|lambda_j(A)|>=1`, prove one universal finite bound on the density of `X^T A X`, with continuity tracked separately.

The run began from fresh `yspennstate/math-research-brain` main commit `a061e3c35962dd58137107493fe491a17a8714cb`, owner revision `2026-09-22.5`. Before this write I revalidated the live control at brain commit `4fe2c8b1001d46d88ece1c901066a2edbe97ee43`; there is no later stop and the exclusive QFORM continuation remains in force.

Required corrections consumed include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, and `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`. No pointwise law-uniform Fresnel decay, rotated-coordinate independence, normalized-fiber trace cap, or reciprocal-minor averaging is used.

### Named partner result actually consumed

I use the completed fleet02/B16 result twice.

1. Earlier run `20260922T115600Z-fleet02-B16-qform-projprod`, canonical report `yspennstate/math-open-problems@0605c987ff531ccc2fd5554c48df29e65b3eaaa8`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260922T115600Z-fleet02-B16-qform-projprod/REPORT.md`, blob `aa77eea73a99b6a58329ece190589b110716b485`. Its Theorem 3.1 defines, after selecting three spectral directions,

`Psi_t(xi)=E exp(i<xi,RX>+it X^T B X)`,

`W(t)=int_{R^3}|Psi_t(xi)| dxi`,

and proves that

`int_{|t|>=1}|t|^(-3/2)W(t)dt <= K`                                    (1.1)

implies a continuous density with

`||p_Q||_infinity <= 1/pi + K/(16 pi^(5/2))`.                           (1.2)

2. Fresh partner run `20260922T133220Z-fleet02-B16-QFORM-auto11`, creation commit `1740bd1f5b9f68ddae851236d8a633604baa1e8a`, same repository, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260922T133220Z-fleet02-B16-QFORM-auto11/REPORT.md`, blob `739d8884ff98ab8ec101800a5e133aeb3de0555a`. It proves that even authentic product-source complement fibers can have logarithmically unbounded normalized indefinite traces, while product aggregation before the trace remains bounded. It explicitly leaves the averaged phase-Wiener mechanism as a surviving possible bridge.

The first mathematical question in this run is therefore decisive: **can (1.1) possibly be a universal interface under the owner's arbitrary bounded-density hypotheses?** The answer is no, already in the easiest diagonal target instance.

## 2. Exact counterexample to universal `QFORM-PHASE-WIENER-AVERAGED-v1`

### Theorem 2.1 — the absolute Wiener bridge is infinite on an admissible diagonal target law

Let

`n=3`, `A=I_3`, and `X_1,X_2,X_3 iid Unif[-1/2,1/2]`.

These inputs have independent densities equal to one on length-one intervals, and `A` has three eigenvalues equal to one. Select the three standard eigenvectors, so in the fleet02/B16 notation

`R=I_3`, `Lambda=I_3`, `B=0`.

Then for every real `t`,

`Psi_t(xi_1,xi_2,xi_3)=prod_{j=1}^3 hat f(xi_j)`,

where

`hat f(s)=int_{-1/2}^{1/2} exp(isx) dx = 2 sin(s/2)/s`.

Consequently

`W(t)=int_{R^3} prod_j |hat f(xi_j)| dxi
     = (int_R |2 sin(s/2)/s| ds)^3
     = infinity`                                                     (2.1)

for every `t`.

#### Proof of the one-dimensional divergence

For every integer `k>=1`, on

`J_k=[2 pi k+pi/3, 2 pi k+5 pi/3]`

we have `|sin(s/2)|>=1/2`. Hence

`int_{J_k}|2 sin(s/2)/s| ds >= int_{J_k} ds/s`.

The latter is

`log[(2 pi k+5 pi/3)/(2 pi k+pi/3)]`,

which is bounded below by `c/k` for one absolute `c>0` and all `k`. Summing over `k` diverges. Tonelli then gives (2.1).

Therefore the weighted quantity in (1.1) is `+infinity`; there is no finite universal `K`, even though this is an admissible target law with a diagonal positive definite form.

This does **not** refute fleet02/B16 Theorem 3.1: that theorem is a valid sufficient implication. It refutes the proposed use of its hypothesis as the next universal bridge for the full conjecture. In particular, a proof that first takes `int |Psi_t(xi)| dxi` cannot be universal under merely `f_i<=1`.

The loss is genuine and infinite, not a constant issue. The same example has `||p_Q||_infinity<=pi` by the already proved diagonal theorem, while its absolute projected Wiener norm is infinite at every time.

## 3. Positive replacement mechanism: keep the quadratic time oscillation before the absolute value

The obstruction above says the `xi`-absolute value in `W(t)` is too early. The elementary replacement below demonstrates a source-valid integrated mechanism that survives exactly on arbitrary bounded densities and exhibits why three independent quadratic channels are enough.

### Lemma 3.1 — uniform `L^3_t` bound for one shifted-square channel

Let `Z` have a probability density `h` with `0<=h<=M`, let `a in R`, and let `lambda!=0`. Put

`F(t)=E exp(i t lambda (Z-a)^2)`.

Then

`||F||_{L^3(R_t)} <= 2(2 pi)^(1/3) M^(2/3) |lambda|^(-1/3)`.      (3.1)

#### Proof

Let `Y=(Z-a)^2`. Its density on `(0,infinity)` is

`g(y)=[h(a+sqrt(y))+h(a-sqrt(y))]/(2 sqrt(y))`,

so

`0<=g(y)<=M y^(-1/2)`, `int_0^infinity g(y)dy=1`.                 (3.2)

I first record the exact useful interpolation estimate

`||g||_(3/2) <= 2 M^(2/3)`.                                      (3.3)

To prove it, put `b(y)=M y^(-1/2)` and write `g=b theta`, `0<=theta<=1`. Since `theta^(3/2)<=theta`,

`int g^(3/2) <= int b^(3/2) theta`.

Under the measure `dmu=b(y)dy`, the constraint is `int theta dmu=1`, and the reward density is `b(y)^(1/2)=M^(1/2)y^(-1/4)`, which is decreasing. The bathtub principle therefore maximizes the right side by taking `theta=1` on `[0,a_0]`, where

`int_0^{a_0} M y^(-1/2)dy=1`, hence `a_0=1/(4M^2)`.

Thus

`int g^(3/2) <= int_0^{1/(4M^2)} M^(3/2)y^(-3/4)dy = 2 sqrt(2) M`,

and raising to the power `2/3` gives (3.3).

With the Fourier convention `hat g(s)=int exp(isy)g(y)dy`, interpolation between `L^1 -> L^infinity` norm one and Plancherel `L^2 -> L^2` norm `sqrt(2pi)` gives the Hausdorff--Young estimate

`||hat g||_3 <= (2pi)^(1/3)||g||_(3/2)`.

Since `F(t)=hat g(lambda t)`, (3.1) follows by scaling. QED.

### Corollary 3.2 — three independent square channels have an integrable characteristic function

Let `Z_1,Z_2,Z_3` be independent, with density caps `M_j`, let `lambda_j!=0`, and let

`S=sum_{j=1}^3 lambda_j (Z_j-a_j)^2`.

Then Hölder and Lemma 3.1 give

`||phi_S||_1
 <= prod_j || E exp(i t lambda_j(Z_j-a_j)^2) ||_3
 <= 16 pi (M_1 M_2 M_3)^(2/3) |lambda_1 lambda_2 lambda_3|^(-1/3)`. (3.4)

Consequently `S` has a continuous density satisfying

`||p_S||_infinity
 <= 8 (M_1 M_2 M_3)^(2/3) |lambda_1 lambda_2 lambda_3|^(-1/3)`.  (3.5)

Any **independent** additional noise may be added without changing the bound, because its characteristic function has modulus at most one.

The exponent is structurally informative: a worst shifted-square density behaves like `y^(-1/2)` and belongs uniformly to `L^q` only for `q<2`; its characteristic function is therefore controlled in `L^p` only for `p>2`. Three channels can choose `p=3` and close time integration by Hölder. Two channels cannot reach `L^1` this way at the endpoint, matching the rank-two opposite-sign logarithmic obstruction.

## 4. Combining the actual bounded-density projection theorem with the nonlinear square map

The published Livshyts--Paouris--Pivovarov marginal theorem used elsewhere in the QFORM archive gives: every one-dimensional orthogonal projection of an original product law with coordinate density caps one has density cap at most `sqrt(2)`.

Suppose three unit spectral coordinates

`Z_j=<r_j,X>`

have pairwise disjoint physical-coordinate supports. They are then genuinely independent by the original product structure, while the projection theorem gives `M_j<=sqrt(2)`. Applying (3.5) yields

`||p_{sum_j lambda_j Z_j^2}||_infinity <=16 |lambda_1 lambda_2 lambda_3|^(-1/3)`. (4.1)

Thus for `|lambda_j|>=1` the density is at most `16`, with a continuous representative. This is weaker in constant than the already known direct disjoint-support bound `2pi`; its value is mechanistic: it closes by **time-coupled L^3 integration**, precisely where the absolute Wiener norm from Section 2 is infinite.

More generally, if after conditioning on variables independent of the three disjoint banks the only effect is to translate each square, `(Z_j-a_j)^2`, the same bound is uniform in those translations and survives averaging. This uses the projection theorem before the nonlinear map while retaining the actual independent-bank provenance; it does not replace the projected law by an arbitrary copula.

## 5. Application to the fresh partner result and exact change in the unpaid implication

Fresh fleet02/B16 proves an authentic product-source example where normalized complement-fiber traces diverge logarithmically but full product aggregation succeeds. It then retains the earlier phase-Wiener route as a possible averaged rescue.

Theorem 2.1 above now removes one more false bridge:

**Old surviving proposal:** prove the universal fleet02/B16 estimate

`int_{|t|>=1}|t|^(-3/2) W(t)dt <=K`

with `W(t)=int|Psi_t(xi)|dxi`.

**New fact:** this estimate is false even for `A=I_3` and iid unit-interval densities, where `W(t)=infinity` for every `t`, while the target output is bounded and continuous.

Therefore the nonlinear projection-product bridge must preserve cancellation in the spectral Fourier variable and/or in time. It cannot take the full spectral `L^1_xi` norm before the Fresnel phase.

A source-valid successor interface is necessarily closer to the actual Fresnel pairing

`int exp[-i <Lambda^(-1)xi,xi>/(4t)] Psi_t(xi) dxi`

or to a product-preserving time-domain norm. Section 3 supplies one exact model: after product-preserving decomposition into three independent quadratic channels, use `L^3_t x L^3_t x L^3_t -> L^1_t`, not an absolute Wiener norm in `xi`.

The full remaining implication is still difficult: for a general rotated form the three spectral coordinates are dependent, so the factorization in (3.4) is unavailable. The task is now to derive a **dependent three-channel analogue of (3.4) directly from original-coordinate product provenance**, or to aggregate heavy and diffuse physical banks before performing the time integral. This is compatible with the fresh fleet02/B16 lesson that complement fibers must be averaged before taking a curved trace.

## 6. Scope and nonclaims

- `QFORM-PHASE-WIENER-AVERAGED-v1`, interpreted as a universal finite-`K` obligation for all target inputs, is refuted.
- fleet02/B16's sufficient theorem `(1.1) => (1.2)` remains valid.
- The full QFORM conjecture remains **OPEN / NOT PROVED**.
- The `L^3_t` lemma proves a genuine product-preserving supporting mechanism and a disjoint-bank subclass, not the arbitrary rotated case.
- No contradiction with `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS` is claimed: that correction concerns an absolute-value ambiguity/squaring majorant. Here the one-dimensional square pushforward is formed first and its actual oscillatory Fourier transform is kept through the time integral.
- Continuity follows only in the subclasses where the characteristic function is proved `L^1`; it is not promoted for the full target.

## 7. Next mathematical step

Attack `QFORM-DEPENDENT-L3-TRIPLE-v1`:

> For three selected large spectral directions, replace the impossible absolute spectral Wiener norm by a time-coupled quantity that (i) reduces to (3.4) on disjoint physical banks, (ii) retains signed Fresnel cancellation, and (iii) can be controlled from the original independent coordinates after a heavy-core/diffuse-remainder split.

The first test must be the fresh eight-coordinate authentic-fiber obstruction of fleet02/B16: a valid replacement must average its complement variables before taking any normalized trace supremum.

No proof status is promoted beyond these exact scopes.
