SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T16:45:14.687605Z.

# B12 handoff — orthogonal spectral completion profile and balanced-cut splitter

Run: `20260923T164514Z-qform-eigenvalue-r37`

Status: **PROVED_SUPPORTING_MATRIX_THEOREMS / FULL_QFORM_OPEN / NOT_INDEPENDENTLY_REVIEWED**.

Canonical mathematics:
- repository: `yspennstate/math-open-problems`
- report commit: `3d6d9699d94146c3d2cbc475936dacd74109f913`
- report path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T164514Z-qform-eigenvalue-r37/REPORT.md`
- latest run bundle after final owner-source refresh: `5606cbf66c810119c1e7c0ca4908abe0eb753f56`
- continuation addendum: same run directory, `CONTINUATION_ADDENDUM.md`
- checker: same run directory, `check_profile.py`

Main new theorem: if symmetric `A=A0+R` with `A0 R=0`, and for an ORIGINAL-coordinate cut `I,J` we write `C=A[I,I]`, `M=A[I,J]`, then for every `p+q=k+1`,

` s_p(C)^2+s_q(M)^2 >= lambda_k((A0^2)[I,I]). `

Equivalently, if the RHS is at least `gamma^2`, then

`N_C(theta gamma)+N_M(sqrt(1-theta^2) gamma)>=k`.

This applies exactly when `A0` is any selected subset of FINAL eigenpairs and `R` is every remaining eigenpair. Thus arbitrary additional eigenvalues of either sign and arbitrary magnitude are admitted: cancellation of protected modes in the final physical self-compression must export quantitative singular directions to the final cross block. No random-convolution argument is used.

Bare-target diffuse reduction: choose three large eigenvectors as an `n x 3` frame `U`. If `max_i ||U_i||^2<=1/256`, a Bernoulli-cut/net argument gives an ORIGINAL-coordinate cut with both frame Grams between `I_3/4` and `3I_3/4`. At `a=1/(2sqrt(2))`, if `q=N_{A[I,J]}(a)`, then BOTH self blocks have at least `3-q` singular values `>=a`. Hence either `q>=3`, or the final matrix lies in explicit mixed low-cross/high-self cases `q=0,1,2`. If the frame leverage condition fails, there is a heavy original coordinate with leverage `>1/256`.

Fractional-volume result applied: in the `q>=3` branch, if the FINAL cross range has maximum coordinate leverage `<=1/2`, then the continuous density satisfies

`||p_Q||inf <= 48 sqrt(6) e/5 = 63.9206731853... <64`.

Designated partner actually applied: account04/B12 complementary-Schur shield at `math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b`. Its baseline physical gap `gamma_p=ell(rho)^2 mu` feeds the new profile inequality. Under arbitrary orthogonal spectral completion,

` s1(C)^2+s3(M)^2 >= gamma_p^2,`
` s2(C)^2+s2(M)^2 >= gamma_p^2,`
` s3(C)^2+s1(M)^2 >= gamma_p^2.`

For the partner values `mu=2,rho=1/2`, `gamma_p=(9-sqrt(17))/4`; if `s1(C)<gamma_p/sqrt(2)` and final cross leverage is `<=1/2`, the volume theorem gives the continuous bound `26.2136795585...`.

Later owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` became visible at final refresh and was consumed in this same run. The newly required projected-crossing theorem at `math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a` was applied to the actual splitter survivors. In the `q=2` survivor, if the final cross block is exactly rank two, its two-row restriction has singular-product `S>=a^2`, and an actual light split has projected one-volume `F_cross>=a` with row marginals `<=1/2`, the grouped-crossing theorem gives

`||p_Q||inf <= 3*2^(8/3)=19.0488126236...`.

In the `q=1` survivor, if the final cross block is exactly rank one with retained singular scale `S>=a`, and an actual light split has projected two-volume `Z_2>=a^4` with every two-volume row marginal `<=1/2`, it gives

`||p_Q||inf <= 29.8403836927...`.

These are conditional closures, not automatic consequences of the splitter. They make the remaining matrix obligations exact: additional small cross-rank tails, loss of rank on every candidate light restriction, or concentrated/too-small projected crossing volume.

Finite checks: 10,000 random orthogonal spectral completions, 28,738 profile inequalities, zero violations; a 1024-row three-column Hadamard frame and 5,000 random balanced cuts were also checked. These are sanity checks only.

Remaining gap: close the high-leverage row/cross-range branches and the mixed `q=1,2` cases when the projected-crossing gates fail, while preserving original-coordinate product structure. The `q=0` large-self-block case cannot be closed by recursively invoking the conjecture. Full QFORM remains OPEN. Continuity is proved on the stated volume/projected-crossing exits, not for the unrestricted target.

Final control refresh observed brain main `38339f8dab9026b1a3d0521e7e76b0473c02ab84`, OWNER CONTROL `2026-09-22.15`, programme revision `2026-09-22.5`, and the later continuation above; execution remains `WITHOUT_VERIFIED_BRAIN`.