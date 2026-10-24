Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT on active R09 successor `CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM`: `p_cert = 1/2 -> 1/2`; this is the first supported unchanged run after the admission-run movement. Tang periodic-tree and G0013 remain retired/frozen. Methods actually used: B6 DEFORM TO A POINT YOU CAN SOLVE, B11 DUALIZE, B24 FIND THE EXTREMAL OBJECT.**

# R09 CLOSABLE OUTSIDE — Gaussian harmonic-mean subuniformity: a strict first-variation theorem away from comonotonicity

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only.

## 1. Continuity and source/current-status gate

I did **not** reopen Pengfei Tang Question 4.11 or G0013. Their controlling R09 states remain:

- Tang periodic-tree clause: **REFUTED / RETIRED**, metric frozen at `UNBOUNDED_ABOVE`, with the physical percolation branch and periodicity hypotheses already checked in the retired package. The transitive-graph clause remains open.
- G0013 / Catalano--Lavenant: **OPEN_CURRENT / PARTIAL / HANDOFF_READY / retired from active R09** after six unchanged runs, frozen at
  \[
  U_*=\frac{1289727882057511}{11918000000000000}=0.10821680500566462\ldots.
  \]
- The active exclusive R09 claim remains `operations/claims/CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM.md`.

I reread/recovered campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the active claim, and the newest complete own report

`runs/R09/20260918T0633Z_gaussian_subuniform_upperhalf_a71c4d.md`.

I also searched the current repository for the exact Chen--Wang--Wang--Zhu title/author cluster and current neighboring R08/R10 material. The exact source cluster still resolves only to the R09 claim/report in the bounded repository search; no second owner was found. The newest searchable R08 material is on unrelated D-series successors; no same-day R10 report was returned by the bounded path search. I used targeted intake/claim searches rather than pretending that the approximately 780-row intake corpus was rendered byte-for-byte through the connector.

### Current literature, dated 2026-09-18

Primary source: Yuyu Chen, Ruodu Wang, Yuming Wang and Wenhao Zhu, *Subuniformity of harmonic mean p-values*, Canadian Journal of Statistics, DOI `10.1002/cjs.70017`, arXiv:2405.01368. Section 7 says the positive-Gaussian statement is not known in the literature, and Section 8 explicitly conjectures subuniformity for Gaussian copulas with positive correlation coefficients.

Fresh searches on the exact title, the exact Gaussian-copula phrase, `harmonic mean p-values Gaussian copula subuniformity 2026`, and the later risk-aggregation terminology found no later primary paper resolving this exact Gaussian conjecture. This is bounded negative evidence, not a novelty certificate.

A relevant later author paper is Chen--Lin--Wang, *Universal Value-at-Risk superadditivity*, arXiv:2606.22884 (22 June 2026). It develops UVS/WUVS for heavy-tailed vectors and preservation properties. The bounded searches did not locate an explicit Gaussian-copula/Pareto theorem there that settles the present source conjecture. Section 4 below records the exact equivalence that makes this framework relevant.

## 2. Frozen metric

The active metric remains

`p_cert` = smallest lower endpoint such that the source subuniformity inequality is proved simultaneously for every `p in [p_cert,1)`, every dimension, every source-positive-correlation Gaussian copula, every source-valid positive weight vector, and every `r<=-1`.

Smaller is better. The previous run proved the universal upper-half theorem and moved

\[
p_{\rm cert}:1\longrightarrow\frac12.
\]

This run does **not** improve the full-source metric, so

\[
\boxed{p_{\rm cert}:\frac12\longrightarrow\frac12.}
\]

The theorem below is a substantial covariance-subclass result but remains PARTIAL and cannot be relabelled as global metric movement.

## 3. B6 — deform from the exactly solved comonotone point

The previous run showed that a pointwise correlation-derivative argument fails in the hard range `p<1/2`. The natural solvable endpoint is instead the **comonotone Gaussian covariance** `J=11^T`, where all Gaussian scores coincide and the harmonic mean is exactly uniform.

The main new result is that this endpoint is not merely exact: it is a **strict one-sided local extremum in every nontrivial covariance direction**, in every dimension and for every positive weight vector.

### Theorem R09-GAUSS-COMONO-FIRST-VARIATION

Fix `n>=2`, positive weights `w_i>0` with `sum_i w_i=1`, and any `n x n` correlation matrix `R`. Let

\[
R_t=(1-t)J+tR,\qquad 0\le t\le1,
\]

where `J` is the all-ones correlation matrix. Let

\[
X(t)\sim N(0,R_t),\qquad U_i(t)=\Phi(X_i(t)),
\]

and let

\[
H_t=\left(\sum_{i=1}^n\frac{w_i}{U_i(t)}\right)^{-1}
\]

