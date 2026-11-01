Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT on active R09 successor `CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM`: `p_cert = 1/2 -> 1/2`; supported unchanged count `3 -> 4`. Methods used: B17, B21, B29.**

# R09 run — compact-interior Hüsler–Reiss second-order theorem

## Continuity / ownership / source status

I did not reopen Tang Q4.11 or G0013. Tang's periodic-tree clause remains REFUTED/RETIRED in this track; the transitive-graph clause remains open. G0013 remains retired after its six-run handoff. The current exclusive R09 claim is `operations/claims/CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM.md`.

The active source is Yuyu Chen, Ruodu Wang, Yuming Wang and Wenhao Zhu, *Subuniformity of harmonic mean p-values*, Canadian Journal of Statistics, DOI 10.1002/cjs.70017, arXiv:2405.01368. A fresh 2026-09-18 search of the exact title/authors and the positive-Gaussian-copula wording again found the source, whose Section 7/Conclusion says the positive-correlation Gaussian case is not known and conjectures subuniformity, and no later primary paper resolving that precise conjecture.

Before research I reread the campaign INDEX/RANKING, POSTED, RESULTS, QUEUE, `operations/NEW_METHODS_2026-09-16.md`, the current claim, the latest R09 report, and re-opened the D--I intake ledgers. Repository-wide searches for the source title, `harmonic mean p-values`, `Gaussian copula`, and the WUVS/Pareto reformulation found no competing owner for this claim.

The fixed metric remains

\[
p_{\rm cert}:=\inf\bigl\{p_0:\ \Pr(M_r^{\mathbf w}(U)\le p)\ge p\ \text{for every }p\in[p_0,1),\ n,\mathbf w,R,\ r\le-1\bigr\},
\]

where `R` ranges over source-admissible Gaussian correlation matrices. Before this run, `p_cert=1/2`; after this run it is still `1/2`.

## Result of B17 — port the higher-order Hüsler–Reiss technique

The previous STUCK1 report identified the singular bivariate transition

\[
(1-\rho)\log(1/p)=\Theta(1)
\]

and obtained a formal positive second-order coefficient. This run upgrades that formal calculation to a rigorous theorem uniformly on compact interior parameter sets.

### Theorem (uniform compact-interior Hüsler–Reiss positivity)

Fix

\[
0<\delta_0<\delta_1<\infty,
\qquad 0<\varepsilon<\frac12.
\]

For `s>0` put

\[
p_s=\Phi(-s),\qquad
\rho_s(\delta)=1-\frac{\delta}{s^2},
\]

and let `(U_s,V_s)` have the bivariate Gaussian copula with latent correlation `rho_s(delta)`. For

\[
w\in[\varepsilon,1-\varepsilon],
\qquad
H_w(U,V)=\left(\frac wU+\frac{1-w}{V}\right)^{-1},
\]

we have, uniformly for

\[
(\delta,w)\in K:=[\delta_0,\delta_1]\times[\varepsilon,1-\varepsilon],
\]

\[
\boxed{
\frac{\Pr\{H_w(U_s,V_s)\le p_s\}}{p_s}
=1+\frac{C(\delta,w)}{s^2}+o_K(s^{-2})
}
\]

with

\[
\boxed{
C(\delta,w)=2\delta w(1-w)
\,\mathbb E\left[\frac{1}{w+(1-w)e^Q}\right],
\qquad Q\sim N(\delta,2\delta).
}
\]

In particular `C` is continuous and strictly positive on `K`, hence

\[
\inf_K C>0,
\]

and there exists `s_0=s_0(K)` such that for all `s>=s_0` and all `(delta,w) in K`,

\[
\Pr\{H_w(U_s,V_s)\le p_s\}>p_s.
\]

By power-mean monotonicity, the same strict inequality holds with `H_w=M_{-1}^{\mathbf w}` replaced by every two-coordinate weighted generalized mean `M_r^{\mathbf w}` with `r<=-1`.

This is PARTIAL, not source closure: it is bivariate and compact-interior in the transition parameter and weights.

## Proof

### 1. Exact one-dimensional representation

