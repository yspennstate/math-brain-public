Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; GPT-6/maximum was requested in prompt text, but the exposed scheduler has no model/reasoning selector. **No movement in the frozen metric:** `B=infinity -> B=infinity`. Methods tried: **B15, B18, B24**.

# HARD7-01 run 2 — a negative transverse Hessian direction off the product manifold

Status: **PARTIAL** for the full even-log-concave dimensional Brunn--Minkowski conjecture. This run does not prove or refute the source conjecture. It identifies, with an exact certificate, a feasible cross-block direction in which the sign-equivalent Brunn--Minkowski defect has strictly negative second variation. Thus the most naive local extension of the run-1 tensorization theorem by transverse convexity is false.

## 1. Continuity and current-state recovery

The admitted canonical target remains `operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md`, owned by HARD7-01. Its source statement is:

For every `n>=1`, every even log-concave probability measure `mu` on `R^n`, all nonempty centrally symmetric convex sets `K,L`, and every `lambda in [0,1]`,
\[
\mu((1-\lambda)K+\lambda L)^{1/n}
\ge (1-\lambda)\mu(K)^{1/n}+\lambda\mu(L)^{1/n}.
\tag{DBM}
\]

I resumed the unique preceding HARD7-01 report,
`runs/hard7_2026-09-18/HARD7-01/2026-09-18T21-03-00Z__admission_tensorization.md`.
That run proved harmonic tensorization for common Cartesian product decompositions and moved the fixed block-count metric from `B=1` to all finite block counts (`B=infinity`). It explicitly left genuinely irreducible cross-block geometry as the next obligation. The present run does not restart admission or re-prove tensorization.

