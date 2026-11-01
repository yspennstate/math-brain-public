Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT in the frozen alpha=1/2 source-case count); genuine theorem progress: C027's finite stretched-exponential ceiling can be removed. One single symmetric strictly positive ENTIRE density has `int exp(c|x|^q)g(x)dx<infinity` for every `c,q>0` simultaneously and ordinary convolution with every half-line-supported probability kernel is nonunimodal. Section-B moves: #1 CHANGE THE CATEGORY, #3 PROVE SOMETHING STRONGER, #18 SAY IT IN ANOTHER LANGUAGE. These are second-cycle reuses because all 30 moves were exhausted historically; the immediately preceding C027 triple was #20/#4/#30, so the preceding triple is not repeated.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY internally already at alpha=1/2 because the frozen arXiv source permits extremal skewness; repository status remains PARTIAL / AUDIT_PENDING. New this run: R19-I0084-C028A/B are CANDIDATE THEOREMS / PROVED INTERNALLY / AUDIT PENDING. No source-level closure promotion is claimed.**

# 1. Continuity and source/version check

I continued from

`runs/R19/2026-09-20_09-39-59_UTC__i0084-entire-finite-order-universal-counterexample_c027_m20w4s30.md`

rather than restarting. I recovered the campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the retained R18 neighboring closure report, the I0084/R19 history and current audit posture. I also rechecked the current primary-source/literature surface on 2026-09-20.

The frozen arXiv-v2 source convention remains decisive. Its Conjecture 5.5 says that `S_t` may be the law of a **classical or free alpha-stable process**, assumes exactly

\[
\int_{\mathbb R}|x|^{2+\alpha}\,d\mu(x)<\infty,
\tag{1.1}
\]

and concludes eventual unimodality of

\[
\boxed{\mu*S_t}.
\tag{1.2}
\]

The star is ordinary classical convolution in the frozen arXiv statement even when `S_t` is the law of a free stable process. I do not replace it by `\boxplus`. The later published ALEA formulation separates the classical `*` and free `\boxplus` branches; that later wording is not substituted for the frozen target.

C027 proved an entire universal counterexample with stretched-exponential moments through any prescribed finite order `Q`, but left open whether one ENTIRE density could have **all** stretched-exponential moments simultaneously. C026 had all orders but only strip holomorphy. C028 closes exactly that regularity gap.

# 2. Three new-method moves

## Move #1 — CHANGE THE CATEGORY

The obstruction in C027 was not probabilistic; it was an entire-function growth problem. I moved the construction to the category of even entire functions and asked for an exponent whose real-axis growth is faster than every power but whose phase under a bounded complex translation changes by `o(1)` at remote positive arguments.

## Move #3 — PROVE SOMETHING STRONGER

Instead of fixing a finite moment ceiling `Q`, target one density satisfying every gauge `exp(c|x|^q)` simultaneously, while remaining kernel-independent and entire.

## Move #18 — SAY IT IN ANOTHER LANGUAGE

Write the bump profile as `psi=exp(-P)` and translate the old leakage-versus-entire-convergence conflict into a growth-design problem for `P`: we want `P(x)` superpolynomial, but with `P(A-a)/P(A)->1` whenever `a=o(sqrt(A))`, and with bounded complex shifts preserving positive real part. The explicit entire function below has exactly that behavior.

# 3. The explicit entire exponent

Define

\[
\boxed{
P(z)=2\sum_{m=0}^{\infty}\frac{z^{2m}}{(4m)!}.
}
\tag{C028.1}
\]

This is an even entire function. Equivalently, with either branch of the square root,

\[
P(z)=\cosh\sqrt z+\cos\sqrt z,
\tag{C028.2}
\]

because both terms are even in `sqrt(z)` and the power series gives the entire continuation.

For real `x`, evenness gives

\[
P(x)=\cosh\sqrt{|x|}+\cos\sqrt{|x|}>0.
\tag{C028.3}
\]

Indeed `cosh u>1>=-cos u` for `u>0`, while `P(0)=2`. Moreover, as `|x|->infinity`,

