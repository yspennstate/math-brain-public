# P0290 recovery theorem: the complex-spectrum extreme ray Q1 is globally second-order safe

Target: Lasse Leskelä, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022), 213--215, DOI `10.1007/s11134-022-09824-0`, Problem 2 on journal p. 214.

Status: **PARTIAL / OPEN**. This note proves the exact fixed-ray recovery theorem prescribed by the preceding STUCK1 diagnosis. It does **not** prove Ross workload monotonicity for all deterministic images of doubly stochastically monotone chains, and it does not refute the source problem. The frozen source metric `Delta_Ross` therefore remains `UNKNOWN/UNMEASURED`.

Methods used: **B11 (dualize), B13 (find what only increases), B19 (make it an algorithm)**.

## 1. Source reduction and fixed recovery target

For a finite stationary hidden chain with generator `Q`, stationary law `pi`, and centered real observable `g`, the recovered light-traffic coefficient is

\[
J_g(c)=\int_0^1(1-u)\langle g,e^{cuQ}g\rangle_\pi\,du.
\]

Put

\[
\Phi(z)=\frac{e^z-1-z}{z^2},\qquad
\Psi(z)=\Phi'(z)=\int_0^1u(1-u)e^{uz}\,du
=\frac{(z-2)e^z+z+2}{z^3}.
\]

Then

\[
J_g'(c)=\langle g,H_Q(c)g\rangle_\pi,
\qquad
H_Q(c)=\frac12\left(Q\Psi(cQ)+[Q\Psi(cQ)]^\dagger\right).
\tag{1.1}
\]

A positive centered eigenvalue of `H_Q(c)` is the established second-order route to a source-valid workload counterexample after the previously proved uniform light-traffic remainder conversion. The preceding mandatory STUCK1 diagnosis isolated the simplest unresolved genuinely nonnormal source-admissible case:

\[
Q_1=
\begin{pmatrix}
-2&1&1&0\\
2&-3&0&1\\
0&2&-3&1\\
0&0&2&-2
\end{pmatrix}.
\tag{1.2}
\]

This chain has uniform stationary law, is doubly stochastically monotone, is nonreversible, and its nonzero characteristic factor is

\[
\lambda^3+10\lambda^2+33\lambda+32,
\]

whose discriminant is `-416`. Thus it has a genuine complex conjugate eigenpair. It is also an exactly certified extreme ray of the fixed-uniform four-state admissible cone from the preceding B16 work.

The recovery question is therefore

\[
H_{Q_1}(c)|_{\{1\}^\perp}\stackrel{?}{\preceq}0
\qquad(c>0).
\tag{1.3}
\]

We prove the stronger strict inequality for every positive `c`.

## 2. Centered representation and reflection blocks

Use the orthonormal centered basis

\[
u=\frac12(1,-1,-1,1)^T,
\quad
v=\frac12(1,1,-1,-1)^T,
\quad
w=\frac12(1,-1,1,-1)^T.
\]

In this basis the centered generator is

\[
M=
\begin{pmatrix}
-4&-1&1\\
1&-2&1\\
-1&1&-4
\end{pmatrix}.
\tag{2.1}
\]

State reflection makes `u` even and `v,w` odd. The self-adjoint derivative therefore has the exact block form

\[
H(c):=\operatorname{Sym}(M\Psi(cM))
=
\begin{pmatrix}
h_+(c)&0&0\\
0&&\\
0&&H_-(c)
\end{pmatrix},
\tag{2.2}
\]

where `H_-(c)` is real symmetric `2 x 2`. Hence strict negativity is equivalent to

\[
h_+(c)<0,
\qquad
\operatorname{tr}H_-(c)<0,
\qquad
\det H_-(c)>0.
\tag{2.3}
\]

The proof splits at `c=3/2`: an exact finite Bernstein certificate handles the compact interval, while a resolvent/energy certificate handles the whole tail.

# B11 -- dualize: exact inverse decomposition of the matrix function

Because `M` is invertible on the centered space and

\[
\Psi(z)=\frac{(z-2)e^z+z+2}{z^3},
\]

direct functional calculus gives

\[
\boxed{
 c^2M\Psi(cM)
 =M^{-1}+\frac2cM^{-2}
 +e^{cM}\left(M^{-1}-\frac2cM^{-2}\right).
}
\tag{3.1}
\]

The exact inverse is

\[
M^{-1}=\frac1{32}
\begin{pmatrix}
-7&3&-1\\
-3&-17&-5\\
1&-5&-9
\end{pmatrix}.
\tag{3.2}
\]

Define

\[
S_1=\operatorname{Sym}(M^{-1}),
\qquad
S_2=\operatorname{Sym}(M^{-2}),
\qquad
L(c)=S_1+\frac2cS_2.
\tag{3.3}
\]

Exact multiplication gives

\[
S_1=
\begin{pmatrix}
-7/32&0&0\\
0&-17/32&-5/32\\
0&-5/32&-9/32
\end{pmatrix},
\tag{3.4}
\]

