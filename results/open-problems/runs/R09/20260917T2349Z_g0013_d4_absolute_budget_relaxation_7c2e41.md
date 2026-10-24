Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — NO MOVEMENT on active R09 successor G0013: `U_* = 1289727882057511/11918000000000000 = 0.10821680500566462... -> same`; Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with supported retirement count `6`, and G0002 remains handed off at `Delta_8=UNMEASURED`. Methods used: B25 COUNT THE SAME THING TWICE, B11 DUALIZE, B15 BREAK THE SYMMETRY ON PURPOSE.** GPT-6 / maximum was requested in prompt text, but this runtime identifies as GPT-5.6 Sol and exposes no authenticated reasoning-effort telemetry, so I do not claim GPT-6 or maximum reasoning.

# R09 CLOSABLE OUTSIDE — G0013: the full D4 absolute-correlation budget, an exact one-dimensional relaxation obstruction, and why local slope magnitudes are still not enough

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only.

## 1. Continuity and current ownership

I did **not** reopen Pengfei Tang, Question 4.11. Its periodic-tree target remains retired from this R09 slot at the frozen metric `UNBOUNDED_ABOVE`, supported retirement count `6`. I also did not reopen G0002 / Cerf Conjecture 53.1, which remains handed off at `Delta_8=UNMEASURED`.

The controlling current exclusive claim is `operations/claims/G0013.md`. R09 owns the Catalano--Lavenant uniform-copula Wasserstein question. With
\[
\lambda=\operatorname{Unif}[0,1],\qquad \nu=\lambda\otimes\lambda,
\]
write
\[
M=\sup_{\pi\in\Pi(\lambda,\lambda)}W_2^2(\pi,\nu).
\]
The source conjecture is
\[
M=\frac1{10},
\]
with the diagonal and antidiagonal couplings as maximizers. The fixed R09 metric is

`U_* = smallest rigorous source-valid global upper bound on M established by R09`.

The preceding complete R09 report is

`runs/R09/20260917T2031Z_g0013_joint_compatibility_penalty_9f4c2a.md`,

which proved the current full-class bound
\[
\boxed{
U_*=
\frac{1289727882057511}{11918000000000000}
=0.10821680500566462\ldots .
}
\tag{1.1}
\]
This run does not lower (1.1), so the supported G0013 unchanged count is now `1`.

A commit search also recovered two R09 artifacts written after that report during an interrupted attempt,

- `artifacts/R09/20260917T2132Z_g0013_joint_slope_relaxation_exact.py` @ `315e315f9b777035491bfb889560e7e88cc4b0a2`,
- `artifacts/R09/20260917T2132Z_g0013_joint_slope_relaxation_exact.out` @ `ea34c19812354f286192ea64944e8413f4ac726a`.

No matching immutable R09 report was found in the bounded repository search. I therefore treat those files as orphaned self-check evidence, not as a supported prior run or as a hidden metric update. Their useful content is incorporated explicitly in Section 7 below.

Before doing new mathematics I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the exclusive G0013 claim, the newest complete R09 report, and current neighboring-track state. The newest R08 report located in the repository is `runs/R08/20260917T2326Z_i0048_threshold_comparison_73b9e1.md`; the bounded R10 commit search still finds its older successor-gate state rather than a newer neighboring report. For the large intake corpus I used exact target/source/ID searches and preserved the claim's prior-attempt history rather than pretending to have rendered every JSONL row through the connector. Root `RESULTS.md` remains stale on R09 relative to the exclusive G0013 claim; this attacking worker does not edit shared roots.

## 2. Fresh source-status check

Primary source: Marta Catalano and Hugo Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034v1 (7 October 2025), Remark 3. The source asks for the farthest coupling from independence for two uniform marginals and conjectures the monotone/antimonotone couplings.

Later primary source: Stefan Schrott, *Couplings Farthest from the Independent Gaussian*, arXiv:2609.10467v1 (9 September 2026). Its abstract still describes the uniform Catalano--Lavenant assertion as a conjecture and proves the Gaussian analogue instead.

Fresh bounded searches on 17--18 September 2026 used the exact titles/authors and combinations of `uniform copula`, `farthest from independence`, `Wasserstein`, `1/10`, and the Schrott title. I found no later source claiming a resolution of the exact uniform conjecture. This is bounded current-status evidence only; **publication novelty remains UNVERIFIED**.

## 3. Inherited Brenier/Jacobi reduction

