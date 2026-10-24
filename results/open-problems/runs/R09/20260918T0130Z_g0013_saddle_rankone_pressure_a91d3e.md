Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — NO MOVEMENT on active R09 successor G0013: `U_* = 1289727882057511/11918000000000000 = 0.10821680500566462... -> same`; supported G0013 unchanged count `1 -> 2`; Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with supported retirement count `6`, and G0002 remains handed off at `Delta_8=UNMEASURED`. Methods used: B13 FIND WHAT ONLY INCREASES, B18 SAY IT IN ANOTHER LANGUAGE, B30 DO ONE SCALE / ONE DIRECTION AT A TIME.** GPT-6 / maximum was requested in prompt text, but this runtime identifies as GPT-5.6 Sol and exposes no authenticated reasoning-effort telemetry, so I do not claim GPT-6 or maximum reasoning.

# R09 CLOSABLE OUTSIDE — G0013: partial-Legendre saddle coordinates, a rank-one pressure theorem, and the first local geometry that rules out the formal anti-pairing escape

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only.

## 1. Continuity, ownership, and what is not being reopened

I did **not** reopen Pengfei Tang, Question 4.11. The later immutable R09 record supersedes the original admission-stage wording: the periodic-tree clause is REFUTED with a source-matching proof, exact checker, two distinct outside audit passes, and a paper package; the transitive-graph clause remains open; the R09 Tang metric is frozen at `UNBOUNDED_ABOVE`; and the six-unchanged retirement limit has already been reached. The controlling Tang retirement report is

`runs/R09/20260917T003156Z_tang_final_scout_retirement_package.md`.

I also did not reopen G0002 / Cerf 53.1, which remains handed off at `Delta_8=UNMEASURED`.

The controlling current exclusive claim is

`operations/claims/G0013.md`.

R09 owns the Catalano--Lavenant uniform-copula Wasserstein question. Put
\[
\lambda=\operatorname{Unif}[0,1],\qquad \nu=\lambda\otimes\lambda,
\]
and
\[
M=\sup_{\pi\in\Pi(\lambda,\lambda)} W_2^2(\pi,\nu).
\]
The source conjecture is
\[
M=\frac1{10},
\]
with the diagonal and antidiagonal couplings as maximizers. The frozen R09 metric is

`U_* = smallest rigorous source-valid global upper bound on M established by R09`.

The newest complete own report recovered before this run is

`runs/R09/20260917T2349Z_g0013_d4_absolute_budget_relaxation_7c2e41.md`

at creation commit

`55df1b0f59c57675c9845041c0af5d2147e38d16`.

It leaves the source-valid bound
\[
\boxed{
U_*=
\frac{1289727882057511}{11918000000000000}
=0.10821680500566462\ldots .
}
\tag{1.1}
\]
This run does not lower (1.1), so the supported G0013 unchanged count becomes `2`.

Before new mathematics I reread/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the exclusive G0013 claim, the newest complete R09 report, the Tang retirement record, the newest R08 neighboring report, the newest available R10 neighboring state, and exact G0013/intake/attempt searches. The root `RESULTS.md` R-series table is still stale relative to the later exclusive G0013 claim and later R09 reports; this attacking worker does not edit shared roots. The large intake corpus was queried by exact target/source/ownership terms rather than pretending that every JSONL row was visibly rendered through the connector.

## 2. Fresh source/current-literature check — 18 September 2026

Primary source:

Marta Catalano and Hugo Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034, submitted 7 October 2025. The source's Remark 3 asks for the farthest coupling from independence for two uniform marginals and conjectures the monotone and antimonotone couplings.

Later primary source:

Stefan Schrott, *Couplings Farthest from the Independent Gaussian*, arXiv:2609.10467, submitted 9 September 2026. Its abstract still states that Catalano--Lavenant conjectured the uniform result and proves the Gaussian analogue instead.

Fresh bounded searches on 18 September used the exact source title, exact Schrott title, author names, `uniform copula`, `farthest from independence`, `Wasserstein`, and the conjectured constant. No later source claiming a resolution of the exact uniform problem surfaced. Catalano's current research page and Lavenant's current research page still list the dependence paper as a submitted preprint. This is bounded dated evidence only; **publication novelty remains UNVERIFIED**.

