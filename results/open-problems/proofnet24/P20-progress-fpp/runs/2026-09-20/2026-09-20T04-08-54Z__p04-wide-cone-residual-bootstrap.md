Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. SOURCE MILESTONE `c_*` REMAINS `0 -> 0`, but this run converts P04's new wide-cone theorem into an explicit finite-target Bellman-residual lower bound and enlarges the proved strict-triangle scope from exactly symmetric wide-cone pairs to an open asymmetric family with fully controlled finite-scale error.**

# P20 T10 — bootstrapping P04's wide-cone defect into an asymmetric Bellman-residual family

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent claim: `operations/claims/PROB10-10.md`; ownership remains with the native PROB10-10 lane. P20 is the complementary LIVE20 Busemann/variational route.  
Model: nearest-neighbor **undirected** FPP on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for full strict convexity. The theorem below is a complete corollary of the newest P04 theorem plus standard time-constant/Bellman identities; it is pending later independent review together with that P04 dependency.

## 1. Exact source, progress contract, and before/after

The outside source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262v2, Question 4: strict convexity of the FPP limit shape for continuous passage-time laws. P20 continues only the source-valid specialization to iid `Exp(1)` nearest-neighbor **undirected** edge weights on `Z^2`. Directed integrable models and sampled numerical curvature are not substituted for this target.

The canonical first directional milestone remains

\[
\Delta_{12}=2\mu(e_1)-\mu(1,1),
\qquad
c_*:=\sup\{c\ge0:\Delta_{12}\ge c\text{ is rigorously proved in this track}\}.
\]

Before this run: `c_*=0`.  
After this run: `c_*=0`.

So the frozen axis/diagonal milestone has **no movement**. The original full ADH problem also remains open.

There is nevertheless source-valid directional movement. The newest P04 companion report proves a positive strict-triangle defect only for symmetric pairs `(x,y),(x,-y)` in the wide cone `|y|>=2x`. This run enlarges that to a genuine open four-parameter family of **asymmetric** opposing-cone pairs and, more importantly for the P20 route, proves a finite-target Bellman-residual lower bound with an explicit exponentially decaying error. An explicit asymmetric integer pair already has a rigorously positive finite expected residual at scale `n=24`.

This is a demonstrated mechanism gain, not a claim of full strict convexity.

## 2. Essential state consumed; prior failures preserved

I read only the dependencies needed for the present argument:

- owner policy `operations/PROGRESS20_2026-09-20.md`;
- canonical parent claim `operations/claims/PROB10-10.md`;
- newest P20 report `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T03-10-00Z__two-terminal-jensen-semigroup.md`;
- newest P04 companion report `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T03-46-21Z__wide-cone-strict-triangle.md`;
- newest native PROB10-10 report `runs/prob10_2026-09-20/PROB10-10/20260920T0218Z__frontier-carry-synchronization-obstruction.md`;
- the exact P04 checker for its rational constants.

The historical R08 failures remain binding and are not reset:

1. local deletion savings may all share one bypass, so independent multiplication of local margins is invalid;
2. finite pointwise strict triangle saving fails on positive-probability cylinder events;
3. old fixed-corner blocks did not reach the axis/diagonal threshold;
4. fluctuation/KPZ results do not imply curvature.

The newest P20 report already avoids (1) algebraically by min-plus Jensen accumulation, but its missing input is an exact/controlled factorization through unrestricted undirected asynchronous blocks. This run does not pretend that factorization is solved. Instead it uses P04's independently proved block-to-infinite-volume inequalities as a rigorous macroscopic input and translates them into the finite-target residual language P20 needs.

## 3. New P04 input actually available now

The P04 report `2026-09-20T03-46-21Z__wide-cone-strict-triangle.md` is the first substantive T10 report under `proofnet24/P04-progress-curvature`. It proves, for

\[
A_0:=
\frac{127596793342690034600361684870097}
{197703921604834678505472000000000}
=0.6453933351799015\ldots,
\tag{3.1}
\]

that

\[
\mu(e_1)\le A_0,
\tag{3.2}
\]

and for every real `x>=0`, `|y|>=2x`,

\[
\mu(x,y)\ge \frac23x.
\tag{3.3}
\]

For integer `a>=1`, `b>=2a`, the same report gives the finite lower-tail estimate

