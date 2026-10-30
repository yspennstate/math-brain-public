# MOC4 fleet01/B07 r1 — exact mixed-minor identity and parity-free support reduction

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira target  
**Worker:** fleet01/B07  
**Outcome:** `ESSENTIAL_STEP_APPLIED` — the orientation/parity variable in the middle exterior-power layer is shown to be an exact linear image of the one-minor matrix, so the full support problem reduces to one explicit mixed `(P,R)` assignment inequality. The unrestricted MOC4 target remains open.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Effective scope and peer inputs

The current owner control supersedes this slot's older benchmark assignment and assigns B07 to MOC4. The source-exact target is: for all complex normal 4-by-4 matrices `A,B`, with spectra `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]

I consumed three exact completed campaign artifacts:

1. **fleet04/B09, `MOC4-U-LIFT-v1`**: an exact rational orthogonal counterexample shows that one spectrum-independent probability law on `S_4` cannot in general reproduce all one- and two-subset squared-minor marginals. This refutes a stronger coefficientwise lift, not MOC4.
2. **fleet03/B09, `MOC4-C2-COMPLEMENT-BOUND-v1`**: the `k=2` layer is compressed into a 3-by-3 complementary-pair transport `R` and a signed orientation matrix `D`; its support estimate leaves an explicit orientation-parity defect plus a joint-assignment problem.
3. **assigned partner fleet02/B08, `MOC4-DOUBLE-EIGENVALUE-LIFT-v1`**: MOC4 is proved on the repeated-eigenvalue boundary (and on the common-reducing-block boundary) by an exact permutation lift. The report identifies the remaining simple-spectrum problem as controlling the orientation/parity term or paying it from the `k=1,3` layer.

The result below sharpens item 2 in exactly that direction: `D` is not an independent middle-layer variable. It is determined *exactly* by the one-minor matrix `P=|U|^2`, and its entire support contribution can be absorbed into the `k=1,3` assignment cost without any absolute-value or parity relaxation.

No claim of worldwide novelty is made; this is a campaign proof reduction.

## 2. Exact exterior-power expansion

After diagonalizing `A`, write

\[
A=\operatorname{diag}(a_1,a_2,a_3,a_4),\qquad
B=U\operatorname{diag}(b_1,b_2,b_3,b_4)U^*,
\]

with `U` unitary. For equal-cardinality subsets `S,T` define

\[
q_{S,T}=|\det U[S,T]|^2,
\qquad a_S=\prod_{i\in S}a_i,
\qquad b_T=\prod_{j\in T}b_j.
\]

Principal-minor expansion and Cauchy–Binet give

\[
D_U(a,b):=\det(A+B)
=\sum_{S\subseteq[4]}a_{S^c}\sum_{|T|=|S|}b_Tq_{S,T}.
\tag{1}
\]

For `k=1`, put `p_{ij}=|u_{ij}|^2`. For `k=3`, Jacobi complementarity for a 4-by-4 unitary gives the same coefficients `p_{ij}`. Hence

\[
L_1+L_3
=\sum_{i,j=1}^4p_{ij}\left(a_{i^c}b_j+a_i b_{j^c}\right).
\tag{2}
\]

The endpoint layers are

\[
L_0=a_1a_2a_3a_4,\qquad L_4=b_1b_2b_3b_4.
\tag{3}
\]

Thus all genuinely new unitary information is in the `k=2` layer.

## 3. Complement-pair coordinates for the middle layer

Use the three oriented complementary row pairs

\[
S_1=12,\qquad S_2=13,\qquad S_3=14
\]

and the same oriented column pairs

\[
T_1=12,\qquad T_2=13,\qquad T_3=14.
\]

For `alpha,beta in {1,2,3}` set

\[
r_{\alpha\beta}
=q_{S_\alpha,T_\beta}+q_{S_\alpha,T_\beta^c},
\qquad
 d_{\alpha\beta}
=q_{S_\alpha,T_\beta}-q_{S_\alpha,T_\beta^c}.
\tag{4}
\]

Also define

\[
A_\alpha^+=a_{S_\alpha^c}+a_{S_\alpha},\qquad
A_\alpha^-=a_{S_\alpha^c}-a_{S_\alpha},
\]

\[
B_\beta^+=b_{T_\beta}+b_{T_\beta^c},\qquad
B_\beta^-=b_{T_\beta}-b_{T_\beta^c}.
\tag{5}
\]

Pairing complementary row and column entries, as in the fleet03/B09 reduction, gives the exact identity

\[
L_2
=\frac12\sum_{\alpha,\beta=1}^3
\left(
 r_{\alpha\beta}A_\alpha^+B_\beta^+
+d_{\alpha\beta}A_\alpha^-B_\beta^-
\right).
\tag{6}
\]

`R=(r_{alpha beta})` is doubly stochastic because the second compound `C_2(U)` is unitary.

## 4. New exact identity: the orientation matrix is determined by `P`

### Lemma 1 — mixed-minor difference identity

For every two-row set `S` and two-column set `T`,

