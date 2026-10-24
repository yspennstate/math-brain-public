# P0290: reversible-neighborhood exclusion, reflection reduction, and the fixed-stationary-law polyhedral search

Target: Lasse Leskelä (2022), *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100, 213--215, Problem 2 on journal p. 214.

Status: **PARTIAL / OPEN**.  This note does not prove or refute the source problem.  It continues the exact light-traffic route after the recovered R7-04 artifacts on the four-state oscillator and the derivative dual.  The new results are theorem-sized and proved below:

1. **B6 (deform from a solved point):** the complete second-order light-traffic derivative is strictly negative not only for every irreducible reversible finite CTMC, but throughout an open neighborhood of each such generator.  Hence a second-order counterexample cannot be an arbitrarily small nonreversible perturbation of a fixed reversible chain.
2. **B14 (find the group acting):** for the exact four-state family `Q_a` previously constructed by R7-04, the derivative operator commutes with state reflection.  Its all-observable sign question splits into one scalar even channel and one `2 x 2` odd block.
3. **B27 (swap the quantifiers):** after fixing a stationary law `pi`, double stochastic monotonicity is a finite system of linear inequalities in the jump rates.  The scale variable can be absorbed into the generator.  Therefore the entire second-order refutation problem at fixed `pi` is exactly the question whether one self-adjoint eigenvalue functional becomes positive anywhere on an explicit polyhedral cone.

The frozen source metric remains `Delta_Ross = UNKNOWN/UNMEASURED`; none of these reductions is itself a positive source-valid workload margin.

---

## 1. Recovered setup

Let `Q` be the generator of an irreducible finite-state CTMC with stationary distribution `pi`.  On real functions write

\[
\langle u,v\rangle_\pi=\sum_i\pi_i u_i v_i,
\qquad
\mathcal H_0(Q)=\{g:\langle g,1\rangle_\pi=0\}.
\]

For centered `g`, the covariance and triangular light-traffic transform are

\[
C_g(t)=\langle g,e^{tQ}g\rangle_\pi,
\qquad
J_g(c)=\int_0^1(1-u)C_g(cu)\,du.
\tag{1.1}
\]

The preceding R7-04 artifact proved the entire-function identities

\[
\Phi(z)=\frac{e^z-1-z}{z^2},
\qquad
\Psi(z)=\Phi'(z)=\frac{(z-2)e^z+z+2}{z^3},
\tag{1.2}
\]

(with removable values at zero) and

\[
J_g(c)=\langle g,\Phi(cQ)g\rangle_\pi,
\qquad
J_g'(c)=\langle g,Q\Psi(cQ)g\rangle_\pi.
\tag{1.3}
\]

Let `A^dagger` denote the `L^2(pi)` adjoint.  Define

\[
H_Q(c)=\frac12\bigl(Q\Psi(cQ)+[Q\Psi(cQ)]^\dagger\bigr).
\tag{1.4}
\]

Then

\[
J_g'(c)=\langle g,H_Q(c)g\rangle_\pi,
\tag{1.5}
\]

and a positive eigenvalue of `H_Q(c)` on `\mathcal H_0(Q)` gives, by the already proved bounded-service remainder estimate, a rigorous source-valid workload counterexample after shifting the corresponding eigenfunction by a constant and taking a sufficiently small intensity amplitude.

The question in this note is therefore the sign of `H_Q(c)`.

---

# B6. Deform from the reversible point

## 2. Scalar sign at a reversible generator

Assume first that `Q_0` is irreducible and reversible with stationary law `pi_0`.  Then `Q_0` is self-adjoint in `L^2(pi_0)`.  Its centered spectrum consists of finitely many eigenvalues

\[
-\alpha_1,\ldots,-\alpha_{n-1},
\qquad \alpha_j>0.
\]

Put

\[
\varphi(x)=\Phi(-x)=\frac{e^{-x}-1+x}{x^2}.
\]

A direct differentiation gives

\[
-\varphi'(x)
=
\frac{x-2+(x+2)e^{-x}}{x^3}
=:g_0(x).
\tag{2.1}
\]

The numerator

\[
N(x)=x-2+(x+2)e^{-x}
\]

satisfies `N(0)=0` and

\[
N'(x)=1-(x+1)e^{-x}>0\qquad(x>0),
\]

because `e^x>1+x` for `x>0`.  Hence

\[
g_0(x)>0\qquad(x>0).
\tag{2.2}
\]

On an eigenvector with eigenvalue `-alpha_j`, the derivative operator has eigenvalue

\[
\frac{d}{dc}\Phi(-\alpha_j c)
=
-\alpha_j g_0(\alpha_j c)<0.
\tag{2.3}
\]

Therefore

