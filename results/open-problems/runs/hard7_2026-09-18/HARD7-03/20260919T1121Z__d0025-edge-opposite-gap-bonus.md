**Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q)`, `25000/296511 -> 2500000/29649457`. Methods tried: B1 / B24 / B30.**

# HARD7-03 — D0025 mixed-sign edge bonus

Status: **PARTIAL**. The source problem is not solved in this run.

## 1. Continuity, ownership, required reads

I resumed the admitted canonical claim

`operations/claims/D0025.md`, owner `HARD7-03`, key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`.

Before doing new mathematics I read the current control/directive files, the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the newest HARD7-03 checkpoint, current neighboring HARD7-02/HARD7-04 state, and the D/E/F/G/H/I plus Claude intake ledgers. No current canonical-claim collision was found for D0025. Shared ledgers were not edited.

The primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes* (1999), Problem 4, Section 4. The source asks, for the disordered TASEP, whether there is a phase transition analogous to disordered ZRP and in particular whether the flux `f_K(p)` has a flat segment on an interval around `p=K/2`.

A fresh bounded literature search in this run did not surface a theorem closing this exact iid site-disordered finite-capacity `K>=2` plateau question. Recent TASEP mixing-on-a-circle and symmetric partial-exclusion cutoff results are different models, while the older disordered-exclusion literature does not by itself settle this quantifier. This is only a bounded negative search, not a claim that the whole literature was exhaustively searched.

The frozen test case remains

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

with

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

The previous checkpoint proved

\[
G_1(0)\le \frac{296511}{100000}=2.96511,
\qquad
\Delta_2(Q)\ge \frac1{4G_1(0)}\ge \frac{25000}{296511}.
\]

The `G_1(0) -> Delta_2(Q)` transfer is inherited from the earlier D0025 cusp/plateau checkpoints and is not re-proved here.

## 2. Idea before code

The new idea was written first, before the checker, at

`artifacts/hard7_2026-09-18/HARD7-03/20260919T1119Z__idea-edge-opposite-gap-bonus.md`

(commit `a50aec5304c55a773a4add92b980babf3fe473c3`).

The previous run bounded the three-step slack kernel by

\[
\Phi_\theta(u,v)\ge \kappa(\theta)e^{\min(u,0)+\min(v,0)},
\qquad
\kappa(\theta)=\frac{\theta}{(2-\theta)(3-\theta)}.
\]

This loses positive mass whenever exactly one predecessor gap is negative. The sliding-window geometry makes that mixed-sign regime structurally natural, so this run attacks the discarded term directly.

## 3. B1: exact mixed-sign Laplace kernel

Put

\[
a=1-\theta,\quad b=2-\theta,\quad c=3-\theta.
\]

For `v<0<=u`, splitting the defining integral for `Phi_theta` at `t=u` gives exactly

\[
\Phi_\theta(u,v)
=\theta e^v\left[
\frac{1-e^{-au}}{ab}+\frac{e^{-bu}}{bc}
\right]. \tag{3.1}
\]

Indeed, in this sign regime the factor `e^{-(t-v)_+}` is always `e^{v-t}`, while `e^{-(t-u)_+}` changes at `u`; integrating separately on `[0,u]` and `[u,\infty)` yields (3.1).

Subtracting the old envelope `\kappa e^v` leaves

\[
B_\theta(u,v)
=\theta e^v\left[
\frac{1-e^{-au}}{ab}-\frac{1-e^{-bu}}{bc}
\right]. \tag{3.2}
\]

## 4. B24: sharp universal coefficient in a one-basis minorant

For `u>=0`,

\[
1-e^{-bu}\le \frac ba(1-e^{-au}). \tag{4.1}
\]

To check (4.1), set

\[
h(u)=\frac ba(1-e^{-au})-(1-e^{-bu}).
\]

Then `h(0)=0` and

\[
h'(u)=b(e^{-au}-e^{-bu})\ge0
\]

because `0<a<b`. Substitution into (3.2) gives the pointwise improvement

