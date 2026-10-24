Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum; authenticated runtime reasoning-effort telemetry and a binding model/effort selector are not exposed.

# C0130 — exact universal depth-three escape formula by a signed hypergeometric resolvent

Target: `C0130`, Elena Kosygina–Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, Problem 3.12.

Status: **PARTIAL relative to the full outside source, but a genuine movement of the frozen finite-depth metric.** This note proves an exact special-function formula for the never-return probability for **every source-valid i.i.d. bounded cookie law neutral after visit 3** in the transient regime. Thus the R7-05 frozen quantity moves from `M_closed=2` to `M_closed=3`. It does not solve arbitrary finite depth, nor the broader stationary-ergodic branch of the survey problem.

The construction deliberately uses a signed auxiliary kernel. Positivity of the auxiliary low rows is unnecessary; only the true excited-walk kernel is used for the final uniqueness argument. This removes the nonnegative-cookie restriction that remained in the preceding GWI reduction.

## 1. Source-valid depth-three setup

At each site let the cookie stack be an i.i.d. copy of

\[
(p_1,p_2,p_3,1/2,1/2,\ldots),
\qquad 0\le p_j\le1,
\]

under the source's bounded i.i.d. and weak-ellipticity assumptions. Put

\[
\alpha_j=2p_j-1,
\qquad
\delta=\mathbb E(\alpha_1+\alpha_2+\alpha_3).
\]

First assume right transience, so `delta>1`. For a fresh site let `S_k` denote the number of successes before the `k`-th failure in its cookie Bernoulli sequence, with `S_0=0`. The standard forward branching-like chain is

\[
V_{n+1}=S_{n+1,V_n},
\]

with absorbing state 0. Let its positive-state transition kernel be `K`, and let

\[
s(k)=\mathbb P_k(V_n>0\text{ for all }n\ge0).
\]

The cumulative R7-05 Siegmund-duality theorem gives

\[
\pi_i=s(i+1)-s(i)
\]

for the stationary law `pi` of the dual backward chain, hence in particular

\[
\pi_0=s(1).
\]

Together with the already-proved first-step escape identity,

\[
\boxed{p_{\rm esc}=\mathbb E[p_1]\,s(1).}
\tag{1.1}
\]

Thus it is enough to evaluate `s(1)` exactly.

Define

\[
T(z)=\frac1{2-z}
\]

and the cubic polynomial

\[
\boxed{
B(z)=\mathbb E\prod_{j=1}^3\big((1-\alpha_j)+\alpha_j z\big).
}
\tag{1.2}
\]

Then

\[
B(1)=1,
\qquad
B'(1)=\delta.
\tag{1.3}
\]

For every `k>=3`, the exact tail-row identity proved in the previous run is

\[
\boxed{
\mathbb E[z^{S_k}]=B(z)T(z)^k.
}
\tag{1.4}
\]

Indeed, after the first three tosses, if `R` successes occurred, then there were `3-R` failures and `k-3+R` further fair failures are required; the elementary identity

\[
T(z)^{-1}(1-p+pzT(z))=(1-\alpha)+\alpha z
\]

gives (1.4) after multiplying the three cookie factors and annealing.

## 2. Exact two-row defect

Extend the tail formula formally to all nonnegative starting states and denote the resulting row generating functions by

\[
\widetilde Q_k(z)=B(z)T(z)^k,
\qquad k\ge0.
\tag{2.1}
\]

For signed cookies the coefficients of `B` need not all be nonnegative, so the low rows of `\widetilde Q` need not be probability measures. They are nevertheless finite signed measures of total mass one, because `B(1)=T(1)=1`. Their total variations are uniformly finite because each row is a convolution of the fixed finite signed polynomial `B` with the probability law having pgf `T^k`.

The true forward rows agree with `\widetilde Q` for all `k>=3`. For the exceptional rows define the following annealed polynomial coefficients:

\[
\boxed{
A=\frac12\mathbb E\big[(1-\alpha_1)(\alpha_2+\alpha_3-\alpha_2\alpha_3)\big],
}
\tag{2.2}
\]

\[
\boxed{
D=\frac14\mathbb E\big[\alpha_3(1+\alpha_1+\alpha_2-3\alpha_1\alpha_2)\big],
}
\tag{2.3}
\]

\[
\boxed{
C=\frac14\mathbb E\big[\alpha_3(1-\alpha_1)(1-\alpha_2)\big].
}
\tag{2.4}
\]

Direct enumeration of the first three tosses gives, with `P_k(z)=E[z^{S_k}]`,

\[
\boxed{
P_1(z)-\widetilde Q_1(z)=A(1-z)+Dz(1-z),
}
\tag{2.5}
\]

