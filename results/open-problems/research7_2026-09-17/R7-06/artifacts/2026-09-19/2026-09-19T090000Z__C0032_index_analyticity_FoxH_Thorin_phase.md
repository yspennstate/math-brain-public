# C0032 — index analyticity, exact Fox-H data, a Thorin obstruction, and the rational/irrational holonomic phase

Target: Charles Bordenave and Djalil Chafaï, *Around the circular law*, Probability Surveys 9 (2012), arXiv:1109.3343v4, heavy-tailed Section 6.6 / p. 39; underlying construction: Charles Bordenave, Pietro Caputo and Djalil Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*, CMP 307 (2011), arXiv:1006.1713.

Status of the source after this artifact: **PARTIAL / OPEN**.  The results below sharpen the all-radius transform obtained in the preceding C0032 reports.  They do not by themselves settle the source's informal word “explicit”, and they have not received the required independent P26 and distinct OTHER-track audits.  No novelty conclusion is inferred from a bounded literature search.

## 1. Cumulative setup

Fix

\[
0<\beta<1,\qquad \alpha=2\beta,
\qquad c_\beta=\Gamma(1-\beta),
\qquad C_\beta=\Gamma(1-\beta)\Gamma(1+\beta).
\]

The preceding verified C0032 work gives

\[
q_\beta(a)=\mathbb E\frac{SS'}{a+SS'},\qquad a>0,
\tag{1.1}
\]

where `S,S'` are iid positive beta-stable variables in the BCC normalization, and

\[
\widehat q_\beta(s)
:=\int_0^\infty a^{s-1}q_\beta(a)\,da
=c_\beta^{2s/\beta}
\frac{\Gamma(s)\Gamma(1-s/\beta)^2}{\Gamma(1-s)},
\qquad 0<\Re s<\beta.
\tag{1.2}
\]

The squared-radius map is

\[
R_\beta(a)=a\left(\frac{q_\beta(a)}{C_\beta}\right)^{1/\beta},
\tag{1.3}
\]

and it is convenient to use the complete-Bernstein map

\[
\boxed{
H_\beta(a):=R_\beta(a)^\beta
=\frac{a^\beta q_\beta(a)}{C_\beta}.
}
\tag{1.4}
\]

Previous C0032 work proves that `H_beta` is a nonconstant complete Bernstein function, is strictly increasing from `0` to `+infinity` on the positive real axis, and that for every `x>0` the equation `H_beta(z)=x` has one and only one solution in the slit plane `C\(-infinity,0]`, namely the positive real solution.  Write

\[
A_\beta(x)=H_\beta^{-1}(x),\qquad x>0.
\tag{1.5}
\]

For physical radius `rho>0`, define

\[
a_\beta(\rho)=A_\beta(\rho^{2\beta}).
\tag{1.6}
\]

Then the physical radial tail is

\[
\boxed{
Q_\beta(\rho):=1-\mu_{2\beta}\{|z|\le \rho\}
=C_\beta\left(\frac{\rho^2}{a_\beta(\rho)}\right)^\beta,
}
\tag{1.7}
\]

and the planar density is

