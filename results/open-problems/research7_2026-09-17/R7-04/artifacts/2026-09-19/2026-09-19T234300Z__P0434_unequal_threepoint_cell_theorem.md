# P0434 — a full unequal-mass three-point rank cell, plus completion of `Unif{1,2,c}`

Status: **PROVED PARTIAL** relative to Scully–Harchol-Balter–Scheller-Wolf (2020), Conjecture 8.1. This proves the factor-two inequality for a nontrivial open set of unequal-mass three-point laws and finishes the entire equal-probability family `Unif{1,2,c}`, but it does not prove the arbitrary-law source conjecture.

Source: Ziv Scully, Mor Harchol-Balter, Alan Scheller-Wolf, *Simple Near-Optimal Scheduling for the M/G/1*, Proc. ACM Meas. Anal. Comput. Syst. 4(1), Article 11 (2020), Section 8, Conjecture 8.1, arXiv:1907.10792, DOI 10.1145/3379477.

## 1. Family and rank cell

Let

\[
X\in\{1,2,2+d\},\qquad
\Pr(X=1)=p,\quad \Pr(X=2)=q,\quad \Pr(X=2+d)=r,
\]

with `p,q,r>0`, `p+q+r=1`, and write

\[
t=q+r=1-p.
\]

Consider the parameter cell

\[
\boxed{
0<r\le t^2,
\qquad
d>\frac{t^2}{pr}.
}
\tag{1.1}
\]

The second inequality is strict. The boundary is used only as a limiting algebraic certificate below; the actual policy topology changes there because of FCFS tie-breaking.

Define

\[
\mu=\mathbb E\min\{X,2\}=2-p=1+t,
\qquad
m=\mathbb EX=\mu+rd,
\]

and

\[
h=\frac{\mu}{1-r}.
\tag{1.2}
\]

### 1.1 M-SERPT has exactly two strict demotions

The SERPT values immediately after the two support points are

\[
S_1=1+\frac{rd}{t},
\qquad
S_2=d.
\]

The first strict comparison is

\[
S_1-m
=
\frac{prd-t^2}{t}>0.
\tag{1.3}
\]

Also, `r<=t^2` implies

\[
\frac{t^2}{pr}\ge \frac tq,
\]

because this inequality is equivalent to `t^2>=r`. Hence (1.1) gives `d>t/q`, and therefore

\[
d-S_1
=
\frac{qd-t}{t}>0.
\tag{1.4}
\]

Thus M-SERPT has the strict three-level feedback form

\[
\boxed{
[0,1):m,
\qquad
[1,2):S_1,
\qquad
[2,2+d):d,
\qquad
m<S_1<d.
}
\tag{1.5}
\]

### 1.2 Gittins has one terminal hill

The exact three-point Gittins candidates established in the preceding R7-04 work specialize on `[0,1)` to

\[
A_1(u)=\frac{1-u}{p},
\qquad
A_2(u)=\frac{\mu-u}{1-r},
\qquad
A_3(u)=m-u.
\tag{1.6}
\]

At age zero,

\[
A_2(0)\le A_1(0)
\iff
r\le t^2.
\]

Moreover

\[
\frac{t^2}{pr}\ge h
\iff
t^2\ge r,
\]

so (1.1) implies `d>h`, and

\[
m-h=r(d-h)>0.
\]

Therefore `A_2` starts below both `A_1` and `A_3`; because `A_2` has slope `-1/(1-r)<-1`, it stays below `A_3`, while `A_1` eventually takes over because it tends to zero at age 1. Hence the fresh Gittins rank is

\[
\boxed{r_G(0)=h.}
\tag{1.7}
\]

On `[1,2)`, the two candidates are

\[
B_1(u)=\frac{t(2-u)}q,
\qquad
B_2(u)=(2-u)+\frac{rd}{t}.
\tag{1.8}
\]

Their crossing distance is `qd/t`. Since (1.1) and `r<=t^2` imply `d>t/q`, the crossing lies outside the interval and

\[
r_G(u)=B_1(u),\qquad 1\le u<2.
\]