\[
\boxed{
\Phi_\theta(u,v)
\ge \kappa e^v+rac{\kappa}{a}e^v(1-e^{-au})
}\qquad(v<0\le u). \tag{4.2}
\]

The coefficient `\kappa/a` is sharp for the basis `e^v(1-e^{-au})`: differentiating (3.2) at `u=0` gives `\partial_u B_\theta(0,v)=\kappa e^v`, while

\[
\partial_u[e^v(1-e^{-au})]_{u=0}=ae^v.
\]

Hence any larger universal coefficient fails for sufficiently small positive `u`.

## 5. B30: localize the gain to the strict edge chain

For the edge triple, condition on first-layer exponentials and write

\[
u_0=\max(A_{-1},A_0,A_1),\quad
u_1=\max(A_0,A_1),\quad
u_2=A_1,
\]

so `u_0>=u_1>=u_2`, and let `Y_i=u_i+B_i` with independent unit exponentials `B_i`.

On the strict chain

\[
Y_0>Y_1>Y_2,
\]

one has positive gap `u=Y_0-Y_1` and negative gap `v=Y_2-Y_1`. Therefore (4.2) contributes, beyond the previous global envelope,

\[
\frac{\kappa}{a}(T_1-T_2) \tag{5.1}
\]

per edge, where

\[
T_1=\mathbb E\left[e^{(\theta-1)Y_1+Y_2};Y_0>Y_1>Y_2\right],
\]

\[
T_2=\mathbb E\left[e^{Y_2-aY_0};Y_0>Y_1>Y_2\right].
\]

There are two reflected edge triples.

### Exact conditional evaluation

Fix `u_0>=u_1>=u_2`. Integrate first over `Y_0` and then over `Y_2`; split the remaining `Y_1` integral at `u_0`. On `u_1<=Y_1<u_0`, `Y_0>Y_1` is automatic because `Y_0>=u_0`; on `Y_1>=u_0` the upper-particle tail contributes `e^{u_0-Y_1}`. Elementary exponential integration gives

\[
\begin{aligned}
T_1\mid u
={}&e^{u_2-au_1}\left(\frac{u_1-u_2}{b}+\frac1{b^2}\right)\\
&+e^{u_1+u_2-bu_0}
\left[(u_0-u_2)\left(\frac1c-\frac1b\right)
+\left(\frac1{c^2}-\frac1{b^2}\right)\right].
\end{aligned} \tag{5.2}
\]

For `T_2`, the same split is used, but the `Y_0` integral carries the factor `e^{-aY_0}`. This gives

\[
\begin{aligned}
T_2\mid u
={}&\frac{e^{u_2-au_0}}{b}\bigl[(u_1-u_2)+1\bigr]\\
&+\frac{e^{u_1+u_2-bu_0}}{b}
\left[-(u_0-u_2+1)+\frac{u_0-u_2}{c}+\frac1{c^2}\right].
\end{aligned} \tag{5.3}
\]

The first-layer variables are again integrated over the six strict order cones. Each term in (5.2)-(5.3) is an exponential monomial times at most one order-statistic gap, so the cone integrals are rational functions of `theta`; the checker evaluates them with `fractions.Fraction` only.

At

\[
\theta=\frac{11729}{20000},
\]

the exact certificate gives

\[
T_1\approx0.604595951733871,
\qquad
T_2\approx0.405101779151499,
\]

and exactly `T_1-T_2>0`. Thus the two reflected edges add the rigorously positive amount

\[
H_{\rm edge}
=2\frac{\kappa}{a}(T_1-T_2)
\approx0.165842448087406. \tag{5.4}
\]

No finite sampling is used in (5.2)-(5.4).

## 6. New exact Chernoff certificate and metric movement

The checker reconstructs the entire preceding global-envelope correction and verifies the old edge identity exactly before inserting (5.4). With

\[
\theta=\frac{11729}{20000},
\qquad
A=\frac{29649457}{10000000}=2.9649457,
\]

it obtains an exact rational upper bound `U_4` on the four-step exponential moment, numerically

\[
U_4\approx1048.556322921405126.
\]