\[
\boxed{
q_{S,T}-q_{S,T^c}
=
\sum_{i\in S}\sum_{j\in T}|u_{ij}|^2-1.}
\tag{7}
\]

### Proof

Let

\[
M=U[S,T],\qquad N=U[S,T^c].
\]

The two selected rows of `U` are orthonormal, so

\[
MM^*+NN^*=I_2.
\tag{8}
\]

Put

\[
z=\operatorname{tr}(MM^*)
=\sum_{i\in S,j\in T}|u_{ij}|^2,
\qquad q=\det(MM^*)=q_{S,T}.
\]

Since `NN*=I-MM*`,

\[
q_{S,T^c}=\det(NN^*)
=\det(I_2-MM^*)
=1-z+q.
\]

Subtracting yields (7). ∎

This is stronger than the previous generic bound `|d_{alpha beta}|<=r_{alpha beta}`: the signed orientation data are fixed once `P=(p_ij)` is fixed.

### Hadamard form

Let

\[
h_1=(1,1,-1,-1),\quad
h_2=(1,-1,1,-1),\quad
h_3=(1,-1,-1,1).
\tag{9}
\]

`S_alpha` is the `+1` support of `h_alpha`. Because `P` is doubly stochastic, (7) is equivalently

\[
\boxed{
 d_{\alpha\beta}
=\frac14 h_\alpha^T P h_\beta.}
\tag{10}
\]

If `H` is the normalized 4-by-4 Hadamard matrix whose rows are

\[
\frac12(1,1,1,1),\quad \frac12h_1,\quad\frac12h_2,\quad\frac12h_3,
\]

then

\[
HPH^T=
\begin{pmatrix}
1&0\\
0&D
\end{pmatrix},
\qquad D=(d_{\alpha\beta}).
\tag{11}
\]

Thus the orientation matrix is literally the mean-zero Hadamard block of the one-point transport.

## 5. New quantitative constraints on `R` from the same 2-by-2 block

Let the eigenvalues of `MM*` in the proof above be `lambda_1,lambda_2 in [0,1]`. Then

\[
z=\lambda_1+\lambda_2,\qquad q=\lambda_1\lambda_2,\qquad d=z-1,
\]

and

\[
r=q_{S,T}+q_{S,T^c}=2q-d.
\]

Since `q>=0` and `q_{S,T^c}>=0`, while AM-GM gives `q<=z^2/4`, we obtain the exact interval

\[
\boxed{
|d_{\alpha\beta}|
\le r_{\alpha\beta}
\le \frac{1+d_{\alpha\beta}^2}{2}.}
\tag{12}
\]

The upper bound is a genuine common-unitary restriction; it is not true for an arbitrary pair consisting only of a doubly stochastic `R` and a dominated signed matrix `D`.

There is also a rowwise Plücker constraint. For fixed `S_alpha`, write

\[
m_{\beta,+}=\det U[S_\alpha,T_\beta],\qquad
m_{\beta,-}=\det U[S_\alpha,T_\beta^c].
\]

The 2-plane Plücker relation is

\[
m_{1,+}m_{1,-}-m_{2,+}m_{2,-}+m_{3,+}m_{3,-}=0.
\tag{13}
\]

Hence the three nonnegative numbers

\[
g_{\alpha\beta}
:=2|m_{\beta,+}m_{\beta,-}|
=\sqrt{r_{\alpha\beta}^2-d_{\alpha\beta}^2}
\tag{14}
\]

are side lengths of a possibly degenerate triangle. Therefore, for each row `alpha`,

\[
 g_{\alpha 1}\le g_{\alpha2}+g_{\alpha3}
\quad\text{and cyclically},
\tag{15}
\]

or equivalently

\[
2\sum_{\beta<\gamma}
(r_{\alpha\beta}^2-d_{\alpha\beta}^2)
(r_{\alpha\gamma}^2-d_{\alpha\gamma}^2)
\ge
\sum_\beta(r_{\alpha\beta}^2-d_{\alpha\beta}^2)^2.
\tag{16}
\]

The analogous three column inequalities follow by applying the same argument to `U^*`. These constraints are available to any next attempt at the remaining joint assignment inequality.

## 6. Parity-free exact support reduction

Fix a support direction `eta` with `|eta|=1`. Define real coefficient arrays

\[
W_{ij}=\Re\!\left[\eta\left(a_{i^c}b_j+a_i b_{j^c}\right)\right],
\tag{17}
\]

\[
X_{\alpha\beta}
=\Re\!\left(\eta A_\alpha^+B_\beta^+\right),
\qquad
Y_{\alpha\beta}
=\Re\!\left(\eta A_\alpha^-B_\beta^-\right).
\tag{18}
\]

By (10), the entire signed middle-layer term is linear in `P`:

\[
\frac12\sum_{\alpha,\beta}d_{\alpha\beta}Y_{\alpha\beta}
=
\sum_{i,j}p_{ij}Z_{ij},
\tag{19}
\]

where

