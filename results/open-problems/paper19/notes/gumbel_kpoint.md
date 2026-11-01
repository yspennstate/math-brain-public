# k-point correlations and the full Gumbel law (conj:gumbel)

Agent note, 2026-06-28. Target: the headline conjecture `conj:gumbel` (Poisson hard-edge extreme
process; equivalently the Gumbel law `P{log M_m + b_m <= x} -> 1 - exp(-e^{d_F x})`). The first
intensity is proved (`EE Z_m^fl(x) -> e^{d_F x}`) and the one-sided Markov bound is proved. By the
method of (factorial) moments / Chen-Stein, the law follows from, for every fixed `k >= 2`,
```
  EE[(N_t)_k] = sum_{(T_1,...,T_k) distinct} P{ smin(A_{T_i}) <= tau_i, all i } -> prod_i lambda_i,
  lambda_i = e^{d_F x_i},   tau_i = e^{x_i - b_m}   (the CENTERED / critical scale).
```
This note asks whether the pair-correlation (k=2) keystone machinery
(`notes/keystone_synthesis.md`, `keystone_tail.md`: two-projection local CLT + small-codimension
negligibility + resolvent/local-law closure) extends to general `k`.

## VERDICT (one line)
PARTIAL, with a clean structural payoff: the feared "new k-point objects" (`det G_k` control,
k-tuple combinatorics) DISSOLVE -- for fixed `k` they collapse to the SAME two-point inputs as
k=2 -- so the MAIN term `lambda^k` closes modulo the SAME off-support local law as the keystone.
The genuine residual is NOT k-point at all: it is the **critical-scale cluster negligibility**,
already open at k=2 *beyond* `prob:pc`, because the bulk-scale `prop:small-D-negligible` has no
exponential room to spend at the centered scale. Precise residual stated in Section 5.

## 0. Setup, notation, and the two regimes

Calibration. With `N = N_m ~ gamma m`, the number of m-subsets is `binom(N,m) = e^{(h(gamma)+o(1))m}`,
`h(gamma) = gamma log gamma - (gamma-1)log(gamma-1)`. For one square n x n hard edge,
`P{smin <= tau} = (1+o(1)) kappa_n tau^{d_F}` with `kappa_n = n^{d_F/2}` (real: `~ sqrt(n) tau`;
complex: `~ n tau^2`). The centering `b_m` makes `lambda := binom(N,m) F_m(e^{-b_m}) = O(1)`, so the
single-event probability is
```
  p_1 := P{smin(A_T) <= tau} = F_m(tau) = lambda / binom(N,m)   (up to (1+o(1))),
```
i.e. EXPONENTIALLY small, `p_1 = e^{-(h(gamma)+o(1))m}`. THIS is the qualitative break from `prob:pc`,
whose threshold sits strictly below the critical line (`tau = e^{-sm}`, `s < h(gamma)/d_F`), where
`binom(N,m) F_m -> infty` and the second-moment method has exponential room.

Geometry of a single event. For `T` of size `m`, `smin(A_T) <= tau` is, to leading order and up to
the harmless `sqrt(m)` operator/Hilbert--Schmidt conversion (`min_i dist(a_i,H_i)/sqrt m <= smin <=
min_i dist(a_i,H_i)`), the event that some row is within `~tau` of the span of the others:
`dist(a_j, span(a_i : i in T\j)) = |<a_j, u_{T\j}>| <= tau'`, where `u_I` is the unit normal of the
`(m-1)`-row span `span(a_i : i in I)`. This is the "slab" picture and the `u_I` are exactly the
normals of `prob:pc`.

Classification of k-tuples by overlap. A k-tuple `(T_1,...,T_k)` is governed by its pairwise
codimensions `D_{ij} = m - |T_i cap T_j|`. Call the tuple SPREAD if all `D_{ij} >= eps m`, and
CLUSTERED otherwise (some pair shares all but `< eps m` rows). For a random pair, `|T_i cap T_j|` is
hypergeometric with mean `m^2/N = m/gamma`, so `D_{ij}` concentrates at `Dbar = m(1 - 1/gamma) =
Theta(m)`: a RANDOM tuple is spread, and clustered tuples carry exponentially small combinatorial
mass (made precise in Section 4).

## 1. The k-point local CLT (extends; no obstruction)

