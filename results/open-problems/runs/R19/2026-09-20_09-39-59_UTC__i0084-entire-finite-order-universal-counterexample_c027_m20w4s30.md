Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT in the frozen alpha=1/2 source-case count); genuine theorem progress: for every finite stretched-exponential order `Q`, one can choose a single symmetric strictly positive **entire** density with `int exp(c|x|^q)g(x)dx<infinity` for every `c>0` and every `0<q<=Q`, yet ordinary convolution with every half-line-supported probability kernel is nonunimodal. Section-B moves: #20 FIND WHY THE ALGORITHM FAILS, #4 PROVE SOMETHING WEAKER COMPLETELY, #30 DO ONE SCALE/DIRECTION AT A TIME. These are second-cycle reuses because all 30 moves were exhausted historically; the immediately preceding C026 triple was #6/#10/#27, so the preceding triple is not repeated.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY internally already at alpha=1/2 because the frozen source permits extremal skewness; repository status remains PARTIAL / AUDIT_PENDING. New this run: R19-I0084-C027A/B are CANDIDATE THEOREMS / PROVED INTERNALLY / AUDIT PENDING. No source-level closure promotion is claimed.**

# 1. Continuity and source check

I continued from

`runs/R19/2026-09-20_08-40-50_UTC__i0084-strip-analytic-universal-halfline-counterexample_c026_m6d10q27.md`

rather than restarting. I reread/recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the controlling new-methods directive, the I0084/R19 history, and the retained R18/P26 audit trail. The current source was also reopened directly on arXiv v2, including printed page 18.

The frozen source convention is unchanged and decisive: Conjecture 5.5 says that `S_t` may be the law of a **classical or free alpha-stable process**, assumes exactly

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

C026 produced one universal counterexample density that is holomorphic on the strip `|Im z|<pi/2` and has **all** stretched-exponential moments. The new question is whether one can force **entireness**. There is a real tradeoff, not a cosmetic one.

# 2. Three new-method moves

## Move #20 — FIND WHY THE ALGORITHM FAILS

A naive attempt is to keep the C026 profile

\[
\psi(z)=Z^{-1}e^{-\cosh z}
\]

and merely make its translated series entire. This fails for the same-profile universal-separation scheme for a quantitative reason.

At the point `z=i pi`,

\[
|\psi(i\pi-A)|=Z^{-1}e^{\cosh A}.
\tag{2.1}
\]

Thus local convergence at `i pi` of a translated term with coefficient `b_n` forces, at minimum,

\[
b_n e^{\cosh A_n}\to0.
\tag{2.2}
\]

But the universal half-line separation argument needs the active coefficient to dominate the left leakage across the preceding gap `D_n=A_n-A_{n-1}`. Since

\[
|\psi'(-D)|\asymp e^D e^{-\cosh D},
\tag{2.3}
\]

that route requires roughly

\[
b_n\gg e^{-\cosh D_n+O(D_n)}.
\tag{2.4}
\]

When `A_{n-1}->infinity`,

\[
\frac{\cosh D_n}{\cosh A_n}
\sim e^{-A_{n-1}}\to0.
\tag{2.5}
\]

So (2.2) wants `-log b_n` at least on the `cosh A_n` scale, while (2.4) wants it below the much smaller `cosh D_n` scale. The direct C026 profile therefore cannot simply be promoted from a strip to the whole plane while keeping the same universal leakage mechanism.

This is a route obstruction, not a theorem saying that an entire/all-orders construction is impossible by every conceivable method.

## Move #4 — PROVE SOMETHING WEAKER, COMPLETELY

Instead of demanding every stretched-exponential order simultaneously, freeze an arbitrary but finite order ceiling `Q`. A generalized Gaussian profile `exp(-a x^r)` with even integer `r>Q` is entire and has enough real-tail separation to make the universal argument close.

## Move #30 — ONE SCALE / ONE DIRECTION AT A TIME

For each fixed finite `Q`, choose one even integer `r>Q`. This solves every tail gauge `exp(c|x|^q)` with `q<=Q` at once. Since `Q` is arbitrary, there is no finite stretched-exponential order at which entireness rescues eventual unimodality for half-line kernels.

# 3. R19-I0084-C027A — universal entire finite-order counterexample

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

Fix an arbitrary finite `Q>0`. Then there exists a single symmetric strictly positive probability density `g_Q` on `R` such that:

1. `g_Q` extends to an **entire function** on `C`;
2. for every `c>0` and every `q` with `0<q<=Q`,
   \[
   \boxed{\int_{\mathbb R}e^{c|x|^q}g_Q(x)\,dx<\infty;}
   \tag{C027.1}
   \]
