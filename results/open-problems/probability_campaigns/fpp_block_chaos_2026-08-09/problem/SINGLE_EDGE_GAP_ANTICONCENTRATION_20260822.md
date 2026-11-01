# Thread B at single-coordinate granularity: the restricted-min gap inherits the weight law's own anticoncentration, and (I1') reduces to (I2)

Date: 2026-08-22, lane P7_threadB (30-hour campaign).
Mission: prove or refute a usable anticoncentration statement for the restricted-min gaps
(the `G_L = C - A` variables of the 08-15 decomposition; single-edge form `g_e = (T_e - w_e)^+`
of `SINGLE_EDGE_GAP_COLLISION` (7)) at the two certified consumption interfaces (P1's (I1'),
P2's remark 5.2).
(I1') to the pure membership-collision sum (I2); two block-level corollaries with their
degradation constants displayed; interface disposition for both certified lanes; falsifier
23/23. chi = 1/3 UNMOVED. No variance bound is improved by this note.
This is the canonical problem-dir copy (filed under mesh claims clm-19e0b50684 /
clm-8bf2f68952); the lane copy is
`12_cognitive_architecture/brain_improvement/campaign_2026-08-22_30h/lanes/P7_threadB/P7_FIRE_20260822.md`.

Falsifier: `12_cognitive_architecture/brain_improvement/campaign_2026-08-22_30h/lanes/P7_threadB/p7_checks.py`
(23 checks, all passing, ~40s, BelowNormal;
exact 184-path enumeration on the 4x4-vertex lattice as primary instrument, so `B_e, C_e,
T_e, G_L` are exact per sample; 7x7 Dijkstra secondary; two negative controls verify that
the load-bearing hypotheses can actually fail - the atomic law breaks the linear rate, and
a strict-subset block shift breaks Proposition 5's speed-1 flow on 78 percent of
environments).

## 0. Scars (checked before starting; nothing below re-opens them)

From `brain.py recall` ("FPP refuted routes chi variance", "FPP Thread B restricted min gap")
plus P1's list and the referee's fire-89 qualifier:

1. (L1') variance-ratio wall: the induction does not start; two-sided sandwich reduces it to a
   per-scale lower-leg contraction rho_L, open (`fpp_two_sided_wall_bootstrap_reclassification`).
   Not touched.
2. Doubling is wall-equivalent - INHERITED IN THE REFEREE'S QUALIFIED FORM (P3 fire-89 verdict:
   the printed window mechanism has two defects; the surviving statement is "doubling delivers
   the ratio core at 9.8's typical/sum-carrying blocks"; the near-band direction and M-to-2
   descent are open). Not consumed here at all.
3. Monotonicity has no consumer (08-15). Not worked.
4. rho = Q^2/D retired by CRUX 9.3; ledger is (L1') wall / (L2') shape / (L3) one power.
   This note works strictly below the wall.
5. (L2') kurtosis measurements cannot resolve FPP shape at laptop block sizes; no kurtosis
   is used here. The only numerics are seconds-scale falsifiers of exact statements.
6. The D-note's self-similar anticoncentration wall (anchored methods penetrate one layer;
   minima over polynomially many attachments reproduce the problem). NOT breached below -
   section 6 states exactly where it still stands and what price my block bounds pay to it.
7. Elboim 2406.10971 localizes to ANCHORED restricted times only; free-endpoint minima do not
   inherit it. Nothing below claims a free-endpoint Mermin-Wagner.
8. Off-U negative increments are real (CRUX D1): the support identity "Delta = 0 off U_L" is
   false. Nothing below uses resampling support.
   below is displayed at the point of use; (H2) is flagged as NEW relative to the arc's
   standing set.

## 1. The two consumption interfaces, stated exactly

**(IF-1) P1's (I1')** (SINGLE_EDGE_SLACK_PIVOTAL section 7(1), referee-confirmed as route map):
for the probed levels - WHICH ARE u = w_e + s BY P1'S OWN LAYER FAMILY (their Lemma A1:
`{z_e > s} = {w_e' - w_e > s} cap {T_e - w_e > s}`, so the threshold family rides on the edge's
own weight) - the noise route needs

    sum_f ( E[ 1_{f in gamma_{C_e} cup gamma_{B_e}} 1_{|T_e - u| <= |w_f' - w_f|} ] )^2

small at the ledger's scale, uniformly in the layer s and integrably for FPP_THRESHOLD (9)
(whose target is written in the increment layers `g_{L,s} = 1_{(X^L - X)^+ > s}` - checked
against the note's own display; the alternative absolute-level representation `h_{L,u} =
1_{X <= u < X^L}` of its (7) is a DIFFERENT family and is not what (9) consumes).
Anticoncentration content: joint (membership x window) smallness at scales delta << b - a.

**(IF-2) P2's remark 5.2** (referee-confirmed): `Cov(T_n, w_e) = E[Psi(c_e)]` - the entire
first-chaos mass is `sum_e E[Psi(c_e)]^2 / sigma^2`, a functional of the pivotal-cap law
(`c_e` = P2's name for the same `T_e`). Consumption analysis (section 5 below): the certified
floor consumes cap-mass LOWER bounds (their (C1) + Lemma 3, certified) plus a corridor
(open, I8-cognate); an anticoncentration UPPER bound is not what that chain is missing.
The weaker Thread-B requirement between the two interfaces is therefore the single-scale,
near-zero form (near-pivotal thinness), and it is proved first (Corollary 2); the full
layer-uniform form for IF-1 follows from the same one-line mechanism (Theorem 3).

## 2. Setting and pinned inputs

`Z^d`, `d >= 2` (campaign `d = 2`); iid edge weights `w` with law `F` on `[a,b] subset
(0, infinity)`; endpoints `0, v = n e_1`. Hypothesis ladder, displayed per claim:

* (H0) iid only - any law.
* (H1) `F` atomless.
* (H2) `F` has a density `rho` with `ess sup rho =: beta < infinity`. NEW relative to the
  arc's standing set (which assumes `rho >= alpha > 0`; the lower bound `alpha` is used
  NOWHERE in this note; U[1,2] has `beta = 1`).

Write `Q_w(lambda) := sup_x P(w in [x, x + lambda])` for the weight's own concentration
function. Pinned inputs, all referee-confirmed in P3's 08-22 pass:

* (P-i) `B_e, C_e` outside-measurable; `X = min(w_e + B_e, C_e)`; `T_e := C_e - B_e <= 3b`
  [GAP_COLLISION (4), (5), (8)].
* (P-ii) under (H1), `{e in gamma} = {w_e < T_e}` a.s. and the single-edge gap is
  `g_e = (T_e - w_e)^+` [GAP_COLLISION (6), (7)].
* (P-iii) `T_e` is 1-Lipschitz in every outside weight; if a level indicator `1_{T_e > u}`
  flips when `w_f` is replaced by `w_f''`, then `|T_e - u| <= |w_f - w_f''|` on both sides and
  `f` lies on `gamma_{C_e} cup gamma_{B_e}` in the environment with `w_f = min(w_f, w_f'')`
  [P1 Lemma B, Corollary B1].
* (P-iv) layer factorization `{z_e > s} = {w_e' - w_e > s} cap {T_e - w_e > s}` [P1 Lemma A1].
* (P-v) block decomposition: `X = min(A, C)` with `C` resample-invariant; on `U_L`,
  `G_L := C - A >= 0` caps `(Delta_L)^+` [POSITIVE_PART section 1].

**Definition.** The SIGNED single-edge gap is `gt_e := T_e - w_e`. So `g_e = (gt_e)^+`, and
under (H1), `{e in gamma} = {gt_e > 0}` a.s. By (P-iv) the engine's increment-layer family
probes exactly the levels of `gt_e`.

## 3. Theorem 1: the gap inherits the weight's own anticoncentration [COMPLETE PROOF]

**Theorem 1.** Under (H0) - iid only, any law - for every `n`, every edge `e`, and every
interval `I`:

    P( gt_e in I ) <= Q_w(|I|).

More is true: conditionally on the outside field `F_e^out := sigma(w_f : f != e)`, the law of
`gt_e` is EXACTLY the reflection of the weight law about the (outside-measurable) point `T_e`:

    P( gt_e in A | F_e^out ) = P_w( T_e - A ),        A Borel,

so under (H2) additionally `P(gt_e in A | F_e^out) <= beta Leb(A)`, hence unconditionally

    sup_s P( gt_e in [s, s + delta] ) <= min( Q_w(delta), beta delta ),

uniformly in `n`, `e`, and the level `s`.

*Proof.* `T_e` is `F_e^out`-measurable by (P-i), and `w_e` is independent of `F_e^out`.
Conditionally on `F_e^out`, `gt_e = T_e - w_e` with `T_e` a constant, so its conditional law
is the stated reflection, and `P(gt_e in I | F_e^out) = P(w_e in T_e - I) <= Q_w(|I|)`.
Integrate. QED.

Three readings, each load-bearing:

* (a) Under (H1): `Q_w(delta) -> 0` as `delta -> 0` (uniform continuity of an atomless cdf on
  a compact support), so the gap has uniform-in-`(n, e, s)` anticoncentration at the weight's
  OWN modulus. No density needed.
* (b) Under (H2): linear rate `beta delta`. This is the quantitative form the interfaces eat.
  (falsifier: two-point law, interval mass 0.1146 <= Q_w = 1/2) while no linear rate exists
  (the atom mass 0.1146 is constant as the interval length goes 1.0 -> 0.02): (H2) is

Sharpness: conditionally the bound is achieved whenever `T_e - I` sits where the density is
maximal, and it is order-attained already on the falsifier lattice: at an endpoint edge with
U[1,2], `P(0 < gt_e <= delta)/delta = 0.672, 0.668, 0.658` at `delta = 0.05, 0.1, 0.2`
(`beta = 1`). The constant cannot be improved beyond an absolute factor. [numerical,
falsifier]

**Remark 1.1 (the slack law itself is atomless).** Under (H1) with `F` absolutely continuous,
the law of `T_e` is absolutely continuous. Proof: `B_e` is a min over through paths `rho` of
`S_rho^{-e} := sum_{g in rho, g != e} w_g` and `C_e` a min over avoiding paths `pi` of
`S_pi`; on the (measurable) event that a given pair `(pi, rho)` attains both minima,
`T_e = S_pi - S_rho^{-e}`. For every pair this is a nondegenerate signed sum of distinct
weights: `edges(pi) = edges(rho) minus {e}` is impossible, because `rho minus {e}` is a union
of two vertex-disjoint segments with degree-1 endpoint set `{0, x} cup {y, v}` (four vertices;
two if `e` is terminal, but then the forced coincidence `x = 0` or `y = v` contradicts
`e = (x,y)` having two distinct endpoints off the path ends), while a simple path has exactly
two. A nondegenerate signed sum of independent a.c. variables is a.c.; a countable union of
a.c.-restricted events gives `P(T_e in N) = 0` for every Lebesgue-null `N`. QED.
Consequence: for every FIXED `n, e, u`, `P(|T_e - u| <= delta) -> 0` as `delta -> 0`. What
remains open at fixed exogenous levels is only UNIFORMITY in `n` (sections 5 and 8).
[complete proof]

## 4. Corollary 2 and Theorem 3: what the interfaces receive

**Corollary 2 (near-pivotal thinness; membership stability).** Under (H1)+(H2):

    P( e in gamma, g_e <= delta ) = P( 0 < gt_e <= delta ) <= min( p_e, beta delta ),

and the event that `e` leaves the geodesic when its own weight is inflated by `delta` is
EXACTLY `{0 < gt_e <= delta}`; hence single-edge membership is `beta`-Lipschitz under own-weight
inflation, uniformly in `n` and `e`. *Proof.* First claim: Theorem 1 with `I = (0, delta]`
plus `{gt_e > 0} = {e in gamma}` (P-ii). Second: inflating `w_e` by `delta` leaves `T_e`
unchanged (outside-measurable), so membership after inflation is `{w_e + delta < T_e}`; the
lost-membership event is `{w_e < T_e <= w_e + delta} = {0 < gt_e <= delta}`. QED. [complete
proof; falsifier verifies the event EQUALITY sample-by-sample, then the probability bound]

**Theorem 3 (layer-adapted master influence bound; (I1'-layer) reduces to (I2)).**
Work on the enlarged space carrying the engine's replacement `w_e'` (independent of
everything). For `f != e` let `w^{(f)}` be the environment with `w_f` replaced by an
independent fresh copy `wh_f`, and define the resampling influence of `f` on the layer
indicator `g_{e,s} := 1_{z_e > s}` as `Inf_f(g_{e,s}) := P( g_{e,s}(w, w_e') !=
g_{e,s}(w^{(f)}, w_e') )`. Let `Gamma_e := gamma_{C_e} cup gamma_{B_e}` (best avoiding and
best through path in the ORIGINAL environment; measurable selections; ties null under (H1)).
Then under (H1)+(H2), for every `s >= 0`:

    (i)  Inf_f(g_{e,s}) <= 2 E[ 1_{w_f < wh_f} 1_{f in Gamma_e} min(1, 2 beta (wh_f - w_f)) ]
                        <= 2 E[ 1_{f in Gamma_e} min(1, 2 beta |w_f - wh_f|) ],

    (ii) Inf_f(g_{e,s}) <= 2 min(1, 2 beta (b-a)) P( f in Gamma_e ),  and uniformly in s:

         sum_{f != e} Inf_f(g_{e,s})^2
             <= 4 min(1, 2 beta (b-a))^2 * sum_{f != e} P( f in Gamma_e )^2.        (*)

*Proof.* (1) The flip of `f` moves only `T_e`; `w_e, w_e'` are untouched, so by (P-iv) the
flip event is contained in `{w_e' - w_e > s} cap {1_{T_e(w) > w_e + s} != 1_{T_e(w^{(f)}) >
w_e + s}}`. (2) Apply (P-iii) pointwise at the realized level `u = w_e + s` (legitimate:
Lemma B is a deterministic statement about the map `x -> T_e(x)` with every other coordinate
frozen, and neither `T_e` nor `Gamma`-membership reads `w_e`): the threshold flip forces
`|T_e(w) - (w_e + s)| <= |w_f - wh_f| =: D` and `f in Gamma_e^{min}` (min-environment).
(3) Symmetry: the flip event is invariant under swapping `(w_f, wh_f)` (it compares the same
two environments), the pair is iid given the rest, and ties are null under (H1); so
`P(flip) = 2 P(flip, w_f < wh_f)`, and on `{w_f < wh_f}` the min-environment IS the original
one: `Gamma_e^{min} = Gamma_e`. (4) Conditioning - the one new move: let
`F' := sigma( (w_g)_{g != e}, wh_f, w_e' )`. Then `T_e(w)`, `T_e(w^{(f)})`, `1_{f in
Gamma_e}`, `1_{w_f < wh_f}`, and `D` are all `F'`-measurable, and `w_e` is independent of
`F'`. The flip requires `w_e in [T_e(w) - s - D, T_e(w) - s + D]`, an `F'`-measurable interval
of length `2D`, so `P(flip | F') <= min(1, Q_w(2D)) <= min(1, 2 beta D)`. (5) Combine and
double for (i); bound `|w_f - wh_f| <= b - a`, square, and sum for (ii). QED. [complete proof;
the falsifier checks the containment of step (2) sample-by-sample at 163 observed flips,
zero violations]

**What (*) says.** The right side of (*) is the restricted-geodesic membership collision sum -
P1's (I2) - with NO anticoncentration content left, and the bound is UNIFORM in the layer `s`
(so the `ds`-integration of FPP_THRESHOLD (9) costs only the factor `R <= b - a`). At
single-edge granularity, the anticoncentration half of (I1') in the layer-adapted
parameterization - which is the parameterization the engine consumes, since (9)'s target is
written in the increment layers - is CLOSED, unconditionally, by the independence of `w_e`
from `T_e`. The reduction is ONE-DIRECTIONAL: (I2) at the ledger's scale is now SUFFICIENT
for (I1'-layer),

    (I2)  sum_{f != e} P( f in gamma_{C_e} cup gamma_{B_e} )^2   at the ledger's scale,

pure restricted-geodesic delocalization, an object with no gap variable in it. Necessity is
NOT claimed: a failing membership sum could in principle be rescued by the fine structure of
small `|w_f - wh_f|` windows, though no mechanism for that is on file. Keep form (i)
for partial-noise couplings: there `|w_f - wh_f|` vanishes with the noise rate and the window
factor pays a genuine extra smallness; at full resampling it is worth only a constant
(consistent with P1's proved anchor "the window spans the support").

**Precise formulation of the surviving open input.** (I2-min): does DEP 2307.01162 Cor 1.3
hold, with uniform constants, for the geodesics of the edge-deleted lattices `Z^d minus {e}`
and for best-through-path minimizers? P3 verified DEP verbatim for `Z^d` only. Nothing here
assumes it.

## 5. Interface disposition (both certified lanes)

**IF-1 (P1, noise route).** Received: Theorem 3. Status of (I1') after this note: the
layer-adapted form holds at the ledger's scale WHENEVER (I2) does (up to the displayed
constants); the anticoncentration ingredient is free. The FIXED-exogenous-level variant
(`sup` over deterministic `u` of the same sum) is NOT proved here and stays open (section 6);
it is not what (9) consumes, but any consumer switching to the absolute-level representation
`h_{e,u} = 1_{X <= u < X^e}` (FPP_THRESHOLD (7)) would need it - that representation probes
passage-time levels, Elboim territory, n-scale, untouched.

**IF-2 (P2, first-chaos route).** The certified chain consumes cap-mass LOWER bounds -
`P(c_e >= tau, e in gamma, w_e >= tau)` via their (C1) + Lemma 3 - and a corridor. An
anticoncentration upper bound is not the missing input, and I checked the natural way one
might feed it in: replacing the fixed `tau` by the bottom scale `a + eps` with
`P(e in gamma, c_e < a + eps) <= F(a + eps) <= beta eps` and `eps = n / (8 beta |A_n|)`
gives a floor of order `n^6 / (beta^4 |A_n|^5)` (since `Psi(a + eps) ~ (Ew - a) rho(a)
eps^2 / 2` - quartic loss), strictly dominated by the certified `n^2 / |A_n|` for every
`|A_n| >= n` [falsifier: ratio 2.4e-4 at `|A_n| = n`]. DEAD REFINEMENT - recorded so no
successor lane re-runs it. What P2's side does receive from this note: the exact conditional
structure of Theorem 1 pins the joint law of `(c_e - w_e, membership)` - the reflected-density
identity - and Corollary 2 makes every membership-built first-chaos functional
`beta`-Lipschitz under per-edge perturbations. The Thread-B convergence on the IF-2 side
remains what the referee called it: directional (remark 5.2 is descriptive); their theorem
chain is complete as certified and waits on the corridor, which is I8-cognate, not Thread B.


**Corollary 4 (block gap near zero; union price).** Under (H1)+(H2), for any edge-block `L`:
`P( U_L, G_L <= delta ) <= beta |L| delta`.
*Proof.* On `U_L` pick any `e in gamma cap L`. Avoiding all of `L` is a stronger constraint
than avoiding `e`, so `C >= C_e`; on `U_L`, `X = A`, and on `{e in gamma}`, `X = B_e + w_e`;
hence `G_L = C - X >= C_e - X = gt_e > 0`. So `{U_L, G_L <= delta} subset cup_{e in L}
{0 < gt_e <= delta}`; union bound and Corollary 2. QED. [complete proof]

**Corollary 4' (boundary refinement).** If `L` is the full edge set inside a vertex box (or
any `L` whose entry edges - edges of `L` traversable before any other `L`-edge - form a set
`dL`), the union need only run over `dL`: `P(U_L, G_L <= delta) <= beta |dL| delta`. For a
`W x W` box in `Z^2`, `|dL| = O(W)` against `|L| = Theta(W^2)`.
*Proof.* Let `e*` be the first `L`-edge in the path order of `gamma`. Every vertex strictly
interior to the box has all incident edges in `L`, so the prefix of `gamma` before `e*`,
which uses no `L`-edge, cannot have reached the strict interior; the vertex from which `e*`
is traversed is non-interior, i.e. `e* in dL`. Apply Corollary 4's containment with the union
restricted to `dL`. QED. [complete proof; falsifier: 244/300 block-hit environments on the
7x7 lattice, zero entry-lemma violations]

**Proposition 5 (all-level block bound; tilt price).** The master inequality (the first
`<=` below) holds under (H0) - any iid law; the displayed evaluations need, respectively, a
density of finite total variation `V_rho` (which implies (H2)) and finite Fisher information
`I_rho`. For every level `s` and `delta > 0`:

    P( G_L in (s, s + delta] ) <= d_TV( P_L, P_L^{+delta} )
        <= min( |L| delta V_rho / 2 ,  sqrt( 2 |L| h^2(delta) ) ),

where `P_L^{+delta}` shifts every block coordinate by `delta`, `V_rho` is the density's total
variation (BV densities), and `h^2(delta)` the squared Hellinger distance of `rho` from its
`delta`-shift (`h^2 <= delta^2 I_rho / 8` for Fisher-finite densities, giving
`d_TV <= delta sqrt(|L| I_rho) / 2`; for `U[a,b]`, `h^2 = delta/(b-a)`).
*Proof.* (1) Monotone flow: every through path uses at least one `L`-edge, so
`A(w_L + delta 1_L) >= A(w_L) + delta` (a min of functions each increased by at least
`delta`); `C` reads no `L`-edge and is invariant; hence `G_L(w + delta 1_L) <= G_L(w) -
delta`, so `{G_L(. + delta 1_L) > s} subset {G_L > s + delta}` pointwise. (2) Therefore
`P(G_L in (s, s+delta]) = P(G_L > s) - P(G_L > s + delta) <= E_P[phi] - E_{P^{+delta}}[phi]`
with `phi = 1_{G_L > s} in [0,1]`, which is at most `d_TV`. (3) Tensorize: TV adds over
coordinates (`<= |L| delta V_rho / 2` by the shift-TV bound); Hellinger:
`h^2_total <= |L| h^2(delta)` and `d_TV <= sqrt(2 h^2_total)`. QED. [complete proof;
falsifier verifies the speed->=1 flow and the `C`-invariance exactly, and the resulting
interval bound empirically]

**Where the wall stands, quantified.** The exact-shift door of Theorem 1 exists because ONE
coordinate (`w_e`) enters the comparison with unit coefficient on one side and zero on the
other, independently of the level. At block granularity no coordinate has that property, and
the two available substitutes pay exactly the wall's price: the union over entries costs
`|dL| ~ W`; the diagonal tilt costs `|L| V/2` or `sqrt(|L| I)` because it must push `|L|`
coordinates to move the gap by `delta`. At the sandwich's fluctuation-scale
tolerances both block bounds are vacuous. The D-note's self-similar obstruction
(anticoncentration stable under minima over polynomially many attachment points) is NOT
breached; the corridor-pair collision object `Q(S(C1) - S(C2); 2 delta)` receives nothing
from this note. Also open: whether the true near-zero block rate has the `|dL|` factor at
all (the falsifier's small blocks cannot separate `|L|` from `|dL|`), and the at-level-`s`
analogue of Corollary 4 (the containment argument fails structurally there: `G_L in
(s, s+delta]` pins no single `gt_e` into a short interval).

## 7. Claim-label summary

  `Q(gt_e; delta) <= Q_w(delta)` is distribution-free; the linear rate needs (H2), and the
  atomic negative control shows (H2) is genuinely load-bearing for the rate.
* Corollary 2, Theorem 3, Corollaries 4/4', Proposition 5: complete proofs under the displayed
  hypotheses.
* (*)'s campaign meaning ("(I2) suffices for (I1'-layer), up to constants"): derivation from
  referee-confirmed inputs; ONE-DIRECTIONAL - I initially wrote it as an iff, and the
  converse direction does not survive its own re-derivation (small windows only shrink
  terms; no lower bound on the windowed sum in terms of the membership sum exists without a
  conditional gap-location statement nobody has). Corrected in place before filing.
  Route-level statement, labeled as such.
* Interface disposition (section 5): derivation + one dead-refinement arithmetic
  [falsifier-checked]; P2-side reading is inspection of their certified chain, not a theorem.
* Numerical items: falsifier only, 23/23, seconds-scale, NOT proof.

## 8. Honesty block

**Hardest open step of this note's own program:** (I2) - the restricted-geodesic collision
sum `sum_f P(f in gamma_{C_e} cup gamma_{B_e})^2` at the DEP scale, for edge-deleted and
file (P3 verified DEP for `Z^d` only, and I checked that status with my own eyes in
P3_VERDICTS "External sources" and in DEP's assumption line quoted there). Second-hardest:
fixed-exogenous-level anticoncentration of `T_e` (uniform in `n`), which Remark 1.1 proves
pointwise-in-`n` but not uniformly - that is the form a DEP-style eps-influential refinement
would want, and my mechanism cannot reach it (no independent randomization rides a
deterministic level).

**Strongest case my main claim is wrong:** the reduction's value collapses if the engine
cannot actually run on layer-adapted levels - i.e., if some consumer of the influence sums
secretly needs FIXED exogenous levels `u`. Then (*) bounds influences of a family the engine
does not consume, the anticoncentration half of Thread B at edge granularity is NOT closed,
and the hard core is the fixed-`u` form this note leaves open.

**The check, executed this session with my own eyes as far as the record reaches:** I
re-read BLOCK_INCREMENT_NOISE_SPLIT (1)-(23) line by line. Its sections 2-3 - the ANOVA
spectrum (8), the exact SS bound (13)-(14), and the approximate SS bound (16)-(17) - operate
on `z_L` DIRECTLY through algorithms/transcripts and revealment; NO layer level appears
anywhere in them, so that consumer is level-free by inspection, not by hope. The
level-bearing consumer is the DE-template route, whose target FPP_THRESHOLD (9) is written
in the increment layers `g_{L,s}` (dummy of `z`'s own layer cake) - the family (*) covers.
The KK/SS conversion of influence sums into noise covariance takes arbitrary Boolean
functions; the level is an index, never a conditioned quantity. RESIDUAL EXPOSURE, honestly
narrowed rather than waved off: (a) DISTINGUISHED_BLOCK's internals I re-read only at the
referee's claim-level descriptions (its confirmed statements are level-free ANOVA
identities); (b) any FUTURE consumer that instantiates the absolute-level representation
`h_{e,u} = 1_{X <= u < X^e}` of FPP_THRESHOLD (7) needs passage-time-level
anticoncentration at n-scale - Elboim territory - and gets nothing from this note; (c)
whether the influence-to-noise conversion CLOSES the edge-granularity budget at the
ledger's scale is P1's (I3)-adjacent open scale question, distinct from the
anticoncentration question this note answers. If a step needing a deterministic level is
ever found in (a), the reduction fails for that consumer and the fixed-`u` problem returns
as Thread B's edge-granularity core - that discovery, not more corroboration of my own
reading, is what would break this note.

(This was the coordinator's 19:06-campaign P7 ask: attack Thread B - restricted-min gap
anticoncentration - at the interfaces certified tonight by the referee from P1's (I1') and
P2's remark 5.2; orient on scars and verdicts first; deliver a usable statement or a
refutation with falsifier, lane-dir fire note, honesty block.)
