Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: full sharp Lyons domination on the mean-zero-transposition face of `S_3`

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; this is the complementary C03 role registered in `operations/progress_first_2026-09-20/REGISTRY.md`.  
Captured fresh master before this artifact: `51c2e88d54f3fb3a09e26d3d0ba48f2f0d3c23e0`.  
Previous checkpoint: `research7_2026-09-17/R7-03/runs/2026-09-20/2026-09-20T054000Z__report.md` (creation commit `580cb6c89545f9f78e8944c6ed3c889513971a21`).  
Status: **CANDIDATE FULL PROOF for the stated restricted `S_3` source class; PROVED PARTIAL relative to full C0036.**

## 1. Exact outside target

Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, ICM 2014, arXiv:1406.2707, Section 5.2, Conjecture 5.7: <https://arxiv.org/abs/1406.2707>.

Section 5.2 fixes a sofic group `Gamma`. The conjecture ranges over every `Gamma`-equivariant positive contraction

\[
0\le Q\le I\qquad\hbox{on }\ell^2(\Gamma),
\]

with group trace

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle
\]

and Fuglede--Kadison determinant

\[
\operatorname{FK}_\Gamma(Q)
=\exp\!\bigl(\operatorname{tr}_\Gamma\log|Q|\bigr).
\]

Writing `P^Q` for the determinantal law, the source asks for the optimal stochastic domination on **every increasing event**

\[
\boxed{
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I}.
}
\tag{1.1}
\]

The published source says this is open even for finite groups. A bounded literature check dated 2026-09-20 found the related Lyons--Thom operator-order coupling theorem (arXiv:1402.0969), but no source-matching resolution of Conjecture 5.7. This negative search is not treated as a certificate of worldwide openness or novelty.

For a finite group of order `N`,

\[
\operatorname{FK}_\Gamma(Q)=(\det Q)^{1/N}.
\tag{1.2}
\]

## 2. Inherited `S_3` bottleneck

Let

\[
H=A_3\cong C_3\triangleleft S_3
\]

and let `D` be multiplication by the sign character. In the `H`-Fourier decomposition, an arbitrary Hermitian `S_3`-equivariant contraction has three two-dimensional blocks

\[
Q_0=\begin{pmatrix}a_0&z_0\\z_0&a_0\end{pmatrix},\qquad
Q_1=\begin{pmatrix}a_1&z\\\bar z&a_2\end{pmatrix},\qquad
Q_2=\begin{pmatrix}a_2&\bar z\\z&a_1\end{pmatrix}.
\tag{2.1}
\]

The preceding run proved that symmetrizing only one active sector can reverse the desired stochastic order. Therefore sequential sector smoothing is not available in general. The simultaneous operator midpoint

\[
G:=Q\#(DQD)
\tag{2.2}
\]

remained plausible.

This run treats the codimension-one face

\[
\boxed{z_0=0.}
\tag{2.3}
\]

In spatial convolution coordinates, (2.3) is exactly the condition that the three transposition coefficients have mean zero. The result below proves the **whole determinantal process inequality**, not only principal inclusion probabilities or a selected orbit event.

## 3. Spatial coordinates on the face

Write `S_3=D_3=<r,s | r^3=s^2=1, srs=r^{-1}>`. Order the group as

\[
e,r,r^2,s,rs,r^2s.
\]

A Hermitian left-equivariant convolution kernel is determined by

\[
q(e)=u,\quad q(r)=v,\quad q(r^2)=\bar v,
\]

and three real transposition coefficients

\[
x_0=q(s),\qquad x_1=q(rs),\qquad x_2=q(r^2s).
\]

The quotient block has off-diagonal entry

\[
z_0=x_0+x_1+x_2.
\tag{3.1}
\]

Hence on the face (2.3) write

\[
x_1=X,\qquad x_2=Y,\qquad x_0=-X-Y.
\tag{3.2}
\]

If `omega=e^{2 pi i/3}`, the standard-sector off-diagonal coordinate is

\[
z=x_0+\omega x_1+\omega^2x_2,
\]

so exactly

\[
\boxed{|z|^2=3(X^2+XY+Y^2).}
\tag{3.3}
\]

The diagonal Fourier parameters are

\[
a_0=u+v+\bar v,
\]

\[
a_1=u-\Re v-\sqrt3\Im v,\qquad
 a_2=u-\Re v+\sqrt3\Im v.
\tag{3.4}
\]

On this face, `Q_0=a_0 I_2`. The condition `0<=Q<=I` is equivalent to

\[
0\le a_0\le1,
\qquad
K:=\begin{pmatrix}a_1&z\\\bar z&a_2\end{pmatrix}
\quad\hbox{being a positive contraction.}
\tag{3.5}
\]

## 4. Exact simultaneous midpoint

In the interior put

\[
\rho:=\sqrt{1-\frac{|z|^2}{a_1a_2}}
      =\sqrt{\frac{\det K}{a_1a_2}}\in[0,1].
\tag{4.1}
\]

(The boundary cases follow by continuity.) In the `D`-eigenbasis of the standard block, `DKD` reverses the sign of `z`. The matrix