\[
\mathbb P\!\left(T(0,n(a,b))\le \frac23 an\right)
\le C_0\,\beta_+^{an},
\tag{3.4}
\]

where

\[
C_0=\frac{27865448}{206955},
\qquad
\beta_+=
\frac{713425217726611388616507115106921327}
{740604339057582092285156250000000000}
<0.963302<1.
\tag{3.5}
\]

It also proves the exact expectation transfer

\[
\mathbb E T(0,6Ne_1)\le 6N A_0
\qquad(N\ge1),
\tag{3.6}
\]

with no independence assumption between translated ladder blocks. By `D_4` symmetry the same holds on the vertical axis.

P04 combines (3.2)--(3.3) only for symmetric pairs `(x,y),(x,-y)`. The next section extracts more directional scope from exactly the same certified constants.

## 4. New asymmetric strict-triangle theorem

Put

\[
G_0:=\frac23-A_0
=
\frac{4205821060533084403286315129903}
{197703921604834678505472000000000}
=0.02127333148676518\ldots>0,
\tag{4.1}
\]

and

\[
\eta_0:=\frac{G_0}{A_0}
=
\frac{4205821060533084403286315129903}
{127596793342690034600361684870097}
=0.03296180844637217\ldots .
\tag{4.2}
\]

### P20-FPP-WIDE-CONE-TRANSVERSE-MISMATCH-15

**Claim: CANDIDATE_PROVED, dependent on P04-T10-WIDE-CONE-STRICT-TRIANGLE-01.**

Let

\[
u=(a,b),\qquad v=(c,-d)
\]

with real `a,c>0`, `b>=2a`, and `d>=2c`. Write

\[
X=a+c,
\qquad H=|b-d|.
\]

Then

\[
\boxed{
\mu(u)+\mu(v)-\mu(u+v)
\ge
\kappa(u,v):=G_0X-A_0H.
}
\tag{4.3}
\]

Consequently every pair satisfying

\[
\boxed{H<\eta_0X}
\tag{4.4}
\]

has a strictly positive directional triangle defect. The same conclusion holds for all simultaneous `D_4` images.

This strictly enlarges P04's symmetric family: P04 corresponds to `a=c` and `b=d`, whereas (4.3) permits both unequal horizontal components and unequal transverse magnitudes.

#### Proof

By the P04 cone lower bound (3.3),

\[
\mu(u)\ge \frac23a,
\qquad
\mu(v)=\mu(c,d)\ge\frac23c.
\tag{4.5}
\]

The sum is

\[
u+v=(X,b-d).
\]

From (3.2), square-lattice symmetry, positive homogeneity, and the triangle inequality,

\[
\mu(X,b-d)
\le X\mu(e_1)+H\mu(e_2)
\le A_0(X+H).
\tag{4.6}
\]

Subtracting (4.6) from (4.5) gives

\[
\begin{aligned}
\mu(u)+\mu(v)-\mu(u+v)
&\ge \frac23X-A_0(X+H)\\
&=(\tfrac23-A_0)X-A_0H\\
&=G_0X-A_0H.
\end{aligned}
\]

If `H<eta_0 X=G_0X/A_0`, this lower bound is strictly positive. QED.

### Explicit asymmetric source-valid pair

Take

\[
u=(16,33),
\qquad v=(15,-32).
\tag{4.7}
\]

Both vectors satisfy the P04 cone hypotheses because `33>=32` and `32>=30`, while

\[
X=31,
\qquad H=1.
\]

The exact lower bound is

\[
\boxed{
\mu(16,33)+\mu(15,-32)-\mu(31,1)
\ge
\frac{86989360432361934422315129903}
{6178247550151083703296000000000}
=0.01407994090981911\ldots>0.
}
\tag{4.8}
\]

This pair is not of P04's symmetric form. Thus the proved strict-triangle scope has genuinely expanded, although it remains far from full strict convexity.

## 5. Finite-target Bellman-residual theorem with controlled error

The P20 route is based on nonnegative finite-target Bellman residuals. For a target `z`, define on an oriented physical edge `(x,y)`

\[
r_z(x,y):=\tau_{xy}+T(y,z)-T(x,z)\ge0.
\tag{5.1}
\]

Let now `a,b,c,d` be positive integers satisfying the hypotheses of Section 4. For an integer scale `n`, set

\[
A_n=n(a,b),
\qquad
Z_n=n(a+c,b-d).
\tag{5.2}
\]