For the new coordinate change below I also searched `partial Legendre transform`, `Monge--Ampere`, `optimal transport`, and `hypercube`. Partial Legendre transforms are standard technology in two-dimensional Monge--Ampere/optimal-transport regularity, including work on optimal mappings between hypercubes. I therefore make **no novelty claim for the partial-Legendre mechanism itself**. The point here is to use that classical coordinate system to expose a source-specific quantitative obstruction that the preceding scalar relaxation discarded.

## 3. Inherited exact Brenier/Jacobi setup

Work first with a strictly positive smooth copula density and its smooth Brenier map
\[
T=\nabla\phi=(u,v):[0,1]^2\to[0,1]^2.
\]
Write
\[
D^2\phi=
\begin{pmatrix}
a&b\\
b&c
\end{pmatrix}\succeq0.
\tag{3.1}
\]
For positive smooth densities on the same square, the standard second-boundary-value regularity gives the face correspondence needed below. In particular, in the smooth approximation class one may use
\[
u(0,y)=0,\quad u(1,y)=1,\qquad
v(x,0)=0,\quad v(x,1)=1.
\tag{3.2}
\]

Define the conditional CDFs
\[
Q(t,y):=q_t(y)=\lambda\{x:u(x,y)\le t\},
\qquad
R(s,x):=r_s(x)=\lambda\{y:v(x,y)\le s\}.
\tag{3.3}
\]
The uniform output marginals imply
\[
\int_0^1Q(t,y)\,dy=t,
\qquad
\int_0^1R(s,x)\,dx=s.
\tag{3.4}
\]
Set
\[
I_1=\int_0^1\operatorname{Var}_y Q(t,\cdot)\,dt,
\qquad
I_2=\int_0^1\operatorname{Var}_x R(s,\cdot)\,ds.
\tag{3.5}
\]
The earlier R09 reduction gives the exact identity
\[
\boxed{S:=W_2^2(\pi,\nu)=I_1+I_2.}
\tag{3.6}
\]

Let
\[
w(z)=z(1-z).
\]
Define the two weighted Hessian energies
\[
J_1=\iint w(x)a(x,y)\,dx\,dy,
\qquad
J_2=\iint w(y)c(x,y)\,dx\,dy.
\tag{3.7}
\]
An integration by parts gives
\[
J_1=2\operatorname{Cov}(X,U),
\qquad
J_2=2\operatorname{Cov}(Y,V),
\tag{3.8}
\]
and hence, because all four one-dimensional marginals are uniform,
\[
\boxed{J_1+J_2=\frac13-S.}
\tag{3.9}
\]

The preceding runs used the sharp Jacobi/Wright--Fisher Poincare inequality
\[
\operatorname{Var}(f)\le\frac12\int_0^1w(z)f'(z)^2\,dz.
\tag{3.10}
\]
The present run keeps the exact local coefficient multiplying those weighted derivative energies instead of replacing it by `<=1` immediately.

## 4. B18 — say it in another language: the Brenier map is a convex-concave saddle map in mixed coordinates

The scalar relaxation treats the families `Q(t,.)` and `R(s,.)` almost independently. The missing datum is which two levels arise at the **same source point**. A partial Legendre transform makes that matching explicit.

Fix `(t,y)` in the interior. By (3.2) and strict convexity, `x -> u(x,y)` increases from 0 to 1, so
\[
x=Q(t,y)
\quad\Longleftrightarrow\quad
u(Q(t,y),y)=t.
\tag{4.1}
\]
Define
\[
V(t,y):=v(Q(t,y),y).
\tag{4.2}
\]
Implicit differentiation of (4.1) gives
\[
Q_t=\frac1a,
\qquad
Q_y=-\frac ba.
\tag{4.3}
\]
Differentiating (4.2),
\[
V_t=\frac ba=-Q_y,
\qquad
V_y=c-\frac{b^2}{a}=\frac{ac-b^2}{a}\ge0.
\tag{4.4}
\]

