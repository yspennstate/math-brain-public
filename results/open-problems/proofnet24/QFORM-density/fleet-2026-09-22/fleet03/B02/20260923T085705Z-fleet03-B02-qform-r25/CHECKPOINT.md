SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T08:57:05Z.
attacking: the mixed-(3+2)-volume heavy-marginal residue by replacing the fixed 1/2--1/2 determinant mixture with a weighted mixture and forcing a common physical anchor when every admissible Fourier marginal gate fails.

# Early substantive checkpoint — weighted mixed-volume interpolation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: fleet03/B02, Integrated Fourier estimate  
Control revision read: `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`; repository transport only.

Let `B=A[I,J]` be an ORIGINAL-coordinate cross block. Fix a physical row anchor `x` and column anchor `y`. Let `J3` be the sum of squared `3x3` minors containing `x,y`; let `N=B[I\{x},J\{y}]` and `E2=e2(N^T N)`. Normalize the incident third-minor and residual second-minor determinant laws, with inclusion marginals `(alpha^(3),beta^(3))` and `(alpha^(2),beta^(2))` (extended by zero at `x,y` for the second-minor law).

For `0<theta<1`, define

`alpha(theta)=theta alpha^(3)+(1-theta)alpha^(2)`,
`beta(theta) =theta beta^(3) +(1-theta)beta^(2)`,

so `sum alpha=sum beta=2+theta`.

The two retained positive families in the diagonal-plus-PSD determinant expansion obey

`A3 >= J3 prod d_i^(alpha_i^(3)) prod e_j^(1-beta_j^(3))`,
`A2 >= E2 prod d_i^(alpha_i^(2)) prod e_j^(1-beta_j^(2))`.

Weighted AM-GM gives the exact interpolation

`A3+A2 >= C_theta J3^theta E2^(1-theta)
              prod d_i^(alpha_i(theta)) prod e_j^(1-beta_j(theta))`,

where

`C_theta=theta^(-theta)(1-theta)^(-(1-theta))`.

Consequently Lieb's Gaussian Brascamp--Lieb formula gives the BL constant

`BL <= C_theta^(-1/2) J3^(-theta/2)E2^(-(1-theta)/2)
       prod alpha_i^(-alpha_i/2)
       prod (1-beta_j)^(-(1-beta_j)/2)`.

Combining one-sided ORIGINAL-coordinate Weyl differencing, Jensen at exponent `q`, and sharp Hausdorff--Young exactly as in the reviewed fractional-volume proof yields, whenever `1<=q<(2+theta)/2` and every mixed row marginal obeys `alpha_i(theta)<=q/2` (or symmetrically every mixed column marginal obeys the gate),

`E F_t^q <= C_theta^(-1/2)e^(2+theta)q^(-(2+theta)/2)
              (pi/|t|)^(2+theta)
              J3^(-theta/2)E2^(-(1-theta)/2)`.

Thus `|phi_Q(t)|<=min(1,K|t|^(-(2+theta)/(2q)))`, with an integrable exponent. Exact inversion gives the candidate weighted theorem

`||p_Q||inf <= e(2+theta)/[(2+theta-2q)sqrt(q)]
  * [theta^theta(1-theta)^(1-theta)]^[1/(2(2+theta))]
  * J3^[-theta/(2(2+theta))]
  * E2^[-(1-theta)/(2(2+theta))].`

At `theta=1/2` this reduces exactly to the preceding B02 mixed-(3+2) theorem. At `theta=1/2, q=6/5`, the gate is relaxed from `1/2` to `3/5` and the coefficient is `54.0054847234` multiplying `(J3 E2)^(-1/10)`.

If both the row and column `3/5` gates fail at this choice, choose a heavy non-anchor row `i` and non-anchor column `j`. Under the equal mixture of the third-minor and second-minor laws,

`P(i in R,j in T) >= P(i in R)+P(j in T)-1 >1/5`.

Therefore at least one constituent determinant law itself has joint incidence greater than `1/5`: either more than `J3/5` of the incident third-volume also contains `i,j`, or more than `E2/5` of the residual second-volume contains `i,j`. This is the first concrete heavy-marginal compiler; the next calculation is to express those two common-anchor banks as exact Schur/star resources and check all constants before the final report.

Status at checkpoint: substantive partial derivation; full QFORM still OPEN; target-wide universal unweighted Fourier `L1` still neither proved nor refuted.
