# An exact third-coefficient sum of squares for four twins over an arbitrary core

Research continuation, 2 October 2026. This is a proved restricted theorem, with
an exact independent audit. Novelty has not been certified. It does not solve
the general forest or random-cluster negative-correlation conjecture.

## Statement

Let H be any finite undirected graph on s>=1 vertices, with positive conductances
w_uv on its edges. Give each core vertex v a positive number a_v. Form G by adding
four terminal vertices 0,1,2,3, joining each terminal to each v in H, and adding
marked edges e=01 and f=23. There are no other terminal-to-terminal edges.
Give every core edge uv activity lambda*w_uv and every terminal-to-core edge iv
activity lambda*a_v. The two marked activities are arbitrary and positive.

Let L_H be the conductance Laplacian of H and put

\[
 D_a=\operatorname{diag}(a_v),\qquad M=L_H+4D_a,\qquad
 W=\det M,\qquad d=\sum_v a_v.
\]

The forest polynomial has the form

\[
 Z=A+z_eB+z_fB+z_ez_fD,
\]

by terminal symmetry. Consequently its marked-edge Rayleigh difference is
\(\mathcal R_{ef}=B^2-AD\), independent of z_e,z_f.

**Theorem.** If s>=2, the two highest coefficients of this Rayleigh difference
vanish, and the third has the exact sum-of-squares formula

\[
\begin{aligned}
\mathcal R_{ef}(\lambda)
 &=H_2\lambda^{2s+2}+O(\lambda^{2s+1}),\\
 H_2&=\frac1{64}\sum_{u,v\in V(H)}a_u a_v
       \left(4d\operatorname{adj}(M)_{uv}-W\right)^2>0.
\end{aligned}
\]

Thus the two marked forest edge indicators are strictly negatively correlated
for all sufficiently large lambda. When s=1, their Rayleigh difference is
identically zero, because the graph consists of two triangles sharing one hub.

This proves a family where the two coefficients H_0,H_1 of
Çiçeksiz–Ravichandran, https://arxiv.org/html/2610.00549v1, both vanish. Their
nonvanishing hypothesis therefore does not supply this conclusion. Their
complete-join Example 4.11 uses marked endpoints in four different join parts,
which gives H_1>0; here both matching edges lie within the four-terminal part,
and H_1=0. For s>=3 the present graphs contain the spanning 3-connected graph
K_{4,s}, so the equality is not caused by a cut vertex or a two-vertex separator.

## 1. Reduction by a core forest

Restrict a forest of G to its core edges. This gives a forest F of H, with
components C_1,...,C_r and weight

\[
 w_F=\prod_{uv\in F}w_{uv},\qquad
 c_j=\sum_{v\in C_j}a_v,\qquad \sum_jc_j=d.
\]

Since F has s-r edges, its activity factor is w_F lambda^{s-r}. Contract each
component C_j. Any terminal may have at most one connection to it, since two
connections would create a cycle with the core tree. Summing the choices of
that one connection gives activity lambda*c_j. More generally, connecting
different current terminal components to C_j is permitted exactly when the
selected terminal blocks are distinct. This contraction therefore gives
precisely the four-terminal hub forest transfer with hub activities
x_j=lambda*c_j. No multiplicity or weight is lost.

Write A(c),B(c),D(c) for the hub forest polynomials with respectively zero, one,
or both marked matching edges forced (with their activities removed). They
start at terminal partition shapes 1111,211,22. Then

\[
 (A,B,D)=\sum_{F\in\mathcal F(H)}w_F\lambda^{s-r(F)}
              (A(c(F)),B(c(F)),D(c(F))).
\]

## 2. Exact four-terminal transfer and its leading coefficients

For a hub of weight x, the five terminal-partition shapes are 1111,211,22,31,4.
Every diagonal transition has weight 1+4x. The non-diagonal transition weights are

| Initial shape | Final shape | Weight |
|---|---|---:|
|1111|211|6x^2|
|1111|31|4x^3|
|1111|4|x^4|
|211|31|4x^2|
|211|22|x^2|
|211|4|2x^3|
|22|4|4x^2|
|31|4|3x^2|

At most three non-diagonal transitions can occur. Let

