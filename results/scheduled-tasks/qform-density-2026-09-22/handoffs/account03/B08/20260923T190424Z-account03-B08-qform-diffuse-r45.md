SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T19:04:24Z.
attacking: the r44 nonzero common-plane edge/tail by exact physical-hub Schur completion: prove the tail cannot cancel a full-rank common-plane mismatch, and pay the exact zero-hub-curvature endpoint without moment assumptions.

# r45 handoff — tail-immune Schur mismatch + zero-hub arbitrary-edge payment

Full immutable mathematics: `yspennstate/math-open-problems@a3624cdb18747a63e9e6991d83233c30e1664f4b`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T190424Z-account03-B08-qform-diffuse-r45/REPORT.md`.

Control refresh: current owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`, OWNER CONTROL revision `2026-09-22.15`, QFORM only; full theorem open. Live corrections reread after proof. Execution remains `WITHOUT_VERIFIED_BRAIN`.

Incoming r43 common-plane state: two physical hub coordinates, disjoint banks `J1,J2`, full-row-rank arms `M_r` with `S_r=s1(M_r)s2(M_r)>L^2/(64 sqrt(896))`, and

`C=A[J1,J2]=M1^T R M2+T`, `P1 T P2=0`.

## New exact E2 identity

For an invertible physical hub block `B=A[H,H]`, exact two-hub Schur completion gives

`C_B=C-M1^T B^{-1}M2=M1^T(R-B^{-1})M2+T`.

If `U_r` are orthonormal frames for `row(M_r)` and `N_r=M_rU_r`, then `U1^T T U2=0` and

`U1^T C_B U2=N1^T(R-B^{-1})N2`.

Therefore

`E2(C_B) >= S1^2 S2^2 |det(R-B^{-1})|^2`.

The tail cannot cancel this full-rank common-plane Schur mismatch; no `||T||` smallness is used.

Using B08 r36 `QFORM-PAIR-SCHUR-E2-LINF-v1`, for invertible indefinite `B`, `Delta=|detB|`, `kappa=smin(B)`,

`||p_Q||_infty <16.511 Delta^{-9/38} kappa^{-5/19}[S1 S2 |det(R-B^{-1})|]^{-5/38}`.

At r43 scale, if `kappa>=tau L` and `delta=L^2|det(R-B^{-1})|>0`,

`||p_Q||_infty <120.649 tau^{-14/19} delta^{-5/38}/L`.

This proves essential boundedness, not continuity.

## New exact-zero hub theorem

If the physical two-hub quadratic block is exactly `B=0`, retain an ARBITRARY light quadratic-affine term `G(X,Y)`, including all common-plane edge/tail and same-bank curvature. Conditionally,

`Q=G(X,Y)+2H^T(M1X+M2Y+eta)`.

The vector `W=M1X+M2Y+eta` has 2D density cap `<=2/max(S1,S2)`. The radial bathtub inequality gives `E||W||^{-1}<=2sqrt(pi M_W)`. Conditioning on the two physical hubs gives density cap `<=1/(sqrt2||W||)`. Hence

`||p_Q||_infty <=2sqrt(pi/max(S1,S2)) <155.158/L`,

and dominated convergence yields a continuous `C0` density. This branch is completely insensitive to the nonzero light-light edge and tail.

Designated partner actually applied: account04/B08 `yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74` gives for its exact scaled anisotropic family

`||p_{Q_(R,L)}||_infty<7.251/L`, `R>=3`.

Regression: 5,000 seeded coefficient tests; zero violations; `QFORM_B08_R45_CHECK_PASS` in the run directory.

Remaining B08 debt: singular/near-singular nonzero two-hub blocks, or indefinite pairs on/near the Schur-matched rank-at-most-one surface `det(R-B^{-1})=0`, retaining the full physical tail and arbitrary rough product laws. Do not reopen the exact `B=0` endpoint; it is paid above. Full QFORM and full-target continuity remain OPEN.
