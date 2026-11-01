Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum, and I do not claim otherwise.

# C27 — Tóth interchange, fixed-prefix macroscopic fresh handoff

**NO MOVEMENT on the frozen metric.** The supported block/leakage exponent remains

\[
\boxed{\theta_{\rm block}=\frac12+\frac{1}{16e\log 2}=0.5331711153389402\ldots}
\]

before and after this run. The raw unchanged-run count is `4 -> 5`; the historical stuck-recovery count remains `2`. This run executed the one recovery action selected by `2026-09-16T20-24-20Z__stuck-recovery-2.md`: attack the simplest two-successive-fresh-guard case. It produces a new analytic PARTIAL theorem but does not move `theta_block`, does not give a source-level numerical `beta_0`, and does not prove any macroscopic-cycle statement. Because the hard target has already used two stuck recoveries and the frozen metric remains unchanged, **the next C27 invocation is not allowed to run STUCK RECOVERY 3 on this target: it must switch and leave/use a handoff.**

Section-B moves used here, all different from the most recent C27 triples, are:

- **10 — DERANDOMIZE.** Replace an adaptive search for a lucky phase by one deterministic prefix interval chosen before any orbit information is read.
- **12 — FIND WHAT IS CONSERVED.** Track the conserved resource: untouched Poisson increments in spatial tubes of that deterministic prefix remain exactly fresh after conditioning on the complementary-time map and after earlier disjoint tube exposures.
- **27 — SWAP THE QUANTIFIERS.** Fix the time guard first, then discover the orbit anchors sequentially. The reverse-looking idea “discover a phase anchor and then call the phase fresh” is anticipative and is explicitly rejected below.

Status remains **PARTIAL / source conjecture OPEN**.

---

## 1. Continuity, whole-repository read, and metric reconciliation

This run read the current campaign surfaces (`probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`), the newest C27 report, the newest neighboring HARD10-03 material, the newest C28 report, and relevant C27/HARD10 attempt history before doing new mathematics. The root ledger is stale for C27 and was not used to reset any proved quantity.

The owner's `203/500` reference has already been located in the `NEW-L96/97` line. It is genuinely the same metric: the same block-visitation event

\[
\mathcal V(\mathcal B)=\{C_{\pi_\beta}(0)\subseteq\cup_iB_i,\ C_{\pi_\beta}(0)\cap B_i\neq\varnothing\ \forall i\},
\]

the same cross-heat hypothesis

\[
\mathcal H_\beta(\mathcal B)\le \frac{k-1}{4e},
\]

and the same scale conversion

\[
r(L)=\max\{2326,\lceil\log_2L/500\rceil\},\qquad k(L)=500r(L)+1.
\]

Thus `203/500` is not differently normalized; it is a valid older lower bound superseded first by `0.472361...` and then by the currently supported `0.5331711153389402...`. No supported improvement is erased.

The retired DLA route remains retired. No once-reinforced-walk restart is made.

---

## 2. Source gate — exact quantifiers remain fixed

The current Ioffe--Tóth source (current arXiv text dated 22 March 2026; paper originally circulated earlier) states in §1.6 that its three conjectures use random stirring **started from the identity**, not stationarity, and run on the original time scale of **unit stirring rate per unoriented nearest-neighbor edge**. Conjecture 1(ii) says that for every `d>=3` there is a finite positive critical inverse temperature `beta_c(d)` such that below it macroscopic cycles disappear in the thermodynamic limit, while above it, for each fixed ordered cycle index `i` and all sufficiently small `epsilon`, the corresponding normalized cycle length has positive thermodynamic-liminf probability of exceeding `epsilon`.

This run therefore does not substitute:

- the stationary split-and-merge theorem;
- a loop-weighted measure;
- a regular-tree theorem;
- or an infinite-volume statement without a finite-torus transfer.

The theorem below is deliberately labelled a local/infinite-volume precursor, hence PARTIAL relative to the source.

---

## 3. New-method attempt that was rejected before the proof

A tempting route was to pre-reserve many deterministic phase windows `I_l` and, for each phase `s_l`, try to apply `NEW-L86` to the phase-lifted points