At run start I reread the controlling HARD7 and new-methods policies, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md` and `RANKING.md`, the current claim, and the latest neighboring KLS/log-concave report located by repository search. Repository-wide alias searches for `Brunn-Minkowski`, `dimensional Brunn-Minkowski`, and `log-concave` recover HARD7-01 as the owner of this source target and no competing equivalent claim. The intake JSONL corpus is too large for the connector to return as one semantic document; I used repository-wide searches across the intake/claim material rather than pretending to have obtained an untruncated 780-row read.

### Fresh literature/status check

A bounded current search on 2026-09-18 UTC rechecked:

- Kai-Wen Yang, *A uniform bound in the dimensional Brunn--Minkowski inequality for even log-concave measures*, arXiv:2607.10104 (11 July 2026): same even-log-concave/symmetric-body scope, with `p_n >= c/(n^2 log n)`, not the conjectured `1/n`.
- Alexandros Eskenazis, Apostolos Giannopoulos, Natalia Tziotziou, *Functional perimeter and the dimensional Brunn-Minkowski inequality for log-concave measures*, arXiv:2605.02747 (4 May 2026): quantitative partial exponent `c_n >= c/(n^3 log n)`.
- Sotiris Armeniakos and Jacopo Ulivelli, *A strengthening of the dimensional Brunn-Minkowski conjecture implies the (B)-Conjecture*, arXiv:2602.23350 (26 February 2026): a stronger condition and a hereditarily-convex class, not a resolution of the full target.
- Armeniakos--Ulivelli, *A new infinitesimal form of the Prekopa--Leindler inequality with multiplicative structure and applications*, arXiv:2602.10812 (11 February 2026): reformulations/partial results.

No later full `p_n=1/n` resolution was located in this bounded search. That is a current-status search result, not proof of worldwide openness. The run-1 tensorization mechanism also remains novelty-UNVERIFIED and may be folklore.

## 2. Frozen quantity

The fixed metric from admission is

`B = largest number of 1D/2D factors for which (DBM) is proved at the source exponent for every common block-product instance`.

Before this run: `B=infinity` (all finite block counts), from run 1.

After this run: `B=infinity`.

Therefore this run has **no movement in the frozen quantity**. The mathematical progress is instead a source-relevant obstruction that sharply identifies what a successful irreducible-extension argument must survive. This is the first unchanged run after the run-1 movement, not a section-I stuck episode.

## 3. B18 — rewrite the source defect as a perturbative covariance Hessian

Let
\[
J_A(\varepsilon)=\int_A e^{-V_0(x)-\varepsilon W(x)}\,dx
\]
for `A` equal to `K`, `L`, or
\[
M=(1-\lambda)K+\lambda L.
\]
The normalization of the probability density cancels from the sign of (DBM): if
`Z_epsilon = J_{R^n}(epsilon)`, every term in the normalized DBM defect carries the same positive factor `Z_epsilon^{-1/n}`. Hence it is enough to study the sign-equivalent unnormalized defect
\[
D(\varepsilon)
=J_M(\varepsilon)^{1/n}
 -(1-\lambda)J_K(\varepsilon)^{1/n}
 -\lambda J_L(\varepsilon)^{1/n}.
\tag{1}
\]

For `h_A=J_A^{1/n}`, differentiation under the integral gives
\[
\frac{h_A'}{h_A}=-\frac1n\,\mathbb E_{A,\varepsilon}W,
\tag{2}
\]
and
\[
\frac{h_A''}{h_A}
=\frac1n\operatorname{Var}_{A,\varepsilon}(W)
 +\frac1{n^2}\big(\mathbb E_{A,\varepsilon}W\big)^2.
\tag{3}
\]
Here the expectation is with respect to the density proportional to
`1_A e^{-V_0-epsilon W}`.

Now let the base measure and all three sets share a Cartesian block decomposition,
\[
e^{-V_0(x)}dx=\bigotimes_{j=1}^m e^{-V_j(x_j)}dx_j,\qquad
A=\prod_{j=1}^m A_j,
\]
with every block restriction even. Take a purely cross-block bilinear perturbation
\[
W(x)=\sum_{r<s}\langle x_r,T_{rs}x_s\rangle.
\tag{4}
\]
Every conditional first moment is zero, so
\[
\mathbb E_{A,0}W=0,
\qquad D'(0)=0.
\tag{5}
\]
Independence and centering also kill every mixed cross term in `E W^2`, giving the exact quadratic form
\[
Q_A(T):=\mathbb E_{A,0}W^2
=\sum_{r<s}\operatorname{Tr}
\!\left(T_{rs}\Sigma_{s,A}T_{rs}^{\mathsf T}\Sigma_{r,A}\right),
\tag{6}
\]
where
\[
\Sigma_{j,A}:=\mathbb E[x_jx_j^{\mathsf T}\mid x_j\in A_j].
\]
Combining (1)--(6),
\[
D''(0)=\frac1n\left[
h_M Q_M
-(1-\lambda)h_K Q_K
-\lambda h_L Q_L
\right].
\tag{7}
\]

Equation (7) is the transverse Hessian of the sign-equivalent source defect at a product instance. It converts the first genuinely irreducible question into an explicit covariance comparison.

## 4. B24 — an exact negative transverse direction

I then looked for an extremal direction making the bracket in (7) negative. The following three-dimensional rational box instance works exactly.

Set `lambda=1/2` and use centered boxes with half-width vectors
\[
K_0=\left(\frac34,1,1\right),\qquad
L_0=\left(\frac15,\frac14,\frac14\right),
\]
so
\[
M_0=\frac12(K_0+L_0)
=\left(\frac{19}{40},\frac58,\frac58\right).
\]
Take
\[
W(x)=x_1x_2+x_2x_3+x_3x_1.
\tag{8}
\]

For a uniform centered box with half-widths `(a1,a2,a3)`, omit the common volume factor `8` and write
\[
p=a_1a_2a_3,\qquad
S=\mathbb E W^2
=\frac{a_1^2a_2^2+a_2^2a_3^2+a_3^2a_1^2}{9}.
\tag{9}
\]
Direct rational arithmetic gives
\[
p_K=\frac34,\quad S_K=\frac{17}{72},
\]
\[
p_L=\frac1{80},\quad S_L=\frac{19}{19200},
\]
and
\[
p_M=\frac{95}{512},\quad S_M=\frac{449}{12288}.
\tag{10}
\]

The ordinary DBM margin, with the common positive factor `2=8^{1/3}` removed, is
\[
g=p_M^{1/3}-\frac12p_K^{1/3}-\frac12p_L^{1/3}>0.
\tag{11}
\]
Thus the product instance itself strictly satisfies the source inequality.

But the transverse second-variation sign is governed by
\[
q=p_M^{1/3}S_M
-\frac12p_K^{1/3}S_K
-\frac12p_L^{1/3}S_L.
\tag{12}
\]
The exact checker proves
\[
\frac{17184150006581}{400000000000000000}
<g<
\frac{85920750032909}{2000000000000000000},
\tag{13}
\]
while
\[
-\frac{62304859527064652989}{720000000000000000000}
<q<
-\frac{8861135577182528409221}{102400000000000000000000}
<0.
\tag{14}
\]
Numerically only for orientation,
`g ≈ 4.2960e-5` and `q ≈ -8.65345e-2`; the proof is the rational enclosure (13)--(14), not floating point.

At the formal uniform-box base,
\[
D''(0)=\frac23 q<0.
\tag{15}
\]
The exact script and archived output for (10)--(14) are in this run's `artifacts/` directory and end `ALL_EXACT_CHECKS_PASS`.

This does **not** by itself give a source counterexample, because the indefinite quadratic `W` in (8) need not preserve log-concavity when added to a flat uniform potential. The next step is to make the same negative direction admissible.

## 5. B15 — break product independence while staying inside even log-concavity

Define a strongly convex non-Gaussian product potential on `R^3`,
\[
V_0(x)=\sum_{i=1}^3(x_i^2+x_i^4),
\tag{16}
\]
and retain `W` from (8). For `|epsilon|<=1/2`, set
\[
V_\varepsilon=V_0+\varepsilon W,\qquad
d\mu_\varepsilon=Z_\varepsilon^{-1}e^{-V_\varepsilon(x)}\,dx.
\tag{17}
\]

The Hessian of `V_0` is at least `2I`. The Hessian of `W` is
\[
B=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix},
\]
whose eigenvalues are `2,-1,-1`. Therefore, for every `|epsilon|<=1/2`,
\[
\nabla^2V_\varepsilon\succeq I.
\tag{18}
\]
Moreover `V_epsilon(-x)=V_epsilon(x)`. Hence (17) is an even, strongly log-concave probability measure throughout the entire interval, and for nonzero epsilon it genuinely couples the three coordinates.

Scale the boxes:
\[
K_t=tK_0,\qquad L_t=tL_0,\qquad M_t=tM_0.
\tag{19}
\]
At `epsilon=0`, the measure is a product and each restricted block is even, so the exact first-order cancellation (5) holds for every `t`:
\[
D_t'(0)=0.
\tag{20}
\]

Now substitute `x=ty`. Uniformly on each fixed box,
\[
e^{-V_0(ty)}=1+O(t^2).
\]
Consequently,
\[
J_{A_t}(0)^{1/3}
=2t\,p_A^{1/3}(1+O(t^2)),
\tag{21}
\]
and because `W(ty)^2=t^4W(y)^2`,
\[
\mathbb E_{A_t,0}W^2=t^4(S_A+O(t^2)).
\tag{22}
\]
Putting (21)--(22) into the exact Hessian formula (7) with `n=3` and `lambda=1/2`,
\[
D_t''(0)=\frac23\,t^5 q+O(t^7).
\tag{23}
\]
Since the exact certificate gives `q<0`, there exists `t_0>0` such that
\[
D_t''(0)<0\qquad(0<t<t_0).
\tag{24}
\]

This is the run's main partial theorem:

> **Transverse-obstruction theorem.** There exist an even strongly log-concave non-Gaussian product measure on `R^3`, symmetric convex product bodies `K,L`, and an admissible smooth one-parameter family of even strongly log-concave measures that breaks product independence, such that the sign-equivalent dimensional Brunn--Minkowski defect is stationary to first order and strictly decreases to second order in the coupling parameter.

The theorem is a local obstruction, not a refutation. In fact (11) and (21) show the base defect is strictly positive for the displayed small-box family, so continuity preserves the source inequality for sufficiently small `epsilon`. What fails is the tempting strategy "tensorization plus nonnegative transverse Hessian extends the theorem to irreducible measures."

## 6. What the three methods established

- **B15 BREAK THE SYMMETRY ON PURPOSE.** Broke block independence, while preserving central symmetry and strong log-concavity, via the cross-block family (17). **Succeeded:** the negative formal direction is realizable inside the exact source class.
- **B18 SAY IT IN ANOTHER LANGUAGE.** Recast the source inequality as the sign of the unnormalized defect (1) and derived the covariance Hessian (7). **Succeeded:** the first irreducible perturbation is an explicit quadratic-form comparison.
- **B24 FIND THE EXTREMAL OBJECT.** Searched for a dangerous transverse configuration rather than another positive lemma. **Succeeded:** the rational boxes (10) give the exact certificate `g>0` but `q<0`.

The next run must use a different triple. A useful target is to characterize when the quadratic form in (7) is nonnegative, or to combine the negative direction with a finite-amplitude convex perturbation and test whether the defect can actually reach zero. Any finite-amplitude candidate must be proved continuously, not inferred from sampling.

## 7. Capability and scheduler honesty

The exposed native scheduler schema still offers title, prompt, schedule, timing mode and enabled state, but no model selector, reasoning-effort selector or guaranteed duration. Therefore GPT-6/maximum remains a prompt request only; changing it requires a platform capability or authorized configuration surface not exposed to this run.

The current root `RESULTS.md` records an important update to the older permission story: P26 was later successfully updated in one authorized context, while another context had returned `You cannot modify this task`. Thus the denial is context/ownership-specific evidence, not proof that P26 is globally immutable. The permitted workaround is to use the authorized task/account/workspace context or platform support; a repository edit or duplicate schedule is not a scheduler repair. This run did not modify any other schedule.

## 8. Exact artifact

Executed exact checker:
`artifacts/hard7_2026-09-18/HARD7-01/2026-09-18T22-15-00Z__transverse_hessian_exact.py`

Archived stdout:
`artifacts/hard7_2026-09-18/HARD7-01/2026-09-18T22-15-00Z__transverse_hessian_exact.out`

The output ends `ALL_EXACT_CHECKS_PASS`. The checker certifies only the finite rational/cube-root inequalities (10)--(14). The perturbative theorem is proved on the page above; the script is not a substitute for that proof.

## 9. ledger_delta

```yaml
track: HARD7-01
source: even-log-concave dimensional Brunn-Minkowski conjecture
claim: operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md
metric: maximum low-dimensional block count B covered at source exponent for all common block-product instances
metric_before: infinity
metric_after: infinity
movement: no movement
status_before: PARTIAL
status_after: PARTIAL
unchanged_count_before: 0
unchanged_count_after: 1
methods_this_run: [15, 18, 24]
new_partial_result: exact negative transverse Hessian direction, realized by an admissible even strongly log-concave cross-block coupling in dimension 3
remaining_obligation: prove or refute DBM for genuinely irreducible even log-concave instances; nonnegative transverse-Hessian continuation is ruled out as a universal route
novelty: UNVERIFIED; elementary perturbative mechanism may be folklore
closure_audits: 0
```
