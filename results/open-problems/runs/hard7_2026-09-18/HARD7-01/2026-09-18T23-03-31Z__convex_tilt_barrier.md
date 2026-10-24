Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run is not verified as GPT-6 at maximum. **No movement in the frozen metric:** `B=infinity -> B=infinity`. Methods tried: **B4, B6, B20**.

# HARD7-01 run 3 — convex-tilt barrier at homothetic equality

Status: **PARTIAL** for the full even-log-concave dimensional Brunn--Minkowski conjecture. This run does not prove or refute the source conjecture. It proves a new source-valid one-sided tangent theorem showing that a large natural counterexample route cannot leave the Lebesgue equality manifold in the wrong direction: every even convex potential tilt of a uniform log-concave measure opens a homothetic Brunn--Minkowski equality with the correct first-order sign, and a strongly convex tilt opens it quantitatively.

## 1. Continuity and repository recovery

The canonical claim remains

`operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md`,

owned by HARD7-01, with exact source target

\[
\mu((1-\lambda)K+\lambda L)^{1/n}
\ge (1-\lambda)\mu(K)^{1/n}+\lambda\mu(L)^{1/n}
\tag{DBM}
\]

for every even log-concave probability measure on `R^n`, all nonempty centrally symmetric convex sets `K,L`, and every `lambda in [0,1]`.

