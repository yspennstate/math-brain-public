Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 2500000/29649457 -> 2500000/29648439`. Methods tried: B29 / B27 / B21.**

# HARD7-03 — exact mixed-sign edge kernel improves the D0025 plateau certificate

Status: **PARTIAL**. Seppäläinen Problem 4 is not solved in full.

## 1. Continuity, ownership, required reads, and source status

This execution resumes the existing exclusive canonical claim

`operations/claims/D0025.md`, owner `HARD7-03`, key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`.

I read the controlling files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the current D0025 claim; the latest own checkpoint `20260919T1121Z__d0025-edge-opposite-gap-bonus.md`; and current neighboring HARD7-02/HARD7-04 state. The latest neighboring states remain on distinct non-Hermitian-matrix and growing-random-graph targets, so there is no canonical collision with D0025. Shared root ledgers were not modified.

The primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1–15, Problem 4, Section 4, DOI `10.11606/resimeusp.v4i1.74889`. The exact residual claim used by this track is the source's general-capacity disordered asymmetric `K`-exclusion phase-transition/flat-flux question after excluding the now-known ordinary `K=1` site-disorder case.

A fresh bounded literature search on 2026-09-19 used the exact source title and the queries `disordered K-exclusion plateau site disorder`, `general K TASEP site disorder plateau`, and `partial exclusion disorder flux site rates`. It recovered the primary source and, among recent work, Schmid–Sly, *Mixing times for the TASEP on the circle*, PTRF 194 (2026), DOI `10.1007/s00440-026-01466-0`, published 19 February 2026. That paper studies homogeneous ordinary TASEP on a finite circle and does not close the iid site-disordered finite-capacity `K>=2` plateau question. Other surfaced defect/dynamic-disorder and partial-exclusion papers likewise concern different models. No theorem closing this exact residual surfaced in this bounded search. This is **not** a claim of exhaustive worldwide openness.

The frozen test case and quantity remain

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\},
\]

with one stable metric: a rigorous lower bound `L <= Delta_2(Q)`.

The previous checkpoint established

\[
G_1(0)\le \frac{29649457}{10000000}=2.9649457,
\qquad
L\ge \frac{2500000}{29649457}.
\tag{1.1}
\]

The already proved `G_1(0) -> Delta_2(Q)` transfer is inherited from the earlier D0025 cusp/plateau checkpoints and is not re-derived here.

## 2. Idea before code and method rotation

Before constructing a checker I recorded the new route in

`artifacts/hard7_2026-09-18/HARD7-03/20260919T1221Z__idea-exact-mixed-sign-edge-kernel.md`

at commit `98ab11a3968ca2970d9a44eccfe3bb8af47533e9`, and read the commit back successfully.

The preceding run used the sharp-at-zero one-basis minorant for a mixed-sign predecessor gap. This run asks whether optimizing a uniform coefficient **before** integration is itself the source of loss.

- **B29 — add the point at infinity.** Compare the exact mixed-sign remainder at `u=0` and `u=+infinity`. It vanishes at the former but is strictly positive at the latter, so local sharpness at zero does not imply integral sharpness.
- **B27 — swap quantifiers.** Instead of choosing one coefficient valid for every `u` and then averaging, integrate the exact `u`-dependent excess on the strict order cone first.
- **B21 — ask who else has this shape.** Recast the new term as a phase-type / exponential-spacing moment integral. First and second moments of independent exponential gaps make the six cone integrals exact rational functions.

B21 and B29 were the only numbered moves not previously used anywhere on this long D0025 track. Since the numbered list has otherwise been exhausted, B27 is an explicitly disclosed reuse from an old stuck-recovery run, in a different exact-kernel role; it is not a repetition of the immediately preceding B1/B24/B30 triple.

## 3. Exact mixed-sign kernel: the old coefficient is only locally sharp

Write

\[
a=1-\theta,\qquad b=2-\theta,\qquad c=3-\theta,
\qquad \kappa=\frac{\theta}{bc}.
\]

For the strict mixed-sign regime `v<0<=u`, the preceding checkpoint derived

\[
\Phi_\theta(u,v)
=\theta e^v\left[\frac{1-e^{-au}}{ab}+\frac{e^{-bu}}{bc}\right].
\tag{3.1}
\]

Subtracting the global baseline `\kappa e^v` gives

\[
B_\theta(u,v)
=\theta e^v\left[
\frac{1-e^{-au}}{ab}-\frac{1-e^{-bu}}{bc}
\right].
\tag{3.2}
\]

The previous run used

\[
B_\theta(u,v)\ge \frac{\kappa}{a}e^v(1-e^{-au}),
\tag{3.3}
\]

whose coefficient is sharp at `u=0`. The **exact residual after (3.3)** is

\[
R_\theta(u,v)
=\frac{\theta e^v}{abc}
\left[b(1-e^{-au})-a(1-e^{-bu})\right].
\tag{3.4}
\]

