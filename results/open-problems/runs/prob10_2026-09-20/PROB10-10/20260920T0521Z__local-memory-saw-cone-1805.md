Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# PROB10-10 — four-step local-self-avoidance transfer extends the certified reflected strict-triangle range to slope 361/200

Status: **PARTIAL / OPEN** for the full source problem. This run gives genuine restricted-direction source progress, with an explicit finite-to-infinite error, but it does **not** prove global strict convexity and does **not** move the canonical axis/diagonal milestone `c_*`.

## 1. Frozen model, source, and before/after metrics

Throughout:

- graph: nearest-neighbor **undirected** `Z^2`;
- physical edge weights: iid rate-one exponentials;
- unrestricted passage time: `T(x,y)`;
- deterministic time-constant norm: `mu`, normalized by `T(0,nv)/n -> mu(v)`.

The source is Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4. The source asks, for continuous edge laws, to show that the limit shape is strictly convex; the exact present parent is the `Exp(1)` specialization above. The current canonical claim is `operations/claims/PROB10-10.md`, source key `ADH_50yearsFPP_Q4::Exp1_Z2_undirected`.

### Full-source / canonical axis-diagonal metric

Let

\[
\Delta_{12}=2\mu(e_1)-\mu(1,1),
\qquad
c_*:=\sup\{c\ge0:\Delta_{12}\ge c\text{ has been rigorously proved in the canonical track}\}.
\]

Before: `c_*=0`.  
After: `c_*=0`.

Thus there is **no movement on the axis/diagonal pair and no global strict-convexity closure**.

### Restricted reflected strict-triangle metric

The newest neighboring P04 theorem before this run, in

`proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T04-47-14Z__ladder8-cone1814-transfer.md`,

had already superseded this track's earlier `15/8` result and proved a positive reflected strict-triangle defect on

\[
|y|\ge \frac{907}{500}x=1.814x,\qquad x>0.
\]

This run enlarges the complete certified range to

\[
\boxed{|y|\ge \frac{361}{200}x=1.805x,\qquad x>0.}
\tag{1.1}
\]

So the cone-boundary slope moves

\[
\boxed{907/500\longrightarrow361/200.}
\]

On the whole new cone we prove

\[
\boxed{
\mu(x,y)+\mu(x,-y)-\mu(2x,0)
\ge \delta x,
}
\tag{1.2}
\]

with the exact positive defect

\[
\boxed{
\delta=
\frac{68977908882155446326458294510291016568757618382301}
{3718960855166042798264926188889970206310400000000000000}
=1.854762971929043\times10^{-5}.
}
\tag{1.3}
\]

The same statement holds under the square-lattice `D_4` symmetries. This is a **restricted reflected-pair strict triangle theorem**, not global strict convexity.

## 2. Continuity, ownership, and consumed evidence

The required immutable handoff of the actual pre-refocus HARD7-03 particle-system work already exists and was re-read rather than duplicated:

`runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__handoff-hard7-03-d0025.md`, blob `1a7045aaf81930242664b944b6f0ab09f791c4c1`.

It preserves D0025 / Seppalainen Problem 4, the exact four-step sign-atlas state, and the moved plateau half-width lower bound

`25000000/291978907 -> 250000000/2919788131`.

No D0025 claim or predecessor artifact is modified here.

Repository state consumed:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- `operations/claims/PROB10-10.md`, blob `6fca778a3608f973175577e9852a61dcd6754c55`;
- newest canonical owner report before this run, `runs/prob10_2026-09-20/PROB10-10/20260920T0416Z__cone-tilt-15over8-extension.md`, blob `9622e0686c7dde018756d6ee4fff28f7399b44b5`;
- newest P04 companion report, `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T04-47-14Z__ladder8-cone1814-transfer.md`, blob `8e36ee8f2841947fdfce0ec67e4e0e89e02a754d`;
- newest P20 companion report, `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T05-09-30Z__axis-busemann-cone-and-policy-separation.md`, blob `0e121a701f1d2566e7bcdf61ec5874dd20fa7498`;
- the canonical R08 failures at `runs/R08/2026-09-16T1329Z_fpp-axis-gap-a1c93e.md`, `runs/R08/2026-09-16T1429Z_fpp-diamond-gap-7e4a9c.md`, `runs/R08/20260916T1528Z_fpp_axis_transition_3b7c92.md`, and `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`;
- the neighboring R07 KPZ history, including `runs/R07/2026-09-16T1525Z_kpz_deep_edges_03.md`, which explicitly does not claim curvature.

