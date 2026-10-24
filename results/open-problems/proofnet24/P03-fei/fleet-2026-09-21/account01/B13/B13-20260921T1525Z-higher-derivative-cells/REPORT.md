# B13 FEI route 2/13: all-pattern higher-derivative cell constraints

**Status: PARTIAL toward full FEI. Full Friedgut--Kalai Fourier entropy--influence remains OPEN.**

Execution label: **WITHOUT_VERIFIED_BRAIN**. No authenticated brain retrieval/context was consumed in this run. This is a creative continuation of APPROACH 2/13, not an audit and not a rerun of the settled read-once certificate. No publication-priority or novelty claim is made here.

## 1. Setup

Let

\[
f:\{-1,1\}^n\to\{-1,1\},\qquad \mu(S)=\widehat f(S)^2,
\]

and let `X` be the spectral sample with law `mu`. Fix a nonempty coordinate block `A subseteq [n]`, `k=|A|`, and a membership pattern `sigma in {0,1}^A`. Write

\[
p_{A,\sigma}=\Pr(X\cap A=\sigma).
\]

The previous B13 block-parity theorem controlled one parity cell at a time. The result below controls **every exact membership cell**, simultaneously at every order `k`.

## 2. Universal all-pattern Laplace inequality

### Theorem B13-HIGHER-CELL-01

If `p=p_{A,sigma}>0`, then for every `0<=s<=1`,

\[
\boxed{
\mathbb E\!\left[s^{|X\setminus A|}\mid X\cap A=\sigma\right]
\le
\min\left\{1,\left(4^{k-1}p\right)^{\frac{1-s}{1+s}}\right\}.
}
\tag{1}
\]

This is dimension-free and genuinely two-sided: it applies to every zero/one pattern on every physical block, not only to the event `A subseteq X` or to a block parity.

### Proof

Identify `sigma` with the subset `R={i in A:sigma_i=1}` and put `T=A\setminus R`. Define

\[
f'=\chi_T f.
\]

Multiplication by `chi_T` translates Fourier indices by symmetric difference with `T`; hence the cell `X cap A=R` for `f` becomes the all-ones cell `A subseteq X'` for the spectral sample `X'=X triangle T` of `f'`. Coordinates outside `A` are unchanged.

Use the normalized discrete derivative

\[
D_i h(x)=\frac{h(x)-h(x^{\{i\}})}2,
\qquad D_A=\prod_{i\in A}D_i,
\]

and set

\[
g=\chi_A D_A f'.
\]

On the Fourier side, `D_A` keeps exactly coefficients whose support contains `A`, and multiplication by `chi_A` removes `A` from those supports. Therefore `g` depends only on `A^c`,

\[
\|g\|_2^2=p,
\]

and, after normalization by `p`, the squared Fourier coefficients of `g` are exactly the conditional law of `X'\setminus A=X\setminus A` given the chosen cell.

The decisive Booleanity input is a granularity statement in physical space. For every `x`,

\[
D_A f'(x)=2^{-k}\sum_{B\subseteq A}(-1)^{|B|}f'(x^B).
\]

The numerator is an even integer because `k>=1` and each summand is `+-1`. Consequently

\[
D_A f'(x)=0\quad\text{or}\quad |D_A f'(x)|\ge 2^{1-k}.
\tag{2}
\]

Also `|D_A f'|<=1`. Put `delta=2^{1-k}`. For `0<=s<=1`, on every nonzero point,

\[
|g|^{1+s}=|g|^2|g|^{s-1}\le \delta^{s-1}|g|^2,
\]

so

\[
\mathbb E|g|^{1+s}\le \delta^{s-1}p.
\tag{3}
\]

Apply Bonami--Beckner hypercontractivity in the form

\[
\|T_{\sqrt s}g\|_2\le\|g\|_{1+s}.
\]

After squaring and using (3),

\[
\sum_{U\subseteq A^c}s^{|U|}\widehat g(U)^2
\le
\left(\delta^{s-1}p\right)^{2/(1+s)}.
\]

