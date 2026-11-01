Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT in the frozen alpha=1/2 source-case count); genuine theorem progress: the exponent `2+alpha` is now proved internally sharp in power-moment order on every two-sided/interior classical-stable and free-stable-law branch under the frozen ordinary-`*` convention. Section-B moves: #2 ATTACK THE NEGATION FIRST, #24 FIND THE EXTREMAL OBJECT, #30 DO ONE SCALE / ONE DIRECTION AT A TIME. These are second-cycle reuses because all 30 moves were exhausted historically; the immediately preceding C021 triple was #3/#20/#21, so the preceding triple is not repeated.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY already at alpha=1/2 because extremal skewness is allowed; repository status remains PARTIAL / AUDIT_PENDING. New this run: R19-I0084-C022A/C022B are PROVED INTERNALLY / AUDIT PENDING.**

# 1. Continuity and frozen source convention

I resumed from the actual latest R19 report

`runs/R19/2026-09-20_03-50-30_UTC__i0084-classical-bellshape-repair_c021_m3f20x21.md`

at creation commit `3ee66335ae4cea303c9f3a3ca5d3970d03dd48f6`. Repository commit search found no later R19 checkpoint before this write. I also re-read the campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the current progress-first owner directive, the I0084 history, and current neighboring R18/R20 activity. The progress-first directive keeps the 90/10 mathematics-first budget and explicitly permits genuine structural theorem progress while the frozen headline metric is already saturated.

The primary source was checked again directly in arXiv v2. Conjecture 5.5 says that `S_t` may be the law of a **classical or free alpha-stable process**, assumes exactly

\[
\int_{\mathbb R}|x|^{2+\alpha}\,d\mu(x)<\infty,
\]

and concludes eventual unimodality of

\[
\boxed{\mu*S_t}.
\]

Thus `*` below is **ordinary classical convolution even when `S_t` is the law of a free stable process**. I do not replace it by `\boxplus`.

The source itself already contains two sharp-looking special mechanisms: Proposition 5.1 constructs a Cauchy counterexample with every power moment below `3` finite, while Theorem 5.2 proves finite third moment suffices; Proposition 5.4 constructs the positive `alpha=1/2` counterexample with every power moment below `5/2` finite and explicitly notes the `5/2` moment diverges. Those posted/known special cases earn no new credit here. The new target of this run was to determine whether the same critical exponent is genuinely sharp for **every interior skewness and both frozen source branches**.

Inherited supported state:

- C008: abstract critical-tail eventual-unimodality theorem; independently audited as `R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF`.
- C017/C018/C019: the complete `alpha=1` endpoint/interior analysis.
- C020: every interior free-stable-law branch for all `0<alpha<2` satisfies the exact `(2+alpha)`-moment sufficiency theorem under ordinary `*`.
- C021: every interior classical-stable branch for all `0<alpha<2` satisfies the exact `(2+alpha)`-moment sufficiency theorem, with the arbitrary-alpha bell-shape gap repaired using Kwaśnicki.
- C011/C017: extremal skewness admits all-polynomial-moment counterexamples, so the universal source conjecture fails at the boundary.

The remaining natural mathematical question was whether the interior moment exponent `2+alpha` could be lowered. This run answers that in the negative.

# 2. Three new-method moves

## Move #2 — ATTACK THE NEGATION FIRST

Instead of trying to improve C008's sufficient condition, I attacked the negation: assume one wants eventual unimodality from a moment exponent `q<2+alpha`. A counterexample must survive **every scale** while its `q`-moment stays finite. This immediately suggests balancing each remote atom's weight against the critical derivative tail of the kernel.

## Move #24 — FIND THE EXTREMAL OBJECT

If `|k'(x)|` is of order `|x|^{-p}`, the dimensionless quantity controlling a remote atom at distance `A` is `w A^p`. To make the `p`-moment fail while every smaller power moment converges, the extremal sparse choice is

\[
w_n=nA_n^{-p}
\]

on a superexponentially separated sequence `A_n`. The extra factor `n` forces `w_nA_n^p=n -> infinity` while the superexponential spacing makes every `q<p` moment summable and prevents neighboring atoms from masking the derivative sign test.