\[
\boxed{P(x)=\frac12e^{\sqrt{|x|}}(1+o(1)).}
\tag{C028.4}
\]

Set

\[
\psi(x)=Z^{-1}e^{-P(x)},
\qquad
Z=\int_{\mathbb R}e^{-P(u)}\,du.
\tag{C028.5}
\]

Then `psi` is even, strictly positive, a probability density, and extends to an entire function `Z^{-1}e^{-P(z)}`.

Because `e^{sqrt(x)}` dominates every power of `x`, for every `c,q>0`,

\[
\boxed{
\int_{\mathbb R}e^{c|x|^q}\psi(x)\,dx<\infty.
}
\tag{C028.6}
\]

For `x>0`,

\[
P'(x)=\frac{\sinh\sqrt x-\sin\sqrt x}{2\sqrt x}>0,
\tag{C028.7}
\]

so `psi` is strictly decreasing on `(0,infinity)` and increasing on `(-infinity,0)`.

For all sufficiently large `x`, crude bounds from (C028.3)--(C028.7) give

\[
P(x)\ge \frac14e^{\sqrt x},
\qquad
0<P'(x)\le e^{\sqrt x}.
\tag{C028.8}
\]

Hence, if

\[
\tau(R)=\sup_{x\le -R}|\psi'(x)|,
\tag{C028.9}
\]

then by evenness and monotonicity of `y e^{-y/4}` for large `y`,

\[
\boxed{
\tau(R)\le C e^{\sqrt R}\exp\{-\tfrac14 e^{\sqrt R}\}
}
\tag{C028.10}
\]

for all large `R`.

# 4. Remote centers and weights

Choose `A_1` sufficiently large and recursively

\[
\boxed{A_{n+1}=A_n^4.}
\tag{C028.11}
\]

Fix

\[
\theta=\frac18
\tag{C028.12}
\]

and put

\[
\widetilde b_n=e^{-\theta P(A_n)}.
\tag{C028.13}
\]

Choose `eta>0` so small that

\[
B:=\sum_{n\ge1}b_n<1,
\qquad
b_n:=\eta\widetilde b_n.
\tag{C028.14}
\]

Define

\[
\boxed{
 g(x)=(1-B)\psi(x)
 +\sum_{n\ge1}\frac{b_n}{2}
 \left[\psi(x-A_n)+\psi(x+A_n)\right].
}
\tag{C028.15}
\]

It is immediately even, strictly positive and integrates to one.

# 5. Entire extension of the translated series

The key point distinguishing C028 from the failed `e^{-cosh z}` route is that a bounded imaginary translation changes `sqrt(A)` only by `O(A^{-1/2})`, so the phase of the dominant `e^{sqrt(A)}` term tends to zero.

Fix a compact disk `|z|<=R`. For `w=A_n+z`, take the principal square root `s=sqrt(w)`. Uniformly on this disk,

\[
\operatorname{Re}s=\sqrt{A_n}+O_R(A_n^{-1/2}),
\qquad
|\operatorname{Im}s|=O_R(A_n^{-1/2}).
\tag{C028.16}
\]

Therefore, for all sufficiently large `n`,

\[
\operatorname{Re}\cosh s
=\cosh(\operatorname{Re}s)\cos(\operatorname{Im}s)
\ge c_R e^{\sqrt{A_n}},
\tag{C028.17}
\]

while

\[
|\operatorname{Re}\cos s|
\le \cosh(|\operatorname{Im}s|)\le 2.
\tag{C028.18}
\]

Thus

\[
\operatorname{Re}P(A_n+z)\ge c_R e^{\sqrt{A_n}}
\tag{C028.19}
\]

for all large `n`, uniformly on `|z|<=R`. By evenness,

\[
P(-A_n+z)=P(A_n-z),
\tag{C028.20}
\]

so the same bound holds for both translated signs. Consequently

\[
|\psi(z\pm A_n)|
\le C_R\exp\{-c_R e^{\sqrt{A_n}}\}.
\tag{C028.21}
\]

