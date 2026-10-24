Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — no authenticated applied reasoning-effort receipt is exposed, so I do not claim a specific effort setting.**

# P20 T10 — geodesic pattern backtracking, flatness residual collapse, and a same-quadrant handoff

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent: `operations/claims/PROB10-10.md`.  
Model: undirected nearest-neighbor FPP on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for strict convexity. New theorem arguments below are **CANDIDATE_PROVED pending later independent review**. No completed certification or novelty claim is made.

## 1. Exact source and source-level before/after

The source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262v2, Question 4 in the limit-shape discussion: prove strict convexity for continuous passage-time laws. The canonical repository specialization is iid `Exp(1)` undirected nearest-neighbor FPP on `Z^2`.

Write `mu` for the deterministic time-constant norm and

`Delta_12 := 2 mu(e1) - mu(1,1) >= 0`.

The frozen source-facing metric is the largest rigorously proved `c>=0` with `Delta_12>=c`.

- **before:** `c_*=0`;
- **after:** `c_*=0`.

So this run does **not** prove the axis/diagonal strict triangle inequality and does not close ADH strict convexity.

The demonstrated mechanism gain is separate and substantive: a valid Jacquet pattern forces **linearly many actual backtracking detours on the true axis geodesic**; under the flat-face contradiction `Delta_12=0`, the exact P20 finite-target residual budget then forces a positive-density subfamily of those detours to have vanishing diagonal-target Bellman residual. This turns the prior vague shared-bypass obstruction into an explicit **co-calibration rigidity alternative** on linearly many true-geodesic pattern crossings.

## 2. Essential state consumed and a source-facing correction

I consumed only the essential current state:

- `operations/PROGRESS20_2026-09-20.md` and the LIVE20 pairing `P04 <-> P20` on T10;
- `operations/claims/PROB10-10.md`;
- P20's preceding report `2026-09-20T09-18-00Z__single-edge-residual-clock-compiler.md`;
- P04's newest report `2026-09-20T09-47-23Z__width7-undirected-cone1362.md`;
- canonical owner report `runs/prob10_2026-09-20/PROB10-10/20260920T1018Z__hard-cone-reset-first-moment-barrier.md`;
- R08 failure history as preserved in the canonical claim and current owner report;
- the already-executed P20 supporting pattern sanity artifact at `proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T10-37-00Z__backtrack-pattern-rigidity-check.py` and its archived output.

The canonical owner report makes an important correction that is binding here. Reflected inequalities of the form

`mu(1,rho)+mu(1,-rho)>mu(2,0)`, `rho>1`,

are not source-facing progress toward `Delta_12`: by D4 symmetry and norm convexity they are already compatible with the exact `l1`-diamond obstruction. Therefore the previously reported reflected-cone bounds remain valid only to the extent their proofs establish those inequalities, but they are **not** counted as movement of `c_*`.

The same owner report also proves a hard first-moment barrier for the weighted-SAW/Chernoff architecture at the diagonal: the monotone E/N path subfamily already defeats the union bound for every target coefficient `c>=58/125=0.464`, whereas P04's current axis upper cap is about `0.51779`. So merely increasing local SAW memory is not a credible diagonal attack.

The retained historical failures remain binding:

1. shared bypasses destroy naive multiplication of independent local surgery gains;
2. finite positive-probability cylinder events can have exact finite triangle equality, so pointwise finite strictness is false;
3. old fixed-corner square blocks did not meet the axis/diagonal threshold;
4. R07/KPZ fluctuation statements are not curvature theorems;
5. directed integrable models and unrestricted-versus-directed comparisons do not prove the same-quadrant strict triangle inequality needed here.

## 3. Exact finite-target residual budget retained from P20

Let

`C_n = n e1`,
`A_n = n(e1+e2)`,

and let `Gamma_n` be the a.s.-unique geodesic from `0` to `C_n`. For an oriented physical edge `x->y`, define the diagonal-target Bellman residual

`r_n(x,y) := tau_xy + T(y,A_n) - T(x,A_n) >= 0`.

The preceding P20 work established the exact samplewise identity

