# Sign-resolved Schur spectral counts

Run: `20260924T121016Z-account03-B11-fixedmult-audit-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Theorem

Let

\[
A=\begin{pmatrix}B&C\\ C^T&D\end{pmatrix}=A^T,
\qquad \det B\neq0,
\qquad S=D-C^TB^{-1}C,
\]

where `B` has order `k`. For `t>0`, write

\[
N_+(H,t)=\#\{j:\lambda_j(H)\ge t\},\qquad
N_-(H,t)=\#\{j:\lambda_j(H)\le -t\},
\]

and let `nu_+(B),nu_-(B)` denote the positive and negative inertia of `B`. Then, even when the ambient matrix `A` is singular,

\[
\boxed{N_+(S,t)\ge N_+(A,t)-\nu_+(B)},
\]

\[
\boxed{N_-(S,t)\ge N_-(A,t)-\nu_-(B)}.
\]

Adding the two inequalities gives the manuscript's unsigned count

\[
N_S(t)\ge N_A(t)-k.
\]

## Proof for invertible `A`

Block Gaussian elimination gives a congruence

\[
LAL^T=B\oplus S.
\]

Hence Sylvester inertia gives

\[
\nu_+(A)=\nu_+(B)+\nu_+(S),\qquad
\nu_-(A)=\nu_-(B)+\nu_-(S).
\]

Also the complementary principal block of `A^{-1}` is `S^{-1}`. By Cauchy interlacing for this principal compression,

\[
\#\{\lambda(S^{-1})>t^{-1}\}
\le
\#\{\lambda(A^{-1})>t^{-1}\}.
\]

For an invertible Hermitian matrix these two counts are respectively

\[
\nu_+(S)-N_+(S,t),\qquad
\nu_+(A)-N_+(A,t),
\]

because `lambda(H^{-1})>t^{-1}` is equivalent to `0<lambda(H)<t`. Thus

\[
\nu_+(S)-N_+(S,t)
\le
\nu_+(A)-N_+(A,t).
\]

Substitute `nu_+(S)=nu_+(A)-nu_+(B)` and rearrange to obtain

\[
N_+(S,t)\ge N_+(A,t)-\nu_+(B).
\]

The negative inequality follows identically from the negative tail of the principal-compression interlacing, or by applying the positive argument to `-A` and `-B`.

## Singular ambient `A`

Choose `epsilon_m ->0` so that `A_m=A+epsilon_m I` is invertible and, for all large `m`, `B_m=B+epsilon_m I` is invertible. The inertia of `B_m` equals the inertia of `B` for sufficiently small `epsilon_m`. Let

\[
S_m=D+\epsilon_m I-C^T(B+\epsilon_m I)^{-1}C.
\]

Then `S_m -> S` in operator norm.

For every eigenvalue `lambda(A)>=t`,

\[
lambda(A)+\epsilon_m\ge t-|\epsilon_m|,
\]

so

\[
N_+(A_m,t-|\epsilon_m|)\ge N_+(A,t).
\]

Apply the invertible theorem to `A_m` at threshold `t-|epsilon_m|`:

\[
N_+(S_m,t-|\epsilon_m|)
\ge N_+(A,t)-\nu_+(B).
\]

If the right side is positive, the corresponding ordered positive eigenvalue of `S_m` is at least `t-|epsilon_m|`; eigenvalue continuity under `S_m->S` gives the same ordered positive eigenvalue of `S` at least `t`. If the right side is nonpositive the assertion is trivial. This proves the positive inequality. The negative inequality is identical.

## Sharpness

The losses `nu_+(B)` and `nu_-(B)` are individually optimal. Take

\[
A=B\oplus S
\]

with all positive (respectively negative) eigenvalues of `B` and `S` having magnitude at least `t`. Then the relevant signed count of `S` is exactly the relevant signed count of `A` minus that of `B`. Optional zero blocks make the ambient matrix singular without changing equality.

## Consequence for the fixed-multiplicity proof

This refinement confirms that Schur spectral loss is not the source of the theorem's current threshold 17.

- A scalar pivot needs only ten large spectral directions to leave the nine directions used by `prop:nine`.
- A definite pair pivot needs no surviving spectral direction after its determinant lower bound.
- An indefinite pair pivot needs only one surviving Schur direction, hence three ambient large directions already suffice for that branch.
- The threshold 17 is forced by the no-pivot order-five crossing-volume branch and its present `4k-3` interpolation cost.

Therefore a genuine threshold reduction below 17 must improve the no-pivot mechanism rather than the Schur count.