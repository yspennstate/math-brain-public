Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT in the frozen alpha=1/2 source-case count); genuine theorem progress: one single symmetric strictly positive real-analytic density, with every stretched-exponential moment finite, defeats ordinary convolution with every half-line-supported probability kernel and hence all four classical/free alpha=1/2 extremal stable endpoint laws at every time. Section-B moves: #6 DEFORM TO A POINT YOU CAN SOLVE, #10 DERANDOMIZE, #27 SWAP THE QUANTIFIERS. These are second-cycle reuses because all 30 moves were exhausted historically; the immediately preceding C025 triple was #1/#19/#29, so the preceding triple is not repeated.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY internally already at alpha=1/2 because the frozen source permits extremal skewness; repository status remains PARTIAL / AUDIT_PENDING. New this run: R19-I0084-C026A/B are CANDIDATE THEOREMS / PROVED INTERNALLY / AUDIT PENDING. No source-level closure promotion is claimed.**

# 1. Continuity, repository state, and exact source convention

I resumed from the actual newest R19 theorem report

`runs/R19/2026-09-20_07-45-13_UTC__i0084-weighted-cinfty-envelope-counterexample_c025_m1a19p29.md`

and its transcription-only erratum

`artifacts/R19/2026-09-20_07-48-51_UTC__c025_formula_erratum.md`.

I queried/reread the current campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, current new-methods operational state, current I0084/R19 history, and the existing R18/P26 audit trail. Current `RESULTS.md` still records the R-series native configuration as prompt-only with no binding model/reasoning selector; targeted search found no later R19 theorem report before this write and no new version-matching full-package I0084 audit. The append-only intake corpus remains too large for a useful byte-for-byte model-visible reread through this connector; I preserve the established I0084 source row rather than pretending the entire corpus was displayed.

The original arXiv-v2 PDF was reopened directly. On printed page 18, Conjecture 5.5 says that `S_t` may be the law of a **classical or free alpha-stable process**, assumes exactly

\[
\int_{\mathbb R}|x|^{2+\alpha}\,d\mu(x)<\infty,
\tag{1.1}
\]

and concludes eventual unimodality of

\[
\boxed{\mu*S_t}.
\tag{1.2}
\]

The star is ordinary classical convolution in the frozen arXiv-v2 statement even when `S_t` is the law of a free stable process. I do not replace it by `\boxplus`.

At alpha=`1/2`, the positive classical half-stable law is supported on a right half-line; the positive free half-stable law is likewise supported on a right half-line. Their reflected skew endpoints are supported on left half-lines. The retained C024/C025 constructions already show that endpoint failure survives very strong `C^\infty` tail regularity. The new question is different:

> Can the bad initial law be made **real analytic and strictly positive everywhere**, while remaining lighter-tailed than every stretched exponential, and can one choose the **same** law independently of the one-sided kernel?

The answer is yes.

# 2. Three new-method moves

## Move #6 — DEFORM TO A POINT YOU CAN SOLVE

The compactly supported microscopic bumps in C025 are ideal for exact support separation but can never be real analytic unless they vanish identically. I therefore deformed the bump profile to

\[
\psi(x)=Z^{-1}e^{-\cosh x},
\qquad
Z=\int_{\mathbb R}e^{-\cosh u}\,du.
\tag{2.1}
\]

This profile is even, strictly positive, real analytic, holomorphic on all of `C`, and has double-exponential real tails. The loss of exact compact support is compensated by a quantitative one-sided leakage estimate.

## Move #10 — DERANDOMIZE

No kernel-specific weights or locations are needed. A completely explicit deterministic choice

\[
A_n=4^n,
\qquad
b_n=\exp\{-e^{A_n/4}\}
\tag{2.2}
\]

works universally. The same initial density handles every one-sided probability kernel, not merely the two half-stable kernels.

## Move #27 — SWAP THE QUANTIFIERS

C024/C025 had the form: for a prescribed countable family of kernels, construct a bad initial law. The new result reverses the dependence:

\[
\boxed{\exists g\ \forall K\text{ supported in a half-line}:\quad g*K\text{ is nonunimodal}.}
\tag{2.3}
\]

The family of kernels is now uncountable and no kernel enters the construction of `g`.

