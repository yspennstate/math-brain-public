# The single-edge slack is one-dimensional: layer factorization, pivotal containment, and the two inputs the noise route still needs

Date: 2026-08-22, lane P1 (30-hour campaign resume)  
Status: dependency verification of the 08-16 single-edge arc completed (verdicts below);
three new elementary lemmas proved in full; one route classification derived and labeled as
a route map, not a theorem. chi = 1/3 UNMOVED.

Companions (bytes pinned; each SHA recomputed today and matched against the SHAs its
consumers printed on 08-16):

* `SINGLE_EDGE_TARGET_MASS_DIRECT_20260816.md`, SHA-256
  `4eea505ef965591bf4c06eb03f5915111e745725d7f4423ca26d593d4e39b923`
* `SINGLE_EDGE_TARGET_MASS_SHARP_MONOTONE_20260816.md`, SHA-256
  `7b3039d5d74283d582bc996333bba27da81bb7569104c592088c06f91f14e68c`
* `SINGLE_EDGE_OUTSIDE_UNCERTAINTY_20260816.md`, SHA-256
  `4118c45e48cf41d68779e27e4177f21f876c6b78f265a3efbba9ffb70c866658`
* `SINGLE_EDGE_JOINT_SHARP_20260816.md`, SHA-256
  `19fb35ca94b5a8559e3cfaafc58a6d78562ff8b517ca75f299516694dca1cbca`
* `SINGLE_EDGE_WEIGHTED_ENGINE_20260816.md`, SHA-256
  `006e1baea140b92672cae7336f174283162560464e37b0cddd11e436e88503d0`
* `SINGLE_EDGE_ENGINE_OPTIMIZED_20260816.md`, SHA-256
  `fa030877868e752582eb5d9733a7650d61f9d7f104856fcb2ee459fe961ad77f`
* `DISTINGUISHED_BLOCK_SPECTRAL_SPLIT_20260816.md`, SHA-256
  `f18916f69b7fbd24c96325ae3da9c046ba31152a893ca736fb11de737e083f0f`
* `BLOCK_INCREMENT_NOISE_SPLIT_20260816.md`, SHA-256
  `c106b719e76e584157c36a840a55fbb3c68571e0b4386ff509bec699366f0de0`
  `1d912a8123f49b831d91bd83b85d1514707e75be2053e82926c9a4108d44e293`

## 0. Dead routes this note does not retread

These are the campaign's scars, listed so nobody reads what follows as re-opening them.

1. Variance MONOTONICITY: removed as a target 2026-08-15 (`fpp_monotonicity_has_no_consumer`).
   It buys nothing; its telescoped "doubling at most scales" consequence is equivalent to the
   linear bound. Not worked here.
2. Constant-A variance DOUBLING: wall-equivalent (fire 89, `DOUBLING_IS_NOT_A_SIDE_DOOR`), and
   the certifiable constant is `A ~ n/log n`. Not a side door; not used as a hypothesis here.
3. The continuity/open-closed bootstrap: closed 08-15 (its base case IS constant-A doubling).
   Not re-opened.
4. rho = Q^2/D as "the wall": retired by CRUX 9.3; the ledger is (L1') = the wall, (L2') =
   scale-free shape, (L3) = one power of n. This note works strictly BELOW the wall: it
   sharpens the campaign's understanding of the single-edge spectral ledger's open inputs.
5. (L2') support from kappa4 ~ 3: deflated 08-15 (the statistic cannot resolve FPP shape from
   summed uniforms at laptop block sizes). No kurtosis measurement is used here.
6. Laptop measurement of Efron-Stein granularity: closed 08-16 (no signal at reachable sizes).
   No such simulation is run here; the only numerics below are seconds-scale falsifiers of
   exact identities, and they are labeled as sanity checks, not evidence.
7. The ESCAPE retraction is unconditional and the sandwich surviving core stands (fires
   77-81). Nothing here touches it.

## 1. Target chosen and why

