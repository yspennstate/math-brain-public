# Positive perturbations remove the archived five-type multiplicity

Parent derivation, 14 September 2026. The operator \(W\) below is the existing five-type example in the project's QSO manuscript, reviewed by [agent006](agents/006.md). This note classifies its whole segment toward the equiprobable operator. [Independent audit052](agents/052.md) passed the complete path classification, boundary-branch derivatives, and instability statement; the parent independently read that full audit. No historical-novelty claim is made.

Let \(F=\{1,2,3\}\). On the five-type simplex, write
\[
W_k(x)=\frac{x_a^2+x_b^2}{2}+2x_ax_b+\frac23x_4x_5,
\quad k\in F,\quad\{a,b\}=F\setminus\{k\},
\]
\[
W_4(x)=x_5\bigl(2x_1+2x_2+2x_3+x_5\bigr),\qquad
W_5(x)=x_4\bigl(2x_1+2x_2+2x_3+x_4\bigr).
\tag{1}
\]
This is the archived strictly non-Volterra operator. Let \(E\) be the equiprobable five-type operator: an equal-parent pair gives probability \(1/4\) to each allowed type, and a distinct-parent pair gives probability \(1/3\) to each allowed type. Define
\[
W_\varepsilon=(1-\varepsilon)W+\varepsilon E,
\qquad 0\le\varepsilon\le1.
\tag{2}
\]
Every allowed coefficient is strictly positive when \(\varepsilon>0\).

**Theorem.** For every \(0<\varepsilon\le1\), \(W_\varepsilon\) has exactly one fixed point in the closed simplex. It is interior and has the form
\[
p_\varepsilon=(r_\varepsilon,r_\varepsilon,r_\varepsilon,
 s_\varepsilon,s_\varepsilon),\qquad
r_\varepsilon=\frac{1-2s_\varepsilon}{3},
\]
where \(s_\varepsilon\) is the unique root in \([0,1/2]\) of
\[
(-108+113\varepsilon)s^2+(36-92\varepsilon)s+11\varepsilon=0.
\tag{3}
\]
It satisfies \(1/5\le s_\varepsilon<1/3\). At \(\varepsilon=0\), there are exactly two fixed points, corresponding to \(s=0\) and \(s=1/3\). Thus multiplicity disappears for every positive amount of this admissible perturbation.

For every \(0<\varepsilon\le6/17\), the unique interior fixed point has a real tangent eigenvalue below \(-1\). In particular it is unstable for the unaveraged map despite its uniqueness and strictly positive allowed coefficients.

## 1. Every fixed point has the displayed symmetry

The coefficient definition of \(E\) gives
\[
E_i(x)=\frac{(1-x_i)^2}{3}-\frac1{12}\sum_{j\ne i}x_j^2,
\]
and therefore
\[
E_i(x)-E_j(x)
=-(x_i-x_j)\left(\frac23-\frac5{12}(x_i+x_j)\right).
\tag{4}
\]
The factor in parentheses is at least \(1/4\) on the simplex.

For distinct \(i,j,k\in F\), the original operator has
\[
W_i(x)-W_j(x)
=-(x_i-x_j)\left(\frac{x_i+x_j}{2}+2x_k\right).
\tag{5}
\]
For the remaining pair,
\[
W_4(x)-W_5(x)=-(x_4-x_5)(2-x_4-x_5).
\tag{6}
\]
Every factor in (5)–(6) is nonnegative. Equations (4)–(6) imply that at a fixed point of any convex combination (2), each tested coordinate difference satisfies \(d=-c d\) with \(c\ge0\). It must vanish. Thus \(x_1=x_2=x_3=r\) and \(x_4=x_5=s\), with \(3r+2s=1\) and \(0\le s\le1/2\). This conclusion holds for every fixed point, including boundary points.

## 2. One scalar equation classifies the full path

At the symmetric vector above, direct substitution gives
\[
W_4=W_5=s(2-3s),\qquad
E_4=E_5=\frac{11-20s+5s^2}{36}.
\tag{7}
\]
The equation for a last coordinate is exactly (3). Conversely, if (3) holds, both last coordinates are fixed. The first three output coordinates are equal by permutation symmetry; their sum is \(1-2s\) by stochasticity, so each equals \(r\). Hence every root in the interval gives a fixed point, with no additional equation to check.

Call the polynomial in (3) \(Q_\varepsilon(s)\). For \(\varepsilon>0\),
\[
Q_\varepsilon(0)=11\varepsilon>0,\qquad
Q_\varepsilon(1/2)=-9-\frac{27}{4}\varepsilon<0.
\tag{8}
\]
A polynomial of degree at most two with opposite, nonzero endpoint signs has exactly one root in the interval: two distinct interior roots would produce two sign changes, and a double root would produce none. The linear case is immediate. Thus (8) proves existence and uniqueness without a numerical root count.

The sharper location follows from
\[
Q_\varepsilon(1/5)=\frac{72}{25}(1-\varepsilon)\ge0,
\qquad Q_\varepsilon(1/3)=-\frac{64}{9}\varepsilon<0.
\tag{9}
\]
This also proves interiority. At \(\varepsilon=0\), the scalar equation is \(36s-108s^2=0\), giving exactly the two archived fixed points
\[
(1/3,1/3,1/3,0,0),\qquad
(1/9,1/9,1/9,1/3,1/3).
\]

For reference, the discriminant of (3) is
\[
36(36-52\varepsilon+97\varepsilon^2)>0.
\tag{10}
\]
The quadratic inside is positive for every real \(\varepsilon\), as its discriminant is negative. A formula avoiding division by the quadratic coefficient is
\[
s_\varepsilon=
\frac{22\varepsilon}
{92\varepsilon-36+6\sqrt{36-52\varepsilon+97\varepsilon^2}},
\qquad \varepsilon>0.
\tag{11}
\]
Its denominator is positive: when the quadratic coefficient is negative, the square root of the full discriminant exceeds the absolute value of the linear coefficient; when that coefficient is nonnegative, the linear coefficient is negative. Equation (11) includes the linear case \(\varepsilon=108/113\).

The branch approaching the old boundary root has derivative \(s'(0)=-11/36\), so it exits the simplex. The physical branch instead approaches \(s=1/3\) and has derivative \(-16/81\) there. The scalar proof above establishes uniqueness for the entire positive parameter interval, beyond this local explanation.

## 3. Uniqueness still permits instability

At the fixed point, symmetry makes \(e_4-e_5\) a tangent eigenvector. From (4) and (6), its eigenvalue is
\[
\mu_\varepsilon=-\left[(1-\varepsilon)(2-2s_\varepsilon)
 +\varepsilon\left(\frac23-\frac56s_\varepsilon\right)\right].
\tag{12}
\]
Since \(s_\varepsilon<1/3\) whenever \(\varepsilon>0\),
\[
-\mu_\varepsilon>
(1-\varepsilon)\frac43+\varepsilon\frac7{18}
=\frac43-\frac{17}{18}\varepsilon.
\]
For \(0<\varepsilon\le6/17\), the right side is at least one, proving \(\mu_\varepsilon<-1\). The fixed point is interior, so this is a feasible tangent instability; no boundary-index interpretation is involved.

This note does not establish uniqueness for arbitrary positive five-type coefficient arrays. It classifies the specific segment (2) and shows why the archived example does not supply robust multiplicity by mixing it with \(E\). The classification of general five-type operators remains separate.