The translated series in (C028.15) therefore converges locally uniformly on every compact subset of `C` (even before exploiting the extra `b_n` factor). By Weierstrass' theorem,

\[
\boxed{g\text{ is entire}.}
\tag{C028.22}
\]

# 6. Every stretched-exponential moment, all orders simultaneously

Fix arbitrary real `c,q>0`. There is `C_q<infinity` such that

\[
|u+A|^q\le C_q(|u|^q+A^q).
\tag{C028.23}
\]

By (C028.6),

\[
M_{c,q}:=\int e^{cC_q|u|^q}\psi(u)\,du<\infty.
\tag{C028.24}
\]

Hence

\[
\int e^{c|x|^q}\psi(x-A_n)\,dx
\le M_{c,q}e^{cC_qA_n^q},
\tag{C028.25}
\]

and likewise for the reflected translate. Since

\[
P(A_n)\sim \tfrac12e^{\sqrt{A_n}},
\tag{C028.26}
\]

we have

\[
\sum_n b_n e^{cC_qA_n^q}
\le \eta\sum_n
\exp\{-\theta P(A_n)+cC_qA_n^q\}<\infty.
\tag{C028.27}
\]

Therefore the SINGLE density `g` satisfies

\[
\boxed{
\int_{\mathbb R}e^{c|x|^q}g(x)\,dx<\infty
\qquad\forall c>0,\ \forall q>0.
}
\tag{C028.28}
\]

This removes the finite-order ceiling from C027.

# 7. The gap asymptotic that makes the universal argument work

Let

\[
D_n=A_n-A_{n-1}.
\tag{C028.29}
\]

Because `A_n=A_{n-1}^4`, for every fixed `C_0`,

\[
\sqrt{D_n-C_0}
=\sqrt{A_n}+o(1),
\tag{C028.30}
\]

hence

\[
\boxed{
\frac{e^{\sqrt{D_n-C_0}}}{e^{\sqrt{A_n}}}\to1.
}
\tag{C028.31}
\]

Also, for all large `A`,

\[
P(A)\le e^{\sqrt A}.
\tag{C028.32}
\]

Combining (C028.10), (C028.13), (C028.31), (C028.32), and `theta=1/8`,

\[
\frac{\tau(D_n-C_0)}{b_n}
\le C
\exp\left\{
\sqrt{D_n-C_0}
-\frac14e^{\sqrt{D_n-C_0}}
+\frac18e^{\sqrt{A_n}}
\right\}
\longrightarrow0.
\tag{C028.33}
\]

The choice `1/8<1/4` leaves a fixed exponential margin.

Furthermore, with

\[
T_n=\sum_{j>n}b_j,
\tag{C028.34}
\]

we have

\[
\boxed{\frac{T_n}{b_n}\to0}
\tag{C028.35}
\]

because `P(A_{n+1})/P(A_n)->infinity`, so `b_{n+1}/b_n->0` super-exponentially and the tail is asymptotically dominated by its first term.

# 8. R19-I0084-C028A — universal entire all-orders counterexample

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

Let `K` be any probability measure supported in a lower-bounded half-line,

\[
\operatorname{supp}K\subset[\ell,\infty).
\tag{C028.36}
\]

Set

\[
h=\psi*K.
\tag{C028.37}
\]

Because `psi` is positive, bounded, `C^1`, integrable, and both `psi,psi'` vanish at infinity,

\[
h>0,\qquad h\in C^1,\qquad h'=\psi'*K,
\qquad h(x)\to0\ (x\to\pm\infty).
\tag{C028.38}
\]

Choose `x_0` with `h(x_0)>0`. Comparing with sufficiently remote points to the left and right and applying the mean-value theorem gives fixed numbers

\[
p<q_0
\tag{C028.39}
\]

such that

\[
\boxed{h'(p)>0>h'(q_0).}
\tag{C028.40}
\]

Let

\[
F=g*K.
\tag{C028.41}
\]

At the remote test point

\[
x_{n,s}=-A_n+s,
\qquad s\in\{p,q_0\},
\tag{C028.42}
\]