The newest fire on file (`SINGLE_EDGE_ENGINE_OPTIMIZED_20260816.md`, 08-16 09:32) closes with
a referee request naming its own load-bearing steps, and its section 5 names the remaining
probabilistic problem: route uncertainty `R = sum_e r_e` is not forced below path-length
scale, and the variance-weighted outside revealment `B = D_z` has no construction.
the exact pivotal containment for `g_{L,s}` under one outside-coordinate switch and run the
squared-influence sum with the point-to-point geometry."

This fire does both things that are actually completable in one unit:

* Part I: the owed dependency verification of the single-edge arc (the five one-dimensional
  notes plus the optimization note), every load-bearing step re-derived independently.
* Part II: the decisive check, executed at single-edge granularity, where the threshold
  structure makes it exactly derivable. The layer events of the positive increment factor
  through a scalar "slack" variable; its pivotal containment is proved; and the containment
  shows exactly which estimates the noise route still needs, the principal one being the
  campaign's Thread B (restricted-min anticoncentration) in quantitative form.

Division of labor: mesh lane P3 is the adversarial referee for unrefereed fires. Part I here
is the narrower thing a lane must do anyway - verify what it consumes - performed by
independent re-derivation. It does not discharge the campaign's convention of a hostile
referee pass; P3's pass is still owed and is not preempted.

## 2. Part I: dependency verification of the 08-16 single-edge arc

Method: every displayed identity and inequality in the chain was re-derived by hand today,
independently of the notes' prose, and the polynomial/kernel identities were additionally
checked by exact rational arithmetic and by random decreasing-threshold numerics
(18 checks, all passing, ~30s total; script filed at
`12_cognitive_architecture/brain_improvement/campaign_2026-08-22_30h/lanes/P1_primary/p1_checks.py`;
numerics are falsifiers, not proof).

VERDICT TABLE (notation of the respective notes):

1. TARGET_MASS_DIRECT (8)-(13): VERIFIED. The pointwise identity
   `z_e = 1_{w'>w} int_w^{w'} 1_{t<T_e} dt`, the kernel
   `E[m_e^2] = iint q(s)q(t) F(min)(1-F(max))`, and `C_edge+P_edge = sum_e E[m_e^2]` are all
   correct; the `1/4` kernel bound is the trivial one it claims to be.
2. TARGET_MASS_SHARP_MONOTONE, Lemma (9): VERIFIED, including the two steps its referee
   request names. The mixture representation (11) is the Stieltjes layer cake
   `mu(da) = a(-dh(a)) + h(1) delta_1(da)`; total mass 1 follows from `int h = 1`; (12),
   the Jensen step, `int_0^a (1-t/a)^2 dt = a/3`, and the final maximization
   `(2/3)A - A^2 <= 1/9` at `A = 1/3` are all correct; equality at `f = c 1_[0,2/3]`
   confirmed exactly (ratio `1/9` at `c = 2/3` by rational arithmetic).
3. OUTSIDE_UNCERTAINTY (4)-(16): VERIFIED. The exact outside-variance kernel (7) was
   re-derived by a second, independent route (section 4 below) and agrees. The closed form
   (14) `2A(x,x+d)/d = dx(1-x) + (d^2/3)(1-3x) - d^3/4` was checked by exact rational
   arithmetic at 40 random rational points; the concave-in-x maximization at `x=(1-d)/2`,
   the reduction to `d/4 - d^2/6`, the maximum `3/32` at `d = 3/4`, and the equality law
   `Tau in {1/8, 7/8}` are all correct.
4. JOINT_SHARP (9)-(21): VERIFIED. The averaging reduction to the two-point inequality (10),
   the identity `g = t^2/9 - phi/36`, the split at `d = 64/81`, the closed form
   `64/729 - g(d)/d = (9d-8)^2(9d+4)/2916`, and the two sharpness constructions are all
   correct (identities re-checked in exact rational arithmetic; (10) also on a 900x900 grid,
   max violation 0). The Pareto reading is stated correctly (pair-sharpness, not joint
   attainability by one law).