\[
\boxed{
P_2(z)-\widetilde Q_2(z)=C(1-z).
}
\tag{2.6}
\]

These are polynomial identities and remain valid with arbitrary signs of the `alpha_j`.

Let `\widetilde K` be the restriction of `\widetilde Q` to positive states. Then the operator

\[
E:=\widetilde K-K
\]

has only rows 1 and 2. For any vector `f` with `f(0)=0`, writing `x=f(1)` and `y=f(2)`, (2.5)–(2.6) give

\[
\boxed{
(Ef)_1=(A-D)x+Dy,
\qquad
(Ef)_2=Cx.
}
\tag{2.7}
\]

## 3. Method B14 — the Möbius group action linearizes the entire auxiliary semigroup

The central observation is that the linear-fractional map `T` is conjugate to translation. Put

\[
u=\frac1{1-z},
\qquad z=1-\frac1u.
\]

Then

\[
\boxed{
T^n(z)=1-\frac1{u+n}.
}
\tag{3.1}
\]

The signed kernel `\widetilde Q` has an exact semigroup formula.

### Lemma 3.1 (exact n-step signed pgf)

For every `n,k>=0`,

\[
\boxed{
\sum_{j\ge0}\widetilde Q^{\,n}(k,j)z^j
=
T^n(z)^k\prod_{\ell=0}^{n-1}B(T^\ell(z)).
}
\tag{3.2}
\]

### Proof

The claim is trivial for `n=0`. If it holds for `n`, one more application of a row with pgf `B(z)T(z)^m` gives

\[
B(z)\left[T^n(T(z))^k\prod_{\ell=0}^{n-1}B(T^\ell(T(z)))\right]
=T^{n+1}(z)^k\prod_{\ell=0}^{n}B(T^\ell(z)).
\]

No positivity was used. QED.

Define

\[
\Pi_n(u)=\prod_{\ell=0}^{n-1}B\!\left(1-\frac1{u+\ell}\right),
\qquad \Pi_0(u)=1,
\tag{3.3}
\]

and

\[
\boxed{
\Phi_k(u)=\sum_{n=0}^{\infty}
\left(\frac{u+n-1}{u+n}\right)^k\Pi_n(u).
}
\tag{3.4}
\]

To see both exact convergence and the hypergeometric structure, define

\[
\mathcal C(u)=u^3B\!\left(1-\frac1u\right).
\]

This is a monic cubic. Let its roots, counted with multiplicity, be `rho_1,rho_2,rho_3`. From (1.3),

\[
\boxed{\rho_1+\rho_2+\rho_3=\delta.}
\tag{3.5}
\]

Moreover

\[
B\!\left(1-\frac1{u+\ell}\right)
=
\frac{\prod_{r=1}^3(u+\ell-\rho_r)}{(u+\ell)^3},
\]

so

\[
\boxed{
\Pi_n(u)=
\frac{(u-\rho_1)_n(u-\rho_2)_n(u-\rho_3)_n}{(u)_n^3}.
}
\tag{3.6}
\]

Gamma-ratio asymptotics give, uniformly for `u` in a compact neighborhood of 1,

\[
\Pi_n(u)=O(n^{-\delta}),
\qquad
\partial_u\Pi_n(u)=O(n^{-\delta}),
\qquad
\partial_u^2\Pi_n(u)=O(n^{-\delta}).
\tag{3.7}
\]

The exponent is independent of `u` because the `u`-coefficients cancel between the three numerator and three denominator Pochhammer symbols. Since `delta>1`, (3.4) and its first two `u`-derivatives converge locally uniformly at `u=1` for `k=0,1,2`.

For example,

\[
\boxed{
\Phi_0(u)=
{}_4F_3\!\left(
\begin{matrix}
 u-\rho_1,u-\rho_2,u-\rho_3,1\\
 u,u,u
\end{matrix};1\right).
}
\tag{3.8}
\]

The `k=1,2` series are contiguous hypergeometric series:

\[
\Phi_1(u)=\frac{u-1}{u}
{}_4F_3\!\left(
\begin{matrix}
 u-\rho_1,u-\rho_2,u-\rho_3,1\\
 u-1,u,u+1
\end{matrix};1\right),
\tag{3.9}
\]

\[
\Phi_2(u)=\left(\frac{u-1}{u}\right)^2
{}_5F_4\!\left(
\begin{matrix}
 u-\rho_1,u-\rho_2,u-\rho_3,u,1\\
 u-1,u-1,u+1,u+1
\end{matrix};1\right),
\tag{3.10}
\]