Normalize

\[
u=p_sa,\qquad v=p_sb.
\]

The inequality `H_w(u,v)<=p_s` is equivalent to

\[
\frac wa+\frac{1-w}{b}\ge1.
\]

For `a<=w` this is automatic. For `a>w`, the boundary is

\[
b=\frac{(1-w)a}{a-w}.
\]

Introduce

\[
a(q)=w+(1-w)e^q,
\qquad
b(q)=1-w+we^{-q}.
\]

Then

\[
b(q)=\frac{(1-w)a(q)}{a(q)-w},
\qquad
\log b(q)=\log a(q)-q,
\qquad da=(1-w)e^q\,dq.
\]

Let `q_-` and `q_+` be the unique solutions of

\[
b(q_-)=p_s^{-1},\qquad a(q_+)=p_s^{-1}.
\]

For

\[
z_s(t):=\Phi^{-1}(p_st),
\qquad
T_s(q):=\frac{z_s(b(q))-\rho_s z_s(a(q))}{\sqrt{1-\rho_s^2}},
\]

the Gaussian conditional law gives the exact identity

\[
\boxed{
R_s(\delta,w):=
\frac{\Pr(H_w\le p_s)}{p_s}
=w+(1-w)e^{q_-}
+\int_{q_-}^{q_+}(1-w)e^q\Phi(T_s(q))\,dq.
}
\]

No asymptotics have been used so far.

### 2. Quantile expansion

Write

\[
h_a(q)=\log a(q),\qquad h_b(q)=\log b(q)=h_a(q)-q,
\qquad k(h)=\frac{h^2}{2}-h.
\]

The standard normal Mills expansion

\[
\log\Phi(-x)=-\frac{x^2}{2}-\log x-\frac12\log(2\pi)-\frac1{x^2}+O(x^{-4})
\]

implies, uniformly whenever `|h|=O(log s)`, 

\[
\boxed{
\Phi^{-1}(e^h\Phi(-s))
=-s+\frac hs+\frac{k(h)}{s^3}
+O\left(\frac{(1+|h|)^3}{s^5}\right).
}
\]

Also

\[
\sqrt{1-\rho_s^2}
=\frac{\sqrt{2\delta}}{s}
\left(1-\frac{\delta}{4s^2}+O_K(s^{-4})\right).
\]

Therefore, on every window on which `h_a,h_b=O(log s)`, uniformly on `K`,

\[
T_s(q)=T_0(q)+\frac{T_2(q)}{s^2}
+O_K\left(\frac{(1+|q|)^3+(\log s)^3}{s^4}\right),
\]

where

\[
T_0(q)=-\frac{q+\delta}{\sqrt{2\delta}}
\]

and

\[
T_2(q)=\frac{S(q)}{\sqrt{2\delta}},
\]

\[
\boxed{
S(q)=h_a(q)(\delta-q)+\frac{q^2}{2}
+q\left(1-\frac\delta4\right)-\frac{\delta^2}{4}.
}
\]

The displayed expression follows from

\[
k(h_b)-k(h_a)+\delta h_a+rac\delta4(h_b-h_a-\delta)
\]

using `h_b=h_a-q`.

### 3. Uniform localization

Choose a large fixed `A`. Split the q-integral into

\[
q<-A\log s,
\qquad
-A\log s\le q\le A\sqrt{\log s},
\qquad
q>A\sqrt{\log s}.
\]

The negative tail is immediate:

\[
0\le(1-w)e^q\Phi(T_s(q))\le e^q,
\]

so it is `O(s^{-A})`, uniformly on `K`. The automatic strip satisfies

\[
(1-w)e^{q_-}=O_K(p_s),
\]

hence is smaller than every inverse power of `s`.

For the positive tail first suppose `x=z_s(a(q))<=0`, and put `y=z_s(b(q))`. Since `q>=0`, `b(q) in [1-w,1]`, hence uniformly on `K`, `y=-s+O_K(s^{-1})`. Since

\[
\log\Phi(x)-\log\Phi(y)=\log\frac{a(q)}{b(q)}=q,
\]

