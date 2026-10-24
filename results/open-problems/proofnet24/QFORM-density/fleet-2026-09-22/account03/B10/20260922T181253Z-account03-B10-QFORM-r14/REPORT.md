SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B10, 2026-09-22T18:12:53Z.
attacking: exact rank-three partial null-ray bank; condition on the genuine bank aggregate, whiten the complementary physical frame, close the diffuse-complement branch, and quantify the remaining high-leverage branch with completed account04 determinant-bank mathematics.

# account03/B10 r14 — partial null-ray bank, diffuse complement

Programme `QFORM-DENSITY-3EIG-20260922`. Assignment: rank-three coupled case. Execution: `WITHOUT_VERIFIED_BRAIN`. New supporting theorem proved; full QFORM remains **OPEN / NOT PROVED**.

## Correction discipline

I use only original-coordinate product independence. The live corrections are binding: arbitrary-joint 3D coarea is false; positive moments of normalized conditional projection densities can diverge; a conditional density cap does not substitute for genuine independence in the hyperbolic branch; naive fiber suprema lose dimension; and law-uniform pointwise quadratic-phase decay is false.

## Exact setup

Let `A=U Lambda U^T`, `U^T U=I_3`, with `Lambda` real symmetric invertible and all three eigenvalues of modulus at least one. Let a nonempty physical-row bank `B` lie on a unit spectral null ray `r`:

`u_i=alpha_i r`, `r^T Lambda r=0`, `i in B`.

Set `L=sum_{i in B} alpha_i^2`, `rho=1-L`, `W=sum_{i in B} alpha_i X_i`. The previous B10 run closed `L=1`; here `0<L<1`. Let `C=B^c` and `U_C` be the complement rows. Parseval gives

`G=U_C^T U_C=I_3-L r r^T`,

so `G` has eigenvalues `(rho,1,1)` and `det G=rho`. Define

`U_tilde=U_C G^(-1/2)`, `Z=U_tilde^T X_C`,

`M=G^(1/2) Lambda G^(1/2)`, `d=G^(1/2) Lambda r`.

Then `U_tilde^T U_tilde=I_3`, `det M=rho det Lambda`, and, because `r^T Lambda r=0`, the original bank/complement split gives the exact identity

`Q=Z^T M Z+2W d^T Z`.                                           (1)

`W` is genuinely independent of the complement original coordinates. No independence among the coordinates of `Z` is asserted.

For each complement row define the whitened leverage

`c_tilde_j=u_j^T G^(-1)u_j=||(U_tilde)_{j,*}||^2`.

## Theorem: `QFORM-PARTIAL-NULL-BANK-DIFFUSE-COMPLEMENT-v1`

If

`max_{j in C} c_tilde_j <=1/2`,

then `Q` has an essentially bounded density with

`||p_Q||_infinity <=3e (rho |det Lambda|)^(-1/3)`.                (2)

Under `|lambda_1 lambda_2 lambda_3|>=1`, this is `<=3e rho^(-1/3)`; if `rho>=1/8`, it is `<=6e<16.310`.

### Proof

Condition on the bank aggregate `W=w`. This is product-preserving because `W` uses only original coordinates in `B`. From (1),

`Q_w=(U_tilde^T X_C)^T M(U_tilde^T X_C)+2w d^T U_tilde^T X_C`.

The linear term is coordinate-separable in the untouched original complement variables:

`2w d^T U_tilde^T X_C=sum_{j in C} 2w <(U_tilde)_{j,*},d> X_j`.

Apply the completed `QFORM-DIFFUSE-SEPARABLE-PHASE-v1` theorem to the genuine Parseval frame `U_tilde`, rank three, matrix `M`, and these coordinate-linear phases. It requires no independence of the projected coordinates and gives uniformly in `w`

`||p_{Q|W=w}||_infinity <=3e |det M|^(-1/3)`

`=3e(rho |det Lambda|)^(-1/3)`.

Mixing over `W` cannot increase a common `L^infinity` bound, proving (2). QED.

Regularity: essential boundedness is proved here. The source diffuse theorem gives a continuous density for every fixed `w`, but this report does not separately verify a jointly measurable parameter-uniform continuous representative before mixing, so continuity of the mixed density is **not claimed here**.

## Completed compatible account04 result applied

Fresh repository inspection found no completed current-QFORM artifact for the exact named partner `account04/B10`; none is fabricated. I applied the completed compatible account04/B16 theorem at `yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T161909Z-account04-B16-QFORM-r2/REPORT.md`.

Apply its exact fixed-pair identity to

`A_CC=U_tilde M U_tilde^T`.

If a whitened row `i` has leverage `c>1/2` and another row `j` has residual leverage

`h=||(I-ee^T)(U_tilde)_{j,*}||^2>1/2`, `e=(U_tilde)_{i,*}/sqrt(c)`,

then its theorem yields `G_ij=ch>1/4` and therefore

`sum_{k in C\{i,j}} |det(A_CC)_{i,j,k}|`
`=|det M| c h > rho |det Lambda|/4`.                              (3)

Thus failure of the diffuse branch cannot erase the third-order determinant resource in a nested-heavy complement.

The same account04 theorem gives a real conditional density gate when an eligible zero-diagonal third-coordinate atom has normalized bank weight at least `tau`. Conditioning on `W=w` only supplies an arbitrary affine term, which that theorem permits, so

`||p_Q||_infinity <= C_off (4/(tau rho |det Lambda|))^(1/3)`,      (4)

where `C_off=2^(4/3)[log3+2log(3/2)]=4.8117455951457755...`. For `rho>=1/8`, `tau>=1/8`, `|det Lambda|>=1`, (4) is `<30.553`.

## Residual

The previous unpaid partial-null-bank problem is strictly reduced. The diffuse whitened-complement branch is closed by (2). A nested-heavy complement has determinant mass (3), and any eligible heavy zero-diagonal atom is paid by (4). Remaining exact-rank-three work is concentrated in: nested-heavy diffuse determinant banks without an eligible heavy atom; the non-nested heavy geometry (one row heavy but all residual row leverages at most one half); and the near-endpoint `rho->0` bridge, where (2) deteriorates although the already-proved endpoint `rho=0` is uniformly bounded. These must be handled without replacing product provenance by a normalized conditional cap.

Arbitrary additional spectral directions are also unpaid for the full owner conjecture.

## Exact sources used

Previous B10 null-ray bank theorem: `yspennstate/math-open-problems@a2970af7de27ec651907650644ca9689880ac5b1`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260922T171741Z-account03-B10-QFORM-r13/REPORT.md`.

Diffuse separable-phase theorem: `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, `proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.

Compatible account04/B16 determinant-bank theorem: `yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T161909Z-account04-B16-QFORM-r2/REPORT.md`.

**Full QFORM conjecture: OPEN / NOT PROVED.**
