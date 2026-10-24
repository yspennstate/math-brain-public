Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run is not verified as GPT-6 at maximum. **No movement in the frozen metric:** `B=infinity -> B=infinity` (third consecutive unchanged run after run 1). Methods tried: **B1, B3, B26**.

# HARD7-01 run 4 — joint body/measure tangent rigidity at homothetic equality

Status: **PARTIAL** for the full even-log-concave dimensional Brunn--Minkowski conjecture. This run does not prove or refute the source conjecture. It closes the specific escape route left open by run 3: allowing the bodies to move together with an admissible convex tilt cannot cancel the positive first-order opening at a homothetic Lebesgue equality. The cancellation of the body-shape terms is exact by mixed-volume homogeneity. Moreover, equality in the remaining potential term is rigid: unless the convex potential is constant on the whole swept homothetic region, the joint first variation is strictly positive. The exceptional flat-core case was then attacked directly; the simplest finite-amplitude radial boundary-layer deformation also moves in the correct direction.

## 1. Continuity, ownership, repository state, and fresh source check

The canonical claim remains

`operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md`,

owned exclusively by HARD7-01, with source target

\[
\mu((1-\lambda)K+\lambda L)^{1/n}
\ge (1-\lambda)\mu(K)^{1/n}+\lambda\mu(L)^{1/n}
\tag{DBM}
\]

for every even log-concave probability measure on `R^n`, all nonempty centrally symmetric convex sets `K,L`, and every `lambda in [0,1]`.

At run start I reread the controlling HARD7 and new-methods policies, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical claim, all three preceding HARD7-01 reports, and the newest neighboring log-concave/KLS report recovered by repository search. Repository-wide searches for `dimensional Brunn-Minkowski`, `Gardner-Zvavitch`, and `log-concave` continue to recover HARD7-01 as the unique owner of this exact source target; no competing equivalent claim was found. The large intake JSONL corpus is not returned by the connector as one untruncated object, so the intake check was performed by repository-wide exact-name/alias search rather than pretending to have semantically reread every row.

Fresh bounded literature searches on **2026-09-19 UTC** found no full resolution of the exact source scope. In particular:

- Kai-Wen Yang, *A uniform bound in the dimensional Brunn--Minkowski inequality for even log-concave measures*, arXiv:2607.10104 (11 July 2026), proves a uniform exponent `p_n >= c/(n^2 log n)` for the same even-log-concave/symmetric-set class, not `p_n=1/n` in full generality.
- Alexandros Eskenazis, Apostolos Giannopoulos, Natalia Tziotziou, *Functional perimeter and the dimensional Brunn-Minkowski inequality for log-concave measures*, arXiv:2605.02747 (4 May 2026), proves another quantitative partial exponent.
- Sotiris Armeniakos and Jacopo Ulivelli, *A strengthening of the dimensional Brunn-Minkowski conjecture implies the (B)-Conjecture*, arXiv:2602.23350 (26 February 2026), treats a stronger condition and special classes, not the full target.

A separate bounded search for `homothetic`, `first variation`, `mixed volumes`, and `dimensional Brunn-Minkowski` did not locate the exact joint tangent-rigidity statement proved below. This is **not** a novelty certificate. The mixed-volume cancellation is classical technology and the resulting observation may be folklore; novelty remains **UNVERIFIED**.

## 2. Frozen metric and streak

The admission metric remains

`B = largest low-dimensional block count for which (DBM) is proved at the source exponent 1/N for every common block-product instance built from 1D/2D factors`.

Run 1 proved all finite block counts, recorded as `B=infinity`. Runs 2 and 3 were unchanged. This run is also

\[
\boxed{B=\infty\ \longrightarrow\ B=\infty.}
\]

Hence this is the **third consecutive unchanged run**. Under section I, the **next** HARD7-01 invocation must be a thinking/stuck run with no new theorem claim, containing the required five-part obstruction report and exactly one recovery choice. This report itself is still the third substantive run in the streak, so it completes the route promised by run 3 before that protocol fires.

No checker was manufactured in this run: the claims below are analytic, not finite exhaustive claims. Their proofs are written on the page.

## 3. B1 — change category: from moving convex bodies to mixed-volume first variation