The age-one jump is not a genuine hill because

\[
B_1(1)=\frac tq\le h
\iff r\le t^2.
\tag{1.9}
\]

At age 2 the long job jumps to rank `d>h`, producing the only genuine hill; its deterministic residual rank then crosses back below the fresh threshold `h` at age `2+d-h`. Thus every long Gittins job has exactly one terminal recycled high-priority block of length

\[
\boxed{h.}
\tag{1.10}
\]

This is the unequal-mass analogue of the `5/2` recycle block in the preceding equal-probability calculation.

## 2. Exact all-load SOAP formulas

Let

\[
V=\mathbb E[\min\{X,2\}^2]=4-3p,
\qquad
M_2=\mathbb EX^2=p+4q+r(2+d)^2,
\]

\[
\alpha=1-\lambda,
\qquad
\beta=1-\lambda\mu,
\qquad
\rho=\lambda m<1.
\]

The common long-job worst-rank waiting term is

\[
W_\infty
=
\frac{\lambda M_2}{2(1-\rho)\beta}.
\tag{2.1}
\]

For M-SERPT, direct SOAP old/new-work accounting gives

\[
\boxed{
T_M(1)=1+\frac{\lambda}{2\alpha},
}
\tag{2.2}
\]

\[
\boxed{
T_M(2)=\frac2\alpha+
\frac{\lambda V}{2\alpha\beta},
}
\tag{2.3}
\]

and

\[
\boxed{
T_M(2+d)=W_\infty+\frac{2+d}{\beta}.
}
\tag{2.4}
\]

For Gittins define

\[
W_h=
\frac{\lambda(V+r h^2)}{2\beta}.
\tag{2.5}
\]

The `r h^2` term is exactly the squared old-work contribution of the recycled terminal block. The conditional means are

\[
\boxed{T_G(1)=1+W_h,}
\tag{2.6}
\]

\[
\boxed{T_G(2)=2+W_h,}
\tag{2.7}
\]

and

\[
\boxed{
T_G(2+d)=
W_\infty+
\frac{2+d-h}{\beta}+h.
}
\tag{2.8}
\]

These formulas are exact for every stable load in the rank cell (1.1).

## 3. Structural lemma: the far-tail location cancels from the policy gap

Let

\[
E_M=pT_M(1)+qT_M(2)+rT_M(2+d),
\qquad
E_G=pT_G(1)+qT_G(2)+rT_G(2+d),
\]

and `D=E_M-E_G`. From (2.2)–(2.8),

\[
\begin{aligned}
D={}&
p\left[\frac{\lambda}{2\alpha}-W_h\right]
+q\left[\frac{2\lambda}{\alpha}
+\frac{\lambda V}{2\alpha\beta}-W_h\right]
+r\frac{\lambda\mu h}{\beta}.
\end{aligned}
\tag{3.1}
\]

In particular,

\[
\boxed{\frac{\partial D}{\partial d}=0.}
\tag{3.2}
\]

This is the main structural handoff to P01-B: **within this rank topology, moving the far-tail atom changes the common heavy-traffic waiting term and the stability restriction, but does not change the M-SERPT-minus-Gittins mean-response penalty at fixed arrival rate.** The location of the last support point cancels completely from the gap.

The exact expanded rational form, independently regenerated by the certificate script, is

\[
D=
\frac{\lambda N(p,r,\lambda)}
{2(\lambda-1)(r-1)(1-\lambda(2-p))},
\tag{3.3}
\]

where

\[
\begin{aligned}
N={}&2\lambda p^2r-3\lambda p^2+\lambda pr^2-4\lambda pr+7\lambda p
-4\lambda r^2+4\lambda r-4\lambda\\
&-2p^2r+3p^2+3pr-7p+4r^2-4r+4.
\end{aligned}
\]

## 4. Tail-displacement monotonicity reduces the factor-two inequality to one boundary

Define

\[
F(d)=2E_G-E_M=E_G-D.
\tag{4.1}
\]

Because `D` is independent of `d`, all `d`-dependence in `F` comes from `E_G`. The only `d`-dependent Gittins conditional term is the long-job term. From (2.1),