# 3. R19-I0084-C026A — universal analytic half-line-kernel counterexample

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

There exists a single symmetric strictly positive probability density `g` on `R` with the following properties.

1. `g` extends holomorphically to the fixed strip
   \[
   \{z\in\mathbb C:|\operatorname{Im}z|<\pi/2\},
   \tag{C026.1}
   \]
   so in particular `g` is real analytic on all of `R`.

2. For every `c>0` and every `q>0`,
   \[
   \boxed{\int_{\mathbb R}e^{c|x|^q}g(x)\,dx<\infty.}
   \tag{C026.2}
   \]

3. Let `K` be **any** probability measure supported in a lower-bounded half-line `[ell,infinity)` for some finite `ell`. Then
   \[
   \boxed{g*K\text{ is nonunimodal}.}
   \tag{C026.3}
   \]

4. By symmetry, if `K` is any probability measure supported in an upper-bounded half-line `(-infinity,u]`, then `g*K` is also nonunimodal.

Translations and positive dilations of `K` remain half-line-supported, so (C026.3) holds simultaneously for every time/scale in any one-sided convolution semigroup.

This is complementary to C025 rather than a formal superset of it: C025 allows essentially arbitrary prescribed positive `C^\infty` envelopes, while C026 forces genuine analyticity and universality over **all** half-line-supported kernels.

# 4. Explicit construction and analytic/tail properties

Let `psi` be (2.1). Put

\[
A_n=4^n,
\qquad
b_n=e^{-e^{A_n/4}},
\qquad
B=\sum_{n\ge1}b_n.
\tag{C026.4}
\]

Since `b_1=e^{-e}` and the later terms are tiny, `B<1`. Define

\[
\boxed{
 g(x)=(1-B)\psi(x)
 +\sum_{n\ge1}\frac{b_n}{2}
 \bigl[\psi(x-A_n)+\psi(x+A_n)\bigr].
}
\tag{C026.5}
\]

Plainly `g` is even, strictly positive and integrates to one.

## 4.1 Holomorphic strip

For `z=x+iy`,

\[
\operatorname{Re}\cosh(z\pm A_n)
=\cosh(x\pm A_n)\cos y.
\tag{C026.6}
\]

Fix a compact subset of `|Im z|<pi/2`; then `|x|<=R` and `|y|<=pi/2-delta` for some `R,delta>0`. Hence

\[
\operatorname{Re}\cosh(z\pm A_n)
\ge (\sin\delta)\cosh(A_n-R)
\ge c_{R,\delta}e^{A_n}
\tag{C026.7}
\]

for all large `n`. Therefore

\[
|\psi(z\pm A_n)|
\le C\exp\{-c_{R,\delta}e^{A_n}\},
\tag{C026.8}
\]

and the series (C026.5) converges locally uniformly on the strip. Thus `g` is holomorphic there.

## 4.2 Every stretched-exponential moment

For every `c,q>0`, the base profile satisfies

\[
M_{c,q}:=\int e^{c|u|^q}\psi(u)\,du<\infty,
\tag{C026.9}
\]

because `cosh u` dominates every power of `|u|`. With

\[
|u+A_n|^q\le C_q(|u|^q+A_n^q),
\tag{C026.10}
\]

we have

\[
\int e^{c|x|^q}\psi(x-A_n)\,dx
\le M_{C_qc,q}\,e^{C_qcA_n^q},
\tag{C026.11}
\]

and the same bound for the reflected translate. Consequently the remote contribution is bounded by a constant times

\[
\sum_n \exp\{-e^{A_n/4}+C_qcA_n^q\}<\infty,
\tag{C026.12}
\]

which proves (C026.2). In particular `g` has every polynomial moment and satisfies the frozen alpha=`1/2` source requirement `int |x|^(5/2)g(x) dx<infinity` by a vast margin.

# 5. Two universal separation estimates

Let

\[
M:=\|\psi'\|_\infty<\infty,
\qquad
\tau(R):=\sup_{x\le -R}|\psi'(x)|.
\tag{C026.13}
\]

Since

\[
\psi'(x)=-Z^{-1}\sinh(x)e^{-\cosh x},
\tag{C026.14}
\]

there are constants `C,R_0` such that

