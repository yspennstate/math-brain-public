Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT in the alpha=1/2 headline metric); genuine theorem progress: general interior free-alpha=1 branch `0/1 -> 1/1` internally, completing the free-alpha=1 skew-parameter classification when combined with C017. Section-B moves: #3, #20, #21, explicitly a second-cycle triple because all 30 moves were exhausted earlier; the immediately preceding triple was #6/#18/#29.**

Problem/source: Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY already at alpha=1/2; repository status remains PARTIAL / AUDIT_PENDING. New this run: PROVED INTERNALLY / AUDIT PENDING source-scope extension R19-I0084-C018. It proves exact-third-moment eventual unimodality for every two-sided free 1-stable kernel under the frozen arXiv ordinary-convolution convention. Together with C017, which gives all-moment all-time counterexamples at the two exceptional endpoints, this yields a complete free-alpha=1 skew-parameter classification.**

## 1. Continuity and controlling instruction

I resumed from the current `master` and from the actual latest R19 report

`runs/R19/2026-09-19_23-48-11_UTC__i0084-alpha1-exceptional-endpoints_c017_m6l18p29.md`

at creation commit `b389a4ac7304eec6af161e2c7b1423563b43d7b3`. I did not restart the problem or replace the frozen source convention.

The pre-write repository head was `027be4259febaf0d9a5211f8c6a7e67e0f5da22c`. The exact comparison from the C017 commit was ahead-only and showed no later R19 report before this write. I read the current campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the current 20 September progress-first owner directive and deployment receipt, the relevant intake/history searches, the latest R19 package, and targeted P26/I0084 audit evidence. The append-only historical intake corpus was not pretended to be manually reread byte for byte; the I0084 source identity/scope was checked directly against the current primary source and repository history.

The 20 September owner directive supersedes the repeated targetless admission/audit-wait loops and requires most useful effort to go to mathematics. The exact next structural hole named by C017 was the generic interior free 1-stable family. This run attacks that hole directly.

## 2. Frozen source convention, rechecked from the PDF

The current arXiv v2 PDF, page 18, Conjecture 5.5, says:

- `S_t` may be the law of a **classical or free alpha-stable process**;
- `alpha in (0,2)`;
- the input law satisfies
  \[
  \int_{\mathbb R}|x|^{2+\alpha}\,d\mu(x)<\infty;
  \]
- the conclusion is eventual unimodality of
  \[
  \boxed{\mu * S_t}.
  \]

The asterisk is ordinary **classical convolution**, including when `S_t` is the law of a free stable process. Nothing below replaces it by `boxplus`.

At `alpha=1` the exact source moment is the third absolute moment.

## 3. The obstruction left by C017

C017 handled the exceptional free 1-stable endpoints `rho=0,1`: up to affine equivalence they are the exceptional law `T` and its reflection, and one side has literal half-line support. C010 therefore gives an initial law with every polynomial moment for which ordinary convolution is nonunimodal for every time.

C017 deliberately stopped at the interior `0<rho<1`. The tempting route was Hasebe--Simon--Wang's bell-shape theorem. But their Theorem 4(d) proves bell shape for the two-sided 1-stable law `C_{a,b}` only when `b=0` or `a/b in pi Z`; Remark 8(b) explicitly says that when `a/b notin pi Z` their total-positivity argument fails and they do not know whether the density is always bell-shaped.

That makes the old route genuinely insufficient for the generic interior family. The new route is to avoid full bell shape completely and verify the weaker C008 hypotheses directly from Bercovici--Pata--Biane's explicit `alpha=1` density parametrization.

## 4. Recalled engine C008

The previously proved R19-I0084-C008 theorem says the following. Let `k` be a probability density, translated so that its unique mode is zero. Suppose:

1. `k in C^2(R)` and `k',k''` are bounded;
2. `k'(x)>0` for `x<0` and `k'(x)<0` for `x>0`;
3. for some `epsilon,c0>0`, `k''(x)<=-c0` on `|x|<=2epsilon`;
4. for some `R,c_+,c_->0`,
   \[
   -k'(x)\ge c_+x^{-p}\quad(x\ge R),\qquad
   k'(x)\ge c_-|x|^{-p}\quad(x\le-R).
   \]

