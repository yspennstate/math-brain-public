Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not an authenticated configurable native setting. SOURCE METRIC NO MOVEMENT: rigorous/repository-supported `kappa=-1` bracket width `6.01666046494 -> 6.01666046494`. Three materially different attacks this run: (1) projective slope-simplex / dual-feasibility normal form for the third-full overlap sector; (2) sharp one-step hinge-kernel semiconvexity with explicit outer-tail control for the nested score/KL moments; (3) differentiation in the prescribed positive comparison gap to obtain a one-dimensional stationary-branch continuation bound.**

# PROB10-03 — R14 bounded substantive iteration: projective third-full chart and uniform tail control

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN / NO NEW RIGOROUS SOURCE ENDPOINT / NEW EXACT THIRD-FULL CERTIFICATION LEMMAS**.

## 1. Contract, continuity, ownership, and exclusions consumed

Read before new mathematics:

- `operations/PROB10_2026-09-20.md` on current `master`;
- root `POSTED.md`; the owner's posted Ising/zero-margin perceptron work remains excluded and does not close this continuous negative-margin exact-sphere target;
- `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`; it still records the intervening successor and is **not** overwritten by this owner-directed PROB10 route;
- immutable Campbell refocus handoff `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`, preserving navigation point `3846db33296cfb6eea59ff7c488929087c7b62a2`;
- newest preceding own R14 report `runs/prob10_2026-09-20/PROB10-03/20260920T0804Z_r14_scale_euler_four_scalar_b81c.md`;
- newest relevant complementary T03 reports, especially NM13-03 `2026-09-20__t03-entropy-kl-alpha1228723.md` and NM13-07 `2026-09-20__t03-posgap4d-certified-microextend-1231963484.md`;
- older R14 negative-margin obstruction/reduction chain rather than restarting the problem.

The newest complementary NM13-07 report strictly improved the review-pending directed-interval complete-second endpoint to `12.31963484`. That update is consumed here as the entering baseline; it is not attributed to R14.

No canonical claim, root ledger, peer report, scheduler state, cadence, task enabled state, permission, workflow, email, Drive item, public posting, or concurrent worker file was edited.

## 2. Exact source target, probability convention, and literature scope

Frozen source model:

\[
M=\lfloor \alpha N\rfloor,\qquad g_a\stackrel{iid}{\sim}N(0,I_N),\qquad
\|\sigma\|_2=\sqrt N,
\]

\[
\langle g_a,\sigma\rangle\ge -\sqrt N\quad(1\le a\le M),
\]

with fixed `alpha` and `N -> infinity`.

A **lower** endpoint means SAT probability tends to one. An **upper** endpoint means SAT probability tends to zero. Changed-radius algorithms, Ising weights, restricted-overlap ansatzes, replica/full-RSB numerics, and unsupported finite-lift stationary points are not source endpoints.

Bounded primary/current-source refresh on 20 September 2026:

- El Alaoui--Sellke, arXiv:2010.15811: exact Gaussian spherical model, but for negative `kappa` the algorithm uses conjectural FRSB/Parisi structure and returns a feasible point on radius `sqrt(qbar N)` with `qbar<1`; this is not the exact-radius threshold theorem.
- Stojnic, arXiv:1306.3980 and arXiv:2312.16531: rigorous RDT/fl-RDT framework and stationarized lifting equations; the 2023 paper explicitly says practical operation requires substantial numerical work. Its finite-lift displayed values are therefore not imported as directed-interval source endpoints.
- Montanari--Zhong--Zhou, arXiv:2110.15824: rigorous lower/upper information-theoretic bounds and the LP success mechanism supplying the retained SAT lower endpoint, but not the exact `kappa=-1` threshold.
- Annesi--Malatesta--Zamponi, arXiv:2410.06717: full-RSB SAT/UNSAT calculation under a full-RSB ansatz, used only as structural guidance.
- Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026: exact thresholds for a dimension-free Lipschitz algorithm class while distinguishing the unrestricted feasible-projection problem.