**Lemma (k-projection local CLT), informal.** Let `u_1,...,u_k in F^m` be fixed unit vectors with
Gram matrix `G_k = (<u_i,u_j>)_{i,j}` and let `x` be one isotropic, mean-zero, bounded-density row.
If the `u_i` are delocalized (`max_l sum_i |(u_i)_l|^2 = o(1)`, a Lindeberg/Lyapunov condition,
automatic for normals of generic high-dim spans) and `G_k` is non-degenerate, then for `t -> 0`
slowly relative to `lambda_min(G_k)`,
```
  P{ |<x,u_i>| <= t  for all i }  =  (1 + o(1)) (c_F t^{d_F})^k (det G_k)^{-d_F/2},
```
with `c_F` the slab/disk constant (`2 phi(0)` real, `pi^{-1}` complex normalization).

Proof mechanism, and why it extends verbatim from k=2. The vector `Y := U^* x in F^k`
(`U = [u_1...u_k]`) has covariance `U^* U = G_k`. Its density at 0 is obtained by k-fold Fourier
inversion `f_Y(0) = (2pi)^{-dk} int phi_Y(xi) dxi`, and `phi_Y(xi) = prod_l psi_l(xi)` factorizes
over the independent coordinates `x_l` of `x` -- this is the SAME char.-function argument as the
two-projection lemma `lem:two-proj`, only with a `k x k` covariance in the Gaussian exponent
`exp(-1/2 xi^* G_k xi)` instead of `2 x 2`. The bounded-density hypothesis supplies the
integrable high-frequency tail (`|psi_l|` bounded away from 1 off a neighborhood of 0), giving
`f_Y(0) -> (2pi)^{-dk/2} (det G_k)^{-d_F/2}` uniformly; multiply by the slab volume `(c_F t^{d_F})^k`.
Multivariate local CLTs of exactly this form are standard. **No new obstruction in the CLT itself.**

Domain of validity / where the danger actually sits. The approximation degrades precisely when
`det G_k -> 0` (some `u_i` nearly dependent on the others): then the Gaussian profile is too flat
on scale `t` and the error swamps the main term. So ALL the difficulty migrates out of the CLT and
into (i) the size of the random factor `(det G_k)^{-d_F/2}` in expectation and (ii) which overlap
configurations realize `det G_k` small. This is the exact analogue of the k=2 statement, where the
factor is `(1 - |rho|^2)^{-d_F/2} = (det G_2)^{-d_F/2}` and the danger is `|rho| -> 1`.

Caveat (which configuration the single-`x` model describes). The clean `det G_k` factor above is the
joint law of ONE shared test row `x = a_j` tested against `k` normals `u_{I_i}`, i.e. the
configuration `T_i = I_i cup {j}` with a COMMON distinguished row `j`. This is the richest
singularity and the natural k-point generalization of the dangerous k=2 "shared-test-row" pair. For
mixed configurations (different subsets use different test rows) the joint event is a PRODUCT of
such determinant factors over the shared-row blocks; those are handled by the same analysis applied
block-by-block (Section 3).

## 2. The main term: `det G_k` collapses to PAIRWISE control (fixed k)

This is the central positive finding. The paper lists "bulk higher-order normal-overlap asymptotic
independence" as a *separate* needed input beyond `prob:pc`, suggesting a genuinely k-point analytic
object. It is not: for FIXED `k` the determinant factor is controlled by the `binom(k,2)` PAIRWISE
overlaps alone.

**(P1) No joint near-degeneracy without a large pairwise overlap.** `G_k = I + E`, `E` the
off-diagonal overlap matrix. By Gershgorin (rows of `E` have zero diagonal, `ell_1` mass
`sum_{j != i}|rho_{ij}|`),
```
  lambda_min(G_k) >= 1 - max_i sum_{j != i} |rho_{ij}| >= 1 - (k-1) max_{i<j} |rho_{ij}|.
```
Hence if `max_{i<j} |rho_{ij}| <= delta < 1/(k-1)` then `det G_k >= (1 - (k-1)delta)^k > 0`. So `k`
unit vectors with all pairwise overlaps small are necessarily well-conditioned: there is NO
"k vectors jointly coplanar yet pairwise near-orthogonal" route to a small determinant when `k` is
fixed. (Three vectors at mutual angles near `90deg` are near-orthonormal, `det ~ 1`; to make them
coplanar you must enlarge some pairwise inner product.) This kills the only candidate genuinely
k-point degeneracy.