Divide by `p` and use `delta^{-2}=4^{k-1}`. This gives (1) whenever the displayed right side is below one; otherwise the trivial probability-generating-function bound by one is stronger. QED.

## 3. Three consequences

### Conditional escape / first moment

Letting `s` increase to one in (1) gives

\[
\boxed{
\mathbb E[|X\setminus A|\mid X\cap A=\sigma]
\ge
\frac12\left[\ln\frac1{4^{k-1}p_{A,\sigma}}\right]_+.
}
\tag{4}
\]

The logarithm here is natural. For `k=1`, the earlier special `{0,+-1}` edge-isoperimetric argument gives the stronger base-two constant; (4) is valuable because it works at every derivative order and for every pattern.

### Cell entropy versus outside influence

Equation (4), including the inactive case `4^{k-1}p>=1`, rearranges to

\[
-\log_2 p_{A,\sigma}
\le
2(k-1)+\frac{2}{\ln2}\,
\mathbb E[|X\setminus A|\mid X\cap A=\sigma].
\tag{5}
\]

Averaging over the pattern on `A` gives the universal projection inequality

\[
\boxed{
H_2(X_A)
\le
2(k-1)+\frac{2}{\ln2}\sum_{i\notin A}\Pr(i\in X).
}
\tag{6}
\]

This is not yet FEI because the additive `2(k-1)` is not summable under a naive recursive partition.

### Inclusion/factorial-moment hierarchy

For `A` of size `k`, let `p_A=Pr(A subseteq X)`. Taking the all-ones cell in (4),

\[
\boxed{
\sum_{j\notin A}p_{A\cup\{j\}}
\ge
\frac{p_A}{2}
\left[\ln\frac1{4^{k-1}p_A}\right]_+.
}
\tag{7}
\]

Summing over all `|A|=k`, with `M_k=E binom(|X|,k)`, yields

\[
\boxed{
(k+1)M_{k+1}
\ge
\frac12\sum_{|A|=k}p_A
\left[\ln\frac1{4^{k-1}p_A}\right]_+.
}
\tag{8}
\]

Thus Booleanity forces a dimension-free hierarchy of conditional escape payments across every derivative order.

## 4. Decisive calculation: the previous clustered loophole dies already at order two

The previous B13 report exhibited the abstract, explicitly non-Boolean law

\[
\nu_{n,L}=\left(1-\frac1L\right)\delta_{\varnothing}
+\frac1L\,\mathrm{Unif}\{S:|S|=L\}.
\tag{9}
\]

It has `E|X|=1`. At `n=4096,L=7` it was engineered so that the **singleton** first-moment constraint is met exactly, while its entropy is large. The new order-two constraint rules it out.

For a fixed pair `A`,

\[
p_A=\Pr(A\subseteq X)=\frac{L-1}{n(n-1)}=\frac1{2,795,520}.
\]

Conditional on `A subseteq X`, exactly `L-2=5` coordinates remain outside `A`. But (4) requires

\[
5
\ge
\frac12\ln\frac1{4p_A}
=
\frac12\ln(698880)
=6.728617166329\ldots,
\]

which is false by a gap `1.728617166329...`.

The committed exact-rational diagnostic records the same calculation. It also checks the dyadic family

\[
n=2^{2r},\qquad L=r+1,
\]

for `2<=r<=20`, and every case violates the order-two inequality. The family-level sign can also be shown analytically; the finite sweep is not used as a theorem.

This is meaningful progress on APPROACH 2/13: the simple high-entropy clustered relaxation that survived the singleton Booleanity payment cannot survive the two-coordinate derivative cell constraint.

## 5. A limitation proved in parallel: the first-moment hierarchy alone is still insufficient

The whole Laplace family (1) is stronger than its derivative (4). It is important not to collapse the two.

There is an abstract exchangeable, non-Boolean family satisfying **all one-sided first-moment constraints (7)** while `H/E|X|` diverges. Let integers `m,B>=2`, `n=mB`, sample

