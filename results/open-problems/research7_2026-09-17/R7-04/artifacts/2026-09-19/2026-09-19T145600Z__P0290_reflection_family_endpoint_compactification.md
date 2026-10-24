# P0290: endpoint exclusion and compactification of the four-state reflection family

Target: Lasse Leskelä, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022), 213--215, DOI `10.1007/s11134-022-09824-0`, Problem 2 on journal p. 214.

Status of this artifact: **PARTIAL / OPEN**. It does not prove or refute the source problem. It proves that the exact source-admissible four-state reflection family previously constructed by R7-04 cannot have a second-order light-traffic reversal near either endpoint of its parameter interval, and that any remaining second-order violation in this family must lie in a genuine compact interior rectangle. It also proves that the tempting Loewner-monotonicity-in-parameter route fails exactly at first order.

The source was rechecked on 2026-09-19 in the accepted author manuscript at
`https://acris.aalto.fi/ws/portalfiles/portal/89616571/Ross_s_second_conjecture_and_supermodular_stochastic_ordering.pdf`.
The displayed Problem 2 asks whether the workload ordering holds when the baseline intensity is `lambda(t)=f(X(t))`, with `f` Boolean or more generally deterministic and `X` a doubly stochastically monotone CTMC. Bounded searches for the exact title/problem and these terms did not locate a later explicit solution. That is negative evidence only, not a novelty certificate or proof of current openness.

---

## 1. Recovered family and second-order operator

For `0<a<=1`, R7-04 previously proved that

\[
Q_a=
\begin{pmatrix}
-2&2-a&a&0\\
2&-(2+a)&0&a\\
0&2a&-(2+a)&2-a\\
0&0&2&-2
\end{pmatrix}
\]

has uniform stationary law, is irreducible, and both `Q_a` and its stationary reversal are stochastically monotone. Thus it is source-admissible. In the orthonormal centered basis

\[
u=\tfrac12(1,-1,-1,1)^T,\quad
v=\tfrac12(1,1,-1,-1)^T,\quad
w=\tfrac12(1,-1,1,-1)^T,
\]

the generator is

\[
M_a=
\begin{pmatrix}
-4&-a&a\\
a&-2a&a\\
-a&a&-4
\end{pmatrix}.
\tag{1.1}
\]

Put

\[
\Psi(z)=\int_0^1u(1-u)e^{uz}\,du
=\frac{(z-2)e^z+z+2}{z^3},
\]
with the removable value `Psi(0)=1/6`, and define

\[
F_a(c)=M_a\Psi(cM_a),\qquad
H_a(c)=\frac12(F_a(c)+F_a(c)^T).
\tag{1.2}
\]

For every centered observable `g`, the recovered triangular light-traffic coefficient satisfies

\[
J_g'(c)=g^TH_a(c)g.
\tag{1.3}
\]

A positive eigenvalue of `H_a(c)` would therefore activate the already-proved small-intensity workload remainder theorem and give a source-valid counterexample. The preceding run proved the exact endpoint theorem

\[
H_1(c)\prec0\qquad(c>0).
\tag{1.4}
\]

The question here is what survives as `a` varies.

---

# B3 -- prove something stronger: both parameter endpoints are globally safe

## 2. The endpoint-neighborhood theorem

**Theorem 2.1.** There exist numbers `epsilon_0>0` and `epsilon_1>0` such that

\[
H_a(c)\prec0\qquad\text{for every }c>0
\]

whenever either

\[
0<a<\epsilon_0
\quad\text{or}\quad
1-\epsilon_1<a\le1.
\tag{2.1}
\]

Thus a second-order reversal in this exact source-admissible family, if one exists at all, cannot approach either the reducible face `a=0` or the certified complex extreme ray `a=1`.

### 2.1 Neighborhood of `a=1`

Suppose the assertion were false near `a=1`. Then there would be `a_n->1`, `c_n>0`, and unit vectors `x_n` with

\[
x_n^TH_{a_n}(c_n)x_n\ge0.
\tag{2.2}
\]

If `(c_n)` has a bounded subsequence, pass to `c_n->c_*>=0` and `x_n->x_*`. Matrix entire functional calculus is jointly continuous in `(a,c)`. At `c_*=0`,

\[
H_1(0)=\frac16\operatorname{Sym}(M_1)\prec0;
\]
for `c_*>0`, (1.4) gives `H_1(c_*)\prec0`. Either case contradicts (2.2).

