Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No movement in the frozen metric: `B=infinity -> B=infinity`. Methods tried: B1 / B11 / B30.**

# HARD7-01 run 9 — transverse concavity for the fully mixed quartic parallelotope recovery

Status: **PARTIAL / second-recovery action / source OPEN**. This run executes the exact action selected by the preceding STUCK2 report: attack the fixed fully mixing Householder orientation directly through the centered-box Hessian, rather than returning to radial-survival or generic boundary-flux arguments.

## 1. Continuity, ownership, repository state, and current literature

I resumed the exclusive claim

`operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md`,

owned by HARD7-01. The source target remains the full dimensional Brunn--Minkowski conjecture

\[
\mu((1-\lambda)K+\lambda L)^{1/n}
\ge (1-\lambda)\mu(K)^{1/n}+\lambda\mu(L)^{1/n}
\tag{DBM}
\]

for every integer `n>=1`, every even log-concave probability measure `mu` on `R^n`, all nonempty centrally symmetric convex sets `K,L`, and every `lambda in [0,1]`.

At run start I reread `operations/hard7_2026-09-18/CONTROL.md`, the current `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, the canonical claim, and the newest HARD7-01 checkpoint. Repository-wide claim/alias search still records `GZ-DIMBM-EVEN-LOGCONCAVE` as hard-owned by HARD7-01 and did not expose a competing equivalent owner. The old Gaussian-neighbor R09 line has rotated to unrelated successor admission/percolation work, so it is not a live equivalent target.

The preceding checkpoint is

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T04-12-00Z__stuck2_parallelotope_recovery.md`.

It selected **B1/B11/B30** and exactly one second-recovery action: prove the simplest still-unproved source-valid subclass, namely concavity of the centered-box mass at the fully mixing orientation

\[
U_*=I-\frac23\mathbf 1\mathbf 1^T
=\frac13\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix}.
\tag{1.1}
\]

A fresh bounded current-status search on **2026-09-19** again found no primary source claiming the full even-log-concave `1/n` theorem or this exact quartic-product / fully-mixed parallelotope subclass. In particular:

- Kai-Wen Yang, *A uniform bound in the dimensional Brunn--Minkowski inequality for even log-concave measures*, arXiv:2607.10104, posted **11 July 2026**, treats the same global class but proves only `p_n >= c/(n^2 log n)`: https://arxiv.org/abs/2607.10104 .
- Alexandros Eskenazis, Apostolos Giannopoulos, Natalia Tziotziou, *Functional perimeter and the dimensional Brunn-Minkowski inequality for log-concave measures*, arXiv:2605.02747, posted **4 May 2026**, gives an exponent of order `c/(n^3 log n)`: https://arxiv.org/abs/2605.02747 .
- Sotiris Armeniakos and Jacopo Ulivelli, *A strengthening of the dimensional Brunn-Minkowski conjecture implies the (B)-Conjecture*, arXiv:2602.23350, posted **26 February 2026**, confirms that a stronger route is genuinely tied to the still-delicate `(B)` mechanism: https://arxiv.org/abs/2602.23350 .
- The known dimension-two / unconditional results of Livshyts--Marsiglietti--Nayar--Zvavitch and rotationally invariant results of Cordero-Erausquin--Rotem remain the nearest full-exponent solved regimes recorded in the claim and preceding reports.

This is bounded negative evidence, not a worldwide novelty certificate.

## 2. Frozen source metric

The canonical metric is still

`B = largest number of 1D/2D factors for which (DBM) is proved at source exponent for every common block-product instance`.

Run 1 already proved all finite block counts, hence

\[
\boxed{B=\infty\longrightarrow B=\infty.}
\]

There is **no movement** and I do not relabel the theorem below as movement of `B`.

## 3. B1 — change category: a general centered-box sign theorem

The second recovery writes the problem as a box probability. Let `f:R^3 -> (0,infinity)` be a `C^1`, centrally symmetric, log-concave density and define

\[
F(a_1,a_2,a_3)
=\int_{-a_1}^{a_1}\int_{-a_2}^{a_2}\int_{-a_3}^{a_3}
 f(y_1,y_2,y_3)\,dy_3dy_2dy_1,
\qquad a_i>0.
\tag{3.1}
\]

For the quartic recovery, `f(y)=Z^{-1}e^{-W_{U_*}(y)}` with

\[
W_{U_*}(y)=\frac14\sum_{j=1}^3 (U_*y)_j^4.
\tag{3.2}
\]

The following sign structure is valid more generally and is the first useful new fact of this run.

### Proposition 3.1 — centered-box Hessian has negative pure and positive mixed curvature

For every `a in (0,infinity)^3`,

\[
\partial_{ii}F(a)\le0,
\qquad
\partial_{ij}F(a)>0\quad(i\ne j).
\tag{3.3}
\]

**Proof.** Fix `i=1`; the other indices are identical. For fixed `a_2,a_3`, put