\[
x_{j,l}=\Phi_{0,s_l}(a_j),\qquad a_j=\pi_\beta^j(0).
\]

This is **not valid** merely from cyclic time-stationarity. Although the phase-return map is conjugate to the original permutation, the root `x_{0,l}=\Phi_{0,s_l}(0)` depends on clocks that also occur in the cyclically shifted slab. It is therefore an anticipative root. “The shifted environment has the same law” does not imply that the rooted orbit has the `NEW-L86` law. This is the same quantifier/predictability defect exposed by the archived `P3` anticipativity example.

That failure is useful: arbitrary interior phases are the wrong place to insist on geometric packing. The nonanticipative geometric object is the phase-zero orbit itself. The replacement is to make the **single deterministic phase-zero prefix macroscopically long when only finitely many orbit steps are requested**.

---

# 4. C27-MACROSCOPIC-FRESH-PREFIX-03 — PROVED (PARTIAL)

We reuse two archived proved estimates, with constants renamed and enlarged/decreased so that `C_0,C_1>=1` and `0<c_1<=1`.

`NEW-L86`: for `h=1`, orbit anchors `a_j=pi_beta^j(0)`, and `R>=1`,

\[
\Pr\!\left(\min_{0\le i<j\le q}|a_i-a_j|_2\le 2R\right)
\le C_0\left(\frac q{\sqrt\beta}+\frac{qR^3}{\beta^{3/2}}\right).
\tag{4.1}
\]

`NEW-L93`: in a fresh space-time tube of duration `G`, the strand started at its measurable center satisfies

\[
\Pr\!\left(\sup_{0\le t\le G}|X_t-X_0|_2\ge r\mid\mathscr F\right)
\le C_1\exp\!\left[-c_1\frac{r^2}{G+r}\right].
\tag{4.2}
\]

### Theorem

Fix an integer `q>=2`. Define

\[
\rho_q:=\min\left\{\frac14,(128C_0q)^{-1/3}\right\},
\qquad
L_q:=\log(32C_1q),
\]

and

\[
\gamma_q:=\min\left\{\frac14,\frac{c_1\rho_q^2}{16L_q}\right\}.
\tag{4.3}
\]

Let

\[
\beta_0(q):=\max\left\{
1,\frac4{\rho_q^2},\left(\frac{2\rho_q}{\gamma_q}\right)^2,
(16C_0q)^2,\frac2{\gamma_q}
\right\}.
\tag{4.4}
\]

For every `beta>=beta_0(q)`, put

\[
r=\lfloor\rho_q\sqrt\beta\rfloor,
\qquad G=\lfloor\gamma_q\beta\rfloor.
\tag{4.5}
\]

In the identity-start nearest-neighbor rate-one interchange process on `Z^3`, with probability at least `3/4`, the first `q` exact permutation-orbit steps

\[
a_0=0,\ a_1=\pi_\beta(a_0),\ldots,\ a_q=\pi_\beta(a_{q-1})
\]

admit a sequential admissible exploration with the following property. For each `j=0,...,q-1`, before computing `a_{j+1}` the entire space-time tube

\[
B_2(a_j,2r)\times[0,G]
\]

is unrevealed; the strand determining the prefix map on `a_j` remains inside `B_2(a_j,r)` throughout `[0,G]`; after that prefix endpoint is revealed, the already conditioned complementary-time map determines `a_{j+1}` exactly. The `q` spatial tubes are pairwise disjoint.

In particular, for `q=2`, after `a_1` has been determined **exactly**, there remains an untouched spatial-phase guard of duration

\[
G=\gamma_2\beta
\]

up to integer rounding around `a_1`, and that guard is sufficient to determine the second exact orbit step. Thus the simplest two-successive-fresh-guard problem selected in STUCK RECOVERY 2 is solved in this fixed-`q` sense.

The constants are explicit functions of the already-proved universal constants `C_0,C_1,c_1`. Because those archived constants were not numerically optimized/recovered, this is **not** advertised as the requested source-level numerical `beta_0`.

