# HARD7-04 — barely-supercritical configuration-model duality: parameter reduction and boundary obstruction

**Status:** self-check / route theorem only. This does not solve the source's second-largest-component problem and makes no novelty claim for the branching-process algebra or fixed-set matching lemma.

## 1. Setup

Let `p_{n,k}` be a degree law (or the empirical law of a deterministic degree sequence), with mean `mu_n>0`. Let `X_n=D_n^*-1` be the size-biased excess degree,

\[
\mathbb P(X_n=j)=\frac{(j+1)p_{n,j+1}}{\mu_n},
\]

and let

\[
g_n(s)=\mathbb E[s^{X_n}].
\]

Assume the barely-supercritical regime

\[
g_n'(1)=\mathbb E X_n=1+\varepsilon_n,\qquad \varepsilon_n\downarrow0.
\]

Assume also that `X_n` converges in law to a nondegenerate critical integer-valued law `X`, and that

\[
\kappa_n:=\mathbb E[X_n(X_n-1)]\longrightarrow\kappa\in(0,\infty).
\tag{1.1}
\]

For the finite-third-moment configuration-model setting, (1.1) follows from convergence of the third degree moments together with convergence of the positive mean degree. Nondegeneracy excludes the limiting `D\equiv2` / `X\equiv1` boundary.

Let `xi_n<1` be the extinction probability of the supercritical Galton--Watson process with offspring `X_n`, and put

\[
q_n:=1-\xi_n.
\]

The ideal dual degree law is

\[
p^{\mathrm{dual}}_{n,k}
=\frac{p_{n,k}\xi_n^k}{G_{0,n}(\xi_n)},
\qquad
G_{0,n}(s)=\sum_k p_{n,k}s^k.
\tag{1.2}
\]

Its excess mean is

\[
\nu_n^{\mathrm{dual}}
=\frac{\sum k(k-1)p_{n,k}\xi_n^k}
       {\sum k p_{n,k}\xi_n^k}
=g_n'(\xi_n).
\tag{1.3}
\]

The frozen admission metric is

\[
\Delta_{\mathrm{dual},n}
:=\left|\frac{1-\nu_n^{\mathrm{dual}}}{\varepsilon_n}-1\right|.
\tag{1.4}
\]

## 2. Route theorem: the dual drift matches the original drift to first order

**Proposition 2.1.** Under the assumptions above,

\[
q_n\sim\frac{2\varepsilon_n}{\kappa},
\qquad
1-\nu_n^{\mathrm{dual}}=\varepsilon_n+o(\varepsilon_n),
\tag{2.1}
\]

and therefore

\[
\boxed{\Delta_{\mathrm{dual},n}\to0.}
\tag{2.2}
\]

### Proof

First `q_n\to0`. If not, pass to a subsequence on which `xi_n=1-q_n\to xi<1`. The pgfs converge pointwise on `[0,1]` to the pgf `g` of the critical limiting offspring law. Since `xi_n=g_n(xi_n)`, continuity gives `xi=g(xi)`. But a nondegenerate critical Galton--Watson law becomes extinct almost surely, so `1` is its only fixed point in `[0,1]`. This contradicts `xi<1`.

Next we need a uniform second-order expansion at the moving point `1-q_n`. Since `\kappa_n\to\kappa<\infty`, the variables `X_n(X_n-1)` are uniformly integrable in the finite-third-moment setting. Hence, because `q_n\to0`,

\[
\sup_{s\in[1-q_n,1]}
|g_n''(s)-\kappa|\to0.
\tag{2.3}
\]

Indeed, truncate `X_n` at a fixed `K`; on the finite part `s^{X_n-2}\to1` uniformly as `q_n\to0`, while the tail is uniformly controlled by `X_n(X_n-1)`.

Taylor's formula with integral remainder gives

\[
\begin{aligned}
g_n(1-q_n)
&=g_n(1)-q_ng_n'(1)
  +\int_{1-q_n}^{1}(t-(1-q_n))g_n''(t)\,dt\\
&=1-(1+\varepsilon_n)q_n
  +\frac{\kappa+o(1)}2q_n^2.
\end{aligned}
\tag{2.4}
\]

Using the extinction fixed-point identity `g_n(1-q_n)=1-q_n` and dividing by `q_n>0`,

\[
\varepsilon_n=\frac{\kappa+o(1)}2q_n,
\]

which proves the first relation in (2.1).

For the dual drift,

\[
\begin{aligned}
g_n'(1)-g_n'(1-q_n)
&=\int_{1-q_n}^{1}g_n''(t)\,dt\\
&=(\kappa+o(1))q_n\\
&=2\varepsilon_n+o(\varepsilon_n).
\end{aligned}
\tag{2.5}
\]

Since `g_n'(1)=1+\varepsilon_n`,

\[
\nu_n^{\mathrm{dual}}=g_n'(\xi_n)
=1-\varepsilon_n+o(\varepsilon_n),
\]