be the weighted harmonic mean. Put

\[
q:=w^TRw\le1.
\]

For every fixed `p in (0,1)`, with

\[
z=\Phi^{-1}(p),\qquad \lambda(z)=\frac{\phi(z)}{\Phi(z)},
\]

we have, as `t downarrow 0`,

\[
\boxed{
\mathbb P\{H_t\le p\}
=
 p+t(1-q)\,\phi(z)\bigl(z+\lambda(z)\bigr)+o(t).
}
\tag{3.1}
\]

Equivalently,

\[
\boxed{
\mathbb P\{H_t>p\}
=
1-p-t(1-q)\,\phi(z)\bigl(z+\lambda(z)\bigr)+o(t).
}
\tag{3.2}
\]

The coefficient is strictly positive whenever `q<1`, because

\[
z+\lambda(z)>0\qquad(z\in\mathbb R).
\tag{3.3}
\]

Consequently, if `R` is non-comonotone on the support of the weights, then for every fixed `p in (0,1)` there exists `t_0=t_0(p,w,R)>0` such that

\[
\mathbb P\{H_t\le p\}>p
\qquad(0<t<t_0).
\tag{3.4}
\]

More uniformly, for every `p_0 in (0,1/2]` there is `t_0=t_0(p_0,w,R)>0` such that, for every `0<t<t_0`,

\[
\mathbb P\{M_r^{\mathbf w}(U(t))\le p\}\ge p
\quad\text{for every }p\in[p_0,1),\ r\le-1.
\tag{3.5}
\]

Thus along **every** covariance segment leaving the comonotone point, the source conjecture is true on every fixed significance window bounded away from zero, for all sufficiently small positive deformation parameters.

### Proof

Represent the Gaussian path exactly as

\[
X_i(t)=\sqrt{1-t}\,Z+\sqrt t\,Y_i,
\tag{3.6}
\]

where `Z~N(0,1)`, `Y~N(0,R)`, and `Z` is independent of `Y`.

Set

\[
g(x)=\frac1{\Phi(x)}.
\]

For fixed `y=(y_1,...,y_n)`, the event `H_t>p` is equivalent to

\[
Z>r_t(y),
\]

where `r_t(y)` is the unique solution of

\[
\sum_iw_i g\!\left(\sqrt{1-t}\,r_t(y)+\sqrt t\,y_i\right)=g(z).
\tag{3.7}
\]

Uniqueness follows because the left-hand side is continuous and strictly decreasing in `r` from `+infinity` to `1`, while `g(z)>1`.

Write

\[
\bar y=\sum_iw_i y_i,
\qquad
V_w(y)=\sum_iw_i(y_i-\bar y)^2.
\tag{3.8}
\]

We first expand the threshold. Put `s=sqrt(t)` and seek

\[
r_t(y)=z+s a+s^2b+o(s^2).
\]

Since

\[
\sqrt{1-s^2}\,r_t(y)
=z+s a+s^2\left(b-\frac z2\right)+o(s^2),
\]

Taylor expansion of (3.7) gives at order `s`

\[
g'(z)(a+\bar y)=0,
\]

hence

\[
a=-\bar y.
\tag{3.9}
\]

At order `s^2`,

\[
g'(z)\left(b-\frac z2\right)
+rac12g''(z)V_w(y)=0.
\]

Now