\[
\tau(R)\le C e^R\exp\{-e^R/3\},
\qquad R\ge R_0.
\tag{C026.15}
\]

Let

\[
D_n:=A_n-A_{n-1}=3\cdot 4^{n-1}=\frac34A_n,
\qquad
T_n:=\sum_{j>n}b_j.
\tag{C026.16}
\]

Then for every fixed real `C_0`,

\[
\boxed{\frac{\tau(D_n-C_0)}{b_n}\longrightarrow0.}
\tag{C026.17}
\]

Indeed, the negative logarithm coming from `tau` has size `e^(3A_n/4+O(1))`, while `-log b_n=e^(A_n/4)`.

Also

\[
\frac{b_{n+1}}{b_n}
=\exp\{-e^{A_n}+e^{A_n/4}\}\longrightarrow0,
\tag{C026.18}
\]

and the ratios decrease super-exponentially, so

\[
\boxed{\frac{T_n}{b_n}\longrightarrow0.}
\tag{C026.19}
\]

These are the only scale-separation estimates needed.

# 6. Proof of universal nonunimodality

Fix an arbitrary probability measure `K` with

\[
\operatorname{supp}K\subset[\ell,\infty)
\tag{C026.20}
\]

for some finite `ell`. Define

\[
h=\psi*K.
\tag{C026.21}
\]

Because `psi>0`, `h>0`. Also `psi,psi'` are continuous, bounded and vanish at infinity, so

\[
h\in C^1,\qquad h'=\psi'*K,
\qquad h(x)\to0\quad(x\to\pm\infty).
\tag{C026.22}
\]

Choose any `x_0` with `h(x_0)>0`. Taking `L<x_0<R` far enough that `h(L),h(R)<h(x_0)` and applying the mean-value theorem gives points

\[
p<x_0<q
\tag{C026.23}
\]

such that

\[
\boxed{h'(p)>0>h'(q).}
\tag{C026.24}
\]

No unimodality or differentiability assumption on `K` is used.

For left-tail control, if `y<=-R`, then every `z` in the support of `K` obeys `y-z<=-R-ell`; hence

\[
|h'(y)|
\le \tau(R+\ell)
\tag{C026.25}
\]

once `R+ell` is large enough.

Now put

\[
F=g*K.
\tag{C026.26}
\]

For `r` equal to `p` or `q`, evaluate at

\[
x_{n,r}=-A_n+r.
\tag{C026.27}
\]

The translate centered at `-A_n` is the active bump and contributes exactly

\[
\frac{b_n}{2}h'(r).
\tag{C026.28}
\]

Every central or remote component whose center lies to the **right** of `-A_n` has its `h'` argument at most

\[
-D_n+r.
\tag{C026.29}
\]

This includes the central bump, all positive-center translates, the reflected partner at `+A_n`, and all negative-center translates with index `<n`. Their total coefficient is at most one. Therefore, with a constant `C_K` depending only on the fixed `p,q,ell`, their combined derivative contribution at either test point is bounded by

\[
\tau(D_n-C_K).
\tag{C026.30}
\]

The only remaining terms are the negative-center translates with index `j>n`, lying still farther to the left. For them we use only

\[
\|h'\|_\infty\le\|\psi'\|_\infty=M,
\tag{C026.31}
\]

so their total derivative contribution is at most

\[
\frac{M}{2}T_n.
\tag{C026.32}
\]

Combining (C026.28)--(C026.32),

\[
F'(x_{n,r})
=\frac{b_n}{2}h'(r)+E_{n,r},
\tag{C026.33}
\]

where

\[
|E_{n,r}|
\le \tau(D_n-C_K)+\frac{M}{2}T_n
=o(b_n)
\tag{C026.34}
\]

by (C026.17) and (C026.19). Therefore for all sufficiently large `n`,

\[
F'(x_{n,p})>0,
\qquad
F'(x_{n,q})<0.
\tag{C026.35}
\]

Since `D_n\to\infty`, for large consecutive indices

\[
x_{n,q}=-A_n+q
< -A_{n-1}+p=x_{n-1,p}.
\tag{C026.36}
\]

Thus at a point farther left the derivative is negative, while at a later point to the right it is positive:

\[
\boxed{F'(x_{n,q})<0<F'(x_{n-1,p}).}
\tag{C026.37}
\]

