Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum; authenticated runtime reasoning-effort telemetry and a binding model/effort selector are not exposed.

# C0130 — all finite cookie depths: exact signed-resolvent formula for the entire `(IID)+(BD)+(WEL)` branch

Target: `C0130`, Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, Problem 3.12.

This note strengthens the same-run depth-three result. It proves an exact finite-dimensional special-function formula for the never-return probability for **every one-dimensional source-valid environment satisfying `(IID)+(BD)+(WEL)`**. Equivalently, it handles every deterministic finite cookie-depth bound `M` in the source's branch (3.10). The source also has the distinct `(SE)+(POS_1)` branch (3.9), which is not treated here, so the full outside Problem 3.12 remains **PARTIAL**.

For the frozen R7-05 metric

`M_closed` = largest finite cookie depth for which every i.i.d. bounded law neutral after that depth has an exact closed escape formula,

there is now **no finite upper depth**: every finite `M` is covered. I record this as

\[
\boxed{M_{\rm closed}:2\longrightarrow\infty\quad\text{(all finite depths).}}
\]

Here `infinity` means “unbounded over finite `M`”, not that infinite non-placebo stacks are covered.

## 1. Source scope and forward survival reduction

Fix a deterministic source bound `M>=1`. At each site let the cookie stack be an i.i.d. copy of

\[
(p_1,\ldots,p_M,1/2,1/2,\ldots),
\qquad 0\le p_i\le1,
\]

with the source's weak ellipticity assumption. Put

\[
\alpha_i=2p_i-1,
\qquad
\delta=\mathbb E\sum_{i=1}^M\alpha_i.
\]

First take the right-transient case `delta>1`. For a fresh site let `S_k` be the number of successes before the `k`-th failure, `S_0=0`, and let

\[
V_{n+1}=S_{n+1,V_n}
\]

be the standard forward branching-like chain. State 0 is absorbing. Write

\[
s(k)=\mathbb P_k(V_n>0\text{ for every }n\ge0).
\]

The cumulative R7-05 Siegmund-duality theorem identifies the stationary law `pi` of the backward branching chain by

\[
\pi_i=s(i+1)-s(i),
\]

hence `pi_0=s(1)`. The cumulative first-step identity then gives

\[
\boxed{p_{\rm esc}=\mathbb E[p_1]\,s(1).}
\tag{1.1}
\]

Thus the problem is reduced to an exact formula for the first value of the forward survival harmonic function.

## 2. The universal high-state linear-fractional kernel

Put

\[
T(z)=\frac1{2-z}
\]

and define the degree-`M` polynomial

\[
\boxed{
B(z)=\mathbb E\prod_{i=1}^M\big((1-\alpha_i)+\alpha_i z\big).
}
\tag{2.1}
\]

Then

\[
B(1)=1,
\qquad B'(1)=\delta.
\tag{2.2}
\]

For every `k>=M`, all first `M` cookies have necessarily been exposed before the `k`-th failure. Conditional on the site stack, if `R` of those `M` tosses are successes, then `M-R` failures have occurred and `k-M+R` additional fair failures are needed. Therefore

\[
\mathbb E[z^{S_k}\mid(p_1,\ldots,p_M)]
=z^R T(z)^{k-M+R}
\]

after averaging over the first `M` tosses. Using

\[
T(z)^{-1}(1-p+pzT(z))=(1-\alpha)+\alpha z,
\]

one gets the exact tail-row identity

\[
\boxed{
P_k(z):=\mathbb E[z^{S_k}]=B(z)T(z)^k,
\qquad k\ge M.
}
\tag{2.3}
\]

Define the **signed auxiliary full kernel** by declaring this tail formula at every state:

\[
\boxed{
\widetilde Q_k(z)=B(z)T(z)^k,
\qquad k\ge0.
}
\tag{2.4}
\]

If some cookies have negative drift, the low rows of `\widetilde Q` may be signed. This is harmless: every row is a finite signed convolution of the polynomial `B` with the probability law having pgf `T^k`, hence has finite total variation, and every row has total mass one.

## 3. The true/auxiliary discrepancy is finite in both rows and columns

