SIGNED IN - auditing fixed-multiplicity quadratic-form bounded-density proof, account account04, slot B11, 2026-09-24T15:15:45Z.
attacking: Schur-complement spectral counts, including singular ambient matrices, and the exact interface to the nine-eigenvalue compiler.

# B11 handoff: Schur count audit and sharpness

## Source pins

- Active objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
- Baseline package: `math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Owner-recorded manuscript SHA256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69` (not independently recomputed in this connector-only run).
- Canonical login commit: `f5507a01d32e4126c7658fc68eb678195d55d53b`.

## Audit result

The manuscript Schur statement is valid for singular ambient matrices. If
[
A=egin{pmatrix}B&C\\ C^T&Dend{pmatrix},qquad det B
e0,qquad
S=D-C^TB^{-1}C,
]
and (B) has order (k), then for every (t>0),
[
N_S(t)ge N_A(t)-k,qquad s_j(S)ge s_{j+k}(A).
]
For invertible (A), use that (S^{-1}) is the complementary principal block of (A^{-1}), apply interlacing to both signs, and translate the strict inverse threshold (>1/t) into the complement of the original non-strict threshold (ge t). For singular (A), regularize (A+arepsilon I), use threshold (t-|arepsilon|), Weyl, and (S_arepsilon	o S).

## Exact sharpness family

For every pivot dimension (k=p+q) and every signature, let
[
J=operatorname{diag}(I_p,-I_q),quad
B=arepsilon J,quad C=sqrtarepsilon,I_k,quad D=J,quad 0<arepsilon<1.
]
Then (S=0), while after permutation (A) is a direct sum of (p) blocks with eigenvalues ({1+arepsilon,0}) and (q) blocks with eigenvalues ({-(1+arepsilon),0}). Hence (N_A(1)=k), (N_S(1)=0), and (|B|=arepsilon	o0). The loss (k) is therefore sharp even for singular ambient matrices and arbitrarily near-null indefinite pivots. No refund may be based on small pivot norm or on the number of large pivot eigenvalues.

## Compiler consequence

For the reviewed (s_9) compiler, the scalar-pivot and pair-pivot Schur branches use fewer than nine ambient large directions. The nine-direction threshold is imposed entirely by the no-pivot Fourier endpoint. Thus any (s_9	o s_8) improvement must repair the no-pivot endpoint; Schur bookkeeping cannot supply it.

Audit: https://github.com/yspennstate/math-open-problems/blob/f2eff4a23cd0335908dde0c5f376c0216c11888a/proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account04/B11/20260924T151545Z-account04-B11-fixedmult-schur-r1/AUDIT.md

Sharpness note: https://github.com/yspennstate/math-open-problems/blob/4a818c0cd169a3a52aac71de48e45ef338cd94fb/proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account04/B11/20260924T151545Z-account04-B11-fixedmult-schur-r1/SCHUR_SHARPNESS_FAMILY.md

Status: baseline fixed-multiplicity proof PASS under this lens. The nine-eigenvalue theorem is unaffected. The (s_8) endpoint and unrestricted three-eigenvalue conjecture remain open; continuity remains separate.
