# I0125 artifact: exact one-root escape tube and robust A4 barrier

Target: five-dimensional kissing number in spherical-code normalization. This artifact proves two restricted structural statements. Neither changes the unrestricted interval `40 <= tau_5 <= 44`.

## Notation

Let

\[
H=\{y\in\mathbb R^5:\sum_{i=1}^5y_i=0\},\qquad
w=\frac1{\sqrt5}(1,1,1,1,1),
\]

and let

\[
r_{ij}=\frac{e_i-e_j}{\sqrt2}\in H\qquad(i\ne j)
\]

be the 20 roots of `A_4`. Every `x in S^4` decomposes uniquely as

\[
x=h w+y,\qquad y\in H,\qquad h^2+\|y\|^2=1.
\]

The kissing inequality against a root is

\[
\langle x,r_{ij}\rangle=\frac{y_i-y_j}{\sqrt2}\le\frac12.
\]

## Theorem 1: exact escape tube after deleting one oriented root

Assume a kissing code contains every `A_4` root except `r_{12}`. Let `x=h w+y` be any other code point and put

\[
a:=\langle y,r_{12}\rangle=\frac{y_1-y_2}{\sqrt2}.
\]

If `a<=1/2`, then `x` also satisfies the missing root inequality, so the full-`A_4` argument applies and

\[
|h|\ge\sqrt{\frac25}.
\]

If `1/2<=a<=1`, then the following sharp inequalities hold:

\[
\boxed{\|y\|^2\le a^2+\frac75(1-a)^2
      =\frac{12a^2-14a+7}{5}},
\]

\[
\boxed{h^2\ge\frac{2(1-a)(6a-1)}5},
\]

and, after writing `y=a r_{12}+z` with `z perpendicular r_{12}` inside `H`,

\[
\boxed{\|z\|^2\le\frac75(1-a)^2}.
\]

In particular the height gap collapses continuously and sharply at the missing root: at `a=1`, equality is attained by `x=r_{12}`, for which `h=0`.

### Proof

Scale `Y=sqrt(2)y`. Then every retained oriented root inequality becomes

\[
Y_i-Y_j\le1
\]

for every ordered pair `(i,j)` except `(1,2)`. Put

\[
d:=Y_1-Y_2=2a\in[1,2],\qquad
m:=\frac{Y_1+Y_2}{2},\qquad
q:=1-\frac d2\in[0,1/2].
\]

For each `k in {3,4,5}`, the retained inequalities `Y_1-Y_k<=1` and `Y_k-Y_2<=1` give

\[
m-q\le Y_k\le m+q.
\]

Write `Y_k=m+u_k`, so `u_k in [-q,q]`. With `S=u_3+u_4+u_5`, the zero-sum condition on `Y` gives

\[
5m+S=0,\qquad m=-S/5.
\]

Now compute exactly:

\[
\begin{aligned}
\|Y\|^2
&=(m+d/2)^2+(m-d/2)^2+\sum_{k=3}^5(m+u_k)^2\\
&=\frac{d^2}{2}+\sum_{k=3}^5u_k^2-\frac{S^2}{5}.
\end{aligned}
\]

The quadratic form

\[
F(u_3,u_4,u_5)=\sum u_k^2-\frac{(\sum u_k)^2}{5}
\]

is convex (its Hessian has eigenvalues `2,2,4/5`). Hence its maximum on the cube `[-q,q]^3` is attained at a vertex. At a vertex, `sum u_k^2=3q^2` and `S^2` is either `q^2` or `9q^2`; the maximum occurs for a two-versus-one sign split and equals `14q^2/5`. Therefore

\[
\|Y\|^2\le\frac{d^2}{2}+\frac{14}{5}\left(1-\frac d2\right)^2.
\]

Divide by two and substitute `d=2a`:

\[
\|y\|^2\le a^2+\frac75(1-a)^2.
\]

The height inequality follows from `h^2=1-||y||^2`, and the perpendicular inequality follows from `||z||^2=||y||^2-a^2`. Equality at `a=1` is the missing root itself. QED.

## Consequence: the exact A4 argument is genuinely brittle under one-root deletion

