Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. This was not GPT-6 at maximum, and I do not claim otherwise.

# P03-A analytic proof report — harmonic-tail/Stieltjes control of the escape tilt

**Status:** PROVED PARTIAL (new repository theorem candidate; not independently audited; no claim of external novelty; the full Lyons–Pemantle–Peres conjecture remains open).

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursive/derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`. The old D0047 history remains untouched. Canonical ownership was checked once: this is complementary research on P03, not a replacement of another owner's claim.

**Captured master immediately before write:** `2f9d17d4171a50d28515ece86224a794e43b9e22`.

## 1. Source convention, current baseline, and continuity

Let `nu` be the offspring variable. The original source problem is the biased nearest-neighbor walk on a supercritical Galton–Watson tree without leaves,

\[
P(\nu=0)=0,\qquad m=E\nu\in(1,\infty).
\]

Ben Arous--Fribergh--Sidoravicius use outward child bias `beta`; I use the reciprocal parent-bias parameter

\[
\lambda=1/\beta,
\]

so at a vertex with `k` children

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+k}.
\]

Increasing `lambda` points toward the root, so the conjectural sign is `ell'_lambda<=0` throughout the transient regime `0<lambda<m`.

Primary/current sources recovered for continuity:

* Ben Arous, Fribergh and Sidoravicius, arXiv:1111.5865 / CPAM 67 (2014), the old high-outward-bias theorem;
* Aidekon, arXiv:1111.4313 / PTRF 159 (2014), Theorem 1.1, giving the exact speed formula for `m in (1,infinity)` and `lambda` in the positive-speed regime;
* Bowditch and Tokushige, arXiv:1906.07913 and arXiv:2006.03433, differentiability / analyticity in ballistic regimes, without the missing sign;
* Song, Wang and Xiang, arXiv:1610.08151, published J. Appl. Probab. 62 (2025), 1044--1052. If the minimum offspring is `d>=2`, their source-uniform theorem gives strict parent-bias decrease for

\[
0\le\lambda\le
\theta_d:=\frac{d}{1+\sqrt{1-1/d}}.
\tag{1.1}
\]

A bounded fresh search on 20 September 2026 recovered the 2025 theorem and a 2026 deterministic-regular-tree paper, but no full-source resolution or checked theorem identical to the distribution-sensitive bounds below. This is bounded negative evidence only.

Repository continuity consumed rather than duplicated:

* P03-A `2026-09-20T0259Z__unbounded-support-mean-defect-extension.md` proved `M'<=U_d(lambda)(M-d)` and a finite-mean near-regular criterion using `M<=E nu`;
* P03-B `2026-09-20T032221Z__exact-backstep-law-and-backstep-only-debt.md` is the distinct coupling route and gives exact super-regeneration backstep laws; none of that coupling work is reproduced here;
* PROB10-06 `20260920T0348Z__joint_tilt_tail_rectangles_6c4e19a2.md` treats the special `{2,3}` family by type-conditioned child patterns; this report instead targets arbitrary support through a new analytic tail functional.

The fixed full-source metric remains

`R_full: 1 -> 1`.

The new goal is to remove the preceding **near-mean** restriction while retaining unbounded offspring support.

## 2. Inherited exact derivative reduction

Assume throughout the new theorem that

\[
P(\nu\ge d)=1,\qquad d\ge2,\qquad m=E\nu<\infty,
\tag{2.1}
\]

and initially `1<=lambda<d`.

Let `B` be the quenched escape probability from a descendant vertex before hitting its parent. Conditional on the current offspring number `n`, let `B_0,...,B_n` be iid copies of `B`, set

\[
S_n=\sum_{i=0}^n B_i,
\]

and define

\[
c_n(\lambda)
:=E\left[\frac{S_n}{(n+1)(\lambda-1+S_n)}\right].
\tag{2.2}
\]

With `p_n=P(nu=n)`, put

\[
C=\sum_{n\ge d}p_n c_n,
\qquad
\pi_n=\frac{p_n c_n}{C},
\qquad
M=\sum_{n\ge d}n\pi_n.
\tag{2.3}
\]

Aidekon's symmetrized formula gives

