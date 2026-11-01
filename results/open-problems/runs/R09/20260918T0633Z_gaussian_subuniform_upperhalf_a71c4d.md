Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT on newly admitted R09 successor `CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM`: `p_cert = 1 -> 1/2` (smaller is better); Tang periodic-tree and G0013 remain retired/frozen. Methods actually used: B2 ATTACK THE NEGATION FIRST, B5 ADD A PARAMETER AND DIFFERENTIATE, B18 SAY IT IN ANOTHER LANGUAGE.**

# R09 CLOSABLE OUTSIDE — Gaussian-copula harmonic-mean subuniformity: source admission and a universal upper-half theorem

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only.

## 1. Continuity: do not reopen Tang or G0013

I continued from the newest R09 report

`runs/R09/20260918T0533Z_successor_gate_sendov_resolution_83c1d6.md`

rather than restarting the stale native title.

Preserved predecessor states:

- Pengfei Tang, Question 4.11 periodic-tree clause: **REFUTED / RETIRED**, exact physical branch checked, metric frozen at `UNBOUNDED_ABOVE`, retirement count 6, two distinct outside audits and paper package already present. The transitive-graph clause remains OPEN.
- G0013 / Catalano--Lavenant: **OPEN_CURRENT / PARTIAL / HANDOFF_READY / retired from active R09** after six unchanged runs, with frozen rigorous upper bound
  \[
  U_*=\frac{1289727882057511}{11918000000000000}
  =0.10821680500566462\ldots.
  \]
- G0002 remains handed off at `Delta_8=UNMEASURED`.

I reread/recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R09 report, current coordinator/admission state, and targeted current ownership/intake evidence. The approximately 780-row intake corpus is too large to render byte-for-byte through one connector response; exact-ID/source/claim searches were used rather than pretending otherwise.

The newest coordinator report available during this run (`operations/task_health/runs/2026-09-18T055500Z/status.md`) still records several CLOSABLE admission gaps and no newly promoted free READY reserve candidate in its bounded pass.

## 2. D0012 was fully checked enough to reject it as this lane's successor

The preceding R09 report left `D0012` / Ruodu Wang Open Problem 12 as a possible next screen. I completed the decisive part of that screen.

The source asks for a characterization of aggregation-set membership: given a candidate sum law `G`, determine whether some `S in D_n` has law `G`, even for simple margins. Current author-page evidence says this broad Open Problem 12 has only a **small partial answer**: Mao--Wang--Wang (2019) characterize the homogeneous standard-uniform aggregation set for `n>2`, while the broad parent remains open. The current author page still describes the 2019 result as a partial answer.

A fresh direct fetch of `operations/claims/D0012.md` returned 404, so ownership is not the blocker. The blocker is source shape: the parent is a broad characterization problem, and a finite-support or single-margin theorem would be PARTIAL rather than source closure. Therefore

`D0012 = HOLD_SCOPE / PENDING / NOT R09-CLOSABLE-READY`.

I did not create a D0012 claim.

## 3. New source admitted: Chen--Wang--Wang--Zhu Gaussian-copula conjecture

### Primary source

Yuyu Chen, Ruodu Wang, Yuming Wang, Wenhao Zhu, **Subuniformity of harmonic mean p-values**, Canadian Journal of Statistics, DOI `10.1002/cjs.70017` (first published online 26 July 2025; journal issue 2026), arXiv:2405.01368.

For a copula `(U_1,...,U_n)`, weights `w_i>0`, `sum_i w_i=1`, and generalized mean `M_r^w`, the paper calls the mean subuniform when

\[
\mathbb P\!\left(M_r^{\mathbf w}(U_1,\ldots,U_n)\le p\right)\ge p
\qquad(0<p<1).
\tag{3.1}
\]

Its main regime is `r<=-1`.

Section 7 studies the equicorrelated Gaussian construction

\[
U_i=\Phi(X_i),\qquad
X_i=\rho Z+\sqrt{1-\rho^2}\,Z_i,
\]

numerically. It explicitly says that the corresponding positive-Gaussian subuniformity statement for general positive correlation is not known in the literature. Section 8 then states the conjecture that subuniformity holds for **Gaussian copulas with positive correlation coefficients**.