Then for the dilation `k_s(x)=s^{-1}k(x/s)`, every probability measure `mu` with finite `p`th absolute moment has `mu*k_s` unimodal for all sufficiently large `s`. The proof is the written Markov-tail / outer derivative-sign / central-concavity argument in the R19 history; no new numerical assumption is added here.

For `alpha=1`, the source exponent is `p=3`. Thus it is enough to verify C008 for every interior free 1-stable density with derivative tails of order `|x|^{-3}`.

# 5. R19-I0084-C018 — complete interior free-alpha=1 theorem

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

Let `0<rho<1`, and let `X_rho` be the canonical free 1-stable law of Bercovici--Pata--Biane / Hasebe--Simon--Wang, normalized by

\[
\phi_\rho(z)=-2\rho i-c_\rho\log z,
\qquad
c_\rho:=\frac{2}{\pi}(1-2\rho).
\]

Let `X_{rho,t}` be the law at time `t` in the corresponding free stable process. Then for every probability measure `mu` satisfying the exact source assumption

\[
M_3:=\int_{\mathbb R}|y|^3\,d\mu(y)<\infty,
\]

the **ordinary classical convolution**

\[
\boxed{\mu*X_{\rho,t}}
\]

is unimodal for all sufficiently large `t`.

The same conclusion holds for every positive affine equivalent two-sided free 1-stable law. Quantitatively, C008 gives a kernel-dependent sufficient scale of order `M_3^{1/3}`.

Combining this with C017 gives the full canonical free-alpha=1 classification:

- `0<rho<1`: the exact finite third moment suffices for eventual unimodality;
- `rho=0,1`: there exists one source-admissible initial law with all polynomial moments for which ordinary convolution is nonunimodal for every `t>0`.

No free convolution appears in the conclusion.

## 5.1 Bercovici--Pata parametrization

Proposition A1.3 of Bercovici--Pata--Biane gives, for `0<rho<1`, a positive analytic density on `R`. Put

\[
c=c_\rho=\frac{2}{\pi}(1-2\rho),
\qquad
A(\theta)=2\rho+c\theta,
\qquad 0<\theta<\pi.
\]

Then

\[
k_\rho(x(\theta))=q(\theta)
:=\frac{\sin^2\theta}{\pi A(\theta)}, \tag{5.1}
\]

where

\[
x(\theta)
=A(\theta)\cot\theta
-c\log\!\left(\frac{\sin\theta}{A(\theta)}\right). \tag{5.2}
\]

The proposition states that for every real `x` there is a unique `theta in (0,pi)` solving this relation.

Differentiating (5.2) gives the useful exact identity

\[
x'(\theta)
=-A(\theta)\csc^2\theta+\frac{c^2}{A(\theta)}
=\frac{c^2\sin^2\theta-A(\theta)^2}
       {A(\theta)\sin^2\theta}. \tag{5.3}
\]

This derivative is **strictly negative everywhere**. Indeed, if `c>=0`, then

\[
A(\theta)-c\sin\theta
=2\rho+c(\theta-\sin\theta)>0, \tag{5.4}
\]

so `A>|c| sin(theta)` and the numerator in (5.3) is negative. If `c<0`, use the exact reflection identity

\[
A_\rho(\theta)=A_{1-\rho}(\pi-\theta),
\qquad c_{1-\rho}=-c_\rho, \tag{5.5}
\]

and the same argument. For `c=0` the sign is immediate. Hence `theta -> x(theta)` is a decreasing analytic diffeomorphism from `(0,pi)` onto `R`.

This matters because it lets us read the complete derivative-sign geometry of the density from the much simpler function `q(theta)`.

## 5.2 Unique mode and strict local concavity without bell shape

From (5.1),