These identities have a generating function. Let
\[
\Psi(t,y)=tQ(t,y)-\phi(Q(t,y),y),
\tag{4.5}
\]
the partial Legendre transform of `phi` in the first variable. Then
\[
\boxed{Q=\Psi_t,\qquad V=-\Psi_y,}
\tag{4.6}
\]
and
\[
\Psi_{tt}=\frac1a\ge0,
\qquad
\Psi_{yy}=-\left(c-\frac{b^2}{a}\right)\le0,
\qquad
\Psi_{ty}=-\frac ba.
\tag{4.7}
\]
Thus `Psi` is convex in `t` and concave in `y`: the original convex-gradient map becomes a **saddle generating function**.

The mixed map
\[
\mathcal C(t,y)=(Q(t,y),V(t,y))
\tag{4.8}
\]
has Jacobian
\[
\det D\mathcal C
=Q_tV_y-Q_yV_t
=Q_tV_y+Q_y^2
=\frac ca>0.
\tag{4.9}
\]
Its inverse uses the other conditional CDF. If `s=V(t,y)` and `x=Q(t,y)`, then `y=R(s,x)`, and differentiating at fixed `s` gives
\[
R_x=-\frac bc.
\tag{4.10}
\]
Consequently the old pointwise joint condition becomes
\[
\boxed{
Q_y(t,y)\,R_x(s,x)=\frac{b^2}{ac}=:\kappa(x,y)\in[0,1],
}
\tag{4.11}
\]
with `(t,s)=(u(x,y),v(x,y))` and `x=Q(t,y)`.

This is more than a change of notation. The two scalar CDF families are the two projections of **one** convex-concave saddle map, and the local product in (4.11) is the square of the Hessian angle: `kappa=1` is rank one, while small `kappa` means substantial two-dimensional determinant.

### 4.1 An unweighted conservation law

The face correspondence in (3.2) implies
\[
Q(0,y)=0,\quad Q(1,y)=1,
\qquad
V(t,0)=0,\quad V(t,1)=1.
\tag{4.12}
\]
Hence `C` maps the square to the square with the corresponding sides. Integrating its Jacobian, or directly changing variables back to `(x,y)`, gives
\[
\boxed{
\iint Q_y(t,y)^2\,dt\,dy
+
\iint Q_t(t,y)V_y(t,y)\,dt\,dy
=1.
}
\tag{4.13}
\]
Indeed, using `dt=a dx`, the left side is
\[
\iint\left(\frac{b^2}{a}+c-\frac{b^2}{a}\right)dx\,dy
=\iint c\,dx\,dy
=1.
\]
So the formal anti-pairing escape from the preceding run has an exact geometric price: making the linked slope product small does not disappear; it moves mass into the positive determinant-overlap term `Q_t V_y`.

### 4.2 The old determinant deficit becomes literal saddle overlap

Define
\[
E_1:=\iint w(y)Q_y(t,y)^2\,dt\,dy.
\tag{4.14}
\]
Changing variables `t=u(x,y)` gives
\[
E_1=\iint w(y)\frac{b^2}{a}\,dx\,dy.
\tag{4.15}
\]
Therefore
\[
\boxed{
J_2-E_1
=
\iint w(y)Q_t(t,y)V_y(t,y)\,dt\,dy\ge0.
}
\tag{4.16}
\]
There is a symmetric identity
\[
J_1-E_2\ge0
\tag{4.17}
\]
for the inverse mixed coordinates.

Earlier R09 work already had an equivalent normalized `Jacobi deficit + determinant deficit` identity, so I do **not** relabel the algebraic deficit budget as a new theorem. What is new in this route is the geometric identification: the determinant deficit is the weighted overlap of the convex and concave curvatures of one saddle potential.

