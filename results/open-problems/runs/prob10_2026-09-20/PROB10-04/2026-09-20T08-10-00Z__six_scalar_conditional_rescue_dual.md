Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 run 9 — six-scalar conditional entropy dual for the Díaz + rescue count

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN**.

**SOURCE-METRIC NO MOVEMENT.**  For the exact owner-frozen iid proper-clause model, the externally verified explicit-decimal bracket remains

\[
[\alpha_L,\alpha_U]=[3.52,4.4898],\qquad
W=0.9698\longrightarrow0.9698.
\]

This run obeys the required method change after repeated endpoint nonmovement.  It does **not** add another rescue motif or another rounded-saddle tune.  I tried three materially different moves:

1. **all-at-once Gibbs dualization of the complete Díaz objective** — **refuted exactly** because the copy-count block has the wrong curvature;
2. **condition on the bad-curvature copy masses and on three normalized rescue aggregates, then dualize every remaining entropy block** — **succeeds**, giving a rigorous six-scalar outer reduction and an explicit rescue-aware dual formula;
3. **eliminate the three rescue aggregates by a global affine/Fenchel lower bound on their product** — **fails quantitatively and structurally on a domain touching the coordinate hyperplanes**, so the six-scalar formulation is retained.

The auxiliary mechanism metric moves from the source's ambient `K=7223` primal coordinates at `M=23` to **six adversarial outer scalars** plus minimizing dual certificate parameters.  This is not a threshold endpoint and is recorded separately from `W`.

## 1. Continuity, ownership, and evidence consumed

I continued only the scoped cluster-aware weighted-counting / overlap-variational claim in

- `operations/claims/PROB10-04.md`, current blob `1095e6bfb106b53e810af56f2605521abb7143b4`.

I did not override the historical `F0097` claim and did not take over either neighboring T04 route.

Consumed repository state included:

- `operations/PROB10_2026-09-20.md` on current `master`;
- current root `POSTED.md`;
- current scoped claim above;
- the actual pre-refocus HARD7-06 handoff `runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`, which preserves the real F0095 / binary-cascade 3-colourability target and its `W_3<=0.6565076260769` history;
- own preceding report `runs/prob10_2026-09-20/PROB10-04/2026-09-20T06-59-00Z__rescue_variational_scalarization.md` @ commit `fe3f52778da2b85a2f15e0ee9005c247d3c301d3`;
- current interpolation neighbor `proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T06-55-00Z__t04_five_support_438908_upper.md` @ commit `a073864668485dc9126aaa5cbb9d81d1c44c7dcf`, which records **CANDIDATE_FULL pending later independent review** at `4.38908`; I do not promote or audit that candidate in this route;
- current constructive neighbor `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T10-28-30__t04_balanced_cell_polarity_refinement.md`, status OPEN/PARTIAL, which keeps the external bracket unchanged and develops a distinct four-spectrum constructive route.

The mathematical idea and exact missing lemma were frozen **before** any implementation work at

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T07-46-00Z__conditional_rescue_dual_idea_before_code.md`

creation commit `e23e3ccd685bf0f7bcc557ac25c4686702727e75`.

The complete formula/proof ledger is frozen separately at

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T08-03-00Z__six_scalar_rescue_dual_formula.md`

creation commit `ea3828b5744071f93e0bc03655643d5fdbe08809`.

No new program was written in this run: the new claim is an analytic entropy-duality theorem rather than a finite enumeration.  This avoids spending the run manufacturing a checker for an unchanged endpoint.

## 2. Fresh source/model check

The owner-frozen model remains `m=floor(alpha n)` independent clauses, each clause choosing three distinct variables uniformly and then three independent fair signs.

The primary Díaz--Kirousis--Mitsche--Pérez-Giménez paper, <https://arxiv.org/abs/0807.3600>, was reread at the parts actually used here:

- equations (11)--(18): the variable, heavy, clause, copy-partition, variable-to-copy and clause-to-copy linear constraints;
- the definition of the exponential objective `F` preceding their equation (19);
- equations (19)--(21): reduction of the first moment to `B max F` and their `4.4898` bound;
- Appendix E, especially equations (24)--(28): the partition functions, the critical-point expression (25), and the six multiplier equations.

A key source detail for this run is that the paper itself says the validity of its numerical maximization relies on uniqueness of the `3 x 3` critical system and then reports a separate `100^3` sweep over the projected three-dimensional copy-count polytope.  That is exactly the structure the new conditional dual exploits: the copy-count coordinates have the opposite curvature from the remaining entropy blocks.

The current external status remains conservative:

- Hajiaghayi--Sorkin, <https://arxiv.org/abs/math/0310193>, gives the explicit lower endpoint `3.52` in the classical independent-clause model;
- Díaz et al. give `4.4898` for the simple proper model, and the no-repeated-whole-clause coupling transfers that a.a.s. upper bound to the owner's iid-with-replacement proper-clause model with `O(1/n)` collision probability;
- Gaia Carenini, ECCC TR26-145, published 16 August 2026, <https://eccc.weizmann.ac.il/report/2026/145/>, proves an `O(n/log n)` scaling window for every fixed `k>=3`, but this does not identify or prove convergence of the centers to a limiting `alpha_3`;
- the March 27, 2026 fixed-small-`k` status discussion in Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis still states that for `3<=k<k_0` the existence of a uniform satisfiability threshold remains open; Ding--Sly--Sun therefore cannot simply be specialized to `k=3`;
- ESA 2025 studies a different `k`-wise-independent clause model and is not substituted for this target.

The stronger internal `4.38908` neighboring endpoint remains a project candidate pending independent review, not a new external baseline for this report.

## 3. Inherited rescue factor, rewritten in normalized coordinates

The preceding PROB10-04 runs proved an iid-priority one-rescue survival factor for `j=1` true centers.  Write

\[
Q=Q_{safe},\qquad B=B_{can},\qquad
E=\sum_{i=1}^{M}f_{i,1,1},
\]

and

\[
u=\ell_{ps},\qquad v=\ell_{ns1},\qquad w=\ell_{ns2},
\qquad \ell_{nu}=\lambda_n-v-w.
\]

Instead of carrying the three ratios with possible zero denominators, introduce normalized outer coordinates

\[
q=Q/u,\qquad \beta=B/\ell_{nu},\qquad e=E/v
\tag{3.1}
\]

when the denominators are positive and use value zero on the corresponding zero-mass face.  Because `Q` is a subset of `ps` slots, `B` is a subset of `nu` slots, and the eligible leaves contribute distinct `ns1` copies,

\[
0\le q,\beta,e\le1.
\tag{3.2}
\]

The proved asymptotic survival factor is

\[
\prod_{i=1}^{M}s_i^{t_{i,1}n+o(n)},
\qquad
s_i=1-\frac12\beta q^i e.
\tag{3.3}
\]

Thus, globally,

\[
\boxed{1/2\le s_i\le1.}
\tag{3.4}
\]

This normalization is already useful: there is no rescue singularity as `v`, `u`, or `ell_nu` tends to zero.  All new nonlinear rescue data now live in the compact cube `[0,1]^3`.

## 4. Attack 1 — the tempting free global dual is false

The source Appendix E defines positive multipliers and the critical-point expression (25).  A natural idea was to reinterpret (25) as a Gibbs/relative-entropy upper bound valid for **arbitrary** positive multipliers, which would immediately remove all primal optimization.

That idea is false, and the obstruction is exact.

After dualizing the variable and clause negative-entropy blocks, the positive-copy simplex contributes, in the simplest `ps`/`pu` slice with total mass `lambda=1`,

\[
H_r(x)=x\log x+(1-x)\log(1-x)-x\log r,
\qquad r=\nu_{ps}\mu_{ps}>0.
\tag{4.1}
\]

Its stationary point is

\[
x_*={r\over1+r},
\]

and

\[
H_r(x_*)=-\log(1+r).
\tag{4.2}
\]