The old generic R08 strict-convexity route remains retired. Its binding failures are preserved: shared bypasses invalidate multiplying local detour margins, positive-probability finite cylinders can have exact finite triangle equality, and the old fixed-corner blocks did not cross the axis/diagonal threshold. R07's fluctuation/KPZ work remains a distinct target and is not imported as curvature.

There is no ownership collision with P04 or P20. P04 owns the finite-ladder axis optimization; this run consumes its proved `A_8` and improves the **oblique path-count compiler** instead. P20 owns the complementary Busemann/variational route; no P20 claim is overwritten.

## 3. Current-source boundary / bounded literature refresh

A bounded 20 September 2026 search again found no theorem closing ordinary iid `Exp(1)`, nearest-neighbor, undirected `Z^2` strict convexity.

Relevant distinctions checked:

1. Auffinger--Damron--Hanson, arXiv:1511.03262, remains the source navigation for strict convexity.
2. Dembin--Elboim--Peled, arXiv:2204.02332, obtain quantitative planar geodesic coalescence under a hypothesis that the limit shape has more than 32 extreme points; that hypothesis does not give the present strict-convexity conclusion.
3. Jacquet, arXiv:2412.20779, proves strict inequality between unrestricted and directed FPP time constants, not the direction-to-direction reflected strict triangle here.
4. Recent work on geodesic patterns/influences or other graphs/models does not identify the `Exp(1)` lattice limit shape.

This is only a bounded negative search. No worldwide novelty or publication-priority claim is made for the restricted theorem below.

## 4. New idea written before code and three materially different attacks