\[
L(\theta):=\frac{q'(\theta)}{q(\theta)}
=2\cot\theta-\frac{c}{A(\theta)}. \tag{5.6}
\]

First assume `0<rho<1/2`, so `c>0`. There is no zero of `L` on `[pi/2,pi)`. On `(0,pi/2)`, `L(theta)=0` is equivalent to

\[
D(\theta):=c\tan\theta-2A(\theta)=0. \tag{5.7}
\]

Now

\[
D'(\theta)=c(\tan^2\theta-1). \tag{5.8}
\]

Thus `D` decreases on `(0,pi/4)` and increases on `(pi/4,pi/2)`. Moreover

\[
D(\pi/3)
=c\left(\sqrt3-\frac{2\pi}{3}\right)-4\rho<0, \tag{5.9}
\]

while `D(theta)->+infinity` as `theta↑pi/2`. Hence there is exactly one root

\[
\theta_m\in(\pi/3,\pi/2). \tag{5.10}
\]

Because `A tan(theta)>0`, the sign of `L` is the opposite of the sign of `D`; therefore `q` increases before `theta_m` and decreases after it. The case `rho>1/2` follows from (5.5), giving

\[
\theta_m\in(\pi/2,2\pi/3), \tag{5.11}
\]

and for `rho=1/2` one has the Cauchy case `theta_m=pi/2` directly.

Since `x'(theta)<0`, this translates into the required strict density derivative signs: after translating the unique mode `m=x(theta_m)` to zero,

\[
k_\rho'(x)>0\quad(x<0),
\qquad
k_\rho'(x)<0\quad(x>0). \tag{5.12}
\]

More importantly, we get strict curvature at the mode. Differentiating (5.6),

\[
L'(\theta)
=-2\csc^2\theta+\frac{c^2}{A(\theta)^2}. \tag{5.13}
\]

At the mode, `c/A=2cot(theta_m)`, so

\[
L'(\theta_m)
=2(\cot^2\theta_m-1)<0, \tag{5.14}
\]

because `theta_m in (pi/3,2pi/3)`. Hence

\[
q''(\theta_m)=q(\theta_m)L'(\theta_m)<0. \tag{5.15}
\]

Also (5.3) gives `x'(theta_m)<0`. Since `q'(theta_m)=0`, the chain rule yields

\[
k_\rho''(m)
=\frac{q''(\theta_m)}{x'(\theta_m)^2}<0. \tag{5.16}
\]

Analyticity therefore gives an `epsilon,c0>0` for which C008's local strong-concavity hypothesis holds.

This is the crucial bypass of the Hasebe--Simon--Wang generic bell-shape gap: C008 needs only one strict mode plus local negative curvature, and both follow directly from the old explicit parametrization.

## 5.3 Exact derivative-tail exponent `p=3`

We now derive the tails directly from the same parametrization, rather than differentiating a bare density asymptotic.

As `theta↓0`, set `a=2rho>0`. Then

\[
A(\theta)=a+c\theta,
\]

and elementary expansions in (5.1)-(5.3) give

\[
x(\theta)=\frac{a}{\theta}-c\log\theta+O(1),
\qquad
x'(\theta)=-\frac{a}{\theta^2}+O(\theta^{-1}), \tag{5.17}
\]

\[
q(\theta)=\frac{\theta^2}{\pi a}(1+O(\theta)),
\qquad
q'(\theta)=\frac{2\theta}{\pi a}+O(\theta^2). \tag{5.18}
\]

Therefore `x~a/theta` and

\[
\begin{aligned}
k_\rho'(x)
&=\frac{q'(\theta)}{x'(\theta)}\\
&=-\frac{2\theta^3}{\pi a^2}(1+o(1))\\
&\sim -\frac{2a}{\pi}x^{-3}
=-\frac{4\rho}{\pi}x^{-3},
\qquad x\to+\infty. \tag{5.19}
\end{aligned}
\]

At the other end put `eta=pi-theta` and `b=2(1-rho)>0`. The reflected expansion gives

\[
x\sim-\frac{b}{\eta},
\qquad
k_\rho'(x)
\sim \frac{2b}{\pi}|x|^{-3}
=\frac{4(1-\rho)}{\pi}|x|^{-3},
\qquad x\to-\infty. \tag{5.20}
\]

Both constants are strictly positive exactly for the interior range `0<rho<1`. Consequently there are `R,c_+,c_->0` with

\[
-k_\rho'(x)\ge c_+x^{-3}\quad(x\ge R),
\qquad
k_\rho'(x)\ge c_-|x|^{-3}\quad(x\le-R). \tag{5.21}
\]

The same parametrization differentiated once more gives

\[
k_\rho''(x)=O(|x|^{-4}) \tag{5.22}
\]

at both ends (indeed the leading constants are `12rho/pi` on the right and `12(1-rho)/pi` on the left). On compact intervals the density is analytic. Thus `k'` and `k''` are globally bounded. All C008 assumptions hold with the **exact source exponent `p=3`**.

It follows immediately that for every `mu` with finite third absolute moment,

\[
\mu * D_sX_\rho
\]

is unimodal for all sufficiently large dilation scales `s`.

## 5.4 Converting spatial scale to the free stable process time

For the canonical law,

\[
\phi_\rho(z)=-2\rho i-c\log z. \tag{5.23}
\]

The time-`t` free additive convolution semigroup has

\[
\phi_{\rho,t}(z)=t\phi_\rho(z). \tag{5.24}
\]

For an affine transform, the Voiculescu transform obeys

\[
\phi_{aX+b}(z)=b+a\phi_X(z/a),\qquad a>0. \tag{5.25}
\]

Taking `a=t` and `b=-ct log t`,

\[
\begin{aligned}
\phi_{tX_\rho-ct\log t}(z)
&=-ct\log t+t\left[-2\rho i-c\log(z/t)\right]\\
&=-2\rho it-ct\log z
=t\phi_\rho(z). \tag{5.26}
\end{aligned}
\]

Therefore

\[
\boxed{X_{\rho,t}\ \stackrel d=\ tX_\rho-ct\log t.} \tag{5.27}
\]

The logarithmic term is only a translation. Translation does not affect unimodality of an ordinary convolution density. Hence C008 applies with spatial scale `s=t` and proves

\[
\boxed{\mu*X_{\rho,t}\text{ is unimodal for all sufficiently large }t,\quad0<\rho<1,} \tag{5.28}
\]

under exactly `int |x|^3 dmu<infinity`.

Hasebe--Simon--Wang state that every free 1-stable distribution is equivalent, by positive scale and translation, to a unique canonical `rho` law. Such affine changes only modify the fixed C008 constants and add translations, so (5.28) covers every two-sided free 1-stable kernel.

## 5.5 Full free-alpha=1 parameter classification

C017 already proves that the canonical endpoints `rho=0,1` are affine transforms of the exceptional law `T` and its reflection, and that there are all-polynomial-moment initial laws whose ordinary convolutions are nonunimodal at every time.

C018 proves the exact-moment positive theorem for every `0<rho<1`.

Thus the free-alpha=1 parameter line is now completely classified under the frozen arXiv convention:

\[
\boxed{
\begin{array}{c|c}
\text{free 1-stable parameter} & \text{ordinary }\mu*S_t\\ \hline
0<\rho<1 & \text{eventually unimodal for every }\mu\text{ with finite third moment}\\
\rho=0,1 & \text{fails for every }t>0\text{ for a fixed all-moment }\mu
\end{array}}
\tag{5.29}
\]

The fixed alpha=1/2 metric remains `2/2`; this is genuine structural progress beyond that saturated metric, not a denominator change.

## 6. The three new-method attacks and what happened

### #3 — PROVE SOMETHING STRONGER

Instead of merely adding another arithmetic subfamily of `C_{a,b}`, I targeted the whole two-sided free-alpha=1 parameter interval. The explicit parameterization is strong enough to verify C008 directly, so the result is the complete interior theorem rather than another restricted case.

**Outcome: success.** Combined with C017, the free-alpha=1 skew-parameter classification is complete.

### #20 — FIND WHY THE ALGORITHM FAILS

The obvious inherited algorithm was: use Hasebe--Simon--Wang bell shape, infer strict curvature, apply C008. Their Remark 8(b) identifies the exact failure: the total-positivity sign-change criterion used for `a/b in pi Z` breaks for generic ratios, and the authors explicitly leave generic bell shape unclear.

The key observation is that this failure is stronger than what C008 actually needs. Full bell shape controls every derivative; C008 only needs first-derivative sign, local second-derivative negativity, and two tail derivative bounds.

**Outcome: success as obstruction diagnosis; it directly suggested the weaker sufficient target.**

### #21 — ASK WHO ELSE HAS THIS SHAPE

Bercovici--Pata--Biane's 1999 appendix gives exactly the missing machinery: an implicit one-parameter formula for the free 1-stable density and its `x^-2` density tails. Rewriting the parametrization in the variables `(A,c,theta)` exposes an elementary derivative identity and makes the `x^-3` derivative tails transparent.

**Outcome: success.** This older representation bypasses the 2020 generic bell-shape gap entirely.

No finite claim was introduced, so no exact-arithmetic checker was manufactured. The theorem-sized analytic proof is written above.

## 7. Prior-art and current-status search — 2026-09-20 UTC

Fresh bounded searches included:

- exact `Hasebe Ueda Conjecture 5.5 stable unimodality`;
- `free 1-stable finite third moment convolution unimodal`;
- `eventual unimodality free stable convolution measure`;
- `large time unimodality free stable third moment`;
- Hasebe--Simon--Wang generic `C_{a,b}` bell shape / `a/b in pi Z`;
- Bercovici--Pata free 1-stable density and tail asymptotics;
- later Hasebe/Ueda work through the current search index.

Primary sources recovered and used:

1. Hasebe--Ueda, arXiv:1710.08240v2, page 18, Conjecture 5.5.
2. H. Bercovici, V. Pata, with Appendix by P. Biane, *Stable laws and domains of attraction in free probability theory*, Annals of Mathematics 149 (1999), Appendix Propositions A1.3, A2.1, A2.2.
3. T. Hasebe, T. Simon, M. Wang, *Some properties of the free stable distributions*, Ann. Inst. H. Poincare Probab. Statist. 56 (2020), especially the alpha=1 parametrization discussion, Theorem 4(d), and Remark 8(b).

The search found no later primary paper explicitly resolving the exact frozen arXiv-v2 ordinary-`*` Conjecture 5.5, and no paper located in this bounded search stated C018's exact-third-moment generic interior free-alpha=1 consequence. This is **bounded negative evidence only, not a novelty certificate**. A complete citation graph was not available through the search interface.

Known ingredients are not claimed as new: Bercovici--Pata--Biane already prove free stable density unimodality and the density-tail asymptotics; Hasebe--Simon--Wang supply the later alpha=1 parameter interpretation and document the generic bell-shape gap. The candidate contribution here is the C008 application after the direct curvature and derivative-tail verification, yielding eventual ordinary-convolution unimodality under the exact third moment for the whole interior free 1-stable family.

## 8. Audit / closure state

The fixed source statement remains mathematically refuted already at alpha=1/2, but protocol closure is not upgraded in this run.

Targeted repository searches still recover only the narrower or differently scoped audit records, including:

- `R18-I0084-C001=PASS` for the classical positive-half-stable finite/symbolic core;
- `R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF` for the **published ALEA free-boxplus scope**, not the frozen ordinary-`*` branch;
- `R18-AUDIT-R19-I0084-C010-ABSTRACT-004=PASS_FULL_MATHEMATICAL_PROOF` for C010;
- the historical P26 I0084 PASS likewise scope-gated to the ALEA/free-`boxplus` package.

I did not locate either required version-matching full-package audit:

1. a P26 end-to-end PASS for the frozen arXiv ordinary-`*` I0084 package;
2. a distinct OTHER-track end-to-end PASS for that same frozen package.

Therefore the version-matching audit gate remains `0/2`. C018 itself is also audit pending.

## 9. What remains mathematically useful

The strongest immediate source-adjacent extension is now the **classical** alpha=1 interior classification under the same exact third moment. Classical stable densities are known to be bell-shaped, so the remaining work is mainly to put the alpha=1 two-sided derivative-tail constants and logarithmically centered semigroup normalization into the exact C008 form without silently changing skewness conventions.

Beyond alpha=1, C013 still gives only a partial free interior theorem away from alpha=1/2 because the available shape input used there was restricted. A second strong route is therefore to ask whether the Bercovici--Pata implicit parametrizations for general alpha can verify C008's much weaker curvature/sign hypotheses directly, just as C018 does at alpha=1, bypassing full bell shape entirely.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R19
  source: "Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / I0084"
  frozen_convolution: "ordinary classical mu * S_t in both classical-law and free-stable-law branches"
  fixed_metric: "number of complete alpha=1/2 classical-stable/free-stable source cases disposed of with full input class and source skewness conventions"
  metric_before: "2/2"
  metric_after: "2/2"
  metric_movement: "NO MOVEMENT"
  substantive_obligation_metric: "generic interior free-alpha=1 exact-third-moment branch"
  substantive_before: "0/1"
  substantive_after: "1/1"
  substantive_progress: true
  new_claim: "R19-I0084-C018"
  new_claim_status: "PROVED INTERNALLY / AUDIT PENDING / source-scope extension"
  source_status: "REFUTED mathematically already at alpha=1/2"
  repository_status: "PARTIAL / AUDIT_PENDING"
  unchanged_count: "UNKNOWN as a headline-stagnation counter; not synthetically reconstructed after progress-first supersession"
  substantive_stagnation_this_run: 0
  tried_moves: [3, 20, 21]
  moves_note: "second-cycle reuses because all 30 Section-B moves were exhausted earlier; preceding triple [6,18,29]"
  evidence:
    - "runs/R19/2026-09-19_23-48-11_UTC__i0084-alpha1-exceptional-endpoints_c017_m6l18p29.md @ b389a4ac7304eec6af161e2c7b1423563b43d7b3"
    - "runs/R19/2026-09-16_17-36-54_UTC__i0084-skewness-classification.md (C008 engine)"
    - "Hasebe-Ueda arXiv:1710.08240v2 page 18 / Conjecture 5.5"
    - "Bercovici-Pata-Biane 1999, Appendix A1.3/A2.1/A2.2"
    - "Hasebe-Simon-Wang 2020, alpha=1 discussion / Theorem 4(d) / Remark 8(b)"
  audits:
    frozen_arxiv_ordinary_star_p26: "PENDING_NOT_LOCATED"
    frozen_arxiv_ordinary_star_other: "PENDING_NOT_LOCATED"
    frozen_package_gate: "0/2"
    C018_independent_audit: "PENDING"
  remaining_obligation:
    - "protocol closure: P26 frozen-arXiv ordinary-* full-package PASS"
    - "protocol closure: distinct OTHER-track frozen-arXiv ordinary-* full-package PASS"
    - "mathematical extension: classical alpha=1 interior in exact source skewness normalization"
    - "mathematical extension: try direct parametrization/C008 beyond the previously covered free-alpha ranges"
```

## 11. Model / scheduler control

Actual model available to this run: **GPT-5.6 Sol**. Applied reasoning level has no authenticated runtime receipt, so it is reported as **UNVERIFIED**. GPT-6 / maximum was requested in prompt text but is not claimed.

The current deployment receipt still records that the exposed scheduler control surface has no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/effort attestation, and no guaranteed full-hour execution setting. Making GPT-6/maximum enforceable requires a scheduler/product/API surface that persists and attests those routing fields.

The historical P26 `You cannot modify this task` event is preserved as an authorization-context issue; later authorized contexts did update P26 successfully. The lawful workaround is the owning/authorized context, supported ownership/permission repair or platform support, never a bypass. No scheduler change was attempted in this research run.
