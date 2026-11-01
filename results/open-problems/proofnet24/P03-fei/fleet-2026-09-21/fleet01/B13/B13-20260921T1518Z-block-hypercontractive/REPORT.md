# B13 FEI route 2/13: Boolean block-profile anti-concentration

**Status: PARTIAL toward full FEI. Full Friedgut--Kalai Fourier entropy--influence remains OPEN.**

Execution label: **WITHOUT_VERIFIED_BRAIN**. The ordinary `math_brain` package startup is unavailable in this executor, so no authenticated brain retrieval/context was consumed.

This run continues APPROACH 2/13. It does not rerun the read-once certificate and does not audit prior FEI work. It starts from the earlier B13 exact-product rigidity theorem and the fleet02 B13 block-parity atom cap. The new result below upgrades the atom cap to a dimension-free *all-Hamming-centres Laplace/dispersion constraint* written purely in the block-correlation profile. No novelty or publication-priority claim is made without literature comparison.

## 1. Setup

Let

\[
f:\{-1,1\}^n\to\{-1,1\},\qquad
\mu(S)=\widehat f(S)^2,
\]

and let `X` denote the spectral sample with law `mu`. For a physical block `J subseteq [n]`, write `x^J` for simultaneous sign flip on `J` and

\[
c_J:=\mathbb E[f(x)f(x^J)]
=\mathbb E[(-1)^{|X\cap J|}].
\]

Let

\[
Y_J:=(-1)^{|X\cap J|}\in\{+1,-1\},
\qquad
r_{J,y}:=\Pr(Y_J=y)=\frac{1+y c_J}{2}.
\]

For `y=+1,-1` define the even/odd Fourier projections

\[
g_{J,+}(x)=\frac{f(x)+f(x^J)}2,\qquad
g_{J,-}(x)=\frac{f(x)-f(x^J)}2.
\]

Booleanity is used at exactly one decisive point:

\[
g_{J,y}(x)\in\{0,\pm1\},\qquad
\mathbb E g_{J,y}^2=r_{J,y},
\]

and the squared Fourier coefficients of `g_{J,y}`, normalized by `r_{J,y}`, are exactly the law of `X` conditioned on `Y_J=y`.

## 2. Main theorem: every parity cell is Hamming anti-concentrated

### Theorem B13-BLOCK-LAPLACE-01

Fix `J`, `y in {+1,-1}` with `r=r_{J,y}>0`, any Hamming centre `T subseteq[n]`, and any `s in [0,1]`. Then

\[
\boxed{
\mathbb E\!\left[s^{|X\triangle T|}\mid Y_J=y\right]
\le r^{(1-s)/(1+s)}.
}
\tag{1}
\]

Equivalently, in unnormalised form,

\[
\boxed{
\sum_{S:\,(-1)^{|S\cap J|}=y}
\mu(S)s^{|S\triangle T|}
\le r^{2/(1+s)}.
}
\tag{2}
\]

#### Proof

Multiply the parity projection by the character `chi_T`:

\[
h=\chi_T g_{J,y}.
\]

Its pointwise absolute value is unchanged, so `h in {0,+-1}` and

\[
\|h\|_{1+s}=r^{1/(1+s)}.
\]

Multiplication by `chi_T` translates the Fourier support:

\[
\widehat h(U)=\widehat {g_{J,y}}(U\triangle T).
\]

Apply Bonami--Beckner hypercontractivity in the standard form

\[
\|T_\rho h\|_2\le\|h\|_{1+\rho^2}
\]

with `rho=sqrt(s)`. Squaring gives

\[
\sum_U s^{|U|}\widehat h(U)^2
\le r^{2/(1+s)}.
\]

Substitute the Fourier translation and the fact that `g_{J,y}` keeps exactly the parity-`y` Fourier coefficients of `f`. This is (2); division by `r` gives (1). QED.

### Small-ball consequence

For every integer `m>=0` and every `0<s<1`,

\[
\boxed{
\Pr\{|X\triangle T|\le m\mid Y_J=y\}
\le s^{-m}r^{(1-s)/(1+s)}.
}
\tag{3}
\]