\[
\boxed{
g_{2\beta}(\rho)=-\frac{Q_\beta'(\rho)}{2\pi\rho}.}
\tag{1.8}
\]

The immediately preceding run also gave the canonical complete-Bernstein Stieltjes density `sigma_beta`:

\[
\frac{H_\beta(z)}{z}
=\int_0^\infty\frac{\sigma_\beta(t)}{z+t}\,dt,
\tag{1.9}
\]

whose Mellin transform is

\[
\boxed{
\widehat\sigma_\beta(s)
=\frac{c_\beta^{2(s+\beta-1)/\beta}}{C_\beta}
\frac{\Gamma(s+\beta-1)\Gamma((1-s)/\beta)^2}
{\Gamma(2-\beta-s)\Gamma(s)\Gamma(1-s)},
\quad 1-\beta<\Re s<1.
}
\tag{1.10}
\]

All statements below start from these already-established identities.

---

## 2. Method B5 — add the stability index as a parameter and differentiate

### Theorem 2.1 — real-analytic dependence on the stability index

The maps

\[
(\beta,a)\mapsto q_\beta(a),\qquad
(\beta,a)\mapsto H_\beta(a)
\]

are jointly real analytic on `(0,1) x (0,infinity)`.  The inverse

\[
(\beta,x)\mapsto A_\beta(x)=H_\beta^{-1}(x)
\]

is jointly real analytic on `(0,1) x (0,infinity)`.  Consequently, for every `rho>0`, both

\[
\beta\mapsto Q_\beta(\rho),
\qquad
\beta\mapsto g_{2\beta}(\rho)
\]

are real analytic.  More strongly, on compact rectangles bounded away from `beta=0,1` and `rho=0,infinity`, all fixed mixed derivatives are bounded uniformly; rational-index formulas therefore converge to irrational-index laws with every fixed finite derivative on compact physical-radius intervals.

### Proof

Let

\[
J=[\beta_-,\beta_+]\Subset(0,1).
\]

Choose one fixed Mellin line

\[
\Re s=\sigma,\qquad 0<\sigma<\beta_-.
\]

Put

\[
M_\beta(s)
=c_\beta^{2s/\beta}
\frac{\Gamma(s)\Gamma(1-s/\beta)^2}{\Gamma(1-s)}.
\tag{2.1}
\]

Then Mellin inversion gives

\[
q_\beta(a)
=\frac1{2\pi i}
\int_{\sigma-i\infty}^{\sigma+i\infty}
M_\beta(s)a^{-s}\,ds.
\tag{2.2}
\]

Uniform Stirling estimates on `beta in J` give, for some constants `K,N` depending only on `J` and `sigma`,

\[
|M_\beta(\sigma+i\tau)|
\le K(1+|\tau|)^N e^{-\pi|\tau|/\beta_+}.
\tag{2.3}
\]

Any fixed number of beta-derivatives only adds digamma/polygamma factors and powers of `s`, hence preserves an exponentially integrable majorant of the same form with a changed polynomial power.  Any fixed number of `a`-derivatives similarly multiplies the Mellin integrand by a polynomial in `s` and a bounded power of `a^{-1}` on compact positive `a`-intervals.  Differentiation under the integral is therefore valid to every order and the usual locally uniform power-series argument gives joint real analyticity.

The first beta-derivative is explicit.  Since

\[
\frac{d}{d\beta}\log c_\beta=-\psi(1-\beta),
\]

we obtain

\[
\boxed{
\partial_\beta\log M_\beta(s)
=\frac{2s}{\beta^2}
\left[
\psi(1-s/\beta)-\log\Gamma(1-\beta)-\beta\psi(1-\beta)
\right].
}
\tag{2.4}
\]

Hence

\[
\boxed{
\partial_\beta q_\beta(a)
=\frac1{2\pi i}\int
M_\beta(s)\,
\frac{2s}{\beta^2}
\left[
\psi(1-s/\beta)-\log\Gamma(1-\beta)-\beta\psi(1-\beta)
\right]
a^{-s}\,ds,
}
\tag{2.5}
\]

on the fixed vertical line above.  From

\[
H_\beta(a)=\frac{a^\beta q_\beta(a)}{C_\beta},
\]

and

\[
\partial_\beta\log C_\beta
=-\psi(1-\beta)+\psi(1+\beta),
\]

we get

\[
\boxed{
\partial_\beta H_\beta(a)
=H_\beta(a)
\left[
\log a+\psi(1-\beta)-\psi(1+\beta)
\right]
+\frac{a^\beta}{C_\beta}\partial_\beta q_\beta(a).
}
\tag{2.6}
\]

Previous work gives `H_beta'(a)>0` for all positive `a`.  Therefore the analytic implicit-function theorem applies globally along the positive inverse graph:

\[
H_\beta(A_\beta(x))=x.
\]

Thus `A_beta(x)` is jointly real analytic and

\[
\boxed{
\partial_\beta A_\beta(x)
=-\frac{\partial_\beta H_\beta(A_\beta(x))}
{H_\beta'(A_\beta(x))}.
}
\tag{2.7}
\]

For a fixed physical radius, the target itself moves with beta.  Differentiating

\[
H_\beta(a_\beta(\rho))=\rho^{2\beta}
\]

gives the useful exact sensitivity formula

\[
\boxed{
\partial_\beta a_\beta(\rho)
=\frac{2(\log\rho)\rho^{2\beta}
-\partial_\beta H_\beta(a_\beta(\rho))}
{H_\beta'(a_\beta(\rho))}.
}
\tag{2.8}
\]

Substitution into (1.7), followed by differentiation in `rho`, proves the assertions for the physical tail and density.

For uniform bounds, a compact `J x [x_0,x_1]` is mapped by `(beta,x) -> A_beta(x)` to a compact positive `a`-interval.  Continuity and strict positivity of `H_beta'` give a positive lower bound there, while the Mellin estimates give finite upper bounds for all required derivatives.  Equation (2.7) and its iterated derivatives then give the claimed compact uniform control.  This proves Theorem 2.1.  □

### Consequence 2.2 — rational approximants converge smoothly

If `beta_n` are rational and `beta_n -> beta_0 in (0,1)`, then for every compact `K subset (0,infinity)` and every fixed `m`,

\[
A_{\beta_n}\longrightarrow A_{\beta_0}
\quad\text{in }C^m(K).
\tag{2.9}
\]

The same statement holds for `Q_beta(rho)` and `g_{2 beta}(rho)` on compact positive-radius intervals.  Thus the rational Meijer-G laws approximate irrational laws smoothly even though their finite holonomic descriptions, as proved in the preceding B27 run, require unbounded complexity near an irrational index.

---

## 3. Method B17 — identify the exact special-function class and test the Thorin subclass

### 3.1 Exact Fox-H representation

Use the standard Fox-H convention

\[
H_{p,q}^{m,n}\!\left[z\,\middle|\,
\begin{matrix}(a_i,A_i)_{1,p}\\(b_j,B_j)_{1,q}\end{matrix}\right]
=\frac1{2\pi i}\int_{\cal L}
\frac{
\prod_{j=1}^m\Gamma(b_j+B_js)
\prod_{i=1}^n\Gamma(1-a_i-A_is)
}{
\prod_{j=m+1}^q\Gamma(1-b_j-B_js)
\prod_{i=n+1}^p\Gamma(a_i+A_is)
}
z^{-s}\,ds.
\tag{3.1}
\]

Comparing (1.2) with (3.1) gives the exact named-function form

\[
\boxed{
q_\beta(a)=
H_{2,2}^{1,2}\!\left[
\frac{a}{c_\beta^{2/\beta}}
\,\middle|\,
\begin{matrix}
(0,1/\beta),(0,1/\beta)\\
(0,1),(0,1)
\end{matrix}
\right].
}
\tag{3.2}
\]

Likewise, factoring

\[
c_\beta^{2(s+\beta-1)/\beta}
=c_\beta^{2(\beta-1)/\beta}
(c_\beta^{2/\beta})^s
\]

out of (1.10) yields

\[
\boxed{
\sigma_\beta(t)
=\frac{c_\beta^{2(\beta-1)/\beta}}{C_\beta}
H_{3,3}^{1,2}\!\left[
\frac{t}{c_\beta^{2/\beta}}
\,\middle|\,
\begin{matrix}
(1-1/\beta,1/\beta),(1-1/\beta,1/\beta),(0,1)\\
(\beta-1,1),(\beta-1,1),(0,1)
\end{matrix}
\right].
}
\tag{3.3}
\]

Equations (3.2)–(3.3) are identities, not merely asymptotic descriptions.  If `beta=p/q` is rational, all slopes are commensurate and Gauss multiplication reduces the Mellin integrand to finitely many unit-slope Gamma factors; hence these Fox-H functions reduce to finite Meijer-G expressions.  This rational-index phenomenon has strong prior-art analogues for positive stable laws (for example Penson–Górska and Demni), so no novelty is claimed for that general mechanism.

### 3.2 The canonical CBF density is not Thorin for beta > 1/2

Set

\[
h_\beta(t)=t\sigma_\beta(t).
\tag{3.4}
\]

For a complete Bernstein representation

\[
H(z)=z\int_0^\infty\frac{\sigma(t)}{z+t}\,dt,
\]

the standard Thorin-Bernstein characterization says precisely that a version of

\[
w(t)=t\sigma(t)
\]

must be nondecreasing.  Equivalently, `H'` must be a Stieltjes function.  We now determine the large-`t` direction of `h_beta` from (1.10).

At `s=1`, `widehat sigma_beta` has residue `-beta`: the double pole of `Gamma((1-s)/beta)^2` is reduced by the simple zero of `1/Gamma(1-s)`.  Shifting the inverse-Mellin contour to the right therefore gives

\[
\sigma_\beta(t)=\frac\beta t+\cdots.
\tag{3.5}
\]

Assume for the moment `beta != 1/2`.  At

\[
s_1=1+\beta
\]

the same Gamma factor has a genuine double pole.  Its double-pole coefficient is

\[
\begin{aligned}
K_\beta
&=\frac{c_\beta^4}{C_\beta}
\frac{\beta^2\Gamma(2\beta)}
{\Gamma(1-2\beta)\Gamma(1+\beta)\Gamma(-\beta)}\\
&=\boxed{
-\frac{\beta\,\Gamma(1-\beta)^2\Gamma(2\beta)}
{\Gamma(1-2\beta)\Gamma(\beta)^2}
}.
\end{aligned}
\tag{3.6}
\]

The inverse-Mellin residue rule for a double pole then gives

\[
\boxed{
\sigma_\beta(t)
=\frac\beta t
+K_\beta t^{-1-\beta}\log t
+O(t^{-1-\beta}),
\qquad t\to\infty,
}
\tag{3.7}
\]

where the `O` term may include a nonlogarithmic `t^{-1-beta}` contribution.  Therefore

\[
h_\beta(t)
=\beta+K_\beta t^{-\beta}\log t+O(t^{-\beta}),
\tag{3.8}
\]

and

\[
h_\beta'(t)
=K_\beta t^{-\beta-1}(1-\beta\log t)+O(t^{-\beta-1}).
\tag{3.9}
\]

If `beta>1/2`, then `1-2 beta` lies in `(-1,0)`, so

\[
\Gamma(1-2\beta)<0,
\]

and (3.6) gives

\[
K_\beta>0.
\]

Equation (3.9) then implies

\[
\boxed{h_\beta'(t)<0\quad\text{for all sufficiently large }t.}
\tag{3.10}
\]

Thus the required nondecreasing Thorin density fails.

### Theorem 3.1 — strict complete-Bernstein/Thorin separation above alpha=1

\[
\boxed{
\frac12<\beta<1
\quad\Longrightarrow\quad
H_\beta\in \mathrm{CBF}\setminus\mathrm{TBF}.
}
\tag{3.11}
\]

Equivalently, for the BCC spectral index,

\[
\boxed{
1<\alpha<2
\quad\Longrightarrow\quad
H_{\alpha/2}\text{ is complete Bernstein but not Thorin-Bernstein}.}
\tag{3.12}
\]

At `beta=1/2` the pole at `1+beta` is resonant with a zero from `1/Gamma(2-beta-s)`, and for `beta<1/2` the sign in (3.9) reverses asymptotically.  Those facts do **not** prove Thorin membership for `beta<=1/2`; no such positive classification is claimed here.

This result explains why the all-radius inverse is more general than the especially tractable inverse transforms occurring in the Thorin/GGC subclass for the upper half of the BCC stability range.

---

## 4. Method B28 — typical versus exceptional index: a holonomic phase transition for the canonical CBF density

The rational/irrational distinction seen previously for `q_beta` persists at the more canonical deterministic density `sigma_beta`.

### Theorem 4.1

\[
\boxed{
\sigma_\beta(t)\text{ is D-finite in }t
\quad\Longleftrightarrow\quad
\beta\in\mathbb Q\cap(0,1).
}
\tag{4.1}
\]

### Proof: rational direction

If `beta=p/q` is rational in lowest terms, (3.3) has commensurate rational slopes.  Gauss's multiplication formula rewrites the Mellin-Barnes integrand using only finitely many unit-slope Gamma factors.  The result is a finite Meijer-G function after an algebraic rescaling of its argument.  Every Meijer-G function satisfies a finite-order linear differential equation with polynomial coefficients.  Hence `sigma_beta` is D-finite.

### Proof: irrational direction

Suppose now that `beta` is irrational and, seeking a contradiction, that `sigma_beta` is D-finite.  Thus there is a nonzero polynomial-coefficient differential equation

\[
\sum_{j=0}^J P_j(t)\frac{d^j}{dt^j}\sigma_\beta(t)=0.
\tag{4.2}
\]

Taking Mellin transforms term by term on a common convergence strip and integrating by parts converts (4.2) into a nontrivial finite integer-shift recurrence

\[
\boxed{
\sum_{k=k_-}^{k_+}R_k(s)\widehat\sigma_\beta(s+k)=0,
}
\tag{4.3}
\]

where the `R_k` are rational functions, not all zero.  This standard Mellin correspondence follows directly from

\[
\mathcal M[t^m f^{(j)}](s)
=(-1)^j(s+m-j)_j\,\widehat f(s+m-j),
\tag{4.4}
\]

first where the boundary terms vanish and then everywhere by meromorphic continuation.

For irrational beta, formula (1.10) shows that `widehat sigma_beta` has an uncancelled double pole at every

\[
\boxed{s_n=1+n\beta,\qquad n=1,2,3,\ldots.}
\tag{4.5}
\]

Indeed, `Gamma((1-s)/beta)^2` has a double pole there, while irrationality prevents `n beta` or `(n+1)beta` from being integers, so none of the denominator Gamma factors cancels it.

Choose an index `k_0` with `R_{k_0}` nonzero.  Apart from finitely many `n`, `R_{k_0}` is finite and nonzero at

\[
s=1+n\beta-k_0.
\]

The `k_0` term in (4.3) then has a double pole.  Could another shifted term have a pole at the same point?  That would require integers `m>=1` and `k_1!=k_0` such that

\[
1+m\beta-k_1=1+n\beta-k_0,
\]

or

\[
(m-n)\beta=k_1-k_0\in\mathbb Z.
\tag{4.6}
\]

Irrationality forces `m=n` and then `k_1=k_0`, a contradiction.  Hence the chosen double pole is unique among the finitely many terms and cannot cancel.  This contradicts (4.3).  Therefore `sigma_beta` is not D-finite.  □

### Corollary 4.2 — exact phase diagram

The C0032 transform has a dense exceptional/typical split:

- if `beta` is rational, `q_beta` and `sigma_beta` reduce to finite Meijer-G data and are D-finite; `H_beta` is D-finite up to multiplication by the algebraic factor `a^beta`, and its local positive inverse `A_beta` is differential-algebraic;
- if `beta` is irrational, `q_beta` (previous C0032 theorem) and now `sigma_beta` are non-D-finite; the canonical deterministic representation remains Fox-H/Mellin-Barnes and the inverse remains the unique complete-Bernstein branch recovered by the finite contour formula.

No claim is made here that `A_beta` is non-D-algebraic or non-D-finite for irrational beta.  That stronger inverse obstruction remains open.

Combining this with Theorem 2.1 gives a useful paradox-free picture: for rational `beta_n -> beta_0` irrational,

\[
A_{\beta_n}\to A_{\beta_0}
\]

smoothly on every compact positive interval, even though the finite holonomic representations of the rational approximants must have unbounded complexity (the preceding B27 theorem).  Thus loss of holonomicity at irrational index is a structural phase transition in representation class, not a discontinuity of the BCC law itself.

---

## 5. What these results do and do not close

This run does not change the already saturated frozen metric `M_jet=+infinity`; it moves global structure instead.

The new facts are:

1. all positive-radius BCC tails, densities and inverse coordinates depend real-analytically on the stability index, with explicit beta-derivative formulas and compact uniform bounds;
2. the auxiliary tail transform and the canonical complete-Bernstein density have exact Fox-H representations for all indices, reducing to Meijer-G at rational indices;
3. for `alpha>1`, the physical radius-power map is a complete Bernstein function but provably **not** a Thorin-Bernstein function;
4. the deterministic canonical density `sigma_beta` is D-finite exactly at rational `beta`, while rational formulas approximate irrational laws smoothly despite unbounded holonomic complexity.

These results strengthen the interpretation of the preceding all-radius contour formula, but source closure still needs a defensible scope judgment that the explicit Fox-H/Stieltjes transform plus certified finite contour inverse answers the source's informal “explicit” request, a full self-contained paper package, and the required independent P26 plus distinct OTHER-track audits.

## 6. Dated literature check, 2026-09-19

Bounded searches checked the Bordenave–Chafaï survey and the Bordenave–Caputo–Chafaï heavy-tail construction again and did not surface a later source-matching all-index/all-radius BCC density formula.  This is negative evidence only.

Relevant prior art/nearby machinery:

- Bordenave–Chafaï, *Around the circular law*, arXiv:1109.3343.
- Bordenave–Caputo–Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*, arXiv:1006.1713.
- James Chen and Sheehan Olver, *Computing Inverses of Stieltjes Transforms of Probability Measures*, arXiv:2410.16178, Mathematics of Computation, electronically published 2026-01-14: rigorous inverse counting and contour recovery for Stieltjes transforms.  The located material does not contain the BCC radius map.
- Nizar Demni, *On classical and free stable laws*, arXiv:1009.4926: representative Bernstein measures expressed by Fox-H functions and special rational reductions.  This is important prior art for the function-class mechanism, not an all-radius BCC spectral-density solution.
- R. L. Schilling, R. Song and Z. Vondracek, *Bernstein Functions: Theory and Applications*, Chapter 8, especially the Thorin-Bernstein characterization `f in TBF iff f' is Stieltjes`, equivalently the complete-Bernstein density can be written with a nondecreasing `w(t)=t sigma(t)`.

No novelty certificate is claimed from search failure.
