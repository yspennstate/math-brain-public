Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. SOURCE-LEVEL DEFECT UNCHANGED: `c_*: 0 -> 0`. This third unchanged directional-defect run executes the required materially different attack: it replaces the stationary one-Busemann/predictable-nonwinner mechanism by a finite two-target Bellman comparison. New proved gains are (i) an exact finite-volume representation of the full directional triangle defect with no Busemann-limit/interface factor, (ii) an Exp(1) disagreement-energy inequality that does not require the disagreement event itself to be predictable before the star is revealed, (iii) a direct fresh-candidate block compiler for P04, and (iv) a quantitative strict-concavity modulus for the local exponential Bellman operator.**

# P20 T10 — finite two-target residuals and disagreement energy

Date: 2026-09-20.
Repository: `yspennstate/math-open-problems`, branch `master`.
Parent claim: `operations/claims/PROB10-10.md` (owned by the canonical PROB10-10 lane; P20 remains the complementary LIVE20 Busemann/variational route).
Status: **PARTIAL / OPEN**.

## 1. Exact source target and before/after

The model is nearest-neighbor **undirected** first-passage percolation on `Z^2` with iid rate-one exponential edge weights. Write `T(x,y)` for passage time and `mu(v)` for the time constant.

The exact outside source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262v2, Question 4 in §2.5.1 / the summary of open questions:

> Show that if `F` is a continuous distribution then the limit shape is strictly convex.

The arXiv record is v2, submitted 10 November 2015 and revised 23 September 2016. P20 works only on the source-valid special case `F=Exp(1)` on undirected nearest-neighbor `Z^2`.

The frozen first directional milestone is

`Delta_12 := 2 mu(e1) - mu(1,1)`

and

`c_* := sup{c >= 0 : Delta_12 >= c has been rigorously proved in this track}`.

Before this run: `c_*=0`.
After this run: `c_*=0`.

So there is **no original-problem/source-metric movement**. The mathematical gain is separate: the previous stationary Busemann residual compiler required a positive density of stars whose *nonwinner status* was predictable before revealing each star. The present finite-target compiler only requires a positive amount of **conditional probability of eventual visit-and-policy-disagreement** at externally selected fresh stars; the disagreement itself may be decided after the star is revealed. It also represents the whole `Delta_12`, not `Delta_12/2`, directly in finite volume.

This is the third consecutive substantive P20 T10 run with `c_*=0`, so the owner directive requires a materially different attack. The finite two-target comparison below is that method change; it is not another sharpening of the one-Busemann toll.

## 2. Continuity and recovered failures

I followed `operations/PROGRESS20_2026-09-20.md` and the latest LIVE20 assignment. P20 remains T10 Busemann/variational curvature; P04 is the designated block-to-infinite-volume companion. No shared `POSTED.md`, claim file, peer report, schedule, permission, email, Drive object, workflow or public post was edited.

The two previous P20 reports are preserved:

- `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T00-08-24Z__busemann-residual-bellman-gap.md`;
- `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T01-48-00Z__sharp-bellman-gap-concentration.md`.

Their valid ingredients are used, not restarted:

1. For a diagonal supporting reconstructed Busemann cocycle `B`, `r_B(x,y)=tau_xy-B(x,y)>=0` and `R_B(a,b)=T(a,b)-B(a,b)`.
2. `Delta_12 = 2 lim_n E R_B(0,n e1)/n`.
3. For a finite target and a fresh four-edge star, the cheapest strictly nonoptimal Bellman departure `S` satisfies the **sharp** conditional tail
   `P(S>u | outside star) >= exp(-3u)` and hence `E[S | outside star]>=1/3`.
4. A stationary weak Busemann limit has a unique zero-residual outgoing edge at every fixed vertex and second residual stochastically bounded below by `Exp(3)`.
5. Under the old explicit predictable-pivot hypothesis, the preceding compiler gave `Delta_12 >= (2/3) alpha - 2 epsilon`; equivalently `alpha>3 epsilon` was sufficient.

The historical R08 failures remain binding and are not relabeled as progress:

- `R08-X001`: many local deletion margins can all arise from a single shared bypass, so local savings cannot simply be multiplied;
- `R08-X002`: a deterministic finite strict triangle saving fails on positive-probability open Exp(1) cylinder events;
- `R08-L003`: retained axis certificate `mu(e1)>=3753/12500=0.30024`;
- fixed-corner exact blocks through size three did not reach the corresponding diagonal threshold `0.60048`;
- old KPZ/fluctuation work is not curvature and is not imported as a theorem.

The exact geometric diagnostic is also preserved: `Delta_12=0` forces equality in the norm triangle inequality between `e1` and `e2`, hence by square-lattice symmetries the first-quadrant boundary of the limit shape is the line segment joining the two axis intercepts; this is a useful contradiction hypothesis, not a proof that it cannot occur.

## 3. Current neighboring block state and P04 coordination boundary

The newest canonical PROB10-10 report read for this run is

`runs/prob10_2026-09-20/PROB10-10/20260920T0127Z__selected-reversal-block.md`

at creation commit `c28e5fa02fb9b6f010adf2f43652408d03567984`.

It proves an unconditional random-endpoint finite-to-infinite block compiler that permits selected true undirected reversals while assigning each physical edge to a disjoint absolute `l1`-level band. Its exact `m=4, J={1,2}` computation improves

`mu(1,1) <= 0.762740573150706 -> 0.758507818076`,

but this remains above `0.60048`, so it does not move `c_*`. The reusable point for the present report is its **physical-edge band ownership**: backtracking does not destroy freshness if the underlying physical edges belong to disjoint bands.

At the repository state inspected here there is still no T10 run root at `proofnet24/P04-progress-curvature/runs/2026-09-20/`. Recent commits carrying the string `P04` concern other historical P04 assignments, not the current T10 FPP companion. I therefore do not fabricate a P04 theorem. Section 7 gives a source-matching quantitative compiler for P04 to consume once a fresh-star block/exploration is available.

## 4. Fresh literature boundary and hypothesis discipline

A fresh 20 September 2026 search did not recover a source-matching proof of strict convexity for ordinary iid continuous undirected nearest-neighbor FPP, nor for the Exp(1) square-lattice special case.

Relevant neighboring results were checked only for what their hypotheses actually give:

- Auffinger--Damron--Hanson arXiv:1511.03262v2 still states Question 4 literally as strict convexity for continuous `F`. Their Busemann Theorem 5.9 in `d=2` gives a coalescing sector-directed family under continuity and differentiability at a chosen boundary point, with finite backward clusters; Lemma 5.10 identifies the mean reconstructed Busemann slope. These are legitimate ingredients but do not prohibit a flat support face.
- Damron--Hanson's sector/Busemann framework likewise gives coalescence and sector-directed geodesics under directional/differentiability hypotheses; it does not settle strict convexity.
- Jacquet, arXiv:2310.04091, proves linear crossings of any admissible fixed local pattern with exponentially small exceptional probability even for unbounded-support laws. Exp(1) is within that distributional scope. However a local pattern crossing is not automatically a disagreement between the Bellman policies for the axis and diagonal targets, so it does not fill the missing hypothesis below.
- Dembin--Elboim--Peled, arXiv:2204.02332, proves quantitative planar coalescence under a hypothesis that the limit shape has more than 32 extreme points. Using it to establish the missing Exp(1) shape geometry would be circular.
- Ahlberg--Deijfen--Sfragara, arXiv:2607.07589 (8 July 2026), uses Busemann functions and local modification in competing FPP under a tangent-line hypothesis. It is relevant technique, not a proof of the missing tangent/strict-convexity property.
- Krishnan's variational/HJB formula (arXiv:1311.0316 / 1406.1108) is conceptually close, but the displayed main discrete theorem assumes edge weights essentially bounded above and bounded away from zero. Rate-one exponentials violate both bounds. I therefore use no theorem from that paper as an Exp(1) transfer. Section 8 instead proves the needed local Bellman strictness directly.