`D_n := T(0,C_n)+T(C_n,A_n)-T(0,A_n)`

`     = sum_{e in Gamma_n} r_n(e)`.                     (3.1)

Translation and square-lattice symmetry give

`E D_n = 2 E T(0,n e1)-E T(0,n(e1+e2))`,

and hence `E D_n/n -> Delta_12`.

Let `C_A<infinity` be a constant in the standard Alexander/ADH mean-convergence estimate

`E T(0,x) <= mu(x)+C_A sqrt(|x| log |x|)`

for large `|x|`; Exp(1) satisfies the required moments. Under the contradiction hypothesis

`Delta_12=0`,                                               (3.2)

D4 symmetry and the supporting-line argument imply the full first-quadrant diamond identity

`mu(x,y)=a(x+y)` for `x,y>=0`, where `a=mu(e1)`.             (3.3)

In particular `mu(n,n)=2an`. Since `E T(0,(n,n))>=mu(n,n)`, (3.1) gives the one-sided finite budget

`E D_n <= 2 C_A sqrt(n log n)`                              (3.4)

(up to harmless changes of `C_A` for the norm convention). This sublinear budget is the contradiction resource used below.

## 4. A valid undirected pattern that forces a real backtrack

Use the six-vertex box

`Lambda = {0,1,2} x {0,1}`

with endpoints

`u=(0,0)`, `v=(2,0)`.

Let the desired path be the four-edge U-detour

`P: (0,0)->(0,1)->(1,1)->(2,1)->(2,0)`.

Define the local pattern event `A_P` by

- each of the four desired edges has weight in `[1,101/100]`;
- each of the other three internal box edges has weight at least `10`.

For iid Exp(1), `P(A_P)>0`. Because the support is unbounded, this is an admissible/valid finite pattern in the sense needed by Jacquet's pattern theorem; the box contains a finite internal connection from `u` to `v`.

The exact checker already committed on master enumerates all self-avoiding `u-v` paths in `Lambda`. It verifies that there are four such paths, the desired path has cost at most `4.04`, and every competitor has cost at least `20` on `A_P`. Hence whenever a geodesic crosses a translate of this pattern through the prescribed endpoints, its internal segment is exactly the U-detour `P` (or the reversed U-detour according to crossing orientation).

Jacquet's pattern theorem for useful FPP with unbounded support applies to Exp(1): for every valid pattern there exist constants `alpha_P>0`, `c_P>0` such that, apart from an event of probability at most `exp(-c_P n)` (after changing constants), every sufficiently long point-to-point geodesic has at least `alpha_P n` translated occurrences of that pattern. We use only this qualitative linear/exponential conclusion; no explicit value of `alpha_P` is claimed.

### Lemma 4.1 — every U-detour has an `l1`-away step

Let `z` be any target and let `p=(x_0,...,x_l)` be any nearest-neighbor path. Let `A_z(p)` be the number of steps for which

`|x_{i+1}-z|_1 = |x_i-z|_1+1`.

Then

`A_z(p) = [ l + |x_l-z|_1 - |x_0-z|_1 ]/2`.               (4.1)

**Proof.** Every nearest-neighbor step changes `l1` distance to `z` by exactly `+1` or `-1`. If `A` steps increase and `l-A` decrease, then

`|x_l-z|_1-|x_0-z|_1 = A-(l-A)=2A-l`.

Rearrange. QED.

For either orientation of `P`, `l=4` while its endpoints are `l1`-distance `2`. The triangle inequality gives

`|x_l-z|_1-|x_0-z|_1 >= -2`,

so (4.1) yields

`A_z(P)>=1`.                                               (4.2)

Thus a U-detour necessarily contains a genuine step away from **every** target, not only away from the axis endpoint.

### Lemma 4.2 — bounded overlap of translated desired paths

A fixed physical edge of `Z^2` belongs to the four-edge desired set of at most two translations of `P`.

**Proof.** A horizontal edge can occupy one of the two horizontal positions on the top of the U, giving at most two translations. A vertical edge can occupy one of the two side positions, again at most two. These exhaust the desired edges. QED.