\[
Z_{ij}
=\frac18\sum_{\alpha,\beta=1}^3
h_\alpha(i)h_\beta(j)Y_{\alpha\beta}.
\tag{20}
\]

Set

\[
C_{ij}=W_{ij}+Z_{ij},
\qquad
C_0=\Re\!\left[\eta(a_1a_2a_3a_4+b_1b_2b_3b_4)\right].
\tag{21}
\]

Combining (2), (3), (6), and (19) gives the exact formula

\[
\boxed{
\Re(\eta D_U(a,b))
=C_0+\langle P,C\rangle
+\frac12\langle R,X\rangle.}
\tag{22}
\]

No absolute value has been taken and no orientation parity has been relaxed.

For `sigma in S_4`, let `rho_sigma in S_3` be its induced permutation of the three complementary pair classes. The same algebra applied to the permutation matrix `P_sigma` and its pair-class matrix `R_sigma` yields

\[
\boxed{
\Re\!\left(\eta\prod_i(a_i+b_{\sigma(i)})\right)
=C_0+\sum_i C_{i,\sigma(i)}
+\frac12\sum_{\alpha=1}^3X_{\alpha,\rho_\sigma(\alpha)}.}
\tag{23}
\]

Therefore the full MOC4 support inequality is **exactly equivalent**, for the actual unitary-generated pair `(P,R)`, to the single mixed assignment inequality

\[
\boxed{
\langle P,C\rangle+\frac12\langle R,X\rangle
\le
\max_{\sigma\in S_4}
\left\{
\sum_i C_{i,\sigma(i)}
+\frac12\sum_{\alpha=1}^3X_{\alpha,\rho_\sigma(\alpha)}
\right\}.}
\tag{MI}
\]

This is the specific remaining mixed-minor inequality requested by the B07 assignment.

### What was removed

The fleet03/B09 bound treated `D` only through `|D|<=R`, then optimized the three orientation signs independently and paid an explicit odd-parity defect. Equations (10) and (19) show that this loss is avoidable: the signed orientation term is already part of the **same one-point transport `P`** that controls `L_1+L_3`. Thus orientation parity is not a separate residual. The only remaining finite-dimensional coupling problem is between the one-point transport `P` and the complement-pair transport `R`, for the structured coefficient pair `(C,X)` arising from the spectra and support direction.

## 7. Relation to the two no-go results and to the partner boundary theorem

`(MI)` does **not** assume that `(P,R)` is a convex combination of the joint permutation pairs `(P_sigma,R_sigma)`. That stronger assertion would reintroduce a common permutation lift and is already ruled out by the fleet04/B09 obstruction. It also does not require the final convex weights to preserve `P`; fleet01/B09 shows that even spectrum-dependent `P`-preserving weights can fail for a support functional while the determinant still lies in the full hull.

Instead, `(MI)` asks only for the structured support directions generated by `(a,b,eta)`. This is precisely the weaker statement that remains logically available after both no-go results.

The assigned partner fleet02/B08 proves the repeated-eigenvalue boundary by an actual lift. In the present coordinates that theorem says `(MI)` is valid on every spectral face with a repeated `a_i` or `b_j`, even though a general joint `(P,R)` lift need not exist. Consequently the next simple-spectrum attack can now be formulated as a deformation/stability problem for `(MI)`, using the exact constraints (10), (12), and (15) rather than an independent parity penalty.

## 8. Exact verification on the shared rational orthogonal example

The companion verifier uses the exact rational orthogonal matrix from fleet04/B09 and real spectra

\[
a=(1,2,3,7),\qquad b=(5,2,2,3),\qquad \eta=1.
\]

It checks using only `fractions.Fraction`:

- exact orthogonality;
- (7) and (10) for all nine complement blocks;
- both inequalities in (12);
- the Plücker relation (13) in every oriented row plane;
- the determinant identity (22);
- formula (23) for all 24 permutations.

Observed output:

```text
PASS
direct_det = 18646794/15625
mixed_reduction = 18646794/15625
max_permutation_product = 1350
example_support_gap = 2446956/15625
```

This finite example is a consistency check, not evidence that `(MI)` is proved universally.

## 9. Status and next obligation

**ESSENTIAL_STEP_APPLIED.** The previous orientation/parity residual is eliminated exactly, and the full MOC4 support problem is reduced to `(MI)` with additional unitary constraints (10), (12), and (15)/(16).

The remaining universal obligation is now sharply stated:

> **MOC4-MIXED-ASSIGNMENT-v1.** For every `U in U(4)`, every complex spectra `a,b`, and every support direction `eta`, the actual unitary-derived matrices `P=|U|^2` and `R` defined in (4) satisfy `(MI)` for the structured coefficient arrays `(C,X)` in (17)–(21).

A productive next recipient should either prove this structured mixed assignment inequality using the quadratic/Plücker restrictions above, or construct a genuine unitary/spectrum/support counterexample to `(MI)`. A counterexample to a stronger unrestricted `(P,R)` polytope statement would not refute MOC4.

No benchmark gold, held-out answers, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid model/API calls, or remote workflows were used.