and the inverse Mills ratio `lambda(t)=phi(t)/Phi(t)` is `O(s)` uniformly for `y<=t<=0`, the mean-value theorem yields

\[
x-y\ge c_K\frac qs.
\]

Because `x<=0`,

\[
y-\rho_s x=(y-x)+(1-\rho_s)x\le y-x,
\]

and therefore

\[
T_s(q)\le-c_Kq.
\]

Thus

\[
(1-w)e^q\Phi(T_s(q))\le C_K e^q e^{-c_Kq^2}.
\]

For `A` large, the integral over `q>A sqrt(log s)` is `o_K(s^{-2})`.

If instead `x>0`, then still `y=-s+O_K(s^{-1})`, and

\[
T_s(q)\le\frac{y}{\sqrt{1-\rho_s^2}}\le-c_Ks^2.
\]

Although `e^{q_+}=O_K(p_s^{-1})`, the Gaussian tail `Phi(-c_Ks^2)` is `e^{-c'_Ks^4}` up to a polynomial factor, so this part is also `o_K(s^{-2})`.

The same elementary bounds apply to the limiting integrand involving `T_0`. Therefore all second-order mass is uniformly localized to the central window.

### 4. Taylor expansion on the central window

On the central window `h_a,h_b=O(log s)` uniformly on `K`, so the quantile expansion above applies. Taylor's theorem gives

\[
\Phi(T_s(q))
=
\Phi(T_0(q))+
\frac{\phi(T_0(q))T_2(q)}{s^2}
+O_K\left(\frac{(1+|q|)^4+(\log s)^4}{s^4}\right).
\]

After multiplication by `(1-w)e^q` and integration on the central window, the remainder is `o_K(s^{-2})`: on the negative side `e^q` supplies exponential damping, and on the positive side `e^q<=exp(A sqrt(log s))=s^{o(1)}`.

It follows that

\[
R_s
=
R_0+
\frac1{s^2}
\int_{\mathbb R}
(1-w)e^q\phi(T_0(q))T_2(q)\,dq
+o_K(s^{-2}).
\]

### 5. The leading term is exactly neutral

Let `D~N(delta,2delta)`. Since

\[
\Phi(T_0(q))=\Pr(D\le-q),
\]

Fubini gives

\[
\int_{\mathbb R}e^q\Phi(T_0(q))\,dq
=
\mathbb E\int_{-\infty}^{-D}e^q\,dq
=
\mathbb E e^{-D}=1.
\]

Hence

\[
R_0=w+(1-w)=1.
\]

This recovers rigorously the first-order neutrality found in STUCK1.

### 6. Exact simplification of the second-order coefficient

The function

\[
\frac{\phi(T_0(q))}{\sqrt{2\delta}}
\]

is the density of `N(-delta,2delta)` at q, and the exponential tilt identity

\[
e^q f_{N(-\delta,2\delta)}(q)=f_{N(\delta,2\delta)}(q)
\]

therefore yields

\[
I(\delta,w)
:=(1-w)\int e^q\phi(T_0(q))T_2(q)\,dq
=(1-w)\mathbb E S(Q),
\]

where `Q~N(delta,2delta)`.

Put

\[
h(q)=\log\bigl(w+(1-w)e^q\bigr).
\]

Gaussian Stein integration by parts gives

\[
\mathbb E[(Q-\delta)h(Q)]
=2\delta\mathbb E h'(Q).
\]

Also

\[
\mathbb E\left[
\frac{Q^2}{2}+Q\left(1-\frac\delta4\right)-\frac{\delta^2}{4}
\right]=2\delta.
\]

Thus