Run 3 left one specific possible escape from its convex-tilt barrier: perhaps a convex potential tilt opens a homothetic equality positively, but a simultaneous deformation of `K` and `L` could contribute a negative first-order geometric term and cancel it. The correct category for that question is mixed-volume calculus.

Let

\[
a=1-\lambda,\qquad b=\lambda,\qquad s=a+bc,
\]

with `lambda in (0,1)` and `c>0`. Let `S,K,A,B` be centrally symmetric convex bodies in `R^n`, all with nonempty interior, and assume that for all sufficiently small `t>=0` the bodies below lie in `S`. Define the Minkowski-direction body paths

\[
K_t=K+tA,\qquad L_t=cK+tB,
\]

and therefore

\[
M_t=aK_t+bL_t=sK+t(aA+bB).
\tag{1}
\]

Let `W:S->R` be even, convex and continuous, and tilt the uniform log-concave measure on `S` by

\[
d\mu_t(x)=Z_t^{-1}\mathbf 1_S(x)e^{-tW(x)}\,dx.
\tag{2}
\]

The source defect is

\[
\Delta(t)=\mu_t(M_t)^{1/n}-a\mu_t(K_t)^{1/n}-b\mu_t(L_t)^{1/n}.
\tag{3}
\]

At `t=0`, the measure is uniform on `S` and `(K,cK)` is a Brunn--Minkowski equality pair, so `Delta(0)=0`.

As in the previous reports, the common normalizer is irrelevant for the sign. Write

\[
J_C(t)=\int_{C_t}e^{-tW(x)}\,dx
\]

for the corresponding moving set, and

\[
D(t)=J_M(t)^{1/n}-aJ_K(t)^{1/n}-bJ_L(t)^{1/n},
\qquad
\Delta(t)=Z_t^{-1/n}D(t).
\tag{4}
\]

Because `D(0)=0`,

\[
\Delta'_+(0)=|S|^{-1/n}D'_+(0).
\tag{5}
\]

For Minkowski addition the classical first variation of volume is

\[
\frac d{dt}|C+tE|\Big|_{t=0^+}=nV(C[n-1],E).
\tag{6}
\]

Also, uniformly on the bounded support,

\[
e^{-tW}=1-tW+O(t^2).
\]

The interaction between the `O(t)` boundary layer and the `O(t)` change in density is `O(t^2)`. Hence

\[
\begin{aligned}
J_K'(0)&=nV(K[n-1],A)-\int_KW,\\
J_L'(0)&=nc^{n-1}V(K[n-1],B)-\int_{cK}W,\\
J_M'(0)&=ns^{n-1}\big(aV(K[n-1],A)+bV(K[n-1],B)\big)-\int_{sK}W.
\end{aligned}
\tag{7}
\]

Now differentiate the `1/n` powers. The **entire shape contribution cancels exactly**. Indeed the shape term from `M_t` is

\[
(s^n|K|)^{1/n-1}s^{n-1}
\big(aV(K[n-1],A)+bV(K[n-1],B)\big)
=
|K|^{1/n-1}\big(aV_A+bV_B\big),
\]

where `V_A=V(K[n-1],A)` and `V_B=V(K[n-1],B)`. The two endpoint shape terms are exactly

\[
a|K|^{1/n-1}V_A+b(c^n|K|)^{1/n-1}c^{n-1}V_B
=
|K|^{1/n-1}(aV_A+bV_B).
\]

Thus they subtract to zero.

Define exactly as in run 3

\[
F(r)=\frac r{|K|}\int_K W(ry)\,dy.
\tag{8}
\]

The surviving derivative is therefore

\[
\boxed{
D'_+(0)=\frac{|K|^{1/n}}{n}
\left[aF(1)+bF(c)-F(s)\right].
}
\tag{9}
\]

This is the key new identity. **To first order, arbitrary Minkowski-direction motion of both bodies is invisible at a homothetic Lebesgue equality.** There is nothing available in the body directions to cancel the convex-tilt opening from run 3.

### Support-function extension

The cancellation is not peculiar to paths of the form `K+tA`. Suppose more generally that a two-sided or one-sided convex-body path is differentiable in support functions at zero,