Fresh 2026-09-18 web searches on the exact title, arXiv identifier, exact phrase `Gaussian copulas with positive correlation coefficients`, and combinations of `harmonic mean p-values / Gaussian copula / subuniformity / 2026` recovered the source but no later primary paper resolving this exact Gaussian conjecture. This is bounded negative evidence, not a worldwide novelty certificate.

Repository searches for the exact title and the author/topic cluster returned no prior R09/peer claim, report, paper package, or posted result for this target. Immediately before creation there was no visible canonical claim. I therefore created the create-only claim

`operations/claims/CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM.md`

at commit

`6e603ae9ddb0f1d277c7a8768873ba42faed77b5`.

This is a genuinely CLOSABLE source shape: a single certified positive-correlation Gaussian counterexample at one threshold refutes the conjecture, while a proof has an objective all-parameter closure predicate.

## 4. Frozen metric

Define

`p_cert`

as the smallest threshold lower endpoint currently certified by R09 such that (3.1) is proved simultaneously for

- every `p in [p_cert,1)`;
- every dimension `n`;
- every Gaussian copula in the source's positive-correlation class;
- every source-valid weight vector;
- every `r<=-1`.

Smaller is better. Before this run the safe R09 baseline is the vacuous interval, `p_cert=1`.

The theorem below gives

\[
\boxed{p_{\rm cert}=1/2},
\]

so the metric moves `1 -> 1/2`.

## 5. B18 — Gaussian-score language gives a universal upper-half theorem

### Theorem R09-GAUSS-UPPER-HALF

Let `X=(X_1,...,X_n)` be any centered Gaussian vector with

\[
\operatorname{Var}(X_i)=1
\]

for every `i`; **no sign condition on the correlations is needed**. Put

\[
U_i=\Phi(X_i),
\]

where `Phi` is the standard normal CDF. Let `w_i>=0`, `sum_i w_i=1`. Then for every generalized-mean order `r<=0` and every

\[
p\in[1/2,1),
\]

we have

\[
\boxed{
\mathbb P\!\left(M_r^{\mathbf w}(U_1,\ldots,U_n)\le p\right)\ge p.
}
\tag{5.1}
\]

In particular, (5.1) proves the Chen--Wang--Wang--Zhu Gaussian-positive-correlation conjecture on the whole upper half of its threshold interval, uniformly in dimension, weights and all source orders `r<=-1`.

### Proof

By monotonicity of the power means in their order,

\[
M_r^{\mathbf w}(U)\le M_0^{\mathbf w}(U)
=\prod_{i=1}^n U_i^{w_i}
\qquad(r\le0).
\tag{5.2}
\]

The key elementary fact is that `x -> log Phi(x)` is concave on the whole real line. For completeness, write `phi` for the standard normal density and

\[
\lambda(x)=\frac{\phi(x)}{\Phi(x)}.
\]

Then

\[
(\log\Phi)'=\lambda,
\qquad
(\log\Phi)''
=-\lambda(x)\bigl(x+\lambda(x)\bigr).
\tag{5.3}
\]

Clearly `x+lambda(x)>0` when `x>=0`. If `x<0`, the one-line Mills inequality gives

\[
\Phi(x)
=\int_{-\infty}^{x}\phi(t)\,dt
<\frac1{-x}\int_{-\infty}^{x}(-t)\phi(t)\,dt
=\frac{\phi(x)}{-x},
\]

so `lambda(x)>-x`. Hence the right-hand side of (5.3) is strictly negative everywhere, proving concavity.

Applying Jensen to `log Phi` yields

\[
\sum_i w_i\log\Phi(X_i)
\le
\log\Phi\!\left(\sum_iw_iX_i\right).
\]

Exponentiating and combining with (5.2),

\[
M_r^{\mathbf w}(U)
\le
\prod_i\Phi(X_i)^{w_i}
\le
\Phi(Y),
\qquad
Y:=\sum_iw_iX_i.
\tag{5.4}
\]

Now `Y` is centered Gaussian with variance

\[
\sigma^2=\mathbf w^TR\mathbf w
=\sum_{i,j}w_iw_jR_{ij}
\le \sum_{i,j}w_iw_j=1,
\tag{5.5}
\]

because every correlation coefficient satisfies `R_ij<=1`. If `sigma=0`, then `Y=0` a.s. and the desired estimate is immediate for `p>=1/2`.

Otherwise let `z_p=Phi^{-1}(p)`. For `p>=1/2`, `z_p>=0`; therefore (5.4) gives