Let `Gamma_n` be the unique `0`-to-`A_n` geodesic (uniqueness holds almost surely for continuous iid weights), and define its target-`Z_n` residual energy

\[
\mathcal R_n:=\sum_{e\in\Gamma_n}r_{Z_n}(e).
\tag{5.3}
\]

Telescoping gives the exact samplewise identity

\[
\boxed{
\mathcal R_n
=T(0,A_n)+T(A_n,Z_n)-T(0,Z_n).
}
\tag{5.4}
\]

This is the general finite-corner identity already used by P20, now applied in a regime where P04 supplies quantitative endpoint estimates.

### P20-FPP-FINITE-WIDE-CONE-RESIDUAL-16

**Claim: CANDIDATE_PROVED, dependent on the P04 finite estimates.**

For every integer `n` divisible by `6`,

\[
\boxed{
\frac{\mathbb E\mathcal R_n}{n}
\ge
\kappa(u,v)-\varepsilon_n,
}
\tag{5.5}
\]

where

\[
\varepsilon_n
:=\frac23 C_0
\left[a\beta_+^{an}+c\beta_+^{cn}\right].
\tag{5.6}
\]

In particular `epsilon_n` decays exponentially, and whenever `kappa(u,v)>0`, the finite expected Bellman residual is positive for all sufficiently large multiples of six.

#### Proof

From the P04 tail estimate (3.4) and nonnegativity of passage times,

\[
\begin{aligned}
\mathbb E T(0,n(a,b))
&\ge \frac23an\,\mathbb P\!\left(T(0,n(a,b))>\frac23an\right)\\
&\ge \frac23an\left(1-C_0\beta_+^{an}\right).
\end{aligned}
\tag{5.7}
\]

By reflection the same argument gives

\[
\mathbb E T(0,n(c,-d))
\ge \frac23cn\left(1-C_0\beta_+^{cn}\right).
\tag{5.8}
\]

Translation invariance identifies

\[
\mathbb E T(A_n,Z_n)=\mathbb E T(0,n(c,-d)).
\tag{5.9}
\]

For the sum endpoint `Z_n=n(X,b-d)`, use a fixed intermediate coordinate-axis corner. Because `n` is divisible by six, both `nX` and `nH` are multiples of six. The exact P04 expectation transfer (3.6), its vertical-axis image, translation invariance, and the triangle inequality give

\[
\mathbb E T(0,Z_n)
\le A_0 nX+A_0 nH
=A_0n(X+H).
\tag{5.10}
\]

Insert (5.7)--(5.10) into the exact residual identity (5.4). The main terms combine to

\[
\frac23n(a+c)-A_0n(X+H)=n\kappa(u,v),
\]

and the two lower-tail losses are exactly `n epsilon_n`. This proves (5.5). QED.

### Exact finite positive residual for the asymmetric example

For `(a,b,c,d)=(16,33,15,32)` and `n=24`, the executed exact-rational checker verifies

\[
\varepsilon_{24}=0.002756669762045304\ldots
<
\kappa=0.01407994090981911\ldots .
\]

Therefore

\[
\boxed{
\mathbb E\mathcal R_{24}
>0.2717585075465713.
}
\tag{5.11}
\]

The displayed decimal is only a rendering of an exact rational comparison performed by the checker. This is not sampled numerical curvature.

## 6. Why this is a Busemann/variational mechanism gain rather than only another norm inequality

Equation (5.4) rewrites the strict triangle defect as accumulated nonnegative **Bellman slack** against the competing terminal `Z_n`. The new content is that P04's block-to-infinite-volume estimates force a linear amount of this residual energy on an explicit open family:

\[
\liminf_{n\to\infty,\ 6\mid n}
\frac{\mathbb E\mathcal R_n}{n}
\ge \kappa(u,v)>0.
\tag{6.1}
\]

Thus the finite-target analogue of a Busemann residual has a strictly positive directional density with an explicit finite error. No stationary Busemann limit, coalescence hypothesis, directed model, or curvature simulation is required.

This is useful for P20's preceding min-plus program in two ways.

1. It provides the first **positive macroscopic calibration case** for the residual/Jensen machinery in this T10 assignment. Any proposed asynchronous block factorization should be able to recover a positive fraction of (6.1) on this family before being trusted on the unresolved axis/diagonal pair.
2. It separates the factorization problem from the local-strictness problem. Here the macroscopic residual is already known to be positive from P04; if a finite-state quotient/block scheme produces zero accumulated Jensen mass, that failure measures information lost by the compression rather than absence of curvature in the true model.