Directed integrable constants and sampled numerical curvature are not used.

## 5. New exact finite-volume representation of the full triangle defect

The stationary Busemann representation in the previous reports is useful but has an avoidable asymmetry: a single diagonal-support cocycle measures only `Delta_12/2` on one axis leg, and block arguments must then pass through an infinite-volume weak Busemann law.

There is a simpler exact finite-target identity.

For `n>=1`, put

`b_n = n e1`,
`z_n = n(e1+e2)`.

For any target `z` and oriented nearest-neighbor edge `(x,y)`, define the finite-target residual

`r_z(x,y) := tau_xy + T(y,z) - T(x,z) >= 0`.

For a path `gamma=(v_0,...,v_k)`, telescoping gives

`sum_{j<k} r_z(v_j,v_{j+1})`
` = T(gamma) + T(v_k,z) - T(v_0,z)`.

### P20-FPP-FINITE-CORNER-RESIDUAL-07

**Claim: PROVED.** Let `Gamma_n` be the a.s.-unique geodesic from `0` to `b_n`. Then

`D_n := sum_{e in Gamma_n} r_{z_n}(e)`

satisfies the exact path-independent formula

`boxed{ D_n = T(0,b_n) + T(b_n,z_n) - T(0,z_n) >= 0. }`          (5.1)

Moreover

`boxed{ lim_{n->infty} E[D_n]/n = Delta_12. }`                    (5.2)

#### Proof

Apply the telescoping identity to `Gamma_n`. Since it is a geodesic, `T(Gamma_n)=T(0,b_n)`, and its endpoint is `b_n`, giving (5.1). Translation invariance and the square-lattice symmetry exchanging `e1,e2` give

`E T(b_n,z_n) = E T(0,n e2) = E T(0,n e1)`.

Therefore

`E D_n = 2 E T(0,n e1) - E T(0,n(e1+e2))`.

Rate-one exponentials have all moments needed for the standard `L1` time-constant convergence, so division by `n` and passage to the limit gives (5.2). QED.

### Why this representation is a real method change

The residual-minimizing path from `0` to `b_n` for target `z_n` is exactly the ordinary `0`-to-`b_n` geodesic because the endpoint correction `T(b_n,z_n)-T(0,z_n)` is fixed. Thus the full directional triangle defect is the asymptotic cost paid by the **axis geodesic under the diagonal-target Bellman policy**.

Unlike the stationary cocycle identity, there is no weak-limit transfer, no unknown stationary environment seen from the geodesic, and no factor `2` to restore at the end. The price is that the comparison policy varies with location because the target `z_n` is finite. That variation is exactly what the next lemma exploits.

## 6. New two-target disagreement-energy inequality

Fix a vertex `x` distinct from two targets `A,C`. Delete `x` and its four incident edges. Let its neighbors be `y_1,...,y_4`. Conditional on every edge outside the star of `x`, define deterministic deleted-star continuation values

`a_i = T_{G\{x}}(y_i,A)`,
`c_i = T_{G\{x}}(y_i,C)`

and fresh iid star weights `E_i~Exp(1)`.

Put

`X_i^A=E_i+a_i`, `M_A=min_i X_i^A`, `I_A=argmin_i X_i^A`,

and similarly `(X_i^C,M_C,I_C)`.

Positive continuous weights imply unique winners a.s. As proved in the preceding P20 report, for target `A` the exact Bellman residual of a nonwinner `j` is

`s_j^A = min(X_j^A-M_A, 2E_j)`,

and the cheapest nonwinner residual

`S_A=min_{j != I_A} s_j^A`

satisfies, uniformly in the outside-star offsets,

`P(S_A>u | outside star) >= e^{-3u}` for every `u>=0`.            (6.1)

Now compare the two target policies. Let

`D={I_A != I_C}`,
`p=P(D | outside star)`.

On `D`, the edge chosen by target `C` is a nonwinner for target `A`, hence

`s_{I_C}^A >= S_A`.

The point is that `D` may be strongly correlated with the event that `S_A` is small. Predictability of `D` is not assumed.