NB the analogous *product* bound `det G_k >= prod_{i<j}(1 - |rho_{ij}|^2)` is FALSE for sign-mixed
overlaps (k=3, `rho_{12}=rho_{13}=t, rho_{23}=-t`: `det = 1 - 3t^2 - 2t^3 < (1-t^2)^3`), so the
control must go through `lambda_min`/Gershgorin, not a naive factorization.

**(P2) Spread expectation -> 1 from the k=2 keystone alone.** On spread tuples (all `D_{ij} >=
eps m`) each `|rho_{ij}|^2 = O(1/D_{ij}) = O(1/m) -> 0` in probability, so `det G_k -> 1`. For the
SUM we need the expectation. Split on `B = {some |rho_{ij}| > 1/(2(k-1))}`:
- On `B^c`: `lambda_min(G_k) >= 1/2`, so `(det G_k)^{-d_F/2} <= 2^{d_F k/2} = O(1)`, and
  `det G_k = 1 - sum_{i<j}|rho_{ij}|^2 + O(max|rho|^3) -> 1`; bounded convergence gives
  `EE[(det G_k)^{-d_F/2}; B^c] -> 1`.
- On `B`: the leading contribution is exactly one large pair `(i,j)`, where
  `det G_k = (1 - |rho_{ij}|^2)(1 + o(1))`, so
  `EE[(det G_k)^{-d_F/2}; B] <= (1+o(1)) sum_{i<j} EE[(1 - |rho_{ij}|^2)^{-d_F/2}; |rho_{ij}| > delta,
  D_{ij} >= eps m] -> 0`
  by the keystone bound `EE[(1-|rho|^2)^{-d_F/2}; D >= eps m] <= 1 + o(1)` applied per pair (its
  large-overlap part on spread is `o(1)`).
```
  ==>  EE[(det G_k)^{-d_F/2} ; SPREAD]  ->  1.
```

**(P3) Higher pairwise negative moments are free.** (P2) needed `EE[(1-|rho_{ij}|^2)^{-p}]` only at
the keystone order `p = d_F/2`. The finer bookkeeping in Section 3/4 needs `p` up to `d_F k/2`
(fixed). These are ALSO supplied by the existing inputs: the tail bound (T) of `keystone_tail.md`,
`P{1-|rho|^2 <= y} <= (C sqrt y)^{D-1} + e^{-cD}`, makes `EE[(1-|rho|^2)^{-p}]` converge whenever
`p < (D-1)/2`, and `D = Theta(m) -> infty` beats every fixed `p`. The mean input is the same
`EE|rho|^2 = O(1/D)`. So no new local-law estimate is needed for any fixed-order negative moment.

**Consequence.** The spread tuples (which carry `1 - o(1)` of the combinatorial mass, Section 4)
contribute `prod_i lambda_i = lambda^k`, modulo the SAME off-support anisotropic local law
[KnowlesYin2017, BEKYY2014] that closes the k=2 keystone -- nothing more. The "higher-order normal
overlap asymptotic independence" is genuinely a corollary of the pairwise statement, for fixed `k`.

## 3. Chen-Stein: ALL k collapse to two-point terms (no new k-tuple combinatorics)

Independent of the moment route, the Arratia-Goldstein-Gordon (AGG) local Poisson approximation
shows the headline worry "k-tuple combinatorics" never materializes. Index events by
`alpha = T` (an m-subset), `I_alpha = 1{smin(A_T) <= tau}`, `p_alpha = p_1`. With a dependency
neighborhood `B_alpha`,
```
  d_TV( N_t , Poisson(lambda) )  <=  b_1 + b_2 + b_3,
  b_1 = sum_alpha sum_{beta in B_alpha} p_alpha p_beta,
  b_2 = sum_alpha sum_{beta in B_alpha, beta != alpha} EE[I_alpha I_beta],
  b_3 = sum_alpha EE | EE[ I_alpha - p_alpha | sigma(I_beta : beta notin B_alpha) ] |.
```
If `d_TV -> 0` then `N_t -> Poisson(lambda)`, which gives the FULL Gumbel law in one shot (all `k`
simultaneously) -- and `b_1, b_2` are PAIRWISE sums, `b_3` is a one-vs-field conditional term. There
is no sum over k-tuples for `k >= 3` anywhere. So the only question is the choice of `B_alpha` and
the size of these three two-point/one-point quantities.