## Move #30 — DO ONE SCALE, ONE DIRECTION AT A TIME

For each fixed dilation scale `s`, I do not seek one universal spatial witness. I choose a sufficiently remote index `n=n(s)` and compare two points associated with that atom: one fixed kernel-scale displacement from the atom, where that atom forces a negative derivative, and the midpoint back toward the origin, where the mass at zero forces a positive derivative. The resulting `-` then `+` derivative pattern is incompatible with unimodality. Since `n` may depend on `s`, this proves failure at **every** scale.

# 3. R19-I0084-C022A — sharpness theorem for critical derivative tails

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

Let `p>0`. Let `k` be a `C^1` probability density on `R`, with bounded derivative, translated so its unique mode is at `0`. Assume

\[
k'(x)>0\quad(x<0),\qquad k'(x)<0\quad(x>0). \tag{C022.1}
\]

Assume also that there are positive constants `R,c_-,C_-,c_+,C_+` such that for every `u>=R`,

\[
c_-u^{-p}\le k'(-u)\le C_-u^{-p}, \tag{C022.2}
\]

and

\[
c_+u^{-p}\le -k'(u)\le C_+u^{-p}. \tag{C022.3}
\]

For `s>0`, write

\[
k_s(x)=s^{-1}k(x/s).
\]

Then there exists a single probability measure `mu`, depending only on `k` and `p`, such that

\[
\int |x|^q\,d\mu(x)<\infty\qquad\text{for every }0<q<p, \tag{C022.4}
\]

but

\[
\int |x|^p\,d\mu(x)=\infty, \tag{C022.5}
\]

and nevertheless

\[
\boxed{\mu*k_s\text{ is nonunimodal for every }s>0.} \tag{C022.6}
\]

## Proof

Set

\[
A_n=2^{2^n}.
\]

Choose `N` so large that

\[
W:=\sum_{n\ge N} nA_n^{-p}<\frac12,
\]

and put

\[
w_n=nA_n^{-p}\quad(n\ge N),\qquad w_0=1-W,
\]

\[
\mu=w_0\delta_0+\sum_{n\ge N}w_n\delta_{-A_n}. \tag{C022.7}
\]

This is a probability measure. For every `q<p`,

\[
\sum_{n\ge N}w_nA_n^q
 =\sum_{n\ge N}nA_n^{q-p}<\infty
\]

because `A_n` grows doubly exponentially, proving (C022.4). At the critical power,

\[
\sum_{n\ge N}w_nA_n^p=\sum_{n\ge N}n=\infty,
\]

which proves (C022.5).

Fix an arbitrary scale `s>0`. Choose any fixed `z>0` and set

\[
d:=-k'(z)>0.
\]

Because `A_{n-1}=\sqrt{A_n}`, we may choose `n` arbitrarily large so that simultaneously

\[
A_{n-1}+sz\le \frac{A_n}{2},\qquad \frac{A_n}{2s}\ge R, \tag{C022.8}
\]

and

\[
dn>2^pC_-s^p. \tag{C022.9}
\]

Consider first

\[
x_n=-A_n+sz.
\]

Since `k'` is bounded and the weights sum to one, differentiation of the atomic convolution is justified term by term and

\[
s^2(\mu*k_s)'(x_n)=
 w_0k'(x_n/s)+\sum_{j\ge N}w_jk'((x_n+A_j)/s). \tag{C022.10}
\]

The `j=n` term equals `-dw_n=-dnA_n^{-p}`. For `j>n`, the argument is positive, so every such term is negative and may be discarded in an upper bound. For `j<n` (including the atom at zero), (C022.8) gives

\[
\frac{x_n+A_j}{s}\le-\frac{A_n}{2s},
\]

so (C022.2) gives a total positive contribution at most

\[
C_-\left(\frac{2s}{A_n}\right)^p
\]

because the total mass of these atoms is at most one. Hence

\[
s^2(\mu*k_s)'(x_n)
\le A_n^{-p}\left(-dn+2^pC_-s^p\right)<0. \tag{C022.11}
\]

