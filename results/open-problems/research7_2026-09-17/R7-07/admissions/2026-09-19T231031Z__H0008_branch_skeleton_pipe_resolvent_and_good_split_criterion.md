Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding scheduler selector is exposed.**

# R7-07 admission-feasibility mathematics — H0008 branch-skeleton compression, exact pipe resolvent, and a good-split criterion

Date: 2026-09-19 UTC  
Worker: `R7-07` / native identity `6aabe8413f60819197825dd81ca138ae`  
Repository: private `yspennstate/math-open-problems`, branch `master`  
Status: **PENDING_ADMISSION**. This artifact does **not** acquire H0008.  
Methods: **B16 COMPUTE SMALL CASES / B7 TAKE THE LIMIT / B25 COUNT THE SAME THING TWICE**.

## 1. Source, ownership, and continuity

The released source under bounded feasibility study remains Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3, open problem (6), **Boundary fluctuations**. This note addresses only the finite-type harmonic-measure side and does not close the source item.

Canonical history `operations/claims/H0008.md` records H0008 as `UNASSIGNED AFTER R14 HANDOFF / SOURCE OPEN / PARTIAL / RELEASED BY R14 AFTER SECTION-I EXHAUSTION`. Because that canonical path already exists, R7-07's create-only acquisition rule forbids overwriting it. R7-07 remains `PENDING_ADMISSION`; no source metric or stagnation clock is started.

The immediately preceding own report is `research7_2026-09-17/R7-07/runs/2026-09-19/2026-09-19T220912Z__report.md` at creation commit `4faf713c2042559392c9bc30fab69f5ca5242215`. Its main new fact was that every fixed positive Renyi conjugation is only an endpoint conductance gauge and has the same quenched exponential rate as the base killed harmonic operator. Thus the right object is the base two-ray Green mass itself.

## 2. Inherited electrical notation and exact target

On a fixed locally finite transient rooted tree, let `B_v` be the probability that simple random walk from `v` never crosses the edge to its parent. For the positive-conductance children of `v`, write

\[
S_v=\sum_u B_u,\qquad B_v=\frac{S_v}{1+S_v},\qquad p_v(u)=\frac{B_u}{S_v}.
\tag{2.1}
\]

Let

\[
(P_2f)(v)=\sum_up_v(u)^2f(u)
\tag{2.2}
\]

be the sub-Markov kernel followed while two independent harmonic rays have not split. If `tau>=1` is their common-prefix lifetime, previous R7-07 work established

\[
\boxed{E_T\tau=\frac1{B_o},\qquad E_T\tau^2=2GV(o)-V(o),\qquad V=1/B,\qquad G=\sum_{n\ge0}P_2^n.}
\tag{2.3}
\]

It also established

\[
\boxed{\widehat P_0^n1(o)=B_oE_T[(\tau-n)_+],\qquad \sum_{n\ge0}\widehat P_0^n1(o)=\frac{B_o}{2}E_T[\tau(\tau+1)],}
\tag{2.4}
\]

where `widehat P_0=(1-B)K_H`. Hence the present feasibility gate is

\[
\boxed{E_{P_i}E_T\tau^2<\infty\quad\text{for each finite source type }i.}
\tag{2.5}
\]

This is sufficient for the earlier failed-excursion/regeneration-roof route; it is not asserted necessary for every possible stationary-environment construction.

---

# Part I. B16 — exact small models expose the pipe contribution

## 3. Positive backbone and exact-pipe vertices

Call a child `u` **positive** if `B_u>0`, and put `N_v=#{u:B_u>0}`. On the positive backbone `N_v>=1`. A vertex is an **exact pipe vertex** if `N_v=1`, and a **genuine branch vertex** if `N_v>=2`.

At an exact pipe vertex, harmonic selection is deterministic. If `u` is its unique positive child,

\[
B_v=\frac{B_u}{1+B_u},
\]

so with `U=1/B`,

\[
\boxed{U_v=U_u+1.}
\tag{3.1}
\]

Thus a run of exact pipes is literally a series-resistance segment.

## 4. Exact source-law pipe resolvent

This subsection extracts a renewal consequence from R14's already-proved extinction-Jacobian subcriticality. The strict inequality `rho(J)<1` is inherited from R14 and is **not** claimed as new here.

Use the finite-type branching parametrization already employed in the H0008 handoff. Let `a_ij=q_j p_ij`, let `G` be the offspring pgf, and put