where at `u=1` the right sides are understood through their removable continuations, equivalently through the absolutely convergent defining series (3.4).

## 4. Extracting the low-state Green matrix exactly

Let

\[
G_{kj}=\sum_{n=0}^{\infty}\widetilde Q^{\,n}(k,j),
\qquad k\ge0,\quad j=0,1,2.
\tag{4.1}
\]

These coefficientwise Green sums converge absolutely. Indeed, by (3.2)–(3.7), for each fixed `j<=2` the coefficient of `z^j` is `O(n^{-delta})` for fixed `k`, and `delta>1`.

Because `z=1-1/u` has

\[
\frac{dz}{du}\bigg|_{u=1}=1,
\qquad
\frac{d^2z}{du^2}\bigg|_{u=1}=-2,
\]

coefficient extraction at `z=0` gives

\[
\boxed{G_{k0}=\Phi_k(1),}
\tag{4.2}
\]

\[
\boxed{G_{k1}=\Phi_k'(1),}
\tag{4.3}
\]

\[
\boxed{
G_{k2}=\frac{\Phi_k''(1)+2\Phi_k'(1)}2.
}
\tag{4.4}
\]

Thus the entire `3 x 3` low-state Green block needed below is an exact special-function object, with no unknown stationary law or hitting probability remaining.

The zero column is especially simple. Put `a_r=1-rho_r` and

\[
F_0={}_3F_2(a_1,a_2,a_3;1,1;1),
\]

\[
F_1={}_3F_2(a_1,a_2,a_3;1,2;1),
\]

\[
F_2={}_3F_2(a_1,a_2,a_3;2,2;1).
\tag{4.5}
\]

The parametric excess in each series is `delta-1>0`, so all three converge absolutely. Since

\[
\Pi_n(1)=\frac{(a_1)_n(a_2)_n(a_3)_n}{(n!)^3},
\]

and `T^n(0)=n/(n+1)`, one obtains

\[
\boxed{G_{00}=F_0,}
\tag{4.6}
\]

\[
\boxed{G_{10}=F_0-F_1,}
\tag{4.7}
\]

\[
\boxed{G_{20}=F_0-2F_1+F_2.}
\tag{4.8}
\]

These identities are symmetric in the roots, hence independent of how the cubic roots are labelled.

## 5. Method B23 — use the signed kernel rather than demanding a Markov auxiliary process

The previous run stopped at the point where `B` is a genuine immigration pgf, which requires nonnegative cookies. That restriction is unnecessary.

Since for real `u>=1` each factor

\[
(1-\alpha_j)+\alpha_j\left(1-\frac1u\right)
=1-\frac{\alpha_j}{u}
\]

is nonnegative, every term in the zero-column series is nonnegative. In particular

\[
G_{00}\ge1.
\]

Define

\[
h_k=\frac{G_{k0}}{G_{00}},
\qquad
s_k^*=1-h_k.
\tag{5.1}
\]

Termwise, `0<=G_{k0}<=G_{00}`, so `0<=h_k<=1`. Also, for each `n>=1`,

\[
\left(\frac n{n+1}\right)^k\to0
\quad(k\to\infty),
\]

and the summable majorant `Pi_n(1)=O(n^{-delta})` gives

\[
\boxed{h_k\to0,\qquad s_k^*\to1.}
\tag{5.2}
\]

The full Green equation

\[
G_{kj}=\mathbf1_{\{k=j\}}+
\sum_{\ell\ge0}\widetilde Q(k,\ell)G_{\ell j}
\tag{5.3}
\]

holds because each signed row has finite total variation and the displayed Green columns are bounded. For `j=0` and `k>0`, (5.3) implies that `h` is `\widetilde Q`-harmonic. Since every signed row has total mass one,

\[
\boxed{(I-\widetilde K)s^*=0\quad\text{on positive states},}
\tag{5.4}
\]

with `s_0^*=0` and `s_k^*->1`.

Next define the Dirichlet Green columns, for `j=1,2`, by the exact Schur complement

\[
\boxed{
U_{kj}=G_{kj}-h_kG_{0j}.
}
\tag{5.5}
\]

Then `U_{0j}=0`, and subtracting `h_kG_{0j}` times the zero-column harmonic equation from (5.3) gives, for every `k>0`,

\[
\boxed{
(I-\widetilde K)U_{\cdot j}=e_j.
}
\tag{5.6}
\]

The columns `U_{\cdot1},U_{\cdot2}` are bounded and tend to zero at infinity. One direct proof uses the exact coefficient formula (3.2): for fixed `n`, every coefficient of degree at most 2 tends to zero as `k->infinity` because the factor `(n/(n+1))^k` dominates the polynomial derivative factors in `k`; uniformly in `k`, the first two derivative factors contribute at most constants times `1`, `k/[n(n+1)]`, and `k^2/[n^2(n+1)^2]`, whose suprema after multiplication by `(n/(n+1))^k` are bounded. The remaining factor is `O(n^{-delta})`, summable since `delta>1`. Dominated convergence therefore gives

\[
\boxed{U_{kj}\to0\quad(k\to\infty),\ j=1,2.}
\tag{5.7}
\]

No auxiliary probability interpretation was used anywhere in (5.3)–(5.7).

For the two boundary states needed below, set

\[
H_k=\Phi_k(1),
\qquad
D_k=\Phi_k'(1),
\qquad
E_k=\frac{\Phi_k''(1)+2\Phi_k'(1)}2,
\quad k=0,1,2.
\tag{5.8}
\]

Then explicitly

\[
h_k=H_k/H_0,
\qquad
s_k^*=1-H_k/H_0,
\tag{5.9}
\]

\[
\boxed{U_{k1}=D_k-(H_k/H_0)D_0,}
\tag{5.10}
\]

\[
\boxed{U_{k2}=E_k-(H_k/H_0)E_0.}
\tag{5.11}
\]

In particular, (4.6)–(4.8) give the simple closed forms

\[
\boxed{s_1^*=F_1/F_0,}
\tag{5.12}
\]

\[
\boxed{s_2^*=(2F_1-F_2)/F_0.}
\tag{5.13}
\]

## 6. Method B27 — swap the order of the infinite tail and finite boundary problem

The actual survival function satisfies

\[
(I-K)s=0,
\qquad s_0=0,
\qquad s_k\to1.
\tag{6.1}
\]

Since `K=\widetilde K-E`, (6.1) becomes

\[
(I-\widetilde K)s=-Es.
\tag{6.2}
\]

Write

\[
x=s(1),\qquad y=s(2).
\]

By (2.7),

\[
r_1:=(Es)_1=(A-D)x+Dy,
\qquad
r_2:=(Es)_2=Cx.
\tag{6.3}
\]

Equations (5.4) and (5.6) show that the unique candidate with the correct limit at infinity is

\[
\boxed{
s=s^*-U_{\cdot1}r_1-U_{\cdot2}r_2.}
\tag{6.4}
\]

Evaluating (6.4) at states 1 and 2 gives a finite `2 x 2` connection problem:

\[
\boxed{
\begin{pmatrix}
1+(A-D)U_{11}+CU_{12} & DU_{11}\\
(A-D)U_{21}+CU_{22} & 1+DU_{21}
\end{pmatrix}
\binom{x}{y}
=
\binom{s_1^*}{s_2^*}.
}
\tag{6.5}
\]

Denote the matrix in (6.5) by `M=(m_ij)` and its determinant by `Delta_M`.

### Lemma 6.1 (the connection matrix is always invertible)

Under the source-valid right-transient assumptions,

\[
\boxed{\Delta_M\ne0.}
\tag{6.6}
\]

### Proof

Suppose instead that the homogeneous version of (6.5) has a nonzero vector `(x,y)`. Form `r_1,r_2` from (6.3) and define

\[
w=-U_{\cdot1}r_1-U_{\cdot2}r_2.
\]

The homogeneous boundary equations say exactly that `w_1=x,w_2=y`. By (5.6),

\[
(I-\widetilde K)w=-r,
\]

while `Ew=r` because `E` depends only on the first two boundary values. Hence

\[
(I-K)w=(I-\widetilde K+E)w=0.
\]

Moreover `w_0=0` and, by (5.7), `w_k->0`.

Extend `w` by `w(0)=0` to the genuine forward Markov chain. For `N>k`, stop at

\[
\tau_N=\inf\{n:V_n=0\text{ or }V_n\ge N\}.
\]

The cumulative R7-05 survival theorem shows that on nonextinction `V_n->infinity`; therefore `tau_N<infinity` almost surely. Bounded optional stopping gives

\[
w(k)=\mathbb E_k[w(V_{\tau_N})].
\]

The contribution on hitting 0 is zero, and on `V_{tau_N}>=N` its absolute value is at most `sup_{m>=N}|w(m)|`, which tends to zero. Thus `w(k)=0` for every `k`. In particular `(x,y)=(0,0)`, a contradiction. QED.

By Cramer's rule, (6.5) therefore gives

\[
\boxed{
 x=\frac{s_1^*m_{22}-m_{12}s_2^*}{\Delta_M},
}
\tag{6.7}
\]

\[
\boxed{
 y=\frac{m_{11}s_2^*-m_{21}s_1^*}{\Delta_M}.
}
\tag{6.8}
\]

Finally combine (1.1) and (6.7):

\[
\boxed{
 p_{\rm esc}
 =\mathbb E[p_1]
 \frac{s_1^*m_{22}-m_{12}s_2^*}{\Delta_M}.
}
\tag{6.9}
\]

Every term in (6.9) is an explicit finite polynomial moment of the three-cookie law, an absolutely convergent generalized-hypergeometric value, or the first/second `u`-derivative at `u=1` of the absolutely convergent series (3.4). There is no implicit stationary distribution, infinite-dimensional linear solve, unknown hitting probability, or numerical limit hidden in the formula.

### Uniqueness identifies the candidate with the true survival function

For completeness, (6.4) is not merely a formal solution. It is bounded, has value zero at 0 and tends to one at infinity. Equation (6.2) plus the self-consistent boundary equations imply it is `K`-harmonic. The difference between it and the true survival function is a bounded `K`-harmonic function vanishing at 0 and at infinity, so the same `tau_N` optional-stopping argument used in Lemma 6.1 makes that difference identically zero. Thus (6.7) is exactly `s(1)`.

## 7. Left transience

If `delta<-1`, reflect space. The reflected cookie stack has right-step probabilities

\[
p_j^{\rm ref}=1-p_j,
\]

hence `alpha_j^{ref}=-alpha_j` and drift parameter `-delta>1`. Apply the entire right-transient construction above to the reflected three-cookie law. The never-return probability in the original walk is then

\[
\boxed{
 p_{\rm esc}^{\rm left}
 =\mathbb E[1-p_1]\,x_{\rm ref},
}
\tag{7.1}
\]

where `x_ref` is given by (6.7) with the reflected law. Therefore the exact depth-three formula covers both transient directions.

## 8. Why this moves the frozen metric

The frozen R7-05 quantity is

`M_closed` = largest finite cookie depth `M` for which an exact closed escape-probability formula is evidenced for **every** i.i.d. bounded stack law neutral after visit `M` in the transient regime.

Before this note the evidenced baseline was `M_closed=2`, from Zerner's source-cited two-cookie formula. Equations (1.2)–(7.1) give an exact, convergent special-function formula for every source-valid i.i.d. depth-three law, with arbitrary signs of the cookie drifts and with both directions handled by reflection. Consequently

\[
\boxed{M_{\rm closed}:2\longrightarrow3.}
\]

The five-run unchanged streak therefore resets rather than triggering the six-unchanged retirement rule.

This is **not** a claim that Kosygina–Zerner Problem 3.12 is solved. The source is broader than depth three. In particular, no corresponding closed formula is proved here for arbitrary finite `M`, and the stationary-ergodic branch of the survey's surrounding hypotheses is untouched. Mathematical status remains **PARTIAL**.

## 9. Prior-art boundary and novelty caution

The critical Galton–Watson-with-immigration interpretation and stopped-at-zero asymptotics are classical; Ivanoff–Seneta and later work treat critical GWI stopped at zero, and Kosygina–Zerner's excursion paper explicitly uses related branching processes and squared-Bessel asymptotics. The present proof therefore makes **no novelty claim for the broad GWI connection**.

The new R7-05 mechanism is narrower: use the exact linear-fractional semigroup outside the two exceptional boundary rows, allow the auxiliary low rows to be signed, compute their low-state Green resolvent by a hypergeometric series, and glue the true rows back through an invertible `2 x 2` boundary matrix. A bounded search on 2026-09-18 did not locate this exact depth-three formula or a general resolution of Problem 3.12. That search result is negative evidence only; worldwide novelty and openness remain **UNVERIFIED**.

## 10. Next mathematical attack

The natural next target is `M=4`. The same tail semigroup still has pgf `B(z)T(z)^k`, now with quartic `B`, but the true/auxiliary defect occupies rows 1,2,3. If the signed-resolvent mechanism survives, one expects a `3 x 3` connection matrix whose entries are the first three low-state Green coefficients of the same translated Möbius semigroup. The next run should not redo the present proof; it should test whether the following three genuinely new methods can advance `M_closed` again:

- **B3 (prove something stronger):** formulate and prove the arbitrary-depth signed finite-rank resolvent theorem before specializing the boundary coefficients;
- **B19 (make it an algorithm):** derive the exact `M-1` boundary matrix directly from cookie-row defect polynomials and hypergeometric Green derivatives;
- **B30 (one scale/direction at a time):** work out `M=4` completely and identify the first obstruction to invertibility or convergence if the general theorem fails.

No full-source closure, independent audit, or publication-novelty claim is made in this artifact.