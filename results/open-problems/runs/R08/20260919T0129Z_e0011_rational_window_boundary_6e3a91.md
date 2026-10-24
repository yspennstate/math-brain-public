Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat >= b12 -> B_cat >= b13 := b12*(p_boot,new/p_boot,old)`, exact gain `>1` with diagnostic `log10(b13/b12)=0.005937578384481549` (about `1.0137656656x`); unchanged count remains `0`. Methods actually used: #7 TAKE THE LIMIT, #13 FIND WHAT ONLY INCREASES, #29 ADD THE POINTS AT INFINITY.**

# R08 CLOSABLE OUTSIDE — rational-window improvement and two structural boundary obstructions

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Active target: **E0011**, Durrett 2009 Problem 5, coexistence in the original two-dimensional no-stirring catalyst/ZGB process.  
Status after this run: **PARTIAL / OPEN_CURRENT_BOUNDED**.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, exclusions, and bounded current-literature check

I continued from the newest complete immutable R08 report

`runs/R08/20260919T0043Z_e0011_one_column_seed_31b7e4.md`

rather than restarting from the stale scheduler title.

Before research I refreshed the current campaign material relevant to this track: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0082.md`, `operations/claims/E0011.md`, the newest own R08 report and its exact checkers, and current neighboring R07/R09 reports. I also searched the intake/claim state for the exact E0011/Durrett target rather than treating a missing global rendering as permission to restart.

The canonical state remains:

- I0082 / Hasebe--Ueda Problem 3.11 is **RETIRED/FROZEN at `2/3` after six supported unchanged runs**, with its immutable handoff preserved. It is not reopened here.
- E0011 remains exclusively owned by R08; I found no competing current owner.
- The old R08 FPP strict-convexity route remains retired from this slot.
- Posted Problem 3.3 and R19's classical-convolution stable-law track remain distinct exclusions.

The frozen E0011 metric is

\[
B_{\rm cat}:=\sup\{b:\text{R08 has a rigorous finite 1-dependent two-child Harris-block event of probability at least }b\text{ at }p=1/2\}.
\]

Entering value:

\[
B_{\rm cat}\ge b_{12},
\qquad
\log_{10}b_{12}\approx-50.31603524108792.
\]

On 2026-09-19 UTC I re-ran bounded source/current-literature searches for the exact no-stirring target and aliases, including combinations of `Rick Durrett`, `Problem 5`, `catalyst`, `ZGB`, `coexistence`, `no stirring`, and 2025--2026 date terms. The searches recovered Durrett's original open-problem source and the known simulation / fast-stirring / modified-model literature, but I found no later primary theorem settling the precise original no-stirring Problem 5. This is **bounded negative evidence only**, not an exhaustive worldwide novelty certificate.

## 2. Idea before code — B7: let the first deterministic window approach its continuous optimum

The previous one-column certificate used a first-stage Poisson mean `lambda=4`, chosen from the integer scan `1,...,8`. The local killed-chain object is continuous in the deterministic-window length, so the integer restriction was artificial.

Keep the exact same one-column initial class, ten-label local alphabet, stage hazard `D=140`, eight-arrival truncation, geometry, later stages, and 1-dependence proof. Let

\[
H=36D=5040
\]

and let `A_n(s)` be the exact integer reaction-weight mass of successful length-`n` local histories from descriptor `s`, using the normalization already certified in the preceding run. For an arbitrary rational Poisson mean `lambda>0`, the deterministic-window success subevent is

\[
q_s(\lambda)
=e^{-\lambda}\sum_{n=0}^{8}\frac{\lambda^n}{n!}\frac{A_n(s)}{H^n}.
\tag{2.1}
\]

I first searched the continuous parameter numerically only to locate a promising rational point, then certified the selected point exactly. The rational choice is

\[
\boxed{\lambda_*=\frac{87}{20}=4.35.}
\]

The exact common-denominator minimization of the polynomial part of (2.1) over all

\[
215383\text{ stable full configurations}\longrightarrow48027\text{ projected descriptors}
\]

gives the minimum integer numerator

\[
\boxed{
M_*=
170968026884070092322809508339561725952
}
\]

at the archived worst descriptor `4782752`.

## 3. Exact exponential lower bound at lambda=87/20

To keep the whole certificate rational, write

\[
e^{-87/20}=e^{-4}e^{-7/20}.
\]

The earlier certified bound gives

\[
e^{-1}>\frac{32}{87},
\qquad	ext{hence}\qquad
e^{-4}>\left(\frac{32}{87}\right)^4.
\tag{3.1}
\]

For `x=7/20`, the alternating Taylor series for `e^{-x}` has monotonically decreasing term magnitudes. Therefore the odd truncation is a lower bound:

\[
e^{-7/20}>
\sum_{k=0}^{7}\frac{(-7/20)^k}{k!}
=oxed{\frac{649440538531}{921600000000}}.
\tag{3.2}
\]

Combining the exact minimized polynomial with (3.1)--(3.2) yields the source-valid first-stage lower bound

