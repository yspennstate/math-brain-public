# B13 FEI route 2/13: integrated block-Laplace inequality and influence-profile localization

**Status: PARTIAL toward full FEI. Full Friedgut--Kalai Fourier entropy--influence remains OPEN.**

Execution label: **WITHOUT_VERIFIED_BRAIN**. The ordinary `math_brain` package is unavailable in this executor, so no authenticated brain retrieval/context was consumed.

This run continues APPROACH 2/13 from the existing B13 block-Laplace theorem. It does not rerun the settled read-once certificate and does not audit other FEI work. The main new step is to integrate the singleton Laplace family exactly. This produces a dimension-free constraint on the entire influence profile, quantitatively rules out the canonical tiny-marginal product obstruction, and isolates a sharper abstract burst-law stress test.

No novelty or publication-priority claim is made. The resulting influence-profile inequality has a Talagrand/KKL shape; literature comparison is still required before any novelty claim.

## 1. Input from the preceding B13 theorem

Let

\[
f:\{-1,1\}^n\to\{-1,1\},\qquad
\mu(S)=\widehat f(S)^2,
\]

and let `X` have law `mu`. Write

\[
q_i=\Pr(i\in X)=\operatorname{Inf}_i(f),\qquad
I=\sum_i q_i=\mathbb E|X|,
\]

and

\[
V=\Pr(X\ne\varnothing)=1-\widehat f(\varnothing)^2=\operatorname{Var}(f).
\]

The preceding B13 block-hypercontractive report proved, for every coordinate with `q_i>0` and every `0<=s<=1`,

\[
\mathbb E\!\left[s^{|X|-1}\mid i\in X\right]
\le q_i^{(1-s)/(1+s)}.
\tag{1}
\]

This is the singleton odd-cell specialization of the full block-parity Laplace inequality.

## 2. PROVED: an integrated influence-moment inequality

Define the probability generating function

\[
F(s)=\mathbb E[s^{|X|}]=\sum_S\mu(S)s^{|S|}.
\]

Then

\[
F'(s)=\sum_i\sum_{S\ni i}\mu(S)s^{|S|-1}.
\]

Multiplying (1) by `q_i` gives

\[
\sum_{S\ni i}\mu(S)s^{|S|-1}
\le q_i^{2/(1+s)}.
\]

Hence, pointwise for `0<=s<=1`,

\[
\boxed{
F'(s)\le\sum_i q_i^{2/(1+s)}.
}
\tag{2}
\]

Integrating from `s=0` to `s=1` yields

\[
V=F(1)-F(0)
\le\sum_i\Psi(q_i),
\qquad
\Psi(q):=\int_0^1 q^{2/(1+s)}\,ds.
\tag{3}
\]

With

\[
u=\frac{1-s}{1+s},\qquad ds=-\frac{2\,du}{(1+u)^2},
\]

we obtain the equivalent influence-moment form

\[
\boxed{
V\le
2\int_0^1\frac{\sum_i q_i^{1+u}}{(1+u)^2}\,du.
}
\tag{4}
\]

This is a dimension-free necessary condition on the complete influence profile of every Boolean spectral sample.

### Proof status

Equations (2)--(4) are exact consequences of the already proved singleton Laplace inequality; no numerical step enters their proof.

## 3. PROVED: a Talagrand-shaped scalar corollary

For `0<q<1`, putting `L=ln(1/q)` in the integral representation gives

\[
\frac{\Psi(q)}q
=2\int_0^1\frac{e^{-Lu}}{(1+u)^2}\,du.
\tag{5}
\]

Therefore

\[
\Psi(q)\le q
\tag{6}
\]

and, by dropping `(1+u)^{-2}` and extending the integral to infinity,

\[
\Psi(q)
\le 2q\int_0^\infty e^{-Lu}\,du
=\frac{2q}{\ln(1/q)}.
\tag{7}
\]

Thus

\[
\boxed{
V\le\sum_i q_i\min\!\left\{1,\frac{2}{\ln(1/q_i)}\right\},
}
\tag{8}
\]

with the natural endpoint convention for `q_i=0,1`.

This has the same qualitative shape as classical Talagrand/KKL influence-profile inequalities; it is recorded here because it drops directly out of the block-profile route and can be used without reverting to an input-side proof.

## 4. PROVED: maximum-influence and influence-mass localization

Let

\[
m:=I/V\ge1
\]

when `V>0`, and set `q_*:=max_i q_i`.

The ratio `Psi(q)/q` in (5) is increasing in `q`. Hence

\[
V\le\sum_i\Psi(q_i)
\le \frac{\Psi(q_*)}{q_*} I
\le\frac{2I}{\ln(1/q_*)}.
\]

Therefore

\[
\boxed{
q_*\ge e^{-2I/V}=e^{-2m}.
}
\tag{9}
\]

More is true. Fix any `A>2` and define

\[
G_A:=\{i:q_i\ge e^{-A I/V}\}.
\]