\[
g'(z)=-g(z)\lambda(z),
\qquad
\frac{g''(z)}{g'(z)}=-(z+2\lambda(z)),
\tag{3.10}
\]

so

\[
b=
\frac z2+rac{z+2\lambda(z)}2V_w(y).
\tag{3.11}
\]

Therefore

\[
r_t(y)=
 z-\sqrt t\,\bar y
+t\left[
\frac z2+rac{z+2\lambda(z)}2V_w(y)
\right]+o(t).
\tag{3.12}
\]

Conditioning on `Y` gives

\[
\mathbb P\{H_t>p\}
=\mathbb E\,\overline\Phi(r_t(Y)).
\tag{3.13}
\]

The needed Gaussian moments are exact:

\[
\mathbb E\bar Y^2=w^TRw=q,
\qquad
\mathbb EV_w(Y)=1-q,
\tag{3.14}
\]

because every diagonal entry of `R` is one.

Expanding `barPhi` at `z` and using `barPhi''(z)=z\phi(z)`, the `sqrt(t)` term has zero expectation and the order-`t` term is

\[
-\phi(z)
\left[
\frac z2+rac{z+2\lambda(z)}2(1-q)
\right]
+rac{z\phi(z)}2q
=-(1-q)\phi(z)(z+\lambda(z)).
\tag{3.15}
\]

This proves (3.2), hence (3.1), once the expansion is justified under expectation.

For completeness, that interchange can be made elementary. On

\[
A_t=\{\max_i|Y_i|\le t^{-1/8}\},
\]

we have `sqrt(t) max_i|Y_i|=O(t^{3/8})`; the implicit-function/Taylor remainder in (3.12) is `o(t)` uniformly on `A_t` (indeed the cubic scale is `O(t^{9/8})`) for `z` in any compact interval. Since each `Y_i` is standard Gaussian,

\[
\mathbb P(A_t^c)\le2n\exp(-t^{-1/4}/2)=o(t^m)
\]

for every fixed `m`. The complement therefore contributes `o(t)` to the bounded probability in (3.13). This proves the fixed-`p` expansion and also its uniformity for `p` in any compact subinterval of `(0,1)`.

Finally, (3.3) is immediate for `z>=0`. For `z<0`, the standard one-line Mills inequality

\[
\Phi(z)<\frac{\phi(z)}{-z}
\]

implies `lambda(z)>-z`, hence `z+lambda(z)>0`.

Also `q<=1` because every correlation coefficient is at most one:

\[
q=\sum_{i,j}w_iw_jR_{ij}\le\sum_{i,j}w_iw_j=1.
\]

With all `w_i>0`, equality means every active `R_ij=1`, i.e. the direction is comonotone on the weighted support. Thus the first variation is strictly favorable in every nontrivial direction.

Uniformity on `[p_0,1/2]` follows from the compact-uniform expansion and the positive continuous coefficient in (3.1). For `p>=1/2`, the previous R09 universal upper-half theorem already holds for **every** Gaussian covariance. Finally, power-mean monotonicity gives `M_r<=M_{-1}=H` for `r<=-1`, so (3.5) follows. `QED`

### What this theorem says geometrically

The source's numerical plots suggested that dependence approaching comonotonicity might drive the harmonic-mean CDF down toward the identity. Formula (3.1) makes the endpoint geometry exact: the comonotone Gaussian copula is a strict **local minimizer of the harmonic-mean CDF**, equivalently a strict local maximizer of the superlevel probability, along every nontrivial covariance segment.

The penalty separates into

\[
(1-q)\times \phi(z)(z+\lambda(z)).
\]

The first factor

\[
1-q=
\mathbb E\sum_iw_i(Y_i-\bar Y)^2
\]

is exactly the weighted Gaussian residual variance away from the common factor. The second factor is positive at every threshold. This is the quantitative mechanism missing from the previous pointwise-correlation derivative attempt.

## 4. B11 — dualize: exact WUVS / Pareto formulation

The source problem has an exact heavy-tail dual that is useful for later attacks.

Let

\[
L_i=U_i^{-1}.
\]

Each `L_i` is standard Pareto on `[1,infinity)`, with

\[
\mathbb P(L_i>x)=\frac1x\qquad(x\ge1).
\]

For the harmonic mean,

\[
H=\frac1{\sum_iw_iL_i}.
\]

Thus, for `p in (0,1)`,

\[
\mathbb P(H\le p)\ge p
\iff
\mathbb P\left(\sum_iw_iL_i\ge\frac1p\right)\ge\frac1{1/p}
\iff
L\preceq_{\rm st}\sum_iw_iL_i,
\tag{4.1}
\]

where `L` denotes a single standard Pareto variable. Under the comonotone coupling, `sum_i w_i L_i=L` identically. Therefore full harmonic-mean subuniformity for all weights is precisely the statement that the actual Pareto portfolio stochastically dominates its comonotone benchmark for every weight vector.

In the terminology of Chen--Lin--Wang (arXiv:2606.22884), this is exactly the weighted universal Value-at-Risk superadditivity (WUVS) viewpoint for the Pareto vector generated by the Gaussian copula.

The Gaussian copula is preserved after reflecting the latent scores: if `V_i=Phi(-X_i)`, then

\[
L_i=\frac1{1-V_i},
\]

so the target can be read as:

> standard Pareto margins, coupled by a positive-correlation Gaussian copula, satisfy WUVS.

The June 2026 UVS/WUVS paper supplies useful preservation machinery, but the bounded current search did not locate an explicit theorem there that already proves this Gaussian-copula/Pareto case. Hence this is a **bridge/reformulation**, not a closure claim.

Why B11 does not immediately finish the source: classical marginal optimal-transport duality is too weak, because arbitrary copulas with the same Pareto margins need not satisfy (4.1). Any successful dual certificate must encode the Gaussian-copula covariance structure rather than only the one-dimensional margins.

## 5. B24 — find the extremal object: local answer, global question remains

B24 now has a rigorous local answer:

\[
\boxed{R=J\text{ is the strict local worst covariance for subuniformity along every nontrivial segment.}}
\]

More concretely, for every fixed target correlation matrix `R`, weights `w`, and threshold `p`, the segment

\[
R_t=(1-t)J+tR
\]

satisfies

\[
\left.\frac d{dt}\right|_{0+}
\mathbb P_{R_t}(H\le p)
=(1-w^TRw)\phi(z_p)(z_p+\lambda(z_p))>0
\]

unless the weighted support is already comonotone.

This is consistent with the source's simulations and with the previous run's failure of pointwise monotonicity: the full correlation path can bend, but it initially moves in the conjectured direction from the comonotone endpoint.

The global extremal statement

\[
\mathbb P_R(H\le p)\ge p
\quad\text{for every positive-correlation }R
\]

is still open. Formula (3.1) says what a counterexample would have to do: it cannot bifurcate infinitesimally from comonotonicity at a fixed threshold; it must arise after a genuinely nonlocal covariance deformation, or in a low-`p` boundary layer whose scale collapses as `R->J`.

## 6. Why the global metric did not move

The active `p_cert` quantifies **all** positive-correlation Gaussian copulas. Theorem (3.1) controls a neighborhood of the comonotone endpoint along every fixed covariance ray, but not arbitrary covariance matrices at finite distance from `J`. Hence it is PARTIAL, and the honest global ledger remains

\[
\boxed{p_{\rm cert}=1/2.}
\]

This is the first supported unchanged run since the metric moved on admission. No checker was manufactured: the new claim is an analytic theorem with no finite core, and the proof is on the page.

## 7. Next new-method attacks

The next triple is deliberately different from B6/B11/B24:

- **B7 TAKE THE LIMIT:** resolve the singular `p downarrow 0` regime for Gaussian-copula Pareto sums using hidden regular variation / Gaussian joint-tail asymptotics. The key goal is the **sign** of the first correction to `P(sum w_i/U_i >= 1/p)=p+o(p)`, not merely tail equivalence.
- **B25 COUNT THE SAME THING TWICE:** in the bivariate case, decompose `{H<=p}` into the two one-big-jump marginal pieces plus the interior harmonic wedge; compare the overlap subtraction and interior addition on the same Gaussian lower-tail scale.
- **B30 ONE SCALE AT A TIME:** separate the ordinary fixed-correlation low-`p` scale from the singular joint limit `1-c` comparable to `1/log(1/p)`. The previous numerical false negatives occurred exactly because these scales were mixed.

If that low-tail sign can be made uniform enough to overlap the compact-threshold local theorem above, it may produce the first all-threshold positive-correlation Gaussian subclass rather than another threshold-only lemma.

## 8. Model / scheduler control boundary

The actual exposed task-management schema still has prompt/title/schedule/timing/enabled-state controls but no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed-duration field. GPT-6/maximum therefore remains prompt-only here. The actual surfaced model for this run is GPT-5.6 Sol; reasoning level is UNVERIFIED.

The historical P26 `You cannot modify this task` event is an authorization/context boundary; repository history records that edits can succeed from a different authorized context. The lawful remedies remain the owning authorized context, ownership/admin transfer, or platform support—not duplication or permission bypass. No scheduler modification was attempted in this run.

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: R09
  lane: CLOSABLE_OUTSIDE
  active_claim: CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM
  predecessor_state:
    tang_q411_periodic:
      status: REFUTED_RETIRED
      metric: UNBOUNDED_ABOVE
    g0013:
      status: OPEN_CURRENT_PARTIAL_HANDOFF_READY_RETIRED_FROM_R09
      U_star: "1289727882057511/11918000000000000"
  metric:
    name: p_cert
    direction: smaller_is_better
    before: 0.5
    after: 0.5
    movement: false
    supported_unchanged_count_after_last_movement: 1
  theorem:
    id: R09-GAUSS-COMONO-FIRST-VARIATION
    statement: "Along R_t=(1-t)J+tR, P(H_t<=p)=p+t(1-w^TRw)phi(z_p)(z_p+phi(z_p)/Phi(z_p))+o(t); strict in every nontrivial direction. Uniform on each p-window [p0,1/2], and combined with the prior upper-half theorem for p>=1/2."
    source_scope: PARTIAL
  dual_reformulation:
    statement: "Gaussian-copula harmonic subuniformity is WUVS for standard Pareto margins generated by that Gaussian copula."
    later_framework: "Chen--Lin--Wang, arXiv:2606.22884"
  methods: [B6, B11, B24]
  checker: none_analytic_theorem_no_finite_core
  next_moves: [B7, B25, B30]
  shared_root_edits: none
  peer_file_edits: none
  scheduler_changes: none
  email_drive_public_posting: none
```