The historical shared-bypass obstruction is therefore not contradicted: (5.5) is an expectation-level global residual estimate assembled from independent upper/lower time-constant transfers, not a multiplication of local surgeries.

## 7. Generic P20 -> P04 asymmetric-cone compiler

The preceding argument abstracts cleanly. Suppose a companion block theorem supplies constants `L>A>0` such that

\[
\mu(x,y)\ge Lx
\qquad\text{on } |y|\ge \sigma x,
\tag{7.1}
\]

and

\[
\mu(e_1)\le A.
\tag{7.2}
\]

Then for opposing-cone vectors `u=(a,b)`, `v=(c,-d)` with `b>=sigma a`, `d>=sigma c`,

\[
\boxed{
\mu(u)+\mu(v)-\mu(u+v)
\ge (L-A)(a+c)-A|b-d|.
}
\tag{7.3}
\]

Hence the allowed transverse mismatch is

\[
\boxed{
\frac{|b-d|}{a+c}<\frac{L-A}{A}.
}
\tag{7.4}
\]

This gives P04 an immediately measurable payoff for every future block improvement:

- improving the cone lower coefficient `L` widens the asymmetric strictness band;
- improving the coordinate upper bound `A` also widens the band;
- reducing the cone aperture `sigma` enlarges the set of directions to which the compiler applies.

For the current P04 theorem, `L=2/3`, `A=A_0`, `sigma=2`, and (7.4) is exactly `H/X<eta_0`.

The finite-error version is equally modular: any lower-tail error for the two opposing cone legs and any expectation upper-transfer error for the coordinate sum leg enter additively in (5.5). This is the precise P20/P04 coordination interface produced in this run.

## 8. What remains unresolved

The full ADH target is still far away.

1. `Delta_12=2mu(e1)-mu(1,1)` remains unresolved, so `c_*=0`.
2. The new family consists of opposing wide-cone vectors whose transverse components nearly cancel. It does not yet reach nearby directions in the same quadrant, which are central to strict convexity.
3. P20's quotient-state drift problem from the preceding report is still open for the axis/diagonal terminals. This run gives it a positive calibration family, not the missing drift theorem.
4. P04's current cone aperture `sigma=2` is deliberately coarse. P04 itself identifies reducing that aperture by optimizing the non-backtracking tilt, Chernoff parameter, Collatz vector and finite ladder as the next block objective.

The important failure diagnosis is now quantitative: the obstacle is no longer proving *some* source-valid strict triangle inequality—the P04/P20 combination now has an open asymmetric family with finite residual control. The obstacle is transporting strictness into the first-quadrant/nearby-direction geometry without an uncontrolled asynchronous reentry loss.

## 9. Next attack

The next P20 attack should use the new positive family as a **calibration problem for the quotient-state/Jensen semigroup**, rather than improving a local Exp constant again.

Concrete target:

1. choose the explicit pair `(16,33),(15,-32)` (or a smaller-rational nearby pair after scaling) and terminalize the two-target min-plus semigroup from the preceding P20 report;
2. construct the simplest unrestricted-undirected asynchronous band decomposition for which the exact block operator can still be written without orientation assumptions;
3. compare its accumulated Jensen gap plus interface/reentry error against the known macroscopic budget `kappa=0.01407994...`;
4. if the compiler loses all of this known residual, identify the exact state variable responsible and enlarge the quotient state only there;
5. once a controlled factorization recovers a positive fraction on the calibration family, move the same state representation continuously toward the unresolved axis/diagonal terminals.

This is a materially sharper test than working blind on `Delta_12`: there is now a rigorous positive answer against which every proposed P20/P04 compression can be falsified.

If this calibration route and one further materially different recovery both fail without mechanism gain, the owner policy's two-failed-recovery scope-switch rule will apply. That trigger has not fired because this run proves new source-valid directional scope and a finite residual estimate.

## 10. Exact artifact

Executed exact-rational checker:

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T04-08-54Z__wide-cone-residual-bootstrap.py`

creation commit `fdea13652e57b3eb5bf5d77376c74d54c49bdb03`.

Archived executed stdout:

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T04-08-54Z__wide-cone-residual-bootstrap.out`