\[
H:=\operatorname{diag}(a_1\rho,a_2\rho)
\tag{4.2}
\]

is the operator geometric mean `K#(DKD)`: one verifies directly that

\[
H K^{-1}H=DKD,
\]

which characterizes the positive geometric mean. Thus the full midpoint is

\[
G_0=a_0 I_2,
\quad
G_1=\operatorname{diag}(a_1\rho,a_2\rho),
\quad
G_2=\operatorname{diag}(a_2\rho,a_1\rho).
\tag{4.3}
\]

Consequently `G` commutes with the quotient sign gauge, its spatial kernel is supported on `A_3`, and

\[
\det G=\det Q.
\tag{4.4}
\]

Moreover (3.3) and (4.1) give the single face relation

\[
\boxed{3(X^2+XY+Y^2)=a_1a_2(1-\rho^2).}
\tag{4.5}
\]

The new point is to prove

\[
\boxed{\mathbf P^G\preccurlyeq \mathbf P^Q}
\tag{4.6}
\]

for **every increasing event**.

## 5. Why only 76 invariant upper sets need be checked

Both `P^Q` and `P^G` are invariant under left translation by `S_3`. If `f` is any increasing function on `2^{S_3}`, then its group average

\[
\bar f(S)=\frac1{6}\sum_{g\in S_3}f(gS)
\]

is invariant and increasing, and the two measures have the same expectation of `f` as of `bar f`. By layer-cake decomposition, an invariant increasing function is a positive combination/integral of indicators of invariant upper sets. Therefore it is enough to compare invariant increasing events.

Exact orbit enumeration under left translation gives

\[
\boxed{16\text{ subset orbits},\qquad 76\text{ invariant upper sets}.}
\tag{5.1}
\]

For an invariant upper set `U`, inclusion--exclusion and the determinantal inclusion formula give

\[
\mathbf P^Q(U)
=\sum_{T\subseteq S_3}c_U(T)\det Q_T,
\tag{5.2}
\]

where

\[
c_U(T)=\sum_{\substack{S\in U\\S\subseteq T}}
(-1)^{|T|-|S|}.
\tag{5.3}
\]

Thus each difference

\[
\Delta_U:=\mathbf P^Q(U)-\mathbf P^G(U)
\tag{5.4}
\]

is an exact polynomial expression in the face parameters.

## 6. Eliminate orientation exactly

The accompanying checker computes every principal minor over the exact field generated by `sqrt(3)` and `i`, forms (5.4), and reduces it modulo (4.5) by a Groebner reduction. After reduction, the dependence on the orientation `(X,Y)` always has the form

\[
C_0+C_1XY+C_2Y^2,
\tag{6.1}
\]

with no linear terms and no residual `X^2` term after using (4.5).

Write

\[
s:=X^2+XY+Y^2\ge0.
\]

The needed orientation ranges are exact:

\[
-1\le \frac{XY}{s}\le\frac13,
\tag{6.2}
\]

\[
0\le\frac{Y^2}{s}\le\frac43,
\tag{6.3}
\]

and

\[
-\frac13\le\frac{XY+Y^2}{s}\le1.
\tag{6.4}
\]

For completeness, these are one-variable generalized Rayleigh quotients for the positive definite quadratic form `s`; the endpoints follow by solving the corresponding `2x2` generalized eigenvalue problems. The checker certifies the sign of every coefficient on `a_0 in [0,1]` by **univariate exact Bernstein coefficients**, then uses (6.2)--(6.4) to obtain a rigorous lower bound `L_U` for every `Delta_U`. No sampled sign decision is used.

There are 73 nonzero lower bounds; the remaining three differences are identically zero at this stage.

## 7. Compress the remaining feasibility region

Set

\[
q:=a_1+a_2,
\qquad
d:=\det K=a_1a_2\rho^2,
\qquad h:=\rho(a_1+a_2).
\tag{7.1}
\]

Every orientation-minimized lower bound is symmetric in `a_1,a_2`, so it can be written in `(a_0,d,h,q)`. The `2x2` contraction constraints imply

\[
0\le d\le1,
\qquad
2\sqrt d\le h\le q\le1+d.
\tag{7.2}
\]

Indeed, the two midpoint eigenvalues `a_1 rho,a_2 rho` have product `d`, hence `h>=2 sqrt(d)`; `rho<=1` gives `h<=q`; and

\[
\det(I-K)=1-q+d\ge0
\]

gives `q<=1+d`.

After clearing the harmless positive factor `3h^2`, every nonzero lower bound factors as

\[
3h^2L_U=(q-h)C_U(a_0,d,h,q).
\tag{7.3}
\]

This factor is structurally correct: `q=h` is the face `rho=1`, where `z=0` and the midpoint is already `Q`.

Now parameterize the whole feasible region by a unit cube. Put

\[
d=T^2,
\tag{7.4}
\]

\[
h=2T+U(1-T)^2,
\tag{7.5}
\]

\[
q=h+V(1+T^2-h),
\tag{7.6}
\]

\[
a_0=A,
\tag{7.7}
\]

