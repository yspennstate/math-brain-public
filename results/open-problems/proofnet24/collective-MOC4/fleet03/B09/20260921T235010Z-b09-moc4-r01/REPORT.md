# MOC4 fleet03/B09 r01 — complementary-pair reduction of the 2-by-2-minor layer

**Campaign:** MOC4 (Marcus–de Oliveira, complex normal 4-by-4 pairs)  
**Worker:** fleet03/B09  
**Outcome:** `AUXILIARY_ONLY` — a rigorous support-function reduction for the middle exterior-power layer; the full MOC4 implication is still open.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## Source-exact target and later-control redirect

The effective owner control is `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, revision `2026-09-22.1`. It supersedes the older benchmark prompt for B09 and assigns this worker to MOC4. The target is: for all complex normal 4-by-4 matrices with spectra `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in \operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]

This run's exact assignment is to exploit the complementary 2-by-2 minors special to dimension four and apply the resulting inequality to the determinant support function. The current source-status record cites Drury's weakened n=4 result, Bebiano–da Providência (2025), and the 2026 variational obstruction; no novelty claim is made here.

I consumed the completed cross-account snapshot `fleet04/B09`, candidate `MOC4-U-LIFT-v1`. It gives an exact rational orthogonal counterexample to the stronger idea that all one- and two-subset squared-minor marginals of a fixed unitary admit one spectrum-independent probability law on `S_4`. That result does **not** refute MOC4; it says a successful proof must use a weaker, spectrum/support-dependent comparison. I did not find a completed current MOC4 artifact from the assigned partner `fleet04/B07` before this derivation, so I did not wait for it.

## 1. Exact determinant layer expansion

After unitary diagonalization write

\[
A=\operatorname{diag}(a_1,a_2,a_3,a_4),\qquad
B=U\operatorname{diag}(b_1,b_2,b_3,b_4)U^*.
\]

For `S,T subset [4]` with `|S|=|T|`, set

\[
q_{S,T}=|\det U[S,T]|^2,
\qquad a_S=\prod_{i\in S}a_i,\quad b_T=\prod_{j\in T}b_j.
\]

Cauchy–Binet gives

\[
D_U(a,b):=\det(A+B)
 =\sum_{k=0}^4 L_k,
\qquad
L_k=\sum_{|S|=|T|=k}a_{S^c}b_Tq_{S,T}.
\tag{1}
\]

The 2-by-2 layer is

\[
L_2=\sum_{|S|=|T|=2}a_{S^c}b_Tq_{S,T}.
\tag{2}
\]

## 2. Dimension-four complement blocks

Use the three complementary pairs

\[
\alpha_1=\{12,34\},\qquad
\alpha_2=\{13,24\},\qquad
\alpha_3=\{14,23\},
\]

and orient them by `S_1=12,S_2=13,S_3=14`; use the same orientation `T_1,T_2,T_3` on the column side. Jacobi's complementary-minor identity for a 4-by-4 unitary implies

\[
q_{S,T}=q_{S^c,T^c}\qquad (|S|=|T|=2).
\tag{3}
\]

Define

\[
r_{\alpha\beta}=q_{S_\alpha,T_\beta}+q_{S_\alpha,T_\beta^c},\qquad
 d_{\alpha\beta}=q_{S_\alpha,T_\beta}-q_{S_\alpha,T_\beta^c}.
\tag{4}
\]

Because the second compound `C_2(U)` is unitary, `Q=(q_{S,T})` is doubly stochastic. Therefore

\[
R=(r_{\alpha\beta})_{1\leq\alpha,\beta\leq3}
\quad\text{is doubly stochastic},
\qquad |d_{\alpha\beta}|\le r_{\alpha\beta}.
\tag{5}
\]

For each oriented complement pair set

\[
A_\alpha^+=a_{S_\alpha^c}+a_{S_\alpha},\qquad
A_\alpha^-=a_{S_\alpha^c}-a_{S_\alpha},
\]

\[
B_\beta^+=b_{T_\beta}+b_{T_\beta^c},\qquad
B_\beta^-=b_{T_\beta}-b_{T_\beta^c}.
\tag{6}
\]

Pairing the four ordered entries in each complement block gives the exact identity

