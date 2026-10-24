# P0290: derivative duality, scale reduction, and endpoint localization of any light-traffic reversal

Target: Lasse Leskelä (2022), *Ross's second conjecture and supermodular stochastic ordering*, Problem 2 (journal p. 214).

Status: **PARTIAL**. This note does not prove or refute the source problem. It converts the remaining second-order counterexample search into an exact self-adjoint eigenvalue question, proves that any positive answer immediately yields a rigorous source-valid workload counterexample with an explicit small-intensity threshold, and proves that no such derivative reversal can occur at either the zero-scale or infinite-scale endpoint for a fixed irreducible finite chain.

The preceding R7-04 artifact `2026-09-19T095000Z__P0290_four_state_oscillator_and_service_reduction.md` established an exact four-state doubly monotone nonreversible family with complex spectrum and covariance rebound, but no rise of the triangular workload transform, and proved the bounded-service light-traffic remainder bound used below.

---

## 1. Setup

Let `Q` be the generator of an irreducible finite-state continuous-time Markov chain with stationary law `pi`, and write

\[
\langle u,v\rangle_\pi=\sum_i\pi_i u_i v_i,
\qquad P_t=e^{tQ}.
\]

Let `g` be a real centered observable,

\[
\langle g,1\rangle_\pi=0,
\]

and define its stationary covariance for `t>=0` by

\[
C_g(t)=\langle g,P_tg\rangle_\pi.
\]

The source-faithful second-order triangular transform is

\[
J_g(c)=\int_0^1(1-u)C_g(cu)\,du,
\qquad c>0.
\tag{1.1}
\]

Adding a constant to the intensity observable changes only the constant mean term: if `f=g+b`, then the `c`-dependent centered part of the second-order coefficient is still `J_g(c)`. Thus a general deterministic nonnegative source image can be recovered from any centered real `g` by taking `b>=-min_i g_i`.

---

# B5. Add the scale parameter and differentiate exactly

## 2. Entire matrix-function formula

Define

\[
\Phi(z)=\frac{e^z-1-z}{z^2},
\qquad \Phi(0)=\frac12.
\tag{2.1}
\]

The scalar identity

\[
\int_0^1(1-u)e^{zu}\,du=\Phi(z)
\]

extends by the convergent power series to matrices. Therefore

\[
\boxed{J_g(c)=\langle g,\Phi(cQ)g\rangle_\pi.}
\tag{2.2}
\]

Let

\[
\Psi(z)=\Phi'(z)
=\frac{(z-2)e^z+z+2}{z^3},
\qquad \Psi(0)=\frac16.
\tag{2.3}
\]

Since `Q` commutes with every entire function of `Q`, differentiation gives

\[
\boxed{
J_g'(c)=\langle g,Q\Psi(cQ)g\rangle_\pi.
}
\tag{2.4}
\]

Equivalently, using

\[
\Phi(z)=\sum_{m=0}^\infty\frac{z^m}{(m+2)!},
\]

we have the absolutely convergent expansion

\[
Q\Psi(cQ)
=
\sum_{m=1}^\infty
\frac{m c^{m-1}Q^m}{(m+2)!}.
\tag{2.5}
\]

This representation avoids eigenvector conditioning and is valid at repeated or defective eigenvalues.

## 3. Exact scale covariance

For `r>0`, replacing the hidden generator by `rQ` merely speeds the hidden chain by `r`. From (1.1),

\[
J_g^{(rQ)}(c)=J_g^{(Q)}(rc),
\]

and hence

\[
\boxed{
\frac{d}{dc}J_g^{(rQ)}(c)
=r\,\frac{d}{dc}J_g^{(Q)}(rc).
}
\tag{3.1}
\]

Positive scaling preserves irreducibility, the stationary law, stochastic monotonicity of `Q`, and stochastic monotonicity of its stationary reversal. Thus the sign search for a second-order reversal depends only on the product `cQ`. In particular, an existential derivative witness at an arbitrary `c_0>0` can equivalently be moved to `c=1` by replacing `Q` with `c_0Q`.

This removes one artificial degree of freedom from any exact counterexample search.

---

# B11. Dualize the search to one self-adjoint eigenvalue

## 4. The derivative quadratic form

Let `A^dagger` denote the adjoint of a matrix `A` in `L^2(pi)`:

\[
A^\dagger=D_\pi^{-1}A^T D_\pi,
\qquad D_\pi=\operatorname{diag}(\pi).
\]

Define the self-adjoint operator

\[
\boxed{
H_Q(c)=\frac12\left(
Q\Psi(cQ)+[Q\Psi(cQ)]^\dagger
\right).
}
\tag{4.1}
\]

Because a real quadratic form only sees the self-adjoint part,

\[
\boxed{
J_g'(c)=\langle g,H_Q(c)g\rangle_\pi.
}
\tag{4.2}
\]

Let

\[
\mathcal H_0=\{g:\langle g,1\rangle_\pi=0\}.
\]

The exact worst derivative at fixed `(Q,c)` is therefore

\[
\boxed{
\sup_{g\in\mathcal H_0,\ \|g\|_\pi=1}J_g'(c)
=\lambda_{\max}\bigl(H_Q(c)|_{\mathcal H_0}\bigr).
}
\tag{4.3}
\]

This is the useful dual formulation: instead of scanning Boolean images one at a time, one diagonalizes one self-adjoint operator. A positive eigenvalue supplies the strongest real deterministic image at that `(Q,c)`.

## 5. Positive eigenvalue implies a source-valid counterexample

Assume for a source-admissible hidden chain `Q` that

\[
\lambda_{\max}\bigl(H_Q(c_0)|_{\mathcal H_0}\bigr)>0.
\]

Choose a real centered unit eigenvector `g` with `J_g'(c_0)>0`. By continuity there exist

\[
0<c_1<c_2
\]

arbitrarily close to `c_0` such that

\[
\delta:=J_g(c_2)-J_g(c_1)>0.
\tag{5.1}
\]

Choose a constant `b` so that

\[
f=g+b\ge0,
\qquad M=\max_i f_i.
\]

Because centering removes the added constant,

\[
J_f(c_2)-J_f(c_1)=\delta.
\tag{5.2}
\]

Now use deterministic unit service and Cox intensity

\[
\lambda_c(t)=\varepsilon f(X_{ct}).
\]

The previously proved bounded-service expansion specializes to

\[
w_\varepsilon(c)
=
\frac{\varepsilon}{2}\,\mathbb E_\pi f
+\varepsilon^2J_f(c)+R_\varepsilon(c),
\tag{5.3}
\]

with the uniform bound

\[
0\le R_\varepsilon(c)
\le
\frac{\varepsilon^3M^3}{2(1-\varepsilon M)}
\qquad(\varepsilon M<1).
\tag{5.4}
\]

Hence

\[
w_\varepsilon(c_2)-w_\varepsilon(c_1)
\ge
\varepsilon^2\delta
-
\frac{\varepsilon^3M^3}{2(1-\varepsilon M)}.
\tag{5.5}
\]

The right side is strictly positive whenever

\[
\boxed{
0<\varepsilon<
\frac{2\delta}{M^3+2\delta M}.
}
\tag{5.6}
\]

The displayed upper bound is automatically `<1/M`, so stability is included. Therefore:

**Reduction theorem.** A single source-admissible finite generator `Q` and a single `c_0>0` for which `H_Q(c_0)` has a positive eigenvalue on the centered subspace give a rigorous counterexample to Leskelä Problem 2 for a deterministic nonnegative image and deterministic unit service. No queueing simulation or moderate-load computation is then needed.

Conversely, if `H_Q(c)` is negative semidefinite on `H_0` for every source-admissible finite `Q` and every `c>0`, the entire established second-order light-traffic refutation route is closed.

---

# B26. Hunt the sporadic case: endpoint reversals are impossible

The dual criterion raises the possibility that a positive eigenvalue might hide near the singular endpoints `c=0` or `c=infinity`. For each fixed irreducible finite chain this cannot happen.

## 6. Strict negativity near `c=0`

From (2.5),

\[
H_Q(0)=\frac16\operatorname{Sym}_\pi(Q),
\]

so

\[
J_g'(0)=\frac16\langle g,Qg\rangle_\pi.
\tag{6.1}
\]

Stationarity gives the exact Dirichlet identity

\[
\langle g,Qg\rangle_\pi
=-\frac12\sum_{i,j}\pi_iq_{ij}(g_j-g_i)^2.
\tag{6.2}
\]