3. for every probability measure `K` supported in a lower-bounded or upper-bounded half-line,
   \[
   \boxed{g_Q*K\text{ is nonunimodal}.}
   \tag{C027.2}
   \]

The same `g_Q` works for the entire uncountable class of half-line-supported kernels. In particular translations and positive dilations of `K` are automatically included.

# 4. Construction

Choose an even integer

\[
r=2m>Q
\tag{C027.3}
\]

and any `a>0`. Let

\[
\psi(x)=Z^{-1}e^{-a x^r},
\qquad
Z=\int_{\mathbb R}e^{-a u^r}\,du.
\tag{C027.4}
\]

Fix `theta` with `0<theta<1`, for example `theta=1/2`. Put

\[
A_n=2^{2^n},
\qquad
\widetilde b_n=e^{-\theta a A_n^r}.
\tag{C027.5}
\]

Choose `eta>0` small enough that

\[
B:=\sum_{n\ge1}b_n<1,
\qquad
b_n:=\eta\widetilde b_n.
\tag{C027.6}
\]

Define

\[
\boxed{
 g_Q(x)=(1-B)\psi(x)
 +\sum_{n\ge1}\frac{b_n}{2}
 \bigl[\psi(x-A_n)+\psi(x+A_n)\bigr].
}
\tag{C027.7}
\]

It is immediately even, strictly positive on `R`, and integrates to one.

# 5. Entire extension

Fix a compact disk `|z|<=R`. Since `r` is even,

\[
(z\pm A_n)^r=A_n^r(1+O_R(A_n^{-1})),
\tag{C027.8}
\]

uniformly on that disk. Hence for all sufficiently large `n`,

\[
\operatorname{Re}(z\pm A_n)^r\ge \frac12A_n^r.
\tag{C027.9}
\]

Therefore

\[
|\psi(z\pm A_n)|
\le Z^{-1}e^{-aA_n^r/2}.
\tag{C027.10}
\]

The translated series in (C027.7) is thus locally uniformly convergent on every disk (in fact the profile decay alone already suffices). By Weierstrass' theorem `g_Q` is entire.

# 6. All stretched-exponential moments up to Q

Fix `c>0` and `0<q<=Q<r`. There is a constant `C_q` such that

\[
|u+A|^q\le C_q(|u|^q+A^q)
\tag{C027.11}
\]

for `u,A` real. Since `r>q`,

\[
M_{c,q}:=\int_{\mathbb R}e^{cC_q|u|^q}\psi(u)\,du<\infty.
\tag{C027.12}
\]

Consequently

\[
\int e^{c|x|^q}\psi(x-A_n)\,dx
\le M_{c,q}e^{cC_qA_n^q},
\tag{C027.13}
\]

and likewise for the reflected translate. Thus the remote contribution to the moment is bounded by a constant times

\[
\sum_n
\exp\{-\theta aA_n^r+cC_qA_n^q\}<\infty
\tag{C027.14}
\]

because `r>q`. This proves (C027.1), simultaneously for every `c>0` and every `q<=Q`.

# 7. Universal half-line nonunimodality

Fix an arbitrary probability measure `K` with

\[
\operatorname{supp}K\subset[\ell,\infty)
\tag{C027.15}
\]

for some finite `ell`, and define

\[
h=\psi*K.
\tag{C027.16}
\]

The profile `psi` is positive, `C^1`, bounded, integrable, and both `psi` and `psi'` vanish at infinity. Therefore

\[
h>0,
\qquad h\in C^1,
\qquad h'=\psi'*K,
\qquad h(x)\to0\quad(x\to\pm\infty).
\tag{C027.17}
\]

Choose a point where `h` is positive and compare with sufficiently remote points on both sides. The mean-value theorem supplies fixed real numbers `p<q_0` such that

\[
\boxed{h'(p)>0>h'(q_0).}
\tag{C027.18}
\]

Let

\[
\tau(R)=\sup_{x\le-R}|\psi'(x)|.
\tag{C027.19}
\]

Since

\[
\psi'(x)=-arx^{r-1}\psi(x),
\tag{C027.20}
\]

there are constants `C,R_0` such that

\[
\tau(R)\le C R^{r-1}e^{-aR^r},
\qquad R\ge R_0.
\tag{C027.21}
\]

Set

\[
D_n=A_n-A_{n-1}.
\tag{C027.22}
\]