The idea was written before any checker at

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0521Z__idea-local-memory-saw-cone.md`, creation commit `f1bd50289aea92bab8d190cbc7604358c9aec1fc`.

Three materially different routes were compared:

1. **Four-step local-self-avoidance transfer — SUCCESS.** Replace the previous non-backtracking superset by a strictly smaller finite-memory superset that still contains every globally self-avoiding path. This improves the oblique lower bound without any block-independence assumption.
2. **Busemann policy-disagreement route — NOT CLOSED.** P20 now proves an axis-support Busemann residual identity and qualitative separation of distinct-mean stationary policies, but there is still no quantitative positive density/energy estimate that survives unrestricted bypasses and closes the central angular sector. I do not promote that conditional interface.
3. **Longer finite-ladder axis optimization — CONSUMED, NOT DUPLICATED.** P04's length-8 exact infection recursion already improved `mu(e1)` to `A_8`; a still longer ladder is a valid separate route but is owned by P04 and computationally expensive. The nonduplicating opportunity in this run is the oblique counting side.

The primary route was attacked at its negation before promotion: every genuine self-avoiding walk through length 9 was exhaustively checked to satisfy the automaton's four-step constraints, and the critical exact Chernoff base was checked against a rational number below one. Those finite checks are self-checks, not independent audits; the general inclusion has the direct proof in Section 6.

## 5. Input from P04: dependence-safe length-8 axis bound

P04 proved by an exact continuous-time infection recursion on the finite ladder `[0,8]x[-1,1]` and a pathwise concatenation argument that

\[
\boxed{
\mu(e_1)\le A_8
:=
\frac{4688722489067361283750127182134186345695457354381617699}
{7437921710332085596529852377779940412620800000000000000}
=0.6303807261851404\ldots .
}
\tag{5.1}
\]

At finite concatenated scales its same argument gives, for every integer `N>=1`,

\[
\mathbb E T(0,8Ne_1)\le 8N A_8.
\tag{5.2}
\]

No independence between adjacent ladder blocks is used: expectation linearity plus a pathwise concatenated competitor is enough. This theorem is a consumed neighboring input, not relabeled as new work.

Set

\[
c:=\frac{63039}{100000}=0.63039.
\tag{5.3}
\]

Then `c>A_8`, and

\[
2(c-A_8)=\delta
\]

is exactly (1.3).

## 6. New finite-memory self-avoiding superset

Use direction labels `E,W,N,S`. A four-step direction word is called **locally self-avoiding** if its five successive vertices, starting at the origin, are all distinct. Let `S_4` be the finite set of such words.

The exact artifact verifies

\[
|S_4|=100.
\tag{6.1}
\]

A direction sequence of length at least four is called **4-local-SAW** if every consecutive block of four directions lies in `S_4`.

### Lemma 6.1 — every global SAW is a 4-local-SAW

Every globally self-avoiding nearest-neighbor path is 4-local-SAW.

#### Proof

Take any four consecutive edges of a globally self-avoiding path. Their five consecutive vertices are a subset of the vertices of the full path. Since the full path visits no vertex twice, those five vertices are distinct. Thus every consecutive four-step word belongs to `S_4`. QED.

The converse is not needed and may fail: `4-local-SAW` is deliberately a finite-memory **superset** of global self-avoiding paths.

Now assign tilted weights

\[
w_E=A,
\quad w_W=A^{-1},
\quad w_N=B,
\quad w_S=B^{-1},
\tag{6.2}
\]

where

\[
A=\frac{1903}{1000},
\qquad
B=\frac{2837}{1000}.
\tag{6.3}
\]

Define the `100x100` nonnegative transfer matrix `M` on `S_4` as follows. From state `(d_1,d_2,d_3,d_4)` to `(d_2,d_3,d_4,d_5)`, a transition is allowed precisely when the latter word lies in `S_4`, and its weight is `w_{d_5}`. The exact automaton has 284 directed transitions.

The checker contains an explicit positive rational vector `z`, normalized so `min_i z_i=1`, and verifies componentwise

\[
Mz\le rz,
\qquad
r=\frac{4999}{1000}.
\tag{6.4}
\]

The largest exact component ratio is

\[
\max_i\frac{(Mz)_i}{z_i}
=
\frac{155793861493490629}{31172848089031000}
<\frac{4999}{1000}.
\tag{6.5}
\]

No floating-point comparison is used in (6.4)--(6.5).

For a state `sigma=(d_1,d_2,d_3,d_4)`, put

\[
a_\sigma:=\prod_{j=1}^4 w_{d_j}.
\]

If `L_m` denotes the total tilted weight of all length-`m` 4-local-SAW direction sequences, then for `m>=4`,

\[
L_m=a^T M^{m-4}{\bf1}
\le a^T M^{m-4}z
\le r^{m-4}a^Tz
=K r^m,
\tag{6.6}
\]

where the exact constant is

\[
\boxed{
K=
\frac{3554873050462117591280503343605858557553719921}
{265274220884995042763620746658426614922920500}.
}
\tag{6.7}
\]

The exact checker separately enumerates lengths `m=1,2,3` and verifies the same bound `L_m<=Kr^m`; hence there is no discarded startup regime.

## 7. Endpoint counting theorem

Fix positive integers `a,b,n`. Let `N_m(n;a,b)` be the number of globally self-avoiding nearest-neighbor paths of length `m` from `0` to `n(a,b)`.

Every such path is 4-local-SAW by Lemma 6.1. Moreover every path with displacement `n(a,b)` has the same tilted product

\[
A^{an}B^{bn},
\tag{7.1}
\]

because `#E-#W=an` and `#N-#S=bn`. Therefore (6.6) gives, for every `m>=1`,

\[
\boxed{
N_m(n;a,b)
\le K r^m A^{-an}B^{-bn}.
}
\tag{7.2}
\]

This is the gain over the preceding canonical compiler: it counts a strictly smaller finite-memory superset than all non-backtracking walks while still containing every possible self-avoiding FPP geodesic.

## 8. Exponential lower-tail transfer on the enlarged cone

A self-avoiding length-`m` path uses `m` distinct physical edges, so its passage weight `S_m` is a sum of `m` independent `Exp(1)` variables. For every `s>0` and `t>0`,

\[
\Pr(S_m\le t)
\le e^{st}(1+s)^{-m}.
\tag{8.1}
\]

Take

\[
s=4,
\qquad
u:=1+s=5,
\qquad
q:=\frac r\nu=\frac{4999}{5000}<1.
\tag{8.2}
\]

Because edge weights are positive almost surely, if `T(0,n(a,b))<=can`, loop erasure produces a self-avoiding competitor of no larger passage time. Every such path has length at least `(a+b)n`. Hence by (7.2), (8.1), and a union bound over deterministic paths,

