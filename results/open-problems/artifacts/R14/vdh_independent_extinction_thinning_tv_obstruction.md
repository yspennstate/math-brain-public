# R14 — independent extinction thinning is not the full marginal dual law

**Status:** rigorous obstruction / self-check from published bounded-degree asymptotics; **not** a source refutation and **not** a novelty claim.

## 1. Why this note is needed

The current R14 target is van der Hofstad's finite-third-moment barely-supercritical configuration-model question asking for the scaling of the second-largest component and whether a discrete duality principle survives after deleting the giant.

The previous R14 stuck-recovery report proposed, as a deliberately stronger bounded-support test case, replacing the random residual degree profile by an independently extinction-thinned profile

\[
\widehat N_{n,d}\sim \operatorname{Bin}(n_d,z_n^d),
\]

followed by a fresh configuration model, with parity conditioning as needed.  This note records a decisive limitation of that proposal: **independent extinction thinning cannot approximate the full marginal law of the actual complement, even in the classical uniformly bounded-degree regime.**  A one-dimensional observable, the number of retained vertices, already has incompatible fluctuation scale.

This does not contradict the useful quenched duality established on the R14 route: conditional on the *realized* residual degree sequence, the complement pairing can be asymptotically fresh.  It also does not preclude comparison of selected coarse observables such as the leading second-largest-component scale.

## 2. Published bounded-degree input

Use Oliver Riordan, *The phase transition in the configuration model*, Combin. Probab. Comput. 21 (2012), 265--299, arXiv:1104.0613, Theorem 1.1.

Let `d=d_n` satisfy Riordan's uniformly bounded-degree assumptions and write

\[
\lambda_n=1+\varepsilon_n,
\qquad \varepsilon_n\downarrow0,
\qquad n\varepsilon_n^3\to\infty.
\]

Let `z_n` be the smallest solution of the usual size-biased extinction equation and

\[
\rho_n=1-\sum_d p_{n,d}z_n^d.
\]

For the configuration multigraph, Riordan proves

\[
\frac{L_{1,n}-\rho_n n}{\sigma_n}\Longrightarrow N(0,1),
\qquad
\sigma_n^2\sim 2\mu_{1,n}\varepsilon_n^{-1}n,
\tag{2.1}
\]

and also

\[
\rho_n\asymp\varepsilon_n.
\tag{2.2}
\]

In fact his formula is

\[
\rho_n\sim \frac{2\mu_{1,n}^2}{\mu_{3,n}}\varepsilon_n.
\]

## 3. The independent-thinning proxy

Let

\[
R_n:=n-L_{1,n}
\]

be the number of vertices outside the actual giant.  Define an ideal independently thinned retained set by keeping each degree-`d_i` vertex independently with probability `z_n^{d_i}`.  Let

\[
\widehat R_n:=\sum_{i=1}^n B_i,
\qquad
B_i\sim\operatorname{Bernoulli}(z_n^{d_i})
\]

independently.

The means agree **exactly**:

\[
\mathbb E\widehat R_n
=\sum_i z_n^{d_i}
=n\sum_d p_{n,d}z_n^d
=n(1-\rho_n).
\tag{3.1}
\]

But the fluctuation scales do not.  Since `0<=z_n^{d_i}<=1`,

\[
\operatorname{Var}(\widehat R_n)
=\sum_i z_n^{d_i}(1-z_n^{d_i})
\le \sum_i(1-z_n^{d_i})
=n\rho_n
=O(n\varepsilon_n).
\tag{3.2}
\]

By contrast, (2.1) gives

\[
\operatorname{Var}(R_n)
\sim 2\mu_{1,n}\frac n{\varepsilon_n}
\tag{3.3}
\]

at the CLT scale.

Thus the standard deviations differ by an asymptotic factor of order `1/epsilon_n`.

## 4. Total-variation obstruction

### Proposition 4.1

Under the bounded-degree weakly-supercritical assumptions above,

\[
\boxed{
 d_{\rm TV}\!\left(\mathcal L(R_n),\mathcal L(\widehat R_n)\right)\longrightarrow1.
}
\tag{4.1}
\]

Consequently any graph-valued law whose measurable state includes the retained vertex count also has total-variation distance tending to one from the corresponding independently extinction-thinned graph law.

### Proof

Put

\[
m_n=n(1-\rho_n)
\]