The key general fact is that for `k<M`, the difference between the true row and the auxiliary row is a **polynomial of degree at most `M-k`**. This is what makes the eventual correction finite-dimensional.

Fix a deterministic stack temporarily and write `q_i=1-p_i`. For `r in {1,...,M+1}` and `k>=0`, let

\[
P_{r,k}(z)
\]

be the true pgf of the number of successes before the `k`-th failure when one starts at cookie `r`, with cookies `r,...,M` followed by fair coins. Use the convention

\[
P_{r,0}(z)=1.
\]

Let `N=M-r+1` be the number of non-placebo cookie positions remaining and define the algebraic auxiliary function

\[
Q_{r,k}(z)
=T(z)^{k-N}\prod_{i=r}^M(q_i+p_i zT(z)).
\tag{3.1}
\]

At `r=M+1`, `N=0` and

\[
P_{M+1,k}=Q_{M+1,k}=T^k.
\]

For `k>=1`, both families satisfy the same one-cookie recursion

\[
X_{r,k}=q_rX_{r+1,k-1}+p_rzX_{r+1,k}.
\tag{3.2}
\]

At `k=0`, however,

\[
P_{r,0}=1,
\]

whereas the auxiliary recursion would continue through the remaining cookies. By the elementary one-cookie identity above,

\[
Q_{r,0}(z)=
\prod_{i=r}^M\big((1-\alpha_i)+\alpha_i z\big),
\tag{3.3}
\]

a polynomial of degree at most `N`.

Set

\[
D_{r,k}=P_{r,k}-Q_{r,k}.
\]

### Lemma 3.1 (finite defect support)

For every `r` with `N=M-r+1`:

- `D_{r,k}=0` for every `k>=N`;
- for `0<=k<N`, `D_{r,k}` is a polynomial of degree at most `N-k`.

### Proof

Induct on `N`. For `N=0`, true and auxiliary processes are both fair and the assertion is immediate. For `N>=1`, the `k=0` assertion follows from (3.3). For `k>=1`, subtract (3.2):

\[
D_{r,k}=q_rD_{r+1,k-1}+p_rzD_{r+1,k}.
\]

If `k>=N`, both terms vanish by the induction hypothesis. If `1<=k<N`, the first term has degree at most

\[
(N-1)-(k-1)=N-k,
\]

while the second has degree at most

\[
1+(N-1-k)=N-k.
\]

QED.

Taking `r=1` and annealing over the i.i.d. stack law proves:

\[
\boxed{
P_k(z)-\widetilde Q_k(z)
\text{ is a polynomial of degree at most }M-k,
\quad1\le k<M,
}
\tag{3.4}
\]

and it is zero for `k>=M`.

Let `K` and `\widetilde K` be the restrictions of the true and auxiliary kernels to positive states. Define

\[
R:=\widetilde K-K.
\]

By (3.4), `R` has nonzero entries only in the finite boundary block

\[
\mathcal B=\{1,2,\ldots,M-1\},
\]

and, more sharply,

\[
R_{kj}=0\quad\text{unless }1\le k<M,\ 1\le j\le M-k.
\tag{3.5}
\]

All entries of the finite matrix `R_B=(R_{kj})_{k,j in B}` are explicit finite polynomial expectations obtained from the recursion above. No infinite-state quantity enters them.

## 4. Method B14 generalized — translation conjugacy gives the exact auxiliary semigroup

The signed auxiliary kernel has the branching/immigration composition law

\[
\boxed{
\sum_{j\ge0}\widetilde Q^{\,n}(k,j)z^j
=T^n(z)^k\prod_{\ell=0}^{n-1}B(T^\ell(z)).
}
\tag{4.1}
\]

for every `n,k>=0`. This follows by induction exactly as in the depth-three note and uses no positivity.

Conjugate the Möbius map `T` to translation by

\[
u=\frac1{1-z}.
\]

Then

\[
T^n(z)=1-\frac1{u+n}.
\tag{4.2}
\]

Define

\[
\Pi_n(u)=\prod_{\ell=0}^{n-1}B\!\left(1-\frac1{u+\ell}\right),
\qquad \Pi_0=1,
\tag{4.3}
\]