For a positive smooth copula density let
\[
T=\nabla\phi=(u,v)
\]
be the Brenier map from the independent uniform square to \(\pi\). Define
\[
q_t(y)=\lambda\{x:u(x,y)\le t\},\qquad
r_s(x)=\lambda\{y:v(x,y)\le s\}.
\]
Uniform target marginals give
\[
\int_0^1q_t(y)\,dy=t,\qquad
\int_0^1r_s(x)\,dx=s.
\tag{3.1}
\]
Put
\[
I_1=\int_0^1\operatorname{Var}(q_t)\,dt,
\qquad
I_2=\int_0^1\operatorname{Var}(r_s)\,ds.
\]
Earlier R09 work proved the exact identity
\[
\boxed{W_2^2(\pi,\nu)=I_1+I_2=:S.}
\tag{3.2}
\]

For each level write
\[
q_t(y)-t=A_t\Bigl(y-\frac12\Bigr)+g_t(y),
\qquad g_t\perp\{1,y-\tfrac12\},
\]
with
\[
h_t=\|g_t\|_2^2,\qquad H_1=\int_0^1h_t\,dt,
\]
and analogously \(\widetilde A_s,\widetilde h_s,H_2\) for \(r_s\). The inherited Jacobi/PSD inequalities are
\[
2I_1+I_2+4H_1\le\frac16,
\qquad
I_1+2I_2+4H_2\le\frac16.
\tag{3.3}
\]
The exact scalar box obstacle is also inherited. If
\[
m=\min(t,1-t),\qquad a=|A_t|,
\]
then necessarily
\[
h_t\ge h_{\min}(m,a),
\tag{3.4}
\]
where
\[
h_{\min}(m,a)=
\begin{cases}
0,&0\le a\le2m,\\[1mm]
\dfrac{(a-2m)^3}{12(6m-a)},&2m<a\le6m-8m^2,\\[3mm]
m(1-m)-\dfrac L6-\dfrac{a^2}{12},&6m-8m^2<a\le6m(1-m),
\end{cases}
\tag{3.5}
\]
with
\[
L=\sqrt{12m(1-m)-2a}.
\tag{3.6}
\]
The preceding run also isolated the genuinely joint pointwise condition. If
\[
D^2\phi=\begin{pmatrix}a&b\\b&c\end{pmatrix}\succeq0,
\]
then at linked levels \(t=u(x,y)\), \(s=v(x,y)\),
\[
\partial_yq_t(y)=-\frac ba,
\qquad
\partial_xr_s(x)=-\frac bc,
\qquad
\boxed{
\partial_yq_{u(x,y)}(y)\,
\partial_xr_{v(x,y)}(x)=\frac{b^2}{ac}\le1.
}
\tag{3.7}
\]

## 4. B25 — count the same Brenier optimality inequality four ways: the full D4 absolute cross-correlation budget

The preceding report used diagonal and anti-diagonal source symmetries but did not use the quarter-turns. Adding them removes the sign-cancellation loophole in the **integrated** cross correlations.

Center source and target coordinates:
\[
Z=(X-\tfrac12,Y-\tfrac12),
\qquad
W=(U-\tfrac12,V-\tfrac12).
\]
All four coordinates are uniform on \([-1/2,1/2]\), hence have variance \(1/12\). Put
\[
r=\rho_S(X,U),\quad
s=\rho_S(Y,V),\quad
p=\rho_S(Y,U),\quad
q=\rho_S(X,V),
\]
and
\[
d=r+s.
\]
Because the quadratic-cost Brenier coupling maximizes \(E[Z\cdot W]\) among all couplings with the same source and target laws, and every square symmetry \(R\in D_4\) preserves the source law,
\[
E[Z\cdot W]\ge E[RZ\cdot W]
\qquad\forall R\in D_4.
\tag{4.1}
\]
Normalize (4.1) by the common variance \(1/12\).

For the diagonal swap \((x,y)\mapsto(y,x)\),
\[
d\ge p+q.
\tag{4.2}
\]
For the anti-diagonal reflection \((x,y)\mapsto(-y,-x)\) in centered coordinates,
\[
d\ge-(p+q).
\tag{4.3}
\]
For the two quarter-turns \((x,y)\mapsto(-y,x)\) and \((x,y)\mapsto(y,-x)\),
\[
d\ge q-p,
\qquad
d\ge p-q.
\tag{4.4}
\]
Therefore
\[
\boxed{
d\ge\max\{|p+q|,|p-q|\}=|p|+|q|.
}
\tag{4.5}
\]
Vertical and horizontal reflections separately give \(r,s\ge0\), although (4.5) is the new point needed here.