\[
s_i=P_i(B>0),\qquad t_i=\sum_j a_{ij}s_j,
\tag{4.1}
\]

so

\[
s_i=1-G(1-t_i).
\tag{4.2}
\]

For a type-`i` positive vertex, the probability before survival conditioning that there is exactly one positive child and it has type `j` is

\[
a_{ij}s_jG'(1-t_i).
\]

Hence under the source law conditioned on `B>0`, the exact-pipe transition matrix is

\[
\boxed{Q_{ij}=\frac{s_j}{s_i}G'(1-t_i)a_{ij}.}
\tag{4.3}
\]

If `J_ij=G'(1-t_i)a_ij`, then

\[
\boxed{Q=D_s^{-1}JD_s,\qquad D_s=\operatorname{diag}(s_i),}
\tag{4.4}
\]

so `rho(Q)=rho(J)<1`.

Let `L` be the number of consecutive exact-pipe vertices starting from an **unbiased source vertex conditioned on survival** before the first genuine branch. Then

\[
\boxed{P_i(L\ge n)=e_i^TQ^n\mathbf1.}
\tag{4.5}
\]

Put `r=(I-Q)1`. Since `rho(Q)<1`, the first genuine branch occurs almost surely and

\[
P_i(L=\ell)=e_i^TQ^\ell r,\qquad \ell=0,1,2,\ldots.
\tag{4.6}
\]

Consequently

\[
\boxed{E_i z^L=e_i^T(I-zQ)^{-1}(I-Q)\mathbf1,\qquad z\rho(Q)<1,}
\tag{4.7}
\]

and

\[
\boxed{E_iL=e_i^TQ(I-Q)^{-1}\mathbf1,}
\tag{4.8}
\]

\[
\boxed{E_iL^2=e_i^TQ(I+Q)(I-Q)^{-2}\mathbf1.}
\tag{4.9}
\]

Thus all source-law exact-pipe moments are finite, and a nontrivial exponential moment exists.

**Scope qualification.** Equations (4.5)--(4.9) start from the unbiased survival-conditioned source law. A child selected at a genuine branch by harmonic or two-ray weights is conductance-biased, so its law is not automatically `P_j(.|B>0)`. Therefore (4.9) does not prove a uniform pipe-moment bound after arbitrarily many pair-spine branch selections. Promoting it that far would repeat the hidden-normalization error warned about in the R14 handoff.

## 5. Exact one-type check

Take one type, deterministic two potential children, and transmission probability `a=3/4`. The nonzero survival probability solves `s=1-(1-as)^2`, hence

\[
\boxed{s=\frac89,\qquad t=as=\frac23.}
\]

Since `G(z)=z^2`,

\[
Q=J=G'(1-t)a=2\left(\frac13\right)\frac34=\frac12.
\]

Therefore

\[
\boxed{P(L\ge n)=2^{-n},\qquad EL=1,\qquad EL^2=3.}
\tag{5.1}
\]

## 6. A fully solvable regular branch skeleton

Temporarily forget source randomness. Suppose every genuine branch has exactly `b>=2` symmetric arms and every arm between consecutive branch vertices has exactly `L>=1` unit-resistance edges. Branch harmonic probabilities are `1/b`.

Let `K` be the number of consecutive branch choices on which two independent harmonic rays choose the same arm before their first split. Then

\[
P(K=k)=\left(1-\frac1b\right)b^{-k},\qquad EK=\frac1{b-1},\qquad EK^2=\frac{b+1}{(b-1)^2}.
\]

The common-prefix lifetime is `tau=1+LK`, hence

\[
\boxed{E\tau^2=1+\frac{2L}{b-1}+\frac{(b+1)L^2}{(b-1)^2}.}
\tag{6.1}
\]

For `b=2,L=3`, this gives `E tau^2=34` exactly.

If instead the successive pipe lengths are iid positive integers with `mu_1=EL_1` and `mu_2=EL_1^2`, independent of the symmetric branch choices, then

\[
\boxed{E\tau^2=1+\frac{2\mu_1+\mu_2}{b-1}+\frac{2\mu_1^2}{(b-1)^2}.}
\tag{6.2}
\]

Thus in this solvable deformation

\[
\boxed{E\tau^2<\infty\iff EL_1^2<\infty.}
\tag{6.3}
\]

**B16 outcome.** Exact small models show quantitatively that long pipes create a quadratic cost. They can make the roof constant large, but an exponential pipe tail cannot by itself generate an infinite second moment in the symmetric branch model.

---

# Part II. B7 — compress exact pipes and take the long-pipe limit

## 7. The branch skeleton as an exact electrical network

Fix a realized transient tree. Suppress every maximal chain of exact-pipe vertices. Keep the root as an anchor even when it is itself a pipe, and keep every genuine branch vertex. Each skeleton edge `e=(x,y)` represents a chain of

\[
L_e=d(y)-d(x)\ge1
\]

original unit-resistance edges. Because series resistances add, the branch skeleton is electrically exact when skeleton edge `e` is assigned resistance `L_e`.

If `S_y` is the total forward conductance at endpoint branch `y`, then the conductance of arm `e`, as seen from `x`, is

\[
\boxed{c_e=\frac1{L_e+1/S_y}=\frac1{L_e-1+1/B_y}.}
\tag{7.1}
\]

The harmonic probability of choosing arm `e` at `x` is

\[
q_x(e)=\frac{c_e}{\sum_{e':x\to *}c_{e'}}.
\tag{7.2}
\]

This is exactly the same harmonic probability as in the unsuppressed tree, because current is constant along a series chain.

**Proof.** Every internal vertex of a suppressed chain has degree two inside the positive backbone and satisfies Kirchhoff's law with the same current entering and leaving. Replacing `L_e` unit resistors in series by one resistor of resistance `L_e` preserves the voltage-drop/current relation on that arm. Performing the replacement on all maximal chains preserves the Dirichlet-to-Neumann map on branch vertices, hence effective conductances, harmonic currents, and branch-choice probabilities. `square`

## 8. Exact selection penalty for a long pipe

Write `ell_e=L_e-1` for the number of internal pipe vertices before the next branch. Then

\[
c_e=\frac1{\ell_e+1/B_y}.
\tag{8.1}
\]

At a genuine branch `x`, let `R_e` be the total conductance of all competing arms. The probability that **both** harmonic rays choose arm `e` is

\[
\boxed{q_x(e)^2=\frac1{\bigl(1+R_e(\ell_e+1/B_y)\bigr)^2}.}
\tag{8.2}
\]

In particular,

\[
\boxed{q_x(e)^2\le\min\left\{1,\frac1{(R_e\ell_e)^2}\right\}\quad(\ell_e\ge1).}
\tag{8.3}
\]

Thus a long pipe is not favored by the two-ray transition. Unless the branch is simultaneously near-pipe in the competitor direction (`R_e ell_e` small), pair selection suppresses the long arm quadratically.

The previously proved source law

\[
P(0<B\le r)\le Ce^{-c/r}
\tag{8.4}
\]

also implies, under a source-Palm view of siblings and finite mean offspring, the same qualitative superexponential rarity for a positive competitor total `R_e` near zero. The event `0<R_e<=r` requires at least one positive sibling with conductance at most `r`, and a union bound over the integrable sibling count yields

\[
P(0<R_e\le r)\le C_1e^{-c_1/r}
\tag{8.5}
\]

for small `r`, with finite-type/Palm-dependent constants.

Hence the only scale on which (8.3) fails to penalize a long length `ell` is `R=O(1/ell)`, while (8.5) assigns that competitor scale an `exp(-c ell)` source cost. This remains a one-branch/source-Palm statement; iterating it under the pair-spine tilted law is the nontrivial point.

## 9. Long-pipe limit in the solvable deformation

Equation (6.1) gives

\[
\boxed{\lim_{L\to\infty}\frac{E\tau^2}{L^2}=\frac{b+1}{(b-1)^2}.}
\tag{9.1}
\]

For iid random pipe lengths in (6.2), a power-tail law `P(L_1>=t) asymp t^{-alpha}` has finite `E tau^2` exactly when `alpha>2`. The H0008 source-law exact-pipe chain instead has an exponential moment by (4.7). Therefore any full-source divergence must be created by **iterated branch-selection bias coupling long pipes to almost-zero competitors**, not by unbiased exact-pipe geometry alone.

**B7 outcome.** Suppressing pipes changes neither the harmonic problem nor the branch split mechanism. The remaining source question can be studied on a weighted branch skeleton; exact pipes contribute explicit series lengths with a source resolvent, while genuine branch points carry all pair-splitting hazard.

---

# Part III. B25 — count Green mass by depth and by skeleton edges

## 10. A subtree electrical identity

Let `theta(v)` be the harmonic cylinder mass of a positive-backbone vertex `v`. The incoming electrical current into `v` is `theta(v)`. The effective forward resistance at `v` is `1/S_v`, so the energy dissipated strictly below `v` by this current is `theta(v)^2/S_v`.

On a unit-resistance tree that same energy is the sum of squared descendant edge currents. Since the edge entering a positive descendant `w` carries current `theta(w)`, Thomson's identity gives

\[
\boxed{\frac{\theta(v)^2}{S_v}=\sum_{w\succ v,\,w\ne v}\theta(w)^2.}
\tag{10.1}
\]

Using `1/B_v=1+1/S_v`,

\[
\boxed{\frac{\theta(v)^2}{B_v}=\sum_{w\succcurlyeq v}\theta(w)^2.}
\tag{10.2}
\]

Summing over `v` and reversing the ancestor-descendant count yields

\[
\boxed{\sum_v\frac{\theta(v)^2}{B_v}=\sum_v(d(v)+1)\theta(v)^2.}
\tag{10.3}
\]

Because `C_n=sum_{|v|=n}theta(v)^2=P_T(tau>n)`, this is equivalently

\[
\boxed{\sum_v(d(v)+1)\theta(v)^2=\sum_{n\ge0}(n+1)C_n=\frac12E_T[\tau(\tau+1)].}
\tag{10.4}
\]

This reproduces the Green identity by direct electrical double count and requires no stationary environment.

## 11. Exact skeleton-edge formula

Group (10.3) by branch-skeleton edges. Let `theta_e` be the harmonic current through `e=(x,y)` and `L_e=d(y)-d(x)`. Current is constant on the `L_e` original vertices after `x` up to and including `y`. Their contribution is

\[
\theta_e^2\sum_{r=1}^{L_e}(d(x)+r+1)=\theta_e^2\left[L_e(d(x)+1)+\frac{L_e(L_e+1)}2\right].
\]

Including the root gives

\[
\boxed{\frac12E_T[\tau(\tau+1)]=1+\sum_{e=(x,y)}\theta_e^2\left[L_e(d(x)+1)+\frac{L_e(L_e+1)}2\right].}
\tag{11.1}
\]

This separates two possible divergence mechanisms: unusually large series lengths `L_e`, and too much squared harmonic current surviving through too many genuine branches. The source resolvent makes the first benign at an unbiased source entrance, while (8.2) shows pair selection penalizes a long arm unless competitors are simultaneously tiny. The unresolved issue is cumulative tilted interaction over many branch renewals.

## 12. Deterministic good-branch criterion

At a genuine branch `x`, define

\[
\Delta_x=1-\sum_{e:x\to *}q_x(e)^2.
\tag{12.1}
\]

This is exactly the probability that two harmonic rays split at that branch, conditional on arriving together.

Fix `delta in (0,1)`. Call a branch **delta-good** if `Delta_x>=delta`. For original depth `n`, let `g_delta(n)` be the minimum, over positive-backbone root-to-level-`n` paths, of the number of delta-good genuine branch ancestors before level `n`.

### Theorem 12.1

For every realized tree,

\[
\boxed{P_T(\tau>n)=C_n\le(1-\delta)^{g_\delta(n)}.}
\tag{12.2}
\]

Consequently, if for some `delta in (0,1)` and `eta>0`, eventually

\[
\boxed{g_\delta(n)\ge\frac{2+\eta}{-\log(1-\delta)}\log(n+2),}
\tag{12.3}
\]

then

\[
\boxed{E_T\tau^2<\infty.}
\tag{12.4}
\]

**Proof.** Compress exact pipes. At branch `x`, the unnormalized pair transition masses are `q_x(e)^2`, with total `s_x=sum_e q_x(e)^2=1-Delta_x`. Conditional on surviving that branch, normalize by `r_x(e)=q_x(e)^2/s_x`. The probability that the rays remain together to level `n` is the Feynman-Kac expectation

\[
C_n=E_r\prod_{x\text{ branch before level }n}s_x.
\tag{12.5}
\]

Every branch path reaching level `n` contains at least `g_delta(n)` good branches. At each good branch `s_x<=1-delta`, and otherwise `s_x<=1`, proving (12.2). Under (12.3), `C_n<=(n+2)^{-2-eta}`. Finally `E tau^2=sum_{n>=0}(2n+1)P(tau>n)`, so the series converges. `square`

### Corollary 12.2

If `E_T tau^2=infinity`, then for every fixed `delta in (0,1)` and every `eta>0`, (12.3) fails infinitely often. Thus a divergence witness cannot merely have long exact pipes or occasional near-pipe branches. It must sustain arbitrarily deep positive-backbone paths overwhelmingly composed of exact/near-pipe branch states.

## 13. Exact remaining obstruction

Source facts now point in the same direction:

- exact-pipe chains from an unbiased surviving source root have the resolvent (4.7) with `rho(Q)<1`;
- small positive conductance has superexponential source tail `exp(-c/B)`;
- at a genuine branch, a long selected arm has exact pair weight (8.2), so avoiding its quadratic length suppression requires a simultaneously tiny competitor;
- only logarithmically many uniformly nondegenerate split points by depth imply the desired pair-overlap second moment.

However the branch state after repeated pair conditioning is not the source law. `Delta_x<delta` depends on descendant conductances and biases the chosen child's future. Replacing the iterated tilted law by the source law would be circular.

The remaining analytic task is therefore to prove, for some fixed `delta>0`, a lower bound of order `c log n` on good branch points under the normalized common-pair spine with `c>2/[-log(1-delta)]`, or any stronger decay making `sum n C_n` finite.

Equivalently, construct a weighted operator for the `delta`-bad branch set and prove its spectral radius is below one. At `delta=0` the operator reduces to the exact-pipe channel whose finite-type boundary is the already-subcritical `J`; the difficult step is a **noncircular perturbation from `delta=0` to small positive `delta` under the pair-spine tilt**. This is narrower than the earlier generic instruction “prove Green summability.”

# 14. Dated source/prior-art check

Bounded current check on 2026-09-19 UTC:

- Kumar arXiv:2608.15987 remains the primary H0008 source record; no later version was surfaced.
- Kumar--Duddala arXiv:2608.21125 remains a companion on front/Bramson and continuous-type limits, not a closure of this finite-type harmonic-measure clause.
- Rousselin's one-type random-environment work remains the closest explicit exit-environment/regeneration architecture.
- Dembo--Sun's multitype Galton--Watson random-walk work supplies critical-bias reversing measures and conductance estimates, but not the transient `lambda=1` multitype harmonic-exit stationary law needed here.
- Lyons--Pemantle--Peres one-type harmonic-measure machinery remains prior art.

Negative search evidence is not proof of worldwide openness or novelty.

# 15. Methods and outcomes

**B16 — COMPUTE EVERY SMALL CASE.** Extracted the exact source-law pipe transition matrix `Q=D_s^{-1}JD_s`, its pgf and first two moments; checked the one-type `nu=2,a=3/4` case exactly (`s=8/9`, `Q=1/2`, `EL=1`, `EL^2=3`); solved the regular weighted-skeleton pair-overlap model exactly.

**B7 — TAKE THE LIMIT.** Suppressed every exact pipe by series reduction, derived the exact long-arm pair-selection factor (8.2), and showed in the solvable deformation that the roof has the sharp pipe second-moment threshold. The source exponential pipe resolvent is not itself the divergence mechanism.

**B25 — COUNT THE SAME THING TWICE.** Counted pair Green mass as depth-weighted collision energy and as a weighted sum over skeleton edges, yielding (11.1). From the normalized branch Feynman-Kac representation, proved the logarithmic good-branch criterion (12.3).

# 16. Honest status and next attack

- R7-07 target: **PENDING_ADMISSION**.
- H0008 source: **OPEN / PARTIAL**.
- H0008 ownership: **UNASSIGNED AFTER R14 HANDOFF**, but canonical path collision prevents R7-07 create-only acquisition.
- Fixed R7-07 source metric: **UNMEASURED -> UNMEASURED**.
- Stagnation count: **NOT_STARTED**.
- No source-level closure, refutation, novelty certificate, or independent audit is claimed.

If no fresh lawful shard-6 source appears first, the next nonrepeating triple should be:

- **B3 PROVE SOMETHING STRONGER:** prove an exponential bound for runs of `delta`-bad branch states under the tilted pair spine;
- **B19 MAKE IT AN ALGORITHM:** formulate the `delta`-bad branch transfer as an explicit positive operator whose spectral radius can be bounded in a source-hypothesis norm;
- **B22 READ THE FAILURES:** compare that operator with the transient-regime limitations in multitype environment-seen-from-particle work and the one-type exit-time regeneration proofs, looking specifically for the missing domination/compactness step.

The cleanest next mathematical target is a perturbation theorem saying that the bad-branch operator remains subcritical for sufficiently small `delta>0`, with `delta=0` anchored by `rho(J)<1`.