and

\[
\boxed{
\Phi_k(u)=\sum_{n=0}^{\infty}
\left(\frac{u+n-1}{u+n}\right)^k\Pi_n(u).
}
\tag{4.4}
\]

The polynomial

\[
\mathcal C(u)=u^M B\!\left(1-\frac1u\right)
\]

is monic of degree `M`. Let its roots be `rho_1,...,rho_M`, with multiplicity. Since `B'(1)=delta`,

\[
\boxed{
\sum_{a=1}^M\rho_a=\delta.
}
\tag{4.5}
\]

Moreover

\[
\boxed{
\Pi_n(u)=
\frac{\prod_{a=1}^M(u-\rho_a)_n}{(u)_n^M}.
}
\tag{4.6}
\]

Hence

\[
\boxed{
\Phi_0(u)=
{}_{M+1}F_M\!\left(
\begin{matrix}
 u-\rho_1,\ldots,u-\rho_M,1\\
 u,\ldots,u
\end{matrix};1\right).
}
\tag{4.7}
\]

The generalized-hypergeometric parametric excess is

\[
Mu-\left(Mu-\delta+1\right)=\delta-1>0.
\]

More importantly for coefficient extraction, the gamma-ratio form of (4.6) gives, uniformly for `u` in a compact neighborhood of 1 and for every fixed derivative order `r`,

\[
\boxed{
\partial_u^r\Pi_n(u)=O_r(n^{-\delta}).
}
\tag{4.8}
\]

The exponent `-delta` is independent of `u`; differentiating does not produce a growing `log n` factor. Formula (4.8) also covers terminating numerator Pochhammer cases by the analytic reciprocal-gamma continuation. Therefore, because `delta>1`, (4.4) may be differentiated termwise any fixed number of times near `u=1`.

## 5. Exact finite low-state Green block

For `j=0,...,M-1`, define

\[
G_{kj}=\sum_{n=0}^{\infty}\widetilde Q^{\,n}(k,j).
\tag{5.1}
\]

The series converges absolutely for every fixed `k` and every `j<M`. Indeed, by (4.1), the coefficient of `z^j` is a fixed-order derivative of the expression in (4.4), and (4.8) gives an `O(n^{-delta})` bound.

Equivalently,

\[
\boxed{
G_{kj}
=[z^j]\left[
\sum_{n=0}^{\infty}
T^n(z)^k\prod_{\ell=0}^{n-1}B(T^\ell(z))
\right].
}
\tag{5.2}
\]

Under `u=1/(1-z)`, every coefficient `G_{kj}` with `j<M` is a universal finite linear combination of

\[
\Phi_k(1),\Phi_k'(1),\ldots,\Phi_k^{(j)}(1).
\tag{5.3}
\]

Thus the required `M x M` low-state Green block is an explicit finite collection of convergent generalized-hypergeometric values and derivatives. There is no stochastic limit hidden in (5.2).

The zero column is particularly transparent:

\[
G_{k0}
=\sum_{n=0}^{\infty}
\left(\frac n{n+1}\right)^k
\frac{\prod_{a=1}^M(1-\rho_a)_n}{(n!)^M}.
\tag{5.4}
\]

Because for real `u>=1`

\[
B\!\left(1-\frac1u\right)
=
\mathbb E\prod_{i=1}^M\left(1-\frac{\alpha_i}{u}\right)\ge0,
\]

all terms of (5.4) are nonnegative. In particular `G_{00}>=1`.

Define

\[
h_k=G_{k0}/G_{00},
\qquad
s_k^*=1-h_k.
\tag{5.5}
\]

Then `0<=h_k<=1`, and dominated convergence in (5.4) yields

\[
\boxed{h_k\to0,\qquad s_k^*\to1.}
\tag{5.6}
\]

## 6. The signed Dirichlet resolvent

The Green equation for the signed full kernel is

\[
G_{kj}=\mathbf1_{\{k=j\}}+
\sum_{\ell\ge0}\widetilde Q(k,\ell)G_{\ell j}.
\tag{6.1}
\]

The sums are legitimate because each signed row has finite total variation and each fixed low-state Green column is bounded.