The Wasserstein cost and the direct Spearman sum are exactly related:
\[
S
=E[(X-U)^2+(Y-V)^2]
=\frac13-\frac d6,
\]
so
\[
\boxed{d=2-6S.}
\tag{4.6}
\]
Moreover, from the conditional-CDF definition,
\[
p=-\int_0^1A_t\,dt,
\qquad
q=-\int_0^1\widetilde A_s\,ds.
\tag{4.7}
\]
Indeed,
\[
E[U\mid Y=y]=\int_0^1(1-q_t(y))\,dt
\]
and the first Jacobi coefficient is
\[
A_t=12\int_0^1(y-\tfrac12)(q_t(y)-t)\,dy.
\]
Combining (4.5)--(4.7) gives the exact global budget
\[
\boxed{
\left|\int_0^1A_t\,dt\right|
+
\left|\int_0^1\widetilde A_s\,ds\right|
+6S\le2.
}
\tag{4.8}
\]
Since the inherited Chatterjee identities are
\[
\xi(Y,U)=6I_1,
\qquad
\xi(X,V)=6I_2,
\]
(4.8) can equivalently be written
\[
\boxed{
|\rho_S(Y,U)|+|\rho_S(X,V)|
+\xi(Y,U)+\xi(X,V)\le2.
}
\tag{4.9}
\]
This is strictly stronger than the preceding report's \(d\ge|p+q|\): opposite signs of the two cross correlations no longer cancel.

### Status of this theorem

Equations (4.5), (4.8), and (4.9) are full-class necessary conditions for smooth Brenier copulas and pass to general copulas through the same marginal-preserving smoothing/compactness argument used in the earlier R09 upper bounds. They are **not** by themselves the source conjecture and therefore do not move `U_*` this run.

## 5. A second exact nesting constraint: the first Jacobi coefficient has a sharp modulus of continuity

Before dualizing, there is one more one-coordinate fact that should not be thrown away.

Let \(0\le s<t\le1\) and \(\delta=t-s\). Since \(q_t\) is a conditional CDF,
\[
0\le q_t(y)-q_s(y)\le1,
\qquad
\int_0^1(q_t-q_s)\,dy=\delta.
\tag{5.1}
\]
Therefore
\[
A_t-A_s
=12\int_0^1(y-\tfrac12)(q_t(y)-q_s(y))\,dy.
\tag{5.2}
\]
Among functions \(f:[0,1]\to[0,1]\) of mass \(\delta\), the absolute first centered moment is maximized by an interval of length \(\delta\) at one endpoint. Hence
\[
\left|\int_0^1(y-\tfrac12)f(y)\,dy\right|
\le\frac{\delta(1-\delta)}2.
\]
Using (5.2),
\[
\boxed{
|A_t-A_s|\le6\delta(1-\delta)\le6\delta.
}
\tag{5.3}
\]
The same bound holds for \(\widetilde A\). Also \(A_0=A_1=0\) and \(\widetilde A_0=\widetilde A_1=0\).

Thus any argument that makes the sign of \(A_t\) oscillate rapidly in order to evade (4.8) must pay a real level-width cost. The next question is whether the already-used scalar/Jacobi information plus this modulus is enough. B11 answers that question negatively, exactly.

## 6. B11 — dualize to a one-dimensional necessary-condition program, then kill that relaxation with an exact rational witness

Consider the following reduced variational relaxation. For \(j=1,2\), choose coefficient functions \(A_j(t)\) and nonnegative higher-mode densities \(h_j(t)\), with
\[
m(t)=\min(t,1-t),
\]
satisfying

\[
h_j(t)\ge h_{\min}(m(t),|A_j(t)|),
\tag{6.1}
\]
\[
|A_j(t)-A_j(s)|\le6|t-s|(1-|t-s|),
\tag{6.2}
\]
and define
\[
H_j=\int h_j,
\qquad
I_j=\int\left(\frac{A_j^2}{12}+h_j\right).
\tag{6.3}
\]
Impose the two inherited Jacobi inequalities
\[
2I_1+I_2+4H_1\le\frac16,
\qquad
I_1+2I_2+4H_2\le\frac16,
\tag{6.4}
\]
and the new full-D4 budget
\[
\left|\int A_1\right|+\left|\int A_2\right|+6(I_1+I_2)\le2.
\tag{6.5}
\]
Every smooth Brenier copula produces data feasible for (6.1)--(6.5). Consequently, if this one-dimensional relaxation had supremum \(I_1+I_2\le1/10\), it would prove the source conjecture after the usual smoothing step.