\[
\begin{aligned}
\Pr\!\left(T(0,n(a,b))\le can\right)
&\le
K A^{-an}B^{-bn}e^{scan}
\sum_{m\ge(a+b)n}q^m\\
&=
C\,[\beta(b/a)]^{an},
\end{aligned}
\tag{8.3}
\]

where

\[
\boxed{
C:=\frac K{1-q}
=
\frac{35548730504621175912805033436058585575537199210}
{530548441769990085527241493316853229845841}
}
\tag{8.4}
\]

and

\[
\beta(\rho)
:=A^{-1}B^{-\rho}e^{sc}q^{1+\rho}.
\tag{8.5}
\]

Since `B>1` and `q<1`, the factor `(q/B)^rho` is strictly decreasing, so `beta(rho)` is strictly decreasing in `rho`.

Set

\[
\rho_0:=\frac{361}{200}=1.805,
\qquad
\widehat\beta:=\frac{249}{250}=0.996.
\tag{8.6}
\]

The finite exact certificate proves

\[
\boxed{\beta(\rho_0)<\widehat\beta<1.}
\tag{8.7}
\]

For completeness, the transcendental comparison is reduced to exact rational arithmetic as follows. Raising to the 200th power clears the denominator of `rho_0`:

\[
\beta(\rho_0)^{200}
=A^{-200}B^{-361}e^{200sc}q^{561}.
\tag{8.8}
\]

Here

\[
x:=200sc=800c=504.312,
\qquad y:=x/1024.
\]

Let

\[
U:=\sum_{j=0}^{24}\frac{y^j}{j!}
+
\frac{y^{25}/25!}{1-y/26}.
\tag{8.9}
\]

For Taylor terms from index 25 onward, each successive ratio is at most `y/26<1`; therefore `e^y<U` and hence `e^x<U^{1024}`. Substitution in (8.8) gives a fully rational upper bound. The executed exact checker verifies

\[
A^{-200}B^{-361}U^{1024}q^{561}
<\left(\frac{249}{250}\right)^{200}.
\tag{8.10}
\]

Decimal values printed only for readability are `0.39921620657242546` for the left rational upper bound and `0.4486086927805973` for the right side. The asserted sign is exact.

Combining monotonicity with (8.3)--(8.7), for every integer `a>=1`, every integer `b` with `b/a>=361/200`, and every `n>=1`,

\[
\boxed{
\Pr\!\left(T(0,n(a,b))\le can\right)
\le C\left(\frac{249}{250}\right)^{an}.
}
\tag{8.11}
\]

This is the explicit finite-to-infinite error requested by the source contract.

## 9. Infinite-volume oblique lower bound

### Theorem 9.1

For every real `x>0` and every real `y` with

\[
|y|\ge\frac{361}{200}x,
\]

\[
\boxed{\mu(x,y)\ge c x.}
\tag{9.1}
\]

#### Proof

First take an integer direction `(a,b)` with `a>=1`, `b/a>=361/200`. From (8.11) and nonnegativity of passage times,

\[
\begin{aligned}
\frac{\mathbb E T(0,n(a,b))}{n}
&\ge ca\left[1-C(249/250)^{an}\right].
\end{aligned}
\tag{9.2}
\]

Let `n->infinity`. Standard `L^1` convergence of FPP passage times in a fixed direction yields

\[
\mu(a,b)\ge ca.
\tag{9.3}
\]

Homogeneity gives the same assertion for rational slopes, and continuity of the norm `mu` extends it to every real slope `y/x>=361/200`. Reflection symmetry handles negative `y`. QED.

## 10. New reflected strict triangle on the full 1.805 cone

For `x>0` and `|y|>=361x/200`, Theorem 9.1, reflection symmetry, homogeneity, and the P04 input (5.1) give

\[
\begin{aligned}
\mu(x,y)+\mu(x,-y)-\mu(2x,0)
&=2\mu(x,y)-2x\mu(e_1)\\
&\ge2cx-2A_8x\\
&=\delta x>0.
\end{aligned}
\tag{10.1}
\]

This proves (1.1)--(1.3). Applying rotations/reflections gives the corresponding complete `D_4` image of the certified range.

## 11. Explicit finite expected triangle residual

The finite-scale statement retains the dependence and interface error explicitly rather than replacing it by a limit.