If
\[
P_1=E_1-2I_1\ge0,
\qquad
P_2=E_2-2I_2\ge0,
\tag{4.18}
\]
are the exact Jacobi spectral deficits, and
\[
D_1=J_2-E_1,
\qquad D_2=J_1-E_2,
\tag{4.19}
\]
then (3.9) gives the exact normalization
\[
\boxed{
P_1+P_2+D_1+D_2=\frac13-3S.
}
\tag{4.20}
\]
Thus the source bound `S<=1/10` is equivalent, in this normalization, to
\[
\boxed{P_1+P_2+D_1+D_2\ge\frac1{30}.}
\tag{4.21}
\]
The diagonal/antidiagonal limit has equality. The remaining task is therefore not “find another scalar CDF inequality”; it is to prove the sharp tradeoff between spectral non-affinity and saddle determinant overlap.

## 5. B13 — a monotone extremality pressure: any counterexample must become quantitatively rank one

The previous run showed that level magnitudes can be formally anti-paired. The saddle coordinates reveal why that does not produce a high-cost counterexample.

Define the local Hessian rank-one ratio
\[
\kappa(x,y)=\frac{b(x,y)^2}{a(x,y)c(x,y)}\in[0,1].
\tag{5.1}
\]
From (4.15),
\[
E_1=\iint w(y)c\,\kappa\,dx\,dy,
\qquad
E_2=\iint w(x)a\,\kappa\,dx\,dy.
\tag{5.2}
\]
Whenever the denominators are nonzero, put
\[
\bar\kappa_y=\frac{E_1}{J_2},
\qquad
\bar\kappa_x=\frac{E_2}{J_1},
\qquad
K=\max\{\bar\kappa_x,\bar\kappa_y\}.
\tag{5.3}
\]
If one `J_i` vanishes, define the corresponding average as zero; the same conclusion follows by deleting that zero term.

By the sharp Jacobi Poincare inequality (3.10),
\[
2I_1\le E_1=\bar\kappa_yJ_2,
\qquad
2I_2\le E_2=\bar\kappa_xJ_1.
\tag{5.4}
\]
Adding and using (3.9),
\[
2S\le K(J_1+J_2)=K\left(\frac13-S\right).
\]
Therefore
\[
\boxed{
S\le \frac{K}{3(2+K)}.
}
\tag{5.5}
\]
Equivalently, every smooth candidate with cost `S>0` must satisfy
\[
\boxed{
K\ge \frac{2S}{1/3-S}.
}
\tag{5.6}
\]
The right side is strictly increasing in `S`. This is the useful B13 monotone quantity: **higher Wasserstein extremality forces the Brenier Hessian to become more rank one in at least one of the two natural weighted measures.**

At the conjectured threshold,
\[
\frac{2(1/10)}{1/3-1/10}=\frac67.
\]
Hence:

> **Rank-one pressure theorem.** If a smooth Brenier copula satisfies
> \[
> \max\{\bar\kappa_x,\bar\kappa_y\}\le\frac67,
> \]
> then
> \[
> W_2^2(\pi,\nu)\le\frac1{10}.
> \]
> In particular the stronger pointwise condition `ess sup kappa <= 6/7` proves the Catalano--Lavenant bound for that subclass.

This is a genuine verified subclass theorem and is labeled **PARTIAL**, not a proof of the source conjecture.

Conversely, every smooth counterexample with `S>1/10` must satisfy
\[
\boxed{K>\frac67.}
\tag{5.7}
\]
Because any nonsmooth source counterexample could be approximated by the same marginal-preserving smooth regularization used in the earlier R09 full-class bounds, a source counterexample would force smooth approximants with (5.7) as well.

### 5.1 Quantitative high-rank-one mass

Normalize the weighted measure corresponding to whichever average in (5.3) attains `K`. If `S>=sigma>1/10`, then its mean `kappa` is at least
\[
A(\sigma)=\frac{2\sigma}{1/3-\sigma}.
\tag{5.8}
\]
Since `0<=kappa<=1`, the elementary two-point extremal estimate gives
\[
\boxed{
\mu\{\kappa\ge6/7\}
\ge 7A(\sigma)-6.
}
\tag{5.9}
\]
whenever the right side is positive.

