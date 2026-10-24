# Same-proof constant improvement: 10000 -> 3910

Run: `20260924T122831Z-account03-B19-FIXMULT-AUDIT-r56`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

This note does **not** change the eigenvalue threshold. It proves that the existing 17-eigenvalue manuscript argument, with no new probabilistic or structural hypothesis, gives

\[
\boxed{\|p_{X^TAX+b^TX+c}\|_\infty\le3910\,K^2/s.}
\]

All signs, dimensions, affine terms, remaining spectrum and arbitrary independent rough coordinate laws are retained.

## 1. Tighten only the quarter-power constant

In the manuscript's quarter-power lemma, the coefficient before `(rho/L)^(1/4)` is

\[
C_q=2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8).
\]

The manuscript relaxes this to `16`. We only need the elementary bound

\[
\boxed{C_q<24/5.}
\]

Here is a proof using rational inequalities only.

First,

\[
2^{5/8}<8/5,
\qquad
\pi^{-1/4}<4/5,
\qquad
e^{3/8}<3/2.
\]

The first follows after taking eighth powers. The second follows from `pi>3>(5/4)^4`. For the third, the exponential series gives

\[
e<\frac83+\frac5{96}=\frac{87}{32}<\frac{11}{4},
\]

and `(11/4)^3<(3/2)^8`, hence `e^{3/8}<3/2`.

For the gamma factor, on `0<=t<=1` the alternating Taylor polynomial gives

\[
e^{-t}\le1-t+\frac{t^2}{2}-\frac{t^3}{6}+\frac{t^4}{24}.
\]

Therefore

\[
\int_0^1 t^{-5/8}e^{-t}\,dt
\le
\frac83-\frac8{11}+\frac4{19}-\frac4{81}+\frac1{105}.
\]

Also `e>8/3`, so

\[
\int_1^\infty t^{-5/8}e^{-t}\,dt
\le e^{-1}<3/8.
\]

The sum is less than `5/2`; in fact the slack is

\[
\frac52-\left(
\frac83-\frac8{11}+\frac4{19}-\frac4{81}+\frac1{105}+\frac38
\right)
=\frac{70811}{4740120}>0.
\]

Thus `Gamma(3/8)<5/2`, and multiplying the four rational bounds yields

\[
C_q<\frac85\frac45\frac32\frac52=\frac{24}{5}.
\]

Hence the quarter-power concentration may be written

\[
\Pr\{|R-a|<\rho\}
\le
\min\left\{1,\frac{24}{5}(\rho/L)^{1/4}\right\}.
\]

## 2. Logarithmic potential

For `L>=1`, layer cake now gives

\[
\sup_a\mathbb E\log_+\frac1{|R-a|}
\le 4+4\log(24/5).
\]

Moreover

\[
\log(24/5)<19/12.
\]

Indeed, with `x=19/12`, positivity of the exponential series gives

\[
e^x>
\sum_{k=0}^{5}\frac{x^k}{k!}
=\frac{144615679}{29859840}
>
\frac{24}{5}.
\]

Therefore the logarithmic constant can be taken as

\[
\boxed{L_0<31/3.}
\]

## 3. Pivot half-potential constants

Keep the manuscript's `eta=1/100`.

For a scalar pivot,

\[
H(Q)
\le10(8+3L_0)
<10(8+31)=390.
\]

For a definite pair,

\[
H(Q)\le40\pi<390.
\]

For an indefinite pair, write `x=sqrt(D)>=1/10`. Since `16x>=8/5>1`, the conditional truncated half-potential is

\[
f(x)=\frac{32+4\log(16x)}{x}.
\]

Its derivative is

\[
f'(x)=-\frac{28+4\log(16x)}{x^2}<0,
\]

so the maximum occurs at `x=1/10`. Since `log(8/5)<1/2` (because `e^{1/2}>1+1/2+1/8=13/8>8/5`),

\[
H(Q)<10(32+2)=340<390.
\]

The no-pivot nine-direction branch already has full half-potential `<200`.

Consequently, under `s_9(A)>=1`,

\[
\boxed{
\sup_a\mathbb E|Q-a|^{-1/2}<391.
}
\]

In the pivot case this is `H(Q)<390` plus the outside-distance-one contribution `<1`; the no-pivot case is already `<200`.

## 4. Main theorem constants

Normalize to `K=s=1` as in the manuscript.

- No pivot: unchanged, `||p_Q||infinity<2400`.
- Scalar pivot: the Schur complement retains at least nine large directions, hence
  \[
  \|p_Q\|_\infty<10\cdot391=3910.
  \]
- Definite pair: unchanged, `<40`.
- Indefinite pair: the Schur remainder has operator norm at least one. With `x=sqrt(D)>=1/10`,
  \[
  p_Q(z)\le
  \frac{6+\log(16x)+L_0}{x}.
  \]
  This function is decreasing on `x>=1/10`; using `L_0<31/3` and `log(8/5)<1/2` gives
  \[
  \|p_Q\|_\infty
  <10\left(6+\frac12+\frac{31}{3}\right)
  =\frac{505}{3}<169.
  \]

Thus every normalized branch is below `3910`. Scaling back exactly as in the manuscript yields

\[
\boxed{
\|p_{X^TAX+b^TX+c}\|_\infty\le3910\,K^2/s
\quad\text{whenever }s_{17}(A)\ge s>0.
}
\]

No continuity claim beyond the manuscript's branchwise scope is added.