Because `A_n=A_{n-1}^2`,

\[
\frac{D_n}{A_n}=1-\frac1{A_{n-1}}\longrightarrow1.
\tag{C027.23}
\]

Hence for every fixed real `C_0`,

\[
\boxed{\frac{\tau(D_n-C_0)}{b_n}\to0.}
\tag{C027.24}
\]

Indeed the logarithm of the ratio is

\[
-a(D_n-C_0)^r+\theta aA_n^r+O(\log A_n)
=-a(1-\theta+o(1))A_n^r\to-\infty.
\tag{C027.25}
\]

Also, with

\[
T_n=\sum_{j>n}b_j,
\tag{C027.26}
\]

we have

\[
\boxed{\frac{T_n}{b_n}\to0}
\tag{C027.27}
\]

because `b_{n+1}/b_n=exp[-theta a(A_{n+1}^r-A_n^r)]->0` super-exponentially.

Now let

\[
F=g_Q*K.
\tag{C027.28}
\]

At the test point

\[
x_{n,s}=-A_n+s,
\qquad s\in\{p,q_0\},
\tag{C027.29}
\]

the active translate contributes exactly

\[
\frac{b_n}{2}h'(s).
\tag{C027.30}
\]

Every central or translated component whose center lies to the right of `-A_n` has its `h'` argument at most `-D_n+O_K(1)`. Their total coefficient is at most one, so their combined derivative contribution is bounded by

\[
\tau(D_n-C_K)
\tag{C027.31}
\]

for a fixed constant `C_K`. The still-more-remote negative-center translates with index `j>n` contribute at most