But

\[
H_r''(x)={1\over x}+{1\over1-x}>0,
\tag{4.3}
\]

so the stationary point is the **minimum**, not the maximum, of this copy block.

For the exact choice `r=2`,

\[
H_2(2/3)=-\log3,
\qquad H_2(0)=0,
\]

and therefore the would-be global inequality would require

\[
0\le-\log3,
\]

which is false.

This precisely explains why the source can use (25) only **after** identifying an interior critical point.  The all-at-once Gibbs dual is not a valid upper certificate.

This failed route is useful: it isolates the only wrong-curvature piece.  Once the copy masses `(ell_ps,ell_ns1,ell_ns2)` are conditioned on, that piece becomes a constant and every remaining entropy block has the correct sign for log-sum duality.

## 5. Attack 2 — six-scalar conditional dual: statement

Let

\[
\theta=(u,v,w,q,\beta,e)
\tag{5.1}
\]

and define the simple compact relaxation

\[
\Omega=\Bigl\{0\le u\le\lambda_p,
\ v,w\ge0,\ v+w\le\lambda_n,
\ 0\le q,\beta,e\le1\Bigr\}.
\tag{5.2}
\]

Every feasible Díaz point maps into `Omega`; `Omega` may contain infeasible points, which is harmless for an upper bound.

For positive

\[
\nu=(\nu_{ps},\nu_{ns1},\nu_{ns2})
\]

define the source light-variable partitions

\[
\Psi_{i,j}(\nu)=
\nu_{ps}^i+(\nu_{ns1}+\nu_{ns2})^j-\nu_{ns2}^j.
\tag{5.3}
\]

For `j=1`, introduce `z>0` and the rescue-modified partition

\[
\boxed{
\Psi^R_{i,1}
=\nu_{ps}^i\left(1-\frac12\beta q^i e\right)+z\nu_{ns1}.}
\tag{5.4}
\]

The variable `z` is the multiplier for the aggregate constraint

\[
E=ev=\sum_i f_{i,1,1}.
\tag{5.5}
\]

For a source extended clause type `alpha`, put

\[
r_Q(\alpha)=ps(\alpha)
\mathbf1\{ps(\alpha)+ns(\alpha)\ge2\},
\tag{5.6}
\]

which counts safe positive slots, and

\[
r_B(\alpha)=
\mathbf1\{\alpha=((0,1),(1,1))
\text{ or }((0,1),(0,2))\},
\tag{5.7}
\]

which counts the one selected canonical `nu` slot in either blocking type that has a `nu` slot.

For positive `mu=(mu_ps,mu_ns1,mu_ns2)` and real tilts `eta,zeta`, define

\[
\boxed{
\Psi_k^{Q,B}(\mu;\eta,\zeta)
=\sum_{\alpha:p(\alpha)=k}
{2\over w(\alpha)!}
\mu_{ps}^{ps(\alpha)}
\mu_{ns1}^{ns1(\alpha)}
\mu_{ns2}^{ns2(\alpha)}
\exp\{\eta r_Q(\alpha)+\zeta r_B(\alpha)\}.}
\tag{5.8}
\]

The fixed copy term is

\[
\begin{aligned}
C_\ell(u,v,w)=\;&u\log u+(\lambda_p-u)\log(\lambda_p-u)\\
&+v\log v+w\log w
+(\lambda_n-v-w)\log(\lambda_n-v-w),
\end{aligned}
\tag{5.9}
\]

with `0 log 0=0`.

For the nine dual parameters

\[
y=(\nu_{ps},\nu_{ns1},\nu_{ns2},
\mu_{ps},\mu_{ns1},\mu_{ns2},z,\eta,\zeta),
\tag{5.10}
\]

where the first seven are positive and `eta,zeta` are real, define

