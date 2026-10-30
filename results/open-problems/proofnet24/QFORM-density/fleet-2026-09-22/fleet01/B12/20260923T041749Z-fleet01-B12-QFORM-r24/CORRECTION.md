# Correction — principal-compression iteration from CHECKPOINT.md

Run: `20260923T041749Z-fleet01-B12-QFORM-r24`.

The early checkpoint contains a correct resolvent-trace lemma under its explicit premise that the four eigenvalues outside `[-t,t]` still have modulus at least one. Its subsequent suggested *iterative* compression algorithm is not justified, because that unit lower bound need not survive earlier physical deletions.

The exact obstruction is the balanced rank-four family

`A_c = c U diag(1,1,-1,-1) U^T`,

where `U` is the repeated normalized 4x4 Hadamard frame. Every row has leverage `4/n`. After deletion of any physical coordinate,

`spec_nonzero(A_c^{(i)}) = {c,-c,c sqrt(1-4/n),-c sqrt(1-4/n)}`.

Thus two large magnitudes can decrease simultaneously. Repeating deletions while continuing to use the original unit lower bound is invalid. The proposed end-to-end iterative reduction in the checkpoint is therefore WITHDRAWN.

The valid replacement is Theorem 2.1 of `REPORT.md`:

`s_{r-k}(A_JJ) >= L sqrt(1-rho_K)`

for an r-dimensional invariant `L`-large subspace and physical deletion set K, with `rho_K=||P_K|_E||op^2`. The Hadamard family attains the one-coordinate r=4 bound exactly.

This correction refutes only the overstrong proof interface. It does not refute QFORM. The same sharp obstruction is uniformly controlled by the designated fleet02/B12 collective-tail theorem, yielding

`||p||_infinity <= 9 e sqrt(3)/(2^(1/6)c) < 37.751/c`.