For `i notin G_A`, equation (7) gives

\[
\Psi(q_i)\le\frac{2V}{AI}q_i.
\]

Consequently

\[
\sum_{i\notin G_A}\Psi(q_i)
\le\frac{2V}{A}.
\]

On the other hand `Psi(q)<=q`, so (3) implies

\[
V\le\frac{2V}{A}+\sum_{i\in G_A}q_i.
\]

Thus

\[
\boxed{
\sum_{i:\,q_i\ge e^{-A I/V}}q_i
\ge\left(1-\frac2A\right)V,
\qquad A>2.
}
\tag{10}
\]

For example, at `A=4`, at least `V/2` total influence is carried by coordinates satisfying

\[
q_i\ge e^{-4I/V}.
\tag{11}
\]

So Booleanity does not merely force one non-tiny influence: a variance-sized amount of influence must live above a dimension-free exponential threshold determined only by `I/V`.

## 5. Decisive product-law obstruction

Take the abstract non-Boolean product law

\[
Q_n=\operatorname{Bernoulli}(1/n)^{\otimes n}.
\]

It has `I=1`, `q_*=1/n`, and

\[
V=1-(1-1/n)^n\to1-e^{-1}.
\]

If it were a Boolean spectral law, (8) would imply

\[
1-(1-1/n)^n\le\frac{2}{\ln n}.
\tag{12}
\]

Already at `n=64`,

\[
1-(63/64)^{64}\approx0.6350135,
\qquad
2/\ln64\approx0.4808983,
\]

so (12) fails by about `0.1541151`.

This is stronger than the earlier exact-product endpoint in a useful sense: it excludes a quantitative neighbourhood of the tiny-marginal regime through a continuous influence-profile inequality, without assuming coordinate independence of the candidate Boolean law.

## 6. A sharper relaxed obstruction: sparse burst laws survive the integrated profile test

The integrated profile inequality does **not** by itself imply FEI. Consider the abstract law

\[
\nu_{n,L}
=\left(1-\frac1L\right)\delta_\varnothing
+\frac1L\operatorname{Unif}\{S:|S|=L\}.
\tag{13}
\]

Then

\[
I=1,\qquad V=1/L,\qquad q_i=1/n.
\]

Condition (8) is compatible with this family whenever roughly

\[
L\ge\frac12\ln n.
\tag{14}
\]

Yet

\[
H(\nu_{n,L})
=h_2(1/L)+\frac1L\log_2\binom nL,
\tag{15}
\]

which is unbounded when `L` grows only logarithmically. For instance `n=4096, L=8` gives

\[
I=1,\qquad H\approx10.6299299161.
\]

Thus any completion of APPROACH 2/13 must use more than the integrated influence profile.

### Full block-Laplace stress test (numerical only)

I also exhaustively evaluated the *full* previously proved block-Laplace inequality over every symmetry type `(j,t,a,y)` for the burst law, where

- `j=|J|`,
- `t=|T|`,
- `a=|J cap T|`,
- `y` is the parity cell,

on a finite grid of `s` values.

For the following even-layer cases, no nondegenerate violation was found:

- `(n,L)=(12,4)`,
- `(16,4)`,
- `(18,6)`,
- `(24,6)`.

A finer `s=k/100`, `0<=k<=100`, sweep likewise found no violation in those cases; `s=1` is equality by definition. By contrast small cases such as `(8,4)` do violate the `s=0` atom endpoint.

This finite computation is **not** a proof that any asymptotic burst family satisfies all block-Laplace constraints. It identifies the next decisive subproblem: prove or refute that an even logarithmic layer `L≈c log n` can satisfy the complete block-Laplace family. If yes, magnitude/support hypercontractivity alone cannot close FEI and a genuinely joint phase/integrality constraint is necessary. If no, the violating block/centre/scale should yield the missing stronger profile inequality.

## 7. Relation to the previous random-chain reduction

The earlier B13 random-chain report obtained

\[
H(f)\le(2+\log_2 e)I(f)+C_{\rm br}(f),
\]

leaving branch/final-set mutual information as the unpaid term. Equations (4) and (10) provide a new universal constraint available for that remaining term: rare next-coordinate labels cannot all come from globally tiny-influence coordinates unless the spectral set is correspondingly large.

I do **not** yet have a summable inequality of the form `C_br<=C I`; that is the remaining universal gap on this route.

## 8. Next move

Two nonduplicative continuations are now precise.

1. **Burst-law decision problem.** Prove/disprove the complete block-Laplace family for `nu_{n,L}` with even `L≈c log n`. This determines whether the entire present magnitude-only block constraint is intrinsically insufficient.
2. **Branch-information payment.** Insert the localization estimate (10) into the random-prefix representation of `C_br`, seeking a stopping-time/charging rule in which an informative next coordinate is charged either to its own influence or to the logarithmically forced companion mass. A valid charge must telescope without reusing the same spectral mass.

Until one of these closes universally, full FEI remains OPEN.