Define for `0<=p<1`

`g(p) := [p + (1-p) log(1-p)]/3`,

and set `g(1)=1/3` by continuity.

### P20-FPP-TWO-TARGET-DISAGREEMENT-ENERGY-08

**Claim: PROVED.** Conditional on the outside-star environment,

`boxed{ E[ s_{I_C}^A 1_D | outside star ] >= g(p) >= p^2/6. }`    (6.2)

No independence between `D` and the Bellman gap is required.

#### Proof

By nonnegativity and the observation above,

`E[s_{I_C}^A 1_D | outside] >= E[S_A 1_D | outside]`.

For every `u>=0`,

`P(D intersect {S_A>u} | outside)`
` >= p - P(S_A<=u | outside)`
` >= p - (1-e^{-3u})`                                              (6.3)

using (6.1). Let

`u_p = -(1/3) log(1-p)`

for `p<1`. The right side of (6.3) is nonnegative exactly for `0<=u<=u_p`. Layer-cake integration yields

`E[S_A 1_D | outside]`
` >= integral_0^{u_p} [p-1+e^{-3u}] du`
` = [p+(1-p)log(1-p)]/3`
` = g(p)`.

For `p=1`, monotone convergence gives `g(1)=1/3`.

Finally `g(p)>=p^2/6`: multiplying by three, this is

`p+(1-p)log(1-p) >= p^2/2`.

The difference has value zero at `p=0` and derivative

`-log(1-p)-p >= 0`,

so it is nonnegative. QED.

### Interpretation

The previous predictable-pivot compiler charged `1/3` only after a star had been selected **and** it was already known that the eventual path would take a nonwinner edge. The new inequality allows the entire visit/disagreement decision to depend on the revealed star. What must remain fresh is only the **identity of the candidate star**. The cost for this extra adaptivity is a quadratic small-`p` modulus `g(p)~p^2/6`, which is unavoidable from the one-star information alone: an adversarial disagreement event can concentrate on near-ties.

## 7. Direct finite-volume compiler for P04

Use the exact finite geometry of Section 5 with targets

`A=z_n=n(e1+e2)`, `C=b_n=n e1`.

At a vertex `x` on the unique axis geodesic `Gamma_n`, the outgoing edge of `Gamma_n` is exactly the `C`-Bellman winner `I_C(x)`. Therefore the `A`-residual term of `Gamma_n` at `x` is positive precisely when `I_A(x) != I_C(x)`.

Consider any block/exploration procedure producing candidate vertices `X_1,...,X_{K_n}` with the following **fresh-candidate** properties:

1. candidate stars are pairwise edge-disjoint;
2. the identity of `X_j` is fixed before the four edges of `star(X_j)` are exposed (a disjoint physical-edge-band construction is sufficient);
3. all information used to select the candidate leaves its four incident Exp(1) edges fresh;
4. no requirement is imposed before reveal on whether `Gamma_n` visits `X_j` or whether the two target policies disagree there.

Let

`D_j = { X_j is a vertex of Gamma_n and I_A(X_j) != I_C(X_j) }`.

Let `F_j` be the pre-star information and

`p_j=P(D_j | F_j)`.

The offsets for the two targets may still be random under `F_j`. To justify using (6.2), condition further on all non-star edges. This fixes the deleted-star offsets. Apply (6.2), then average back to `F_j`. Since

`g'(p)=-(1/3)log(1-p)`, `g''(p)=1/[3(1-p)]>0`,

`g` is convex, so Jensen gives the same lower bound `g(p_j)` after forgetting the additional non-star information.

The residual charged at distinct visited candidates is a subset of the nonnegative residual terms in (5.1). Hence

### P20-FPP-FRESH-CANDIDATE-COMPILER-09

**Claim: PROVED under the explicit fresh-candidate hypothesis above.**

`boxed{ E D_n >= E sum_{j<=K_n} g(p_j) >= (1/6) E sum_{j<=K_n} p_j^2. }`  (7.1)

In particular, if for constants `C,eta>0` and all large `n`,