At the present global upper endpoint (1.1), the exact arithmetic is
\[
A(U_*)
=
\frac{7738367292345066}{8048816353827467}
=0.9614292278721488\ldots,
\tag{5.10}
\]
so a hypothetical smooth map **attaining that endpoint** would have at least
\[
\frac{5875672923450660}{8048816353827467}
=0.7300045951050419\ldots
\tag{5.11}
\]
of one natural weighted Hessian measure in the region `kappa>=6/7`.

The exact rational claims in this subsection are checked by

`artifacts/R09/20260918T0130Z_g0013_rankone_pressure_exact.py`

at commit

`c21a3b112274acf7b4f3f386ed83646123a58ae8`,

with executed archived output

`artifacts/R09/20260918T0130Z_g0013_rankone_pressure_exact.out`

at commit

`3c85291750e4ebf650d0e6fdc8eeea255f1de4e4`,

ending `SELF_CHECK_ONLY / PASS`. This is a self-check, not an independent audit.

## 6. B30 — localize the previous anti-pairing escape: it cannot support a counterexample unless the level matching becomes almost rank one

The preceding run found a formal complementary-level pairing of preferred scalar slopes with
\[
\kappa_{\rm formal}\le\frac{82944}{130321}=0.636459\ldots
\tag{6.1}
\]
in the middle regime and the still smaller tail bound
\[
\kappa_{\rm formal}\le\frac{180}{361}=0.498615\ldots .
\tag{6.2}
\]
That showed only that comparing raw slope magnitudes could not itself produce a contradiction.

The new theorem shows something stronger: **if an actual Brenier map realized such a low-product anti-pairing globally, it would be nowhere near a source counterexample.** From (5.5), (6.1) would imply
\[
S\le
\frac{82944/130321}{3(2+82944/130321)}
=
\boxed{\frac{13824}{171793}}
=0.08046893645\ldots,
\tag{6.3}
\]
and the tail value (6.2) would give
\[
S\le\boxed{\frac{30}{451}}=0.06651884701\ldots .
\tag{6.4}
\]
Both are far below `1/10`.

So the anti-pairing idea is now localized correctly. A counterexample cannot merely pair large slope levels with small slope levels. It must arrange the **actual source-point matching** so that, in at least one weighted orientation, a substantial fraction of mass has
\[
\frac{b^2}{ac}\approx1.
\]
In other words, it must spend most of the relevant mass in nearly rank-one sign cells and then glue those cells together while preserving both uniform target marginals. The gluing region, where the orientation changes or determinant opens, is exactly where the positive saddle-overlap term in (4.16) is paid.

This kills the preceding anti-pairing route as a plausible counterexample mechanism without claiming that anti-pairing is algebraically impossible.

## 7. Two further local identities that any sign-cell/gluing argument must obey

The mixed-coordinate reformulation yields two exact constraints that were not present in the one-dimensional relaxation.

### 7.1 Boundary regression flux