\[
\begin{aligned}
\mathcal D(\theta;y)=\;&C_\ell(u,v,w)+h_{ps}\log\nu_{ps}\\
&+\sum_{(i,j):j\ne1}\hat\delta_{i,j}
\log{\Psi_{i,j}(\nu)\over\hat\delta_{i,j}}\\
&+\sum_i\hat\delta_{i,1}
\log{\Psi^R_{i,1}(\nu,z;q,\beta,e)\over\hat\delta_{i,1}}\\
&+h_{ns}\log{\nu_{ns1}+\nu_{ns2}\over h_{ns}}\\
&+\sum_{k=0}^{3}\hat\gamma_k
\log{\Psi_k^{Q,B}(\mu;\eta,\zeta)\over\hat\gamma_k}\\
&-u\log(\nu_{ps}\mu_{ps})
-v\log(\nu_{ns1}\mu_{ns1})
-w\log(\nu_{ns2}\mu_{ns2})\\
&-ev\log z-\eta qu
-\zeta\beta(\lambda_n-v-w).
\end{aligned}
\tag{5.11}
\]

Zero fixed masses are simply omitted from their `delta log(Psi/delta)` or `gamma log(Psi/gamma)` terms.

### Theorem 5.1 — conditional rescue dual

Let `F_R(x)` be the Díaz exponential objective `F(x)` multiplied by the proved iid-priority rescue factor from (3.3), with subexponential terms suppressed exactly as in the preceding finite-to-asymptotic transfer.  Then for every feasible source point `x` mapping to `theta` and **every** dual tuple `y`,

\[
\boxed{\log F_R(x)\le \mathcal D(\theta;y).}
\tag{5.12}
\]

Hence

\[
\boxed{
\sup_{x\in P}\log F_R(x)
\le
\sup_{\theta\in\Omega}
\inf_y\mathcal D(\theta;y).}
\tag{5.13}
\]

On every fixed-aggregate fiber with a relative-interior feasible point, finite-dimensional entropy duality has no gap, so the fiber maximum equals `inf_y D`.  Boundary fibers still obey the one-sided inequality (5.12), which is sufficient for an upper-threshold certificate.

## 6. Proof of Theorem 5.1

Everything is a blockwise application of the log-sum inequality

\[
\sum_r x_r\log{a_r\over x_r}
\le X\log{\sum_r a_r\over X},
\qquad X=\sum_r x_r.
\tag{6.1}
\]

### 6.1 Ordinary variable blocks

For a fixed light degree `(i,j)` with `j!=1`, the true state gets weight `nu_ps^i`, while false state `k` gets weight

\[
{j\choose k}\nu_{ns1}^k\nu_{ns2}^{j-k}.
\]

Source constraint (11) fixes their total mass to `hat_delta_{i,j}`.  Therefore

\[
\begin{aligned}
&-t_{i,j}\log t_{i,j}
-\sum_k f_{i,j,k}\log{f_{i,j,k}\over {j\choose k}}\\
&\le
\hat\delta_{i,j}\log{\Psi_{i,j}\over\hat\delta_{i,j}}
-i t_{i,j}\log\nu_{ps}\\
&\quad-\sum_k kf_{i,j,k}\log\nu_{ns1}
-\sum_k(j-k)f_{i,j,k}\log\nu_{ns2}.
\end{aligned}
\tag{6.2}
\]

### 6.2 Rescue-modified `j=1` blocks

For `(i,1)`, the logarithm of the rescue factor adds `t_{i,1} log s_i` to the objective.  Apply (6.1) to the two weights

\[
\nu_{ps}^i s_i,\qquad z\nu_{ns1}.
\]

Then

\[
\begin{aligned}
&-t_{i,1}\log t_{i,1}-f_{i,1,1}\log f_{i,1,1}
+t_{i,1}\log s_i\\
&\le
\hat\delta_{i,1}\log{\Psi^R_{i,1}\over\hat\delta_{i,1}}
-i t_{i,1}\log\nu_{ps}
-f_{i,1,1}\log\nu_{ns1}
-f_{i,1,1}\log z.
\end{aligned}
\tag{6.3}
\]

After summing over `i`, the final term is exactly

\[
-E\log z=-ev\log z.
\tag{6.4}
\]