`K_n <= C n` almost surely,

and

`E sum_{j<=K_n} p_j >= eta n`,

then

`boxed{ Delta_12 >= eta^2/(6C) >0. }`                             (7.2)

#### Proof of the last implication

By Cauchy--Schwarz, pointwise on `K_n>0`,

`sum_j p_j^2 >= (sum_j p_j)^2/K_n >= (sum_j p_j)^2/(C n)`.

Using (7.1), Jensen, and the assumed first moment,

`E D_n`
` >= (1/(6 C n)) E[(sum_j p_j)^2]`
` >= (1/(6 C n)) (E sum_j p_j)^2`
` >= eta^2 n/(6C)`.

Divide by `n` and use (5.2). QED.

### Controlled-error version

If P04 works with a block proxy and proves only

`D_n >= sum_j charged_j - L_n`

with `E L_n <= epsilon n+o(n)`, then the same proof gives

`boxed{ Delta_12 >= eta^2/(6C) - epsilon. }`                      (7.3)

Thus the exact source-level success condition for such a block scheme is

`eta^2 > 6 C epsilon`.

A more local version is often sharper: if at least `alpha n+o(n)` fresh candidates have `p_j>=p0`, then

`Delta_12 >= alpha g(p0) - epsilon`,                              (7.4)

so it suffices that `alpha g(p0)>epsilon`.

This is the concrete P04 interface produced in the present run. It is strictly more permissive than the previous predictable-nonwinner interface: **candidate selection must be fresh, but visit and target-policy disagreement may be post-reveal random events.**

## 8. Variational form: strict concavity of the local Exp Bellman operator

The same mechanism has a clean HJB/Bellman formulation that may be more useful for a stationary-frontier block recursion.

For deterministic vectors `a,c in R^4`, with the same iid `E_i~Exp(1)`, put

`M(a)=min_i(E_i+a_i)`,
`I_a=argmin_i(E_i+a_i)`.

Let

`p=P(I_a != I_c)`.

Pointwise concavity of `min` gives

`M((a+c)/2) >= [M(a)+M(c)]/2`.

The Exp law makes the inequality quantitatively strict whenever the policies disagree.

For a score vector `a`, let `G_a` be the gap between the smallest and second-smallest values among `(E_i+a_i)`. The same memoryless argument used for the Bellman slack gives

`P(G_a>u)>=e^{-3u}`                                               (8.1)

uniformly in `a`: conditional on the winning channel and winning score, each of the three nonwinner score gaps stochastically dominates an independent rate-one exponential.

If `I_a != I_c`, then for every channel `k` at least one of

`(E_k+a_k)-M(a)`, `(E_k+c_k)-M(c)`

is a nonwinner gap. Therefore

`M((a+c)/2)-[M(a)+M(c)]/2`
` = (1/2) min_k {[(E_k+a_k)-M(a)]+[(E_k+c_k)-M(c)]}`
` >= (1/2) min(G_a,G_c) 1_{I_a != I_c}`.                         (8.2)

By the union bound and (8.1),

`P(min(G_a,G_c)<=u) <= 2(1-e^{-3u}) <= 6u`.                      (8.3)

Exactly as in Section 6, for the disagreement event of probability `p`,

`E[min(G_a,G_c) 1_{I_a != I_c}]`
` >= integral_0^{p/6} (p-6u) du = p^2/12`.

Combining with (8.2) proves:

### P20-FPP-EXP-BELLMAN-STRICT-CONCAVITY-10

**Claim: PROVED.**

`boxed{ E M((a+c)/2) - (E M(a)+E M(c))/2 >= p^2/24. }`           (8.4)

The modulus is invariant under adding constants to either offset vector, as it must be. This is an Exp-specific local strict-concavity statement for the averaged Bellman operator modulo constants.

### Why this does not already prove strict convexity of the limit shape