\[
h_{K_t}=h_K+t u+o(t),\qquad
h_{L_t}=c h_K+t v+o(t),
\tag{10}
\]

and the standard Alexandrov first-variation formula applies. Since

\[
dS_{rK}=r^{n-1}dS_K,
\]

the first volume derivatives are linear in `u,v` with the same scaling factors as in (7). The support function of `aK_t+bL_t` has derivative `au+bv`, so the same root-volume scaling cancels the entire body contribution. Consequently (9) remains valid under these standard first-variation hypotheses. The source-relevant conclusion is therefore a tangent-cone statement, not merely a Minkowski-sum curiosity.

## 4. B3 — prove something stronger: universal joint tangent rigidity

Run 3 proved `F` is convex when `W` is even and convex. Here the equality case is needed, because a potential with zero first-order opening is the only way a joint body/measure perturbation can still hope to reach a negative second-order term.

Subtract the irrelevant constant `W(0)` and, for fixed `y in K`, set

\[
\phi_y(r)=W(ry)-W(0),\qquad r\ge0.
\tag{11}
\]

Evenness and convexity of `W` imply that `phi_y` is convex, nonnegative, nondecreasing on `[0,infinity)`, and `phi_y(0)=0`. Put

\[
h_y(r)=r\phi_y(r).
\tag{12}
\]

Because `phi_y` and its one-sided slope are both nonnegative and nondecreasing, the one-sided slope of `h_y`,

\[
h'_{y,+}(r)=\phi_y(r)+r\phi'_{y,+}(r),
\]

is nondecreasing. Hence `h_y` is convex. Averaging (12) over `K` proves convexity of `F` after removal of the linear `rW(0)` term. Since `s=a+bc`, (9) yields

\[
D'_+(0)\ge0.
\tag{13}
\]

The important point is that equality is rigid.

### Lemma 1 — equality in the radial Jensen gap

Assume `c!=1` and `lambda in (0,1)`. Then

\[
aF(1)+bF(c)-F(s)=0
\tag{14}
\]

if and only if `W` is constant on

\[
r_{\max}K,\qquad r_{\max}=\max\{1,c\}.
\tag{15}
\]

#### Proof

The Jensen gap for each `h_y` is nonnegative. If the averaged gap (14) is zero, then the pointwise gap is zero for almost every `y in K`. Equality for a convex function at the strict convex combination `s=a*1+b*c` forces `h_y` to be affine on the interval with endpoints `1` and `c`.

On that interval write

\[
h_y(r)=Ar+B.
\]

Then

\[
\phi_y(r)=A+\frac Br.
\tag{16}
\]

there. Since `phi_y` is nondecreasing, (16) forces `B<=0`; since `phi_y` is convex, it forces `B>=0`. Thus `B=0`, so `phi_y` is constant on the interval. A convex nondecreasing function with `phi_y(0)=0` that is constant on a positive interval away from zero must in fact equal zero from `0` through the right endpoint of that interval: the secant slope on the constant interval is zero, convexity makes all earlier secant slopes at most zero, while nonnegativity makes them at least zero. Hence

\[
W(ry)=W(0)\qquad
(0\le r\le r_{\max})
\]

for almost every `y in K`. Convex functions are continuous on the interior of their domain, and `K` has interior, so this extends to every point of `r_max K`. The converse is immediate. `square`

Combining (5), (9), (13), and Lemma 1 gives the run's main theorem.

> **Theorem 2 — joint body/measure tangent rigidity at homothetic equality.**
> Let `S,K,A,B` be centrally symmetric convex bodies with nonempty interior, let `c>0`, `lambda in (0,1)`, and let `W` be even convex on `S`. For the source-valid paths (1)--(3),
> \[
> \boxed{
> \Delta'_+(0)=
> \left(\frac{|K|}{|S|}\right)^{1/n}
> \frac{aF(1)+bF(c)-F(a+bc)}{n}\ge0.
> }
> \tag{17}
> \]
> The expression is independent of the first-order body directions `A,B`. If `c!=1`, equality in (17) holds exactly when `W` is constant on `max(1,c)K`. The same conclusion holds for support-function-differentiable body paths under the standard first-variation formula.