\[
\mathbb E S(Q)
=2\delta\bigl(1-\mathbb E h'(Q)\bigr).
\]

But

\[
h'(q)=\frac{(1-w)e^q}{w+(1-w)e^q},
\qquad
1-h'(q)=\frac{w}{w+(1-w)e^q}.
\]

Consequently

\[
I(\delta,w)
=
2\delta w(1-w)
\mathbb E\left[\frac1{w+(1-w)e^Q}\right]
=C(\delta,w)>0.
\]

This proves the theorem.

## Result of B29 — add the boundary faces and identify why the compact theorem does not yet glue globally

The coefficient has explicit asymptotics on all three singular faces.

For fixed interior `w`, as `delta downarrow 0`, `Q -> 0` in probability and bounded convergence gives

\[
\boxed{C(\delta,w)\sim2\delta w(1-w).}
\]

For fixed `delta>0`, as `w downarrow 0`, dominated convergence against the lognormal law gives

\[
\boxed{C(\delta,w)\sim2\delta w,}
\]

because `E e^{-Q}=1`; symmetrically

\[
\boxed{C(\delta,w)\sim2\delta(1-w)}
\qquad(w\uparrow1).
\]

Finally, for `delta -> infinity`, uniformly for `w` in a fixed compact subset of `(0,1)`,

\[
\mathbb E\frac1{w+(1-w)e^Q}
=
\frac{e^{-\delta/4}}{\sqrt{4\pi\delta}}
\int_{\mathbb R}
\frac{e^{q/2}e^{-q^2/(4\delta)}}{w+(1-w)e^q}\,dq.
\]

Dominated convergence and the beta integral

\[
\int_{\mathbb R}
\frac{e^{q/2}}{w+(1-w)e^q}\,dq
=
\frac{\pi}{\sqrt{w(1-w)}}
\]

give

\[
\boxed{
C(\delta,w)
\sim
\sqrt{\pi\delta w(1-w)}\,e^{-\delta/4}.
}
\]

Thus positivity survives pointwise on every face approach but the margin degenerates: linearly at `delta=0`, linearly at `w=0,1`, and exponentially as `delta -> infinity`. This is precisely why the compact-interior theorem does not by itself provide the uniform all-parameter gluing needed to lower `p_cert`.

## Result of B21 — a tempting Gaussian-convexity route and its exact obstruction

Let

\[
f(x)=\frac1{\Phi(x)}.
\]

With `lambda=phi/Phi`,

\[
f''(x)=f(x)\lambda(x)\bigl(x+2\lambda(x)\bigr)>0,
\]

because the Mills inequality gives `x+lambda(x)>0` for all x. Hence

\[
\{H_w>p\}
=
\left\{(x,y):wf(x)+(1-w)f(y)<\frac1p\right\}
\]

is convex in Gaussian score space.

This makes Colin Fogarty's 2026 *Gaussian comparison above the median* look almost tailor-made: for closed convex sets with reference probability at least one half, it gives a one-sided comparison when covariance matrices are ordered in Loewner order. At the comonotone covariance `J=11^T`, the acceptance probability here is `1-p>=1/2` for `p<=1/2`.

However the required covariance order fails exactly where it would be needed. If `R` is any nondegenerate two-coordinate correlation matrix and `v` is a nonzero vector orthogonal to `1`, then

\[
v^T(J-R)v=-v^TRv<0.
\]

Thus `R <= J` in Loewner order is false. The reverse order also fails in general. Consequently Fogarty's theorem cannot compare a general positive-correlation Gaussian copula directly to the comonotone endpoint. This is a precise obstruction, not merely a missing technical estimate.

I also checked the adjacent Gaussian supermodular-ordering literature. The indicator of the curved convex harmonic acceptance set is not presently shown to be supermodular, so that ordering does not immediately substitute for the missing Loewner comparison.

## Literature / ownership check for the new mechanism

Fresh searches on 2026-09-18 found:

1. Chen--Wang--Wang--Zhu, the active source, still states the positive-Gaussian subuniformity problem as open.
2. Hashorva--Peng--Weng, *Higher-order expansions of distributions of maxima in a Hüsler-Reiss model*, Methodology and Computing in Applied Probability 18 (2016), arXiv:1402.5608. It develops higher-order triangular-array Gaussian/Hüsler--Reiss expansions under refined conditions. This is the technique ported here; their theorem concerns rectangular maxima, not the nonlinear harmonic wedge, and does not imply the result above.
3. Fogarty, *Gaussian comparison above the median*, arXiv:2607.06874 (2026), gives the convex-set comparison under Loewner covariance ordering; the ordering obstruction above prevents direct use here.
4. The fixed-correlation heavy-tail literature (including Kortschak's second-order sum tails and Das--Fasen-Hartmann's Gaussian-copula heavy-tail analysis) is adjacent to the previous fixed-rho run, but I found no source treating this moving-correlation harmonic wedge or giving the coefficient `C(delta,w)` above.

I therefore record the compact-interior theorem as an R09 result with priority **unverified** beyond this bounded search. It is not claimed as a literature-first theorem until an independent priority audit is completed.

## What moved and what did not

The mathematical understanding moved: the formal second-order Hüsler--Reiss coefficient from STUCK1 is now a rigorous, uniform compact-interior theorem, and its three degenerating boundary faces are explicit.

The fixed fleet metric did **not** move:

\[
\boxed{p_{\rm cert}:\frac12\longrightarrow\frac12.}
\]

Reason: the theorem is bivariate and its uniformity excludes `delta -> 0`, `delta -> infinity`, and `w -> 0,1`; it therefore cannot yet certify every source-admissible Gaussian copula below `p=1/2`.

Supported unchanged count: `3 -> 4`.

Status: **PARTIAL / OPEN_CURRENT**.

## Next route

This run used B17, B21, B29. The next fresh triple is **B14, B20, B23**:

- **B14 (find the group acting):** exploit the `w <-> 1-w`, coordinate-swap and Gaussian sign/score symmetries to see whether the weight faces can be reduced to one controlled fundamental domain rather than estimated separately.
- **B20 (find why the algorithm fails):** formulate the desired global interpolation from fixed-rho low-p, compact Hüsler--Reiss, and comonotone first variation as an explicit covering algorithm in `(s,delta,w)`, then identify the exact uncovered parameter strip. The obstruction, rather than another local lemma, is the target.
- **B23 (do what the proposer did not expect):** actively search for an interior bivariate counterexample by studying whether the CDF can dip below `p` between the three now-positive asymptotic regimes; if no dip is possible, isolate the monotone quantity that forbids it.

If the metric remains unchanged for two more supported runs, the CLOSABLE six-run retirement rule fires and R09 must hand this target off rather than continuing to manufacture local results.

## Model / scheduler control status

The task-management surface exposed in this environment still has controls for title/prompt/schedule/timing/enabled state, but no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry. Therefore `GPT-6 / maximum` remains prompt text only here; the actual run metadata I can honestly state is `GPT-5.6 Sol / reasoning UNVERIFIED`.

The historical `P26: You cannot modify this task` condition remains an authorization-context issue. The legitimate remedies are the owning authorized context, an ownership/admin transfer, or platform support. Duplicating the task or bypassing permissions is not a valid workaround. No scheduler or permission change was attempted in this run.

## Bookkeeping

No checker-only artifact was created: this run's new claim is an analytic theorem with its proof written on this page and no finite computational core. No email, Drive, public posting, purchase, workflow execution, permission change, scheduler change, shared-root edit, or peer-track edit was performed.

```yaml
ledger_delta:
  track: R09
  active_claim: CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM
  source_status: OPEN_CURRENT
  result_status: PARTIAL
  metric_name: p_cert
  metric_before: 1/2
  metric_after: 1/2
  movement: no_movement
  supported_unchanged_before: 3
  supported_unchanged_after: 4
  methods_used: [B17, B21, B29]
  new_result:
    type: theorem
    name: compact-interior Huesler-Reiss second-order positivity
    scope: bivariate Gaussian copula; delta in compact subset of (0,infinity); weights bounded away from 0 and 1
    coefficient: "C(delta,w)=2 delta w(1-w) E[1/(w+(1-w) exp(Q))], Q~N(delta,2delta)"
    sign: strictly_positive
  prior_art_status: bounded_search_no_resolution_found_priority_unverified
  next_methods: [B14, B20, B23]
  tang_q411_periodic_tree: RETIRED_REFUTED
  g0013: RETIRED_HANDOFF_READY
```