Let
\[
m_U(y)=E[U\mid Y=y]=\int_0^1u(x,y)\,dx.
\]
Differentiating under the integral and using `b=v_x`,
\[
\boxed{
m_U'(y)=\int_0^1b(x,y)\,dx=v(1,y)-v(0,y).
}
\tag{7.1}
\]
Hence
\[
|m_U'(y)|\le1.
\tag{7.2}
\]
Moreover `v(1,.)` and `v(0,.)` are nondecreasing because `c=v_y>=0`. Each is `[0,1]`-valued, so distributionally
\[
\boxed{\operatorname{TV}(m_U')\le2.}
\tag{7.3}
\]
Symmetrically,
\[
\boxed{
m_V'(x)=u(x,1)-u(x,0),\quad |m_V'|\le1,\quad \operatorname{TV}(m_V')\le2.
}
\tag{7.4}
\]
Thus opposite-sign rank-one cells cannot be glued with arbitrary boundary flux. Any proposed oscillatory construction has a finite boundary-orientation budget.

### 7.2 The two cross-conditional paths have the same total W1 variation

For fixed `y`, change variables `t=u(x,y)` in (4.3):
\[
\int_0^1|Q_y(t,y)|\,dt
=\int_0^1|b(x,y)|\,dx.
\tag{7.5}
\]
For the inverse family, changing `s=v(x,y)` gives
\[
\int_0^1|R_x(s,x)|\,ds
=\int_0^1|b(x,y)|\,dy.
\tag{7.6}
\]
Therefore
\[
\boxed{
\iint|Q_y|\,dt\,dy
=
\iint|R_x|\,ds\,dx
=
\iint|b|\,dx\,dy.
}
\tag{7.7}
\]
In one dimension `int |partial CDF|` is the natural `W_1` path-length density, so (7.7) says the two cross-conditional-law paths have exactly the same total metric variation.

Finally PSD gives `|b|<=sqrt(ac)<=(a+c)/2`; by the face conditions `int a=int c=1`. Hence
\[
\boxed{
\iint|Q_y|=\iint|R_x|=\iint|b|\le1.
}
\tag{7.8}
\]
This common path-length conservation is another obstruction to treating the two scalar CDF families independently.

## 8. What this run establishes, and what it does not

The global tracked source metric does **not** move:
\[
\boxed{
U_*^{\rm before}=U_*^{\rm after}
=
\frac{1289727882057511}{11918000000000000}
=0.10821680500566462\ldots .
}
\tag{8.1}
\]
Status remains **PARTIAL / OPEN_CURRENT**. The supported G0013 unchanged count is `2`.

What did move mathematically is the description of the obstruction:

1. the two conditional-CDF families are not merely linked by the pointwise product `<=1`; they are generated by one convex-concave partial-Legendre potential;
2. the determinant slack is literally the overlap `Q_t V_y` of the saddle curvatures;
3. extremal cost imposes the monotone rank-one pressure (5.6);
4. any source counterexample must have weighted average `kappa>6/7`, so the formal low-product anti-pairing found last run cannot be the geometry of a counterexample;
5. the boundary regression and common-W1 identities quantify additional gluing constraints that the scalar relaxation omitted.

This is why I did **not** spend the run tuning another scalar penalty constant. The old scalar route has an explicit exact witness above `1/10`; the remaining theorem must exploit the two-dimensional saddle compatibility.

## 9. Method accounting

### B13 — FIND WHAT ONLY INCREASES

Success. The forced weighted rank-one ratio
\[
\frac{2S}{1/3-S}
\]
is monotone increasing in the target cost `S`. At `S=1/10` it crosses the exact threshold `6/7`. This gives a clean rigidity gate for every future counterexample or near-extremizer analysis.

### B18 — SAY IT IN ANOTHER LANGUAGE

Success. The partial Legendre transform rewrites the Brenier map as a convex-concave saddle potential with
\[
Q=\Psi_t,\qquad V=-\Psi_y,
\]
and turns the previously abstract PSD slack into the explicit overlap `Q_tV_y`. The transform is classical Monge--Ampere technology; the report claims no priority for that mechanism.

### B30 — DO ONE SCALE / ONE DIRECTION AT A TIME

Success as a structural localization, not as source closure. The previous complementary-level anti-pairing is quantitatively harmless if realized as a true low-`kappa` matching. Any counterexample must instead spend enough weighted mass in nearly rank-one sign cells, and the only plausible remaining loss is the cost of gluing those cells while maintaining the two marginal constraints.

## 10. Exact remaining obligation and next genuinely different methods

The source would close if one can prove the sharp saddle tradeoff
\[
\boxed{
P_1+P_2+D_1+D_2\ge\frac1{30}
}
\tag{10.1}
\]
for every admissible mixed Brenier saddle map, with equality classification giving the diagonal/antidiagonal limits. The old scalar obstacles control `P_1+P_2`; the new coordinate system identifies `D_1+D_2` as saddle determinant overlap. What is still missing is a quantitative theorem preventing both from being simultaneously too small under the **same source-point level matching**.

This is not yet a formal Section-I stuck run because the supported unchanged count is `2`, not `3`. If the metric is unchanged next run, the full five-part stuck protocol must trigger.

The next triple is deliberately different:

- **B9 RANDOMIZE:** sample/construct random near-rank-one sign-cell saddle fields satisfying the exact side data, to see whether the `1/30` tradeoff fails before imposing the final uniform-`V` marginal; this is a counterexample search against the proposed saddle inequality, not simulation as proof.
- **B19 MAKE IT AN ALGORITHM:** turn saddle feasibility into a constructive recovery problem: given `Q`, recover the least nonnegative `V_y` compatible with `V_t=-Q_y`, the face data, and the second uniform marginal. If the recovery always pays an explicit determinant-overlap cost, the algorithm is the missing proof.
- **B28 REPLACE FOR ALL WITH FOR TYPICAL:** use (5.9) to isolate the typical near-rank-one region of any hypothetical `S>1/10` map and prove a stability/classification theorem there; quantify the exceptional gluing set rather than treating all source points equally.

## 11. Structured ledger_delta

```json
{
  "worker": "R09",
  "deployment": "NEW-METHODS-2026-09-16",
  "active_claim": "G0013",
  "source": "Catalano-Lavenant arXiv:2510.06034 Remark 3 / Schrott arXiv:2609.10467 Conjecture 1.1",
  "status_before": "PARTIAL / OPEN_CURRENT",
  "status_after": "PARTIAL / OPEN_CURRENT",
  "metric": "U_* = smallest rigorous source-valid global upper bound on M=sup W_2^2(pi,lambda^2)",
  "metric_before": "1289727882057511/11918000000000000",
  "metric_after": "1289727882057511/11918000000000000",
  "movement": "NO_MOVEMENT",
  "supported_unchanged_count_before": 1,
  "supported_unchanged_count_after": 2,
  "new_partial_results": [
    "partial-Legendre saddle representation Q=Psi_t, V=-Psi_y",
    "unweighted conservation int Q_y^2 + int Q_t V_y = 1",
    "rank-one pressure S <= K/[3(2+K)]",
    "smooth subclass esssup(b^2/ac)<=6/7 satisfies S<=1/10",
    "any smooth counterexample S>1/10 has weighted mean kappa>6/7",
    "boundary regression flux and TV constraints",
    "equal total W1 variation of the two cross-conditional paths"
  ],
  "methods": [13, 18, 30],
  "next_methods": [9, 19, 28],
  "predecessors": {
    "Tang-2020-Q4.11-periodic": {
      "metric": "UNBOUNDED_ABOVE",
      "status": "RETIRED_FROZEN",
      "supported_retirement_count": 6
    },
    "G0002": {
      "metric": "Delta_8=UNMEASURED",
      "status": "HANDED_OFF"
    }
  },
  "source_current_status_check": "bounded 2026-09-18 search found Schrott 2026 Gaussian analogue still calling uniform result a conjecture; no later exact resolution surfaced; novelty UNVERIFIED",
  "self_check": {
    "source": "artifacts/R09/20260918T0130Z_g0013_rankone_pressure_exact.py",
    "source_commit": "c21a3b112274acf7b4f3f386ed83646123a58ae8",
    "output": "artifacts/R09/20260918T0130Z_g0013_rankone_pressure_exact.out",
    "output_commit": "3c85291750e4ebf650d0e6fdc8eeea255f1de4e4",
    "verdict": "SELF_CHECK_ONLY / PASS"
  },
  "shared_roots_edited": false,
  "scheduler_changed": false,
  "email_or_drive_used": false,
  "public_posting": false
}
```

## 12. Model/scheduler-control note

The exposed automation/task-control surface still provides prompt/title/schedule/timing/enabled-state controls but no model-family selector, reasoning-effort selector, or authenticated completed-run model telemetry. Therefore GPT-6/maximum remains request text only in this environment. The repository also records that a historical P26 update was denied in one authorization context but later succeeded in another authorized context; that makes the failure context-dependent, not a mathematical or repository issue. The legitimate remedies remain the authorized owning context, ownership/admin transfer, or platform support. No scheduler modification, permission change, duplicate task, email, Drive operation, workflow execution, or public posting was attempted in this run.
