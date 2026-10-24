# Account04/B13 independent audit: definite and hyperbolic pair branches

## Verdict

**PASS, with one nonfatal exposition repair and one quantitative improvement.**

I independently reconstructed the definite-pair coarea formula, the indefinite
hyperbolic envelope, its infinite-line bathtub step, the full negative-half
potential, and the conditional averaging in the nine-eigenvalue theorem. No
fatal gap was found.

The indefinite-pair branch sharpens to

\[
20\left(8+\log\frac{1444}{5}\right)=273.31\ldots<274,
\]

rather than the earlier \(<337\) independent-reconstruction bound. The global
constant remains \(<375\), controlled by the no-pivot branch.

## Source pin

Primary source: yspennstate/math-open-problems commit
eeb752c8943536541b34b42b8bf48e924f4d3d2f, file
proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex,
blob 19fb119877426b640b2c0dae19ec2f78a399fe11, SHA-256
bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3.

Independent comparison: proofnet24/QFORM-density/nine-eigenvalues-paper-2026-09-24/paper.tex,
blob 823201f05363fcc60c38cce0feb5abb636f081d7.

## Definite pair: PASS

For positive definite \(B\), complete the square and write

\[
w=w_0+\sqrt{\delta/\mu_1}\cos\theta\,e_1+
       \sqrt{\delta/\mu_2}\sin\theta\,e_2.
\]

The Jacobian is \(1/(2\sqrt{\det B})\). A joint density bounded by \(M\)
therefore pushes forward to a density bounded by

\[
\frac1{2\sqrt{\det B}}\int_0^{2\pi}M\,d\theta
=\frac{\pi M}{\sqrt{\det B}}.
\]

Negating the form treats negative definite \(B\). This is a deterministic
change of variables and does not use independence after rotation.

## Hyperbolic coarea: PASS

For eigenvalues \(\mu_+>0>\mu_-\), set \(D=\mu_+|\mu_-|\). The two branches
of \(q=v+\delta\), \(\delta>0\), are

\[
w_\varepsilon(\delta,t)
=\varepsilon\sqrt{\delta/\mu_+}\cosh t\,e_+
+\sqrt{\delta/|\mu_-|}\sinh t\,e_-.
\]

Their Jacobian is \(1/(2\sqrt D)\), so against nonnegative test functions,

\[
p_q(v+\delta)
=\frac1{2\sqrt D}\sum_{\varepsilon=\pm1}
 \int_{\mathbb R}f_1(w_{\varepsilon,1}(t))
 f_2(w_{\varepsilon,2}(t))\,dt
\]

for almost every \(\delta>0\). This formulation remains valid after
conditioning without selecting density values on conditioning-dependent
exceptional slices.

Write a branch as \(ue^t+u'e^{-t}\), where

\[
|u|=|u'|=\frac12\sqrt{\delta\Lambda},
\qquad \Lambda=\mu_+^{-1}+|\mu_-|^{-1}.
\]

Choose an original coordinate \(i\) with
\(|u_i|\ge\sqrt{\delta\Lambda}/(2\sqrt2)\). On the positive tail its coordinate
is monotone and \(|y'(t)|\ge|y(t)|/3\). After the cutoff where \(|y|\ge m\ge1\),

\[
\int_T^\infty f_1f_2\,dt
\le3\int_{\substack{|y|\ge m\\\mathrm{one\ sign}}}
       \frac{f_i(y)}{|y|}\,dy
\le3\log(1+1/m)\le3\log2.
\]

The middle inequality needs no attained optimizer. Write the decreasing weight
as an integral of superlevel indicators and bound each overlap by the smaller
of the interval length and one.

For the negative tail one must reselect a coordinate \(j\) with
\(|u'_j|\ge\sqrt{\delta\Lambda}/(2\sqrt2)\). Both manuscripts use shorthand
that might be read as retaining \(i\); this explicit reselection is the only
wording repair found.

The tails and middle interval give

\[
p_q(z)\le D^{-1/2}
\left(6+\log_+\frac{16\sqrt D}{|z-v|}\right).
\]

## Full pair half-potential: PASS

After \(Z=(Q-v)/\sqrt D\), rearrangement by interval superlevels gives

\[
\int_{|z-a|\le\delta}|z-a|^{-1/2}
\left(6+\log_+\frac{16}{|z|}\right)dz
\le4\sqrt\delta\left(8+\log\frac{16}{\delta}\right).
\]

The complement contributes at most \(\delta^{-1/2}\). At
\(\delta=1/64\), the sum is \(12+5\log2<16\), hence

\[
\sup_a\mathbb E|Q-a|^{-1/2}<16D^{-1/4}.
\]

## New direct integration: indefinite pair below 274

The independent reconstruction proves

\[
\Pr(|R-a|<\rho)\le\min\{1,19\sqrt\rho\}
\]

whenever the quadratic matrix of \(R\) has norm at least one. If
\(19\sqrt c\ge1\), layer cake gives

\[
\begin{aligned}
\mathbb E\log_+\frac{c}{|R-a|}
&=\int_0^\infty\Pr(|R-a|<ce^{-u})\,du\\
&\le\int_0^\infty\min\{1,19\sqrt c\,e^{-u/2}\}\,du\\
&=2+2\log19+\log c.
\end{aligned}
\]

For an indefinite pivot with \(D\ge1/400\), its conditional critical value has
a Schur-complement quadratic matrix with at least seven eigenvalues of modulus
at least one. Taking \(c=16\sqrt D\ge4/5\) therefore yields

\[
p_Q(z)\le D^{-1/2}
\left(8+2\log19+\log(16\sqrt D)\right).
\]

With \(x=\sqrt D\ge1/20\), the right side is decreasing, since its numerator
is greater than one throughout this domain. Thus

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le20\left(8+\log\frac{1444}{5}\right)
=273.31\ldots<274.
}
\]

This is uniform in all affine terms, the remaining spectrum, dimension, and
rough cap-one product laws. Conditional domination is interpreted against
nonnegative test functions, so Tonelli proves absolute continuity and the
essential density bound.

## Scope

- The pair arguments pass.
- The negative-tail coordinate reselection is a nonfatal wording correction.
- The indefinite-pair branch improves to \(<274\).
- The global nine-eigenvalue theorem remains \(<375\).
- Continuity and the eight- and three-eigenvalue cases remain open.