\[
\boxed{
L_2(U)=\frac12\sum_{\alpha,\beta=1}^3
\Big(r_{\alpha\beta}A_\alpha^+B_\beta^+
+d_{\alpha\beta}A_\alpha^-B_\beta^-\Big).}
\tag{7}
\]

This is the first useful compression: the 36 squared 2-by-2 minors enter the middle determinant layer only through a 3-by-3 doubly stochastic transport `R` and a signed orientation matrix `D` dominated entrywise by `R`.

## 3. Support inequality and the parity defect

Fix a support direction `eta` with `|eta|=1`, and write

\[
x_{\alpha\beta}=\Re\big(\eta A_\alpha^+B_\beta^+\big),\qquad
 y_{\alpha\beta}=\Re\big(\eta A_\alpha^-B_\beta^-\big).
\tag{8}
\]

From (5) and (7),

\[
\Re(\eta L_2(U))
\le \frac12\sum_{\alpha,\beta}r_{\alpha\beta}
\big(x_{\alpha\beta}+|y_{\alpha\beta}|\big).
\tag{9}
\]

Birkhoff's theorem for the 3-by-3 doubly stochastic matrix `R` now yields

\[
\boxed{
\Re(\eta L_2(U))
\le
\max_{\rho\in S_3}\frac12\sum_{\alpha=1}^3
\left(x_{\alpha,\rho(\alpha)}+|y_{\alpha,\rho(\alpha)}|\right).}
\tag{10}
\]

The right side is close to, but not automatically equal to, the best middle-layer value coming from an actual permutation in `S_4`. To make the difference exact, note that every `sigma in S_4` induces a permutation `rho_sigma in S_3` of the three complementary pair classes and signs `epsilon_alpha in {+1,-1}` telling whether `sigma(S_alpha)` equals the selected representative of `rho_sigma(alpha)` or its complement. For each fixed `rho`, exactly four lifts occur, and their sign triples are precisely the four even-parity triples

\[
(+++),(+--),(-+-),(--+).
\tag{11}
\]

Thus for fixed `rho`, if

\[
y_\alpha:=y_{\alpha,\rho(\alpha)},
\]

then the best actual `S_4` middle-layer support above `rho` is

\[
H_\rho^{\rm perm}
=\frac12\sum_\alpha x_{\alpha,\rho(\alpha)}
+\frac12\max_{\epsilon_1\epsilon_2\epsilon_3=1}
\sum_\alpha\epsilon_\alpha y_\alpha.
\tag{12}
\]

The last finite maximization is explicit:

\[
\max_{\epsilon_1\epsilon_2\epsilon_3=1}\sum\epsilon_\alpha y_\alpha
=
\begin{cases}
\sum |y_\alpha|,& y_1y_2y_3\ge0,\\
\sum |y_\alpha|-2\min_\alpha|y_\alpha|,& y_1y_2y_3<0.
\end{cases}
\tag{13}
\]

Define the parity defect

\[
\delta_\rho(\eta;a,b)=
\begin{cases}
0,&\prod_\alpha y_{\alpha,\rho(\alpha)}\ge0,\\
\min_\alpha|y_{\alpha,\rho(\alpha)}|,&\prod_\alpha y_{\alpha,\rho(\alpha)}<0.
\end{cases}
\tag{14}
\]

Combining (10)-(14) gives the support bound

\[
\boxed{
\Re(\eta L_2(U))
\le \max_{\rho\in S_3}
\left(H_\rho^{\rm perm}+\delta_\rho(\eta;a,b)\right).}
\tag{15}
\]

In particular,

\[
\Re(\eta L_2(U))
\le \max_{\sigma\in S_4}\Re(\eta L_2(\sigma))
+\Delta_2(\eta;a,b),
\qquad
\Delta_2:=\max_{\rho\in S_3}\delta_\rho.
\tag{16}
\]

This is a genuine dimension-four reduction: the obstruction left by the entire 2-by-2 compound layer is compressed to an explicit three-coordinate parity penalty depending only on the spectra and support direction, not on `U`.

### Zero-defect cases

Equation (15) has no parity loss whenever the relevant three `y` values have nonnegative product. In particular, for real spectra and real support direction, the sign of

\[
\prod_{\alpha=1}^3
(A_\alpha^-B_{\rho(\alpha)}^-)
=\left(\prod_\alpha A_\alpha^-\right)
\left(\prod_\beta B_\beta^-\right)
\tag{17}
\]

