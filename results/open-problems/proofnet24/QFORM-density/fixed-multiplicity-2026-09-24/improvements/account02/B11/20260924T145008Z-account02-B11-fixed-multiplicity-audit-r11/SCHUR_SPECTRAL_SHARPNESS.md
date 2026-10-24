# QFORM-SCHUR-RANK-PROOF-AND-SHARPNESS-v1

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Worker: account02/B11  
Pinned baseline manuscript: commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Theorem 1 — rank-only Schur spectral count

Let
\[
A=\begin{pmatrix}B&C\\C^T&D\end{pmatrix}=A^T,
\qquad B\in\mathbb R^{k\times k},\quad \det B\ne0,
\qquad S=D-C^TB^{-1}C.
\]
Then for every `t>0`,
\[
N_S(t)\ge N_A(t)-k.
\]
No invertibility assumption on the ambient matrix `A` is needed.

### Proof

Set
\[
U=\begin{pmatrix}I_k\\C^TB^{-1}\end{pmatrix}.
\]
Direct multiplication gives
\[
A=UBU^T+\operatorname{diag}(0_k,S).
\]
The first summand has rank at most `k`. The singular-value rank perturbation inequality therefore gives
\[
s_{j+k}(A)\le s_j(S),\qquad 1\le j\le n-k.
\]
Counting values at least `t` proves the claim. This is valid when `A` and/or `S` are singular. QED.

This is a shorter replacement proof for manuscript lines 183--207. It is not needed to repair the theorem—the manuscript's moving-threshold perturbation argument is already valid—but it removes all inverse-compression and endpoint-limit bookkeeping.

## Theorem 2 — the loss `k` is sharp for arbitrarily small invertible pivots, every signature

Fix any signs `sigma_i in {+1,-1}` and put `J=diag(sigma_1,...,sigma_k)`. For every `0<epsilon<1`, let
\[
B_\epsilon=\epsilon J,\qquad C_\epsilon=\sqrt\epsilon I_k,
\qquad D=J,
\]
\[
A_\epsilon=\begin{pmatrix}B_\epsilon&C_\epsilon\\C_\epsilon&D\end{pmatrix}.
\]
Then
\[
S_\epsilon=D-C_\epsilon^TB_\epsilon^{-1}C_\epsilon=0,
\]
and, after a permutation into `k` two-dimensional blocks,
\[
\operatorname{spec}(A_\epsilon)=
\{\sigma_i(1+\epsilon):1\le i\le k\}\cup\{0\}^k.
\]
Thus at `t=1`,
\[
N_A(1)=k,\qquad N_S(1)=0,\qquad N_{B_\epsilon}(1)=0.
\]
So the loss `k` cannot be reduced by the smallness of the pivot, the number of threshold-large eigenvalues inside the pivot, near-singularity, or pivot signature. For `k=2` and `J=diag(1,-1)`, one positive and one negative large direction are both consumed by an arbitrarily tiny indefinite pair.

## Theorem 3 — naive Moore--Penrose singular-pivot extension is false

For
\[
A=\begin{pmatrix}0&I_k\\I_k&0\end{pmatrix},
\qquad B=0_k,\quad C=I_k,\quad D=0_k,
\]
the pseudoinverse expression gives `S_dagger=D-C^TB^dagger C=0`, but `A` has `k` eigenvalues `+1` and `k` eigenvalues `-1`. Hence
\[
N_A(1)=2k,\qquad N_{S_\dagger}(1)=0,
\]
so even a loss-`k` statement is false. The manuscript's `det B !=0` hypothesis is essential.

## Theorem 4 — compatible singular pivots admit a correct extension

If `B=B^T` may be singular but `range(C) subset range(B)`, set `X=B^dagger C` and
\[
S_\dagger=D-C^TB^\dagger C.
\]
Then `BX=C` and
\[
A=
\begin{pmatrix}I\\X^T\end{pmatrix}B\begin{pmatrix}I&X\end{pmatrix}
+\operatorname{diag}(0,S_\dagger).
\]
The first term has rank at most `rank B<=k`, hence the same singular-value argument gives
\[
N_{S_\dagger}(t)\ge N_A(t)-k.
\]
The range condition cannot be omitted by Theorem 3.

## Fixed-multiplicity consequence

Schur complementation is not the route to improve the complete nine-eigenvalue theorem to eight. The scalar/pair spectral charges one/two are already sharp in the strongest near-singular sense above. The current multiplicity-eight debt lies in the no-pivot overlap-one/shared-anchor analytic receiver, not in Schur bookkeeping. No eight-eigenvalue theorem and no unrestricted three-eigenvalue theorem is claimed here.