The committed exact checker verifies this multiplicity statement and the distance identity on a finite window as a sanity check; the proof above is the general argument.

## 5. Linear backtracking on the actual axis geodesic

Let `N_n^P` be the number of translated occurrences of the U-pattern traversed by the actual axis geodesic `Gamma_n`. Let `B_n` be the number of oriented edges `x->y` of `Gamma_n` for which

`|y-C_n|_1 = |x-C_n|_1+1`,

that is, steps moving away from the endpoint in `l1` distance.

### P20-FPP-JACQUET-BACKTRACK-DENSITY-33 — CANDIDATE_PROVED

There are constants `alpha_P,c_P>0` such that

`P( B_n >= (alpha_P/2)n ) >= 1-exp(-c_P n)`                (5.1)

for all sufficiently large `n` (after modifying constants). Consequently

`E B_n >= (alpha_P/2)n [1-exp(-c_P n)]`.                   (5.2)

### Proof

Jacquet gives

`N_n^P >= alpha_P n`                                      (5.3)

outside an exponentially small exceptional event.

By Lemma 4.1, from each traversed pattern occurrence choose one desired edge of its U-segment that is `l1`-away from `C_n`. Lemma 4.2 says that any physical edge can be selected by at most two different translated occurrences. Therefore

`B_n >= N_n^P/2`                                           (5.4)

samplewise. Combining (5.3)--(5.4) proves (5.1), and taking expectations gives (5.2). QED.

This is a true-geodesic statement, not a statement about a constructed comparison path and not sampled numerical curvature. It resolves one previously ambiguous part of the ancestry problem: the axis geodesic itself has linearly many geometrically nonmonotone local pieces.

## 6. New flatness rigidity: positive-density patterns must become diagonally co-calibrated

For each translated pattern occurrence `q` traversed by `Gamma_n`, orient its four-edge desired U-segment in the direction in which `Gamma_n` traverses it and define its total diagonal-target residual

`R_n(q) := sum_{e in P_q} r_n(e) >= 0`.                    (6.1)

Because each physical edge lies in at most two translated desired U-paths, Lemma 4.2 and (3.1) imply the exact samplewise overlap bound

`sum_{q in Occ_n(P)} R_n(q) <= 2 D_n`.                     (6.2)

This observation is the main mechanism gain of the run.

### P20-FPP-PATTERN-RESIDUAL-COLLAPSE-34 — CANDIDATE_PROVED

Assume `Delta_12=0`. Then

`E sum_q R_n(q) <= 4 C_A sqrt(n log n)`.                   (6.3)

For every deterministic threshold `lambda_n>0`, let

`M_n(lambda_n) := #{ q in Occ_n(P): R_n(q)>=lambda_n }`.

Then

`E M_n(lambda_n)`
` <= (4 C_A/lambda_n) sqrt(n log n)`.                       (6.4)

In particular, if

`lambda_n >> sqrt(log n / n)`,                              (6.5)

then

`M_n(lambda_n)=o_P(n)`.                                    (6.6)

At the concrete choice `lambda_n=n^(-1/4)`,

`E M_n(n^(-1/4)) = O(n^(3/4) sqrt(log n)) = o(n)`.          (6.7)

Combining this with Jacquet's theorem, under flatness the actual axis geodesic has a positive linear number of U-pattern occurrences but all except an `o_P(n)` subfamily have total diagonal-target residual below `n^(-1/4)`.

### Proof

Under `Delta_12=0`, (3.4) and (6.2) give

`E sum_q R_n(q) <= 2 E D_n <= 4 C_A sqrt(n log n)`,

which is (6.3).

Since each `R_n(q)>=0`,

`lambda_n M_n(lambda_n) <= sum_q R_n(q)`.

Take expectations and use (6.3) to get (6.4). If (6.5) holds, the right side of (6.4) is `o(n)`. Markov's inequality then gives (6.6). The choice `lambda_n=n^(-1/4)` yields (6.7). Finally Jacquet gives `N_n^P>=alpha_P n` with exponentially high probability, so a positive-density set of pattern occurrences remains after removing the `o_P(n)` robust-residual exceptional occurrences. QED.