\[
H_{Q_0}(c)|_{\mathcal H_0(Q_0)}\prec0
\qquad\text{for every }c>0.
\tag{2.4}
\]

This is the familiar reversible exclusion, but the strictness is what permits the deformation argument below.

## 3. A global open-neighborhood theorem

**Theorem 3.1 (reversible-neighborhood exclusion).**  Let `Q_0` be any finite irreducible reversible CTMC generator.  There exists a neighborhood `U` of `Q_0` within the finite-state generator space such that every irreducible generator `Q in U` satisfies

\[
H_Q(c)|_{\mathcal H_0(Q)}\prec0
\qquad\text{for every }c>0.
\tag{3.1}
\]

In particular, if `Q_0` is also doubly stochastically monotone, no second-order P0290 counterexample can converge to `Q_0` through source-admissible generators.

### Proof

There are three scale regimes.

### 3.1 Small `c`

The power series of `Psi` gives

\[
Q\Psi(cQ)=\frac16Q+O(c)
\qquad(c\downarrow0),
\]

uniformly for `Q` in a bounded finite-dimensional neighborhood.  Consequently

\[
H_Q(0)=\frac16\operatorname{Sym}_\pi(Q).
\tag{3.2}
\]

For every stationary finite generator,

\[
\langle h,Qh\rangle_\pi
=-\frac12\sum_{i,j}\pi_iq_{ij}(h_j-h_i)^2.
\tag{3.3}
\]

At the irreducible `Q_0`, the right side is strictly negative on the centered unit sphere.  Irreducibility persists after restricting to a sufficiently small generator neighborhood that keeps one fixed spanning collection of positive edges positive.  The stationary law depends continuously on `Q` there.  By finite-dimensional compactness, after shrinking the neighborhood there are constants `eta_0>0` and `c_0>0` such that

\[
\langle g,H_Q(c)g\rangle_{\pi_Q}\le-\eta_0\|g\|_{\pi_Q}^2
\]

for all centered `g` and all `0\le c\le c_0`.

### 3.2 Intermediate compact interval

Fix any finite `C>c_0`.  At `Q_0`, equation (2.3) and the finite spectral decomposition imply that the largest centered eigenvalue of `H_{Q_0}(c)` is a continuous strictly negative function on `[c_0,C]`.  Hence its maximum there is `-eta_1<0`.

To compare nearby nonreversible generators, conjugate the `L^2(pi_Q)` operator to Euclidean space by `D_{pi_Q}^{1/2}` and project onto the orthogonal complement of `sqrt(pi_Q)`.  The stationary vector, this projection, the matrix exponential, and the entire function `Psi(cQ)` are continuous jointly in `(Q,c)` near an irreducible generator.  Thus, after another shrinking of `U`, the maximal centered eigenvalue remains at most `-eta_1/2` on the whole compact interval `[c_0,C]`.

### 3.3 Large `c`

On the centered subspace `Q` is invertible.  From the closed form for `Psi`,

\[
Q\Psi(cQ)
=
\frac1{c^2}Q^{-1}
+
\frac2{c^3}Q^{-2}
+
E_Q(c),
\tag{3.4}
\]

where `E_Q(c)` is exponentially small after multiplication by the appropriate polynomial powers of `c`; uniformly on a sufficiently small neighborhood of `Q_0`, all nonzero eigenvalues stay in a fixed left half-plane and therefore

\[
\|E_Q(c)\|\le K e^{-\gamma c}/c^2
\tag{3.5}
\]

for fixed positive `K,gamma` and all large `c`.

The leading symmetric form is strictly negative for every irreducible `Q`.  Indeed, for centered nonzero `g`, put `h=Q^{-1}g` in the centered subspace.  Then

\[
\langle g,Q^{-1}g\rangle_\pi
=
\langle Qh,h\rangle_\pi
=-\frac12\sum_{i,j}\pi_iq_{ij}(h_j-h_i)^2<0.
\tag{3.6}
\]

At `Q_0` the largest eigenvalue of `Sym_{pi_0}(Q_0^{-1})` on the centered subspace is therefore strictly negative.  By continuity, after shrinking `U` it stays below `-eta_2<0` for every `Q in U`.  The `c^{-3}` and exponential terms in (3.4) are uniformly dominated by `(eta_2/2)c^{-2}` once `c>=C` for `C` chosen sufficiently large.  Hence

\[
H_Q(c)|_{\mathcal H_0(Q)}\prec0
\qquad(c\ge C,Q\in U).
\]

Combining the three regimes proves (3.1).  `square`

### 3.4 Meaning for the search

The earlier endpoint result said that for a *fixed* irreducible chain any reversal must live at an intermediate scale.  Theorem 3.1 adds a different exclusion: a putative source counterexample also must be genuinely nonreversible in generator space.  It cannot be obtained by taking a fixed reversible doubly monotone chain and introducing an arbitrarily small circulation.

