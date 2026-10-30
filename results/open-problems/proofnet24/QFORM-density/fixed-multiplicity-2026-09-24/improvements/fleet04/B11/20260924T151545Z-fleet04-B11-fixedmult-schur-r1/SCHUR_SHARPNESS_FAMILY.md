# Uniform sharpness of Schur spectral loss

Run: `20260924T151545Z-fleet04-B11-fixedmult-schur-r1`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `manuscript.tex` blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, owner-recorded SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Proposition

Fix integers (p,q\ge0), (k=p+q\ge1), and (0<\varepsilon<1). Put
[
J=\operatorname{diag}(I_p,-I_q),\qquad
B=\varepsilon J,\qquad C=\sqrt\varepsilon I_k,\qquad D=J
]
and
[
A_\varepsilon=
\begin{pmatrix}B&C\\ C^T&D\end{pmatrix}.
]
Then:

1. (B) is invertible and (|B|=\varepsilon), so the pivot may be arbitrarily small.
2. Its Schur complement is identically zero:
[
S=D-C^TB^{-1}C
=J-(\sqrt\varepsilon I_k)(\varepsilon^{-1}J)(\sqrt\varepsilon I_k)=0.
]
3. After simultaneously permuting coordinates, (A_\varepsilon) is the direct sum of (p) blocks
[
\begin{pmatrix}\varepsilon&\sqrt\varepsilon\\
\sqrt\varepsilon&1\end{pmatrix}
]
and (q) blocks
[
\begin{pmatrix}-\varepsilon&\sqrt\varepsilon\\
\sqrt\varepsilon&-1\end{pmatrix}.
]
The first block has eigenvalues (1+\varepsilon,0); the second has eigenvalues (-(1+\varepsilon),0). Hence
[
\operatorname{spec}(A_\varepsilon)
={1+\varepsilon}^{p}\cup{-(1+\varepsilon)}^{q}\cup{0}^{k}.
]
At threshold (t=1),
[
N_+(A_\varepsilon,1)=p,quad
N_-(A_\varepsilon,1)=q,quad
N_S(1)=0,
]
while (N_B(1)=0).

Thus the sign-resolved Schur bounds
[
N_+(S,t)\ge N_+(A,t)-\nu_+(B),\qquad
N_-(S,t)\ge N_-(A,t)-\nu_-(B)
]
and their unsigned sum
[
N_S(t)\ge N_A(t)-k
]
are simultaneously sharp for every pivot dimension and every pivot signature, even when the ambient matrix is singular and the pivot norm tends to zero.

## Consequence for fixed-multiplicity descent

No universal improvement may replace the loss (k) by:

- the number of threshold-large eigenvalues of (B);
- a quantity tending to zero with (|B|);
- loss one for a near-null indefinite pair; or
- a smaller signature-blind rank charge.

Therefore the current threshold descent cannot be improved merely by sharper Schur counting. For the reviewed nine-eigenvalue theorem, scalar and pair pivot branches are already cheaper than the no-pivot branch; the remaining (9\to8) obstruction is the no-pivot Fourier endpoint, not spectral bookkeeping across a pivot.

This family uses only exact algebra; no numerical experiment or probabilistic assumption enters.