### Interpretation

For an occurrence traversed from `s` to `t`, telescoping gives

`R_n(q) = T(P_q)+T(t,A_n)-T(s,A_n)`.                       (6.8)

On the pattern event

`4 <= T(P_q) <= 4.04`.                                     (6.9)

Thus `R_n(q)<=lambda` forces

`T(s,A_n)-T(t,A_n) in [4-lambda,4.04]`.                    (6.10)

So under the flat-face contradiction, a positive-density set of explicit backtracking U-segments of the **axis** geodesic must simultaneously be asymptotically calibrated for the **diagonal** target: the diagonal continuation profile drops across that segment by essentially its entire passage cost.

This is much sharper than merely saying that two target policies might sometimes agree. It says that flatness leaves only a concrete co-calibration scenario on linearly many forced nonmonotone geodesic patterns.

It is not yet a contradiction. Undirected geodesics to the diagonal target may themselves contain backtracking segments, and a finite local pattern alone does not forbid a common calibrated segment for two different targets. That is precisely the residual global obstruction.

## 7. A second exact consequence: linear cheap-forward compensation

The same pattern theorem gives a useful unconditional axis-geodesic balance law.

Orient `Gamma_n` from `0` to `C_n`. Let `F_n` be its number of `l1`-toward steps and `B_n` its number of `l1`-away steps. Then

`F_n-B_n=n`.                                               (7.1)

Set `a=mu(e1)>0` and define

`K_n := sum_{e in Gamma_n, e toward C_n} (a-tau_e)_+`.     (7.2)

### P20-FPP-BACKTRACK-COMPENSATION-35 — CANDIDATE_PROVED

Samplewise,

`K_n >= a B_n - [T(0,C_n)-a n]`.                           (7.3)

Consequently there is a constant `beta_P=alpha_P/2>0` such that

`E K_n >= a beta_P n[1-exp(-c_P n)] - C_A sqrt(n log n)`.  (7.4)

Using the retained canonical lower certificate

`a=mu(e1) >= 3002823/10000000`,                            (7.5)

the linear coefficient in (7.4) may be replaced by `(3002823/10000000) beta_P`.

### Proof

Write the passage time centered by the macroscopic axis slope as

`T(0,C_n)-an`
` = sum_{toward}(tau_e-a) + sum_{away}(tau_e+a)`.           (7.6)

For a toward edge,

`tau_e-a >= -(a-tau_e)_+`,

while for an away edge `tau_e+a>=a`. Hence (7.6) gives

`T(0,C_n)-an >= -K_n+aB_n`,

which is (7.3).

Take expectations. The axis mean-convergence bound gives

`0 <= E T(0,C_n)-an <= C_A sqrt(n log n)`,

and Theorem 33 gives the lower bound on `E B_n`. This proves (7.4); (7.5) is the retained canonical exact lower certificate. QED.

This theorem says that the linear true-geodesic backtracking forced by the pattern theorem must be paid for by a linear amount of unusually cheap forward-edge weight along the optimized path. It is a quantitative selection-bias identity, not itself curvature.

## 8. Why the pattern attack does not yet close the defect

This run deliberately tests whether Jacquet's pattern theorem can supply the missing P20 ancestry/disagreement mass. It succeeds only halfway.

**What is now proved.** There are linearly many path-relevant pattern candidates on the true axis geodesic. Under the flatness hypothesis, their aggregate diagonal residual is only `O(sqrt(n log n))`, so a positive-density subfamily must be almost diagonally calibrated.

**What fails.** The U-pattern does not force diagonal noncalibration. The outside continuation profile can make the same U-segment nearly optimal toward `A_n`; indeed Theorem 34 shows that this near-common-calibration is exactly what flatness would have to arrange. The old shared-bypass obstruction therefore reappears in a much more rigid form, rather than disappearing.

A purely finite local pattern cannot by itself decide the sign of the target-dependent continuation offset. Making a larger finite moat does not remove this logical issue without a theorem controlling the continuation profile at the block boundary. Therefore I do **not** claim that Jacquet plus the one-edge residual-clock lemma proves a positive defect.