Let

\[
q(u)=b(1-e^{-au})-a(1-e^{-bu}).
\]

Then

\[
q(0)=0,
\qquad
q'(u)=ab(e^{-au}-e^{-bu})>0\quad(u>0),
\tag{3.5}
\]

because `0<a<b`, and

\[
\lim_{u\to\infty}q(u)=b-a=1.
\tag{3.6}
\]

Therefore (3.3) is pointwise strict for every `u>0`. This is the B29 boundary diagnosis: the old basis is tangent at the origin but leaves a nonzero large-gap remainder.

## 4. B27: integrate the exact excess on the strict edge chain

For one edge triple, condition on the first layer and write

\[
u_0=\max(A_{-1},A_0,A_1),\quad
u_1=\max(A_0,A_1),\quad
u_2=A_1,
\]

so `u_0>=u_1>=u_2`, and set `Y_i=u_i+B_i` with independent `B_i~Exp(1)`.

On the strict chain

\[
Y_0>Y_1>Y_2,
\tag{4.1}
\]

the mixed-sign gaps are `u=Y_0-Y_1>0` and `v=Y_2-Y_1<0`. Define

\[
T_1=\mathbb E[e^{(\theta-1)Y_1+Y_2};(4.1)],
\tag{4.2}
\]

\[
T_2=\mathbb E[e^{Y_2-aY_0};(4.1)],
\tag{4.3}
\]

and the new transform

\[
T_3=\mathbb E[e^{Y_1+Y_2-bY_0};(4.1)].
\tag{4.4}
\]

Multiplying (3.2) by the inherited factor `e^{theta Y_1}` and expanding the two exponentials gives the **exact** edge correction beyond the global envelope:

\[
\boxed{
E_{\rm edge}^{\rm exact}
=\frac{\theta}{ab}(T_1-T_2)-\kappa(T_1-T_3).
}
\tag{4.5}
\]

The previous checkpoint retained only

\[
E_{\rm edge}^{\rm old}
=\frac{\kappa}{a}(T_1-T_2).
\tag{4.6}
\]

Equation (3.4) proves directly that the difference between (4.5) and (4.6) is positive, without relying on numerical sampling.

## 5. B21: the new transform is an exact exponential-gap moment

Fix `u_0>=u_1>=u_2`. Under the shifted-exponential density, the integrand in (4.4) cancels the `Y_1,Y_2` density factors. Hence

\[
\begin{aligned}
T_3\mid u
&=e^{u_0+u_1+u_2}
\int_{u_0}^\infty e^{-cy_0}
\int_{u_1}^{y_0}\int_{u_2}^{y_1}dy_2\,dy_1\,dy_0\\
&=\frac{e^{u_1+u_2-bu_0}}2
\left[
\frac{(u_0-u_2)^2-(u_1-u_2)^2}{c}
+\frac{2(u_0-u_2)}{c^2}
+\frac2{c^3}
\right].
\end{aligned}
\tag{5.1}
\]

The inner two integrations give

\[
\frac12\left[(y_0-u_2)^2-(u_1-u_2)^2\right],
\]

and the last integral follows from the first two moments of an exponential variable. This proves (5.1) on the page.

On each of the six strict order cones for `(A_{-1},A_0,A_1)`, every `u_i` is an order statistic. If an exponential monomial tilts the three independent spacing variables to rates `r_j>0`, then for a gap

\[
D=\sum_{j\in J}Z_j,\qquad Z_j\sim \mathrm{Exp}(r_j)\text{ independent},
\]

one has exactly

\[
\mathbb E D=\sum_{j\in J}\frac1{r_j},
\qquad
\mathbb E D^2=\left(\sum_{j\in J}\frac1{r_j}\right)^2+\sum_{j\in J}\frac1{r_j^2}.
\tag{5.2}
\]

Thus every term in (5.1), as well as the already established formulas for `T_1,T_2`, is a rational function of rational `theta`. No continuous-path simulation, floating optimization, or finite sampling enters the certificate.

## 6. Exact certificate at a new rational Chernoff point

Take

\[
\theta=\frac{733}{1250}=0.5864,
\qquad
a=\frac{517}{1250},\quad
b=\frac{1767}{1250},\quad
c=\frac{3017}{1250}.
\tag{6.1}
\]

The exact checker reconstructs the entire inherited global-envelope correction, verifies the old closed-form edge identity `P2=P2_closed`, and obtains

\[
T_1\approx0.604500935755453,
\quad
T_2\approx0.405020327261966,
\quad
T_3\approx0.223946377991763.
\tag{6.2}
\]

The old and exact per-edge corrections are

\[
E_{\rm edge}^{\rm old}\approx0.082893844524077,
\qquad
E_{\rm edge}^{\rm exact}\approx0.134666362413922,
\tag{6.3}
\]

with exact positive residual

