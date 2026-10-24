# Deterministic checks — account01/B04 r35

Marker: `QFORM_B04_R35_ARBITRARYSELF_EXACT_OPT_CHECK_PASS`.

The exact optimizer was differentiated symbolically in the report. Numerical checks used the same formulas independently:

- `eta=sqrt(2*pi*e)*erfc(1/sqrt(2)) = 1.311359084837597...`.
- Stress-pair data: `D=16`, `kappa=(sqrt(73)-3)/2`, `R=16 sqrt(332)=32 sqrt(83)`.
- `rho=2^(11/4)D/sqrt(kappa R)=3.7862666732672867... > sqrt(2)`.
- Exact optimized row certificate: `D^(-1/2)[4+eta+2 log(rho/sqrt(2))]=1.8202432195622835...`.
- The source theorem's displayed `q=1` choice gives `1.9476932346662073...`, strictly larger.
- For the unperturbed account02/B04 r22 stress matrix, `c_{ij}=16(j-i)^2`; exact enumeration of ordered disjoint physical pair-pairs gives `J=158720` and partner bound `3*2^(4/3)J^(-1/6)=1.0273599697935472...`.

Exact matrix checks used in the report:

- Base partner matrix characteristic polynomial: `(lambda-2)^3(lambda^3-59 lambda^2+34 lambda+960)`.
- The perturbed matrix differs from the base only in the symmetric `(3,4),(4,3)` edge by `1/10`, hence the perturbation operator norm is exactly `1/10`. The three base eigenvalues `2` therefore stay in `[1.9,2.1]` by Weyl, proving at least three target-scale eigenvalues without relying on floating point.
- For physical pair `H={1,2}`, `B=[[0,4],[4,3]]`, `det B=-16`, `sigma_min(B)=(sqrt(73)-3)/2`.
- The exact Schur complement on coordinates `3,4,5,6` is
  `[[5,41/10,5,6],[41/10,8,8,10],[5,8,13,14],[6,10,14,20]]`.
  Thus the last Schur self coefficient is `20` (genuinely nonzero), and its off-diagonal Schur-numerator row norm is `16 sqrt(6^2+10^2+14^2)=32 sqrt(83)`.
- The perturbation destroys the particular diagonal-plus-rank-one residual identity used by account02/B04 r22: on four distinct residual indices, `A_14 A_23=4*(61/10)=122/5`, whereas `A_13 A_24=3*8=24`.

No Monte Carlo or histogram enters any proof claim.
