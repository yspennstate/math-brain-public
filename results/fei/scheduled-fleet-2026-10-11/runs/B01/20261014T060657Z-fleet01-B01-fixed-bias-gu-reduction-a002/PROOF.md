# Fixed-bias hardness reduction for GU

All logarithms are base two.  For a Boolean sign \(q\), define, on two
fresh uniform inputs \(y,z\),

\[
\mathcal T(q)(z,y,x)=
\begin{cases}
1,&z=+1,\\
yq(x),&z=-1.
\end{cases}
\]

Write \(m=\mathbb E q\).  The result is an exact hardness-preserving
reduction, not a proof of GU.

## 1. Exact spectral law

Expanding

\[
\mathcal T(q)=\frac{1+z}{2}+\frac{1-z}{2}yq
\]

gives

\[
p_{\mathcal T(q)}(\varnothing)
=p_{\mathcal T(q)}(\{z\})=\frac14,
\]

and, for every Fourier label \(S\) of \(q\),

\[
p_{\mathcal T(q)}(S\cup\{y\})
=p_{\mathcal T(q)}(S\cup\{y,z\})
=\frac14p_q(S). \tag{1}
\]

In particular,

\[
\mathbb E\mathcal T(q)=\frac12. \tag{2}
\]

Summing the set sizes in (1) gives

\[
I(\mathcal T(q))=1+\frac12I(q). \tag{3}
\]

For \(S\cup\{y\}\), the upper-set mass is \(\pi_q(S)/2\);
for \(S\cup\{y,z\}\), it is \(\pi_q(S)/4\).  The
\(\varnothing\), \(\{z\}\), and extra factor-two terms contribute
one bit in total.  Hence

\[
U(\mathcal T(q))=1+\frac12U(q). \tag{4}
\]

## 2. Exact restriction drift

Let \(A(q)\) be the fair activation that equals \(1\) in one selector
branch and \(q\) in the other.  Its exact upper-set formula is

\[
U(A(q))=\frac12U(q)+R(\mathbb E q), \tag{5}
\]

where, with \(h(u)=u\log_2(1/u)\) and zero terms interpreted
continuously,

\[
R(t)=h\!\left(\frac{(1+t)^2}{4}\right)
+\frac12h\!\left(\frac{(1-t)^2}{4}\right)
-\frac12h(t^2)+\frac{1-t^2}{4}. \tag{6}
\]

The selector restriction of \(\mathcal T(q)\) gives \(1\) and
\(yq\), so (4) implies

\[
\Delta_zU(\mathcal T(q))=1.
\]

The balancing-input restrictions give \(A(q)\) and \(A(-q)\), hence

\[
\Delta_yU(\mathcal T(q))
=1-\frac{R(m)+R(-m)}2.
\]

Every old physical restriction commutes with \(\mathcal T\), and (4)
then gives

\[
\Delta_iU(\mathcal T(q))=\frac12\Delta_iU(q).
\]

Therefore

\[
\boxed{
G(\mathcal T(q))=\frac12G(q)+\kappa(m),
\qquad
\kappa(m)=2-\frac{R(m)+R(-m)}2.
} \tag{7}
\]

The correction is uniformly bounded.  Since
\(0\le h(u)<1\) for \(u\in[0,1]\), (6) yields

\[
-\frac12\le R(t)\le\frac74,
\qquad
\frac14\le\kappa(t)\le\frac52. \tag{8}
\]

Only boundedness is needed below.

## 3. Fixed-bias GU with a sublinear terminal is universal

Fix \(0\le a<\infty\), \(0\le b<1\), and a real sequence
\((e_N)\) satisfying

\[
\frac{|e_N|}{N}\longrightarrow0.
\]

Assume that every Boolean sign \(F\) on every \(N\)-cube with
\(\mathbb E F=1/2\) satisfies

\[
\boxed{G(F)\le aI(F)+bU(F)+e_N.} \tag{FB}_{1/2}
\]

Let \(q\) be any nonconstant Boolean sign on \(n\) inputs.  For
\(t\ge1\), let \(q_t=q^{\otimes t}\) on disjoint blocks.  Exact
tensor additivity gives

\[
(G,I,U)(q_t)=t(G,I,U)(q),\qquad \mathbb E q_t=m^t.
\]

Apply \((\mathrm{FB}_{1/2})\) to
\(F_t=\mathcal T(q_t)\), which has \(N_t=tn+2\) inputs and mean
\(1/2\).  Equations (3), (4), and (7) give

\[
\frac t2G(q)+\kappa(m^t)
\le a\left(1+\frac t2I(q)\right)
+b\left(1+\frac t2U(q)\right)+e_{tn+2}.
\]

Equivalently,

\[
G(q)\le aI(q)+bU(q)
+\frac{2(a+b-\kappa(m^t))}{t}
+\frac{2e_{tn+2}}{t}. \tag{9}
\]

The first error tends to zero by (8), and

\[
\frac{e_{tn+2}}t
=\frac{e_{tn+2}}{tn+2}\frac{tn+2}{t}\longrightarrow0.
\]

Letting \(t\to\infty\) in (9) proves

\[
\boxed{G(q)\le aI(q)+bU(q)}
\]

for every nonconstant \(q\).  Constants have \(G=I=U=0\).

Conversely, the universal exact GU inequality trivially implies
\((\mathrm{FB}_{1/2})\) with \(e_N=0\).  Thus universal GU with a
given pair \((a,b)\) is equivalent to GU on the single output-bias slice
\(\mathbb EF=1/2\), even after permitting a uniform sublinear
dimension terminal on that slice.

## 4. Consequence and exact scope

The source-reviewed restriction induction then gives

\[
U(f)\le\frac{a}{1-b}I(f),\qquad
H(f)\le\left(2+\frac{2a}{1-b}\right)I(f).
\]

No pair \((a,b)\) satisfying \((\mathrm{FB}_{1/2})\) is proved here.
The theorem identifies a strictly smaller hardness-equivalent target.  It
also shows that vanishing output bias cannot be the sole universal
obstruction: every seed, including rare and near-constant seeds, embeds
into functions having the fixed Fourier mass
\(p_{\varnothing}=1/4\).

The reduction retains two fresh coordinates and disjoint tensor copies.
Those are used only for the hardness embedding; no claim is made that the
fixed-bias slice is restriction-closed.