A bounded fresh search did not surface a later primary theorem plainly closing the unrestricted exact-radius `kappa=-1` target. This is dated negative evidence, not a worldwide novelty or priority certificate.

## 3. Entering source metric

After consuming the newer NM13-07 certificate, the repository-supported bracket entering this run is

\[
\alpha_L=6.30297437506,\qquad
\alpha_U=12.31963484,
\]

\[
W=\alpha_U-\alpha_L=6.01666046494.
\]

The `12.31643335693...` positive-gap third-full point and the `12.28722222159...` third-full capacity zero remain **NUMERICAL / CONDITIONAL** because the four-dimensional nested Gaussian root has not been outward certified.

## 4. Attack 1 — projective slope-simplex normal form

Full proof was written before the checker in

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0853Z_r14_projective_tail_continuation.md`

creation commit

`63cdb645774a7df9ab71b44dc27a77afcb07b6a5`.

Retain the strict third-full overlap domain

\[
0<p_3<p_2<1,\qquad 0<q_3<q_2<1.
\]

Set

\[
w_0=1-p_2,\quad w_1=p_2-p_3,\quad w_2=p_3,
\]

and the three secant slopes

\[
r_0=\frac{1-q_2}{w_0},\quad
r_1=\frac{q_2-q_3}{w_1},\quad
r_2=\frac{q_3}{w_2}.
\]

The already-proved strict q-sector cone is

\[
r_1>r_2>0,\qquad r_1^2<r_0r_2.
\]

Define the projective coordinates

\[
x=\frac{r_0r_2}{r_1^2}>1,\qquad y=\frac{r_1}{r_2}>1,
\]

and

\[
Z=xy^2w_0+yw_1+w_2.
\]

### Theorem R14-T03-PROJECTIVE

The transformation is bijective between the strict overlap cone and

\[
w_i>0,\quad w_0+w_1+w_2=1,\quad x>1,\quad y>1,
\]

via

\[
r_2=Z^{-1},\qquad r_1=yZ^{-1},\qquad r_0=xy^2Z^{-1},
\]

\[
p_2=1-w_0,\quad p_3=w_2,\quad
q_3=\frac{w_2}{Z},\quad q_2=\frac{yw_1+w_2}{Z}.
\]

Most importantly, the complete third-full q-sector reconstruction becomes

\[
\boxed{
c_2=\frac{(x-1)\sqrt Z}{xyw_0},\qquad
c_3=\frac{(y-1)\sqrt Z}{yw_1},\qquad
\gamma_p=\frac{xy}{2\sqrt Z}.}
\]

The two cancellation-prone q-Gaussian denominators simplify exactly to

\[
\boxed{A_q=\frac{y}{\sqrt Z},\qquad D_q=\frac1{\sqrt Z},}
\]

so

\[
\frac{A_q}{2\gamma_p}=\frac1x,\qquad \frac{D_q}{A_q}=\frac1y.
\]

The remaining hierarchy inequality `c2>c3>0` is equivalent to the single elementary inequality

\[
\boxed{(x-1)w_1>x(y-1)w_0.}
\]

This chart therefore builds the overlap cone, positivity of `Aq,Dq`, and the log arguments into the coordinates instead of asking interval arithmetic to rediscover them.

### Scale and prescribed-gap simplification

The previous exact scale-Euler quantity becomes

\[
S=\frac{r_1}{r_0\sqrt{r_2}}=\frac{\sqrt Z}{xy}.
\]

For prescribed comparison gap `delta>=0`, `Psi3=delta`, the exact reconstruction is

\[
\gamma_{sq}=\frac12\left(\frac{\sqrt Z}{xy}+\delta\right),
\]

\[
\boxed{B(\delta)=
\frac{(x-1)\sqrt Z}{2w_0(\sqrt Z+\delta xy)}.}
\]

At capacity (`delta=0`) this collapses further to

\[
\boxed{B=\frac{x-1}{2w_0}.}
\]

This removes the subtraction `r0 r2-r1^2` from the previous B formula.

### New c-sector normal form and structural positivity

Define

\[
k(y)=\frac{y(y\log y-y+1)}{(y-1)^2},\qquad
h(x)=\frac{x(x-1-\log x)}{(x-1)^2}.
\]

Exact substitution into the q-Gaussian c-derivatives gives

\[
\boxed{A_{c_3}=\frac{w_1}{2Z}\{w_2+w_1k(y)\},}
\]

\[
\boxed{A_{c_2}=\frac{w_0}{2}
\left\{1-\frac{xy^2w_0}{Z}h(x)\right\}.}
\]

For `x,y>1`, `k(y)>0` and `0<h(x)<1`. Since `xy^2w0/Z=1-q2<1`, this yields the strict analytic bounds

\[
\boxed{A_{c_3}>\frac{w_1w_2}{2Z}>0,\qquad
A_{c_2}>\frac{w_0q_2}{2}>0.}
\]

These signs had previously been part of the interval-certification burden. They are now theorems throughout the projective cone.

## 5. Attack 2 — sharp kernel semiconvexity and explicit outer-tail envelopes

For the exact one-step hinge kernel

\[
f(x)=\mathbb E_H\exp[-B(x+sH)_+^2],\qquad u(x)=\log f(x),
\]

with `B>0`, `s>0`, put `A=1+2Bs^2`.

### Theorem R14-T03-KERNEL-CURVATURE

Globally on the real line,

\[
\boxed{-\frac{2B}{A}\le u_{xx}(x)\le0.}
\]

The upper bound is log-concavity: `exp(-B y_+^2)` is log-concave and Gaussian convolution preserves log-concavity.

For the lower bound, write

\[
e^{-By_+^2}=e^{-By^2}e^{By_-^2}.
\]

The second factor is log-convex. Completing the square in the Gaussian convolution factors `f` as

\[
A^{-1/2}e^{-Bx^2/A}
\times
\mathbb E e^{B( x/A+sZ/\sqrt A)_-^2}.
\]

Gaussian convolution preserves log-convexity by Hölder. Therefore `u(x)+Bx^2/A` is convex, proving the lower bound.

If `rho_x` is the normalized one-step tilted H-law, differentiation and monotone exponential tilting give

\[
u_B=-\mathbb E_{\rho_x}(x+sH)_+^2,
\qquad
u_x=-2B\mathbb E_{\rho_x}(x+sH)_+,
\]

and therefore

\[
0\le -u_B\le x^2+s^2,
\]

\[
|u_x|^2\le4B^2(-u_B)\le4B^2(x^2+s^2),
\]

\[
0\le-u\le B(x^2+s^2).
\]

### Nested outer-tail consequence

Write

\[
d^2=p_2-p_3,\qquad a(v)=\sqrt{p_3}v-1,\qquad X=dU+a(v),
\]

and let `<.>_v` be the exact inner tilted U-law. For

\[
F(v)=\log\mathbb E_U e^{m u(X)},
\]

one has

\[
F''(v)=mp_3\langle u_{xx}\rangle_v
+m^2p_3\operatorname{Var}_v(u_x).
\]

Prekopa gives `F''<=0`, while the kernel lower curvature bound gives

\[
\boxed{-\frac{2mBp_3}{A}\le F''(v)\le0.}
\]

Thus, if `S0>=|<u_x>_0|` and

\[
C_1=\frac{2B\sqrt{p_3}}{A},
\]

then

\[
|\langle u_x\rangle_v|\le S_0+C_1|v|.
\]

The inner tilted U-law is 1-strongly log-concave, so Brascamp--Lieb gives `Var_v(U)<=1`. Gaussian integration by parts gives `<U>_v=md<u_x>_v`. Consequently

\[
E_2(v)=1-p_3+
\left(|a(v)|+md^2[S_0+C_1|v|]\right)^2
\]

bounds `<X^2+s^2>_v`. Hence every nonlinear moment needed by the entropy-stable four-overlap compiler has an explicit quadratic outer envelope:

\[
\langle u_x\rangle_v^2\le(S_0+C_1|v|)^2,
\]

\[
\langle u_x^2\rangle_v\le4B^2E_2(v),
\]

\[
\langle -u_B\rangle_v\le E_2(v),
\]

\[
-\langle u\rangle_v\le B E_2(v).
\]

For the KL residuals from NM13-03,

\[
0\le D_U(v)\le mB[1-p_3+a(v)^2],
\]

\[
0\le D_H(v)\le mB E_2(v).
\]

Thus the outer V-tail of every score/KL quantity needed by `(R3,R2,RU,RH)` is reduced to closed Gaussian tail moments. For example,

\[
\mathbb E[(C_0+C_1|V|)^2\mathbf1_{|V|>T}]
\]

is bounded explicitly by

\[
2\{C_0^2Q(T)+2C_0C_1\phi(T)+C_1^2[T\phi(T)+Q(T)]\}.
\]

This removes the previously unproved **outer-tail** layer of a directed-interval third-full certificate. It does not by itself enclose the compact inner integral.

## 6. Attack 3 — prescribed-gap branch deformation

Let a smooth strict-interior full-stationary branch be parametrized by `alpha`, and put

\[
\delta=\Psi_3.
\]

The exact stationary envelope identity is

\[
\frac{d\Psi_3}{d\alpha}=-\frac{Q}{c_3}>0.
\]

Therefore, wherever the stationary Jacobian is nonsingular,

\[
\boxed{\frac{d\alpha}{d\delta}=-\frac{c_3}{Q}>0.}
\]

NM13-03's exact power-mean collapse gives `L<=Q<=mL<0`, with `m=c3/c2` and `L` a one-dimensional Gaussian expectation. Hence

\[
\boxed{
\frac{c_3}{-L}
\le \frac{d\alpha}{d\delta}
\le \frac{c_2}{-L}.}
\]

Once one third-full stationary point is rigorously certified, this gives an exact route for transporting density along positive comparison gap using a one-dimensional envelope rather than repeatedly enclosing the full nested objective.

## 7. Negation / falsification test

The projective chart is **not** automatically a better Euclidean conditioning chart. At the already archived `delta=10^-3` numerical waypoint, a finite-difference scout gives a substantially worse raw Euclidean condition number in `(w0,w2,x,y)` than in `(p2,p3,q2,q3)` (approximately `5.2e4` versus `2.7e3`). Therefore I reject the tempting stronger claim that the coordinate change by itself solves the Krawczyk conditioning problem.

What survives rigorously is more useful and narrower: the projective chart removes q-sector cancellation/domain checks, while a weighted/preconditioned Krawczyk map is still needed for the residual root.

The analytical sharp-curvature theorem was also numerically falsification-tested on a grid at the existing `delta=10^-3` waypoint; no violation was found. This grid is not the proof.

## 8. Executed exact/symbolic checks

Checker source:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0853Z_r14_projective_tail_continuation.py`