Thus the proposed run-3 escape mechanism fails in a stronger form than anticipated: **no first-order deformation of the bodies can pay for the positive opening created by a nontrivial convex tilt.**

If `W` is `m`-strongly convex, the quantitative bound from run 3 survives unchanged under simultaneous body motion. With

\[
r_*=\min\{1,c\},\qquad
M_2(K)=\frac1{|K|}\int_K|y|^2dy,
\]

one has

\[
\Delta'_+(0)
\ge
\left(\frac{|K|}{|S|}\right)^{1/n}
\frac{3m r_*M_2(K)}{2n}
\lambda(1-\lambda)(1-c)^2.
\tag{18}
\]

Equation (18) is not a new independent estimate; the new content is that arbitrary first-order body motion contributes **exactly zero**, so the run-3 lower bound cannot be cancelled geometrically.

## 5. B26 — hunt the sporadic case: can the flat-core equality case escape at finite amplitude?

Lemma 1 leaves one exceptional perturbative possibility: choose a convex potential that is completely flat on the whole base region `r_max K`, so the joint first derivative vanishes, and try to exploit the first place where a moving body exits that flat core.

I attacked the simplest such construction directly rather than adding another formal Hessian lemma.

Assume `c>1` (the other order is obtained by swapping the endpoints). Let `S` contain `(c+eta)K` for some `eta>0`, and let `W` be any even convex function such that

\[
W=0\quad\text{on }cK,
\qquad
W\ge0\quad\text{on }S.
\tag{19}
\]

A canonical example is the convex hinge

\[
W(x)=\big(\|x\|_K-c\big)_+,
\tag{20}
\]

where `||.||_K` is the gauge norm of the symmetric body `K`.

Fix `d>0` and use a single small parameter `t` for both tilt and body motion:

\[
K_t=K,
\qquad
L_t=(c+dt)K,
\qquad
M_t=(s+bdt)K.
\tag{21}
\]

Because `s=a+bc<c`, for all sufficiently small positive `t`,

\[
M_t\subset cK.
\tag{22}
\]

Therefore the unnormalized integrals satisfy **exactly**

\[
J_K(t)=|K|,
\qquad
J_M(t)=|M_t|,
\tag{23}
\]

while from `W>=0`,

\[
J_L(t)=\int_{L_t}e^{-tW}\,dx\le |L_t|.
\tag{24}
\]

Consequently

\[
\begin{aligned}
D(t)
&=J_M(t)^{1/n}-aJ_K(t)^{1/n}-bJ_L(t)^{1/n}\\
&\ge |M_t|^{1/n}-a|K|^{1/n}-b|L_t|^{1/n}\\
&=|K|^{1/n}\big[(s+bdt)-a-b(c+dt)\big]\\
&=0.
\end{aligned}
\tag{25}
\]

If `W>0` on a positive-volume part of the newly exposed shell `L_t\setminus cK`, then (24) is strict and so is (25). If the larger endpoint moves inward instead, all three homothetic bodies remain inside the flat core and the defect stays exactly zero.

Thus the most obvious flat-core boundary-layer construction cannot exploit the equality case left by Theorem 2. It either leaves the source equality unchanged or makes the desired inequality strictly easier. This is a **finite-amplitude statement** for the specified radial/homothetic escape family, not a discrete simulation and not an asymptotic fit.

What remains genuinely open after this test is much narrower: a perturbative counterexample based at a Lebesgue homothetic equality would have to use a flat-core convex potential together with a **nonhomothetic angular boundary deformation** whose higher-order weighted contribution is not reduced to the endpoint suppression argument (25), or abandon exact equality and work from a near-equality configuration.

## 6. What the three methods did

- **B1 CHANGE THE CATEGORY.** Recast simultaneous body deformation through mixed volumes / support-function first variation. **Succeeded:** every first-order body-shape term cancels exactly at a homothetic Lebesgue equality, leaving the scalar potential Jensen gap (9).
- **B3 PROVE SOMETHING STRONGER.** Instead of finding one body deformation that fails to cancel the run-3 barrier, proved that **all** first-order Minkowski directions, and more generally all support-differentiable directions under the standard first-variation formula, fail to cancel it. Equality was characterized exactly by flatness of `W` on `max(1,c)K`. **Succeeded.**
- **B26 HUNT THE SPORADIC CASE.** Attacked the only first-order equality mechanism, a convex potential flat on the swept homothetic region. For the canonical radial/homothetic boundary escape, the full finite-amplitude defect has the correct sign by the exact comparison (25). **Succeeded as an obstruction result.**