\[
h(s)=\int_{-a_2}^{a_2}\int_{-a_3}^{a_3}f(s,u,v)\,dvdu.
\tag{3.4}
\]

By Prekopa's theorem, `h` is log-concave because it is the marginal of the log-concave function

\[
(s,u,v)\mapsto f(s,u,v)\mathbf 1_{[-a_2,a_2]\times[-a_3,a_3]}(u,v).
\]

Central symmetry of `f` and symmetry of the integration rectangle give

\[
h(-s)=h(s).
\]

An even log-concave function is nonincreasing on `[0,infinity)`, hence `h'(a_1)<=0`. Differentiating the two moving faces gives

\[
\partial_1F=h(a_1)+h(-a_1)=2h(a_1),
\qquad
\partial_{11}F=2h'(a_1)\le0.
\tag{3.5}
\]

For `i=1,j=2`, two applications of the endpoint rule yield

\[
\partial_{12}F(a)
=\sum_{\varepsilon_1,\varepsilon_2\in\{\pm1\}}
\int_{-a_3}^{a_3}
 f(\varepsilon_1a_1,\varepsilon_2a_2,s)\,ds.
\tag{3.6}
\]

Every term is positive because `f>0`, proving `partial_{12}F>0`; permutation of coordinates gives all other mixed derivatives. ∎

Thus the box-mass Hessian is a symmetric **Metzler-sign** matrix: nonpositive diagonal and positive off-diagonal. This is not enough by itself for concavity, but it exposes precisely where the mixed-facet obstruction lives.

## 4. B11 — dualize the `3 x 3` Hessian by permutation representations

Now assume in addition that `f` is invariant under all coordinate permutations. At a diagonal width vector

\[
a=t\mathbf1=(t,t,t),\qquad t>0,
\]

permutation invariance forces

\[
\nabla F(t\mathbf1)=g(t)\mathbf1,
\tag{4.1}
\]

and

\[
D^2F(t\mathbf1)
=\big(d(t)-o(t)\big)I+o(t)J,
\tag{4.2}
\]

where `J=11^T`,

\[
d(t)=\partial_{11}F(t\mathbf1)\le0,
\qquad
o(t)=\partial_{12}F(t\mathbf1)>0.
\tag{4.3}
\]

This decomposes the Hessian exactly into the trivial representation `span{1}` and the two-dimensional standard representation `1^perp`.

Let

\[
G(a)=F(a)^{1/3}.
\tag{4.4}
\]

Then

\[
D^2G
=\frac13F^{-2/3}D^2F
-\frac29F^{-5/3}(\nabla F)(\nabla F)^T.
\tag{4.5}
\]

For every nonzero transverse vector `z` satisfying `z_1+z_2+z_3=0`, the rank-one term vanishes and (4.2) gives

\[
z^TD^2G(t\mathbf1)z
=\frac13F(t\mathbf1)^{-2/3}
\big(d(t)-o(t)\big)\|z\|^2<0.
\tag{4.6}
\]

The strict sign follows from `d<=0` and `o>0`.

### Theorem 4.1 — strict transverse `1/3`-concavity at every diagonal box

If `f` is positive, centrally symmetric, permutation-invariant and log-concave on `R^3`, then the function

\[
(a_1,a_2,a_3)\mapsto
\left(\int_{[-a_1,a_1]\times[-a_2,a_2]\times[-a_3,a_3]}f\right)^{1/3}
\]

has strictly negative Hessian on the entire two-dimensional subspace `1^perp` at every point `(t,t,t)`, `t>0`.

This is an on-page analytic theorem; it is not a finite/exhaustive assertion and therefore no checker was manufactured for it.

The same representation decomposition identifies the *only* diagonal mode not settled by Theorem 4.1. In the radial direction `1`, (4.5) is nonpositive exactly when

\[
F(t\mathbf1)\big(d(t)+2o(t)\big)\le2g(t)^2.
\tag{4.7}
\]

Indeed, if `q(t)=F(t,t,t)`, then

\[
q'(t)=3g(t),
\qquad
q''(t)=3\big(d(t)+2o(t)\big),
\tag{4.8}
\]

so (4.7) is precisely

\[
3q(t)q''(t)\le2q'(t)^2,
\tag{4.9}
\]

i.e. ordinary one-variable concavity of `q(t)^{1/3}`.

Thus at a permutation-symmetric diagonal point the full `3 x 3` Hessian problem is **exactly one scalar radial inequality plus two automatically strict transverse inequalities**.

## 5. B30 — localize to the fully mixing Householder orientation

For the selected matrix `U_*`, note that

\[
U_*=I-\frac23J
\]

commutes with every coordinate permutation. Since `x -> sum_i x_i^4/4` is permutation-invariant, `W_{U_*}` in (3.2) is permutation-invariant. It is convex because it is a convex quartic potential composed with an orthogonal map, and it is even. Hence