\[
\ell_\lambda=\frac{M-\lambda}{M+\lambda},
\qquad
\ell'_\lambda=
\frac{2(\lambda M'-M)}{(M+\lambda)^2}.
\tag{2.4}
\]

Writing

\[
g_n=-\partial_\lambda\log c_n,
\]

the previous P03-A reports established

\[
M'=-\operatorname{Cov}_\pi(\nu,g_\nu)
=\sum_{n<m}\pi_n\pi_m(m-n)(g_n-g_m),
\tag{2.5}
\]

and, for `1<=lambda<d`,

\[
0\le g_n\le
\frac{d-1}
{(d-\lambda)[\lambda-1+(n+1)(1-\lambda/d)]}.
\tag{2.6}
\]

In particular, with

\[
U_d(\lambda)
:=\frac{d-1}{(d-\lambda)(d-\lambda/d)},
\qquad
a_d(\lambda):=\lambda U_d(\lambda),
\tag{2.7}
\]

and `x:=M-d>=0`, the Gini bound from the previous run gives

\[
M'\le U_d(\lambda)(M-d)=U_d(\lambda)x,
\]
so

\[
\boxed{
\lambda M'-M\le (a_d(\lambda)-1)x-d.
}
\tag{2.8}
\]

The entire new argument is therefore about controlling the **tilted degree defect** `x=M-d` much more sharply than `x<=m-d`.

## 3. New lemma: two-sided Stieltjes bounds for every escape weight

For `1<=lambda<d`, the standard minimum-degree escape comparison gives

\[
1-\frac\lambda d\le B\le1.
\tag{3.1}
\]

Set

\[
b:=1-\lambda/d>0.
\]

Then conditional on degree `n`,

\[
(n+1)b\le S_n\le n+1.
\tag{3.2}
\]

For `lambda>=1`, the function

\[
\phi_\lambda(s)=\frac{s}{\lambda-1+s}
\]

is increasing on the relevant positive range. Therefore (2.2)--(3.2) imply the **pointwise-in-degree two-sided bound**

\[
\boxed{
\frac1{n+\kappa_\lambda}
\le c_n(\lambda)\le
\frac1{n+\lambda},
}
\tag{3.3}
\]

where

\[
\boxed{
\kappa_\lambda:=\frac{\lambda(d-1)}{d-\lambda}.
}
\tag{3.4}
\]

Indeed, the upper bound is

\[
c_n\le\frac1{n+1}\frac{n+1}{\lambda+n}=\frac1{n+\lambda}.
\]

For the lower bound,

\[
c_n\ge
\frac{b}{\lambda-1+(n+1)b}
=\frac{d-\lambda}{n(d-\lambda)+\lambda(d-1)}
=\frac1{n+\kappa_\lambda}.
\]

At `lambda=1`, both bounds coincide with the exact value `c_n=1/(n+1)`.

This is the main mechanism advance of the run: the escape tilt is trapped between two explicit **Stieltjes kernels** in the offspring degree.

## 4. Exact law-dependent defect certificate

Since

\[
x=M-d
=\frac{\sum_{n\ge d}(n-d)p_n c_n}{\sum_{n\ge d}p_n c_n},
\tag{4.1}
\]

(3.3) gives, at each fixed `lambda in [1,d)`,

\[
\boxed{
x\le Q_P(\lambda):=
\frac{E[(\nu-d)/(\nu+\lambda)]}
{E[1/(\nu+\kappa_\lambda)]}.
}
\tag{4.2}
\]

Combining with (2.8),

\[
\boxed{
\lambda M'-M
\le
(a_d(\lambda)-1)Q_P(\lambda)-d.
}
\tag{4.3}
\]

Thus any interval on which the right-hand side is negative is a rigorous monotonicity interval. This criterion uses only bounded transforms of the offspring law; the support may be arbitrarily large.

For a convenient interval certificate, fix `L<d` and define

\[
A_L:=a_d(L),\qquad
\kappa_L:=\frac{L(d-1)}{d-L}.
\tag{4.4}
\]

Also set

\[
H:= (d+1)E\left[\frac1{\nu+1}\right],
\qquad
J_L:=E\left[\frac1{\nu+\kappa_L}\right].
\tag{4.5}
\]

Because `(nu-d)/(nu+lambda)` decreases in `lambda`, `kappa_lambda` increases in `lambda`, and `a_d(lambda)` increases on `[1,d)`, for every `1<=lambda<=L` beyond the source-uniform point (where `a_d>=1`) we have

\[
Q_P(\lambda)
\le\frac{1-H}{J_L}.
\tag{4.6}
\]

Hence:

### Proposition 4.1 — Stieltjes-transform interval certificate

If

\[
\boxed{
(A_L-1)\frac{1-H}{J_L}<d,
}
\tag{4.7}
\]

then `ell'_lambda<0` for every `1<=lambda<=L`; combined with (1.1), the speed is strictly decreasing throughout `0<=lambda<=L`.

This already removes the old P03-A requirement that `E nu` be numerically close to `d`.

## 5. Closed-form harmonic-tail theorem

The Stieltjes denominator in (4.5) has a clean lower bound in terms of `H`. Since `kappa_L>=1` and `n>=d`,

\[
\frac{n+1}{n+\kappa_L}
\ge
\frac{d+1}{d+\kappa_L}.
\]

Averaging gives

\[
J_L
\ge
\frac{H}{d+\kappa_L}.
\tag{5.1}
\]

Moreover

\[
d+\kappa_L=\frac{d^2-L}{d-L}.
\tag{5.2}
\]

Therefore

\[
x\le
\frac{d^2-L}{d-L}\frac{1-H}{H}
\qquad(1\le\lambda\le L).
\tag{5.3}
\]

Substitution into (2.8) shows that it is enough to require

\[
H>
\rho_d(L):=
\frac{2Ld^2-d^3-L^2}{L^2(d-1)}.
\tag{5.4}
\]

The algebra is exact: if

\[
K_L:=(A_L-1)\frac{d^2-L}{d-L},
\]

then

\[
K_L=\frac{2Ld^2-d^3-L^2}{(d-L)^2},
\qquad
K_L+d=\frac{L^2(d-1)}{(d-L)^2},
\]

so `K_L(1-H)/H<d` is precisely (5.4).

Solving `H=rho_d(L)` for the smaller root gives the closed endpoint

\[
\boxed{
\Lambda_d(H)
:=
\frac{d}
{1+\sqrt{(1-1/d)(1-H)}}.
}
\tag{5.5}
\]

Observe that

\[
\Lambda_d(0)=\theta_d,
\qquad
\Lambda_d(1)=d,
\tag{5.6}
\]

and `Lambda_d(H)` is strictly increasing in `H`.

### Theorem 5.1 — explicit law-dependent extension for every finite-mean minimum-degree law

Assume (2.1) and define

\[
H=(d+1)E[(\nu+1)^{-1}]\in(0,1].
\]

If `H<1`, then

\[
\boxed{
\ell'_\lambda<0
\quad\text{for every }1\le\lambda<\Lambda_d(H),
}
\tag{5.7}
\]

and, using the published theorem below `theta_d`, the speed is strictly decreasing throughout

\[
\boxed{
0\le\lambda\le\Lambda_d(H).
}
\tag{5.8}
\]

If `H=1`, then `nu=d` almost surely, so the tree is regular and the exact speed `(d-lambda)/(d+lambda)` is strictly decreasing on the full transient interval `0<=lambda<d`.

#### Why this is a genuine enlargement of the preceding P03-A theorem

The previous unbounded-support theorem controlled the tilt by `M<=E nu`, hence required the **mean** to be close enough to `d` for a specified post-`theta_d` interval. Theorem 5.1 instead depends on the bounded harmonic-tail statistic `H`; a law can have a very large mean and still have `H` close to one. Thus this theorem covers high-variance offspring laws that the preceding mean-defect criterion does not.

Also, for every fixed finite-mean law with minimum degree `d>=2`, `H>0`, so (5.5) gives an explicit law-dependent endpoint strictly beyond the source-uniform `theta_d` unless the law is already regular (where the full result is elementary).

No claim is made that this is externally novel; it is a new proved partial result in the repository pending independent review.

## 6. Clean corollaries

Because

\[
H\ge P(\nu=d),
\tag{6.1}
\]

Theorem 5.1 immediately yields simple tail-insensitive criteria.

### Minimum degree 2

For `d=2`,

\[
\rho_2(3/2)=\frac79,
\qquad
\rho_2(7/4)=\frac{47}{49},
\qquad
\rho_2(9/5)=\frac{79}{81}.
\]

Hence, with arbitrary finite-mean tail above degree 2,

\[
P(\nu=2)>\frac79
\Longrightarrow
\ell_\lambda\text{ strictly decreases on }[0,3/2],
\tag{6.2}
\]

and

\[
P(\nu=2)>\frac{47}{49}
\Longrightarrow
\ell_\lambda\text{ strictly decreases on }[0,7/4].
\tag{6.3}
\]

### Minimum degree 3

For `d=3`,

\[
\rho_3(2)=\frac58,
\qquad
\rho_3(5/2)=\frac{47}{50}.
\]

Thus, with arbitrary finite-mean tail above degree 3,

\[
P(\nu=3)>\frac58
\Longrightarrow
\ell_\lambda\text{ strictly decreases on }[0,2].
\tag{6.4}
\]

These are not bounded-support statements.

## 7. High-variance worked example not covered by the old mean criterion

Take

\[
P(\nu=2)=\frac{24}{25},
\qquad
P(\nu=100)=\frac1{25}.
\tag{7.1}
\]

Then

\[
E\nu=\frac{148}{25}=5.92,
\]

so the preceding P03-A mean-defect theorem cannot reach `L=7/4` (its mean threshold there is `112/47 approximately 2.383`).

But

\[
H=3E[(\nu+1)^{-1}]
=\frac{2427}{2525}
>\frac{47}{49}.
\]

Hence Theorem 5.1 proves strict speed decrease through `lambda=7/4`.

The sharper Stieltjes certificate (4.7) gives a quantitative check. At `L=7/4`,

\[
A_L=\frac{56}{9},
\qquad
\kappa_L=7,
\qquad
J_L=E[(\nu+7)^{-1}]=\frac{859}{8025},
\]

and

\[
d-(A_L-1)\frac{1-H}{J_L}
=\frac{27712}{260277}>0.
\tag{7.2}
\]

Consequently, on `1<=lambda<=7/4`,

\[
\lambda M'-M\le-\frac{27712}{260277}.
\]

Using `M-d<= (1-H)/J_L =31458/86759` gives the explicit uniform derivative certificate

\[
\boxed{
\ell'_\lambda
\le
-\frac{76936493056}{6110845095267}
<-1.25\times10^{-2}
}
\tag{7.3}
\]

on that interval.

This example is useful because the improvement is not caused by a small mean; it comes from controlling how the escape tilt discounts the rare very-high-degree tail.

## 8. What remains open and the next analytic attack

The full-source metric is unchanged:

`R_full: 1 -> 1`.

The new obligation ledger is:

1. **DONE:** exact two-sided Stieltjes envelopes (3.3) for `c_n`;
2. **DONE:** pointwise law-dependent defect certificate (4.2)--(4.3);
3. **DONE:** closed harmonic-tail endpoint (5.5), removing the prior near-mean restriction for minimum degree `d>=2`;
4. **OPEN:** cross the deterministic barrier `lambda=d` for nonregular laws with mean `m>d`;
5. **OPEN:** handle the original minimum-offspring-one case, where the deterministic escape lower bound used in (3.1) gives no positive room at `lambda>=1`;
6. **OPEN:** full monotonicity on every `0<lambda<m`.

The precise obstruction is that both the inherited logarithmic escape sensitivity bound (2.6) and the deterministic lower escape comparison (3.1) become singular/useless at `lambda=d`. Repeating the same `U_d` envelope will not solve this.

### Next attack

Use the **averaged** escape recursion instead of the deterministic minimum-degree floor. For every `lambda>1`, regardless of a positive deterministic lower bound, `S_n<=n+1` gives

\[
\frac{S_n}{\lambda-1+S_n}
\ge\frac{S_n}{\lambda+n},
\]
so if `b_lambda:=E B`, then

\[
\boxed{
c_n(\lambda)\ge\frac{b_\lambda}{n+\lambda}.}
\tag{8.1}
\]

The next run should pair (8.1) with a **distribution-averaged logarithmic sensitivity estimate** for `g_n`, derived from the fixed-point recursion for `(B,-B')`, rather than the pointwise factor `(d-lambda)^{-1}`. If that succeeds, the same Stieltjes covariance framework can in principle continue beyond `lambda=d` whenever `b_lambda>0`, which is exactly the missing analytic bridge for nonregular laws with `m>d`.

P03-B's backstep law is complementary evidence about the same difficult regime but is not duplicated here.

## 9. Self-checks performed

The following algebraic identities were checked exactly before writing:

* `(A_L-1)(d^2-L)/(d-L)=(2Ld^2-d^3-L^2)/(d-L)^2`;
* adding `d` to the preceding coefficient gives `L^2(d-1)/(d-L)^2`;
* solving the resulting quadratic gives exactly (5.5);
* the rational thresholds in Section 6 and the fractions in Section 7 reduce exactly as printed.

These are self-checks only. Independent proof review is deliberately deferred under the owner progress-first directive and does not freeze this research slot.