and consider the event

\[
A_n:=\{|x-m_n|\le\sqrt n\}.
\]

For the independently thinned variable, (3.2) and Chebyshev give

\[
\mathbb P(\widehat R_n\notin A_n)
\le \frac{\operatorname{Var}(\widehat R_n)}n
=O(\varepsilon_n)\to0.
\tag{4.2}
\]

For the actual complement,

\[
R_n-m_n=-(L_{1,n}-\rho_n n).
\]

By (2.1), with

\[
\sigma_n\asymp\sqrt{n/\varepsilon_n},
\]

we have

\[
\frac{R_n-m_n}{\sigma_n}\Longrightarrow N(0,1),
\]

while

\[
\frac{\sqrt n}{\sigma_n}=O(\sqrt{\varepsilon_n})\to0.
\]

Since the limiting normal distribution has no atom at zero,

\[
\mathbb P(R_n\in A_n)\to0.
\tag{4.3}
\]

Therefore

\[
d_{\rm TV}(\mathcal L(R_n),\mathcal L(\widehat R_n))
\ge
|\mathbb P(R_n\in A_n)-\mathbb P(\widehat R_n\in A_n)|
\to1.
\]

As total variation is at most one, (4.1) follows.  `square`

## 5. What this does and does not say about discrete duality

The obstruction is to a **marginal iid-thinning law**, not to the source's second-largest-component duality principle.

Riordan's own bounded-degree theorem already shows this distinction.  His Theorem 1.2 gives the sharp barely-subcritical extreme-component law

\[
L_1
=\delta_n^{-1}\left(
\log\Lambda_n-\frac52\log\log\Lambda_n+O_p(1)
\right),
\qquad \Lambda_n=n\varepsilon_n^3,
\tag{5.1}
\]

with

\[
\delta_n\sim\frac{\varepsilon_n^2\mu_{1,n}}{2\mu_{3,n}}.
\]

Immediately after Theorem 1.2 he states that the supercritical `L_2` bound is obtained by applying that theorem to what remains after deleting the largest component, with the parameters of the **dual distribution**.  Thus the bounded-degree version of the source phenomenon is prior art, even though the full residual profile is not iid extinction thinning in total variation.

The correct hierarchy is therefore:

1. **quenched pairing duality:** condition on the actual residual degree sequence; the remainder behaves as a fresh configuration model on that sequence;
2. **extreme-observable duality:** show that the residual sequence lies in a class on which the subcritical extreme-component theorem is stable;
3. **full marginal profile law:** much stronger, and the naive independent-thinning candidate is false by Proposition 4.1.

The R14/HARD7 finite-third-moment route should target levels 1--2, not level 3.

## 6. Two route corrections for the next run

First, the bounded-support special case selected in the previous R14 stuck report is **KNOWN**, not a fresh special case: van der Hofstad's 2026 notes explicitly say that Riordan had already carefully analyzed both barely sub- and barely supercritical regimes for uniformly bounded degrees, and Riordan's Theorems 1.1--1.2 contain the corresponding second-component/dual-distribution mechanism.

Second, a point process cut only at a fixed `a epsilon_n^{-2}` scale is not centered at the nondegenerate extreme scale.  Riordan's formula (5.1) shows that the largest subcritical component carries an additional `log(n epsilon_n^3)` factor.  Any stronger finite-third-moment distributional target should therefore be centered at the logarithmic extreme scale (with the `-(5/2) log log` correction if one seeks the bounded-degree-level refinement), not at a fixed multiple of `epsilon_n^{-2}`.

## 7. Constant cross-check with the finite-third-moment route

At criticality let `mu_r=E[(D)_r]`.  The R14/HARD7 constant

\[
R_*:=\frac{\mathbb E[D(D-2)^2]}{\mathbb ED}
\]

matches Riordan's bounded-degree constant because

\[
\mathbb E[D(D-2)^2]
=\mu_3-\mu_2+\mu_1
=\mu_3
\]

when criticality gives `mu_2=mu_1`.  Hence

\[
R_*=\frac{\mu_3}{\mu_1}
\]

and the existing leading candidate

\[
\frac{2R_*}{\varepsilon_n^2}\log(n\varepsilon_n^3)
\]

reduces exactly to Riordan's bounded-degree leading coefficient.

This is a consistency check, not an independent proof of the finite-third-moment theorem.