This explains why naive perturbations of birth-death and two-state examples are structurally poor counterexample candidates.

---

# B14. Use the reflection group on the exact four-state family

## 4. The recovered family

The interrupted preceding attempt constructed, for `0<a<=1`,

\[
Q_a=
\begin{pmatrix}
-2&2-a&a&0\\
2&-(2+a)&0&a\\
0&2a&-(2+a)&2-a\\
0&0&2&-2
\end{pmatrix}.
\tag{4.1}
\]

It proved exactly that `pi=(1/4,1/4,1/4,1/4)`, both `Q_a` and its stationary reversal are stochastically monotone, and if `R` reverses the four states then

\[
Q_a^T=RQ_aR,
\qquad R^2=I=R^T.
\tag{4.2}
\]

At `a=5/6` this family has a genuine complex conjugate eigenpair and a Boolean image with a covariance rebound, so it is a meaningful stress test rather than a reversible toy.

## 5. Exact block decomposition of the derivative operator

Put

\[
F_c(Q)=Q\Psi(cQ).
\]

Because `F_c` is an entire matrix function with real coefficients and because of (4.2),

\[
F_c(Q_a)^T
=F_c(Q_a^T)
=F_c(RQ_aR)
=RF_c(Q_a)R.
\tag{5.1}
\]

Since the stationary law is uniform, Euclidean transpose is the stationary adjoint.  Thus

\[
H_{Q_a}(c)
=\frac12\bigl(F_c(Q_a)+RF_c(Q_a)R\bigr).
\tag{5.2}
\]

Conjugating by `R` gives

\[
RH_{Q_a}(c)R=H_{Q_a}(c).
\tag{5.3}
\]

So `H_{Q_a}(c)` commutes with the order-two reflection group.

Use the orthonormal basis

\[
e=\tfrac12(1,1,1,1)^T,
\quad
u=\tfrac12(1,-1,-1,1)^T,
\]
\[
v=\tfrac12(1,1,-1,-1)^T,
\quad
w=\tfrac12(1,-1,1,-1)^T.
\tag{5.4}
\]

Here `e,nu` are `R`-even and `v,w` are `R`-odd.  The constant vector `e` is annihilated by the derivative operator.  Hence on the centered space the block form is exactly

\[
H_{Q_a}(c)|_{\mathcal H_0}
=
\begin{pmatrix}
h_+(a,c)&0&0\\
0& *&*\\
0& *&*
\end{pmatrix},
\tag{5.5}
\]

where the lower-right block `H_-(a,c)` is a real symmetric `2 x 2` matrix on `span{v,w}`.

Therefore the all-observable light-traffic derivative is nonpositive on this whole family if and only if

\[
h_+(a,c)\le0,
\qquad
\operatorname{tr}H_-(a,c)\le0,
\qquad
\det H_-(a,c)\ge0
\tag{5.6}
\]

for every `c>0`.  No scan over Boolean or nonnegative images is needed.

For `a=5/6`, the previously studied Boolean image `(0,1,1,0)` has centered part proportional to `nu`, so its triangular-transform derivative is precisely the scalar channel `h_+(5/6,c)` up to the fixed positive normalization.  The covariance rebound in that channel therefore does **not** by itself say anything about the odd `2 x 2` determinant obstruction.

This reduction leaves three scalar analytic inequalities instead of a continuum of observables.  It is the natural exact target if this family is to be eliminated completely or converted into a counterexample.

---

# B27. Swap the quantifiers and expose the polyhedral cone

## 6. Fixed stationary law makes both monotonicity constraints linear

Fix a strictly positive probability vector

\[
\pi=(\pi_0,\ldots,\pi_{n-1}).
\]

Treat the off-diagonal rates `q_ij (i!=j)` as variables and put

\[
q_{ii}=-\sum_{j\ne i}q_{ij}.
\]

The generator and stationarity constraints

\[
q_{ij}\ge0,
\qquad
\pi Q=0
\tag{6.1}
\]

are linear.

For states in their source order, stochastic monotonicity is given by the standard generator inequalities: for every `i<i'` and every upper set `U={k,...,n-1}` containing neither compared state,