\[
Q\sim\mathrm{Beta}(1,B-1),
\]

and, conditional on `Q`, include the `n` coordinates independently with probability `Q`.

For every fixed `k`-set `A`,

\[
p_A=\mathbb E Q^k=\frac{k!}{(B)_k},
\qquad
\mathbb E[|X|-k\mid A\subseteq X]
=(n-k)\frac{k+1}{B+k}.
\tag{10}
\]

Write

\[
\Psi_k=\ln\frac1{4^{k-1}p_A}.
\]

For `k<=B`,

\[
\mathbb E[|X|-k\mid A\subseteq X]
\ge \frac{(m-1)(k+1)}2,
\]

while, from `(B)_k<=(2B)^k` and `k!>=(k/e)^k`,

\[
\Psi_k
\le k(\ln B+1-\ln2)+\ln4.
\]

Hence if

\[
m-1\ge\ln B+1-\ln2,
\qquad m-1\ge\ln4,
\tag{11}
\]

then (7) holds for every `k<=B`. For `k=B`,

\[
4^{B-1}p_B
=\frac{4^{B-1}}{\binom{2B-1}{B}}\ge1,
\]

because `binom(2B-1,B)<=4^{B-1}`; thereafter `Psi_k` decreases, so every `k>=B` is inactive. For example `B=floor(e^{m-2})` and `m>=3` satisfy (11).

Yet `E|X|=m`, and conditioning on `Q` gives

\[
H(X)\ge H(X\mid Q)
=n\,\mathbb E h_2(Q)
\ge \frac{n}{\ln2}\mathbb E[Q\ln(1/Q)].
\]

For `Q~Beta(1,B-1)`,

\[
\mathbb E[Q\ln(1/Q)]=\frac{H_B-1}{B},
\]

so

\[
\boxed{
\frac{H(X)}{\mathbb E|X|}
\ge\frac{H_B-1}{\ln2}\to\infty.
}
\tag{12}
\]

Therefore the factorial/conditional-mean hierarchy (7)--(8), even at **all orders**, cannot by itself prove FEI. A successful continuation must use the full small-ball/Laplace information in (1), the two-sided pattern family, or an additional phase/correlation consistency constraint.

This beta-mixture is only an abstract set distribution. It is **not** a Boolean FEI counterexample.

## 6. Next exact target

The route has moved from singleton rigidity to a full all-pattern hierarchy. The next question is now sharp:

> Does the complete family (1), for every block `A`, every pattern `sigma`, and every `s in [0,1]`, already imply `H(X)<=C E|X|`? If not, what additional Boolean correlation/phase identity separates spectral samples from abstract laws satisfying (1)?

A useful stress family is the beta-binomial mixture above. Preliminary calculations suggest that polynomial choices of `B` can satisfy a surprisingly large range of the full Laplace inequalities while retaining a growing entropy/mean ratio, but this has **not** been proved and is not recorded as a theorem here. The next B13 run should either (i) prove such a full-Laplace abstract counterfamily, decisively killing magnitude-only cell hypercontractivity as a complete route, or (ii) locate a rigorous `(A,sigma,s)` failure and convert its mechanism into the missing stronger Boolean profile constraint.

## 7. Relation to current literature

A fresh literature search found the recent 2026 FEI work of Gonzalez--MacManus--Pereyra emphasizing restriction/stopping-tree entropy payments, along with the established composition and extremal-class FEI literature. I did not find, in that bounded search, this exact all-pattern derivative-cell inequality. That is **not** a novelty determination; no publication-priority claim is made without a dedicated primary-literature comparison.

## 8. Files

- `check_higher_derivative_cells.py`: exact-rational clustered-law diagnostic and dyadic-family check.
- `verification.json`: recorded decisive `n=4096,L=7` output.
- this report: analytic theorem, proof, corollaries, exact obstruction, and the proved limitation of the first-moment hierarchy.

Full FEI remains **OPEN**.