For an irreducible chain the underlying undirected graph is connected, so the right side vanishes only for constant `g`. A centered nonzero `g` is not constant. Therefore

\[
\boxed{J_g'(0)<0\quad\text{for every nonzero centered }g.}
\tag{6.3}
\]

Because `H_Q(c)` depends continuously on `c` and the unit sphere of the finite-dimensional centered subspace is compact, there exists `c_-(Q)>0` such that

\[
H_Q(c)|_{\mathcal H_0}\prec0
\qquad (0\le c<c_-(Q)).
\tag{6.4}
\]

Thus no infinitesimal-scale sporadic counterexample exists.

## 7. Strict negativity for sufficiently large `c`

Finite irreducibility gives exponential mixing on the centered subspace. Put

\[
A_g=\int_0^\infty C_g(t)\,dt
=\langle g,(-Q)^{-1}g\rangle_\pi,
\tag{7.1}
\]

where the inverse is on `H_0`. If `h=(-Q)^{-1}g`, then `g=-Qh` and

\[
A_g=\langle -Qh,h\rangle_\pi
=\frac12\sum_{i,j}\pi_iq_{ij}(h_j-h_i)^2.
\tag{7.2}
\]

For nonzero centered `g`, the solution `h` is nonconstant, hence

\[
A_g>0.
\tag{7.3}
\]

Also let

\[
B_g=\int_0^\infty tC_g(t)\,dt,
\]

which is finite by exponential mixing. From

\[
J_g(c)
=
\frac1c\int_0^c C_g(t)\,dt
-
\frac1{c^2}\int_0^c tC_g(t)\,dt,
\tag{7.4}
\]

we obtain

\[
J_g(c)=\frac{A_g}{c}-\frac{B_g}{c^2}+O(e^{-\gamma c}/c)
\tag{7.5}
\]

for some `gamma>0`, and therefore

\[
\boxed{
J_g'(c)=-\frac{A_g}{c^2}+O(c^{-3})<0
\quad\text{for all sufficiently large }c.
}
\tag{7.6}
\]

Again compactness of the centered unit sphere, together with the finite-dimensional resolvent representation, gives a chain-dependent `c_+(Q)<infinity` for which the maximal derivative is negative for all `c>c_+(Q)`.

## 8. Consequence: every second-order counterexample is an intermediate-scale resonance

Combining (6.4) and (7.6): for every fixed irreducible finite source-admissible hidden chain, any positive eigenvalue in the derivative dual must occur at an intermediate scale

\[
\boxed{
c\in[c_-(Q),c_+(Q)].
}
\tag{8.1}
\]

Thus neither a zero-scale degeneracy nor an infinite-scale tail can generate the desired light-traffic reversal. The only remaining second-order mechanism is a genuine intermediate-scale resonance of the nonselfadjoint semigroup strong enough to make `H_Q(c)` positive on the centered subspace.

This sharply explains the earlier four-state result: complex eigenvalues and pointwise covariance rebound are possible, but they are not by themselves enough. What must change sign is the self-adjoint derivative operator (4.1).

---

## 9. Current mathematical status and next exact target

The frozen source metric remains

`Delta_Ross = UNKNOWN/UNMEASURED`.

No positive eigenvalue of `H_Q(c)` has yet been certified for a source-admissible doubly monotone chain, so this note does not move the source-level workload margin.

The next decisive finite-dimensional question is now exact:

> Does double stochastic monotonicity force `H_Q(c)|_{H_0} <= 0` for every finite irreducible generator `Q` and every `c>0`?

A **NO** plus (5.6) immediately refutes the source problem. A **YES** closes the complete second-order light-traffic route and forces subsequent work to third-order and higher queueing interactions.

For four states, the natural next attack is to write the forward- and reverse-monotonicity constraints as a polyhedral cone in the jump rates, use the scale covariance (3.1) to normalize one degree of freedom, and seek either (i) an exact rational cone point and rational interval on which a principal minor of `-H_Q(c)` changes sign, or (ii) a cone-dual certificate that `-H_Q(c)` is positive semidefinite. Numerical eigendecomposition alone is not a certificate, especially near repeated eigenvalues; the entire series (2.5) is the safe representation for any certified computation.