\[
f_{U_*}(y)=Z^{-1}e^{-W_{U_*}(y)}
\]

satisfies every hypothesis of Theorem 4.1.

Therefore, for the exact source-valid fully mixed common-normal parallelotope family selected at STUCK2,

\[
P_{U_*}(a)=\{x: |(U_*x)_i|\le a_i,\ i=1,2,3\},
\tag{5.1}
\]

the desired `1/3`-concavity has now been proved **infinitesimally in every shape-changing direction at every cubic member** `a=t1`. Two of the three Hessian eigenmodes are settled for every `t>0`.

The remaining diagonal mode is the homothetic cube dilation. It is exactly the scalar condition already isolated in run 6. For

\[
A=P_{U_*}(\mathbf1),
\qquad
m(t)=\mathbb E[V(X)\mid X\in tA],
\qquad
v(t)=\operatorname{Var}(V(X)\mid X\in tA),
\]

run 6 showed that radial `1/3`-concavity is equivalent to

\[
\boxed{4m(t)^2+12v(t)\le15m(t).}
\tag{5.2}
\]

Consequently the diagonal Hessian problem for the fully mixed Householder boxes has been reduced from a correlated `3 x 3` matrix inequality to the single scalar conditional-energy inequality (5.2). What is *not* proved is (5.2) for every `t`, nor the Hessian inequality away from the diagonal `a_1=a_2=a_3`.

This matters because it separates the two difficulties cleanly:

1. **shape modes at cubic boxes:** settled strictly by Prekopa plus facet/edge signs;
2. **radial mode:** the conditional quartic-energy inequality (5.2);
3. **off-diagonal widths:** loss of the `S_3` representation decomposition, where the positive mixed-face terms must be balanced non-symmetrically.

## 6. Outcomes of the three required new-method moves

**B1 — CHANGE THE CATEGORY: succeeded.** Recasting the recovery as a centered-box probability exposed the global sign theorem (3.3), which was invisible in the generic moving-body formulation.

**B11 — DUALIZE: succeeded.** At diagonal widths, `S_3` representation theory diagonalizes the derivative matrix into one radial and two transverse modes. The transverse modes are now rigorously negative, and the full local question is equivalent to one scalar inequality.

**B30 — ONE SCALE / ONE DIRECTION AT A TIME: succeeded partially.** For the exact fully mixing `U_*` family, every shape-changing tangent direction at every cubic member is closed. The unresolved radial mode is (5.2); arbitrary unequal widths remain open.

No numerical sampling is used as proof, and no discrete path/finite checker is relevant to these analytic claims.

## 7. Section-I accounting

This run is the substantive action chosen by the **second and final** STUCK recovery. It produced a genuine theorem and sharpened the remaining obligation, but the frozen source metric `B` did not move. I do not open a third recovery here.

Under the owner's protocol, if the next invocation again triggers the formal stuck condition through the unchanged frozen metric, it must **handoff and rotate to a fresh admissible externally posed hard target**, rather than adding another lemma to this source. The useful handoff checkpoint is now explicit: any fresh route on this target should begin from the scalar radial inequality (5.2) and the off-diagonal-width problem, not re-prove transverse diagonal concavity.

## 8. Scheduler/model capability truth

The actual model visible to this run is **GPT-5.6 Sol**. The reasoning level is **UNVERIFIED**. This is not GPT-6 at maximum and I do not claim otherwise.

The currently exposed scheduler interface still has no model selector, reasoning-effort selector, or guaranteed execution-duration control. GPT-6/maximum therefore remains a prompt request only. Changing that requires a product/platform capability that exposes those controls; a GitHub repository edit cannot do it.

The controlling policy also records that native modification probes for P26 (and P01/P03) returned **`You cannot modify this task`**. The authorized workaround is to resolve task/account/workspace ownership in the authorized scheduler interface or through platform support; do **not** bypass the restriction by creating a duplicate schedule. No schedule was created, modified, disabled, or reactivated in this run.

## 9. ledger_delta

```yaml
ledger_delta:
  worker: HARD7-01
  target: GZ-DIMBM-EVEN-LOGCONCAVE
  source_status: OPEN
  research_status_before: PARTIAL_STUCK2
  research_status_after: PARTIAL_SECOND_RECOVERY_ACTION
  metric: B
  before: infinity
  after: infinity
  movement: none
  methods: [B1, B11, B30]
  new_result: "strict transverse 1/3-concavity at every permutation-symmetric diagonal centered box; applies to U_* quartic recovery"
  exact_remaining_diagonal_obligation: "4 m(t)^2 + 12 v(t) <= 15 m(t) for A=P_{U_*}(1), all t>0"
  off_diagonal_obligation: "control unequal-width fully mixed box Hessian"
  closure: false
  next_if_formally_stuck: "handoff and rotate; no third recovery"
```