The previous I0125 theorem used the full 20-root section to force `|h|>=sqrt(2/5)` for every extra point. Theorem 1 shows that deleting only one oriented root destroys every positive uniform height lower bound: the missing root is itself an admissible equatorial limit point, and points violating the missing inequality are confined only to the sharp tube

\[
\|z\|\le\sqrt{\frac75}(1-a),\qquad
|h|\ge\sqrt{\frac{2(1-a)(6a-1)}5}.
\]

Thus a one-root-deletion continuation cannot simply reuse the Petersen projection threshold unchanged.

## Theorem 2: quantitative robust A4-neighborhood barrier

Let

\[
\sigma_{11}:=\min_{u_1,\dots,u_{11}\in S^3}\max_{i<j}\langle u_i,u_j\rangle.
\]

Bachoc--Vallentin's theorem `A(4,1/6)=10` and compactness imply

\[
\sigma_{11}>\frac16.
\]

Define

\[
\varepsilon_*:=\min\left\{
\frac{\sqrt5-2}{4},
\frac12\left(\sqrt{\frac{5}{6(1-\sigma_{11})}}-1\right)
\right\}>0.
\]

Suppose a five-dimensional kissing code `C` contains 20 labeled points `q_{ij}` (`i ne j`) such that, after one ambient orthogonal transformation,

\[
\|q_{ij}-r_{ij}\|\le\varepsilon<\varepsilon_*
\]

for every `i ne j`. Then

\[
\boxed{|C|\le40}.
\]

### Proof

Let `x=h w+y` be any code point outside these 20 distinguished points. Since `x.q_{ij}<=1/2` and `||x||=1`,

\[
\langle x,r_{ij}\rangle
\le\langle x,q_{ij}\rangle+\|q_{ij}-r_{ij}\|
\le\frac12+\varepsilon.
\]

Applying this also to `q_{ji}` gives

\[
|y_i-y_j|\le\frac1{\sqrt2}+\sqrt2\,\varepsilon
=\frac{1+2\varepsilon}{\sqrt2}.
\]

The five-coordinate range-variance inequality yields

\[
\|y\|^2\le M_\varepsilon:=\frac35(1+2\varepsilon)^2.
\]

Hence every extra point has

\[
|h|\ge h_0:=\sqrt{1-M_\varepsilon}.
\]

The first term in the definition of `epsilon_*` guarantees `M_epsilon<3/4`, hence `h_0>1/2`. For two extra points in the same hemisphere,

\[
x=a w+\sqrt{1-a^2}\,u,\qquad
x'=b w+\sqrt{1-b^2}\,v,
\]

with `a,b>=h_0` and `u,v in S^3`. Their kissing inequality gives

\[
\langle u,v\rangle\le
F(a,b):=\frac{1/2-ab}{\sqrt{1-a^2}\sqrt{1-b^2}}.
\]

On `a,b>=h_0>1/2`,

\[
\operatorname{sign}(\partial F/\partial a)=\operatorname{sign}(a/2-b)<0
\]

and symmetrically in `b`. Therefore

\[
\langle u,v\rangle\le F(h_0,h_0)
=1-\frac1{2M_\varepsilon}=:t_\varepsilon.
\]

The second term in `epsilon_*` is exactly the condition `t_epsilon<sigma_11`. Consequently neither hemisphere can contain 11 extra points. There are no equatorial extras because `h_0>0`. Thus there are at most 10 extras above and 10 below, so

\[
|C|\le20+10+10=40.
\]

QED.

## Interpretation

Theorem 2 is a robust structural obstruction: if a 41--44 point five-dimensional kissing code exists, then no 20-point subconfiguration can lie arbitrarily close (after isometry and labeling) to the standard `A_4` root section. The theorem is quantitative in the intrinsic 11-point `S^3` gap `sigma_11-1/6`, although no new exact value of `sigma_11` is claimed here.

## Scope and status

These are restricted structural statements only. They do not increase the 40-point lower bound or decrease the 44-point unrestricted upper bound, and therefore they do not move the frozen I0125 metric. Publication novelty is unverified.