\[
\sum_{j\in U}q_{ij}
\le
\sum_{j\in U}q_{i'j},
\tag{6.2}
\]

and for every lower set `D={0,...,k}` containing neither compared state,

\[
\sum_{j\in D}q_{ij}
\ge
\sum_{j\in D}q_{i'j}.
\tag{6.3}
\]

The stationary reversal has

\[
q^*_{ij}=\frac{\pi_j}{\pi_i}q_{ji}
\qquad(i\ne j).
\tag{6.4}
\]

With `pi` fixed, (6.4) is linear in the same off-diagonal variables.  Applying (6.2)--(6.3) to `Q^*` therefore adds only more linear inequalities.

Consequently:

**Proposition 6.1.**  For fixed positive stationary law `pi`, the set

\[
\mathcal C_\pi
=
\{Q:\pi Q=0,\ Q\text{ and }Q^*\text{ stochastically monotone}\}
\tag{6.5}
\]

is a closed convex polyhedral cone in the off-diagonal jump rates.  If `pi` is rational, it is a rational polyhedral cone.

No spectral calculation is involved in this proposition.

## 7. Absorb the modulation scale into the cone point

The preceding derivative artifact proved the scale identity

\[
J_g^{(rQ)}(c)=J_g^{(Q)}(rc).
\]

At the operator level, if `R=cQ`, then

\[
Q\Psi(cQ)=\frac1cR\Psi(R),
\]

so

\[
\boxed{
H_Q(c)=\frac1c H_R(1),
\qquad R=cQ.
}
\tag{7.1}
\]

Positive scaling preserves `pi`, irreducibility, stochastic monotonicity of `Q`, and stochastic monotonicity of `Q^*`.  Thus `Q in C_pi` if and only if `cQ in C_pi` for `c>0`.

Combining (7.1) with the Rayleigh-quotient dual gives the exact quantifier swap:

\[
\boxed{
\begin{aligned}
&\exists Q\in\mathcal C_\pi\text{ irreducible},\ \exists c>0,\ \exists g\in\mathcal H_0:\ J_g'(c)>0\\
&\qquad\Longleftrightarrow\\
&\exists R\in\mathcal C_\pi\text{ irreducible}:\
\lambda_{\max}\bigl(H_R(1)|_{\mathcal H_0}\bigr)>0.
\end{aligned}}
\tag{7.2}
\]

So neither the observable nor the modulation scale needs to be scanned as an independent outer variable.  For fixed `pi`, the complete second-order refutation route is a single positivity question for a self-adjoint eigenvalue functional on a known polyhedral cone.

Along any ray `R=r\bar Q`, the earlier endpoint theorem says this eigenvalue is strictly negative for all sufficiently small and all sufficiently large `r` when `\bar Q` is irreducible.  Theorem 3.1 additionally removes open neighborhoods of every reversible cone point.  The remaining candidate region is therefore the genuinely nonreversible, intermediate-scale part of `C_pi`.

This formulation suggests a certified next step: choose low-denominator rational `pi`, enumerate or decompose the relevant four-state cone faces exactly, and attack the sign of the three reflection-reduced scalar functions or the principal minors of `-H_R(1)`.  A numerical eigensolver alone is not a closure certificate.

---

## 8. What failed in the bounded exploratory attack

A bounded exploratory search was used only to stress-test the reduction, not as mathematical evidence.  For several fixed stationary laws in dimensions four through eight, random linear objectives were optimized over the linear double-monotonicity constraints and random convex combinations of returned feasible boundary points were tested through the self-adjoint derivative criterion.  No robust positive derivative was found.

One apparent tiny positive value near a nearly reducible boundary point disappeared when the matrix-function derivative was recomputed by direct high-order quadrature; it was cancellation in an inverse-power formula.  This failure is useful: subsequent certified work should use the entire power series or direct positive-order quadrature/interval evaluation rather than subtracting nearly singular `Q^{-1}` and `Q^{-2}` terms near reducibility.

Because the search was neither exhaustive nor interval-certified, it gives **no bound on `Delta_Ross` and no proof that the four-state cone is safe**.

---

## 9. Current conclusion

The second-order counterexample mechanism is now localized more sharply:

- three hidden states are excluded by the previous exact real-spectrum/two-mode theorem;
- an exact four-state doubly monotone complex-spectrum/covariance-rebound family exists, but covariance rebound alone is insufficient;
- every fixed irreducible reversible generator has an entire open neighborhood with no second-order reversal at any scale;
- the four-state reflection family reduces to one scalar and one `2 x 2` block;
- for each fixed stationary law, source admissibility is a polyhedral cone and the modulation scale can be absorbed into the cone point.

The decisive remaining second-order question is therefore:

\[
\text{Does there exist a positive stationary law }\pi\text{ and an irreducible }R\in\mathcal C_\pi
\text{ with }
\lambda_{\max}(H_R(1)|_{\mathcal H_0})>0?
\]

A YES, together with the already proved explicit small-intensity remainder threshold, refutes Leskelä Problem 2.  A proof of NO for all finite `pi` would close the entire second-order light-traffic route but would still not by itself prove the full queueing statement.

No independent P26 or distinct OTHER-track audit is claimed here.