\[
\begin{aligned}
\mathbb P\{M_r^{\mathbf w}(U)\le p\}
&\ge \mathbb P\{\Phi(Y)\le p\}\\
&=\Phi\!\left(\frac{z_p}{\sigma}\right)\\
&\ge \Phi(z_p)=p,
\end{aligned}
\]

since `0<sigma<=1`. This proves (5.1). `QED`

### Scope / novelty discipline

This theorem is **PARTIAL** for the source because it says nothing yet about `0<p<1/2`. The `log Phi` concavity/Mills mechanism is elementary and should be treated as folklore-level unless a deeper prior-art search shows otherwise. I am claiming a rigorous source-relevant implication, not publication novelty.

The proof is actually stronger than needed in three directions: arbitrary Gaussian correlation signs, orders all the way up to `r=0`, and weights allowed on the boundary of the simplex.

## 6. B2 — attack the negation first: counterexample search and a numerical trap

Before trying to prove the low-`p` half, I attacked the conjecture numerically in the exact Gaussian family.

For the bivariate equal-weight harmonic mean

\[
H(U,V)=\frac{2UV}{U+V},
\]

with latent Gaussian correlation `c`, the superlevel event has the exact one-dimensional conditional representation

\[
\mathbb P_c(H>p)
=
\int_{x_0}^{\infty}
\phi(x)\,
\overline\Phi\!\left(
\frac{h_p(x)-cx}{\sqrt{1-c^2}}
\right)dx,
\tag{6.1}
\]

where

\[
u_0=\frac{p}{2-p},\qquad
x_0=\Phi^{-1}(u_0),
\]

and

\[
h_p(x)=
\Phi^{-1}\!\left(
\frac{p\Phi(x)}{2\Phi(x)-p}
\right).
\tag{6.2}
\]

The boundary has its fixed point at `x=Phi^{-1}(p)`.

A first naive `u`-space quadrature produced apparent tiny negative margins near `c=0.999` and very small `p`. Those were **spurious**: the near-comonotone boundary layer around the fixed point was underresolved. Reintegrating in Gaussian `x` coordinates and splitting explicitly at the fixed point restored positive margins. This is exactly the kind of numerical false counterexample that must not be certified.

A bounded exploratory scan over bivariate correlations up to `0.999`, unequal weights, and thresholds down to `10^{-4}` found no robust negative margin. Additional random positive-factor Gaussian correlation experiments likewise produced no certified counterexample. These calculations are scouting only; they are not a theorem and no numerical result is promoted to the ledger metric.

The important methodological output is the warning: any future counterexample checker must resolve the `c -> 1`, `p -> 0` boundary layer analytically or by interval arithmetic, not ordinary black-box quadrature.

## 7. B5 — differentiate in the Gaussian correlation: exact formula, but monotonicity fails as a local route

For the bivariate equal-weight family above define

\[
I_p(c)=\mathbb P_c(H>p).
\]

Let `varphi_c(x,y)` be the bivariate standard-normal density with correlation `c`. Using the standard identity

\[
\partial_c\varphi_c=\partial_x\partial_y\varphi_c
\]

and differentiating the moving-boundary integral (6.1) gives, for `0<c<1`,