### Proof

Write the one-period map chronologically as

\[
P=Q\circ W,
\]

where `W=Phi_[0,G]` is generated by the deterministic prefix clocks and `Q=Phi_[G,beta]` by the complementary clocks. These are independent Poisson increments. Condition on the entire map `Q`. This destroys no clock in the prefix `[0,G]`.

Define the global geometric event

\[
\mathsf{Sep}_q=
\left\{
\min_{0\le i<j\le q}|a_i-a_j|_2>4r
\right\}.
\]

Apply (4.1) with `R=2r`. Since `r<=rho_q sqrt(beta)`,

\[
\Pr(\mathsf{Sep}_q^c)
\le C_0\left(\frac q{\sqrt\beta}+\frac{8qr^3}{\beta^{3/2}}\right)
\le C_0\frac q{\sqrt\beta}+8C_0q\rho_q^3.
\tag{4.6}
\]

By (4.3), `8C_0q rho_q^3<=1/16`; by (4.4), the first term is at most `1/16`. Hence

\[
\Pr(\mathsf{Sep}_q^c)\le\frac18.
\tag{4.7}
\]

Now run the following stopped exploration. At stage `j`, the anchor `a_j` is already known. If its `2r`-ball meets a previously opened `2r`-ball, declare geometric failure. Otherwise reveal only the prefix clocks on edges incident to `B_2(a_j,r)` (equivalently, reveal inside the protective `2r`-ball as needed) and follow the strand from `a_j` until time `G` or until it exits `B_2(a_j,r)`. On exit, declare tube failure. If there is no exit, its exact endpoint

\[
y_j=W(a_j)
\]

has been determined. Since `Q` was already conditioned, set

\[
a_{j+1}=Q(y_j).
\]

This is the exact next iterate of `P`, not a surrogate chronological walk.

Before a nonfailed stage is opened, its prefix clocks are genuinely fresh. The conditioned object `Q` uses disjoint physical times. Earlier prefix exposures lie in spatially disjoint protective balls. Therefore the conditional hypothesis of `NEW-L93` is satisfied at every stage up to the stopping time. By (4.2), uniformly in the adaptive history,

\[
\Pr(\text{tube exit at stage }j\mid\text{past})
\le C_1\exp\!\left[-c_1\frac{r^2}{G+r}\right].
\tag{4.8}
\]

For `beta>=beta_0(q)`, integer rounding gives

\[
r\ge\frac{\rho_q}{2}\sqrt\beta,
\qquad
r\le\frac{\gamma_q}{2}\beta,
\qquad
G+r\le2\gamma_q\beta.
\]

Consequently

\[
c_1\frac{r^2}{G+r}
\ge \frac{c_1\rho_q^2}{8\gamma_q}
\ge 2L_q.
\tag{4.9}
\]

A union bound over the `q` stages gives

\[
\Pr(\text{some tube exit before geometric failure})
\le qC_1e^{-2L_q}
=\frac{qC_1}{(32C_1q)^2}
\le\frac1{1024}.
\tag{4.10}
\]

On `Sep_q`, no geometric-overlap stop occurs: centers among `a_0,...,a_q` are more than `4r` apart, so the protective tubes opened at stages `0,...,q-1` are disjoint. Combining (4.7) and (4.10),

\[
\Pr(\text{successful q-stage exact exploration})
\ge1-\frac18-\frac1{1024}>\frac34.
\]

This proves the theorem. `square`

---

## 5. What moved mathematically, and what emphatically did not

The new point is not another fair-cut estimate. It is a scale deformation of the fresh-tube mechanism: once the requested orbit horizon is fixed, the spatial radius may be taken of order `sqrt(beta)` and the fresh deterministic prefix can therefore occupy a **positive fraction of the entire physical time slab**. Earlier near-`sqrt(beta)`-many-anchor results necessarily used a sublinear window; this theorem trades orbit length for a macroscopic guard.

For fixed `q`, the construction supplies exactly the predictability order that was missing:

1. choose `[0,G]` before seeing the orbit;
2. condition only on `[G,beta]`;
3. discover `a_j` exactly;
4. test disjointness before opening its prefix tube;
5. only then expose fresh clocks in that tube.

There is no use of a phase chosen from its own endpoint.

However the theorem does **not** iterate to the long-cycle conjecture. From (4.3), the certified macroscopic fraction behaves, at best within this argument, like

\[
\gamma_q\asymp \frac{q^{-2/3}}{\log q}
\]

up to universal constants. Thus the guard fraction collapses as `q` grows. The next missing mechanism is not “get a second fresh guard” anymore; it is:

> obtain a guard/revealment mechanism whose usable time fraction does not collapse as the number of exact orbit steps grows, or prove a block-level replacement that glues these fixed-horizon macroscopic guards without conditioning away all future phases.

This is why no source-level `beta_0`, no positive-density cycle theorem, and no improvement of `theta_block` is claimed.

---

## 6. Literature / neighboring-field check, dated 16 September 2026 UTC

Queries included:

- `Ioffe Toth Conjecture 1(ii) random stirring identity`;
- `Infinite cycles in the interchange process in five dimensions Elboim Sly`;
- `random stirring model Hammond trees infinite cycles`;
- `Bjornberg Ueltschi random loop regular trees interchange`;
- `random interchange Z3 infinite cycles 2025 2026`.

Findings:

1. Ioffe--Tóth §1.6 still gives the identity-start, unit-edge-rate finite-torus formulation fixed above.
2. Elboim--Sly, arXiv:2211.17023, prove existence of infinite cycles for `d>=5` at sufficiently large `beta`, using cyclic-time random walk, multiscale diffusion/Brownian coupling, and a local-escape mechanism. This is the nearest solved Euclidean theorem, but it does not cover `d=3`.
3. Hammond's infinite-cycle and sharp-transition results are on infinite rooted/regular trees; the acyclic tree geometry is load-bearing.
4. Björnberg--Ueltschi study random loop models on high-degree regular trees; interchange is a special case, but the regular-tree recursion/high-degree geometry and, in the broader loop model, loop weights prevent treating those results as an unweighted `Z^3` transfer.

The bounded search found no source-matching `d=3` closure. That is a limitation statement, **not** proof of openness and not a novelty certificate for the theorem above.

---

## 7. Directed second audit — C28 actual newest claims

Newest audited C28 report:

`proofnet24/C28-closure-hypercontractivity/runs/2026-09-16/2026-09-16T20-24-56Z__i0032-dyadic-sharpness-instability.md`.

### Verdict

\[
\boxed{\texttt{C27-AUDIT-C28-I0032-DYADIC-SHARP-INSTABILITY-04 = PASS (claim-scoped)}}.
\]

Independent check:

Take the product of a symmetric two-state chain with positive eigenvalue `1` and an `m`-state refresh chain with positive eigenvalue `lambda`, multiplicity `M=m-1`. Uniform transitivity gives local positive-spectrum masses `1,M,M` at eigenvalues `1,lambda,lambda+1`, hence

\[
F_{M,\lambda}(t)=e^{-2t}+Me^{-2\lambda t}+Me^{-2(\lambda+1)t}.
\]

For `3<lambda<4`, the frozen binary dyadic surrogate is

\[
D_M(t)=e^{-2t}+Me^{-4t}+Me^{-8t}.
\]

The level-three thresholds satisfy

\[
s_{M,\lambda}=\frac{\log(M/3)}{2\lambda}+o(1),
\qquad
S_M=\frac{\log(M/3)}4+o(1),
\]

so `S_M/s_{M,lambda}->lambda/2`, and `lambda->4-` proves factor `2` sharpness.

For the instability claim take `lambda_-=4-epsilon`, `lambda_+=4+epsilon`. The forms obey

\[
\mathcal E_-\le\mathcal E_+\le
\frac{4+\epsilon}{4-\epsilon}\mathcal E_-.
\]

On the minus side the two fast masses fall in successive dyadic bands, so

\[
D_-(t)=e^{-2t}+Me^{-4t}+Me^{-8t};
\]

