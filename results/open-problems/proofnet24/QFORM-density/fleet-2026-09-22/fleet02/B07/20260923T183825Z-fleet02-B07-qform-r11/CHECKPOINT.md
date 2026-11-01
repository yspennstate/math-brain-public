SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T18:38:25Z.
attacking: partner r35 rank-two interface tube — retain its E2 volume law, identify when the two-heavy spectral carrier itself is physically support-concentrated, and turn that aggregate carrier mass into an actual bounded physical principal core without selecting one coordinate minor.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T183825Z-fleet02-B07-qform-r11`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **new carrier-Pluecker bounded-core lemma in progress; full QFORM open**.

The first unpaid implication is now isolated as follows. Fleet03/B07 r35 (source commit `3a3334245375f0d72687f3cb482b4478d51f3188`) supplies an original-coordinate cross block `K=A[L,R]` with

`Z=e_2(KK^T)>Z0 h^4`, `Z0=854675.100194511`,
`h=(2sqrt(2)-1)/1572864`,

and, on its low-E3 branch, the two-compound spectral projection `P` onto singular directions whose pair-volume inclusion marginal exceeds `2/3`, with `rank(P)<=2` and

`||(I-P)A[L,L^c]||_F < eps0 h`, `eps0=3/sqrt(Z0)=0.003245045039...`.

The new observation is strongest when `rank(P)=2`. Write the selected singular directions as `a,b`. In the singular-index pair law

`q_rs=s_r^2 s_s^2/Z`,

both inclusion marginals exceed `2/3`; hence inclusion-exclusion gives

`q_ab > 1/3`, so

`(s_a s_b)^2 > Z/3`.                                           (C1)

Let `U=(u_a,u_b)` and `V=(v_a,v_b)` be the corresponding ORIGINAL-coordinate left/right two-frames, and let

`C=s_a u_a v_a^T+s_b u_b v_b^T`.

For physical supports `R0 subset L`, `C0 subset R`, define their rank-two Pluecker capture

`rho_L=det(U_R0^T U_R0)
      =sum_{S subset R0, |S|=2} det(U_S)^2`,
`rho_R=det(V_C0^T V_C0)
      =sum_{T subset C0, |T|=2} det(V_T)^2`.

These are aggregate determinant weights; no pair is selected. Cauchy-Binet and (C1) give exactly

`e_2(C[R0,C0] C[R0,C0]^T)
 =(s_a s_b)^2 rho_L rho_R
 >(Z/3) rho_L rho_R`.                                           (C2)

The r35 tail bound restricts to `||K-C||_F<eps0 h`. Under the strict-N3 physical entry cap `|K_ij|<=h/8`, if `|R0|,|C0|<=m`, then

`s_1(C[R0,C0]) <= (m/8+eps0)h`.

Since the carrier restriction has rank two, (C2) therefore yields

`s_2(C[R0,C0])
 > [sqrt(Z0/3)*sqrt(rho_L rho_R)/(m/8+eps0)] h`.                (C3)

After restoring the true tail and the two actual same-side physical blocks,

`s_4(A[R0 union C0,R0 union C0])
 > h[ sqrt(Z0/3)*sqrt(rho_L rho_R)/(m/8+eps0)
      -eps0 -(m-1)/8-h/128 ].                                  (C4)

Thus if each carrier Pluecker law places at least half its mass on supports of size at most `m`, i.e. `rho_L,rho_R>=1/2`, the bracket is positive for every `m<=131`; at `m=131` it is still

`0.041311209789...`,

so an actual principal block on at most `262` ORIGINAL coordinates has four eigenvalues of modulus at least

`4.8023564996e-8`.

Conditioning only outside this physical core preserves independence and the cap-one laws. The already-completed finite-dimensional spectral theorem then gives a universal essential-density bound on this branch. The point is that the support hypothesis is on the entire rank-two Pluecker volume, not on a best coordinate pair.

The remaining low-E3 state is therefore sharper than r35's generic rank-two tube: either the compound projection has rank at most one, or at least one of the two physical rank-two Pluecker laws is genuinely support-diffuse (no <=131-coordinate support carries half its area). I will record the exact core constant and an exact diffuse target-class regression in the full report.

Full QFORM remains OPEN. Continuity is not claimed by this checkpoint.