The neighborhood is forced to be SMALL. Two natural choices:
- `B_alpha = {beta : beta shares >= 1 row with alpha}`. Then non-neighbors are row-disjoint from
  `alpha`, so `b_3 = 0` exactly. But `sum_{beta in B_alpha} p_beta = p_1(binom(N,m) - binom(N-m,m))
  = lambda(1 - e^{-c_gamma m}) ~ lambda`, whence `b_1 ~ lambda * lambda = lambda^2 -/-> 0`. FAILS.
- `B_alpha = {beta : 1 <= D(alpha,beta) < eps m}` (only strong overlaps). Then
  `b_1 = sum_alpha p_1 (p_1 |B_alpha|) = lambda^2 |B_alpha|/binom(N,m) = lambda^2 e^{-c(eps) m} -> 0`
  (the clustered neighborhood is an exponentially small fraction of all subsets, Section 4). Good.
  Now `b_3 != 0` because spread `beta` (`D >= eps m`) STILL share up to `m - eps m` rows with
  `alpha`, so non-neighbors generate (collectively) almost all rows.

So with the working (small) neighborhood the budget is:
```
  b_1 -> 0     (pure counting; exp-small clustered neighborhood),
  b_2 = sum over CLUSTERED pairs of EE[I_alpha I_beta]   <-- critical-scale cluster negligibility,
  b_3 = decorrelation of I_alpha from the SPREAD field    <-- bulk asymptotic independence.
```
`b_2` is precisely the two-point clustered sum; `b_3` is the rigorous home of "bulk higher-order
normal-overlap asymptotic independence." Crucially, both are TWO-POINT-flavoured: `b_2` is a literal
pairwise sum, and `b_3` is controlled by the weak dependence of a single event on the field, the
same local-CLT mechanism (`det G_2 -> 1`, i.e. a spread `beta` perturbs `I_alpha`'s conditional law
by `O(|rho|^2) = O(1/m)`) that already underlies the keystone. No genuinely new k-point determinant
or k-tuple count is required: the AGG reduction has done the combinatorial collapse for us.

## 3b. The factorial-moment route gives the same two needs (cross-check)

Directly, `EE[(N_t)_k] = lambda^k * EE_{configs}[ prod-of-det-factors ]`. The config sum splits into
SPREAD (-> `lambda^k` by Section 2) and tuples with >= 1 clustered pair. A tuple with exactly one
clustered pair `(i0,j0)` and the rest spread factorizes asymptotically into [clustered-pair
contribution] x [prod of `lambda_l` over the `k-2` spectators]; the clustered-pair contribution,
summed over clustered configs, is the SAME `b_2`-type quantity, `o(lambda^2)`. Summed over the
`binom(k,2)` choices of clustered pair, still `o(lambda^k)`. Tuples with `>= 2` clustered subsets
(e.g. a common-core "sunflower" `T_i = S cup P_i`) are rarer still; their enhancement is the
higher conditional-density moment `EE[(det G_j)^{-d_F/2}]` over a SHARED low-dim null space, which
must be subexponential to be beaten by the exp-small count (Section 4). Both routes therefore land
on the identical pair of residual estimates.

## 4. The residual: critical-scale cluster negligibility (the only genuine gap)

Write the clustered two-point sum exactly. The pair probability factors as `p_2(D) = p_1^2 M(D)`
where, conditioning on the shared rows `A_S` (`S = T_i cap T_j`) and using that the two events are
conditionally INDEPENDENT given `A_S` (disjoint private rows), with conditional probabilities
`q(omega) = P{smin(A_T) <= tau | A_S = omega} = c(omega) tau^{d_F}(1+o(1))`,
```
  M(D) = EE[q^2]/(EE q)^2 = 1 + Var(q)/(EE q)^2 = 1 + CV^2(c) = EE[(1-|rho|^2)^{-d_F/2} | codim D].
```
`M(D)` is the conditional overlap moment and is SCALE-FREE (the `tau^{d_F}` cancels). Using the
Vandermonde identity `sum_D binom(m,D) binom(N-m,D) = binom(N,m)`, the clustered Chen-Stein term is
exactly
```
  b_2 = lambda^2 * EE_{Vand}[ M(D) ; 1 <= D < eps m ],
  P_Vand(D) = binom(m,D) binom(N-m,D) / binom(N,m)   (law of the codimension of a random pair).
```
NEED: `b_2 -> 0`, i.e. `EE_{Vand}[M(D); D < eps m] -> 0`.