It does **not**. There is a completely explicit rational feasible point above \(1/10\).

Take both families identical and put
\[
\boxed{
A_1(t)=A_2(t)=\frac83m(t),
\qquad
h_1(t)=h_2(t)=\frac{m(t)^2}{40}.
}
\tag{6.6}
\]
First verify the exact scalar obstacle (6.1).

For \(0\le m\le5/12\), \(a=(8/3)m\) lies in the one-sided clipped branch and
\[
h_{\min}\left(m,\frac83m\right)
=\frac{m^2}{135}
<\frac{m^2}{40}.
\tag{6.7}
\]
For \(5/12\le m\le1/2\), the two-sided branch has
\[
L^2=\frac43m(5-9m),
\]
and
\[
h_{\min}
=m-\frac{43}{27}m^2-\frac L6.
\]
The desired inequality \(h_{\min}\le m^2/40\) is equivalent, after moving terms, to
\[
L\ge m\left(6-\frac{1747}{180}m\right).
\tag{6.8}
\]
The right-hand side is positive on this interval, so square both sides. After division by \(m>0\), the difference is
\[
P(m)=\frac{20}{3}-12m-m\left(6-\frac{1747}{180}m\right)^2.
\tag{6.9}
\]
An exact derivative factorization gives
\[
P'(m)=-\frac{(1747m-720)^2}{10800}\le0,
\tag{6.10}
\]
while
\[
P(1/2)=\frac{2231}{259200}>0.
\tag{6.11}
\]
Hence (6.8), and therefore (6.1), holds on the full interval.

The modulus (6.2) also holds. The tent function \(m(t)\) satisfies
\[
|m(t)-m(s)|\le\min\{\delta,1-\delta\},
\qquad \delta=|t-s|.
\]
If \(\delta\le1/2\), then
\[
\frac83\delta\le3\delta\le6\delta(1-\delta),
\]
and if \(\delta\ge1/2\),
\[
\frac83(1-\delta)\le3(1-\delta)\le6\delta(1-\delta).
\]
Thus (6.2) is satisfied exactly.

Now use
\[
\int_0^1m(t)\,dt=\frac14,
\qquad
\int_0^1m(t)^2\,dt=\frac1{12}.
\tag{6.12}
\]
For each family,
\[
H=\frac1{480},
\qquad
I=\frac{(8/3)^2}{12}\frac1{12}+\frac1{480}
=\boxed{\frac{667}{12960}},
\tag{6.13}
\]
and
\[
\left|\int A\right|=\frac23.
\tag{6.14}
\]
The two Jacobi constraints coincide and have the strict margin
\[
3I+4H
=\frac{703}{4320}
<\frac16,
\qquad
\frac16-rac{703}{4320}=\boxed{\frac{17}{4320}}>0.
\tag{6.15}
\]
The full-D4 budget also has strict margin:
\[
2\cdot\frac23+6(2I)
=\frac{2107}{1080}
<2,
\qquad
2-\frac{2107}{1080}=\boxed{\frac{53}{1080}}>0.
\tag{6.16}
\]
Yet the relaxed objective is
\[
\boxed{
I_1+I_2
=\frac{667}{6480}
=0.102932098765432\ldots
>\frac1{10}
}
\tag{6.17}
\]
with exact excess
\[
\frac{667}{6480}-\frac1{10}
=\boxed{\frac{19}{6480}}.
\tag{6.18}
\]
Even the elementary pointwise variance cap is respected, since
\[
\frac{A^2}{12}+h
=\frac{667}{1080}m^2
\le m(1-m)
\qquad(0\le m\le1/2).
\]

### Consequence of B11

The scalar box obstacle, the Jacobi spectral inequalities, the new full-D4 absolute-correlation budget, and the sharp level-modulus (5.3), **even taken together**, are not sufficient to prove \(M\le1/10\). The obstruction is not numerical looseness in the old scalar envelope. A successful dual certificate must contain genuinely local two-coordinate information from the same Brenier map, not only one-dimensional level data and integrated D4 moments.