This is an honest failed recovery of the naive `pattern => disagreement` idea, but it yields the new co-calibration theorem above, so the run is not an unchanged failure and does not trigger a T01--T10 scope switch.

## 9. Coordination with P04 after the canonical source reset

P04's latest width-7, length-4 undirected moving slab proves the genuine dependence-controlled axis construction

`mu(e1) <= 1035580351964689/2000000000000000`

`        = 0.5177901759823445...`,                         (9.1)

with an explicit `O(sqrt N)` endpoint repair. The construction technique is useful, but its reflected-cone consequence is not counted as source progress after the canonical correction in Section 2.

The canonical owner has now rotated the block method to the correct same-quadrant target. It retains the exact lower certificate

`mu(e1) >= b := 3002823/10000000 = 0.3002823`,             (9.2)

so it is enough to prove

`mu(1,1) < 2b = 3002823/5000000 = 0.6005646`.              (9.3)

Its moving-centered diagonal-slab compiler, in rotated coordinates `s=x+y`, `d=x-y`, says that a finite block with expected crossing time `q_{L,W}` and transverse second moment `v_{L,W}` yields

`E T(0,N(L,L)) <= N q_{L,W}+sqrt(N v_{L,W})`,              (9.4)

and therefore

`mu(1,1) <= q_{L,W}/L`.                                    (9.5)

Thus one exact finite block satisfying

`q_{L,W}/L < 0.6005646`                                    (9.6)

would immediately prove `Delta_12>0`.

The P20 handoff to P04 is now more specific than before: augment a diagonal moving-slab frontier state, when feasible, with the **two continuation profiles** for the axis and diagonal targets (or with their normalized difference), and test whether the flatness alternative from Theorem 34 can persist through successive blocks. A block-level rigidity theorem of the following form would close the P20 route:

> if a block contains one of the forced U-pattern crossings and the two frontier continuation profiles are not nearly translates, then that block contributes a definite diagonal residual; if the profiles are nearly translates on almost every forced pattern block, the terminal boundary conditions force an accumulated profile mismatch exceeding the allowed interface error.

The exact quantitative target remains the earlier P20 residual compiler: total certified residual energy only needs to dominate the `sqrt(n log n)` Alexander error. Linear density is more than sufficient.

P20 should not duplicate P04's finite `q_{L,W}` computation. Conversely P04 need not preserve a pristine four-edge star: P20's preceding single-edge residual-clock theorem already shows that one reserved Exp residual clock is enough once a target-policy disagreement is certified.

## 10. Bounded current-literature check

A bounded fresh check was made only for dependencies material to this run.

- Auffinger--Damron--Hanson arXiv:1511.03262 remains the exact source navigation; the ordinary iid Exp(1), undirected nearest-neighbor strict-convexity problem is not closed there.
- Jacquet's pattern theorem, arXiv:2310.04091, proves linear occurrence of any valid pattern along long geodesics with exponentially small exceptional probability in the unbounded-support setting; Exp(1) fits its useful/unbounded hypotheses. This is the external theorem used in Sections 4--7.
- Jacquet's later unrestricted-versus-directed comparison (arXiv:2412.20779) is a different strictness statement and is not imported as a solution here.
- Dembin--Elboim--Peled's quantitative coalescence theorem assumes a nontrivial extreme-point hypothesis on the limit shape and cannot supply the missing geometry without circularity.
- Krishnan's exact HJB/duality variational formula remains conceptually relevant, but no current theorem located in the bounded check turns it into strict convexity for this lattice Exp(1) model.

No novelty claim is made from this bounded search.

## 11. Supporting executed artifact

The supporting exact checker already committed in the current master state is

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T10-37-00Z__backtrack-pattern-rigidity-check.py`

creation commit

`865fc89f262f5559dcefc55d4a31bc67e62fcbcf`.

Its archived executed output is

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T10-37-00Z__backtrack-pattern-rigidity-check.out`

creation commit

`65c662f2c37072ceccfae4952e0f98e1d05096dd`.

The output records