on the plus side both fast masses fall in `[4,8)`, so

\[
D_+(t)=e^{-2t}+2Me^{-8t}.
\]

Therefore the surrogate-threshold ratio tends to `2` as `M->infinity`, whereas the true-threshold ratio tends to `(4+epsilon)/(4-epsilon)`, which tends to `1` with `epsilon`. The hard-bin discontinuity claim is correct.

Scope: this PASS covers the factor-two sharpness and hard-band instability claims only. It does **not** audit a soft/resolvent replacement, optimal source characterization, admission/READY status, or closure of Aldous--Fill Open Problem 8.23.

---

## 8. Handoff state forced by the hard-task stuck rule

C27 has now consumed its two allowed stuck recoveries on this hard target. This run successfully proves the special case selected by Recovery 2, but the **frozen metric still did not move**. Therefore a third recovery on the same target is forbidden.

Handoff payload to preserve:

- frozen supported metric: `theta_block = 1/2 + 1/(16 e log 2) = 0.5331711153389402...`;
- same-metric historical lower bounds: `203/500`, then `0.472361...`, then the current value;
- exact `NEW-L86` orbit-packing theorem and `NEW-L93/94/95/95B` fresh-window machinery;
- `C27-FRESH-PAIR-01`;
- `C27-GUARDED-TYPICAL-PHASE-02` and its predictability requirement;
- `C27-MACROSCOPIC-FRESH-PREFIX-03` from this run;
- exact anticipativity warning: arbitrary phase-lifted roots may not be treated as fresh solely by cyclic time-stationarity;
- current obstruction: keep a nonvanishing usable guard fraction while the exact orbit horizon grows, or replace that requirement by a block-level gluing mechanism;
- tree/loop and stationary results remain transfer heuristics only;
- retired DLA/ORRW routes remain retired.

The next C27 invocation must move to the next genuinely eligible hard target according to the current queue/ownership rules and leave this package as a handoff rather than manufacture STUCK RECOVERY 3.

---

## 9. `ledger_delta` for P26

```yaml
track: C27
status: PARTIAL
source: "Toth (1993) / Ioffe-Toth section 1.6 Conjecture 1(ii), d=3 identity-start unweighted interchange"
metric:
  name: theta_block
  before: "1/2 + 1/(16 e log 2) = 0.5331711153389402..."
  after: "1/2 + 1/(16 e log 2) = 0.5331711153389402..."
  movement: false
raw_unchanged_runs: 5
stuck_recovery_count: 2
new_claim:
  id: C27-MACROSCOPIC-FRESH-PREFIX-03
  status: PROVED_PARTIAL
  statement: "For every fixed q, an exact q-step orbit prefix admits with probability >3/4 a sequential fresh exploration through one deterministic prefix guard of length gamma_q beta; in particular q=2 gives an untouched macroscopic guard after exact determination of a1."
source_beta0_numeric: UNMEASURED
source_long_cycle_status: OPEN
next_action: "MANDATORY SWITCH/HANDOFF on next C27 invocation; no third stuck recovery on this hard target"
audit:
  id: C27-AUDIT-C28-I0032-DYADIC-SHARP-INSTABILITY-04
  verdict: PASS
  scope: "C28 factor-2 sharpness and hard-bin instability only"
```

No shared ledger or peer file was edited.

---

## 10. Runtime/model-control escalation

The exposed task controls still provide task text/title, scheduling/timing, enabled state, and notification metadata, but no model-family selector and no reasoning-effort selector. Therefore GPT-6/maximum remains a prompt request only; this run actually used GPT-5.6 Sol with reasoning level UNVERIFIED.

Making GPT-6/maximum enforceable requires scheduler/backend support, or an authorized enclosing runtime, to expose, persist, and bind those two fields. A task-level `You cannot modify this task` response is an ownership/permission-context boundary; the supported workaround is modification by the owner/admin/coordinator from the owning authorized workspace, or platform support if that ownership context is defective. It is not a reason to bypass permissions or create a duplicate schedule.