These are new routes for this target; none of B1/B3/B26 appeared in runs 1--3.

## 7. Why this matters and what is still missing

The sequence of runs now gives a fairly sharp perturbative map around product/homothetic configurations:

1. Run 1: common low-dimensional Cartesian products tensorize all the way to the source exponent.
2. Run 2: a genuinely cross-block, log-concave-admissible direction can have negative second variation, so naive transverse convexity is false.
3. Run 3: at a flat homothetic equality, every admissible convex potential tilt has nonnegative first variation, quantitatively positive for strongly convex tilts.
4. This run: moving the bodies cannot cancel that first variation; equality forces a flat-core potential, and the simplest finite-amplitude flat-core radial escape also has the correct sign.

The remaining obstruction is therefore not “find another Hessian direction.” A source counterexample or a proof route must address **irreducible nonhomothetic geometry away from the exact Lebesgue equality manifold**, or a genuinely higher-order angular boundary-layer mechanism in the flat-core case. The negative run-2 Hessian and the positive run-3/run-4 tangent barrier are compatible because they live at different base points/tangent cones.

The full source conjecture remains **OPEN** and this track remains **PARTIAL**. No claim here upgrades a restricted theorem to the general even-log-concave case.

## 8. Section-I trigger for the next run

Because the frozen quantity has now been unchanged in runs 2, 3, and 4, HARD7-01 is now **STUCK under the owner's formal rule**. The next invocation must not add another auxiliary lemma. It must write the five-part thinking report:

(a) the exact blocking source-level statement in one displayed formula;
(b) every route tried and the precise failure of each;
(c) the ingredient a successful proof would need that none has;
(d) the simplest still-unproved source-valid special case;
(e) the nearest solved analogue and the ingredient its proof has.

It must then choose exactly one recovery action. A natural candidate to assess there is **prove the simplest unproved special case**: a genuinely nonproduct `n=3` even log-concave class not covered by unconditionality, rotation invariance, or the block-product theorem. But the next run must make that choice only after the mandated comparison; this report does not pre-commit the recovery.

For the next thinking run, the natural unused section-B lenses are **B22 (read the failures), B23 (assume the opposite of the expected answer), and B29 (add the boundary/compactification)**. They are suggestions, not work claimed here.

## 9. Capability / scheduler honesty

Actual runtime model available to this report is **GPT-5.6 Sol**. Reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. This run therefore does **not** claim GPT-6 at maximum.

The native automation schema exposed in this runtime permits title, prompt, schedule, timing mode and enabled state, but has **no model selector, no reasoning-effort selector and no guaranteed execution duration**. GPT-6/maximum can only be requested in prompt text with the present interface. Changing that requires a platform/runtime configuration surface that actually exposes model and reasoning controls; no repository edit can provide it.

The repository records both a historical P26 modification denial (`You cannot modify this task`) in one native context and a later successful update from an authorized context. The legitimate workaround for a denied task is therefore to use the authorized account/workspace/task context or platform support. Creating a duplicate schedule, bypassing ownership, or editing repository text is not a scheduler repair. This run did not modify any schedule.

## 10. ledger_delta

```yaml
track: HARD7-01
canonical_claim: GZ-DIMBM-EVEN-LOGCONCAVE
source_status: OPEN
research_status: PARTIAL
metric: B
before: infinity
after: infinity
movement: no movement
unchanged_streak: 3
section_I_state: STUCK_TRIGGERED_NEXT_RUN_THINKING_ONLY
methods: [B1, B3, B26]
new_result: joint body/measure first-variation cancellation plus rigidity; radial flat-core finite-amplitude escape has correct sign
finite_checker: not_applicable
closure_claimed: false
novelty: UNVERIFIED
next_obligation: mandatory Section-I five-part thinking report and exactly one recovery choice
```
