# Addendum — the exact critical endpoint, if it exists at all, is forced to `m=3`

**Status:** **PROVED under the same simultaneous exact scalar-frontier critical-endpoint hypothesis as REPORT.md.** Full FEI remains **OPEN / NOT PROVED**. This addendum strengthens only the exact-equality endpoint analysis; it does not supply the required quantitative stability theorem.

The main report proved that exact Booleanity forces

\[
\theta=\frac1{m^2},\qquad
\tau=\frac1{m^2+1},\qquad
r=\kappa(\tau)
\]

for an integer `m>=2`. The argument below adds the *global* constraints `r=H/I` and Parseval/integer Fourier arithmetic. Those constraints eliminate every `m` except `m=3`.

## 1. Parseval forces the hard-core partition numerator to be a power of two

Let

\[
A_S:=2^n\widehat f(S)\in\mathbb Z.
\]

Let `d=max{|S|:S in mathcal F}`. From the exact endpoint law and `theta=1/m^2`,

\[
|A_S|=|A_\varnothing|m^{-|S|}.
\]

Choose a set of degree `d`. Then

\[
b:=|A_\varnothing|/m^d\in\mathbb N,
\qquad
|A_S|=b\,m^{d-|S|}.
\tag{A1}
\]

Parseval gives

\[
2^{2n}=\sum_S A_S^2
=b^2 Q,
\qquad
Q:=\sum_{S\in\mathcal F}m^{2(d-|S|)}\in\mathbb N.
\tag{A2}
\]

Since a product of the positive integers `b^2` and `Q` is a pure power of two, both have no odd prime factor. Hence

\[
\boxed{Q=2^L}
\tag{A3}
\]

for an integer `L>=0` (in fact `L` is even). Consequently

\[
p_S=\frac{m^{2(d-|S|)}}{2^L},
\qquad
I=\frac{R}{2^L}\in\mathbb Q,
\quad
R:=\sum_{S\in\mathcal F}|S|m^{2(d-|S|)}.
\tag{A4}
\]

The spectral entropy is therefore

\[
H
=\sum_Sp_S\bigl[L-2(d-|S|)\log_2m\bigr]
=L-2d\log_2m+2I\log_2m.
\]

Thus the global ratio of any exact Boolean hard-core endpoint satisfies

\[
\boxed{
\frac HI=\frac LI+\left(2-\frac{2d}{I}\right)\log_2m,
}
\tag{A5}
\]

so it lies in the two-dimensional `Q`-span of `1` and `log_2 m`.

## 2. Closed form for the scalar critical ratio

At

\[
\tau=\frac1{m^2+1},
\]

a direct simplification of

\[
\kappa(\tau)=\frac{h_2(\tau)+1-h_2(1/2+\sqrt{\tau(1-\tau)})}{\tau}
\]

gives

\[
\boxed{
 r_m=(m+1)^2\log_2(m+1)
 +(m-1)^2\log_2(m-1)
 -2m^2\log_2m.
}
\tag{A6}
\]

(The `m=2` term containing `log_2(m-1)` is zero.)

At a simultaneous exact *critical* endpoint, (A5) equals (A6). Therefore

\[
(m+1)^2\log_2(m+1)+(m-1)^2\log_2(m-1)
\in \operatorname{span}_{\mathbb Q}\{1,\log_2m\}.
\tag{A7}
\]

Clear denominators in this rational linear relation and exponentiate. Unique prime factorization then has an immediate consequence. Any odd prime dividing `m+1` divides neither `m` nor `m-1`, so it cannot occur on the right side generated only by powers of `2` and `m`; its positive coefficient in (A7) cannot cancel. Hence `m+1` has no odd prime divisor and is a power of two. The same argument applied to `m-1` shows that `m-1` is also a power of two.

Thus

\[
m-1=2^a,\qquad m+1=2^b,
\]

with `a,b>=0`, and

\[
2^b-2^a=2.
\]

The only solution is `a=1,b=2`, i.e.

\[
\boxed{m=3.}
\tag{A8}
\]

So if a simultaneous exact scalar-frontier critical Boolean endpoint exists at all, its parameters are forced to

\[
\boxed{
\theta=\frac19,\qquad
\tau=\frac1{10},\qquad
r=36-18\log_2 3
=7.4706749870191887\ldots.
}
\tag{A9}
\]

This is much stronger than the discrete sequence in the main report: all other reciprocal-square activities are incompatible with the *global* critical ratio.

## 3. Further necessary degree arithmetic; degrees 5 and 10 are impossible

For `m=3`, equations (A5) and (A9) read

\[
\frac LI+\left(2-\frac{2d}{I}\right)\log_2 3
=36-18\log_2 3.
\]

Since `log_2 3` is irrational (otherwise unique factorization would give `2^a=3^b` for positive integers), the rational and `log_2 3` coefficients agree separately:

\[
\boxed{I=\frac d{10},\qquad L=\frac{18d}{5}.}
\tag{A10}
\]

In particular

\[
\boxed{5\mid d.}
\tag{A11}
\]

Now let `M in mathcal F` have size `d`. Downward closure gives the whole cube `2^M subseteq mathcal F`. In the integer weights of (A2), that base cube contributes

\[
Q_0=\sum_{S\subseteq M}9^{d-|S|}=10^d,
\qquad
R_0=\sum_{S\subseteq M}|S|9^{d-|S|}=d10^{d-1},
\]

so its weighted mean size is already exactly `d/10`, the value required by (A10). Therefore if there are extra support sets outside `2^M`, their own `9^{d-|S|}`-weighted average size must also equal `d/10`.

### Degree `d=5`

The required extra average is `1/2`, but every set outside `2^M` is nonempty and has size at least one. Hence there can be no extra set. Then `Q=10^5`, contradicting (A3) and (A10), which require

\[
Q=2^L=2^{18}.
\]

So `d=5` is impossible.

### Degree `d=10`

The required extra average is one. Since every extra set has size at least one, equality forces *every* extra set to be a singleton outside `M`. If there are `s` such singletons, then

\[
Q=10^{10}+s9^9.
\]

But (A10) requires `Q=2^{36}`. Exact integer division gives

\[
2^{36}-10^{10}=58,719,476,736,
\]

while

\[
9^9=387,420,489,
\]

and

\[
58,719,476,736\equiv218,982,897\pmod{387,420,489}.
\]

Thus no integer `s` exists. Degree `10` is impossible.

Combining with (A11), any exact critical endpoint that survives all current arithmetic conditions must satisfy

\[
\boxed{d\ge15.}
\tag{A12}
\]

Together with the main report's link theorem at `m=3`, every relevant coordinate would also need at least seven Fourier co-neighbors and at least ten active lower-link fibres.

## 4. What this does and does not close

This addendum **eliminates every exact critical hard-core endpoint except one sharply specified candidate regime**:

\[
\theta=1/9,\quad\tau=1/10,\quad r=7.470674987\ldots,\quad d\in15,20,25,\ldots
\]

with the stated link-expansion conditions. It does **not** rule out approximate endpoint sequences, and it does not prove FEI. The full conjecture remains **OPEN**.

The next full-scope obligation is still quantitative stability: show that a critical core near the scalar frontier either pays a dimension-free amount of scalar slack, or its approximately geometric signed Fourier links force enough global dependence/recombination payment to select a coordinate. The exact arithmetic classification gives a much narrower target for that stability theorem but is not itself the theorem.