Why `prop:small-D-negligible` does NOT transfer. `P_Vand(D)` concentrates at `Dbar = m(1-1/gamma)`
and is exponentially small on the clustered range: for `D = o(m)`,
`P_Vand(D) ~ (gamma-1)^D m^{2D}/(D!)^2 * e^{-h(gamma) m}`. So the clustered mass is `e^{-Theta(m)}`.
But the crude bound `M(D) <= p_1/p_1^2 = 1/p_1 = binom(N,m)/lambda = e^{+h(gamma) m}/lambda` is
ALSO exponential, and the two exponentials are of the SAME order `h(gamma) m`. At the bulk scale of
`prob:pc` the threshold sits below the critical line and this product carries a strictly negative
exponent (room to spend); at the CENTERED scale the room is gone, and the negligibility is a genuine
`e^{-Theta} x e^{+Theta}` cancellation that the bulk lemma never had to perform.

What actually saves it (and is the residual lemma). The crude `M(D) <= 1/p_1` is enormously lossy:
a clustered pair `T_i, T_j` with subset-codimension `D` does NOT force the NORMAL overlap `|rho| ->
1`. Indeed at `D = 1` (differ in one row) the two subsets share the `(m-1)`-set, so they share the
SAME normal `u_S` but use DISTINCT, independent test rows `a_p, a_q`; the events factorize and
`M(1) = O(1)`, not `1/p_1`. The singular `|rho| -> 1` regime needs the two normal-DEFINING sets to
nearly coincide, which is far more special than subset-codimension `D` being small. The required
statement is therefore a UNIFORM polynomial bound on the conditional overlap moment:
```
  (R2)   M(D) = EE[(1-|rho|^2)^{-d_F/2} | codim D]  <=  poly(m)   for ALL 1 <= D < eps m.
```
Given (R2), `b_2 <= lambda^2 * poly(m) * sum_{D<eps m} P_Vand(D) <= lambda^2 poly(m) e^{-c(eps)m}
-> 0`. (R2) is plausibly true and provable -- the small-`D` analysis is a finite-dimensional
shared-null-space computation, and the tail (T) already gives `M(D) <= O(1)` for `D >= 1 + d_F`,
leaving only the few smallest codimensions to bound by hand -- but it is NOT contained in `prob:pc`
(which only asserts `M(D) <= 1 + o(1)` on `D >= eps m`) and is NOT delivered by the resolvent
closure (an `eps m`-scale estimate). This is the precise residual at k=2.

The `k >= 3` increment (and why it is still not a brick wall). For sunflower/common-core clustered
tuples the enhancement is the higher conditional-density moment `EE[(det G_j)^{-d_F/2} | shared
core]` (`3 <= j <= k`), i.e. higher moments of the SAME random density `c(.)`. The required input is
the uniform subexponential bound
```
  (R3)   EE[(det G_j)^{-d_F/2} | clustered core] <= subexp(m)   for fixed 3 <= j <= k,
```
the `j`-fold analogue of (R2). On SPREAD cores it is `1 + o(1)` (Section 2, pairwise). On clustered
cores it is a JOINT near-degeneracy of `j` overlapping null vectors confined to one shared low-dim
space -- an object the PAIRWISE resolvent closure does not directly bound. However: (i) by AGG
(Section 3) Poisson convergence is reduced to `b_1, b_2, b_3`, none of which contains (R3), so (R3)
is needed only on the redundant factorial-moment route, not for the law itself; (ii) even on that
route, only a SUBEXPONENTIAL (not sharp) bound is needed, against an `e^{-Theta(m)}` count. So (R3)
is a strengthening of the local-law input, not a new impossibility.

## 5. Ledger: proved vs. open, and the precise residual