\[
\frac{\|\psi'\|_\infty}{2}T_n.
\tag{C027.32}
\]

Therefore

\[
F'(x_{n,s})
=\frac{b_n}{2}h'(s)+o(b_n)
\tag{C027.33}
\]

uniformly for the two fixed choices `s=p,q_0`. For all large `n`,

\[
F'(x_{n,p})>0,
\qquad
F'(x_{n,q_0})<0.
\tag{C027.34}
\]

For large consecutive indices,

\[
x_{n,q_0}<-A_{n-1}+p=x_{n-1,p}.
\tag{C027.35}
\]

Hence the derivative is negative at a point and positive at a later point to its right:

\[
\boxed{F'(x_{n,q_0})<0<F'(x_{n-1,p}).}
\tag{C027.36}
\]

A differentiable unimodal density cannot have this sign order. Thus `g_Q*K` is nonunimodal.

If `K` is supported in an upper-bounded half-line, reflect it. Since `g_Q` is even, reflection preserves the conclusion. This proves C027A.

# 8. R19-I0084-C027B — frozen alpha=1/2 corollary

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

Let `L_t` be the positive classical alpha=`1/2` stable law from Hasebe--Ueda Section 5.2, let `F_t` be the positive free alpha=`1/2` stable law in the frozen arXiv-v2 sense, and let `check L_t`, `check F_t` be the reflected extremal endpoint laws. Each time marginal is half-line-supported.

For every finite `Q>0`, the single density `g_Q` from C027A satisfies, for every `t>0`,

\[
\boxed{
 g_Q*L_t,\quad g_Q*F_t,\quad
 g_Q*\check L_t,\quad g_Q*\check F_t
 \text{ are all nonunimodal},
}
\tag{C027.37}
\]

while

\[
\boxed{
\int e^{c|x|^q}g_Q(x)\,dx<\infty
\quad\forall c>0,\ 0<q\le Q.
}
\tag{C027.38}
\]

In particular, choose any `Q>5/2`; then `g_Q` is an **entire**, strictly positive, ultra-light initial density satisfying the exact source `5/2` moment by a vast margin, yet all four extremal alpha=`1/2` classical/free ordinary-convolution evolutions remain nonunimodal for every time.

The point is not another metric case—the frozen metric was already saturated at `2/2`—but a stronger regularity statement: **no fixed finite stretched-exponential tail order, even together with entireness and strict positivity, rescues the endpoint conjecture.**

# 9. Relation to C025/C026 and the honest limit of the method

C025 allowed arbitrary countable `C^infty` derivative envelopes but used compactly supported microscopic bumps, hence could not be analytic.

C026 used the common profile `e^{-cosh x}` and achieved one strip-holomorphic density with *all* stretched-exponential moments, universal over all half-line-supported kernels.

C027 moves analyticity in the other direction: it upgrades the density from strip-holomorphic to **entire**, while retaining all stretched-exponential moments only up to an arbitrary prescribed finite ceiling `Q`. Since `Q` can be chosen as large as desired, this rules out every fixed finite-order tail criterion of that form.

I do **not** claim an entire density having all stretched-exponential moments simultaneously. Move #20 above explains why the direct common-profile C026 mechanism cannot simply deliver that stronger statement.

# 10. Current literature / prior-art search, 2026-09-20

Fresh bounded searches covered:

- exact `Hasebe Ueda Conjecture 5.5` and `arXiv:1710.08240`;
- `2+alpha` moment + stable convolution + eventual unimodality;
- `entire density` / `real analytic density` + convolution + unimodality counterexample;
- `half-line kernel` + convolution + nonunimodality;
- later Hasebe/Ueda unimodality papers and related stable-law work.

The current search again recovered the original Hasebe--Ueda paper and later multiplicative-unimodality work, but did not locate a later primary theorem resolving the exact frozen arXiv-v2 ordinary-`*` Conjecture 5.5 or stating the universal entire finite-order theorem C027A. Search results around entire-function convolution were unrelated approximation/deconvolution work. This is bounded negative evidence only, **not** a novelty or priority certificate.

The original paper itself already proves a classical Brownian threshold under one Gaussian-square exponential moment and constructs a sub-Gaussian counterexample below that threshold. That makes it especially important not to advertise C027 as a generic discovery that "light tails can fail"; the specific new content is the combination of **entireness + arbitrary finite stretched-exponential order + one kernel-independent density for every half-line-supported kernel**.

# 11. Checks and audit posture

No finite arithmetic claim is introduced, so no checker was manufactured merely for bookkeeping. The theorem-sized claim is proved on the page.

Retained audit state:

- `R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF` for the positive interior smoothing engine;
- narrower historical C010/P26 and half-stable checks remain preserved;
- no version-matching end-to-end P26 PASS for the full frozen arXiv ordinary-`*` package and no distinct second full-package PASS were located;
- C021--C027 remain self-proved / independent audit pending.

Therefore repository closure is not claimed.

# 12. Model/scheduler control status

The exposed automation/task surface available in this run still has no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guaranteed one-hour runtime field. Thus the requested `GPT-6 / maximum` remains prompt text only here; this report truthfully records **GPT-5.6 Sol / UNVERIFIED**.

The current repository ledger records that the historical P26 `You cannot modify this task` failure was authorization-context-specific and that a later authorized context successfully updated P26. The supported workaround is the owning/authorized context, supported permission/ownership repair or transfer, or platform support—not a bypass or duplicate task. Enforceable GPT-6/maximum would require explicit persisted model/reasoning fields plus trustworthy per-run runtime attestation in the scheduler/product/API surface.

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
  unchanged_count: "UNKNOWN for the saturated headline metric; preserve UNKNOWN rather than infer a streak"
  substantive_stagnation_this_run: 0
  status: "SOURCE REFUTED MATHEMATICALLY INTERNALLY; repository PARTIAL / AUDIT_PENDING"
  tried_moves: [20, 4, 30]
  move_note: "second-cycle reuses because all 30 were exhausted historically; preceding C026 triple was 6/10/27"
  new_claims:
    c027a: "for every finite Q, one symmetric strictly positive entire density with all exp(c|x|^q), q<=Q, moments finite defeats ordinary convolution with every half-line-supported probability kernel"
    c027b: "same density defeats all four alpha=1/2 extremal classical/free stable endpoint laws at every t>0 under ordinary *"
  failed_route:
    c026_entire_direct: "same-profile e^{-cosh z} translation scheme cannot simultaneously satisfy entire local convergence at z=i*pi and the universal previous-gap leakage domination; this is a route obstruction, not an impossibility theorem"
  evidence:
    - "runs/R19/2026-09-20_08-40-50_UTC__i0084-strip-analytic-universal-halfline-counterexample_c026_m6d10q27.md"
    - "Hasebe-Ueda arXiv:1710.08240v2, printed page 18, Conjecture 5.5"
    - "this report: complete C027A/B proof"
  audit_ids:
    c008: "R18-AUDIT-R19-I0084-C008-ABSTRACT-003=PASS_FULL_MATHEMATICAL_PROOF"
    frozen_package_p26: "NOT_LOCATED / version-matching end-to-end gate unfilled"
    frozen_package_second: "NOT_LOCATED / distinct end-to-end gate unfilled"
  remaining_obligation: "independent theorem-level review of C021-C027 and two version-matching end-to-end outside audits before repository closure; do not replace ordinary * by free convolution"
```
