Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0032 — exact boundary germ, certified arbitrary-index inversion, and a rational/irrational holonomicity dichotomy

Target: Charles Bordenave and Djalil Chafaï, *Around the circular law*, Probability Surveys 9 (2012), arXiv:1109.3343v4, request to identify the heavy-tailed limiting law `mu_alpha` explicitly; scalar characterization from Charles Bordenave, Pietro Caputo and Djalil Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*, CMP 307 (2011), arXiv:1006.1713.

Date of this derivation: 2026-09-19 UTC.

This artifact executes the precommitted Section-B methods **B4 / B19 / B23**.  It does not claim source closure or novelty from search failure.  The fixed campaign metric `M_jet` was already saturated at `+infinity` before this run, so none of the global structural progress below changes that metric.

## 1. Starting equations

Put

\[
\beta=\alpha/2\in(0,1),\qquad
c_\beta=\Gamma(1-\beta),\qquad
C_\beta=\Gamma(1-\beta)\Gamma(1+\beta).
\]

Let `S,S'` be iid positive beta-stable variables normalized by

\[
\mathbb E e^{-tS}=e^{-c_\beta t^\beta}.
\]

For squared radius `r=|z|^2`, the preceding C0032 runs introduced

\[
F_\beta(a)=\mathbb E(S'+a/S)^{-\beta},
\qquad
r(a)=aF_\beta(a)^{1/\beta},
\tag{1.1}
\]

and proved the exact squared-radius tail identity

\[
q_\beta(a):=1-M(r(a))=C_\beta F_\beta(a).
\tag{1.2}
\]

Equivalently, if

\[
T=SS',\qquad U=T^{-1},
\]

then

\[
\boxed{q_\beta(a)=\mathbb E\frac{T}{a+T}=\mathbb E\frac1{1+aU}.}
\tag{1.3}
\]

The positive stable negative moments are explicit.  For every `x>0`,

\[
\mathbb E S^{-x}
=\frac1{\Gamma(x)}\int_0^\infty t^{x-1}e^{-c_\beta t^\beta}\,dt
=\frac{\Gamma(1+x/\beta)}{\Gamma(1+x)c_\beta^{x/\beta}}.
\tag{1.4}
\]

Hence

\[
\boxed{
\mu_n:=\mathbb E U^n
=\left[
\frac{\Gamma(1+n/\beta)}{\Gamma(n+1)c_\beta^{n/\beta}}
\right]^2,
\qquad n=0,1,2,\ldots .
}
\tag{1.5}
\]

These identities are the only probabilistic input needed below.

---

# 2. Method B4 — prove a weaker statement completely: the exact boundary germ

Instead of trying again to invert the full all-radius law, first determine exactly what kind of function `q_beta(a)` is at the solvable endpoint `a=0`.

## Theorem 2.1 — exact finite Taylor formula with a signed global remainder

For every integer `N>=0` and every `a>=0`,

\[
\boxed{
q_\beta(a)
=\sum_{n=0}^{N}(-1)^n\mu_n a^n
+(-1)^{N+1}a^{N+1}
\mathbb E\frac{U^{N+1}}{1+aU}.
}
\tag{2.1}
\]

Consequently

\[
\boxed{
\left|q_\beta(a)-\sum_{n=0}^{N}(-1)^n\mu_n a^n\right|
\le \mu_{N+1}a^{N+1},
}
\tag{2.2}
\]

and for every `m>=0`,

\[
\boxed{
\sum_{n=0}^{2m+1}(-1)^n\mu_n a^n
\le q_\beta(a)
\le
\sum_{n=0}^{2m}(-1)^n\mu_n a^n.
}
\tag{2.3}
\]

### Proof

For every `x>=0`, the finite geometric identity is exact:

\[
\frac1{1+x}
=\sum_{n=0}^{N}(-x)^n+rac{(-x)^{N+1}}{1+x}.
\]

Set `x=aU` and take expectations.  All moments in (1.5) are finite.  This gives (2.1).  Since `0<(1+aU)^{-1}<=1`, (2.2) follows, and the remainder sign gives (2.3).  No exchange of an infinite series and expectation is used.  QED.

## Corollary 2.2 — `q_beta` is C-infinity at zero but never analytic there

For every `n>=0`,

\[
\boxed{q_\beta^{(n)}(0+)=(-1)^n n!\mu_n.}
\tag{2.4}
\]

Thus the formal Taylor coefficients are

\[
\boxed{
a_n:=\frac{q_\beta^{(n)}(0+)}{n!}
=(-1)^n
\left[
\frac{\Gamma(1+n/\beta)}{\Gamma(n+1)c_\beta^{n/\beta}}
\right]^2.
}
\tag{2.5}
\]

Their exact ratio obeys

\[
\left|\frac{a_{n+1}}{a_n}\right|
=c_\beta^{-2/\beta}
\frac{\Gamma(1+(n+1)/\beta)^2}
{\Gamma(1+n/\beta)^2(n+1)^2}
\sim
(\beta c_\beta)^{-2/\beta}n^{2/\beta-2}.
\tag{2.6}
\]

Because `0<beta<1`, the exponent `2/beta-2` is positive, so the ratio tends to infinity.  Hence the formal Taylor series has radius of convergence zero for every heavy-tail index under consideration.

This is not a contradiction with smoothness: (2.1) proves a genuine Poincare asymptotic expansion to every finite order while also proving that the full formal series diverges at every nonzero `a`.

## Corollary 2.3 — exact Gevrey order

Let

\[
\boxed{\sigma_\beta=\frac2\beta-2.}
\tag{2.7}
\]

Then the formal germ `sum a_n a^n` has exact Gevrey order `sigma_beta`: for every `epsilon>0`, its coefficients satisfy a bound of the form

\[
|a_n|\le A_\epsilon B_\epsilon^n(n!)^{\sigma_\beta+\epsilon},
\]

while no bound with exponent strictly smaller than `sigma_beta` is possible.

Indeed, Stirling applied to (2.5) gives

\[
\log|a_n|
=\sigma_\beta\log(n!)+O(n),
\tag{2.8}
\]

and (2.6) gives the same order directly.

**B4 outcome.**  The all-radius source problem remains open, but the endpoint has now been classified completely: `q_beta` is smooth and nonanalytic at `a=0`, its full formal germ and signed remainder are exact, and its Gevrey order is `2/beta-2`.

---

# 3. Method B19 — make it an algorithm: certified evaluation and inversion for every index

The previous runs removed the PWIT self-consistency algebraically.  Here the remaining one-dimensional representation is turned into a deterministic validated algorithm with an exponentially small contour tail.

## 3.1 Exact Mellin transform of the radial tail coordinate

For `0<Re(s)<beta`, use (1.3), Tonelli, and `a=Tu`:

\[
\begin{aligned}
\int_0^\infty a^{s-1}q_\beta(a)\,da
&=\mathbb E\int_0^\infty a^{s-1}\frac{T}{a+T}\,da\\
&=\mathbb E[T^s]\int_0^\infty\frac{u^{s-1}}{1+u}\,du.
\end{aligned}
\]

For `0<Re(s)<beta`,

\[
\mathbb E S^s
=c_\beta^{s/\beta}
\frac{\Gamma(1-s/\beta)}{\Gamma(1-s)},
\]

and Euler's beta integral gives

\[
\int_0^\infty\frac{u^{s-1}}{1+u}\,du
=\Gamma(s)\Gamma(1-s).
\]

Therefore

\[
\boxed{
\widehat q_\beta(s)
=c_\beta^{2s/\beta}
\frac{\Gamma(s)\Gamma(1-s/\beta)^2}{\Gamma(1-s)},
\qquad 0<\Re s<\beta.
}
\tag{3.1}
\]

Mellin inversion gives, for any fixed `c in (0,beta)`,

\[
\boxed{
q_\beta(a)
=\frac1{2\pi}
\int_{-\infty}^{\infty}
\widehat q_\beta(c+it)a^{-c-it}\,dt.
}
\tag{3.2}
\]

This formula contains only Gamma functions and elementary operations.  There is no stable random variable and no fixed-point unknown left to solve numerically.

## 3.2 An exponentially decaying certified contour

Take the symmetric line

\[
c=\beta/2.
\]

Stirling's formula on fixed vertical lines, with its standard explicit remainder bound, gives

\[
\boxed{
|\widehat q_\beta(\beta/2+it)|
\le K_\beta(1+|t|)^{\beta-1}e^{-\pi|t|/\beta}
}
\tag{3.3}
\]

for a finite constant `K_beta` depending only on beta.  This exponent can also be checked term by term: `Gamma(s)` contributes `e^{-pi|t|/2}`, the two `Gamma(1-s/beta)` factors contribute `e^{-pi|t|/beta}`, and `1/Gamma(1-s)` contributes `e^{+pi|t|/2}`, leaving exactly `e^{-pi|t|/beta}`.  The power on this line is `beta-1`.

For certification, one does not need to guess `K_beta`: choose a finite `T0`; bound the Gamma factors on `1<=|t|<=T0` by complex ball/interval evaluation; beyond `T0`, use an explicit Stirling remainder.  Taking the maximum of those two validated bounds produces a rigorous finite `K_beta`.  This is a finite deterministic procedure for every fixed beta in `(0,1)`.

Define the truncated contour

\[
q_{\beta,T}(a)
=\frac{a^{-\beta/2}}{2\pi}
\int_{-T}^{T}
\widehat q_\beta(\beta/2+it)e^{-it\log a}\,dt.
\tag{3.4}
\]

For `T>=1`, (3.3) gives the explicit tail bound

\[
\boxed{
|q_\beta(a)-q_{\beta,T}(a)|
\le
\frac{K_\beta\beta}{\pi^2}
 a^{-\beta/2}T^{\beta-1}e^{-\pi T/\beta}.
}
\tag{3.5}
\]

The only estimate used after (3.3) is that `t^(beta-1)` is decreasing:

\[
\int_T^\infty t^{\beta-1}e^{-\pi t/\beta}\,dt
\le \frac\beta\pi T^{\beta-1}e^{-\pi T/\beta}.
\]

Differentiating under the absolutely convergent contour gives

\[
q_\beta'(a)
=-\frac1{2\pi a}
\int_{-\infty}^{\infty}
(\beta/2+it)\widehat q_\beta(\beta/2+it)
a^{-\beta/2-it}\,dt.
\tag{3.6}
\]

Using `|beta/2+it|<=2t` for `t>=1`, one obtains, for example,

\[
\boxed{
|q_\beta'(a)-q_{\beta,T}'(a)|
\le
\frac{2K_\beta}{\pi}a^{-\beta/2-1}
\frac{T^\beta e^{-\pi T/\beta}}
{\pi/\beta-\beta/T}.
}
\tag{3.7}
\]

The denominator is positive for `T>=1` and `0<beta<1`.  Higher derivatives are handled identically by inserting the rising factor `(s)_k`; the exponential rate is unchanged.

On the finite interval `[-T,T]`, validated quadrature plus complex Gamma ball arithmetic gives a rigorous enclosure.  Since the integrand is analytic and pole-free on the chosen line, standard interval Taylor or validated Gauss/tanh-sinh quadrature terminates at any requested precision.  Equations (3.5) and (3.7) close the infinite-tail part explicitly.

## 3.3 The inversion is uniquely and stably posed

From (1.1)-(1.2),

\[
\boxed{
r(a)=a\left(\frac{q_\beta(a)}{C_\beta}\right)^{1/\beta}.}
\tag{3.8}
\]

The derivative is strictly positive.  Indeed, differentiating the original expectation for `F_beta`,

\[
-aF_\beta'(a)
=\beta\,\mathbb E\left[
\frac{a/S}{S'+a/S}(S'+a/S)^{-\beta}
\right]
<\beta F_\beta(a).
\tag{3.9}
\]

Since `q_beta=C_beta F_beta`,

\[
0<-a\frac{q_\beta'(a)}{q_\beta(a)}<\beta,
\tag{3.10}
\]

and hence

\[
\boxed{
r'(a)=
\left(\frac{q_\beta(a)}{C_\beta}\right)^{1/\beta}
\left(1+\frac{a}{\beta}\frac{q_\beta'(a)}{q_\beta(a)}\right)>0.}
\tag{3.11}
\]

Also `r(a)->0` as `a downarrow 0`, while the already established large-`a` asymptotic `r(a)^beta=beta log a+O(1)` gives `r(a)->infinity`.  Thus `a -> r(a)` is a global increasing bijection.

Finally, because `M'(r)=pi g_alpha(sqrt(r))`, (1.2) gives

\[
\boxed{
g_\alpha(\sqrt{r(a)})
=-\frac{q_\beta'(a)}{\pi r'(a)}.}
\tag{3.12}
\]

## Theorem 3.1 — certified arbitrary-index evaluator

Fix any `0<alpha<2`, any `rho>0`, and any target precision `epsilon>0`.  There is a deterministic algorithm using only elementary operations, Gamma-function interval evaluation, and validated finite quadrature which returns rigorous intervals of width at most `epsilon` containing

\[
a(\rho^2),\qquad
1-M(\rho^2),\qquad
g_\alpha(\rho).
\]

### Proof of termination

1. Evaluate `q_beta(a)` by (3.4) with the explicit infinite-contour error (3.5).
2. Use (3.8) to enclose `r(a)`.
3. A dyadic search finds `a_-<a_+` with `r(a_-)<rho^2<r(a_+)`, because `r` is continuous, strictly increasing, and has endpoints `0,infinity`.
4. Validated bisection shrinks `[a_-,a_+]`.  Whenever the current interval evaluation overlaps the target, increase `T` and quadrature precision; the exponentially small error bounds force eventual sign resolution unless the midpoint is the exact root, in which case an enclosure is already obtained.
5. Evaluate `q_beta,q_beta'` at the resulting `a` enclosure; (3.11)-(3.12) then enclose the CDF tail and density.  Continuity and `r'(a)>0` guarantee arbitrarily small final widths.

Thus the original recursive PWIT characterization has been replaced, for numerical purposes, by a one-dimensional exponentially convergent **certified** special-function computation for every real `alpha in (0,2)`, including irrational indices.

**B19 outcome.**  Arbitrary-index evaluation is no longer an uncontrolled root solve or Monte Carlo problem.  It has a rigorous, exponentially convergent contour certificate.  This is computational explicitness, not yet source-level symbolic closure.

---

# 4. Method B23 — do what the proposer did not expect: classify the obstruction itself

The rational-index cases have a finite Mellin-shift ODE and Meijer-G representation.  The natural question is whether the failure to find such an ODE at irrational beta is merely technical.  The exact boundary coefficients from B4 answer this completely.

## Definition

Call `q_beta` D-finite (holonomic) in the parameter `a` if it is annihilated on a positive interval by a nonzero linear differential operator

\[
\sum_{j=0}^m P_j(a)\frac{d^j}{da^j},
\qquad P_j\in\mathbb C[a].
\]

Because `q_beta` is C-infinity at zero, any such equation induces a linear recurrence with polynomial coefficients for its formal Taylor coefficients `a_n`; equivalently `(a_n)` is P-recursive.  Convergence of the formal series is not required for this implication.

## Theorem 4.1 — holonomicity dichotomy

\[
\boxed{
q_\beta(a)\text{ is D-finite in }a
\quad\Longleftrightarrow\quad
\beta\in\mathbb Q\cap(0,1).
}
\tag{4.1}
\]

### Rational direction

Write `beta=p/q` in lowest terms.  From (3.1), Gamma's functional equation gives the exact finite shift ratio

\[
\boxed{
\frac{\widehat q_\beta(s+p)}{\widehat q_\beta(s)}
=(-1)^p(\beta c_\beta)^{2q}
\frac{\prod_{j=0}^{p-1}(s+j)^2}
{\prod_{k=0}^{q-1}(s+\beta k)^2}.
}
\tag{4.2}
\]

A rational Mellin shift is equivalent, under Mellin inversion, to a finite linear differential equation with polynomial coefficients in `a`.  This is the ODE constructed explicitly in the preceding C0032 run.  Thus rational beta is D-finite.

### Irrational direction — elementary P-recursive obstruction

Assume beta is irrational and suppose, for contradiction, that the coefficient sequence `a_n` in (2.5) is P-recursive.  Then there are polynomials `P_0,...,P_m`, not all zero, such that for all sufficiently large `n`,

\[
\sum_{j=0}^mP_j(n)a_{n+j}=0.
\tag{4.3}
\]

Let `d_j=deg P_j` for nonzero `P_j`, and let `p_j` be its leading coefficient.  From (2.6), for every fixed `j`,

\[
\frac{a_{n+j}}{a_n}
=(-A_\beta)^j n^{j\sigma_\beta}(1+o(1)),
\qquad
A_\beta=(\beta c_\beta)^{-2/\beta}>0,
\tag{4.4}
\]

where `sigma_beta=2/beta-2`.

After dividing (4.3) by `a_n`, the `j`th term has leading order

\[
p_j(-A_\beta)^j n^{d_j+j\sigma_\beta}.
\]

For the sum to vanish, the maximum of the finitely many exponents

\[
E_j=d_j+j\sigma_\beta
\]

must be attained by at least two distinct indices.  If `i != j` tie, then

\[
\sigma_\beta=\frac{d_i-d_j}{j-i}\in\mathbb Q.
\tag{4.5}
\]

But

\[
\sigma_\beta=\frac2\beta-2
\]

is irrational whenever beta is irrational.  Therefore the maximal exponent is unique, its nonzero leading term cannot cancel, and (4.3) is impossible.  Hence `(a_n)` is not P-recursive and `q_beta` is not D-finite.  QED.

## Corollary 4.2 — rational indices are exactly the finite-Meijer-G side

A finite Meijer-G function satisfies a finite linear differential equation.  D-finite functions are closed under multiplication by algebraic functions and algebraic pullback.  Therefore, for irrational beta,

\[
\boxed{
q_\beta\text{ cannot be represented by a finite Meijer-G expression
with algebraic prefactor and algebraic change of variable.}
}
\tag{4.6}
\]

This explains structurally why the Gamma-multiplication collapse in the preceding run works for every rational beta and cannot simply be continued to irrational beta by taking a larger finite Meijer-G parameter list.  The natural arbitrary-index object is genuinely of Fox-H/Mellin-Barnes type, where irrational Gamma slopes are allowed.

The statement is only about this auxiliary transform `q_beta(a)` and finite holonomic special-function representations.  It does **not** prove that every conceivable notion of a symbolic closed form for the radial density is impossible.

**B23 outcome.**  The rational/irrational split is intrinsic, not an artifact of our algebra: rational beta is holonomic; irrational beta is provably non-holonomic by a two-line dominant-balance obstruction once the exact boundary coefficients are known.

---

# 5. Relation to known stable-law special-function literature

The bounded literature check on 2026-09-19 found the following relevant established fact.  Penson and Górska, *Exact and Explicit Probability Densities for One-Sided Lévy Stable Distributions* (Phys. Rev. Lett. 105, 210604, 2010; arXiv:1007.0193), give explicit known-function formulas for one-sided stable densities at every rational stable index `l/k`.  Saa and Venegeroles (Phys. Rev. E 84, 026702, 2011) likewise discuss numerical use of those rational-index Meijer-G formulas.  This is strongly compatible with the rational side of Theorem 4.1.

The searches performed combined the BCC/Bordenave-Chafaï source titles and authors with `corrigendum`, `explicit density`, `Mellin`, `Meijer G`, `Fox H`, `D-finite`, `holonomic`, `rational index`, and `stable distribution`.  They did not surface a later paper giving the all-radius BCC spectral density for arbitrary alpha, a corrigendum of the BCC tail formula, or this exact `q_beta` holonomicity classification.  These misses are negative evidence only and are **not** a novelty certificate.

The current source status therefore remains **PARTIAL / OPEN** for this campaign.

---

# 6. What has and has not been solved

What is now rigorous:

1. The BCC self-consistent scalar variable is globally eliminated in favor of the monotone parameter `a`.
2. Every origin jet of the density was already explicit before this run (`M_jet=+infinity`).
3. This run proves the exact full smooth-but-divergent boundary germ of the radial tail coordinate, including global signed finite-order remainder bounds.
4. This run gives a certified exponentially convergent arbitrary-index evaluator/inverter for the CDF and density.
5. This run proves the exact dichotomy `q_beta D-finite iff beta rational`; irrational beta cannot be reduced to a finite Meijer-G expression by algebraic pullback/prefactor.
6. Rational beta retains the preceding finite Meijer-G and direct finite-ODE descriptions.

What remains unresolved:

- For irrational beta, the final map from the explicit Mellin-Barnes/Fox-H coordinate to physical radius still requires inversion of the strictly increasing function `r(a)`.
- The survey's word `explicit` is informal, so it is not source-safe to declare the problem solved merely because a certified one-dimensional inversion algorithm exists.
- The proposed correction of the printed BCC far-tail exponential constant from the preceding runs still needs independent P26 and distinct OTHER-track audit before any closure or correction claim is promoted.
- No source-level paper package or closure audits exist yet.

Therefore this artifact is a substantial structural reduction and a complete theorem about the remaining transform, **not** a proof that the full source request is closed.

# 7. Fixed metric and protocol consequence

The frozen metric is

`M_jet = largest finite origin-jet order proved explicitly for every alpha in (0,2)`.

It remains

\[
\boxed{M_{\rm jet}: +\infty\to+\infty\quad\text{(NO MOVEMENT).}}
\]

The two immediately preceding ordinary C0032 runs also had no movement in this already-saturated metric.  Consequently this is the third consecutive ordinary no-movement run under the owner protocol.  The **next R7-06 run must be the Section-I STUCK1 thinking-only diagnosis**, despite the genuine global progress above.  This artifact does not pre-empt that diagnosis or silently change the frozen metric.