# Arbitrary weighted `K_{2,3}` apex stability

## Status and theorem

**Proved, with exact symbolic verification and an independent reconstruction.**
This is a complete theorem for one backbone graph, not a solution of the
general forest negative-association conjecture.

Let `K_{2,3}` have endpoint side `{0,1}` and arm side `{2,3,4}`, with arbitrary
positive weights

\[
 (w_{02},w_{03},w_{04};w_{12},w_{13},w_{14})=(a,b,c;d,e,f).
\]

After adjoining an apex `*` and assigning independent variables `z_i` to the
five apex edges, the complete forest polynomial `P(z_0,...,z_4)` is real
stable.  Hence the five apex-edge indicators are strongly Rayleigh and
negatively associated under arbitrary positive external fields and
positive-probability spoke conditioning.

This removes the rank-one restriction from the preceding checkpoint and
covers all six positive backbone activities.

## 1. Construction and criterion

For every backbone forest `A`, an apex-spoke subset remains acyclic exactly
when it chooses at most one vertex from each component.  Therefore

\[
 P(z)=\sum_{A\text{ forest}}w(A)
 \prod_{C\in\operatorname{comp}(A)}\left(1+\sum_{i\in C}z_i\right).
\]

There are 54 backbone forests, 32 spoke monomials, and 712 augmented forests
at unit weights.  Put

\[
 \Delta_{ij}=P_iP_j-PP_{ij}.
\]

For a real multiaffine polynomial, real stability is equivalent to
`Delta_ij>=0` at every real specialization for every pair.  Column
permutations and endpoint exchange reduce the ten pairs to the three generic
types `(0,1)`, `(0,2)`, `(2,3)`, with simultaneous relabeling of the six
parameters.

## 2. Positive helper polynomials

Define

\[
 R(u,v;r,s)=(1+u+v)(1+r)(1+s)+uv(1+r+s)>0
\]

and, for two columns `(u,r),(v,s)`,

\[
 T(u,v;r,s)=us(u+1)(s+1)+vr(v+1)(r+1)-2uvrs.
\]

To prove `T>0`, set
`A=us(u+1)(s+1)` and `B=vr(v+1)(r+1)`.  Since

\[
 AB=uvrs(u+1)(v+1)(r+1)(s+1)>(uvrs)^2,
\]

strict AM--GM gives `A+B>2uvrs`.

Finally define the coefficient-positive 54-term polynomial

\[
\begin{aligned}
Q={}&(1+a+b+c)(1+d)(1+e)(1+f)\\
&+ab(1+f)(1+d+e)+ac(1+e)(1+d+f)\\
&+bc(1+d)(1+e+f)+abc(1+d+e+f).
\end{aligned}
\]

## 3. Endpoint--endpoint pair

Set

\[
 x=z_3+1+b+e,\qquad y=z_4+1+c+f,
\]

and collect `Delta_01` as a quadratic in `t=z_2`.  Its leading coefficient is

\[
 A_{01}=cf(c+1)(f+1)x^2+2bcefxy+be(b+1)(e+1)y^2.
\]

The determinant of this binary form is

\[
 bcefR(b,c;e,f)>0.
\]

Its discriminant factors as

\[
 D_{01}=-4ad\,x^2y^2\Phi(x,y),
\]

where the two diagonal coefficients of `Phi` are coefficient-positive and

\[
 \det\Phi=bcef(a+1)(d+1)Q>0.
\]

Thus `A_01` and `Phi` are positive definite.  The only degenerate point is
`x=y=0`; the complete axis formulas are

\[
\begin{aligned}
 \Delta_{01}|_{x=0}&=be(b+1)(e+1)y^2(t+a+d+1)^2,\\
 \Delta_{01}|_{y=0}&=cf(c+1)(f+1)x^2(t+a+d+1)^2.
\end{aligned}
\]

Therefore `Delta_01>=0` globally.

## 4. Endpoint--internal pair

Use the same `x,y` and collect `Delta_02` in `t=z_1`.  Exact expansion gives

\[
 A_{02}=a(a+1)x^2y^2,\qquad D_{02}=D_{01}.
\]

The generic case follows from the preceding discriminant certificate.  The
two entire zero-leading axes are

\[
\begin{aligned}
 \Delta_{02}|_{x=0}&=e(e+1)T(a,b;d,e)y^2,\\
 \Delta_{02}|_{y=0}&=f(f+1)T(a,c;d,f)x^2.
\end{aligned}
\]

They are nonnegative by the strict AM--GM lemma.  Parameter relabeling and
endpoint exchange cover all six endpoint--internal pairs.

## 5. Internal--internal pair

Put

\[
 x=z_0+1+a+b+c,\qquad y=z_1+1+d+e+f,
\]

and collect `Delta_23` in the unused spoke `t=z_4`.  Its leading coefficient
is

\[
 A_{23}=de(d+1)(e+1)x^2+2abde,xy+ab(a+1)(b+1)y^2,
\]

with determinant

\[
 abdeR(a,b;d,e)>0.
\]

Write the discriminant as `D_23` and the binary form `-D_23=Ux^2+2Vxy+Wy^2`.
The diagonal expansions `U,W` now contain negative coefficients, so a
coefficientwise proof would be invalid.  The exact determinant instead is

\[
 UW-V^2=16abcdef\,
 T(a,b;d,e)T(a,c;d,f)T(b,c;e,f)Q>0.                 \tag{1}
\]

It remains to justify the sign of `U`, not merely its nonvanishing.  Equation
(1) implies `U` can never be zero on the positive orthant, since at such a
point the determinant would be `-V^2<=0`.  The positive orthant is connected,
so the continuous function `U` has constant sign there.  At
`a=b=c=d=e=f=1`, exact evaluation gives `U=432>0` (and `W=432`).  Hence
`U>0` everywhere, and (1) makes `-D_23` positive definite.

At the sole degenerate point of `A_23`, namely `x=y=0`, direct substitution
gives

\[
 \Delta_{23}=T(a,c;d,f)T(b,c;e,f)>0.
\]

Thus `Delta_23>=0`; column permutations cover all three internal pairs.  All
ten Rayleigh differences are nonnegative, proving the theorem.

## 6. Consequences and limits

Every nonzero nonnegative profile specialization `z_i=t beta_i` is
real-rooted; positivity of the coefficients and constant term puts every
root strictly on the negative real axis.  The previously audited four-core
Stieltjes transfer therefore gives the inherited proportional-row
disjoint-marked-edge negative-correlation corollary.

This theorem does **not** cover theta subdivisions, arbitrary graph
backbones, conditioning on backbone edges, nonproportional external marked
rows, or joint negative association involving backbone and spoke variables.
The famous arbitrary-graph forest conjecture remains open.