I reread `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, the current claim, both preceding HARD7-01 reports, and repository-wide alias/collision search results. The repository search still returns HARD7-01 as the unique owner of the exact even-log-concave dimensional Brunn--Minkowski target; no competing canonical claim was found. The intake corpus cannot be returned by the connector as one untruncated 780-row object, so I used repository-wide exact-name/alias searches across the indexed intake/claims/reports rather than pretending to have read an unavailable monolithic dump.

The previous run proved an exact negative second-variation direction transverse to product structure, but also identified its obstruction: the useful quadratic coupling is indefinite, so at a flat uniform base it does not preserve log-concavity; making the base strongly convex admits the coupling but destroys exact equality and leaves a positive zeroth-order source gap. This run attacks that obstruction directly.

### Current literature/status check

A fresh bounded search on 2026-09-18 UTC again found no full resolution of the exact source scope. In particular:

- Kai-Wen Yang, *A uniform bound in the dimensional Brunn--Minkowski inequality for even log-concave measures*, arXiv:2607.10104 (11 July 2026), states the same even-log-concave/symmetric-body conjecture and proves only `p_n >= c/(n^2 log n)`.
- Alexandros Eskenazis, Apostolos Giannopoulos, Natalia Tziotziou, *Functional perimeter and the dimensional Brunn-Minkowski inequality for log-concave measures*, arXiv:2605.02747 (4 May 2026), proves `c_n >= c/(n^3 log n)`.
- Yang's introduction explicitly says the full conjecture remains open for general even log-concave measures in dimensions `n>=3` and recalls the solved Gaussian, rotationally invariant, dimension-two, and unconditional-measure/unconditional-body regimes.
- The 2017 Livshyts--Marsiglietti--Nayar--Zvavitch theorem covers unconditional log-concave measures with unconditional bodies, not arbitrary even log-concave measures and arbitrary symmetric bodies.

This is a bounded current-status check, not a proof of worldwide openness. The theorem proved below may be elementary folklore; novelty remains **UNVERIFIED**.

## 2. Frozen metric

The admission metric is still

`B = largest low-dimensional block count for which (DBM) is proved at source exponent 1/N for every common block-product instance built from 1D/2D factors`.

Run 1 proved all finite block counts, recorded as `B=infinity`. Run 2 therefore had no metric movement. This run also has

`B=infinity -> B=infinity`.

This is the **second consecutive unchanged run** after the run-1 movement. It does not yet trigger section I's three-unchanged-run protocol. The source remains OPEN and this track remains PARTIAL.

## 3. B6 — deform from an exact equality ensemble

The most tempting way to exploit run 2 is to begin at an exact Brunn--Minkowski equality for Lebesgue measure and turn on a coupling while staying inside the source class.

Let `S subset R^n` be a bounded centrally symmetric convex body with nonempty interior. Let `K` be another centrally symmetric convex body and let `c>0` be such that

\[
K\cup cK\subseteq S.
\]

Fix `lambda in (0,1)`, put

\[
a=1-\lambda,\qquad b=\lambda,\qquad s=a+bc,
\]

and take the homothetic pair

\[
L=cK,\qquad M=(1-\lambda)K+\lambda L=sK.
\]

Let `W:S->R` be even and convex. For `epsilon>=0` define

\[
d\mu_\varepsilon(x)=Z_\varepsilon^{-1}
\mathbf 1_S(x)e^{-\varepsilon W(x)}\,dx.
\tag{1}
\]

Because `S` is convex and symmetric and `W` is convex and even, every `mu_epsilon` is an even log-concave probability measure. At `epsilon=0`, `mu_0` is uniform on `S`, and because `K,cK,sK` all lie in `S`, classical Brunn--Minkowski is an equality for this homothetic pair:

\[
\mu_0(sK)^{1/n}=a\mu_0(K)^{1/n}+b\mu_0(cK)^{1/n}.
\tag{2}
\]

The question is whether an admissible convex tilt can make the source defect immediately negative.

## 4. B4 — prove the first-order statement completely

Define the normalized source defect

\[
\Delta(\varepsilon)
=\mu_\varepsilon(sK)^{1/n}
-a\mu_\varepsilon(K)^{1/n}
-b\mu_\varepsilon(cK)^{1/n}.
\tag{3}
\]

Since the same normalization factor `Z_epsilon^{-1/n}` multiplies every term, write instead

\[
J_r(\varepsilon)=\int_{rK}e^{-\varepsilon W(x)}\,dx,
\qquad
D(\varepsilon)=J_s(\varepsilon)^{1/n}
-aJ_1(\varepsilon)^{1/n}
-bJ_c(\varepsilon)^{1/n},
\tag{4}
\]

so that `Delta(epsilon)=Z_epsilon^{-1/n}D(epsilon)`. Equation (2) gives `D(0)=Delta(0)=0`.

For `r>0`, changing variables `x=ry` gives

\[
J_r(0)=r^n|K|,
\qquad
-\frac{J_r'(0)}{J_r(0)}
=\frac1{|K|}\int_K W(ry)\,dy.
\tag{5}
\]

Hence

\[
\frac{d}{d\varepsilon}J_r(\varepsilon)^{1/n}\Big|_{\varepsilon=0}
=-\frac{|K|^{1/n}}{n}\,F(r),
\tag{6}
\]

where

\[
F(r):=\frac r{|K|}\int_K W(ry)\,dy.
\tag{7}
\]

The key point is that `F` is convex on `[0,infinity)`.

### Lemma 1 — radial convex-tilt functional

If `W` is even and convex, then for every fixed `y`,

\[
r\longmapsto r\,[W(ry)-W(0)]
\tag{8}
\]

is convex on `[0,infinity)`. Consequently `F` in (7) is convex.

#### Proof

For fixed `y`, let

\[
\phi(r)=W(ry)-W(0).
\]

Because `W` is even and convex, `phi` is even and convex, `phi(0)=0`, and `phi` is nonnegative and nondecreasing on `[0,infinity)`. For a smooth approximation,

\[
\frac{d^2}{dr^2}[r\phi(r)]
=2\phi'(r)+r\phi''(r)\ge0.
\]

The general convex case follows by one-dimensional mollification (or by monotonicity of the right derivative). Adding back the linear term `rW(0)` preserves convexity. Integrating over `y in K` preserves convexity, proving the claim for `F`. `square`

Since `s=a+bc`, convexity gives

\[
F(s)\le aF(1)+bF(c).
\tag{9}
\]

Combining (4)--(7),

\[
D'(0)
=\frac{|K|^{1/n}}n
\left[aF(1)+bF(c)-F(s)\right]\ge0.
\tag{10}
\]

Because `D(0)=0`, differentiating `Delta=Z^{-1/n}D` yields

\[
\Delta'(0)=|S|^{-1/n}D'(0)\ge0.
\tag{11}
\]

This proves:

> **Theorem 2 — convex-tilt barrier at homothetic equality.**
> Let `S,K` be centrally symmetric convex bodies in `R^n`, let `c>0` with `K,cK subset S`, and let `W` be even convex on `S`. For the even log-concave path (1), every homothetic source equality `(K,cK)` opens with the correct one-sided first-order sign:
> \[
> \frac d{d\varepsilon}\Big[
> \mu_\varepsilon(((1-\lambda)+\lambda c)K)^{1/n}
> -(1-\lambda)\mu_\varepsilon(K)^{1/n}
> -\lambda\mu_\varepsilon(cK)^{1/n}
> \Big]_{\varepsilon=0^+}\ge0.
> \]
> Thus an admissible convex potential tilt of a uniform log-concave measure cannot produce a first-order counterexample by starting from a homothetic Lebesgue equality.

No finite sampling is involved in this result.

## 5. Quantitative strictness for strongly convex tilts

The same argument gives a quantitative barrier. Suppose `W` is `m`-strongly convex on `S` in Euclidean norm, with `m>0`, and set

\[
M_2(K)=\frac1{|K|}\int_K |y|^2\,dy,
\qquad
r_*=\min\{1,c\}.
\tag{12}
\]

Along each ray, evenness gives the derivative at the origin equal to zero, while strong convexity gives

\[
\phi'(r)\ge mr|y|^2,
\qquad
\phi''(r)\ge m|y|^2
\]

in the smooth case and in the standard a.e./distributional sense in general. Therefore

\[
\frac{d^2}{dr^2}\big(r[W(ry)-W(0)]\big)
\ge 3mr|y|^2.
\]

Averaging over `K` shows that on the interval joining `1` and `c`,

\[
F''(r)\ge 3m r_* M_2(K).
\tag{13}
\]

Strong convexity of this one-dimensional `F` yields the Jensen gap

\[
aF(1)+bF(c)-F(s)
\ge \frac{3m r_* M_2(K)}2\,ab(1-c)^2.
\tag{14}
\]

Hence

\[
\boxed{
\Delta'(0)
\ge
\left(\frac{|K|}{|S|}\right)^{1/n}
\frac{3m r_* M_2(K)}{2n}
\lambda(1-\lambda)(1-c)^2.
}
\tag{15}
\]

In particular the opening is strictly positive whenever `c!=1`, `lambda in (0,1)`, and `W` is strongly convex.

## 6. B20 — why the obvious counterexample algorithm fails

Run 2 found a negative transverse second derivative using an **indefinite** cross-block quadratic perturbation. That suggested a simple algorithm:

1. start at a source equality;
2. move in the negative-Hessian direction;
3. preserve even log-concavity;
4. obtain an actual counterexample for small parameter.

Theorem 2 identifies the precise failure of this algorithm at the natural equality base.

At a uniform measure, preserving log-concavity to first order requires the added potential to be convex. But for every even convex perturbation, the radial functional `F(r)=r Avg_K W(r\cdot)` is convex, and this forces the first variation of the homothetic source defect to be **nonnegative**. Under strong convexity it is bounded away from zero by (15).

Thus the run-2 negative Hessian is not merely missing a technical regularization. There is a genuine sign barrier separating the two desiderata:

- **flat equality base:** exact homothetic DBM equality, but admissible convex potential directions have the correct first-order sign;
- **strongly convex base:** indefinite cross couplings become admissible and can have negative second variation, but the base DBM gap is already positive.

A successful perturbative counterexample would therefore have to do something qualitatively different: for example, couple the body deformation to the measure deformation so that the positive first-order opening is cancelled, or find a non-homothetic equality/near-equality mechanism with a different tangent cone. Simply regularizing the run-2 indefinite direction around Lebesgue equality cannot work.

## 7. Method outcomes

- **B6 DEFORM TO A POINT YOU CAN SOLVE.** Deformed from the exactly solved uniform-on-convex-body ensemble through the source-valid path `1_S e^{-epsilon W}`. **Succeeded:** reduced the first escape from equality to the scalar radial functional `F`.
- **B4 PROVE SOMETHING WEAKER, COMPLETELY.** Proved the full first-order homothetic statement for every dimension, every symmetric convex `S,K`, and every even convex tilt `W`, with the quantitative strong-convexity bound (15). **Succeeded.**
- **B20 FIND WHY THE ALGORITHM FAILS.** Isolated the exact obstruction to converting run 2's negative transverse Hessian into an immediate source counterexample: convexity of `F` enforces the opposite first-order sign at the flat equality manifold. **Succeeded as an obstruction result.**

The next run must use a different numbered triple. Since the frozen metric has now been unchanged twice, one more unchanged run will trigger the section-I stuck protocol. A mathematically honest next target is the joint body/measure tangent problem: allow `K_epsilon,L_epsilon` to vary with the convex tilt and ask whether their first-order geometry can cancel (15) while leaving a negative second-order source defect. If that route does not move the frozen quantity, the next report must be a section-I thinking report rather than another auxiliary lemma.

## 8. Capability / scheduler honesty

Actual runtime model available to this report is GPT-5.6 Sol; the reasoning-effort telemetry is not exposed, so it is recorded as **UNVERIFIED**. The native scheduler surface available to this fleet still exposes title, prompt, schedule, timing mode and enabled state, but no model selector, reasoning-effort selector or guaranteed run duration. Therefore GPT-6/maximum remains prompt-requested only. Changing that requires a platform capability or authorized configuration surface that exposes model/reasoning controls; this repository cannot supply it.

The permission story for P26 remains context-dependent: one recorded native context returned `You cannot modify this task`, while a later authorized context successfully updated P26. The legitimate workaround is to use the authorized account/workspace/task context or platform support. Creating a duplicate schedule or editing repository text is not a scheduler repair. This run did not modify any schedule.

## 9. ledger_delta

```yaml
track: HARD7-01
source: even-log-concave dimensional Brunn-Minkowski conjecture
claim: operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md
metric: maximum low-dimensional block count B covered at source exponent for all common block-product instances
metric_before: infinity
metric_after: infinity
status_before: PARTIAL
status_after: PARTIAL
unchanged_count_before: 1
unchanged_count_after: 2
methods_this_run: [4, 6, 20]
main_result: convex-tilt barrier at homothetic Lebesgue equality, with quantitative strong-convexity lower bound on the first variation
remaining_obligation: full irreducible DBM; next attack is joint body/measure tangent cancellation, otherwise section-I stuck protocol
novelty: UNVERIFIED; elementary mechanism may be folklore
closure_audits: 0
```