and

\[
S_2=\frac1{1024}
\begin{pmatrix}
39&0&0\\
0&305&133\\
0&133&105
\end{pmatrix}.
\tag{3.5}
\]

Its leading principal minors are

\[
\frac{39}{1024},\qquad
\frac{11895}{1048576},\qquad
\frac{273}{524288},
\]

all strictly positive. Thus

\[
\boxed{S_2\succ0.}
\tag{3.6}
\]

# B13 -- a Loewner monovariant controls the entire large-c tail

Since `S_2` is positive definite,

\[
L'(c)=-\frac2{c^2}S_2\prec0.
\tag{4.1}
\]

Thus `L(c)` is strictly decreasing in Loewner order. At the single rational point `c=3/2`,

\[
L(3/2)=
\begin{pmatrix}
-43/256&0&0\\
0&-103/768&13/768\\
0&13/768&-37/256
\end{pmatrix}.
\tag{4.2}
\]

Moreover

\[
-\left(L(3/2)+\frac3{25}I\right)
\]

has exact leading principal minors

\[
\frac{307}{6400},\qquad
\frac{83197}{122880000},\qquad
\frac{13201}{4608000000},
\]

so Sylvester's criterion yields

\[
L(3/2)\prec-\frac3{25}I.
\]

By (4.1), for every `c>=3/2`,

\[
\boxed{L(c)\prec-\frac3{25}I.}
\tag{4.3}
\]

It remains to dominate the exponential term in (3.1). We have

\[
\operatorname{Sym}(M)=
\begin{pmatrix}
-4&0&0\\
0&-2&1\\
0&1&-4
\end{pmatrix}.
\]

The matrix

\[
-\left(\operatorname{Sym}(M)+\frac{19}{12}I\right)
\]

has exact leading principal minors

\[
\frac{29}{12},\qquad
\frac{145}{144},\qquad
\frac{29}{1728},
\]

hence

\[
\operatorname{Sym}(M)\prec-\frac{19}{12}I.
\tag{4.4}
\]

For `x(t)=e^{tM}x(0)`, differentiating `||x(t)||_2^2` and using (4.4) gives the standard energy estimate

\[
\boxed{\|e^{tM}\|_2\le e^{-19t/12}.}
\tag{4.5}
\]

Exact Frobenius calculations give

\[
\|M^{-1}\|_F^2=\frac{489}{1024}<\frac{49}{100},
\qquad
\|M^{-2}\|_F^2=\frac{149929}{1048576}<\frac4{25}.
\]

Therefore

\[
\|M^{-1}\|_2<\frac7{10},
\qquad
\|M^{-2}\|_2<\frac25.
\tag{4.6}
\]

For `c>=3/2`, equations (4.5)--(4.6) imply

\[
\left\|e^{cM}\left(M^{-1}-\frac2cM^{-2}\right)\right\|_2
<e^{-19c/12}\left(\frac7{10}+\frac4{5c}\right)
\le \frac{37}{30}e^{-19/8}.
\tag{4.7}
\]

No numerical exponential bound is needed. The degree-five Taylor lower bound gives exactly

\[
e^{19/8}>
\sum_{k=0}^{5}\frac{(19/8)^k}{k!}
=\frac{40829419}{3932160}
>\frac{185}{18}.
\]

Hence

\[
\frac{37}{30}e^{-19/8}
<\frac{37}{30}\frac{18}{185}
=\frac3{25}.
\tag{4.8}
\]

Taking symmetric parts cannot increase operator norm. Combining (3.1), (4.3), and (4.8) therefore proves

\[
\boxed{H(c)\prec0\qquad(c\ge3/2).}
\tag{4.9}
\]

This settles the entire unbounded tail by one monotone matrix inequality plus one elementary exponential estimate.

# B19 -- exact finite algorithm on 0 <= c <= 3/2

The matrix function has the absolutely convergent power series

\[
M\Psi(cM)
=
\sum_{n=0}^{\infty}
\frac{c^nM^{n+1}}{n!(n+2)(n+3)}.
\tag{5.1}
\]

Let `H_N(c)` be the symmetric truncation through `N=50`, and write its reflection blocks as `h_N(c)` and

\[
H_{-,N}(c)=
\begin{pmatrix}
a_N(c)&b_N(c)\\b_N(c)&d_N(c)
\end{pmatrix}.
\]

Because

\[
\|M\|_2\le\sqrt{\|M\|_1\|M\|_\infty}\le6
\]

and `0<=c<=3/2`, every matrix entry of the omitted tail has absolute value at most

\[
\epsilon
\le 6\sum_{n=51}^{\infty}\frac{9^n}{n!}
\le 6e^9\frac{9^{51}}{51!}
<6\,3^9\frac{9^{51}}{51!}
<3.532\times10^{-13}.
\tag{5.2}
\]

For a polynomial `p(c)=sum_{k=0}^n p_k c^k`, its exact Bernstein coefficients on `[0,B]`, `B=3/2`, are