is independent of `rho`. Hence if the product in (17) is nonnegative, then `Delta_2=0` and the middle layer alone satisfies the exact `S_4` permutation support bound. The same holds if any complementary-pair difference on either spectral side vanishes.

## 4. Application to the full determinant support expression

The dimension-four Jacobi identity also couples layers 1 and 3. Put `p_ij=|u_ij|^2`. Then

\[
L_1+L_3
=\sum_{i,j=1}^4p_{ij}
\left(a_{i^c}b_j+a_i b_{j^c}\right),
\tag{18}
\]

where `a_{i^c}` is the product of the three `a`'s other than `a_i`, and similarly for `b_{j^c}`. Since `P=(p_ij)` is doubly stochastic, for every support direction

\[
\Re\big(\eta(L_1+L_3)\big)
\le
\max_{\pi\in S_4}\sum_i
\Re\left(\eta(a_{i^c}b_{\pi(i)}+a_i b_{\pi(i)^c})\right).
\tag{19}
\]

The endpoint layers are fixed:

\[
L_0=a_1a_2a_3a_4,\qquad L_4=b_1b_2b_3b_4.
\tag{20}
\]

Therefore the full support inequality has now been reduced to a **joint coupling problem between two finite permutation optimizations**: the one-point/three-point assignment in (19), and the pair-partition assignment plus parity defect in (15). The missing MOC4 step is not a 36-minor inequality anymore. It is to prove that the common-unitary constraints prevent the maxima in (19) and (15) from combining more favorably than one actual `sigma in S_4`, or otherwise pay the explicit `delta_rho` parity term from the slack in layers 1 and 3.

Equivalently, define for each `sigma`

\[
H_\sigma(\eta)=\Re\left(\eta\prod_i(a_i+b_{\sigma(i)})\right).
\]

The target is `Re(eta D_U)<=max_sigma H_sigma`. Equations (15) and (19) isolate two exact residual issues:

1. **assignment coupling:** the Birkhoff optimizer for `P` need not be the same lift as the optimizer for the three pair classes;
2. **orientation parity:** the relaxed signs in (10) may have odd parity, costing exactly `delta_rho` relative to an actual `S_4` lift.

This interfaces directly with the fleet04/B09 no-go: its counterexample says one cannot generally eliminate both residuals by demanding a single spectrum-independent permutation law reproducing `P` and `Q`. The present reduction instead keeps only the scalar support information actually needed by MOC4.

## 5. Exact check on the cross-account rational orthogonal matrix

I reused only the public mathematical matrix from the fleet04/B09 handoff,

\[
U=\begin{pmatrix}
492/625&-31/625&-48/125&12/25\\
-9/25&12/25&-4/5&0\\
-36/125&48/125&9/25&4/5\\
-256/625&-492/625&-36/125&9/25
\end{pmatrix}.
\]

With real spectra

\[
a=(1,2,3,7),\qquad b=(5,2,2,3),\qquad \eta=1,
\]

the exact Fraction verifier obtains

\[
L_2(U)=\frac{193455501}{390625}\approx495.2461,
\]

while the best actual permutation middle layer is `583`. The sharper right side of (15) is `587`; the coarse form (16) gives `583+11=594`. Thus the new inequality holds nontrivially on the same unitary that destroys the universal marginal-lift strategy, and it does so without inventing a forbidden common permutation law.

For the same example, the exact layer identity reconstructs

\[
\det(A+UBU^T)=\frac{18646794}{15625},
\]

from `L_0+L_4`, `L_1+L_3`, and `L_2` exactly.

## 6. Status and next mathematical obligation

**Outcome:** `AUXILIARY_ONLY`, but it removes a large amount of irrelevant coefficient-level freedom from the first missing support inequality. The middle layer is now a 3-by-3 transport plus one explicit parity defect, and the 1+3 layer is an ordinary 4-by-4 transport. The next useful step is to derive a **joint scalar coupling inequality** between `P` and `(R,D)` for the fixed support coefficients, strong enough to absorb `delta_rho` and force one common permutation lift at the level of the objective only. This is strictly weaker than the refuted universal-marginal lift and is therefore still viable.

No full proof, counterexample to MOC4, or novelty claim is made.