A flat macroscopic support face can in principle be carried by one sector-valued corrector/policy, so local strictness does not automatically imply a positive density of competing policies. What (8.4) does provide is an exact quantitative certificate for any P04/PROB10-10 stationary-frontier scheme that carries two competing continuation states through fresh bands: whenever their optimal local channels disagree with probability `p`, the one-step averaged Bellman recursion loses at least `p^2/24` relative to affine interpolation.

This is the rigorous local variational ingredient that generic HJB language alone did not supply for unbounded Exp(1) weights.

## 9. A tempting Busemann consequence and why it is not yet the closure

Under the contradiction hypothesis `Delta_12=0`, the first-quadrant boundary is the flat segment joining the two axis intercepts. Its interior diagonal point has a unique supporting line, so the ADH reconstructed-Busemann machinery applies there. Let the support vector be `rho=(b,b)`; then flatness gives `b=mu(e1)`. The retained certified bound gives

`b >= 0.30024 > 1/4`.

At finite targets, a fixed channel which is not the Bellman winner has conditional score/residual gap stochastically bounded below by a rate-one exponential. Passing this intuition to a symmetric diagonal Busemann limit suggests a strong forward bias of the zero-residual successor: each of the east and north channels must carry substantial calibrated mass. This is potentially useful with the absolute-`l1` physical bands of the block lane.

I do **not** promote the resulting path-drift heuristic to a theorem here. The reason is important: a spatially stationary outdegree-one coalescing forest can have a different environment law when viewed from its forward path. Mass transport gives

`E[# {x : the k-th successor of x is 0}] = 1`,

while ADH's finite-backward-cluster property makes that ancestor count tend to zero almost surely as `k->infty`; hence the sequence is necessarily non-uniformly integrable. A positive spatial arrow bias therefore does not by itself give a pathwise velocity bound. This is a concrete failure of the naive “local bias implies directed path speed” shortcut.

Likewise, swap symmetry of a reconstructed diagonal Busemann law does not force every ergodic component to be swap-symmetric; a mixture of symmetry-broken components is possible. I do not use that shortcut either.

## 10. Residual obstruction after the method change

The old bottleneck was phrased as “prove a positive density of predictable forced non-Busemann departures.” The finite two-target attack narrows it:

> **Residual obstruction T10/P20 after this run.** Construct at most `C n` externally selected fresh stars, preferably by physical-edge `l1` bands, for which the sum of the conditional probabilities
> `P(axis geodesic visits the star AND axis-target winner differs from diagonal-target winner | pre-star data)`
> is at least `eta n`, with either no comparison loss or a loss `epsilon n` satisfying `eta^2>6C epsilon`.

This is genuinely weaker than requiring the charged event to be known before reveal.

Two obvious shortcuts still fail:

1. **Pattern theorem alone.** Jacquet gives linearly many crossings of any admissible local passage-time pattern, but such a pattern does not uniformly force the two target Bellman policies to disagree; outside continuation offsets can favor the same channel for both targets.
2. **Many low-probability candidates.** Taking `O(n^2)` spatial candidates with individual visit probabilities `O(1/n)` does not help because the unavoidable local modulus is quadratic at small disagreement probability: `g(p)~p^2/6`. P04 needs a block exploration concentrating the geodesic's candidate mass onto only `O(n)` fresh stars or a comparably strong frontier compression.

This is why the current PROB10-10 idea of carrying a bounded transverse frontier rather than resetting to one point is especially relevant. A bounded frontier can keep `C` finite, while (8.4) can charge genuine policy mixing inside each fresh band.

## 11. Next attack

The next P20 attack should not return to numerical curvature or another refinement of the `1/3` star constant. The high-value target is a **reserved-star frontier lemma** compatible with the physical-edge-band compiler:

1. In each absolute `l1` band, reveal enough of the band to determine a bounded transverse candidate set, but reserve one or a bounded number of complete stars.
2. Prove that the axis-target and diagonal-target continuation states entering the band have a nontrivial conditional policy-disagreement mass `p0` at one reserved star, or else show that their continuation vectors differ only by an additive constant across the whole frontier.
3. In the latter alternative, propagate that near-constant difference to the next band. If it persists for linearly many bands, use the incompatible terminal boundary conditions at `b_n` and `z_n` to force a band where the disagreement mass is bounded below.
4. Charge each such band by (6.2) or, for a frontier recursion, by the Bellman concavity modulus (8.4).