\[
E_{\rm edge}^{\rm exact}-E_{\rm edge}^{\rm old}
=\frac{593694737268844997570037841796875000000}
{11467372294544881657837765193394436395261}>0.
\tag{6.4}
\]

There are two reflected edges. Inserting their exact correction into the inherited four-step block formula gives the exact rational `U_4` archived by the checker, numerically

\[
U_4\approx1047.684404290162547.
\tag{6.5}
\]

Now choose

\[
A=\frac{29648439}{10000000}=2.9648439,
\qquad
x=4\theta A=\frac{21732305787}{3125000000}.
\tag{6.6}
\]

For `x>0`, the positive Taylor partial sum

\[
S_{32}(x)=\sum_{k=0}^{32}\frac{x^k}{k!}
\]

satisfies `S_32(x)<e^x`. The exact rational computation proves

\[
S_{32}(x)-U_4>0,
\qquad
S_{32}(x)-U_4\approx1.81516256588\times10^{-4}.
\tag{6.7}
\]

Consequently

\[
U_4<S_{32}(x)<e^{4\theta A}.
\]

The already proved four-step block Chernoff lemma therefore yields

\[
\boxed{G_1(0)\le \frac{29648439}{10000000}=2.9648439.}
\tag{6.8}
\]

Applying the previously proved D0025 plateau transfer gives

\[
\boxed{
\Delta_2(Q)\ge \frac1{4G_1(0)}
\ge \frac{2500000}{29648439}
\approx0.084321471359757.
}
\tag{6.9}
\]

Hence the frozen metric moves rigorously from

\[
\frac{2500000}{29649457}
\quad\text{to}\quad
\frac{2500000}{29648439},
\]

with exact gain

\[
\boxed{
\frac{2500000}{29648439}-\frac{2500000}{29649457}
=\frac{2545000000}{879060117247623}>0.
}
\tag{6.10}
\]

This is a quantitative theorem only for the frozen `K=2` binary environment and remains **PARTIAL** for the source's general problem.

## 7. Exact artifacts and readback

Idea before code:

- `artifacts/hard7_2026-09-18/HARD7-03/20260919T1221Z__idea-exact-mixed-sign-edge-kernel.md`
- commit `98ab11a3968ca2970d9a44eccfe3bb8af47533e9`

Exact checker:

- `artifacts/hard7_2026-09-18/HARD7-03/exact_edge_kernel_20260919T1221Z.py`
- commit `aea05494363b93bc675d2c3c61a4683f9cd84768`

Executed output:

- `artifacts/hard7_2026-09-18/HARD7-03/exact_edge_kernel_20260919T1221Z.out`
- commit `674547b746e2048be656c2fc575bd950ecaf7886`

All three commits were read back successfully. The executed output ends

`ALL_EXACT_CHECKS_PASS = True`.

These are self-checks, not independent closure audits.

## 8. What the methods actually changed

- **B29 succeeded:** the point `u=+infinity` reveals a unit limiting bracket in (3.6), proving that the previous coefficient-sharp-at-zero lower bound necessarily discards positive mass away from the origin.
- **B27 succeeded:** integrating the exact mixed-sign kernel before collapsing it to a universal coefficient introduces `T_3` and increases the edge correction by the exact positive amount (6.4).
- **B21 succeeded:** the new transform is not a new high-dimensional integral; it is a second-moment calculation for independent exponential spacings, making the improvement exactly certifiable with rational arithmetic.

The next mathematically natural route is to apply the same exact-kernel integration to the near-edge and central mixed-sign branches, where the global exponential envelope still discards positive `u`-dependent mass. A distinct route is to optimize the exact edge formula jointly in `theta` and a finite family of branch-specific transforms, but only after an analytic decomposition is written down before code.

## 9. Model/scheduler capability honesty

The task interface available to this worker exposes scheduling fields such as title, prompt, schedule/timing mode, and enabled state. It still exposes **no model selector, reasoning-effort selector, or guaranteed execution-duration field**. GPT-6 maximum therefore remains a prompt request only. To make it an enforceable scheduler setting, the platform would have to expose model and reasoning fields in the automation interface. This execution actually ran as **GPT-5.6 Sol / reasoning UNVERIFIED**.

For any task whose native interface returns `You cannot modify this task`, including the historically reported P26 case, this worker has no legitimate bypass. The remedy is modification from the owning account/workspace with edit permission or platform/support repair of the task ownership/permission state; creating a duplicate job would violate the owner directive. No other schedule was created, modified, enabled, disabled, or replaced in this run.

## 10. Ledger delta for the shared-root maintainer

```text
track: HARD7-03
target: D0025 / Seppalainen Problem 4
status: PARTIAL
metric: L <= Delta_2(Q)
before: 2500000/29649457
after: 2500000/29648439
movement: +2545000000/879060117247623
methods: B29,B27,B21
unchanged_run_count: 0
stuck: false
shared_roots_modified: none
```

No closure is claimed, so no paper folder or closure-audit request is triggered.