\[
b_j=\sum_{k=0}^j p_kB^k\frac{\binom jk}{\binom nk},
\qquad 0\le j\le n.
\tag{5.3}
\]

The Bernstein convex-hull property gives global interval bounds from these rational coefficients. Applying (5.3) to the exact rational coefficient lists of `h_N`, `tr(H_{-,N})`, and `det(H_{-,N})` gives

\[
\max_{[0,3/2]} h_N(c)
\le -0.07319147107671882\ldots,
\tag{5.4}
\]

\[
\max_{[0,3/2]}\operatorname{tr}H_{-,N}(c)
\le -0.16264256497775212\ldots,
\tag{5.5}
\]

\[
\min_{[0,3/2]}\det H_{-,N}(c)
\ge 0.006460307878780131\ldots.
\tag{5.6}
\]

All displayed decimals are summaries of exact rational Bernstein bounds; the checker archives the complete rational values.

Adding the entrywise tail (5.2) gives the certified global inequalities

\[
\boxed{h_+(c)<-0.07319147107636566\ldots<0,}
\tag{5.7}
\]

\[
\boxed{\operatorname{tr}H_-(c)<-0.1626425649770458\ldots<0.}
\tag{5.8}
\]

For the determinant, if each omitted entry has magnitude at most `epsilon`, then

\[
|\det H_- - \det H_{-,N}|
\le
\epsilon(A_N+D_N+2B_N)+2\epsilon^2,
\tag{5.9}
\]

where `A_N,D_N,B_N` are exact Bernstein absolute bounds for `a_N,d_N,b_N`. The exact computation gives

\[
\boxed{\det H_-(c)>0.006460307878309258\ldots>0}
\tag{5.10}
\]

throughout `[0,3/2]`. Equations (5.7)--(5.10), together with the `1 x 1 + 2 x 2` reflection decomposition, imply

\[
\boxed{H(c)\prec0\qquad(0\le c\le3/2).}
\tag{5.11}
\]

The finite exact checker is

`research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T133700Z__P0290_q1_exact_certificate.py`

creation commit `904cfda95f4d32ed3c884120607277dfc572064f`.

Its archived executed output is

`research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T133700Z__P0290_q1_exact_certificate.out`

creation commit `a4fe4b60f3719292e2c115a03115d7c988fd4246`, ending `ALL_EXACT_CHECKS_PASS`.

Both files were read back at their exact creation SHAs before this note was written.

# 6. Fixed-ray theorem and meaning for P0290

**Theorem 6.1 (global Q1 second-order exclusion).** For the source-admissible four-state generator `Q_1` in (1.2),

\[
\boxed{
H_{Q_1}(c)|_{\{1\}^{\perp}}\prec0
\qquad\text{for every }c>0.
}
\]

Equivalently, for every nonconstant deterministic real observable `g`, the triangular covariance transform satisfies

\[
\boxed{J_g'(c)<0\qquad(c>0).}
\]

### Proof

The compact regime is (5.11). The tail regime is (4.9). Their union covers every `c>0`. `square`

This theorem eliminates the exact complex-spectrum extreme ray chosen by the mandatory STUCK1 recovery. It is stronger than checking Boolean images: **every** deterministic observable on this chain is second-order safe. It also shows concretely that complex spectrum plus nonnormality is still insufficient to produce the desired reversal.

It does **not** imply the source workload theorem. The remaining possibilities include another four-state generator, a higher-dimensional hidden chain, a higher-order light-traffic mechanism, or a moderate/heavy-load mechanism. In particular, the source metric remains

`Delta_Ross: UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED (NO MOVEMENT)`.

# 7. Literature/status boundary, 2026-09-19

The controlling 2022 accepted manuscript/journal Problem 2 was rechecked this run. A bounded 2026-09-19 search for the exact title/problem, deterministic images of doubly stochastically monotone CTMCs, and Ross workload monotonicity found the original source and no explicit later source-specific solution. This is negative evidence only. It does not establish present openness, novelty of Theorem 6.1, or absence of an equivalent result under different terminology.

The result above is therefore recorded only as a new internal **PARTIAL** theorem relative to the recovered campaign history. No source-level PROVED/REFUTED/KNOWN claim is made, and no closure audit is requested from this note alone.

# 8. Next mathematical attack

The fixed extreme ray has been completely eliminated. The next nonrepeating Section-B triple is **B3 / B5 / B20**:

- **B3 -- prove something stronger:** try to extend Theorem 6.1 from `a=1` to the complete source-admissible reflection family `Q_a`, `0<a<=1`.
- **B5 -- add a parameter and differentiate:** differentiate the inverse/Loewner and compact-block margins in `a` to see whether the `a=1` certificate propagates through the family rather than restarting a two-dimensional scan.
- **B20 -- find why the algorithm fails:** if a uniform-in-`a` certificate breaks, isolate the first exact obstruction (loss of inverse Loewner margin, dissipation margin, or compact determinant margin). That obstruction, rather than a blind floating search, becomes the next candidate counterexample mechanism.