It remains to exclude `c_n->infinity`. On the centered space `M_a` is invertible for every `a>0`, and the closed form of `Psi` gives the exact identity

\[
\boxed{
 c^2F_a(c)
 =M_a^{-1}+\frac2cM_a^{-2}
 +e^{cM_a}\left(M_a^{-1}-\frac2cM_a^{-2}\right).
}
\tag{2.3}
\]

In a fixed neighborhood of `a=1`, `M_a^{-1}` and `M_a^{-2}` are uniformly bounded. Moreover `-Sym(M_a)` is uniformly positive definite, so the elementary energy estimate gives

\[
\|e^{cM_a}\|_2\le Ce^{-\gamma c}
\tag{2.4}
\]

for fixed positive `C,gamma`. Finally, `Sym(M_1^{-1})` is strictly negative definite by the preceding exact proof, and hence so is `Sym(M_a^{-1})` uniformly after shrinking the neighborhood. Taking symmetric parts in (2.3), the `c^{-1}` and exponential terms are uniformly smaller than this negative leading form for all sufficiently large `c`. This contradicts (2.2). Therefore the `a=1` endpoint has a full all-scale safe neighborhood.

### 2.2 The singular endpoint `a=0`

The point `a=0` is reducible, so ordinary compact continuity in `(a,c)` is not enough: the dangerous scale can diverge like `1/a`. We deal with all scales at once by contradiction.

The characteristic polynomial of `M_a` is

\[
\lambda^3+(8+2a)\lambda^2+(16+16a+a^2)\lambda+32a.
\tag{2.5}
\]

At `a=0` there is one simple eigenvalue `0` and a semisimple double eigenvalue `-4`. Analytic perturbation of the simple root gives a real slow eigenvalue

\[
\boxed{\mu(a)=-2a+\frac18a^3+O(a^4).}
\tag{2.6}
\]

The associated rank-one spectral projection is analytic,

\[
P_a=P_0+O(a),\qquad P_0=vv^T,
\tag{2.7}
\]

and its fast-fast block is `O(a^2)` while its slow-fast blocks are `O(a)`. The complementary two-dimensional spectral cluster stays in a fixed left half-plane and tends to `-4I` on `span{u,w}`.

Assume now that there are `a_n downarrow 0`, `c_n>0` for which `H_{a_n}(c_n)` is not negative definite.

If `(c_n)` is bounded, pass to `c_n->c_*`. At `a=0`, the fast eigenvalue of `H_0(c_*)` is

\[
-4\Psi(-4c_*)<0
\]

with multiplicity two, while the slow eigenvalue is zero. Because

\[
\frac{d}{dz}\bigl[z\Psi(cz)\bigr]_{z=0}=\Psi(0)=\frac16
\]

and the slow eigenvalue of `M_a` has derivative `-2`, the slow eigenvalue of `H_a(c)` is

\[
-\frac a3+O(a^2)
\tag{2.8}
\]

uniformly for `c` in compact sets. Slow-fast entries are `O(a)`, while the fast block has a fixed negative margin, so its Schur complement is negative for all sufficiently small `a`. Contradiction.

Hence we need only consider `c_n->infinity`. Put

\[
x_n=a_nc_n.
\]

On the slow mode, (2.6) gives

\[
f_n:=\mu(a_n)\Psi(c_n\mu(a_n))<0.
\tag{2.9}
\]

Writing

\[
q(x)=2\Psi(-2x)>0,
\]
we have, uniformly along subsequences,

\[
|f_n|=a_n q(x_n)(1+o(1)).
\tag{2.10}
\]

The useful endpoint asymptotics are

\[
q(x)\to\frac13\quad(x\downarrow0),
\qquad
x^2q(x)\to\frac12\quad(x\to\infty).
\tag{2.11}
\]

On the fast two-dimensional cluster, the exact inverse formula (2.3) and the spectral gap from zero give

\[
H_{a_n}^{\rm fast}(c_n)
=-\frac1{4c_n^2}I_2+o(c_n^{-2}).
\tag{2.12}
\]

The nonorthogonality generated by the slow projection contributes `O(a_n|f_n|)` to the slow-fast block and `O(a_n^2|f_n|)` to the fast-fast block. The complementary fast projection contributes only `O(a_nc_n^{-2})` off diagonal. Thus, in the fixed orthogonal splitting `span{v} \oplus span{u,w}`, the symmetric matrix has the block orders