\[
\boxed{
p_{\rm boot,new}
=
\frac{
123539713657298039111724857042855116928492053
}{
24075437167336631152925319821710205078125000000000000
}.
}
\tag{3.3}
\]

The old first-stage factor was

\[
p_{\rm boot,old}
=
\frac{449855540637605888}
{88875222725965541291015625}.
\tag{3.4}
\]

Exact cross multiplication gives

\[
\boxed{
\frac{p_{\rm boot,new}}{p_{\rm boot,old}}
=
\frac{
34717319668318843590202198742697856944700233990464479
}{
34245904058199771001461521651828906250000000000000000
}>1.
}
\tag{3.5}
\]

Numerically only for scale,

\[
\frac{p_{\rm boot,new}}{p_{\rm boot,old}}
\approx1.01376566562929593,
\qquad
\log_{10}\frac{p_{\rm boot,new}}{p_{\rm boot,old}}
\approx0.005937578384481549.
\]

No later stage, spatial support, seed, dependency family, or block implication changes. Thus define

\[
\boxed{
b_{13}:=b_{12}\frac{p_{\rm boot,new}}{p_{\rm boot,old}}.}
\tag{3.6}
\]

Then exact arithmetic proves

\[
\boxed{B_{\rm cat}\ge b_{13}>b_{12}.}
\]

For diagnostic scale,

\[
\boxed{\log_{10}b_{13}\approx-50.31009766270344.}
\]

This is real metric movement, but it is still astronomically below the sufficient `63/64` block threshold. No coexistence theorem is claimed.

The finite exact claim is self-checked by

`artifacts/R08/20260919T0129Z_e0011_rational_window_check.cpp`

with archived output

`artifacts/R08/20260919T0129Z_e0011_rational_window_check.out`.

The checker independently re-enumerates the 215383 full stable states and 48027 descriptors, reconstructs the ten-label recursion through eight arrivals, performs the exact rational evaluation at `87/20`, and verifies the strict gain by integer cross multiplication.

## 4. B13: a forward-invariant trap kills the naive one-vacancy bootstrap in the maximal frozen patch

The next natural deformation is to weaken the seed further from one guaranteed empty column to a single guaranteed vacancy. Rather than assume that more accepted arrivals would eventually repair every exterior, I searched for a state class that can never escape.

Freeze the 16-cell local patch

\[
\begin{aligned}
S=\{&(-2,0),(-2,1),(-1,-1),(-1,0),(-1,1),(-1,2),\\
&(0,-1),(0,0),(0,1),(0,2),(1,-1),(1,0),(1,1),(1,2),(2,0),(2,1)\}.
\end{aligned}
\]

Enumerating **every** square-lattice CO root and every nearest-neighbor O2 edge whose complete adsorption/reaction support is contained in this patch gives exactly

\[
\boxed{13\text{ support-preserving labels}=6\text{ CO}+7\text{ O2}.}
\]

Thus this is the maximal local alphabet for this frozen patch, not a hand-selected subset.

For the stable ternary state encoded by

\[
\boxed{s_{\rm trap}=5513529}
\]

with the designated seed site `(-1,0)` vacant, exact BFS over **all 13 labels and every instantaneous reaction branch** finds a forward-invariant reachable class of exactly

\[
\boxed{6\text{ states}.}
\]

None of the six states has the target six-site vacancy rectangle

\[
\{-1,0,1\}\times\{0,1\}.
\]

Hence:

> Within this exact 16-cell patch and its maximal support-preserving adsorption alphabet, the one-vacancy bootstrap has an admissible stable exterior from which the target is unreachable even with an arbitrarily long accepted local history.

This is a **route obstruction, not a source-level impossibility theorem**. A larger patch, a different seed geometry, or a different protected event could still succeed. The point is that merely sending the current local-history budget to infinity cannot repair this deformation.

The closed-class claim is certified in

`artifacts/R08/20260919T0129Z_e0011_structural_limit_check.py`

and its archived PASS output.

## 5. B29: the sole L=7 shared edge is a genuine semantic boundary variable

The preceding run reduced the spacing-eight construction to a literal distance-two disjoint dependency family. Pushing the same one-column geometry to spacing `L=7` leaves no shared CO clock and exactly one shared O2 edge between distance-two blocks:

\[
\boxed{e_7=\{(8,1),(9,1)\}.}
\tag{5.1}
\]

A tempting boundary compactification is to regard this edge as an irrelevant point-at-infinity and omit it from one block's sigma-field. I tested that idea directly.

In terminal-stage local coordinates, take a stable state having CO only at

\[
(-1,2),\qquad(1,1),
\]

with the generated trailing target rows otherwise vacant as required. Consider the controlled accepted O2 mark on

\[
((-1,1),(0,1)).
\]

Without the shared boundary edge firing first, each newly adsorbed O has a unique CO reaction partner; both reactions occur and the six-site target is vacant. If the boundary O2 edge corresponding to `e_7`, locally `((2,1),(3,1))`, fires first, its O at `(2,1)` uniquely consumes the CO at `(1,1)`. The subsequent controlled O2 mark then leaves an O at the target site `(0,1)`, and the target event fails.