5. WEIGHTED_ENGINE Lemma (6) and (13)-(20): VERIFIED as displayed, INCLUDING the three steps
   its referee request names: the decomposition (7) needs exactly `lambda >= mu >= 0`; the
   order (17) is `mu = kappa + (1-kappa)^r <= 1 + kappa = lambda`, which holds with no
   asymptotic choice of `r`; the passage (18) to (20) uses only positivity and the relaxation
   of `P_z`'s coefficient from 1 to `1+kappa`, which is stated in its break check 3.
   SCOPE CAVEAT carried forward: (18) itself is the distinguished-block engine inequality,
   which is NOT verified here (see item 8).
6. ENGINE_OPTIMIZED (7)-(24): VERIFIED. (7)-(12): the minimizer `kappa_r = 1 - r^{-1/(r-1)}`,
   the bounds `(log r)/(2(r-1)) <= kappa_r <= (log r)/(r-1)` (which need
   `x = log r/(r-1) <= 1`, true for every integer `r >= 2`), `mu_r^* <= (1+log r)/r`, and
   `1+kappa_r <= 3/2` are all correct. (14)-(16): re-derived by hand
   (`F_r'(kappa) = (T+A) - Ar(1-kappa)^{r-1}` is nonnegative everywhere iff `Ar <= T+A`,
   and at the interior critical point `Aq^r = (T+A)q/r` collapses `F_r` to (15)); also
   confirmed against direct minimization (200 random instances, 2000-point grids).
   (17)-(23): correct, including `kappa_r <= mu_r^*` (immediate from
   `mu_r^* = kappa_r + (1-kappa_r)^r`). The constant 4 in (22) holds numerically with margin
   already from `S/B = 10` (worst ratio observed 0.34 over `S/B in [1e1, 1e20]`).
7. ENGINE_OPTIMIZED (25), lower bound: VERIFIED WITH A SUPPLIED ARGUMENT. The note's one-line
   sketch ("splitting at r of order ((A/B) log(A/B))^{1/3}") is right but incomplete as
   stated, because on the small-r branch `log r` can be of order 1 while the naive bound
   only reaches `Phi/L`. The complete argument: let `L = log(A/B)`,
   `Phi = A^{2/3}B^{1/3}L^{2/3}`, `rho = A/Phi = (A/B)^{1/3}L^{-2/3}`. For any integer
   `r >= 2`, `A mu_r^* + c_r B >= A log r/(2r) + r^2 B/4`. If `A log r/(2r) >= Phi/8`, done.
   Otherwise `r/log r > 4 rho`; for `A/B` large, `rho >= 1`, which excludes `r = 2`
   (`2/log 2 < 4`), so `r >= 3`, `log r > 1`, hence `r > r/log r > 4 rho` and
   `log r > log(4 rho)`, giving `r > 4 rho log(4 rho)`; then
   `r^2 B/4 >= 4 rho^2 log^2(4 rho) B = 4 (Phi/L^2) log^2(4 rho) >= Phi/9`
   using `log(4 rho) >= L/6` for `L >= 12`. So the infimum is `>= Phi/9` for `A/B >= e^12`,
   which is the claimed asymptotic order.