creation commit `d4ed161c5c817dca5cb270ff3ab0df8d7e16b3c1`.

The output verifies exactly:

- the P04 rational `A_0`, `G_0`, `delta_0` and `eta_0` values;
- the asymmetric example hypotheses;
- exact positivity of `kappa`;
- `beta_+<1`;
- at `n=24`, the exact inequality `epsilon_24<kappa` and hence positivity of the finite expected residual lower bound.

It ends `ALL_EXACT_CHECKS_PASS`. No Monte Carlo or sampled curvature is used.

## 11. Fresh literature/source boundary

A bounded 20 September 2026 recheck again found no source-matching theorem proving strict convexity for ordinary iid `Exp(1)` nearest-neighbor undirected FPP on `Z^2`. Auffinger--Damron--Hanson arXiv:1511.03262 remains the exact source navigation. Recent search results still separate the target from different models/results: 2026 Brochette FPP has line-correlated weights and an `L^1` diamond; Haßler's `1+1` model has deterministic vertical weights; Dembin--Elboim--Peled's quantitative planar coalescence uses nontrivial limit-shape extreme-point hypotheses. Search misses are bounded negative evidence only; no priority or publication-novelty claim is made.

## 12. Short cyclic-interval handoff

The displaced P20 source `FOKAM-BITJOKA-2026-CYCLIC-INTERVAL` remains preserved and is not reopened. Its source-literal YES proof candidate remains intact, the supplementary exact checker remains PASS, and P26's full-proof/source-quantifier audit remains PASS. The last recovered independent-audit count remains `1/2`; the second distinct audit was missing. No completed campaign certification or publication-novelty claim is implied, and this run spent no research time waiting for that audit.

## 13. Before/after and ledger

| Quantity | Before | After | Meaning |
|---|---:|---:|---|
| full ADH strict convexity | OPEN | OPEN | unresolved |
| canonical axis/diagonal `c_*` | `0` | `0` | no movement |
| P04 strict pair scope consumed by P20 | symmetric wide-cone pairs | asymmetric open transverse-mismatch family | proved conditional corollary |
| finite positive Bellman residual from block theorem | none in an actual positive-defect family | explicit `E R_n/n >= kappa-epsilon_n` | new controlled-error mechanism |
| explicit asymmetric finite example | none | `(16,33),(15,-32)`, positive already at `n=24` in expectation | exact rational check |

### ledger_delta

```text
P20 / T10 / ADH_Q4_EXP1_Z2_UNDIRECTED
source_metric: c_* = 0 -> 0 (axis/diagonal still OPEN)
new_directional_scope: P04 symmetric wide-cone strict pairs -> open asymmetric family u=(a,b), v=(c,-d), b>=2a, d>=2c, |b-d| < eta_0(a+c), eta_0=4205821060533084403286315129903/127596793342690034600361684870097
new_candidate_proved: P20-FPP-WIDE-CONE-TRANSVERSE-MISMATCH-15 (dependency: P04-T10-WIDE-CONE-STRICT-TRIANGLE-01)
new_candidate_proved: P20-FPP-FINITE-WIDE-CONE-RESIDUAL-16 (explicit finite Bellman residual error)
explicit_pair: (16,33)+(15,-32) -> (31,1), defect >= 86989360432361934422315129903/6178247550151083703296000000000 = 0.01407994090981911...
finite_calibration: n=24, E[corner residual] > 0.2717585075465713 by exact-rational error comparison
mechanism_gain: P04 block-to-infinite bounds compiled into a finite-target nonnegative Bellman-residual density; generic asymmetric-cone compiler (L-A)X-AH
residual_obstruction: transport strictness toward same-quadrant/axis-diagonal directions through unrestricted asynchronous block/reentry geometry
next_attack: calibrate P20 quotient-state/Jensen block factorization on the explicit positive wide-cone residual family before moving it toward axis/diagonal terminals
cyclic_interval_handoff: proof candidate preserved; P26 audit PASS; last audit gate 1/2; no closure claim; no waiting
parent_claim: operations/claims/PROB10-10.md unchanged
shared_POSTED_RESULTS_QUEUE: untouched
```

No historical or peer file was overwritten. No shared claim/POSTED ledger, email, Drive object, public post, workflow, permission, paid compute, access setting, or schedule was changed.

END OF P20 FPP RUN REPORT