Thus the single L=7 overlap is **not semantically dead for the current terminal event**. It cannot simply be deleted from the dependency cone by the same argument that worked for the older spacing-eight coarse overlap.

Again, the scope is limited: this does **not** prove `L=7` impossible. It proves only that the current event cannot cross the spacing-seven boundary by naive omission of the one shared edge. A redesigned robust terminal event could still neutralize it.

The exact witness is included in

`artifacts/R08/20260919T0129Z_e0011_structural_limit_check.py`,

whose archived output records

- `L7_shared_CO=[]`;
- `L7_shared_edges=[((8,1),(9,1))]`;
- target succeeds without the edge history;
- target fails with the edge history, leaving O at `(0,1)`.

## 6. What the three methods actually accomplished

**B7 TAKE THE LIMIT — succeeded quantitatively.** Treating the deterministic-window mean as a genuine continuous parameter rather than an integer scan moved the rigorous first-stage factor. The exact rational point `87/20` improves the full block certificate by about 1.38%.

**B13 FIND WHAT ONLY INCREASES — the scalar-monovariant hope failed, but the route produced a stronger finite obstruction.** The single-vacancy deformation has a six-state forward-invariant trap under the maximal support-preserving 16-cell alphabet, so infinite accepted-arrival budget alone cannot save that route.

**B29 ADD THE POINTS AT INFINITY — failed as a direct spacing-seven fix, with an exact reason.** The one L=7 shared edge is not a harmless boundary artifact: an explicit legal local history changes a terminal success into failure.

This is the desired type of failure information: both negative results identify what a successful redesign must change rather than merely reporting that a numerical search did not work.

## 7. Remaining obstruction and next route

The current block lower bound is still on the scale `10^-50`. Further one-dimensional tuning of the existing deterministic windows cannot plausibly bridge that gap. The two new obstructions suggest that the next useful object is a **robust terminal policy** that treats the L=7 shared edge as an explicit adversarial/environmental input rather than insisting that it be absent.

The next nonrepeating method triple is:

- **B1 CHANGE THE CATEGORY:** formulate the terminal-stage problem as a finite reachability game / controlled automaton whose environment move is the shared boundary-edge clock;
- **B19 MAKE IT AN ALGORITHM:** solve for a boundary-edge-robust accepted policy or word family that reaches the target from every generated shield state;
- **B27 SWAP THE QUANTIFIERS:** distinguish `one fixed local history works for every boundary-edge timing` from `for every boundary-edge timing there exists a certified local response`, and determine which stronger uniform policy is actually needed for a source-valid block event.

A success there could validate spacing seven or a multitype block construction. A failure with a finite game certificate would be a real obstruction theorem for the current seed/event family.

## 8. Model / scheduler-control status

The exposed scheduled-task control surface still has **no binding model-family selector and no reasoning-effort selector**, and I found no authenticated completed-run telemetry that could certify GPT-6/maximum. Therefore GPT-6 maximum remains prompt text only; this report honestly identifies the actual runtime as GPT-5.6 Sol with reasoning level UNVERIFIED.

Changing this requires a platform/scheduler capability that binds model family and reasoning effort to the task. The historical P26 `You cannot modify this task` failure remains authorization-context-specific: a later update succeeded from an authorized P/C context. For a task that still refuses modification, the legitimate workaround is the authorized owning context, a supported ownership/admin transfer, or platform support. I made no scheduler changes in this run.

## 9. Structured ledger delta

```yaml
ledger_delta:
  worker: R08
  allocation: CLOSABLE_OUTSIDE
  source: "Rick Durrett, Coexistence in stochastic spatial models (2009), Problem 5"
  active_target: E0011_Durrett_Problem_5_no_stirring_catalyst
  predecessor_I0082: RETIRED_FROZEN_2_of_3
  metric: B_cat
  before: ">= b12"
  after: ">= b13 = b12 * (p_boot_new/p_boot_old)"
  exact_movement: true
  exact_gain: "34717319668318843590202198742697856944700233990464479 / 34245904058199771001461521651828906250000000000000000"
  diagnostic_log10_before: -50.31603524108792
  diagnostic_log10_after: -50.31009766270344
  unchanged_count: 0
  status: PARTIAL
  methods_tried: [B7, B13, B29]
  remaining_obligation: "Raise a source-valid finite 1-dependent two-child block probability above 63/64 and complete the comparison/continuity argument; current explicit certificate remains about 10^-50.31."
  evidence:
    - artifacts/R08/20260919T0129Z_e0011_rational_window_check.cpp
    - artifacts/R08/20260919T0129Z_e0011_rational_window_check.out
    - artifacts/R08/20260919T0129Z_e0011_structural_limit_check.py
    - artifacts/R08/20260919T0129Z_e0011_structural_limit_check.out
  audits: []
  next_methods: [B1, B19, B27]
```

The exact checkers above are **self-checks**, not independent audits. No closure status is claimed.
