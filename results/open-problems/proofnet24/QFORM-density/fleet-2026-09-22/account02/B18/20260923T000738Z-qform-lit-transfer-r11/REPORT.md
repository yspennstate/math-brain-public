# account02/B18 — literature-to-proof transfer, strict-N3 cross-rank obstruction and paid branches

Status: **supporting theorems proved; full QFORM remains OPEN / NOT PROVED.**

Run: `20260923T000738Z-qform-lit-transfer-r11`.

Control/source pins used in this run:

- pinned owner synthesis package `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` in `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`;
- completed partner account03/B18 r19, canonical proof `yspennstate/math-open-problems@9415d0f2696d2e6ca05243c8e8f34b665bf5d42f`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260922T225637Z-account03-B18-QFORM-r19/ADDENDUM_CROSSBLOCK.md`;
- primary source Madiman–Melbourne–Xu, *Rogozin's convolution inequality for locally compact groups*, arXiv:1705.00642, Theorem 1.5 and §2.1;
- primary source Livshyts–Paouris–Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949v2.

The live owner reduction is the strict no-pivot statement N3: for a fixed `tau in (0,1]`, control forms with at least three eigenvalues of modulus at least one under

`|A_ii| < tau` and `|det A[{i,j},{i,j}]| < tau` for every physical coordinate pair.

N3 is still open. The first unpaid implication after the present run is stated in §6.

## 1. Primary-source transfer: exact extreme-law reduction for interval concentration

### Claim `QFORM-MMX-OPEN-INTERVAL-EXTREME-v1`

Fix `n`, a real quadratic polynomial

`Q(x)=x^T A x+b^T x+c`,

and a bounded open interval `J=(s,s+h)`. Among all independent input laws on `R` with densities bounded by one,

`sup P(Q(X) in J)`

is unchanged if each input density is restricted to the form `1_U`, where `U` is a compact measurable subset of `R` of Lebesgue measure one. The same supremum is unchanged if one further restricts to measure-one finite unions of bounded intervals.

This is a **supremum reduction for a fixed interval**, not a statement that one universal extreme law dominates all intervals or all quadratic forms.

### Proof and source match

Let `P_1(R)` denote the probability measures absolutely continuous with respect to Lebesgue measure with essential density cap one. Define

`Phi_J(mu_1,...,mu_n) = (mu_1 x ... x mu_n)(Q^{-1}(J))`.

For each coordinate separately the product measure is affine in that coordinate, hence `Phi_J` is coordinate-affine and therefore coordinate-convex. Because `Q` is continuous and `J` is open, `Q^{-1}(J)` is open. Product weak convergence follows from weak convergence of the marginals, and Portmanteau gives lower semicontinuity of `Phi_J`.

Madiman–Melbourne–Xu Theorem 1.5 applies to Polish measure spaces with regular Borel reference measures and to every coordinate-convex lower-semicontinuous functional on the product of capped-density classes. In the non-atomic case their §2.1 identifies the extreme class exactly as compactly supported measures with density `m 1_U`, `alpha(U)=1/m`. Taking Lebesgue reference measure and `m=1` yields the first assertion.

For the finite-union assertion, let `U` be compact with `|U|=1`. By regularity, approximate `U` in symmetric difference by a finite union of bounded intervals. Adjust one endpoint, or add/remove one tiny disjoint interval, to make the approximant `V` have exactly measure one while keeping `|U triangle V|` arbitrarily small. The total variation distance of `1_U dx` and `1_V dx` is `|U triangle V|/2`. For product laws, the total variation distance is at most the sum of the marginal total variation distances, so every fixed event probability, in particular `{Q in J}`, changes by arbitrarily little.

Finally, an essential density bound `||p_Q||_infinity <= C` is equivalent to

`P(Q in (s,s+h)) <= C h` for every `s` and `h>0`.

The reverse implication does not assume a density in advance: interval domination implies domination by `C` times Lebesgue measure on open sets and hence absolute continuity with Radon–Nikodym derivative at most `C` almost everywhere. Thus both the full conjecture and N3 may, at the level of the universal supremum, be tested on finite-union indicator laws. This does **not** add any support-radius or moment bound: the sets may be arbitrarily far apart and highly disconnected.

This transfer is source-matching. No rearrangement theorem for linear maps is being extended to a quadratic map; only MMX's general extreme-point Theorem 1.5 is used.

## 2. A strict-N3 counterfamily to rank-three physical-cross extraction

### Claim `QFORM-N3-CROSSRANK3-EXTRACTION-FALSE-v1`

For every fixed `tau in (0,1]` there are target-valid matrices in strict N3 for which **every physical bipartition has cross-block rank at most two**.

For `m>=2`, let

`g_m = m^{-1/2} 1_m`,

`S_m = [[0, g_m^T],[g_m, 0_{m x m}]]`,

and set

`A_m = S_m direct_sum (J_m/m)`.

Then:

1. `spec(S_m)={1,-1,0^(m-1)}` and `spec(J_m/m)={1,0^(m-1)}`, hence `A_m` has exactly three nonzero eigenvalues `1,-1,1`.
2. Every star diagonal is zero and every bank diagonal is `1/m`.
3. Every physical `2 x 2` principal determinant has modulus either `0` or `1/m`: hub/leaf pairs have determinant `-1/m`; all leaf/leaf and same-bank pairs have determinant zero; pairs from different direct-sum components have determinant zero.
4. Therefore, whenever `m>1/tau`, all actual diagonal and pair-minor inequalities of strict N3 hold.
5. For every physical partition `I | J`, the star cross block has rank at most one: the hub belongs to one side, so all cross-star entries occupy one row or one column. The rank-one bank cross block also has rank at most one. Since the two components are on disjoint row and column sets,

`rank((A_m)_{I,J}) <= 2`.

Thus neither N3 nor the full spectral hypothesis can force a rank-`>=3` physical cross cut. This is a structural counterexample only; it is **not** a counterexample to bounded density.

The construction is source-compatible with the pinned `RESULTS.md` observation that a star plus a rank-one term can have every physical off-diagonal block of rank at most two. The point added here is that the normalized star plus normalized bank can be made to satisfy the *strict N3 physical no-pivot inequalities themselves*.

## 3. The same obstruction is paid by the pinned hub theorem

The previous family does not threaten QFORM. The pinned `RESULTS.md` Theorem H closes it, and more generally closes a source-coordinate star-plus-diffuse-bank class.

Let `g in R^p`, `||g||_2>=1`, and let `v in R^q`, `||v||_2=1`, with `|lambda|>=1`. Consider the direct-sum quadratic matrix made from

`[[0,g^T],[g,0]]`

and `lambda v v^T`. Assume the physical leverage conditions

`max_j g_j^2/||g||_2^2 <= 1/2`,

`max_k v_k^2 <= 1/2`.

Choose Theorem H with hub set `H={hub}`, light set `I={all star leaves and all bank coordinates}`, `J=empty`, and rank parameter `r=1`. On `I`,

`A_II=lambda v v^T`,

and the extended row vectors are `(0,g_j)` on star leaves and `(v_k,0)` on bank coordinates. Hence

`G_tilde = diag(1, ||g||_2^2)`,

`det G_tilde = ||g||_2^2`,

and the normalized row leverages are exactly `g_j^2/||g||_2^2` and `v_k^2`. Theorem H therefore gives, uniformly over arbitrary independent cap-one input laws,

`|phi_Q(t)| <= 4 pi^(3/2) |lambda|^(-1/2) ||g||_2^(-1) |t|^(-3/2)`.

Writing

`K=4 pi^(3/2) |lambda|^(-1/2)||g||_2^(-1)`,

and using also `|phi_Q(t)|<=1`,

`int_R min(1,K|t|^(-3/2)) dt = 6 K^(2/3)`.

Fourier inversion gives a continuous density and the exact bound

`||p_Q||_infinity <= (3/pi)K^(2/3)`

`= 3*2^(4/3) |lambda|^(-1/3)||g||_2^(-2/3)`

`<= 3*2^(4/3) < 7.56`.

For `A_m` above, `||g_m||_2=1`, `v=m^{-1/2}1_m`, and both leverage maxima are `1/m<=1/2`. Consequently every member of the strict-N3 counterfamily satisfies

`||p_{X^T A_m X}||_infinity <= 3*2^(4/3) = 7.559526299...`

for **every** independent cap-one input law, and the density has a continuous representative.

This is an actual application of a completed theorem from the pinned owner package to the live N3 obstruction. It shows why “all physical cuts have rank <=2” is not itself a counterexample mechanism: rank can be organized into source-coordinate hubs, and a hub supplies a full `|t|^{-1}` factor while one diffuse square supplies the additional `|t|^{-1/2}`.

## 4. Completed partner application: three diffuse physical banks

The latest completed designated-partner result used here is account03/B18 r19, `QFORM-CROSSBLOCK-RANKGE3-FRESNEL-v1`, proved at `math-open-problems@9415d0f2696d2e6ca05243c8e8f34b665bf5d42f`.

Its exact statement needed here is: for a bipartition of the **original independent coordinates**, arbitrary measurable same-side phases `F(X_I),G(X_J)`, and physical cross matrix `B` of rank `r>=3` with nonzero singular values `sigma_1,...,sigma_r`,

`||p_Q||_infinity <= [2r/(r-2)] (prod sigma_l)^(-1/r)`.

For `r=3` this is

`||p_Q||_infinity <= 6 (sigma_1 sigma_2 sigma_3)^(-1/3)`.

The partner proof uses a thin SVD *inside each already-independent physical block*, LPP projection-density caps, complex amplitudes, Cauchy–Schwarz and Plancherel. It never asserts that all rotated coordinates are independent.

Primary-source verification of the LPP input: arXiv:1507.07949v2 states that for a product density `f=prod f_i` with `||f_i||_infinity<=1`, every `k`-dimensional orthogonal marginal has density cap at most `2^(k/2)`. It assumes neither moments, bounded support, log-concavity nor smoothness. This is exactly the use in the partner proof. If a physical block has dimension exactly `k`, its orthogonal transform trivially has joint density cap at most one, so the full-dimensional endpoint needs no extension of LPP.

Now let `S_1,S_2,S_3` be disjoint physical supports, let `u_l` be unit vectors supported on `S_l`, and let `|lambda_l|>=1`. Put

`A = direct_sum_{l=1}^3 lambda_l u_l u_l^T`.

Assume

`max_i u_l(i)^2 <= delta < 1/2` for `l=1,2,3`.

For each `l`, greedily collect coordinates until the squared mass first reaches `1/2`. Since every atom is at most `delta`, one obtains a subset with squared mass

`s_l in [1/2,1/2+delta]`.

Use those three subsets as one side of a single global physical cut. The three cross-bank pieces occupy orthogonal row and column supports and therefore have singular values

`sigma_l = |lambda_l| sqrt(s_l(1-s_l))`

`>= |lambda_l| sqrt(1/4-delta^2)`.

The partner theorem gives the **target-level** bound

`||p_Q||_infinity`

`<= 6 |lambda_1 lambda_2 lambda_3|^(-1/3) (1/4-delta^2)^(-1/2)`

`<= 12/sqrt(1-4delta^2)`.

For `delta<=1/4`, this is at most `8 sqrt(3) = 13.85640646...`.

This class genuinely intersects strict N3. If `|lambda_l| max_i u_l(i)^2 < tau` for each bank, every diagonal is below `tau`; same-bank `2 x 2` minors vanish, and a pair from distinct banks has determinant equal to the product of two diagonal entries, hence magnitude `<tau^2<=tau`.

In particular, for even `m`,

`A = (J_m/m) direct_sum (J_m/m) direct_sum (-J_m/m)`

lies in strict N3 once `m>1/tau`, and the exact half-support cut has `sigma_1=sigma_2=sigma_3=1/2`. Thus

`||p_Q||_infinity <= 12`.

This partner application is complementary to §3: diffuse three-bank N3 forms are paid by a rank-three physical cross cut; star-plus-bank N3 forms can have no such cut but are paid by Theorem H.

## 5. A necessary cross-volume geometry for any genuine counterexample sequence

The pinned `FOURIER_ROUTE_REPORT.md` proves the unconditional five-volume decoupling bound. For any physical bipartition `I|J`, put `B=A_IJ` and

`Z_5(B)=e_5(B^T B)`.

Then, with no marginal condition,

`||p_Q||_infinity <= 5 sqrt(2e) Z_5(B)^(-1/10)`.

Therefore, if `M=||p_Q||_infinity`, every cut satisfies

`Z_5(A_IJ) <= (5 sqrt(2e)/M)^10`.

Consequently any target-valid sequence with `M_k -> infinity` would necessarily obey the strong matrix condition

`sup_{I|J} e_5((A_IJ)^T A_IJ) -> 0`.

This is not heuristic; it is a direct rearrangement of a completed source theorem. It rules out any counterexample mechanism retaining a fixed amount of five-dimensional physical cross volume on even one cut.

The partner theorem sharpens the same necessary geometry on exact low cross rank. If some cut has exact cross rank three,

`M <= 6 (sigma_1 sigma_2 sigma_3)^(-1/3)`, hence

`sigma_1 sigma_2 sigma_3 <= (6/M)^3`.

If it has exact cross rank four,

`M <= 4 (sigma_1 sigma_2 sigma_3 sigma_4)^(-1/4)`, hence

`sigma_1 sigma_2 sigma_3 sigma_4 <= (4/M)^4`.

Finally, the pinned D' theorem says that if the volume-sampling row marginal of a rank-three cut is bounded by a fixed `h<3/4`, then

`M <= 6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1) Z_3^(-1/6)`.

Thus an unbounded-density sequence must simultaneously make every five-volume vanish, make the singular product vanish on every exact rank-three/four cut, and force any surviving three-volume into the high-marginal/hub regime or into higher-rank near-degeneracy. The strict-N3 star-plus-bank construction shows that the hub regime is real, but §3 shows its simplest realization is already paid.

## 6. First unpaid implication

The structural statement “strict N3 forces a rank-three physical cross cut” is false by §2, so it must not appear in a full proof.

The first honest unpaid implication is instead:

### `QFORM-N3-HUB-OR-CROSSVOLUME-GLUE-v1`

For one fixed `tau in (0,1]`, let `A` satisfy the N3 physical no-pivot inequalities and have three eigenvalues of modulus at least one. Prove, with universal quantitative parameters, that at least one of the following source-coordinate payable alternatives occurs:

1. a physical cut with enough three/five-dimensional cross volume and sufficiently nonconcentrated row volume to invoke D', D5, or the account03/B18 cross-block theorem; or
2. a source-coordinate hub/light-block frame satisfying a Theorem-H determinant/leverage condition with dimension-free payment; or
3. one of the already completed scalar-pivot/ridge/physical-pair branches from the owner synthesis.

A proof may not rotate the product law and infer independence afterwards, and an arbitrary bounded joint projection density is not a substitute for product provenance.

The present calculations suggest the right matrix invariant is not cross rank alone but a dichotomy between distributed exterior volume and concentrated source-coordinate incidence (“hub mass”). D5 supplies a quantitative certificate for the first side; the normalized star construction identifies a genuine model for the second side.

## 7. Scope and correction status

What is proved here:

- an exact primary-source extreme-law reduction for interval concentration to compact measure-one indicator laws, and hence by approximation to finite unions of intervals;
- a strict-N3 family refuting rank-three physical-cross extraction;
- a universal continuous-density bound `<7.56` for that family via the pinned Theorem H;
- a universal partner-derived bound for three diffuse disjoint rank-one banks, including a strict-N3 uniform-bank family with bound `12`;
- necessary vanishing of physical five-volume, and corresponding low-rank cross singular products, along any hypothetical unbounded-density sequence.

What is **not** proved:

- N3 in full;
- the unrestricted QFORM conjecture;
- any support, variance, moment, log-concavity or smoothness reduction;
- independence of coordinates after a general rotation;
- novelty from a literature search miss;
- continuity for branches where the invoked theorem only supplies essential boundedness.

The extreme-law reduction is variational and interval-by-interval; it does not validate finite numerical search as a proof and does not furnish a universal compact support radius. The complete target therefore remains **OPEN / NOT PROVED**.