creation commit

`108f7f57613a31d5e174806bd7bdf66aa2f5a0b0`.

Archived executed output:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0853Z_r14_projective_tail_continuation.out`

creation commit

`e0f194b1f484795ec682adc94c126fb1d6dd6f41`.

The exact SymPy section verifies:

- the projective q-sector reconstruction;
- the exact `Aq,Dq` and log-ratio formulas;
- the simplified `A_c2,A_c3` identities;
- the prescribed-gap B reconstruction.

The output ends

`ALL_EXACT_SYMBOLIC_CHECKS_PASS`

and separately

`ALL_NUMERICAL_FALSIFICATION_CHECKS_PASS`.

The numerical section is explicitly a self-check only; it is not an independent audit and no numerical value is promoted to a source endpoint.

## 9. Before/after source metric and auxiliary movement

### Source metric

Before:

`alpha_L = 6.30297437506`,

`alpha_U = 12.31963484`,

`W = 6.01666046494`.

After:

`alpha_L = 6.30297437506`,

`alpha_U = 12.31963484`,

`W = 6.01666046494`.

**Source movement: none.**

The numerical positive-gap point `alpha≈12.31643335693` is not a rigorous endpoint. The numerical capacity zero `alpha≈12.28722222159` is not a rigorous endpoint.

### Exact auxiliary movement

1. Bijection from the strict overlap cone to a positive simplex plus `x>1,y>1`, with cancellation-free q-sector reconstruction.
2. Automatic formulas `Aq=y/sqrt(Z)`, `Dq=1/sqrt(Z)` and exact hierarchy test `(x-1)w1>x(y-1)w0`.
3. Exact positive normal forms and structural lower bounds for `A_c2,A_c3`.
4. Sharp global one-step curvature `-2B/(1+2Bs^2)<=u_xx<=0`.
5. Explicit quadratic outer-tail envelopes for all score/KL moments used by the entropy-stable four-overlap residual.
6. Exact prescribed-gap continuation law with one-dimensional slope bounds.

## 10. Remaining full-scope gap and next source-moving obligation

The source target remains **OPEN / PARTIAL**. The remaining third-full certification problem is now narrower but not solved.

A bracket-moving run must:

1. take the existing `delta=10^-3` waypoint only as a numerical center;
2. choose a small overlap or projective box and prove the strict hierarchy inequality throughout it;
3. use the new analytical quadratic envelopes to remove the outer `|V|>T` tails rigorously;
4. outward-enclose the remaining compact two-level Gaussian score/KL integrals on `|V|<=T`, with all parameter dependence retained;
5. build a weighted/preconditioned interval Jacobian and prove a Krawczyk/contraction inclusion for the four residuals `(R3,R2,RU,RH)`;
6. only after a true root is certified invoke the exact prescribed-gap identity `Psi3=delta>0` and the source comparison implication to promote its reconstructed `alpha` to an upper endpoint;
7. retain the required independent source/theorem review before any closure claim.

The new projective chart should be used for cancellation/domain control, **not** as an unproved conditioning shortcut.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  task: PROB10-03
  worker_route: R14 owner-refocused complementary route
  status: PARTIAL
  exact_target: negative-margin spherical Gaussian perceptron, kappa=-1, exact sphere
  probability_convention:
    lower: "SAT probability -> 1"
    upper: "SAT probability -> 0"
  source_metric_before:
    alpha_L: "6.30297437506"
    alpha_U: "12.31963484"
    width: "6.01666046494"
  source_metric_after:
    alpha_L: "6.30297437506"
    alpha_U: "12.31963484"
    width: "6.01666046494"
  source_movement: none
  auxiliary_movement:
    - "projective slope-simplex bijection and cancellation-free q-sector"
    - "automatic positivity of Aq,Dq and exact hierarchy inequality"
    - "closed positive normal forms for A_c2 and A_c3"
    - "sharp global hinge-kernel semiconvexity"
    - "explicit outer Gaussian-tail envelopes for all entropy-stable score/KL moments"
    - "one-dimensional prescribed-gap branch derivative bounds"
  numerical_only:
    positive_gap_waypoint_alpha: "~12.31643335693 at delta=1e-3"
    capacity_zero: "~12.28722222159"
    projective_raw_conditioning: "worse than old coordinates; weighted preconditioning still required"
  exact_artifacts:
    proof: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0853Z_r14_projective_tail_continuation.md @ 63cdb645774a7df9ab71b44dc27a77afcb07b6a5"
    checker: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0853Z_r14_projective_tail_continuation.py @ 108f7f57613a31d5e174806bd7bdf66aa2f5a0b0"
    output: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0853Z_r14_projective_tail_continuation.out @ e0f194b1f484795ec682adc94c126fb1d6dd6f41"
  campbell_handoff_preserved: "artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md"
  independent_audit: none_this_run
```

No source closure is claimed. No scheduler/cadence/enabled-state change was attempted.
