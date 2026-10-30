# MOC4 fleet03/B07 r12 — standard-representation reduction and exact parity-slack gate

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira target  
**Worker:** fleet03/B07 (campaign lead)  
**Outcome:** `ESSENTIAL_STEP_APPLIED` — the exact mixed `(P,R)` support inequality is compressed to a 3-by-3 signed-permutation support problem with only six fibers, and a precise scalar parity-slack condition is isolated. A complete target-level proof is **not** obtained.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and peer results actually consumed

For complex normal 4-by-4 matrices `A,B`, with eigenvalues `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]

After diagonalizing `A`, write `B=U diag(b) U*`. This run directly consumes the following completed campaign results.

1. **fleet01/B07, `MOC4-MIXED-ASSIGNMENT-v1`**: for `P=(|u_ij|^2)` and the complementary-pair transport `R`, the full support inequality is exactly
   \[
   \langle P,C\rangle+\tfrac12\langle R,X\rangle
   \le
   \max_{\sigma\in S_4}\left\{\langle P_\sigma,C\rangle+\tfrac12\langle R_\sigma,X\rangle\right\}.\tag{MI}
   \]
   It also proves that the signed orientation block `D=(d_{\alpha\beta})` is the mean-zero Hadamard block of `P` and that `|d_{\alpha\beta}|\le r_{\alpha\beta}`.
2. **assigned partner fleet04/B08, `MOC4-GENERIC-STRICT-SUPPORT-v1`**: any genuine MOC4 counterexample can be perturbed to a simple-spectrum, irreducible, strict-compound, unique-support-vertex counterexample. Thus the remaining obstruction is genuinely interior.
3. **fleet04/B09, `MOC4-PR-JOINT-LIFT-v1 = REFUTED` plus structured-coefficient identities**: an unrestricted common convex lift of `(P,R)` to coupled permutation vertices is false; the proof must use the actual structured support coefficients. The same report gives a nondegenerate Bezout/Vandermonde structure for the complex coefficient gauge on the simple-spectrum locus.
4. **fleet02/B07, `MOC4-BIRAYLEIGH-ORBIT-v1`**: a hypothetical support-violating global maximizer satisfies twelve exact two-plane top-eigenvector conditions and the 24 column-label orbit has the same barycenter as the 24 target vertices. This strengthens the interior critical-point description but leaves the final support bound unpaid.

The goal here is to compress `(MI)` further without reintroducing the already-refuted unrestricted joint lift.

## 2. The standard-representation block of every doubly stochastic `P`

Let

\[
H=\frac12\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix}.
\]

`H` is real orthogonal. If `P` is doubly stochastic, then its row and column sums are one, hence

\[
HPH^T=\begin{pmatrix}1&0\\0&D\end{pmatrix},\tag{1}
\]

where `D` is exactly the 3-by-3 matrix from the fleet01/B07 mixed-minor difference identity,

\[
D_{\alpha\beta}=\frac14 h_\alpha^TPh_\beta=d_{\alpha\beta}.\tag{2}
\]

For any real 4-by-4 coefficient matrix `C`, set

\[
\widehat C=HCH^T=\begin{pmatrix}c_{00}&*\\ *&K\end{pmatrix},\tag{3}
\]

with `K` the lower-right 3-by-3 block. Frobenius invariance under `H` gives

\[
\boxed{\langle P,C\rangle=c_{00}+\langle D,K\rangle.}\tag{4}
\]

Thus, modulo the irrelevant doubly-stochastic row/column gauge, the entire `P` contribution to `(MI)` depends only on the nine entries of `D`, not on sixteen entries of `P`.

## 3. The 24 permutation vertices become tetrahedral signed permutations

For `\sigma\in S_4`, let `P_\sigma` be its 4-by-4 permutation matrix. Define

\[
HP_\sigma H^T=\begin{pmatrix}1&0\\0&S_\sigma\end{pmatrix}.\tag{5}
\]

Because `S_4` permutes the three complementary pair classes

\[
\{12,34\},\qquad \{13,24\},\qquad \{14,23\},
\]

each `S_\sigma` is a 3-by-3 signed permutation matrix. If `\rho_\sigma\in S_3` is the induced permutation of those three pair classes, then

\[
\boxed{|S_\sigma|=R_{\rho_\sigma}}\tag{6}
\]

entrywise, where the right side is the corresponding ordinary 3-by-3 permutation matrix. The kernel of `S_4\to S_3` is the Klein four group. For each fixed `\rho`, the four matrices in its fiber have the same nonzero positions and their three nonzero signs run through exactly

\[
(+,+,+),\quad (+,-,-),\quad(-,+,-),\quad(-,-,+).\tag{7}
\]

Equivalently, the product of the three nonzero signs is always `+1`.

A standard-library exact verifier included with this report enumerates all 24 permutations and checks (5)–(7) with integer/Fraction arithmetic.

## 4. Exact six-fiber form of the full MOC4 support inequality

Combining (4)–(6), the fleet01/B07 mixed assignment inequality `(MI)` is exactly equivalent to

\[
\boxed{
\langle D,K\rangle+\frac12\langle R,X\rangle
\le
\max_{\sigma\in S_4}
\left\{\langle S_\sigma,K\rangle+\frac12\langle |S_\sigma|,X\rangle\right\}.
}\tag{SR}
\]

No relaxation has been made. In particular, the false global `(P,R)` joint lift is not assumed.

Now fix `\rho\in S_3`. Let

\[
x_i=K_{i,\rho(i)},\qquad i=1,2,3.
\]

The four signed matrices in that fiber optimize precisely the even-parity sign functional

\[
\phi(x_1,x_2,x_3)
:=\max_{\epsilon_1\epsilon_2\epsilon_3=1}
\sum_{i=1}^3\epsilon_ix_i.\tag{8}
\]

Hence, defining

\[
F_\rho(K):=\phi\bigl(K_{1,\rho(1)},K_{2,\rho(2)},K_{3,\rho(3)}\bigr),\tag{9}
\]

we obtain the six-state identity

\[
\boxed{
\text{RHS(SR)}
=\max_{\rho\in S_3}\left\{F_\rho(K)+\frac12\sum_iX_{i,\rho(i)}\right\}.
}\tag{10}
\]

The fiber cost has the closed form

\[
\boxed{
\phi(x)=
\begin{cases}
|x_1|+|x_2|+|x_3|,&x_1x_2x_3\ge0,\\
|x_1|+|x_2|+|x_3|-2\min_i|x_i|,&x_1x_2x_3<0.
\end{cases}}
\tag{11}
\]

So the only difference between an unrestricted absolute-value assignment and the exact `S_4` support is an explicit **odd-transversal parity penalty**.

## 5. A scalar convex-roof sufficient condition

Every 3-by-3 doubly stochastic `R` has a Birkhoff decomposition

\[
R=\sum_{\rho\in S_3}\lambda_\rho R_\rho,
\qquad \lambda_\rho\ge0,\quad \sum_\rho\lambda_\rho=1.\tag{12}
\]

Define the scalar convex roof

\[
\Psi_K(R)
:=\min_{\lambda:\,(12)}\sum_\rho\lambda_\rho F_\rho(K).\tag{13}
\]

### Proposition 1 — parity-roof gate

If

\[
\boxed{\langle D,K\rangle\le\Psi_K(R),}\tag{14}
\]

then the full mixed assignment inequality `(MI)` holds for this `(D,R,K,X)`, for **every** real `X`.

### Proof

Choose a minimizing Birkhoff decomposition in (13). Then

\[
\frac12\langle R,X\rangle
=\sum_\rho\lambda_\rho\frac12\langle R_\rho,X\rangle.
\]

By (14),

\[
\langle D,K\rangle+\frac12\langle R,X\rangle
\le
\sum_\rho\lambda_\rho\left(F_\rho(K)+\frac12\langle R_\rho,X\rangle\right)
\]

and the right side is a convex combination of the six quantities in (10), hence at most their maximum. This is `(SR)` and therefore `(MI)`. ∎

This does **not** assert the false joint lift. It asks only for one scalar support comparison for the structured `K` relevant to the chosen spectra/support direction.

## 6. Exact parity-slack form using the genuine unitary inequality `|D|<=R`

For every actual unitary, fleet01/B07 gives

\[
|D_{ij}|\le R_{ij}.\tag{15}
\]

Therefore, for every real `K`,

\[
\langle D,K\rangle\le\langle R,|K|\rangle.\tag{16}
\]

For a Birkhoff decomposition (12),

\[
\langle R,|K|\rangle
=\sum_\rho\lambda_\rho\sum_i|K_{i,\rho(i)}|.\tag{17}
\]

By (11), define

\[
m_\rho(K)=
\begin{cases}
0,&\prod_iK_{i,\rho(i)}\ge0,\\
\min_i|K_{i,\rho(i)}|,&\prod_iK_{i,\rho(i)}<0.
\end{cases}\tag{18}
\]

Then

\[
\sum_\rho\lambda_\rho F_\rho(K)
=\langle R,|K|\rangle-2\sum_\rho\lambda_\rho m_\rho(K).\tag{19}
\]

Consequently (14) is guaranteed whenever one can choose a Birkhoff decomposition of `R` satisfying

\[
\boxed{
2\sum_\rho\lambda_\rho m_\rho(K)
\le
\sum_{ij}\bigl(R_{ij}|K_{ij}|-D_{ij}K_{ij}\bigr).
}\tag{PS}
\]

The right side is a genuine nonnegative **unitary orientation slack**. The left side is the exact weighted odd-transversal penalty. This is the first remaining quantitative implication in this route.

The fleet04/B09 arbitrary `(P,R)` separator shows that a statement like `(PS)` cannot hold for every arbitrary real `K`; the structured spectral origin of `K` is essential. On the generic strict-support locus of fleet04/B08, `|D_{ij}|<R_{ij}` entrywise, so the right side is strictly positive whenever the corresponding `K_ij` is nonzero. The remaining task is to show that the structured Bezout/Vandermonde coefficient family prevents the odd-transversal penalty from outrunning this slack.

## 7. Immediate proved subclass: nonnegative transversal products

### Corollary 2

If the structured 3-by-3 coefficient block `K` satisfies

\[
\prod_{i=1}^3K_{i,\rho(i)}\ge0
\qquad\text{for every }\rho\in S_3,\tag{20}
\]

then `(MI)` holds for the actual unitary `U` and for the given spectra/support direction.

### Proof

Condition (20) makes every `m_\rho(K)=0`. Thus `(PS)` is automatic from (15), and Proposition 1 gives `(MI)`. ∎

This is not claimed to cover every support direction. It is a clean target-valid subclass derived from the actual common-unitary variables, not from a bistochastic surrogate.

## 8. Compact conditional end-to-end argument after this run

The smallest surviving chain is now:

1. By fleet04/B08, any MOC4 failure can be taken on the simple-spectrum, irreducible, strict-compound, unique-support-vertex locus.
2. By fleet01/B07, every such failure is exactly a violation of `(MI)` for the actual unitary-generated `(P,R)` and structured `(C,X)`.
3. By sections 2–4 above, `(MI)` is exactly the six-fiber signed-standard inequality `(SR)` with coefficient block `K`.
4. By Proposition 1, it suffices to prove the scalar parity-roof inequality (14), equivalently the explicit slack payment `(PS)`, for the **structured** `K` arising from the spectra/support direction.
5. fleet04/B09 gives exact algebraic structure for that coefficient family on the simple-spectrum locus, including a nonzero Vandermonde determinant for the complex reduced gauge. The next step is to push that structure through the real support block `K` and prove `(PS)`, or construct a genuine true-unitary/spectrum counterexample to `(PS)` and then return to the weaker exact inequality `(SR)`.

Thus the first essential missing implication is now:

> **`MOC4-PARITY-SLACK-v1`.** For every generic strict-support MOC4 datum `(a,b,U,eta)`, with `D,R` the exact unitary blocks and `K` the mean-zero Hadamard block of the exact real support coefficient matrix, there exists a Birkhoff decomposition `R=sum lambda_rho R_rho` satisfying `(PS)`.

This statement is deliberately stronger than the exact target `(SR)` but far weaker than the already-refuted common `(P,R)` lift: it preserves only one scalar structured support cost. Proving it closes MOC4 through the chain above. Refuting it would be useful because `(SR)` remains the exact fallback and the witness would identify precisely which support directions require the `X` term to rescue the inequality.

## 9. What failed / what is not claimed

- No unrestricted common permutation lift is resurrected.
- No arbitrary doubly-stochastic `(D,R)` statement is asserted.
- The sign-transversal subclass in Corollary 2 is not presented as the generic case.
- A failure of `(PS)` would not disprove MOC4, because `(PS)` is sufficient, not necessary for the exact `X`-dependent inequality `(SR)`.
- Full MOC4 remains open.

## 10. Next recipients

Recommended immediate recipients: fleet04/B08 (assigned partner, to test the generic strict-support coefficient signs against `(PS)`), fleet04/B09 (to combine the Bezout/Vandermonde coefficient formula with the parity-roof), fleet01/B07 (to integrate the six-fiber form into the mixed-minor route), fleet02/B07 (to compare bi-Rayleigh criticality against the parity-slack witness), and fleet03/B20 (team integrator).

No benchmark gold, held-out answers, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid model/API calls, Codex, or remote workflows were used.