In particular, at `s=1/2`,

\[
\Pr\{|X\triangle T|\le m\mid Y_J=y\}
\le 2^m r^{1/3}.
\tag{4}
\]

At `s=0`, (2) recovers the previous block-parity atom cap

\[
\mu(T)\le r^2
\]

whenever `T` belongs to the indicated parity class. Thus the old atom inequality is only the zero-noise endpoint of a full one-parameter anti-concentration family.

## 3. Stronger first-moment form from edge isoperimetry

The derivative of the hypercontractive bound at `s=1` gives only a natural-log constant. For `{0,+-1}` projections one can do better by using the cube edge-isoperimetric inequality directly.

### Theorem B13-BLOCK-DISPERSION-02

Under the same hypotheses, for every centre `T`,

\[
\boxed{
\mathbb E[|X\triangle T|\mid Y_J=y]
\ge \frac12\log_2\frac1r.
}
\tag{5}
\]

#### Proof

Again put `h=chi_T g_{J,y}` and let `A={x:h(x) ne 0}`. Then `|A|/2^n=r`. With

\[
D_kh(x)=\frac{h(x)-h(x^{\{k\}})}2,
\]

Parseval gives

\[
\sum_U |U|\widehat h(U)^2
=\sum_k\mathbb E(D_kh)^2.
\]

If the support indicator `1_A` changes across a `k`-edge, one endpoint of `h` is zero and the other is a sign, so `(D_k h)^2=1/4`. Hence

\[
\sum_k\mathbb E(D_kh)^2
\ge \frac14 I(1_A).
\]

The edge-isoperimetric/log-Sobolev bound

\[
I(1_A)\ge2r\log_2(1/r)
\]

therefore yields

\[
\sum_U |U|\widehat h(U)^2
\ge\frac r2\log_2(1/r).
\]

Translate Fourier indices back by `T` and divide by `r`. QED.

## 4. Pure block-correlation-profile inequality

For each coordinate `k`, let

\[
p_k^{J,y}:=\Pr(k\in X\mid Y_J=y).
\]

The Hamming centre minimizing conditional expected distance is obtained coordinatewise, hence

\[
\min_T\mathbb E[|X\triangle T|\mid Y_J=y]
=\sum_k\min\{p_k^{J,y},1-p_k^{J,y}\}.
\]

The conditional marginal itself is determined by the deterministic block-flip correlations:

\[
\boxed{
p_k^{J,y}
=\frac{1-c_{\{k\}}+y c_J-y c_{J\triangle\{k\}}}
{2(1+y c_J)}.
}
\tag{6}
\]

Indeed `1_{k in X}=(1-Y_{\{k\}})/2` and `Y_JY_{\{k\}}=Y_{J triangle {k}}`.

Combining (5) and (6) gives the promised profile-only Booleanity constraint:

\[
\boxed{
\sum_{k=1}^n
\min\!\left\{
\frac{1-c_k+y c_J-y c_{J\triangle k}}{2(1+y c_J)},
1-\frac{1-c_k+y c_J-y c_{J\triangle k}}{2(1+y c_J)}
\right\}
\ge
\frac12\log_2\frac{2}{1+y c_J}.
}
\tag{7}
\]

Here `c_k` abbreviates `c_{\{k\}}`. This is dimension-free, nonlinear, two-sided (`y=+1` and `y=-1`), and stated entirely in terms of genuine Boolean block correlations.

A useful weighted version follows by multiplying by `r_{J,y}` and summing over the two parity cells:

\[
\frac12 h_2(r_{J,-})
\le
\sum_{y=\pm1}r_{J,y}
\sum_k\min\{p_k^{J,y},1-p_k^{J,y}\}.
\tag{8}
\]

The right side is the residual coordinatewise spectral ambiguity after revealing the block parity. Equation (8) suggests a possible entropy-payment scheme via carefully chosen block parities, but it is not yet a summable potential-drop theorem.

## 5. Coordinate form and a decisive exact product obstruction