\[
\frac{\partial W_\infty}{\partial d}
=
\frac{\lambda}{2\beta}
\left[
\frac{2r(2+d)}{1-\lambda m}
+
\frac{\lambda rM_2}{(1-\lambda m)^2}
\right]>0.
\]

Hence

\[
\boxed{
F'(d)=E_G'(d)
=r\left(\frac{\partial W_\infty}{\partial d}+\frac1\beta\right)>0.
}
\tag{4.2}
\]

Therefore the hardest point of the strict cell is the one-sided topology boundary

\[
d_0=\frac{t^2}{pr}.
\tag{4.3}
\]

At that boundary

\[
m_0=\mu+r d_0=\frac1p.
\tag{4.4}
\]

For every strict-cell stable point, `m>1/p`, so stability implies `lambda<p`. Thus write

\[
p=1-t,
\qquad
r=u t^2,\quad 0<u\le1,
\qquad
\lambda=xp,\quad 0<x<1.
\tag{4.5}
\]

It is enough to prove positivity of the continuation

\[
F_0(t,u,x)=\lim_{d\downarrow d_0}F(d).
\]

Notice that this is only an algebraic one-sided continuation of the strict-cell formulas; no claim is made that the policy at equality has the same tie topology.

## 5. Exact Bernstein certificate for the full unequal-mass cell

Exact elimination gives

\[
\boxed{
F_0(t,u,x)=
\frac{Q(t,u,x)}
{2(1-t)(1-x)(1-u t^2)
[1-x(1-t)]
[1-x(1-t^2)]}.
}
\tag{5.1}
\]

Every denominator factor is strictly positive for

\[
0<t<1,\qquad 0<u\le1,\qquad 0<x<1.
\]

The numerator has degree `(8,2,3)` and is

\[
\begin{aligned}
Q={}&2 t^{8} u^{2} x^{3} - t^{8} u^{2} x^{2} + t^{7} u^{2} x^{2} - 3 t^{7} u x^{3} + 2 t^{7} u x^{2} \\
&- 12 t^{6} u^{2} x^{3} + 15 t^{6} u^{2} x^{2} - 4 t^{6} u^{2} x + 9 t^{6} u x^{3} - 12 t^{6} u x^{2} + 2 t^{6} u x \\
&+ 16 t^{5} u^{2} x^{3} - 29 t^{5} u^{2} x^{2} + 12 t^{5} u^{2} x - 14 t^{5} u x^{3} + 21 t^{5} u x^{2} - 8 t^{5} u x \\
&+ 5 t^{5} x^{3} - 4 t^{5} x^{2} - 6 t^{4} u^{2} x^{3} + 14 t^{4} u^{2} x^{2} - 8 t^{4} u^{2} x \\
&+ 18 t^{4} u x^{3} - 27 t^{4} u x^{2} + 10 t^{4} u x - 13 t^{4} x^{3} + 17 t^{4} x^{2} - 4 t^{4} x \\
&- 15 t^{3} u x^{3} + 30 t^{3} u x^{2} - 14 t^{3} u x + 10 t^{3} x^{3} - 18 t^{3} x^{2} + 8 t^{3} x \\
&+ 5 t^{2} u x^{3} - 14 t^{2} u x^{2} + 11 t^{2} u x - 2 t^{2} u - 2 t^{2} x^{3} + 4 t^{2} x^{2} - 2 t^{2} x \\
&+ t x^{3} - 3 t x^{2} + 2 t x - x^{3} + 4 x^{2} - 5 x + 2.
\end{aligned}
\tag{5.2}
\]

Convert `Q` exactly to the tensor Bernstein basis on `[0,1]^3` at degrees `(8,2,3)`. There are `9*3*4=108` rational coefficients. The archived exact computation gives

- `90` coefficients strictly positive;
- `18` coefficients equal to zero;
- `0` negative coefficients;
- smallest strictly positive coefficient `1/112`.