8. NOT VERIFIED HERE (open referee debt, P3's lane): the distinguished-coordinate level
   estimate and noise bound (DISTINGUISHED_BLOCK (5), (8), hence (14)); the stop-early engine
   inequality `Var <= kappa A_2^+ + S_z(t)` (BLOCK_INCREMENT (5), which rests on MG2B 8.1 -
   ledger item 1 is referee-verified for the published form, not for the stop-early variant -
   (BLOCK_INCREMENT (13), (16), (17)). Everything in Part II below that feeds these steps is
   therefore conditional on them and is labeled so.

Net: no errors found in the five one-dimensional notes or the optimization note. One
incomplete proof sketch (item 7) received a complete argument. The arithmetic checks in the
notes' own break-check sections all reproduce.

## 3. Setting and pinned facts

Standing hypotheses of the single-edge arc: `Z^d`, `d >= 2` (campaign target `d = 2`), iid
edge weights with density `rho` on `[a,b] subset (0,infinity)`, `rho >= alpha > 0` a.e.;
endpoints `0, v`; `X = T(0,v)`; a.s.-unique geodesic `gamma`.

Pinned single-edge structure (from SINGLE_EDGE_GAP_COLLISION section 1, re-verified): for an
edge `e`, with `B_e` = min over through-`e` paths of (cost `- w_e`) and `C_e` = min over
avoiding paths, both outside-measurable,

`X = B_e + min(w_e, T_e),      T_e := C_e - B_e <= 3b,      {e in gamma} = {w_e < T_e}` a.s.

Call `T_e` the SLACK of `e`. Let `w_e'` be the independent replacement, `X^e` the replaced
passage time, `z_e = (X^e - X)^+`, `Y_e = (w_e, w_e')`.

## 4. Lemma A: the increment is an exact minimum, and its layers factor

**Lemma A** (complete proof). Pointwise on the full-measure set where the pinned identities
hold,

`z_e = min( (w_e' - w_e)^+ , (T_e - w_e)^+ ).`

Proof. `X^e - X = min(w_e', T_e) - min(w_e, T_e)` with the SAME outside-measurable `T_e`,
because `B_e, C_e` do not read `w_e`. If `w_e' <= w_e` the difference is `<= 0` and both
sides vanish. If `w_e' > w_e`: for `T_e <= w_e` the difference is 0 and `(T_e - w_e)^+ = 0`;
for `w_e < T_e <= w_e'` it is `T_e - w_e = min(w_e' - w_e, T_e - w_e)`; for `T_e > w_e'` it
is `w_e' - w_e = min(w_e' - w_e, T_e - w_e)`. QED

This is one integration away from TARGET_MASS_DIRECT (8) and is claimed as new only as a
STATED identity; it is elementary in kind.

**Corollary A1** (layer factorization). For every `s >= 0`,

`{z_e > s} = {w_e' - w_e > s} intersect {T_e - w_e > s}.`

Proof. `min(A,B) > s` iff both exceed `s`; `(x)^+ > s` iff `x > s` for `s >= 0`. QED

So at single-edge granularity the layer event `g_{e,s} = 1_{z_e > s}` of
FPP_THRESHOLD section 3 FACTORS as an `Y_e`-measurable rectangle times ONE outside threshold
event `{T_e > u}` at the level `u = w_e + s`. The block-level obstruction ("the passage time
is not a one-dimensional threshold in the full block vector") is absent at this granularity.

**Corollary A2** (Lipschitz form). For fixed `Y_e`, the map `T -> min((w_e'-w_e)^+, (T-w_e)^+)`
is nondecreasing and 1-Lipschitz. Immediate.

**Corollary A3** (exact conditional reduction; audit cross-check). Conditionally on
`Y_e = (w, w')`, `z_e = int_0^{(w'-w)^+} 1_{T_e > w+s} ds`, so for every sigma-field or noise
operator on the outside environment, conditional means, variances, and noise covariances of
`z_e` are the corresponding `ds ds'` integrals for the indicator family `{T_e > u}`,
`u in [w, max(w,w')]`. In particular

`Var(z_e | Y_e) = iint_{[0,(w'-w)^+]^2} [ q_e(w + max(s,s')) - q_e(w+s) q_e(w+s') ] ds ds',`

and averaging over the iid pair reproduces OUTSIDE_UNCERTAINTY (4)-(6) exactly (substitute
`sigma = w+s, tau = w+s'`; the pair constraint becomes `w < min, w' > max`, giving the
`F(min)(1-F(max))` kernel). This is the second derivation used in the audit above.

## 5. Lemma B: slack pivotality is contained in a window and a membership event

**Lemma B** (complete proof). Fix `e`, an outside edge `f != e`, and all weights except
`w_f = x`.

(i) On `[a,b]`, `C_e(x) = min(k_0, k_1 + x)` and `B_e(x) = min(m_0, m_1 + x)` with constants
(possibly `+infinity`) not depending on `x`: both are nondecreasing, concave, 1-Lipschitz.

(ii) `T_e = C_e - B_e` is 1-Lipschitz in `x`: `|T_e(x) - T_e(x')| <= |x - x'|`.

(iii) If `1_{T_e(x) > u} != 1_{T_e(x') > u}` then

  (a) `|T_e(x) - u| <= |x - x'|` and `|T_e(x') - u| <= |x - x'|`; and

  (b) `f` lies on the best avoiding-`e` path or on the best through-`e` path in the
      environment with `w_f = min(x, x')`.

Proof. (i): partition the (finitely many, simple) competing paths by whether they use `f`; a
simple path uses `f` at most once, so the `f`-using family has cost `constant + x` and the
`f`-avoiding family constant cost. (ii): for `x < x'`, `C_e(x') - C_e(x)` and
`B_e(x') - B_e(x)` both lie in `[0, x'-x]`, so their difference lies in `[-(x'-x), x'-x]`.
(iii)(a): the flip puts `T_e(x)` and `T_e(x')` on opposite sides of `u`; with (ii), both are
within `|x - x'|` of `u`. (iii)(b): the flip forces `C_e(x) != C_e(x')` or
`B_e(x) != B_e(x')`. Say `C_e` changed and `x < x'`: `min(k_0, k_1+x) != min(k_0, k_1+x')`
requires `k_1 + x < k_0`, i.e. at `w_f = x` some minimizing avoiding-`e` path uses `f`.
Same for `B_e`. QED

**Corollary B1** (resampling influence of the slack indicator). With `(w_f, w_f')` iid and
exchangeable, for every `u`:

`Inf_f(1_{T_e > u})
 <= 2 E[ 1_{f in gamma_{C_e} union gamma_{B_e}} 1_{|T_e - u| <= |w_f' - w_f|} ]
 <= 2 P( f in gamma_{C_e} union gamma_{B_e}, |T_e - u| <= b-a ),`

where `gamma_{C_e}, gamma_{B_e}` are the avoiding/through restricted geodesics in the
ORIGINAL environment. Proof: the flip event is symmetric in the pair, so restrict to
`{w_f < w_f'}` and double; on that event the "smaller value" environment of Lemma B(iii) is
the original one. QED

## 6. Lemma C: transcript precision converts to residual variance

BLOCK_INCREMENT (15)-(17) prices an approximate decision transcript by its residual variance
`e_L = E[Var(z_L | T_L)]`. At edge granularity this residual has an exact handle:

**Lemma C** (complete proof). Let a transcript `T` (adaptive queries of outside coordinates;
private randomness independent) admit a `T`-measurable estimator `hat T` with
`|hat T - T_e| <= delta` a.s. Then

`e_e := E[ Var(z_e | T, Y_e) ] <= min( delta^2 , E[Var(z_e | Y_e)] ).`

Proof. Given `(T, Y_e)`, `z_e = psi(T_e)` with `psi` the 1-Lipschitz map of Corollary A2,
and `hat z := psi(hat T)` is `(T, Y_e)`-measurable; conditional variance is at most the
conditional mean square deviation from any measurable point:
`Var(z_e | T, Y_e) <= E[(psi(T_e) - psi(hat T))^2 | T, Y_e] <= delta^2`. The second bound is
the tower property (conditioning on more never raises expected conditional variance). QED

Reading: the missing "conditional decision algorithms" of the weighted engine need, at edge
granularity, to pin the SLACK to additive precision `delta_e` on exactly those edges whose
outside variance exceeds `delta_e^2`, at low revealment away from a bounded exceptional
neighborhood of `e` (the near-`e` coordinates are compulsory and must go into the
exceptional set of DISTINGUISHED_BLOCK section 1, whose price is its pure-exceptional mass).
Determining `z_e` EXACTLY means resolving the restricted-geodesic comparison to zero error
whenever `T_e in (w_e, w_e')`, which is the exploration obstruction Ahlberg-Hillairet-
Toropova warn about. Lemma C is what "truncated exploration" must prove instead.
steps - audit item 8.]

## 7. What the containment buys, and what it cannot


(1) PROVED ANCHOR (window width vs support). In Corollary B1 the window width is
`|w_f' - w_f| <= b - a`, the FULL support length, while the probed levels `u = w_e + s` lie
in `[a, b]`. For every probed `u`, `u - (b-a) <= a` and `u + (b-a) >= b`, so the
constant-width window `[u - (b-a), u + (b-a)]` CONTAINS the entire weight support `[a, b]`:
`{T_e in [a,b]} subseteq W_u` for every probed level. So at FULL resampling the window
factor does not constrain: all smallness must come either from the membership factor
`P(f in gamma_{C_e} union gamma_{B_e})` or from the fine structure of SMALL `|w_f' - w_f|`
windows - that is, from quantitative anticoncentration of the slack `T_e` at scales
`delta << b - a`, jointly with membership:

`(I1')   sum_f ( E[ 1_{f in gamma_{C_e} union gamma_{B_e}} 1_{|T_e - u| <= |w_f' - w_f|} ] )^2`
        small at the ledger's scale, for the probed `u`.

The `f`-free special case of the inner event is exactly restricted-min gap anticoncentration
- the campaign's Thread B, in quantitative, summed form. At edge granularity the
it. (Same shape as fire 89's verdict on doubling.)

(2) PROVED ANCHOR (the mechanism cannot come from the slack's spread). Dembin-Elboim's
crossing-time argument gets its vanishing factor because their pivotal window (also of
support width) sits inside a variable whose spread DIVERGES (the crossing time; small ball
`~ 1/sqrt(log n)` per unit window). The slack satisfies `T_e <= 3b` deterministically
(plaquette detour), and the probed windows sit inside an `O(b)`-length range: the
window-to-spread ratio is order one, permanently. Concretely, for endpoint edges the window
mass provably does not vanish: a simple pigeonhole witness -

**Proposition D** (complete proof). For every `n` there exist an edge `e*` incident to `0`
and a level `u_0 in (a, 3b]` with

`P( |T_{e*} - u_0| <= b-a ) >= 1/(2d) * 1/ceil((3b-a)/(b-a)) > 0,`

uniformly in `n` and `v`. Proof. The geodesic, a simple path from `0`, uses exactly one
edge incident to `0`, so `sum_{e ni 0} p_e = 1` and some incident `e*` has
`p_{e*} >= 1/(2d)`. Since `q_{e*}(w) = P(T_{e*} > w) <= P(T_{e*} > a)` for every `w >= a`,
`P(T_{e*} > a) >= E[q_{e*}(w_{e*})] = p_{e*} >= 1/(2d)`; also `T_{e*} <= 3b` always
(plaquette detour). Partition `(a, 3b]` into
`ceil((3b-a)/(b-a))` intervals of length `<= b-a`; one carries mass `>= 1/(2d ceil(...))`;
take `u_0` its midpoint. QED

Endpoint edges are already marked exceptional in DISTINGUISHED_BLOCK section 5; Proposition
D says the containment route CANNOT rehabilitate them - they must be paid for through the
exceptional set, not through decay.

(3) THE TWO OPEN INPUTS, named. Beyond (I1'), running the squared-influence sum needs

`(I2)` influence/delocalization control for RESTRICTED geodesics (the graph with `e`
deleted, and the best through-`e` path). Dembin-Elboim-Peled Corollary 1.3 is stated for the
plausible but is NOT on file and is not claimed here.

`(I3)` for the exceptional-set route: with `E_e` a radius-1 ball of pair coordinates around
`e`, write `W_nbr` for the OLD weights of the ball's edges other than `e` itself (the
replacement half of those pairs never enters `z_e`, and `w_e` stays integrated). Given
`W_nbr`, the conditional survival `q^{nbr}(t) = P(T_e > t | W_nbr)` is still decreasing, so
the sharp monotone kernel lemma applies conditionally and, after taking expectations,

`(E z_e)^2 + Var(E[z_e | Y_{E_e}]) <= (1/(9 alpha^2)) E[ P(e in gamma | W_nbr)^2 ].`

So the new obligation is the NEIGHBOR-CONDITIONED squared influence sum
`sum_e E[P(e in gamma | W_nbr)^2]` at `n^{2/3+o(1)}` - a two-replica statement (two
environments sharing only the ball around `e` both route through `e`) that is strictly more
local than block chaos. Open; named here so it stops being assumed.

(4) HONEST LIMIT OF THE CLASSIFICATION. (1)-(2) close the containment-based DE template at
per-coordinate pivotal containment altogether (a direct spectral/hypercontractive argument
on pair-block noise, or the anti-symmetric in-block Mermin-Wagner perturbation mused in
FPP_THRESHOLD section 2). Necessity is claimed only route-level.

## 8. Standing

* PROVED HERE: Lemmas A, A1-A3, B, B1, C; Proposition D; the supplied lower-bound argument
  for ENGINE_OPTIMIZED (25); the verification verdicts of section 2.
* ROUTE MAP, NOT THEOREMS: section 7 (1)-(3) as classification; the necessity of Thread B is
* CONDITIONAL: anything feeding Lemma C into the block criterion inherits the unverified
  spectral steps (audit item 8).
* chi = 1/3 UNMOVED. No variance bound is improved by this note. The wall ledger
  ((L1') wall, (L2') shape, (L3) one power) is unchanged.

## 9. Break checks

1. Falsifier for Lemma A/A1 and the pinned identity `X = min(B_e + w_e, C_e)`: exact
   Dijkstra on a 5x5 lattice, 150 random environments, random edge, random replacement,
   random layer level: zero violations at 1e-9 tolerance. Falsifier for Lemma B(ii): 11-point
   sweeps of one outside weight, increments never exceed the weight increment. (Seconds-scale
   sanity numerics; not proof; no simulation sweeps run.)
2. Lemma B(iii)(b) needs SOME minimizing path, not uniqueness; at ties (a null set) the
   statement is read a.s.
3. Proposition D uses only simplicity of the geodesic at `0` and `T_e <= 3b`; it makes no
   claim that `u_0` is probed by the layer family of `e*` (probed levels lie in `[a,b]`;
   `u_0` may sit above `b`). Its role is strictly to witness non-decay of the window factor
   over the threshold family.
4. The claim "the window spans the support" in 7(1) is the two inequalities
   `u - (b-a) <= a`, `u + (b-a) >= b` for `u in [a,b]`; it is NOT a claim that
   `P(W_u) = Theta(1)` for bulk edges - for bulk edges `P(W_u)` is a near-usability
   probability and may well be small; the point is that the containment gives no decay
   MECHANISM there beyond membership itself.
5. Everything consumed from the 08-16 arc was verified in section 2 except the spectral
   steps listed in audit item 8, which nothing in sections 4-6 uses.

## 10. Honesty block

THE SINGLE HARDEST OPEN STEP of the direction this note maps: proving any nontrivial case of
(I1') - anticoncentration of the slack `T_e` at scales below the support length, jointly
with restricted-geodesic membership, summed over `f`. Nothing here proves any instance of
it; it is Thread B territory, and Thread B is exactly where the sandwich referee located the
renormalization-shaped difficulty.

STRONGEST CASE THAT THE MAIN CLAIM IS WRONG: the route classification (7) would be wrong as
containment - most plausibly the anti-symmetric perturbation route: perturb the original and
replacement copies of the target pair in OPPOSITE directions inside a Mermin-Wagner scheme,
so the window variable becomes a coupled DIFFERENCE whose spread might be made to diverge
with the annulus count, unlike `T_e`.

THE ONE CONCRETE CHECK THAT WOULD CONFIRM IT: carry out Elboim's annulus perturbation
computation for the pair observable `(X, X^e)` with an anti-symmetric tilt confined to the
pair coordinate, and compute whether the accumulated drift acts on `X^e - X` (it must NOT
cancel) with a product-cost still summable over annuli. If that calculation produces a
diverging-spread window variable for the difference, section 7(2)'s mechanism argument no
longer binds, and the classification must be retracted in place.