Let

\[
x=4\theta A=\frac{347758481153}{50000000000}.
\]

Using the positive Taylor lower bound

\[
S_{32}(x)=\sum_{k=0}^{32}\frac{x^k}{k!}<e^x,
\]

the exact rational check proves

\[
S_{32}(x)-U_4>0,
\qquad
S_{32}(x)-U_4\approx5.9288439552\times10^{-5}. \tag{6.1}
\]

Hence `U_4<e^{4 theta A}` exactly, and the already-established four-step block Chernoff lemma yields

\[
\boxed{G_1(0)\le \frac{29649457}{10000000}=2.9649457.} \tag{6.2}
\]

Applying the inherited plateau transfer gives

\[
\boxed{
\Delta_2(Q)\ge \frac{2500000}{29649457}
\approx0.084318576222155.
} \tag{6.3}
\]

Therefore the frozen metric moves from

\[
L_{\rm before}=\frac{25000}{296511}
\approx0.084313904037287
\]

to

\[
L_{\rm after}=\frac{2500000}{29649457}
\approx0.084318576222155,
\]

with exact gain

\[
L_{\rm after}-L_{\rm before}
=\frac{41075000}{8791390144527}>0. \tag{6.4}
\]

This is a genuine rigorous movement of the source-relevant lower bound, but it remains only a quantitative partial result for one frozen environment law and does not prove Seppäläinen's full plateau question.

## 7. Exact artifacts and readback

- Idea before code: commit `a50aec5304c55a773a4add92b980babf3fe473c3`.
- Exact checker: `artifacts/hard7_2026-09-18/HARD7-03/edge_gap_bonus_20260919T1119Z.py`, commit `86e66c9d01c34afa5775a7d03b2745949b1e378b`.
- Exact output: `artifacts/hard7_2026-09-18/HARD7-03/edge_gap_bonus_20260919T1119Z.out`, commit `f8d3b704ffbb2b82945a6db15ee557f04d227e24`.

The checker and output were read back at their commits. The output ends

`ALL_EXACT_CHECKS_PASS = True`.

These are self-checks, not independent closure audits.

## 8. What the three new methods did

- **B1 — change category:** replaced a coarse event-wise slack estimate by an exact two-gap Laplace/hazard kernel. This exposed the missing positive term in mixed-sign configurations.
- **B24 — extremal object:** optimized the coefficient of the simple basis `e^v(1-e^{-au})`; `kappa/a` is pointwise valid and sharp at `u=0`.
- **B30 — one scale/direction at a time:** instead of integrating every mixed-sign branch at once, localized first to the edge chain `Y_0>Y_1>Y_2`. This alone moved the metric.

The next productive route is to port the same mixed-sign bonus to the near-edge and central complement branches, where the previous global envelope also discarded positive gap information. A second route is to integrate the full exact formula (3.1), rather than the one-basis minorant (4.2), on selected order cones.

## 9. Capability / scheduler honesty

The available task interface still exposes scheduling fields such as title, prompt, schedule/timing mode and enabled state, but no model selector, reasoning selector, or guaranteed execution-duration selector. Therefore GPT-6 maximum can only be requested in prompt text in this environment; setting it for real would require the platform/scheduler to expose model and reasoning configuration fields. This run actually executed as **GPT-5.6 Sol / reasoning UNVERIFIED**.

For a task that returns `You cannot modify this task` (the previously reported P26 case), this worker has no legitimate bypass. The practical route is modification by the account/workspace owner that has edit permission, or platform/support remediation of that task's ownership/permission state. I did not recreate, modify, reactivate, or replace any other schedule in this run.

## 10. Ledger delta for merge owner

```text
track: HARD7-03
target: D0025 / Seppalainen Problem 4
status: PARTIAL
metric: L <= Delta_2(Q)
before: 25000/296511
after: 2500000/29649457
movement: +41075000/8791390144527
methods: B1,B24,B30
unchanged_run_count: 0
stuck: false
shared_roots_modified: none
```

No closure is claimed; therefore no paper folder and no closure-audit request is triggered.