which proves (2.1)--(2.2). `square`

### Configuration-model interpretation

Equation (2.2) says that at the level of the ideal branching-process dual, deleting the supercritical survival mass transforms the distance `+epsilon_n` from criticality into the subcritical distance `-epsilon_n` to first order. This is the parameter identity one would need before a barely-supercritical second-largest component can be reduced to an appropriate barely-subcritical largest-component theorem. It is **not** the graph-level duality statement: the random residual empirical degree sequence still has to be controlled at the required precision.

## 3. B2 boundary attack: the nondegeneracy hypothesis is structural

The first-order coefficient in Proposition 2.1 fails if the critical limit degenerates to degree two.

For `0<a<1/2`, define a degree law on `{1,2,4}` by

\[
p_1=\frac{4a}{2+a},\qquad
p_2=\frac{2(1-2a)}{2+a},\qquad
p_4=\frac{a}{2+a}.
\tag{3.1}
\]

Its size-biased excess offspring law is exactly

\[
\mathbb P(X_a=0)=a,\qquad
\mathbb P(X_a=1)=1-2a,\qquad
\mathbb P(X_a=3)=a,
\tag{3.2}
\]

so

\[
\mathbb E X_a=1+a.
\]

Thus the supercriticality parameter is `epsilon=a`. Its pgf satisfies

\[
g_a(s)-s
=a(s-1)(s^2+s-1).
\tag{3.3}
\]

Besides `1`, the extinction root is the constant

\[
r=\frac{\sqrt5-1}{2},
\tag{3.4}
\]

independent of `a`. Therefore

\[
\frac{1-g_a'(r)}a
=2-3r^2
=\frac{3\sqrt5-5}{2}
\ne1.
\tag{3.5}
\]

Consequently

\[
\Delta_{\mathrm{dual}}
\to 1-\frac{3\sqrt5-5}{2}>0,
\]

rather than zero.

At the same time

\[
p_2\to1,
\qquad
\mathbb E[D_a^3]\to8<\infty.
\tag{3.6}
\]

Thus finite third moments alone do not force first-order drift reflection; the excluded `D\equiv2` boundary is real, not cosmetic. This does **not** refute the source question because the source's critical configuration-model hypotheses exclude this degenerate limit.

The exact finite algebra in (3.1)--(3.6) is checked by

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T0838Z__vdh_duality_boundary_exact.py`

with archived output ending `ALL_EXACT_CHECKS_PASS = True`.

## 4. B19 algorithmic reformulation: exact deletion lemma for a fixed component

The configuration model is a uniform perfect matching of its half-edges. This gives an exact finite decomposition which isolates the remaining graph-level difficulty.

**Lemma 4.1 (fixed-component deletion).** Fix a deterministic vertex set `U`. Conditional on the event that no matching edge crosses from `U` to `U^c`, the restriction of the matching to the half-edges of `U^c` is a uniform perfect matching. The same conclusion holds after additionally conditioning that the graph induced by `U` is connected. Hence, conditional on `U` being a connected component, the graph on `U^c` is exactly the configuration model with the original degrees restricted to `U^c`.

### Proof

Let `H_U` and `H_{U^c}` be the two half-edge sets. Under the no-crossing event every admissible global perfect matching is uniquely a pair `(M_U,M_{U^c})`, where each coordinate is a perfect matching of the corresponding half-edge set. Because the original law assigns equal mass to every global perfect matching, every pair `(M_U,M_{U^c})` has the same conditional mass. Marginalizing over `M_U` makes `M_{U^c}` uniform. Connectivity of the induced graph on `U` depends only on `M_U`, so conditioning on it changes only the `M_U` factor and leaves the uniform `M_{U^c}` marginal unchanged. `square`

### Why this does not yet prove source duality

If `U` is declared to be **the largest** component, one also conditions on the complement having no component of size at least `|U|`; that condition depends on `M_{U^c}` and destroys the literal factorization. More importantly, for the random giant `U=C_1`, the residual degree histogram itself is random.

The source question can therefore be split into two sharp obligations:

1. **residual-law obligation:** prove that after deleting the giant, the empirical residual degree law is close, at barely-supercritical precision, to the ideal tilted law (1.2), with dual drift `1-\varepsilon_n+o(\varepsilon_n)`;
2. **largest-conditioning obligation:** show that the extra conditioning implicit in selecting the largest component is asymptotically irrelevant for the scale of the largest residual component.

Once these are available, the second-largest component of the original graph becomes the largest component of a barely-subcritical residual configuration model, and sharp subcritical technology can be applied under the exact residual assumptions.

## 5. Checkpoint

This iteration establishes the parameter-level half of the hoped-for discrete duality and identifies a genuine boundary obstruction. It does **not** establish concentration of the random residual histogram, the scale of `C_2`, or a source closure. The highest-value next mathematical attack is the residual-law obligation, not another finite matching checker.