\[
 a_j'=1+4x_j,\quad t_j=\frac{x_j^2}{a_j'},\quad
 u_j=\frac{x_j^3}{a_j'},\quad v_j=\frac{x_j^4}{a_j'},\quad
 P=\prod_ja_j',\quad T=\sum_jt_j,\quad U=\sum_ju_j,\quad V=\sum_jv_j.
\]

With E_k the elementary symmetric functions in the t_j, the transition table
immediately gives

\[
\begin{aligned}
 A/P&=1+6T+4U+V+30E_2+12\sum_{i\ne j}t_i u_j+96E_3,\\
 B/P&=1+5T+2U+16E_2,\\
 D/P&=1+4T.
\end{aligned}
\]

These formulas are exact rational representations of polynomials. They also
hold with r=1; empty sums vanish.

Now specialize x_j=lambda*c_j and define

\[
 K=4^r\prod_jc_j,\quad
 h=\sum_j\frac1{c_j},\quad q_1=h/4,\quad
 q_2=\frac1{16}\sum_{i<j}\frac1{c_ic_j}.
\]

Expanding the preceding exact formulas gives

\[
\begin{aligned}
 A(c)&=K\lambda^{r+3}(a_0+a_1\lambda^{-1}+a_2\lambda^{-2}
                                     +O(\lambda^{-3})),\\
 B(c)&=K\lambda^{r+2}(b_0+b_1\lambda^{-1}+b_2\lambda^{-2}
                                     +O(\lambda^{-3})),\\
 D(c)&=K\lambda^{r+1}(d_0+d_1\lambda^{-1}+d_2\lambda^{-2}
                                     +O(\lambda^{-3})),
\end{aligned}
\]

where

\[
\begin{array}{lll}
 a_0=d^3/4,&
 a_1=d^3q_1/4+3(6-r)d^2/16,&
 a_2=d^3q_2/4+3(6-r)d^2q_1/16
                 +3d^2h/64+3(r^2-13r+38)d/64,\\[2pt]
 b_0=d^2/2,&
 b_1=d^2q_1/2+(11-2r)d/8,&
 b_2=d^2q_2/2+(11-2r)dq_1/8
                 +(r^2-12r+32)/32+dh/16,\\[2pt]
 d_0=d,&
 d_1=dq_1+(4-r)/4,&
 d_2=dq_2+(4-r)q_1/4+h/16.
\end{array}
\]

For example the coefficients follow from
\(t_j=c_j\lambda/4-1/16+1/(64c_j\lambda)+O(\lambda^{-2})\)
and the analogous expansions u_j=c_j lambda*t_j, v_j=c_j^2 lambda^2*t_j.
The cancellations use only sum c_j=d, so there is no assumption of equal core
component weights.

## 3. A component-count variance identity

Define a probability measure on core forests by

\[
 \nu(F)=\frac{w_F4^{r(F)}\prod_jc_j}{W}.
\]

The normalization W and its determinantal interpretation are justified in the
next section. Under this measure the preceding coefficient averages give

\[
 A=W\lambda^{s+3}(a_0+\mathbb E a_1\lambda^{-1}
                              +\mathbb E a_2\lambda^{-2}+\cdots),
\]

with analogous expansions for B,D. Put

\[
 \alpha=a_1/a_0=q_1+\frac{3(6-r)}{4d},\quad
 \beta=b_1/b_0=q_1+\frac{11-2r}{4d},\quad
 \delta=d_1/d_0=q_1+\frac{4-r}{4d}.
\]

Pointwise beta=(alpha+delta)/2 and b_0^2=a_0d_0=d^4/4. Hence H_0=H_1=0.
For the next coefficient, direct substitution from the displayed table gives

\[
 2\frac{b_2}{b_0}-\frac{a_2}{a_0}-\frac{d_2}{d_0}
       =\frac{-r^2+15r-50}{16d^2}.
\]

Also alpha-delta=(7-r)/(2d). Thus

\[
\begin{aligned}
\frac{H_2}{W^2a_0d_0}
 &=\mathbb E\left[2b_2/b_0-a_2/a_0-d_2/d_0\right]
                   +(\mathbb E\beta)^2-(\mathbb E\alpha)(\mathbb E\delta)\\
 &=\frac{\mathbb E[-r^2+15r-50]+(7-\mathbb Er)^2}{16d^2}\\
 &=\frac{\mathbb Er-1-\operatorname{Var}r}{16d^2}.
\end{aligned}
\]