The key new possibility is step 3: local strict concavity converts “two continuation states are not translates” into energy, while translation-equivalent continuation states can be propagated algebraically. This is a finite-dimensional variational dichotomy and avoids assuming a priori geodesic curvature.

If this frontier/translation dichotomy fails in the next recovery, the failure should be recorded explicitly and P20 should switch unresolved T-scope after the owner-prescribed two failed recoveries rather than continue polishing the same star lemma.

## 12. Essential sanity checks / code status

No finite enumeration or simulation is essential to Claims 07--10. Their proofs are algebraic/probabilistic and are complete on page. I therefore did **not** add a sampled curvature computation or a checker whose output could be mistaken for source evidence.

As a private arithmetic sanity check only, the exact modulus

`g(p)=[p+(1-p)log(1-p)]/3`

was evaluated at representative `p` and compared with `p^2/6`; the analytic derivative proof in Section 6 is the certification. No code artifact is needed for any theorem claim in this report.

## 13. Short handoff of displaced cyclic-interval work

The earlier P20 source `FOKAM-BITJOKA-2026-CYCLIC-INTERVAL` remains preserved and untouched. P20's source-literal YES proof candidate `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01` remains on record together with the supplementary exact sanity output. The P26 full-proof/source-quantifier audit remains PASS; the last recovered state had no second genuinely distinct non-P20/non-P26 full-proof audit. No completed certification or public novelty claim is implied. Under the current owner directive P20 does not spend FPP runs waiting for that audit.

## 14. Ledger delta

P20 does not edit shared ledgers. Requested reconciliation only:

- Keep parent ownership of `PROB10-10` unchanged; P20 remains the complementary T10 Busemann/variational lane.
- Record source metric `c_*: 0 -> 0` for this P20 run. Original strict convexity remains OPEN.
- Record demonstrated mechanism gains separately:
  - `P20-FPP-FINITE-CORNER-RESIDUAL-07 = PROVED`;
  - `P20-FPP-TWO-TARGET-DISAGREEMENT-ENERGY-08 = PROVED`;
  - `P20-FPP-FRESH-CANDIDATE-COMPILER-09 = PROVED / CONDITIONAL BLOCK INPUT`;
  - `P20-FPP-EXP-BELLMAN-STRICT-CONCAVITY-10 = PROVED`.
- This is the third `c_*=0` P20 T10 substantive run; the required material method change was executed here (finite moving-target/two-policy comparison instead of stationary one-Busemann predictable pivots).
- P04 companion request: use a fresh physical-edge-band/block exploration to seek constants `(C,eta,epsilon)` satisfying `eta^2/(6C)>epsilon`, or `(alpha,p0,epsilon)` satisfying `alpha g(p0)>epsilon`. Crucially, only the candidate-star identity must be fixed before reveal; visit and policy disagreement may be decided after reveal.
- PROB10-10 frontier request: in any bounded-frontier carry recursion, use (8.4) as an exact Exp(1) strict-concavity toll for non-translate competing continuation states rather than extending fixed-size enumeration solely for a numerical diagonal bound.
- Preserve R08 failure states and the cyclic-interval handoff; do not reopen or overwrite them.

## 15. Status

`c_*=0` and global strict convexity remains **OPEN**.

What is now proved is a stronger finite-volume/variational mechanism: the full axis/diagonal triangle defect equals a moving-target residual energy, and any externally fresh block family with linear total axis-vs-diagonal policy-disagreement probability yields an explicit positive defect after the quadratic Exp(1) disagreement modulus and controlled block errors.

The unresolved mathematical task is no longer to manufacture a local toll. It is to prove a **linear amount of concentrated two-target policy disagreement in only O(n) fresh candidates**, or to use the strict Bellman concavity modulus to force such disagreement from non-translate frontier states.

END OF P20 FPP RUN REPORT