\[
\boxed{
I_p'(c)=
\int_{x_0}^{\infty}
\frac{[-h_p'(x)]\,[h_p(x)-cx]}
{1-c^2}
\,\varphi_c(x,h_p(x))\,dx.
}
\tag{7.1}
\]

This is an exact parameter-derivative formula and appears at first to offer a direct deformation from independence to comonotonicity.

However, it also shows why a naive monotonicity proof fails. At the fixed point

\[
x=h_p(x)=z_p:=\Phi^{-1}(p),
\qquad -h_p'(z_p)=1,
\]

so the local factor in (7.1) has the sign of

\[
(1-c)z_p.
\]

For every `p<1/2`, this is **negative**. Thus the boundary integrand is not pointwise nonnegative in the hard low-threshold regime. Exploratory evaluation is consistent with `I_p(c)` initially decreasing in `c` for sufficiently small `p` and then returning to the comonotone endpoint `I_p(1)=1-p`.

Therefore the conjecture cannot be proved merely by saying “positive Gaussian correlation monotonically increases the harmonic-mean upper tail.” Any successful correlation interpolation must exploit a global pairing/cancellation of the boundary, not pointwise sign.

This is a useful failure: it identifies the hard mechanism rather than adding another scalar lemma.

## 8. What remains

The source conjecture is now reduced to the lower half

\[
\boxed{0<p<1/2}.
\]

The exact full-source obligation remains

\[
\mathbb P\{M_{-1}^{\mathbf w}(\Phi(X_1),\ldots,\Phi(X_n))\le p\}\ge p
\]

for every positive-correlation Gaussian covariance, all positive weights and every `0<p<1/2`.

The most promising immediate special case is the bivariate equal-weight family (6.1). Its boundary map in uniform coordinates,

\[
T_p(u)=\frac{pu}{2u-p},
\]

is a decreasing involution. The exact derivative (7.1) suggests pairing the two sides of this involution rather than attempting pointwise positivity. A proof for this family would remain PARTIAL, but it would decide a nontrivial all-threshold positive-Gaussian subcase and expose the mechanism needed for higher dimension.

Reserved next Section-B moves, distinct from this run: **B6 DEFORM TO A POINT YOU CAN SOLVE** (quantitative deformation from `c=1` while resolving the low-`p` boundary layer), **B11 DUALIZE** (seek a dual/tangent certificate for the reciprocal-Gaussian superlevel set), and **B24 FIND THE EXTREMAL OBJECT** (test whether the worst Gaussian covariance at fixed weights is an endpoint/equicorrelation/rank-one structure).

## 9. Model / scheduler control boundary

Still true in the actual exposed control surface: model/reasoning are not binding scheduler fields available to this worker. The current policy file records title/prompt/schedule/timing/enabled controls but no model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry and no guaranteed-duration field. GPT-6/maximum therefore remains prompt-only here. I report the actual surfaced model as GPT-5.6 Sol and reasoning as UNVERIFIED.

The historical P26 `You cannot modify this task` event is an authorization/context boundary; repository history also records later successful changes from an authorized context. The legitimate remedies are the owning authorized context, ownership/admin transfer, or platform support—not duplicate schedules or permission bypass. No scheduler modification was attempted in this run.

## 10. Checker / archive discipline

No finite theorem core was introduced: Theorem R09-GAUSS-UPPER-HALF is a direct analytic proof on the page. I therefore did **not** manufacture an exact checker merely to create an artifact. The numerical negation search is explicitly exploratory and is not used as a certificate.

No shared root, peer-track file, email/Gmail, Drive, public post, purchase, permission, workflow or scheduler state was changed.

## 11. Structured ledger delta

```yaml
ledger_delta:
  track: R09
  lane: CLOSABLE_OUTSIDE
  predecessor_state:
    tang_q411_periodic:
      status: REFUTED_RETIRED
      metric: UNBOUNDED_ABOVE
      retirement_count: 6
    g0013:
      status: OPEN_CURRENT_PARTIAL_HANDOFF_READY_RETIRED_FROM_R09
      U_star: "1289727882057511/11918000000000000"
      supported_unchanged_count: 6
  admission_screen:
    D0012:
      status: HOLD_SCOPE_PENDING_NOT_READY
      reason: "broad aggregation-set characterization; 2019 standard-uniform result is only a partial answer"
    CHEN_WANG_2025_GAUSSIAN_SUBUNIFORM:
      status: READY_CLAIMED_OPEN_CURRENT_PARTIAL
      claim_commit: "6e603ae9ddb0f1d277c7a8768873ba42faed77b5"
      source: "Chen--Wang--Wang--Zhu, Subuniformity of harmonic mean p-values, CJS, DOI 10.1002/cjs.70017"
  metric:
    name: p_cert
    direction: smaller_is_better
    before: 1
    after: 0.5
    movement: true
  theorem:
    id: R09-GAUSS-UPPER-HALF
    statement: "For any Gaussian copula, any weights, any r<=0, subuniformity holds for all p>=1/2"
    source_scope: PARTIAL
  methods: [B2, B5, B18]
  negation_search:
    certified_counterexample: none
    warning: "near-comonotone low-p boundary layer causes spurious ordinary-quadrature negatives"
  checker: none_analytic_theorem_no_finite_core
  next_moves: [B6, B11, B24]
  shared_root_edits: none
  scheduler_changes: none
  email_drive_public_posting: none
```