The exact finite arithmetic for (6.7)--(6.18) is archived in

`artifacts/R09/20260917T2349Z_g0013_d4_relaxation_exact.py`

with executed output

`artifacts/R09/20260917T2349Z_g0013_d4_relaxation_exact.out`,

which ends `SELF_CHECK_ONLY / PASS`. The checker certifies the rational algebra and the polynomial monotonicity identity; it is not an independent audit and the witness is explicitly a witness to the **relaxation**, not a copula counterexample.

## 7. B15 — break symmetry: coherent scalar saturation is impossible, but raw slope-product magnitudes can be anti-paired

The strengthened D4 inequality (4.9) finally makes sense of the orphaned 21:32 UTC self-check.

For the preceding report's preferred scalar-envelope family at
\[
k=\frac{6137}{775},\qquad m_0=\frac{19}{48},
\]
the exact checker lower-bounds, for one coherently oriented conditional family,
\[
|\rho|+\xi
\ge
\frac{10445}{10368}
=1+\frac{77}{10368}>1.
\tag{7.1}
\]
Therefore **two coherent copies cannot simultaneously occur as the two Brenier-linked cross families**, because (4.9) would require the sum of their \(|\rho|+\xi\) values to be at most \(2\).

This is a real joint incompatibility statement. It removes the previous report's integrated sign-cancellation loophole.

However, B15 also tests the opposite, deliberately asymmetric geometry. The same exact checker pairs preferred active-ramp slope magnitudes at complementary levels \(m\leftrightarrow1/2-m\). At the level of this formal magnitude pairing it finds
\[
\max \sigma(m)\sigma(1/2-m)
\le\frac{82944}{130321}
<1
\tag{7.2}
\]
on the middle lower-ramp pairing, while for a tail/lower pairing it obtains the stricter bound
\[
\sigma_{\rm tail}\sigma_{\rm lower}
\le\frac{180}{361}
<1.
\tag{7.3}
\]
Thus the pointwise Hessian condition (3.7) cannot be converted into a contradiction merely by comparing the **multiset of preferred slope magnitudes** from the two scalar families: an anti-pairing of levels can keep every tested product below one.

This anti-pairing is **not** asserted to come from an actual Brenier map. It is a counterexample to a proof strategy, not a counterexample to Catalano--Lavenant. It identifies the missing datum precisely: one must control which level pair \((t,s)=(u(x,y),v(x,y))\) occurs at the same source point, or equivalently control the source/level change of variables. Magnitudes alone do not encode that matching.

## 8. What moved and what did not

The tracked source-valid metric does not move:
\[
\boxed{
U_*^{\rm before}=U_*^{\rm after}
=rac{1289727882057511}{11918000000000000}
=0.10821680500566462\ldots .
}
\]
Status remains **PARTIAL / OPEN_CURRENT**. The supported unchanged count is `1`.

The run nevertheless changes the route materially:

1. the integrated D4 constraint is now the sharp absolute form \(d\ge|p|+|q|\), not merely \(d\ge|p+q|\);
2. nesting forces the exact modulus \(|A_t-A_s|\le6\delta(1-\delta)\);
3. an exact rational witness proves that the entire resulting one-dimensional necessary-condition relaxation still allows \(S=667/6480>1/10\);
4. coherent saturation of both scalar families is excluded by D4, but raw slope magnitudes admit anti-pairing below the Hessian product threshold.

Therefore another run optimizing scalar constants, another generic rank-correlation inequality, or another slope-magnitude checker would be the wrong use of the slot. The missing theorem has to couple **source position, both output levels, and the sign/orientation of the mixed Hessian**.

## 9. Exact remaining obligation

A source-level proof must add a quantitative constraint absent from (6.1)--(6.5). The cleanest current formulation is to exploit the actual level map
\[
(x,y)\longmapsto (u(x,y),v(x,y))
\]
together with
\[
q'_{u(x,y)}(y)\,r'_{v(x,y)}(x)=\frac{b(x,y)^2}{a(x,y)c(x,y)}\le1.
\]
What is missing is an inequality that survives integration and still remembers **which** \(q\)-level is paired with **which** \(r\)-level at the same source point.