the active negative-center translate contributes exactly

\[
\frac{b_n}{2}h'(s).
\tag{C028.43}
\]

For the central term, all positive-center translates, and all negative-center translates with index `j<n`, the argument of `h'` is at most `-D_n+O_K(1)`. Since `K` is lower-bounded, their combined derivative magnitude is at most

\[
\tau(D_n-C_K)
\tag{C028.44}
\]

for a fixed constant `C_K`. By (C028.33), this is `o(b_n)`.

For the still-more-remote negative-center translates `j>n`, use

\[
\|h'\|_\infty\le\|\psi'\|_\infty.
\tag{C028.45}
\]

Their combined magnitude is at most

\[
\frac{\|\psi'\|_\infty}{2}T_n=o(b_n)
\tag{C028.46}
\]

by (C028.35). Consequently

\[
\boxed{
F'(x_{n,s})=\frac{b_n}{2}h'(s)+o(b_n),
\qquad s\in\{p,q_0\}.
}
\tag{C028.47}
\]

For all large `n`,

\[
F'(x_{n,p})>0,
\qquad
F'(x_{n,q_0})<0.
\tag{C028.48}
\]

For consecutive large indices,

\[
x_{n,q_0}<-A_{n-1}+p=x_{n-1,p}.
\tag{C028.49}
\]

Hence

\[
\boxed{
F'(x_{n,q_0})<0<F'(x_{n-1,p})
\quad\text{with}\quad x_{n,q_0}<x_{n-1,p}.
}
\tag{C028.50}
\]

A differentiable unimodal density cannot have a negative derivative at one point and a positive derivative at a later point to its right: a unimodal differentiable density is nondecreasing before a mode and nonincreasing after it. Therefore

\[
\boxed{g*K\text{ is nonunimodal}.}
\tag{C028.51}
\]

If `K` is supported in an upper-bounded half-line, reflect it. Since `g` is even, reflection preserves the conclusion.

Thus there exists ONE symmetric strictly positive entire probability density `g`, independent of `K`, satisfying every stretched-exponential moment (C028.28), such that ordinary convolution `g*K` is nonunimodal for **every** half-line-supported probability kernel `K`.

# 9. R19-I0084-C028B — frozen alpha=1/2 consequence

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

Let `L_t` be the positive classical alpha=`1/2` stable law in Hasebe--Ueda Section 5.2, let `F_t` be the positive free alpha=`1/2` stable law in the frozen arXiv-v2 sense, and let `check L_t`, `check F_t` be their reflected extremal endpoint laws. Every such time marginal is supported in a half-line.

The SINGLE density `g` from C028A satisfies, simultaneously for every `t>0`,

\[
\boxed{
 g*L_t,\quad g*F_t,\quad
 g*\check L_t,\quad g*\check F_t
 \text{ are all nonunimodal},
}
\tag{C028.52}
\]

while

\[
\boxed{
\int e^{c|x|^q}g(x)\,dx<\infty
\quad\forall c,q>0.
}
\tag{C028.53}
\]

In particular `g` satisfies the exact source `5/2` moment by an enormous margin. The endpoint obstruction is therefore not atomic, not merely smooth, not merely strip-analytic, not tied to any fixed finite stretched-exponential order, and not kernel-specific. It persists for one **entire, strictly positive, ultra-light, kernel-independent** initial density.

This strictly strengthens C026 and C027:

- C026: one strip-holomorphic density, all stretched-exponential orders;
- C027: entire density, any prescribed finite order ceiling;
- C028: one entire density, **all stretched-exponential orders simultaneously**.

# 10. Literature/prior-art check — 2026-09-20

Fresh bounded searches covered:

- exact `Hasebe Ueda Conjecture 5.5`, `arXiv:1710.08240`, later author work and citing/related unimodality papers;
- `entire density` / `real analytic density` + convolution + unimodality counterexample;
- `half-line kernel` + convolution + nonunimodality;
- the stable-process `2+alpha` moment threshold and later Hasebe/Ueda multiplicative work.

The search recovered the original Hasebe--Ueda paper, the later published ALEA formulation, earlier free-unimodality work, and later multiplicative-unimodality papers. I did not locate a primary theorem resolving the exact frozen arXiv-v2 ordinary-`*` statement or stating C028A's universal entire/all-orders half-line-kernel theorem. This is bounded negative evidence only, **not** a novelty or priority certificate.

The published ALEA wording is materially different from the frozen arXiv target: it says `mu*S_t` for a classical stable process and `mu boxplus T_t` for a free stable process. The frozen arXiv wording says ordinary `mu*S_t` even when `S_t` is a free stable law. This report remains inside the frozen scope assigned to R19.

# 11. Checks and audit posture

No finite arithmetic claim is introduced, so no checker was manufactured merely for bookkeeping. The theorem-sized claim is proved on the page. The key quantitative inequalities are (C028.19), (C028.28), (C028.33), (C028.35), and the derivative-sign reduction (C028.47)--(C028.50).

Retained independent evidence:

- `R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF` for the positive interior smoothing engine;
- narrower historical C010/P26 and half-stable checks remain preserved;
- no version-matching end-to-end P26 PASS for the full frozen arXiv ordinary-`*` package and no distinct second full-package PASS were located;
- C021--C028 remain self-proved / independent audit pending.

The neighboring R18 Hasebe--Ueda--Wang Problem 4.11 track is separately `PROVED / AUDIT-COMPLETE / PACKAGED`; it is a multiplicative-free problem and does not close or audit this frozen additive ordinary-`*` package.

Therefore repository closure is not claimed.

# 12. Model/scheduler control status

The operative implementation manifest still records no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guaranteed one-hour runtime field. Thus the requested `GPT-6 / maximum` remains prompt text only here; this report truthfully records **GPT-5.6 Sol / UNVERIFIED**.

The historical P26 `You cannot modify this task` event is also recorded in that manifest. Repository history later records successful P26 updates from an authorized context. The supported remedy is the owning/authorized context, supported permission/ownership repair or transfer, or platform support—not a bypass or duplicate schedule. Enforceable GPT-6/maximum would require explicit persisted model/reasoning fields plus trustworthy per-run runtime attestation in the scheduler/product/API surface.

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
  tried_moves: [1, 3, 18]
  move_note: "second-cycle reuses because all 30 were exhausted historically; preceding C027 triple was 20/4/30"
  new_claims:
    c028a: "one symmetric strictly positive entire density with all exp(c|x|^q) moments finite for every c,q>0 defeats ordinary convolution with every half-line-supported probability kernel"
    c028b: "the same single density defeats all four alpha=1/2 extremal classical/free stable endpoint laws at every t>0 under ordinary *"
  mechanism:
    exponent: "P(z)=cosh(sqrt(z))+cos(sqrt(z))=2 sum z^(2m)/(4m)! is even entire, P(x)~(1/2)e^(sqrt(|x|)) on R"
    centers: "A_(n+1)=A_n^4"
    weights: "b_n=eta exp[-P(A_n)/8]"
    key_gap: "sqrt(A_n-A_(n-1)-C)=sqrt(A_n)+o(1), so previous-gap leakage is o(b_n) while b_n still beats every exp(c A_n^q) moment cost"
  evidence:
    - "runs/R19/2026-09-20_09-39-59_UTC__i0084-entire-finite-order-universal-counterexample_c027_m20w4s30.md"
    - "Hasebe-Ueda arXiv:1710.08240v2, Conjecture 5.5"
    - "this report: complete C028A/B proof"
  audit_ids:
    c008: "R18-AUDIT-R19-I0084-C008-ABSTRACT-003=PASS_FULL_MATHEMATICAL_PROOF"
    frozen_package_p26: "NOT_LOCATED / version-matching end-to-end gate unfilled"
    frozen_package_second: "NOT_LOCATED / distinct end-to-end gate unfilled"
  remaining_obligation: "independent theorem-level review of C021-C028 and two version-matching end-to-end outside audits before repository closure; do not replace ordinary * by free convolution"
```