Consequently

\[
 H_2=\frac{d^2W^2}{64}
          (\mathbb Er-1-\operatorname{Var}r).
\]

## 4. The rooted core forest and positivity

The weighted matrix-forest theorem gives

\[
 W(z)=\det(L_H+4zD_a)
      =\sum_{F\in\mathcal F(H)}w_F(4z)^{r(F)}\prod_jc_j.
\]

Indeed, the root weight at vertex v is 4z*a_v, and choosing one root in C_j
contributes sum_{v in C_j}4z*a_v=4z*c_j. Therefore W=W(1), and
W(z)/W(1) is the probability generating function of r under nu.
The matrix-forest theorem is classical; see Chebotarev–Shamis,
https://arxiv.org/abs/math/0602575. One can also prove this weighted diagonal
version directly by expanding the determinant into principal Laplacian minors
and applying the all-minors matrix-tree theorem.

Let mu_i be the nonnegative eigenvalues of
D_a^{-1/2}L_H D_a^{-1/2}. Then

\[
 \frac{W(z)}{W(1)}=\prod_{i=1}^s\frac{\mu_i+4z}{\mu_i+4}
                  =\prod_{i=1}^s(1-p_i+p_i z),\qquad
 p_i=\frac4{4+\mu_i}.
\]

Thus r is distributed as a sum of independent Bernoulli variables, with p_i=1
for every zero eigenvalue. In particular

\[
 \mathbb Er-1-\operatorname{Var}r=\sum_i p_i^2-1.
\]

There is at least one zero eigenvalue. If s>=2, either there is another zero
one or there is a strictly positive eigenvalue whose p_i is still positive.
Therefore this expression is strictly positive. This proves H_2>0.

## 5. The explicit adjugate sum of squares

There is a useful matrix expression that avoids spectral denominators. Set

\[
 Q=4D_a^{1/2}M^{-1}D_a^{1/2},\qquad
 u=(\sqrt{a_v})_v/\sqrt d.
\]

Q is symmetric positive definite, its eigenvalues are p_i, and Qu=u since
L_H*1=0. Therefore

\[
 \sum_i p_i^2-1=\lVert Q-uu^T\rVert_F^2.
\]

As M^{-1}=adj(M)/W, its (v,w) summand after multiplication by d^2W^2/64 is

\[
 \frac{a_va_w}{64}(4d\operatorname{adj}(M)_{vw}-W)^2.
\]

Summing proves the theorem. Equality would require Q=uu^T, impossible for s>=2
because Q has rank s while uu^T has rank one. This gives a second direct proof
of strictness and an explicit polynomial sum of squares.

## 6. Checks, reductions, and scope

For an empty core with a_v=1, M=4I, d=s, W=4^s. The formula reduces to

\[
 H_2=4^{2s-3}s^2(s-1),
\]

agreeing with the exact all-fugacity formula for K_{4,s}+{e,f}. For s=2 the
H_2 coefficient is independent of the one possible core-edge conductance:
H_2=4a_1^2a_2^2(a_1+a_2)^2.

`twin_core_high_fugacity_audit.py` uses exact Fraction arithmetic, directly
enumerates core edge subsets, rejects cycles by union-find, and computes all
four-terminal partition transitions independently of the five-shape formulas.
It obtains the complete Rayleigh polynomial and compares its top three
coefficients with both the rooted-component moment formula and the independently
computed adjugate sum of squares. Eighteen cases passed: empty, path, and complete
cores through six vertices, disconnected cores, unequal integer weights, and
unequal rational spoke/core weights. All exact values are saved in
`twin_core_high_fugacity_audit_results.json`.

Those eighteen full polynomials also had nonnegative power coefficients. That
extra observation is **not** a proof of all-fugacity negative correlation for an
arbitrary core, and is not asserted as a theorem here. The coefficient table,
component-count identity, and matrix-forest argument above, rather than these
finite tests, prove the high-fugacity family for every finite H.

The theorem concerns this one marked matching pair and four twins sharing
identical spoke conductances. It does not cover arbitrary endpoint geometry,
arbitrary graph edge pairs, or the general q<1 random-cluster model. Targeted
primary-source comparison did not locate this H_2 formula, but full novelty
review remains outstanding.