Now take the midpoint

\[
y_n=-\frac{A_n}{2}.
\]

The atom at zero contributes positively, and for all sufficiently large `n`, (C022.2) gives

\[
w_0k'(-A_n/(2s))
\ge w_0c_-\left(\frac{2s}{A_n}\right)^p. \tag{C022.12}
\]

Every atom with index `j<n` is still to the left of the mode at this test point and therefore contributes positively, so those terms may be discarded in a lower bound. For `j=n`, (C022.3) gives the negative bound

\[
w_n\left|k'(A_n/(2s))\right|
\le 2^pC_+s^p nA_n^{-2p}. \tag{C022.13}
\]

For `j>n`, since `A_j-A_n/2\ge A_j/2`,

\[
w_j\left|k'((A_j-A_n/2)/s)\right|
\le 2^pC_+s^p jA_j^{-2p}. \tag{C022.14}
\]

Therefore

\[
\begin{aligned}
s^2(\mu*k_s)'(y_n)
\ge 2^ps^p\Bigg[
&w_0c_-A_n^{-p}\\
&-C_+nA_n^{-2p}
-C_+\sum_{j>n}jA_j^{-2p}
\Bigg]. \tag{C022.15}
\end{aligned}
\]

The bracket is positive for all sufficiently large `n`. Indeed,

\[
nA_n^{-2p}=o(A_n^{-p}),
\]

and, because `A_{j+1}=A_j^2`, the future series is dominated by its first term for large `n`, so

\[
\sum_{j>n}jA_j^{-2p}=O(nA_{n+1}^{-2p})
=O(nA_n^{-4p})=o(A_n^{-p}). \tag{C022.16}
\]

Thus we may enlarge the same `n=n(s)` so that

\[
(\mu*k_s)'(y_n)>0. \tag{C022.17}
\]

Finally, (C022.8) also gives `x_n<y_n`. We have therefore found two ordered points with

\[
(\mu*k_s)'(x_n)<0<(\mu*k_s)'(y_n),\qquad x_n<y_n. \tag{C022.18}
\]

A differentiable unimodal density cannot have a negative derivative at an earlier point and a positive derivative at a later point: before a mode it is nondecreasing and after a mode it is nonincreasing. Hence `mu*k_s` is nonunimodal. Since `s>0` was arbitrary, (C022.6) holds for every scale. QED.

# 4. R19-I0084-C022B — exact power-moment threshold on every interior stable branch

**STATUS: PROVED INTERNALLY from C022A plus the retained stable-density results; AUDIT PENDING.**

Fix `0<alpha<2` and set

\[
p=2+\alpha.
\]

Take any **interior/two-sided** skewness parameter in either of the frozen source branches:

1. a classical alpha-stable process, or
2. a free alpha-stable process whose time-t law is used as a kernel under ordinary classical convolution `*`.

Then the following two statements hold together:

### Sufficiency at the critical exponent

For every probability measure `mu` with

\[
\int |x|^{2+\alpha}\,d\mu(x)<\infty,
\]

`mu*S_t` is unimodal for all sufficiently large `t`.

This is the retained C018/C019/C020/C021 interior theorem package, based on C008.

### Sharpness below the critical exponent

There exists a single probability measure `mu_*` such that

\[
\int |x|^q\,d\mu_*(x)<\infty
\qquad\text{for every }q<2+\alpha, \tag{C022.19}
\]

but

\[
\int |x|^{2+\alpha}\,d\mu_*(x)=\infty, \tag{C022.20}
\]

and

\[
\boxed{\mu_* * S_t\text{ is nonunimodal for every }t>0.} \tag{C022.21}
\]

## Verification of the C022A hypotheses for the stable kernels

For the **classical branch with alpha != 1**, C021 gives a unique mode, strict derivative signs and eventual convexity of both tails. Its density tails satisfy

\[
k(x)\sim D_+x^{-1-\alpha},\qquad
k(-x)\sim D_-x^{-1-\alpha},
\]

with `D_+,D_->0` precisely in the interior skewness range. The lower derivative bound already used in C021 follows from convexity:

\[
-k'(x)\ge\frac{k(x)-k(2x)}{x}\asymp x^{-2-\alpha}.
\]

The matching upper bound follows from the other secant of a decreasing convex function:

\[
-k'(x)\le \frac{2(k(x/2)-k(x))}{x}
\le \frac{2k(x/2)}{x}
=O(x^{-2-\alpha}). \tag{C022.22}
\]

Reflection gives the matching two-sided bounds. Thus (C022.2)--(C022.3) hold with `p=2+alpha`.

For the **classical alpha=1 interior**, C019 already establishes the exact derivative tails of order `x^{-3}` with positive coefficients on both sides, so C022A applies with `p=3`.

For the **free branch with alpha != 1**, C020 derives directly from the angular parametrization

\[
k'(x)\sim-
\frac{\alpha+1}{\pi}\sin(\pi\alpha\rho)x^{-\alpha-2},
\]

and

\[
k'(-x)\sim
\frac{\alpha+1}{\pi}\sin(\pi\alpha(1-\rho))x^{-\alpha-2},
\]

with both coefficients positive in the interior range. For **free alpha=1**, C018 gives the corresponding positive two-sided `x^{-3}` derivative tails. Hence C022A applies throughout the free interior as well.

Finally, stable time evolution is a spatial dilation plus a translation (with the familiar logarithmic centering at `alpha=1`). Translation does not affect unimodality, while C022A fails unimodality for **every** spatial dilation. This proves (C022.21) for every `t>0`.

# 5. Resulting moment/skewness phase diagram

The supported internal picture is now sharper than a yes/no answer to Conjecture 5.5:

| Stable skewness regime | Exact source moment `2+alpha` | Any lower power-moment assumption |
|---|---|---|
| two-sided / interior, classical kernel | sufficient for eventual unimodality | insufficient: one `mu_*` has every `q<2+alpha` moment finite yet fails for every `t>0` |
| two-sided / interior, free-stable law used under ordinary `*` | sufficient for eventual unimodality | insufficient in the same strong all-time sense |
| extremal boundary, classical/free branches | source conjecture fails | C011/C017 are stronger: even all polynomial moments do not force eventual unimodality |

Thus, **inside the two-sided region, `2+alpha` is the exact threshold in power-moment order**. At the extremal boundary there is a discontinuous change of behavior: no finite collection of polynomial moment assumptions repairs the source statement.

For the frozen `alpha=1/2` task specifically, this adds a sharpness statement for every interior skewness in both branches, but the fixed source-case metric remains `2/2`; the source had already been refuted by admissible endpoints and no duplicate metric credit is claimed.

# 6. Why this is not just the known special cases

Hasebe--Ueda already prove the critical-power counterexample mechanism for the symmetric Cauchy kernel (`p=3`) and the positive half-stable kernel (`p=5/2`). Those cases earn no new credit. C022A abstracts their sparse-atom idea at the **derivative-tail exponent**, and C022B applies it to every interior skewness, every `0<alpha<2`, and both classical-stable and free-stable-law ordinary-convolution branches. The interior kernels are exactly the regime in which the retained C008 theorem also proves sufficiency at that same exponent, so the upper and lower mechanisms now match.

# 7. Prior-art/current-status check — 2026-09-20

Fresh bounded web searches included:

- exact Hasebe--Ueda Conjecture 5.5 and its current arXiv v2 text;
- `"2+alpha" stable convolution unimodality finite moment counterexample`;
- `"eventual unimodality" stable convolution finite moment`;
- `stable density convolution unimodality moment 2+alpha`;
- later Hasebe/Ueda work and citing/related unimodality papers.

The searches recovered the 2018 paper, its known Cauchy and positive-half-stable sharpness examples, and later Hasebe/Ueda work on different multiplicative/free-unimodality questions. I did **not** locate a later primary theorem stating C022A/C022B or resolving this exact frozen arXiv-v2 ordinary-`*` Conjecture 5.5. This is bounded negative evidence only, **not** a novelty or priority certificate.

# 8. Validation, audit state, and next attack