### 6.3 Heavy negative split

Using source constraint (12) with weights `nu_ns1,nu_ns2`,

\[
\begin{aligned}
-h_{ns1}\log h_{ns1}-h_{ns2}\log h_{ns2}
\le\;&h_{ns}\log{\nu_{ns1}+\nu_{ns2}\over h_{ns}}\\
&-h_{ns1}\log\nu_{ns1}-h_{ns2}\log\nu_{ns2}.
\end{aligned}
\tag{6.5}
\]

### 6.4 Clause block with the two rescue aggregates

For syntactic clause class `k`, source constraint (14) fixes total mass `hat_gamma_k`.  Apply (6.1) with the tilted weights in (5.8).  Summing over `k`, using source copy constraint (18), and using

\[
Q=qu,\qquad B=\beta(\lambda_n-v-w),
\]

gives

\[
\begin{aligned}
-\sum_\alpha c_\alpha\log((w(\alpha)!/2)c_\alpha)
\le\;&
\sum_k\hat\gamma_k\log{\Psi_k^{Q,B}\over\hat\gamma_k}\\
&-u\log\mu_{ps}-v\log\mu_{ns1}-w\log\mu_{ns2}\\
&-\eta qu-\zeta\beta(\lambda_n-v-w).
\end{aligned}
\tag{6.6}
\]

### 6.5 Collect the copy constraints

Source constraint (17) implies

\[
\sum i t_{i,j}=u-h_{ps},
\quad
\sum kf_{i,j,k}=v-h_{ns1},
\quad
\sum(j-k)f_{i,j,k}=w-h_{ns2}.
\tag{6.7}
\]

Combining (6.2)--(6.5) therefore turns all variable-side multiplier terms into

\[
h_{ps}\log\nu_{ps}
-u\log\nu_{ps}-v\log\nu_{ns1}-w\log\nu_{ns2}.
\tag{6.8}
\]

Finally add the fixed copy numerator `C_ell` from the source definition of `F`, then (6.6).  This is exactly (5.11), proving (5.12).

The relative-interior equality statement follows because, after fixing the six aggregates, the copy term is constant and the remaining objective is a finite sum of strictly concave negative-entropy terms plus linear terms on a polytope cut out by linear equalities.  Its Lagrange/Fenchel dual is exactly (5.11).  Weak duality, which is the part needed for (5.13), requires no interior assumption.  QED.

## 7. Exact consistency test against Díaz equation (25)

The new formula has a strong algebraic check.

Turn the rescue off:

\[
q\beta e=0,\qquad z=1,\qquad \eta=\zeta=0.
\]

Now impose the source critical copy splits from (27):

\[
u={\lambda_p\nu_{ps}\mu_{ps}\over\Psi_p},
\qquad
\lambda_p-u={\lambda_p\over\Psi_p},
\]

and

\[
v={\lambda_n\nu_{ns1}\mu_{ns1}\over\Psi_n},\quad
w={\lambda_n\nu_{ns2}\mu_{ns2}\over\Psi_n},\quad
\lambda_n-v-w={\lambda_n\over\Psi_n}.
\]

Then the copy part of (5.11) collapses identically to

\[
\lambda_p\log{\lambda_p\over\Psi_p}
+\lambda_n\log{\lambda_n\over\Psi_n}.
\tag{7.1}
\]

Together with the ordinary variable, heavy and clause partition terms, (5.11) becomes the logarithm of the source critical-point value (25).

Thus the new conditional dual is not a different counting model: it recovers the exact Díaz expression at the Díaz stationary copy split, while remaining a valid upper bound away from that split because `(u,v,w)` are kept as outer variables instead of incorrectly minimizing their convex copy entropy.

## 8. Attack 3 — trying to remove `(q,beta,e)` globally

A tempting next compression is to use

\[
-\log(1-x)\ge x
\]

and then separate the monomial `beta e q^i` by Fenchel/Young inequalities.  The sign needed for an **upper count** is a lower bound on `beta e q^i`.  Standard Young/AM-GM inequalities instead give upper bounds, i.e. the wrong direction.