A differentiable unimodal density cannot decrease and then increase in this order: if its mode were to the right of the first point, the negative derivative is impossible on the nondecreasing side; if the mode were at or to the left of the first point, the later positive derivative is impossible on the nonincreasing side. Hence `F=g*K` is nonunimodal.

This proves C026A.

# 7. Upper half-lines and affine changes

If `K` is supported in `(-infinity,u]`, let `check K` be its reflection. Then `check K` is lower-bounded. Since `g` is even,

\[
g*K
\tag{C026.38}
\]

is the reflection of `g*check K`; reflection preserves unimodality/nonunimodality. Thus C026A also covers every upper-bounded half-line kernel.

If `K_{a,b}` is an affine image of `K` with `a>0`, its support remains a half-line. Therefore the conclusion is automatically stable under the time-dependent dilations and translations appearing in stable-process conventions.

# 8. R19-I0084-C026B — alpha=1/2 frozen-source corollary

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

Let `L_t` be the positive classical alpha=`1/2` stable law from Hasebe--Ueda Section 5.2, and let `F_t` be the law at time `t` of the positive free alpha=`1/2` stable process in the frozen arXiv-v2 sense. Both are supported in right half-lines. Let their reflected endpoint laws be `check L_t` and `check F_t`.

For the single density `g` in C026A, for every `t>0`,

\[
\boxed{
 g*L_t,\quad g*F_t,\quad g*\check L_t,\quad g*\check F_t
 \text{ are all nonunimodal}.
}
\tag{C026.39}
\]

At the same time, for every `c,q>0`,

\[
\int e^{c|x|^q}g(x)\,dx<\infty.
\tag{C026.40}
\]

In particular `g` satisfies the exact source `5/2`-moment hypothesis. Thus the frozen Conjecture 5.5 is not merely false at alpha=`1/2`; it already fails for one **strictly positive real-analytic ultra-light initial density**, simultaneously for both classical/free laws and both extremal skewnesses.

The same abstract theorem also applies without modification to any other one-sided stable endpoint law (classical or free) whose time marginals are half-line-supported. I do not use that broader observation to alter the fixed alpha=`1/2` metric.

# 9. What this adds beyond C024/C025

C024 gave a symmetric `C^infty` initial density with every stretched-exponential moment finite, for a countable chosen family of one-sided kernels.

C025 strengthened the pointwise smooth tail control to an arbitrary countable family of positive derivative envelopes and removed the global bound on the kernel derivative, but still used compactly supported microscopic bumps and hence was necessarily non-analytic.

C026 makes a different strengthening:

- `g` is strictly positive everywhere and real analytic on `R`;
- `g` has a holomorphic extension to the fixed strip `|Im z|<pi/2`;
- `g` has every stretched-exponential moment, including `int e^{c x^2}g(x)dx<infinity` for every `c>0`;
- **one and the same** `g` defeats every lower- or upper-half-line-supported probability kernel, an uncountable class, without any kernel-specific choice.

This also highlights a sharp qualitative contrast with the Brownian result in the same Hasebe--Ueda paper: their classical Brownian theorem proves eventual unimodality under one Gaussian-square exponential moment, whereas the analytic `g` above has all such moments and nevertheless never becomes unimodal under the one-sided half-stable endpoint kernels. There is no contradiction because the smoothing kernels are different.

# 10. Prior-art and current-source search, 2026-09-20

I searched the current web/primary-source surface for combinations of:

- `Hasebe Ueda arXiv 1710.08240 Conjecture 5.5 stable unimodality ordinary convolution`;
- `Conjecture 5.5 Hasebe Ueda stable unimodality`;
- `eventual unimodality stable convolution analytic density counterexample`;
- `real analytic density convolution one sided stable nonunimodal counterexample`;
- `unimodality convolution half-line kernel counterexample density`;
- later Hasebe/Ueda unimodality papers and author publication lists.

The search recovered the original arXiv/ALEA paper, Hasebe--Simon--Wang on free stable shape, and later multiplicative-unimodality work, but I did **not** locate a later primary theorem resolving this exact frozen arXiv-v2 ordinary-`*` Conjecture 5.5 or stating the universal real-analytic half-line-kernel theorem C026A. This is bounded negative search evidence only, not a novelty or priority certificate.