\[
\begin{pmatrix}
-|f_n|(1+o(1))
& O(a_n|f_n|+a_nc_n^{-2})\\
O(a_n|f_n|+a_nc_n^{-2})
&-\frac1{4c_n^2}I_2+o(c_n^{-2})+O(a_n^2|f_n|)
\end{pmatrix}.
\tag{2.13}
\]

The slow contamination of the fast diagonal is negligible because

\[
\frac{a_n^2|f_n|}{c_n^{-2}}
=a_nx_n^2q(x_n)(1+o(1))\longrightarrow0,
\tag{2.14}
\]
where `x^2q(x)` is bounded on `(0,infinity)`. For the slow-fast term, its square divided by the product of the two diagonal scales tends to zero. Indeed the first contribution gives

\[
\frac{a_n^2|f_n|^2}{|f_n|c_n^{-2}}
=a_nx_n^2q(x_n)(1+o(1))\to0,
\tag{2.15}
\]
while the second gives

\[
\frac{a_n^2c_n^{-4}}{|f_n|c_n^{-2}}
=\frac{a_n}{q(x_n)c_n^2}(1+o(1)).
\tag{2.16}
\]
If `x_n` is bounded away from zero, (2.16) plainly tends to zero. If `x_n->0`, then `q(x_n)->1/3` and `c_n=x_n/a_n->infinity`, so it again tends to zero. If `x_n->infinity`, (2.11) gives the same conclusion. Therefore the Schur complement of (2.13) is strictly negative for all sufficiently large `n`, contradiction.

No violating sequence can approach `a=0`; the first endpoint neighborhood in (2.1) follows.

This proves Theorem 2.1.

---

# B5 -- differentiate in the family parameter: the naive monotonic route fails

## 3. Exact failure of Loewner monotonicity in `a`

One tempting way to extend the `a=1` theorem to all `a` is to hope that `H_a(c)` is monotone in `a` in Loewner order. That strategy fails before any matrix exponential enters.

At `c=0`,

\[
H_a(0)=\frac16\operatorname{Sym}(M_a)
=\frac16
\begin{pmatrix}
-4&0&0\\
0&-2a&a\\
0&a&-4
\end{pmatrix}.
\tag{3.1}
\]

The derivative on the odd `(v,w)` block is

\[
\frac{\partial}{\partial a}H_{a,-}(0)
=\frac16
\begin{pmatrix}-2&1\\1&0\end{pmatrix},
\tag{3.2}
\]
with

\[
\boxed{\det\frac{\partial}{\partial a}H_{a,-}(0)=-\frac1{36}<0.}
\tag{3.3}
\]

Hence the parameter derivative is indefinite. Neither increasing nor decreasing Loewner continuation in `a` can prove the family theorem, even infinitesimally at `c=0`. This is the exact obstruction requested by B5.

The large-`c` main term nevertheless has useful uniform structure. Put

\[
S_1(a)=\operatorname{Sym}(M_a^{-1}),\qquad
S_2(a)=\operatorname{Sym}(M_a^{-2}).
\]

Exact algebra gives

\[
S_1=
\begin{pmatrix}
 a/32-1/4&0&0\\
0&-(a^2+16)/(32a)&-(a+4)/32\\
0&-(a+4)/32&-(a+8)/32
\end{pmatrix}.
\tag{3.4}
\]

For `0<a<=1`, Sylvester's criterion yields the useful uniform bound

\[
\boxed{-S_1(a)\succ\frac15I.}
\tag{3.5}
\]

The exact leading minors of `-S_1-I/5` are archived in the checker. Also `S_2(a)\succ0`; in particular

\[
\det S_{2,-}(a)=\frac{8-a^2}{512a^2}>0,
\quad
\det S_2(a)=\frac{(a-4)(a+12)(a^2-8)}{524288a^2}>0.
\tag{3.6}
\]

The largest generalized eigenvalue of `S_{2,-}` relative to `-S_{1,-}` is

\[
r_+(a)=\frac{(a+4)^2+\sqrt{D(a)}}{64a},
\]
where

\[
D(a)=a^4+80a^3+96a^2-256a+256.
\]

For `0<a<=1`,

\[
\boxed{r_+(a)<\frac3{5a}.}
\tag{3.7}
\]

Indeed `192/5-(a+4)^2>0`, and the exact squared-margin identity is