For the zero column and `k>0`, (6.1) makes `h` `\widetilde Q`-harmonic. Since each row sums to one,

\[
\boxed{(I-\widetilde K)s^*=0\quad\text{on positive states}.}
\tag{6.2}
\]

For every boundary column `j in B`, define the exact Dirichlet Green column

\[
\boxed{
U_{kj}=G_{kj}-h_kG_{0j}.
}
\tag{6.3}
\]

Then `U_{0j}=0`, and subtracting the zero-column harmonic equation from (6.1) gives

\[
\boxed{
(I-\widetilde K)U_{\cdot j}=e_j,
\qquad j\in\mathcal B.
}
\tag{6.4}
\]

For every fixed `j<M`, the column `U_{\cdot j}` is bounded and tends to zero as `k->infinity`. To see this directly from (4.1), fix `n`. Any derivative of order `j` of `T^n(z)^k` at zero is a polynomial of degree at most `j` in `k`, multiplied by `(n/(n+1))^k` and powers of `1/[n(n+1)]`. The supremum in `k` of each such product is bounded by a constant depending only on `j`. The remaining `n`-factor is `O(n^{-delta})`, summable. For fixed `n`, the coefficient tends to zero as `k->infinity`, so dominated convergence gives

\[
\boxed{U_{kj}\to0\quad(k\to\infty).}
\tag{6.5}
\]

This is the point at which allowing a signed auxiliary process matters: none of (6.1)–(6.5) requires `\widetilde Q` itself to be a Markov kernel.

## 7. Method B27 generalized — the infinite problem becomes an `(M-1) x (M-1)` matrix inversion

Let

\[
x=(s(1),\ldots,s(M-1))^\mathsf T,
\]

and let

\[
s^*_{\mathcal B}=(s_1^*,\ldots,s_{M-1}^*)^\mathsf T.
\]

Let `U_B` denote the boundary block

\[
(U_{kj})_{k,j\in\mathcal B}
\]

and `R_B` the finite true/auxiliary defect matrix from Section 3.

Because

\[
K=\widetilde K-R,
\]

the true harmonic equation `(I-K)s=0` is

\[
(I-\widetilde K)s=-Rs.
\tag{7.1}
\]

Since `R` acts only on the boundary coordinates, `Rs=R_Bx`. Equations (6.2) and (6.4) therefore suggest

\[
\boxed{
s=s^*-UR_Bx.}
\tag{7.2}
\]

Restricting (7.2) to the boundary gives the finite linear system

\[
\boxed{
\left(I_{M-1}+U_BR_B\right)x=s^*_{\mathcal B}.
}
\tag{7.3}
\]

### Theorem 7.1 (universal invertibility)

For every source-valid right-transient i.i.d. bounded cookie law,

\[
\boxed{
I_{M-1}+U_BR_B\text{ is invertible}.}
\tag{7.4}
\]

### Proof

Assume a nonzero boundary vector `x` solves the homogeneous system. Put

\[
r=R_Bx
\]

and

\[
w=-Ur.
\]

The homogeneous boundary equations imply that the boundary values of `w` are exactly `x`. By (6.4),

\[
(I-\widetilde K)w=-r.
\]

Because `R` only reads the boundary values, `Rw=r`; hence

\[
(I-K)w=(I-\widetilde K+R)w=0.
\]

Moreover `w(0)=0`, `w` is bounded, and (6.5) gives `w(k)->0`.

For the genuine forward chain `V`, define

\[
\tau_N=\inf\{n:V_n=0\text{ or }V_n\ge N\}.
\]

The cumulative R7-05 duality/survival theorem proves that on nonextinction `V_n->infinity`, so `tau_N<infinity` almost surely. Bounded optional stopping yields

\[
w(k)=\mathbb E_k[w(V_{\tau_N})].
\]

On absorption at zero the terminal value is zero; on the other event its absolute value is at most `sup_{m>=N}|w(m)|`, which tends to zero. Therefore `w(k)=0` for every `k`, so its boundary vector `x` is zero, contradiction. QED.

It follows that