Take `J={i}` and the odd cell `y=-1`. Then `r=q_i=Inf_i(f)`. Choosing centre `T={i}` in (1) gives

\[
\boxed{
\mathbb E\!\left[s^{|X|-1}\mid i\in X\right]
\le q_i^{(1-s)/(1+s)}.
}
\tag{9}
\]

The edge-isoperimetric form is

\[
\boxed{
\sum_{j\ne i}\Pr(i,j\in X)
\ge\frac{q_i}{2}\log_2\frac1{q_i}.
}
\tag{10}
\]

The even cell similarly gives

\[
\boxed{
\sum_{j\ne i}\Pr(i\notin X,\ j\in X)
\ge\frac{1-q_i}{2}\log_2\frac1{1-q_i}.
}
\tag{11}
\]

Adding (10) and (11) yields the simple necessary marginal/global relation

\[
\boxed{I(f)-q_i\ge\frac12h_2(q_i).}
\tag{12}
\]

Now test the canonical non-Boolean high-entropy product law

\[
Q=\operatorname{Bernoulli}(1/64)^{\otimes64}.
\]

For `J={i}`, conditional on `i in X`, the other 63 coordinates remain independent `Bernoulli(1/64)`. At `s=1/2`, the left side of (9) would equal

\[
\left(1-\frac1{64}+\frac1{128}\right)^{63}
=\left(\frac{127}{128}\right)^{63}.
\]

Booleanity would require this to be at most

\[
(1/64)^{1/3}=1/4.
\]

But Bernoulli's inequality gives the exact contradiction

\[
\left(\frac{127}{128}\right)^{63}
\ge1-\frac{63}{128}
=\frac{65}{128}
>\frac14.
\tag{13}
\]

So the product obstruction is not merely ruled out at exact independence by the previous rational-divisibility argument: it violates a quantitative inequality with a macroscopic gap. By continuity this also excludes an open neighbourhood of that product profile in the relevant parity-cell Laplace statistic.

## 6. Why this still does not close FEI

The first-moment consequence alone is not enough. Consider the abstract, explicitly **non-Boolean** set law

\[
\nu_{n,L}
=\left(1-\frac1L\right)\delta_\varnothing
+\frac1L\,\operatorname{Unif}\{S:|S|=L\}.
\tag{14}
\]

It has `E|X|=1` and every marginal `q_i=1/n`. Conditional on `i in X`, exactly `L-1` other coordinates are present. If

\[
L-1\ge\frac12\log_2 n,
\]

then the singleton version of the mean-dispersion lower bound is satisfied. Yet

\[
H(\nu_{n,L})
=h_2(1/L)+\frac1L\log_2\binom nL,
\]

which is unbounded with `n` for `L` of logarithmic size. For the concrete diagnostic `n=4096, L=7`, the singleton mean bound is met at equality (`6=0.5 log2 4096`) while the entropy is about `10.833585840878` bits at mean size one.

This is not a Boolean counterexample and does not test all block/Laplace inequalities. It shows only that (10) by itself cannot prove FEI. A successful continuation has to exploit the full family over blocks/centres/scales, or prove a summable payment rule for them.

## 7. Next universal target

The useful next lemma is no longer mere positivity of total correlation. The block inequalities suggest a parity-reveal potential:

1. choose a block parity `Y_J`;
2. charge its entropy `h_2(r_{J,-})` using (8);
3. prove that the charged post-reveal ambiguity is a *drop* of a nonnegative Booleanity potential, so that it cannot be reused at every depth.

Concretely, seek a functional `Phi` of the block-correlation profile with `Phi<=C I(f)` and, for an adaptively chosen `J`,

\[
h_2(r_{J,-})+\mathbb E[\Phi(\text{child})]
\le\Phi(\text{parent}).
\]

The obstruction is that conditioning a spectral parity cell turns the physical projection into a `{0,+-1}` function; iterating arbitrary parity projections can create half-integer values, so the one-step Boolean support argument does not automatically recurse. Any next proof must either build a class closed under the chosen reveal or carry a quantitative integrality/phase remainder.

That is the present gap. The theorem above is universal, but **full FEI remains OPEN**.