One plausible target is a compensated two-field inequality of the form
\[
\mathcal D_q+\mathcal D_r
\ge c_0\int_{[0,1]^2}
\Phi\!\left(
|q'_{u(x,y)}(y)|,
|r'_{v(x,y)}(x)|
\right)\,dx\,dy,
\tag{9.1}
\]
where \(\mathcal D_q,\mathcal D_r\) are the scalar-envelope deficits and \(\Phi\) vanishes exactly when the slope pair is jointly admissible. A sharp enough positive lower bound at every putative \(S>1/10\) would close the conjecture.

The next three genuinely different methods are:

- **B13 FIND WHAT ONLY INCREASES:** search for an orientation/coherence functional of the mixed Hessian \(b=\phi_{xy}\) whose evolution across CDF levels controls sign changes and prevents arbitrary anti-pairing;
- **B18 SAY IT IN ANOTHER LANGUAGE:** rewrite the joint condition as a Monge--Ampere / angle-field or compensated-compactness statement for the PSD Hessian, rather than as two separate conditional-CDF inequalities;
- **B30 DO ONE SCALE / ONE DIRECTION AT A TIME:** localize to connected sign cells of \(b\), prove the sharp inequality on one sign cell, then quantify the deficit paid when cells of opposite orientation are glued.

Do **not** repeat B25/B11/B15 next run.

## 10. Model / scheduler-control status

The limitation remains exactly as recorded by the controlling repository policy and current root ledger. The exposed task-management schema permits prompt/title/schedule/timing/enabled-state changes but has **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. In this run the runtime identifies as GPT-5.6 Sol; reasoning effort is therefore reported as `UNVERIFIED`. GPT-6/maximum remains prompt text only.

The historical P26 `You cannot modify this task` response is authorization-context-dependent: the current root ledger records that a full P26 prompt update later succeeded in another authorized context. A denied task must be handled through the authorized owning context, ownership/admin transfer, or platform support. Duplicating a task or bypassing permissions is not a valid workaround. No scheduler modification was attempted in this run, consistent with the current R09 deployment instruction.

## 11. Structured ledger delta

```yaml
ledger_delta:
  track: R09
  active_claim: G0013
  source: "Catalano--Lavenant, Measures of Dependence based on Wasserstein distances, arXiv:2510.06034, Remark 3"
  status_before: "PARTIAL / OPEN_CURRENT"
  status_after: "PARTIAL / OPEN_CURRENT"
  metric_name: "U_* = smallest rigorous source-valid global upper bound on M"
  metric_before: "1289727882057511/11918000000000000 = 0.10821680500566462..."
  metric_after: "1289727882057511/11918000000000000 = 0.10821680500566462..."
  movement: "NO MOVEMENT"
  supported_unchanged_count: 1
  methods_used: [25, 11, 15]
  new_structural_results:
    - "full D4 Brenier optimality gives d >= |rho(Y,U)| + |rho(X,V)|"
    - "equivalently |int A| + |int Atilde| + 6S <= 2"
    - "nesting gives |A_t-A_s| <= 6 delta (1-delta)"
    - "exact rational relaxation witness A=(8/3)m, h=m^2/40 reaches S=667/6480>1/10 while satisfying scalar obstacle, Jacobi, D4, and coefficient modulus constraints"
    - "coherent scalar saturation violates strengthened D4, but complementary-level slope anti-pairing stays below product one in the recovered exact checker"
  checker:
    source: "artifacts/R09/20260917T2349Z_g0013_d4_relaxation_exact.py"
    source_commit: "aff2fafc270f7f2fbb86c823fadfff5559289061"
    output: "artifacts/R09/20260917T2349Z_g0013_d4_relaxation_exact.out"
    output_commit: "b6bc852a3ec49509faac3c64a86308311b1f552e"
    verdict: "SELF_CHECK_ONLY / PASS"
  recovered_orphan_evidence:
    source: "artifacts/R09/20260917T2132Z_g0013_joint_slope_relaxation_exact.py"
    source_commit: "315e315f9b777035491bfb889560e7e88cc4b0a2"
    output: "artifacts/R09/20260917T2132Z_g0013_joint_slope_relaxation_exact.out"
    output_commit: "ea34c19812354f286192ea64944e8413f4ac726a"
    note: "no matching immutable run report recovered; not counted as a supported prior run"
  predecessors:
    Tang_Q4_11: "RETIRED/FROZEN; metric UNBOUNDED_ABOVE; supported retirement count 6"
    G0002: "HANDED_OFF; Delta_8=UNMEASURED"
  next_methods: [13, 18, 30]
  closure: false
  audits: "not requested; source not closed"
```