\[
\boxed{
x=\left(I_{M-1}+U_BR_B\right)^{-1}s^*_{\mathcal B}.}
\tag{7.5}
\]

The same optional-stopping uniqueness argument shows that the function (7.2) with the vector (7.5) is exactly the true survival function: it is bounded, `K`-harmonic, zero at state 0, and tends to one at infinity.

Combining the first coordinate of (7.5) with (1.1) gives the promised exact formula:

\[
\boxed{
 p_{\rm esc}
 =\mathbb E[p_1]\,
 e_1^\mathsf T
 \left(I_{M-1}+U_BR_B\right)^{-1}
 s^*_{\mathcal B}.
}
\tag{7.6}
\]

Every object in (7.6) is explicit from the one-site cookie-stack law:

1. `B` is the finite polynomial expectation (2.1);
2. `R_B` is obtained by the finite recursion (3.1)–(3.4);
3. `G`, hence `h`, `s^*` and `U_B`, are finite low-degree coefficients of the absolutely convergent hypergeometric series (4.4), equivalently finite derivatives at `u=1`;
4. the only linear algebra is the inversion of an `(M-1) x (M-1)` matrix, proved nonsingular above.

There is no unknown stationary distribution, no infinite-dimensional linear solve and no uncontrolled numerical limiting procedure.

## 8. Left transience and the complete `(IID)+(BD)+(WEL)` branch

If `delta<-1`, reflect space. Replace every stack by

\[
(1-p_1,\ldots,1-p_M,1/2,1/2,\ldots).
\]

The reflected drift is `-delta>1`, so (7.6) applies. If `x_ref` denotes the first component of the reflected vector (7.5), then

\[
\boxed{p_{\rm esc}^{\rm left}=\mathbb E[1-p_1]\,x_{\rm ref}.}
\tag{8.1}
\]

Under `(IID)+(BD)+(WEL)`, the source Theorem 3.10 says the walk is transient precisely when `|delta|>1` (aside from its separately noted degenerate edge case). Because `(BD)` supplies some finite deterministic depth bound `M`, formulas (7.6) and (8.1) therefore compute the never-return probability throughout the **entire transient branch (3.10)**.

## 9. What is and is not closed

### Closed here

- every finite deterministic cookie-depth bound `M` in the source's i.i.d. bounded model;
- arbitrary signs of the cookie drifts;
- arbitrary dependence among cookies within one site stack;
- both right and left transient directions;
- the exact scalar `P_0[forall n>=1: X_n !=0]` through a finite matrix of convergent special-function values.

Thus the frozen metric is no longer a finite integer:

\[
\boxed{M_{\rm closed}=\infty\text{ in the sense “all finite }M\text{”.}}
\]

### Not closed here

Problem 3.12 is stated after Theorem 3.10, which also has the different branch

`(SE)+(POS_1)`.

That branch allows spatial dependence and need not have a deterministic finite bound on the number of non-placebo cookies. The one-site i.i.d. branching semigroup used above does not cover it. Therefore the **full source problem remains PARTIAL**, not PROVED.

This note also does not establish publication novelty. The branching-process connection itself is classical and is explicitly emphasized by Kosygina–Zerner. The potentially new ingredient is the signed finite-rank hypergeometric resolvent and its use to obtain an explicit formula for every finite-depth i.i.d. law. A bounded literature search dated 2026-09-18 did not locate this formula or a later complete resolution of Problem 3.12. That is negative evidence only.

## 10. Immediate next attack

Because the entire finite-depth i.i.d. metric is now saturated, the next mathematical question should not be another `M=4` calculation. The next nonrepeating triple should attack the **remaining source branch** instead:

- **B3:** prove a stronger theorem that replaces i.i.d. sites by a finite-state stationary Markov environment and identify the transfer-operator analogue of `B(z)`;
- **B19:** formulate an exact matrix-product algorithm for a periodic or finite-state ergodic stack process, looking for a computable Lyapunov/transfer resolvent;
- **B30:** isolate the simplest genuinely non-i.i.d. `(SE)+(POS_1)` example and determine exactly where the one-site semigroup factorization fails.

No full-source closure, protocol audit, or novelty certification is claimed.