Fix integers `a>=1`, `b/a>=361/200`, and `n>=1`, and put

\[
u=n(a,b),
\qquad v=2an e_1.
\]

Define the pathwise nonnegative triangle residual

\[
\mathcal R_{a,b,n}:=T(0,u)+T(u,v)-T(0,v)\ge0.
\tag{11.1}
\]

Translation and reflection make the first two terms identically distributed. From (8.11),

\[
\mathbb E T(0,u)
\ge can\left[1-C(249/250)^{an}\right].
\tag{11.2}
\]

If `an` is divisible by four, then `2an` is divisible by eight, so the finite P04 block transfer (5.2) gives

\[
\mathbb E T(0,v)\le2A_8an.
\tag{11.3}
\]

Thus

\[
\boxed{
\frac{\mathbb E\mathcal R_{a,b,n}}{an}
\ge
\delta-2cC\left(\frac{249}{250}\right)^{an}.
}
\tag{11.4}
\]

The executed exact checker finds that the right side is positive already at

\[
\boxed{an=5552,}
\tag{11.5}
\]

with decimal readability margin

\[
2.41973922860306\times10^{-7}>0.
\]

The preceding multiple of four, `an=5548`, gives a negative value for this particular explicit lower bound (`-5.386907112415423e-8`). Thus 5552 is the first positive multiple-of-four scale for the archived bound, not a sampled shape claim.

## 12. Exact checker and tests actually run

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0521Z__local_saw_cone_exact.py`, creation commit `d82cec078daee90c29958c249fc867cfa25d12a7`.

Archived output:

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0521Z__local_saw_cone_exact.out`, creation commit `1da9304b8c7ae6465f0b08bcbb84d17ea1a3f69f`.

The checker was executed in this run and verifies with Python `Fraction` arithmetic:

- exactly 100 admissible four-step states and 284 transitions;
- all 100 component inequalities `Mz<=rz`;
- exact startup bounds for lengths 1, 2, and 3;
- exhaustive inclusion of all genuine self-avoiding direction words through length 9 (`25,520` such words across lengths 4--9) in the four-window automaton;
- the exact rational comparison `beta(rho_0)^200 < (249/250)^200` through the Taylor/geometric upper certificate;
- positivity of `delta`;
- positivity of the finite residual bound at `an=5552` and nonpositivity of this explicit bound at `an=5548`.

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

The exhaustive short-word test is a **self-check**, not an independent audit and not a substitute for Lemma 6.1's general proof.

## 13. Source-level before/after versus auxiliary progress

| Quantity | Before | After | Classification |
|---|---:|---:|---|
| Full Exp(1) strict convexity | OPEN | OPEN | source status unchanged |
| Canonical axis/diagonal `c_*` | 0 | 0 | no movement |
| Certified reflected-pair cone boundary slope | `907/500 = 1.814` | `361/200 = 1.805` | **source-valid restricted-direction movement** |
| Defect on the newly certified cone | positive on old cone only | `delta = 1.854762971929043e-5` on full 1.805 cone | restricted theorem |
| Explicit finite residual positive scale from this compiler | not available at slope 1.805 | `an=5552` (multiples of 4) | auxiliary finite-to-infinite certificate |
| Path-count mechanism | non-backtracking superset | 4-local-SAW superset | mechanism advance |

## 14. Remaining full-scope gap

The full source problem remains far from closed. In particular:

1. the central angular sector between the certified wide cone and the axes remains uncovered;
2. the canonical pair `2mu(e1)-mu(1,1)` still has no positive certified lower bound (`c_*=0`);
3. finite-memory local self-avoidance reduces path entropy but does not approach exact global self-avoidance automatically; proving a systematic `k -> infinity` transfer with controlled spectral data is a separate problem;
4. P20's Busemann policy-separation mechanism still needs a quantitative disagreement-density / bypass-control theorem before it can yield global curvature;
5. source closure still requires a complete all-direction proof and independent validation under the repository standard.

A natural next nonrepeating attack, if this track continues, is to increase the local memory **analytically rather than by blind enumeration**: quotient the `k`-local-SAW automaton by lattice symmetries and derive a monotone spectral-radius comparison, then ask whether the resulting directional lower bound can reach slope `1` before state growth becomes prohibitive. The failure threshold itself would quantify how much path entropy remains to be removed.