PROVED here (modulo the same off-support anisotropic local law as the k=2 keystone):
1. k-point local CLT (Section 1): joint slab probability `(1+o(1))(c_F t^{d_F})^k (det G_k)^{-d_F/2}`,
   by k-fold Fourier inversion -- the verbatim multivariate extension of `lem:two-proj`.
2. `det G_k` is pairwise-controlled for fixed `k` (Section 2, Gershgorin): no joint near-degeneracy
   without a large pairwise overlap; the naive product bound is false, the `lambda_min` bound holds.
3. The SPREAD main term `EE[(det G_k)^{-d_F/2}; spread] -> 1`, hence the spread tuples contribute
   `lambda^k`, using ONLY the keystone pairwise bound (all fixed-order pairwise negative moments are
   free because `D = Theta(m) -> infty`). So "higher-order asymptotic independence" is a corollary
   of the two-point statement, NOT a new k-point input.
4. Chen-Stein/AGG (Section 3): the full Poisson limit (all `k` at once) reduces to two-point/
   one-vs-field terms `b_1` (counting, `->0`), `b_2` (clustered pairs), `b_3` (spread decorrelation).
   No `k >= 3` tuple sum survives; the feared "k-tuple combinatorics" obstruction does not exist.

OPEN (the genuine residual, identified exactly):
- (R2) Critical-scale cluster negligibility, k=2: `M(D) = EE[(1-|rho|^2)^{-d_F/2} | codim D] <=
  poly(m)` UNIFORMLY for all `1 <= D < eps m`. This makes `b_2 = lambda^2 EE_Vand[M; D<eps m] ->0`.
  Already open BEYOND `prob:pc`: the bulk `prop:small-D-negligible` cannot be cited because at the
  centered scale `p_1 ~ binom(N,m)^{-1}` leaves no exponential room (the negligibility is a genuine
  `e^{-Theta(m)} x e^{+Theta(m)}` cancellation). The resolvent closure controls only `D >= eps m`.
- (b_3) Spread decorrelation: `EE|EE[I_alpha - p_1 | spread field]| -> 0`, the rigorous form of bulk
  asymptotic independence; expected to follow from the `det G_2 -> 1` weak-dependence (each spread
  neighbour perturbs the conditional law by `O(1/m)`), but must be written out as a field statement.
- (R3) Only on the redundant factorial-moment route: subexponential `EE[(det G_j)^{-d_F/2} |
  clustered core]` for `3 <= j <= k` (joint near-degeneracy of `j` overlapping null vectors). Not
  needed for the law via AGG; a strengthening, not an impossibility.

CLASSIFICATION: **partial**. The full Gumbel law does NOT hit a new k-point obstruction. For every
fixed `k` the k-point machinery reduces to (a) the SAME off-support local law that closes the k=2
keystone -- which already yields the main term `lambda^k` -- plus (b) ONE genuinely separate
two-point estimate, critical-scale cluster negligibility (R2) (with the spread-field decorrelation
`b_3`). The single load-bearing residual is (R2): a uniform `poly(m)` bound on the conditional
overlap moment `M(D)` across ALL codimensions, the centered-scale replacement for the bulk-scale
`prop:small-D-negligible`.

HONEST CAVEATS.
- The single-event-to-slab reduction (`smin <= tau` <-> nearest-row distance) costs `sqrt(m)`
  factors absorbed into `b_m`/the `log m` correction; the leading `det G_k` law is unaffected, but a
  fully rigorous account must track these polynomial conditioning factors (the same ones already
  implicit at k=2).
- (R2) is asserted plausible (the small-`D` normal overlap is not forced to 1; tail (T) already
  covers `D >= 1 + d_F`), not proved here; the smallest codimensions need a direct shared-null-space
  computation. This is the same FLAVOUR of estimate as the keystone but at a scale the keystone does
  not reach.
- Everything inherits the keystone's standing dependence on the anisotropic local law
  [KnowlesYin2017, BEKYY2014] for the off-support resolvent / `EE|rho|^2 = O(1/D)` input; `prob:pc`'s
  call for a self-contained proof applies a fortiori here.
- All `det G_k` collapse arguments use `k` FIXED. They are uniform only on `k = O(1)`; a `k`-uniform
  (e.g. `k` growing) statement would re-expose the joint-degeneracy question and is out of scope.