with

\[
(A,T,U,V)\in[0,1]^4.
\]

Conversely, every interior feasible quadruple in (7.2) has such parameters; the boundary follows by continuity.

## 8. Exact Bernstein positivity certificate

After (7.4)--(7.7), the 73 nonzero event bounds collapse to only

\[
\boxed{33\text{ distinct nonzero polynomials }\widehat C_U(A,T,U,V).}
\tag{8.1}
\]

For a polynomial

\[
P(x)=\sum_j p_jx^j
\]

of coordinatewise degree `n`, the multivariate Bernstein coefficient at multi-index `k` is

\[
b_k=\sum_{j\le k}p_j
\prod_r\frac{\binom{k_r}{j_r}}{\binom{n_r}{j_r}}.
\tag{8.2}
\]

Because all Bernstein basis functions are nonnegative on the unit cube, `b_k>=0` for every `k` implies `P>=0` on that cube.

The exact checker recomputes all 33 polynomials from the group law and principal minors and verifies **every** Bernstein coefficient rationally. The degree distribution is

- 30 certificates of degree `(2,6,3,1)`;
- 1 certificate of degree `(2,6,2,0)`;
- 1 certificate of degree `(2,6,2,1)`;
- 1 certificate of degree `(1,4,1,1)`.

Across all certificates it obtains

\[
\boxed{5269\text{ Bernstein coefficients},}
\]

of which 2362 are zero and **none is negative**. The smallest strictly positive coefficient is

\[
\boxed{1/45.}
\tag{8.3}
\]

The archived exact execution ends `ALL_EXACT_CERTIFICATES_PASS`.

Therefore `C_U>=0`, hence by (7.3) `L_U>=0`, hence by construction `Delta_U>=0` for all 76 invariant upper sets. Section 5 then gives (4.6) for every increasing event.

This is a finite-core exact certificate supporting the proof. It is owner-track self-verification, **not** an independent review.

## 9. Main restricted theorem

### Theorem 9.1 (mean-zero transposition `S_3` theorem)

Let `Q` be any `S_3`-equivariant positive contraction on `ell^2(S_3)`. Write `q(s),q(rs),q(r^2s)` for its three real transposition convolution coefficients. Assume only

\[
\boxed{q(s)+q(rs)+q(r^2s)=0.}
\tag{9.1}
\]

Equivalently, the trivial and sign one-dimensional Fourier eigenvalues are equal (`z_0=0`). Then the complete sharp Lyons product bounds hold:

\[
\boxed{
\operatorname{Ber}(\operatorname{FK}_{S_3}(Q))^{\otimes S_3}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\operatorname{Ber}\!\left(1-\operatorname{FK}_{S_3}(I-Q)\right)^{\otimes S_3}.
}
\tag{9.2}
\]

Both constants are optimal.

### Proof

The preceding sections prove `P^G <=st P^Q` for the simultaneous midpoint `G`. By (4.3), `G` is `A_3`-supported, so its DPP splits over the two `A_3` cosets into two identical `C_3` determinantal processes. The sharp `C_3` instance of Lyons 5.7 was proved self-containedly earlier in the R7-03 chain. By (4.4),

\[
(\det G)^{1/6}=(\det Q)^{1/6}
=\operatorname{FK}_{S_3}(Q),
\]

so tensoring the two subgroup couplings and then using `P^G <=st P^Q` proves the lower bound in (9.2).

The face condition is preserved by complementation: `I-Q` still has zero sum of its off-identity transposition coefficients. Apply the just-proved lower statement to `I-Q`, then complement configurations, to obtain the upper bound. Finally, the full-set event has probability `det Q` and the empty-set event has probability `det(I-Q)`, forcing the two product densities in (9.2); hence they are sharp. `QED`

## 10. What changed, and what remains open

This is strictly more than a necessary condition or a finite example: it proves stochastic domination of the **entire process** on a genuinely noncentral codimension-one family of arbitrary `S_3`-equivariant contractions. It is also different from the previously proved constant-transposition-coset family. A constant nonzero transposition coefficient has nonzero sum, while (9.1) allows arbitrary unequal transposition coefficients subject only to their sum being zero.

The full-source quantifier in Lyons 5.7 is still open in this research chain, and arbitrary `S_3` with `z_0 != 0` is not claimed. The preceding run showed that quotient-sector smoothing alone can reverse stochastic order, so the remaining case genuinely requires simultaneous cross-sector compensation.

A natural next parameterization is

\[
g_0=\sqrt{a_0^2-z_0^2},\qquad
\xi=a_0-g_0\ge0,
\]

for the quotient-sector midpoint loss and

\[
\eta=q-h\ge0
\]

for the standard-sector midpoint loss. The next attack is to compute the exact **simultaneous** invariant-event differences and seek a decomposition into nonnegative boundary pieces plus a mixed `xi*eta` compensation term. The theorem above settles the complete `xi=0` boundary; the earlier two-dimensional/constant-coset theorems settle complementary structured faces. A successful mixed certificate would close arbitrary `S_3` rather than adding another isolated orbit calculation.