No new finite arithmetic claim was introduced, so I did not spend the run manufacturing a checker. The evidence is the theorem-sized analytic proof above. This follows the current 90/10 rule: the sparse construction and all-scale sign proof are the research contribution; repository/source checks and delivery are the small validation portion.

Existing relevant independent evidence remains:

- `R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF` for the abstract sufficiency engine C008;
- P26 independently audited C010's sparse-bump theorem, but that is not an end-to-end audit of the current frozen arXiv ordinary-`*` package;
- the historical free-`boxplus` audit is a different source-version branch and does not substitute for the frozen ordinary-`*` branch.

Targeted repository search found no new version-matching P26 end-to-end PASS and no distinct second full-package PASS for the frozen ordinary-`*` I0084 package after C021. C022 itself is unaudited. Therefore repository closure remains **PARTIAL / AUDIT_PENDING** even though the current internal mathematics now gives a complete skewness classification plus sharp interior moment order.

The strongest next mathematical attack is no longer another sufficiency lemma. It is to package the proof into one source-matching theorem with a clean parameter statement and test whether the boundary/interior dichotomy can be characterized by the vanishing of one stable derivative-tail coefficient, i.e. whether C008+C022 admit a general kernel theorem with a necessary-and-sufficient two-sided critical-tail condition. That would separate the stable-specific formulas from the real mechanism.

# 9. Scheduler/model control note

The current controlling owner directive still records that the exposed scheduler surface has **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed full-hour duration field**. GPT-6/maximum is therefore still prompt-only here; I cannot truthfully claim it ran. The historical P26 `"You cannot modify this task"` event was context-specific: the retained RESULTS ledger records that a later authorized context successfully updated P26. The supported remedy is the owning/authorized context, ordinary permission/ownership repair or transfer, or platform support — not a bypass. This R19 contract also forbids scheduler changes, so none was attempted in this run.

```yaml
ledger_delta:
  track: R19
  source: "Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084"
  source_version_scope: "frozen arXiv v2: S_t may be classical or free alpha-stable; ordinary classical convolution mu*S_t in both branches"
  target: "eventual unimodality under the exact (2+alpha)-moment assumption; frozen headline alpha=1/2 classical/free source cases"
  metric: "number of complete alpha=1/2 classical-stable/free-stable source cases proved with full input class and original skewness conventions"
  before: "2/2"
  after: "2/2"
  movement: "NO MOVEMENT in fixed metric; substantive theorem progress C022A/C022B"
  status: "PARTIAL_AUDIT_PENDING; mathematical source statement already REFUTED by endpoint skewness"
  unchanged_count: "UNKNOWN; not reconstructed synthetically from commits"
  substantive_stagnation_this_run: 0
  tried_moves: [2, 24, 30]
  move_cycle_note: "all 30 moves exhausted historically; second-cycle reuse; preceding C021 triple was [3,20,21]"
  new_claims:
    - "R19-I0084-C022A: for any strictly unimodal C1 kernel whose two derivative tails are comparable to |x|^{-p}, there is one sparse atomic mu with every q<p moment finite, infinite p moment, and mu*k_s nonunimodal for every s>0"
    - "R19-I0084-C022B: on every interior classical-stable and free-stable-law ordinary-* branch, p=2+alpha is sharp in power-moment order; the counterexample fails unimodality for every t>0"
  retained_positive_result: "C018/C019/C020/C021 + audited C008: finite exact (2+alpha) moment suffices on every interior branch"
  retained_boundary_result: "C011/C017: extremal skewness fails even for an all-polynomial-moment initial law"
  evidence:
    - "full analytic proof in this immutable report"
    - "arXiv:1710.08240v2 primary source, Proposition 5.1 / Theorem 5.2 / Proposition 5.4 / Conjecture 5.5"
    - "R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF"
  audit_ids:
    - "R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF (subtheorem only)"
    - "P26 audit of C010 sparse-bump theorem (subtheorem only; not frozen-package closure)"
  remaining_obligation: "independent audit of C021/C022 and two version-matching end-to-end audits of the frozen arXiv ordinary-* package before repository closure; bounded prior-art search is not a novelty certificate"
```