`vertices=6`, `edges=7`, `self_avoiding_u_v_paths=4`,

`desired_upper_cost=4.04`, `competing_lower_cost_min=20.0`,

and ends

`ALL_EXACT_CHECKS_PASS=True`.

The checker is supplementary only; Sections 4--7 contain the general proofs.

## 12. Short handoff of the displaced P20 cyclic-interval proof

The previous P20 source `FOKAM-BITJOKA-2026-CYCLIC-INTERVAL` remains preserved and is not reopened. The source-literal YES proof candidate `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01` and its finite sanity artifact remain on record. P26's full-proof/source-quantifier audit remains PASS. The last recovered certification state still lacked a second genuinely independent audit. No completed certification or novelty claim is implied, and no research time in this run was spent waiting for that audit.

## 13. Residual obstruction and next attack

The residual obstruction is now precise:

> Under `Delta_12=0`, the axis geodesic contains linearly many explicit U-backtracking patterns, yet the total diagonal-target residual across all those pattern segments is only `O(sqrt(n log n))`. Therefore flatness forces positive-density **near-common calibration** of highly nonmonotone local segments for the axis and diagonal targets. The missing theorem is to show that such near-common calibration cannot persist across enough successive dependence-controlled blocks while matching the incompatible terminal continuation profiles.

The next P20 attack should therefore be a **two-profile min-plus block rigidity theorem**, not another local-gap constant improvement and not another reflected cone. In a moving-centered slab, carry normalized continuation profiles `h_C,h_A` on the frontier. For every traversed U-pattern segment `s->t`, the exact identity

`R = T(P)+h_A(t)-h_A(s)`

shows that `R<=lambda` pins the profile difference across its endpoints to the narrow interval `[4-lambda,4.04]`. The goal is to prove that a sequence of such pinned drops either accumulates a positive residual exceeding the `sqrt(n log n)` budget or forces the normalized frontier profiles into a near-translation class incompatible with the final axis/diagonal boundary data. P04's physical-edge slab ownership provides the natural place to make that argument finite-dimensional.

If this two-profile rigidity route fails twice without a demonstrated gain, preserve the present pattern-collapse theorem and switch to another unresolved T01--T10 scope as required by the owner policy.

## 14. Compact ledger_delta

`ledger_delta:`

- `target`: `T10 / ADH_50yearsFPP_Q4::Exp1_Z2_undirected`.
- `original_problem_before`: `c_*=0` for `Delta_12>=c_*`.
- `original_problem_after`: `c_*=0`; full strict convexity OPEN.
- `mechanism_gain_1`: Jacquet valid U-pattern + bounded-overlap proof gives linear `l1`-backtracking density on the **actual** axis geodesic.
- `mechanism_gain_2`: under `Delta_12=0`, aggregate diagonal residual over all those linearly many U-patterns is at most `O(sqrt(n log n))`; robust-residual pattern count obeys `E M_n(lambda)<=4 C_A sqrt(n log n)/lambda`.
- `mechanism_gain_3`: unconditional backtrack-compensation identity forces linear total forward-edge cheapness `E K_n >= a beta_P n-O(sqrt(n log n))`.
- `canonical_correction_consumed`: reflected-cone inequalities are not source-facing movement; first-moment weighted-SAW diagonal route has a hard monotone-path barrier at `c>=0.464`.
- `P04_handoff`: direct source-facing block target is `q_{L,W}/L<0.6005646`; complementary P20 target is a two-profile min-plus rigidity theorem on forced U-pattern blocks.
- `failed_route`: a finite valid pattern alone does not force axis-vs-diagonal policy disagreement; flatness can only be reduced to near-common calibration, not yet contradicted.
- `cyclic_interval_handoff`: proof candidate preserved; P26 audit PASS; second independent audit last known missing; no waiting.
- `next_attack`: two-profile frontier rigidity / near-translation dichotomy with residual accumulation above the Alexander `sqrt(n log n)` scale.
- `status`: `PARTIAL / OPEN`; new claims `CANDIDATE_PROVED pending independent review`.

END OF P20 FPP RUN REPORT