\[
\left(\frac{192}{5}-(a+4)^2\right)^2-D(a)
=-\frac{64}{25}(25a^3+30a^2+40a-96)>0,
\tag{3.8}
\]

because the cubic on the right is strictly increasing and equals `-1` at `a=1`. The even generalized ratio obeys the same bound. Therefore

\[
S_2(a)\preceq\frac3{5a}[-S_1(a)].
\tag{3.9}
\]

This explains why the inverse tail is robust even though the direct parameter derivative is not: if `ac>=12/5`, then the nonexponential main part in (2.3) satisfies

\[
S_1+\frac2cS_2\preceq\frac12S_1\prec0.
\tag{3.10}
\]

Equation (3.10) is not by itself a full global proof, because the nonnormal exponential remainder must still be controlled in the same geometry.

---

# B20 -- locate exactly where a decisive algorithm still has to work

## 4. Compact-interior reduction

**Theorem 4.1 (compactification of the remaining family problem).** There exist constants

\[
0<\epsilon_0<1-\epsilon_1<1,
\qquad
0<c_0<C<\infty,
\]

such that

\[
\lambda_{\max}(H_a(c))<0
\]

outside the compact rectangle

\[
\boxed{
[\epsilon_0,1-\epsilon_1]\times[c_0,C].
}
\tag{4.1}
\]

Therefore the entire unresolved second-order sign question for the reflection family is a finite compact two-variable problem. No violation can hide at `a=0`, `a=1`, `c=0`, or `c=infinity`.

### Proof

Theorem 2.1 removes neighborhoods of `a=0` and `a=1`. On the remaining compact parameter interval `A=[epsilon_0,1-epsilon_1]`,

\[
H_a(0)=\frac16\operatorname{Sym}(M_a)\prec0
\]

uniformly: in fact `-Sym(M_a)\succeq aI`, so its smallest eigenvalue is bounded below on `A`. Joint continuity then supplies `c_0>0` such that `H_a(c)\prec0` for every `a in A` and `0<=c<=c_0`.

For large `c`, use (2.3). On `A`, `S_1(a)=Sym(M_a^{-1})` is continuous and strictly negative definite, hence has a uniform negative margin. `S_2(a)` and the inverse matrices are uniformly bounded, while the spectra of the generators stay uniformly inside a left half-plane; equivalently the semigroups obey a uniform exponential bound. Thus the `2S_2/c` and exponential terms are uniformly dominated by `S_1` once `c>=C`. This proves (4.1). `square`

### 4.2 What this says about the failed algorithm

The previous search had an unbounded domain `(a,c) in (0,1] x (0,infinity)` and a nearly reducible face where floating arithmetic can manufacture tiny false positive eigenvalues. Theorems 2.1 and 4.1 remove exactly those pathologies. The remaining question can in principle be decided by a finite certified subdivision of one compact rectangle, with the three reflection-reduced scalar inequalities

\[
h_+(a,c)<0,
\qquad
\operatorname{tr}H_-(a,c)<0,
\qquad
\det H_-(a,c)>0.
\]

The reason the simpler algorithm did not already settle the family is now exact: Loewner monotonicity in `a` fails by (3.3), so a proof must control the compact interior rather than propagate a one-dimensional endpoint certificate.

---

## 5. Exact finite algebra self-check

The finite identities used in Sections 2--3 were checked after the derivation by

`research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T145200Z__P0290_endpoint_compactification_check.py`.

Its archived output ends `ALL_SYMBOLIC_CHECKS_PASS` and verifies:

- the exact inverse and symmetric inverse powers;
- `det S1_odd=1/(8a)`;
- positivity formulas for `S2`;
- all Sylvester minors proving (3.5);
- the indefinite parameter derivative determinant `-1/36`;
- the generalized-eigen polynomial and discriminant;
- the exact squared margin behind (3.7);
- the slow eigenvalue expansion (2.6) through cubic order.

This is a self-check, not an independent P26 or OTHER-track audit.

---

## 6. Source-level meaning

The result is deliberately not called a source solution. It proves a stronger all-observable second-order exclusion on two endpoint neighborhoods of one explicit four-state source-admissible family and reduces that family's remaining second-order search to a compact interior. It gives neither a positive `Delta_Ross` witness nor the full universal workload theorem. Higher-order and moderate-load mechanisms remain possible even if the compact second-order rectangle is eventually certified negative.
