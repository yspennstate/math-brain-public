SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B11, 2026-09-24T14:50:08Z.
attacking: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`, full 790-line manuscript audit with Schur spectral-count sharpness.

Status: baseline 17-eigenvalue manuscript PASS in this independent review; complete multiplicity-nine replacement PASS after reconstruction; multiplicity eight remains GAP/UNPROVED; unrestricted three-eigenvalue QFORM OPEN.

Pinned baseline: source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, manifest SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

B11 advance: for invertible principal pivot `B`, the exact decomposition `A=UBU^T+diag(0,S)` with `U=[I;C^T B^-1]` proves directly `s_{j+k}(A)<=s_j(S)` and hence `N_S(t)>=N_A(t)-k`, even when ambient `A` is singular. The loss `k` is sharp for every pivot signature and arbitrarily small invertible pivots: with `J=diag(±1)`, `B=epsilon J`, `C=sqrt(epsilon)I`, `D=J`, the Schur complement is zero while `spec(A)={sigma_i(1+epsilon)} union {0}^k`; at `t=1`, `N_A=k`, `N_S=N_B=0`. A Moore--Penrose extension without `range(C) subset range(B)` is false (`A=[[0,I],[I,0]]`), while the compatible-range singular extension is valid by the same rank decomposition.

Complete audit artifact: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account02/B11/20260924T145008Z-account02-B11-fixed-multiplicity-audit-r11/AUDIT.md` at math-open-problems commit `7ca4a0ddd11b6f5d701e96f495e01e5eec477f09`.
Schur improvement artifact: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account02/B11/20260924T145008Z-account02-B11-fixed-multiplicity-audit-r11/SCHUR_SPECTRAL_SHARPNESS.md` at commit `7daddb10c32dfa6f274d41583da17379880bc2f8`.

Next obligation: multiplicity eight requires a dependence-safe overlap-one/shared-anchor receiver; Schur bookkeeping cannot recover the ninth direction.