The complete 108-entry coefficient table is archived in the `.out` certificate file. Therefore `Q>=0` on the closed cube. On the source-relevant interior `0<t<1`, `0<x<1`, `0<u<1`, every Bernstein basis function is positive and at least one coefficient is positive, so `Q>0`. On the allowed face `u=1`, the surviving degree-2 `u` coefficients include strictly positive entries, so the same strict positivity holds there for interior `t,x`.

Thus

\[
F_0(t,u,x)>0.
\]

By (4.2), every strict cell point has `F(d)>F_0>0`. Hence

\[
\boxed{
\frac{E_M}{E_G}<2
}
\tag{5.3}
\]

for **every stable load** and every three-point service law in (1.1).

This is a genuinely unequal-mass theorem; the equal-probability case is only one slice.

## 6. Corollary: finish the entire equal-probability family `Unif{1,2,c}`

Take `p=q=r=1/3` and write `c=2+d`.

The new cell condition becomes

\[
d>4\iff c>6.
\]

Equation (3.1) simplifies exactly to

\[
\boxed{
E_M-E_G
=
\frac{\lambda(37-39\lambda)}
{12(1-\lambda)(3-5\lambda)}.
}
\tag{6.1}
\]

Stability gives

\[
\lambda<\frac3{c+3}<\frac13.
\]

The derivative of the right-hand side has numerator

\[
127\lambda^2-234\lambda+111,
\]

whose discriminant is `-1632`, hence the gap is strictly increasing on this interval. Therefore

\[
E_M-E_G< D(1/3)=\frac34.
\]

Since `E_G>=EX=(c+3)/3>3`,

\[
\boxed{
\frac{E_M}{E_G}<1+\frac{3/4}{3}=\frac54<2
\qquad(c>6).
}
\tag{6.2}
\]

The preceding R7-04 theorem already proved

- ratio `=1` for `2<c<=9/2`, and
- ratio `<4/3` for `9/2<c<=6`.

Therefore the **entire** equal-probability three-point family satisfies

\[
\boxed{
X\sim\operatorname{Unif}\{1,2,c\},\ c>2
\Longrightarrow
\frac{E_M}{E_G}<\frac43<2,
}
\tag{6.3}
\]

where the strict `<4/3` is understood as the uniform bound obtained by combining the three topology cells (the neutral first cell has ratio 1 and the new last cell has the stronger `<5/4`).

## 7. Why this matters for the arbitrary-law worker

The transferable lemma is not merely another solved numeric family. In the cell above:

1. all far-tail dependence cancels from `D=E_M-E_G`;
2. the factor-two slack `F=2E_G-E_M` is strictly increasing when the final support point is moved outward at fixed masses and arrival rate;
3. consequently the full continuum of tail locations reduces to the **rank-topology boundary** where consecutive M-SERPT envelope levels first tie;
4. after that reduction, a fixed-degree positive polynomial certificate controls all masses and all stable loads.

This suggests an arbitrary-law strategy: decompose a service law into successive M-SERPT envelope valleys, show that moving mass farther into a terminal valley changes the M-SERPT/Gittins gap only through local recycle charges while increasing a common Gittins waiting term, and reduce each valley configuration to its envelope-contact boundary. The missing general theorem is precisely a multi-valley analogue of the cancellation (3.2) and monotonicity (4.2).

## 8. Exact certificate

Checker:
`research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T234000Z__P0434_unequal_threepoint_cell_certificate.py`

Executed output:
`research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T234000Z__P0434_unequal_threepoint_cell_certificate.out`

The output ends with `ALL_EXACT_CHECKS_PASS` and contains the complete 108-entry exact rational Bernstein table. This is self-validation/certification of the algebra, not an independent audit of the full source conjecture.

## 9. Remaining source gap

Conjecture 8.1 remains open here. Three-point laws outside (1.1) include other Gittins lower-envelope types, multiple pre-terminal recycle configurations, and cells where the fresh Gittins rank is `A1` or `A3` rather than `A2`. Larger finite supports can have several interacting valleys. The next useful finite-law objective is to derive the analogue of (3.2) for the neighboring three-point cells and determine whether every tail-location variable can be pushed to an envelope-contact boundary before optimizing masses/load.
