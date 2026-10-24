# account01/B14 FEI handoff — near-deterministic MUX physical data block

**Classification:** `ESSENTIAL_STEP_APPLIED / PHYSICAL_DATA_BLOCK / FULL_FEI_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Scientific commit:** `e60ab8ec6cdd4048a340e0cbeea4f743cb34ff33`  
**Report blob:** `3726dc2b26e5c9440e8b9af8abd825c52aff2ba2`

Source-bound dependencies actually used:

- account04/B12 `20260922T0452Z-unequal-mux-cross-deficit`, blob `59ea7f1466e7abeff9d9756654fd6c4efa2bda98`;
- account04/B18 exact six-weight MUX formulas and source-robust derivative bound `|Gamma^dagger'(u)|<31 log2(1/u)+47` on the small side;
- account04/B16 `20260922T061055Z-cell-local-mux-quadratic`, blob `b78f51929cc557cd48a8003c0d3d3cd674728066`, used to assemble the current adaptive MUX block policy rather than duplicate its selector-cell region.

New theorem.  For

\[
M(A;D_0,D_1)=D_A,
\qquad
1/8\le p_A,p_{D_0}\le7/8,
\qquad
0\le p_{D_1}\le2^{-17},
\]

the live fixed candidate `Gamma^dagger` has `D_{Gamma^dagger}(M)>=0`.  The actual first block is the original coordinate `D_1`; its two children are AND/OR gates.  If the parent were negative, account04/B12 would force

\[
R_1^\dagger<-(a^\dagger-c_{RO})Q_0<-49/16384=-3136/2^{20}.
\]

The source envelope, exact six-mass movement and six-point Fannes--Audenaert bound instead give

\[
R_1^\dagger>-2855/2^{20},
\]

a contradiction with exact gap `281/2^20`.  By branch exchange and simultaneous data/output complementation, the same holds when either data bias is within `2^-17` of `0` or `1`, provided the selector and the other data bias lie in `[1/8,7/8]`.

This is complementary to account04/B16: use selector `A` in its balanced same-cell region, use the near-deterministic data coordinate in the new collar, and preserve the already-proved common-data/zero-credit/complementary-data branches.  The residual compact MUX region is still open.  The next useful extension is a boundary-adaptive version whose collar width scales with `Q_j=p(1-p)q_j(1-q_j)` rather than the fixed core lower bound `49/4096`.

**Full FEI remains OPEN / NOT PROVED.**