The source paper itself already contains very light-tail counterexample philosophy in its Brownian sections and an atomic half-stable counterexample in Proposition 5.4. C024/C025 are retained internal predecessors. Accordingly, novelty claims must be phrased around the **analytic universal half-line-kernel quantifier swap**, not around the generic fact that light tails can coexist with nonunimodality.

# 11. Checks and audit posture

No finite arithmetic claim is introduced, so I did not manufacture a checker merely for bookkeeping. The theorem-sized claim is proved on the page above.

Retained audit state:

- `R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF` for the abstract positive smoothing theorem used in interior cases;
- the older C010 sparse-bump package has narrower P26 review history;
- targeted repository search still finds **no** version-matching end-to-end P26 PASS for the full frozen arXiv ordinary-`*` package and **no** distinct second full-package PASS;
- C021--C026, including this new universal analytic theorem, remain self-proved / independent audit pending.

Therefore repository closure is not claimed.

# 12. Model/scheduler control status

The exposed scheduler/task-control surface available to this worker still does not provide a binding model-family selector, a binding reasoning-effort selector, authenticated per-run applied-model/applied-effort telemetry, or a guaranteed one-hour execution field. Thus `GPT-6 / maximum` remains prompt text only here; this report truthfully records GPT-5.6 Sol / UNVERIFIED.

Repository deployment history also preserves the historical P26 `You cannot modify this task` event and a later successful P26 update from a different authorized context. The lawful workaround is therefore the owning/authorized context, supported ownership/permission repair or transfer, or platform support — not a bypass or a duplicate task. Actual GPT-6/maximum enforcement would require a scheduler/product/API layer that persists explicit model and reasoning fields and returns trustworthy runtime attestation.

# 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R19
  lane: CLOSABLE_OUTSIDE
  source: "Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / I0084"
  source_version_scope: "frozen arXiv v2: ordinary classical convolution mu*S_t for both classical-stable and free-stable-law branches"
  fixed_metric: "number of complete classical-stable/free-stable alpha=1/2 source cases proved, retaining full input class and original skewness conventions"
  before: "2/2"
  after: "2/2"
  metric_movement: "NO MOVEMENT"
  unchanged_count: "UNKNOWN for the saturated headline metric; do not infer from repeated 2/2"
  substantive_stagnation_this_run: 0
  status: "SOURCE REFUTED MATHEMATICALLY INTERNALLY; repository PARTIAL / AUDIT_PENDING"
  tried_moves: [6, 10, 27]
  move_note: "second-cycle reuses because all 30 were exhausted historically; preceding C025 triple was 1/19/29"
  new_claims:
    c026a: "single symmetric strictly positive strip-holomorphic density with all stretched-exponential moments defeats ordinary convolution with every half-line-supported probability measure"
    c026b: "same density defeats all four alpha=1/2 extremal classical/free stable endpoint laws at every t>0 under ordinary *"
  evidence:
    - "runs/R19/2026-09-20_07-45-13_UTC__i0084-weighted-cinfty-envelope-counterexample_c025_m1a19p29.md"
    - "artifacts/R19/2026-09-20_07-48-51_UTC__c025_formula_erratum.md"
    - "Hasebe-Ueda arXiv:1710.08240v2 PDF, printed page 18, Conjecture 5.5"
    - "this report: complete C026A/B proof"
  audit_ids:
    c008: "R18-AUDIT-R19-I0084-C008-ABSTRACT-003=PASS_FULL_MATHEMATICAL_PROOF"
    frozen_package_p26: "NOT_LOCATED / version-matching end-to-end gate unfilled"
    frozen_package_second: "NOT_LOCATED / distinct end-to-end gate unfilled"
    c026: "SELF-PROOF ONLY / INDEPENDENT AUDIT PENDING"
  remaining_obligation:
    - "independent theorem-level audit of C021--C026, especially C026's universal half-line leakage argument"
    - "version-matching P26 full-package audit of frozen arXiv ordinary-* scope"
    - "distinct second end-to-end audit by another track"
    - "prior-art/priority check remains bounded, not certified exhaustive"
  scheduler_model_control: "no binding model/reasoning selector or authenticated runtime receipt exposed; GPT-6 maximum prompt-only"
```