There is a universal lower bound on `[0,1]`, obtained from the union bound on complements:

\[
\beta e q^i
\ge
\bigl[\beta+e+iq-(i+1)\bigr]_+.
\tag{8.1}
\]

But it is useless in the actual Díaz saddle regime.  The already archived rounded-source inputs imply approximately

\[
q\approx0.747987,\qquad
\beta\approx0.127883,\qquad
e\approx0.002081.
\]

For every `i>=1`, the right side of (8.1) is zero.  More generally, any globally valid affine lower bound that is strictly positive in the interior must confront the three coordinate hyperplanes on which the product is exactly zero.

**Outcome:** do not destroy the rescue correction by forcing a global separable affine surrogate.  Keep `(q,beta,e)` as outer coordinates.  Six adversarial scalars are already small enough for a serious interval branch-and-bound certificate.

## 9. Auxiliary progress metric

The source writes its polytope in ambient dimension

\[
K=(M+1)^2(1+M/2)+23.
\]

At `M=23`,

\[
\boxed{K=7223.}
\]

Theorem 5.1 removes all of those high-dimensional entropy coordinates from the adversarial maximization.  The remaining maximization can be relaxed to the six compact scalars

\[
\boxed{(u,v,w,q,\beta,e)}.
\]

The nine variables in `y` are **minimizing certificate parameters**, not additional adversarial primal coordinates.  Thus a certified upper bound can be organized as a six-dimensional outer interval cover with a local dual witness in each box.

This is the run's real progress.  It also removes the preceding report's requirement to prove separately that a maximizing high-dimensional primal point stays away from every boundary face: weak duality (5.12) is valid on boundary fibers too, and the normalized rescue coordinates keep `s_i` bounded in `[1/2,1]`.

## 10. Exact unresolved full-scope gap

The source endpoint remains unchanged because I have **not** yet produced the six-dimensional interval certificate.  The next obligation is now sharply reduced to the following statement.

Choose some explicit `alpha<4.4898`, recompute the source deterministic core masses and prefactor `B(alpha)` with the same `M=23` truncation, and prove

\[
\boxed{
(1+10^{-7})B(\alpha)
\exp\left\{
\sup_{\theta\in\Omega(\alpha)}
\inf_y\mathcal D_\alpha(\theta;y)
\right\}<1.}
\tag{10.1}
\]

A complete certificate must provide, for every outer interval box, explicit finite dual parameters `y` whose interval evaluation bounds `D`; no assumption of a unique critical point is needed.  The exact source heavy/light error terms and continuity slack must be retained.  Only after (10.1) is proved may the resulting simple-formula UNSAT endpoint be transferred to the owner-frozen iid-with-replacement model using the `O(1/n)` repeated-whole-clause coupling.

This is substantially more concrete than the preceding obligation "interval-reoptimize the full Díaz polytope": the adversarial optimization is now six-dimensional, compact, ratio-singularity-free, and comes with an explicit pointwise dual witness formula.

## 11. Before/after accounting

External source metric:

\[
[3.52,4.4898]\to[3.52,4.4898],
\qquad W:0.9698\to0.9698.
\]

No source endpoint moved; status remains **PARTIAL / OPEN**.

Separate auxiliary progress:

- false route eliminated: Díaz (25) is **not** a free global dual; exact two-state obstruction identified;
- correct route proved: conditional six-scalar rescue dual (Theorem 5.1);
- high-dimensional adversarial primal: source ambient `7223` coordinates -> six outer scalar coordinates for certification;
- source stationary formula recovered exactly when rescue is disabled and the source copy split is inserted;
- boundary rescue ratios normalized so every rescue factor stays in `[1/2,1]`;
- no finite simulation, SAT instance, or physics value was counted as threshold progress.

The full classical random 3-SAT threshold, the convergence of its sharp-threshold centers, and any explicit endpoint below the externally verified `4.4898` therefore remain unresolved in this track.
