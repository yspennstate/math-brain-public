SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T08:43:18Z.
attacking: Additional eigenvalue control — full nonseparable spectral tails at matrix level by protecting a three-dimensional complementary Schur shield and charging only leakage into that shield.

# account03/B12 — anisotropic three-shield leakage stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T084318Z-qform-eigenvalue-r29`  
Assignment: Additional eigenvalue control  
Status: **PROVED SUPPORTING STABILITY THEOREM / NEWEST-CLAUDE RESULT APPLIED / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**  
Continuity: the Schur-shield branch below proves an essential-L-infinity bound only; the separate three-volume branch in Section 8 has a continuous C0 density.

## 1. Exact target and control scope

The sole target remains: for every dimension, every independent real product law with one-dimensional probability densities bounded by one, and every real symmetric matrix A with at least three eigenvalues of absolute value at least one, prove a universal bound on the density of Q=X^T A X, or give a valid counterexample.

No Gaussianity, moment, compact-support, log-concavity, connected-support, or post-rotation independence is used below. Every probabilistic endpoint is applied on ORIGINAL independent coordinates. Orthogonal bases W,Z appear only inside deterministic matrix algebra.


## 2. Completed sources actually used

### Designated account04/B12 partner

The completed partner theorem is

`yspennstate/math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T081758Z-account04-B12-complementary-schur-shield-r4/REPORT.md`.

Its exact complementary-Schur shield says that if an actual physical block is B+U Theta U^T, W spans range(U), Z is its orthogonal complement, D=Z^T B Z has three singular values at least mu, and rho=||W^T B Z D^{-1}||op, then for every symmetric Theta

`s3(B+U Theta U^T) >= ell(rho)^2 mu`,

where

`ell(rho)=(sqrt(rho^2+4)-rho)/2`.                                (2.1)

The result is matrix algebra; no independence in the W,Z coordinates is asserted. I apply (2.1) at equation (4.8), after first proving that the *perturbed* complementary block and shear still satisfy explicit bounds.

The algebra beneath (2.1) was also checked against the account01/B12 singular-core source

`yspennstate/math-open-problems@e1c78c69591e4d0cf3107a610ab0f764670d1928`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B12/20260923T065152Z-account01-B12-QFORM-r28/REPORT.md`.

### Required newest-Claude/volume-stability source

The required current volume-stability source is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For an ORIGINAL-coordinate cross block M=M0+E with s3(M0)>=a, maximum range-projection row leverage <=1/2, and ||E||op<=a/16, it proves

`||p_Q||infinity <= 24 sqrt(3) e/(5a) < 23/a`,                    (2.2)

with a continuous C0 density, while self blocks, outside couplings and affine terms are arbitrary. Section 8 applies this theorem to an actual spectral-addition inequality.

### Finite physical spectral receiver

The finite-dimensional physical receiver used after (4.8) is the established three-large-direction bound: if an ORIGINAL-coordinate block of size m has three actual eigenvalues of modulus at least gamma, then

`||p_Q||infinity <= 2 sqrt(6 pi m)/gamma`.                        (2.3)

One direct route is the proved physical-fiber estimate from the current Claude package, choosing a three-dimensional large spectral subspace and using Cauchy-Schwarz on its physical-coordinate leverage. This remains a statement about the actual m original coordinates; it does not rotate the random vector and declare the spectral coordinates independent.

## 3. What was missing in the partner theorem

The partner result makes an arbitrary active update U Theta U^T completely free, but its protected complementary block D and its cross shear are held fixed. For the B12 assignment, the next natural question is whether a genuinely nonseparable added spectrum may also leak into the protected three-dimensional complement.

A global operator-norm bound on the whole added matrix is too crude: large eigenvalues supported in the active face should cost nothing. Conversely, calling X^T E X a small random error from a small matrix norm is invalid for arbitrary unbounded inputs.

The correct quantity is therefore anisotropic: charge only the matrix columns that enter the protected three-dimensional shield.

## 4. New theorem — anisotropic three-shield leakage stability

Let I be an ORIGINAL-coordinate physical block of size m>=3. Inside the deterministic Euclidean space R^I choose an orthogonal decomposition

`R^I = W direct_sum Z`, `dim Z=3`.                                (4.1)

Relative to orthonormal bases of W and Z, write the baseline physical compression

`H0 = [[A0,C0],[C0^T,D0]]`.                                      (4.2)

Assume D0 is invertible and define

`mu0  = sigma_min(D0) > 0`,
`rho0 = ||C0 D0^{-1}||op`.                                       (4.3)

Now add an arbitrary symmetric matrix on the same physical block,

`E = [[G,F],[F^T,EZ]]`.                                          (4.4)

There is **no restriction whatsoever on G**. It may have arbitrary rank, signs, eigenvectors and operator norm. Assume only

`eta     = ||F||op`,
`epsilon = ||EZ||op < mu0`.                                      (4.5)

Put

`mu = mu0-epsilon`,
`rho_bar = (rho0*mu0+eta)/(mu0-epsilon)`,
`ell(r)=(sqrt(r^2+4)-r)/2`,
`gamma = mu * ell(rho_bar)^2`.                                   (4.6)

### Theorem 4.1 — `QFORM-ANISOTROPIC-THREE-SHIELD-LEAKAGE-STABILITY-v1`

For the actual final physical block H=H0+E,

`boxed: s3(H) >= gamma.`                                         (4.7)

Consequently, for the complete ambient quadratic form, with arbitrary additional coordinates, arbitrary outside self block, and arbitrary couplings between I and its complement,

`boxed:
 ||p_(X^T A X)||infinity
 <= 2 sqrt(6 pi m)/gamma.`                                       (4.8)

The estimate is uniform over the unrestricted active face G. For bounded m and a positive numerical shield margin gamma, this is dimension-free in the ambient problem.

### Proof

Set

`D=D0+EZ`, `C=C0+F`.                                              (4.9)

Weyl gives

`sigma_min(D) >= mu0-epsilon = mu >0`.                            (4.10)

The first essential implication is a resolvent/shear bound that depends only on shield leakage. Since D0=D-EZ,

`D0 D^{-1}=I-EZ D^{-1}`.                                         (4.11)

Therefore

`C D^{-1}`
`= C0 D0^{-1}(D0 D^{-1}) + F D^{-1}`                             (4.12)

and hence

`||C D^{-1}||op`
`<= rho0(1+epsilon/mu)+eta/mu`
`= (rho0*mu0+eta)/mu`
`= rho_bar`.                                                       (4.13)

Now freeze the perturbed C,D and absorb every other W-W term into the active update. More explicitly, use the partner theorem with active subspace W, complementary subspace Z, baseline

`B'=[[A0,C],[C^T,D]]`

and arbitrary active update

`[[G,0],[0,0]] = W G W^T`                                        (4.14)

(in coordinates adapted to W direct_sum Z). Because dim Z=3, equation (4.10) supplies exactly three complementary singular values at least mu. Equation (4.13) bounds the partner shear by rho_bar. Since ell is decreasing on [0,infinity), the partner inequality (2.1) gives

`s3(H)
 >= mu * ell(||C D^{-1}||op)^2
 >= mu * ell(rho_bar)^2
 = gamma`.                                                        (4.15)

This proves (4.7).

For completeness, the same step can be seen from the exact factorization

`H = L diag(S,D) L^T`,
`L=[[I,C D^{-1}],[0,I]]`,
`S=A0+G-C D^{-1} C^T`.                                           (4.16)

The Schur block S can be completely singular. The diagonal matrix in (4.16) nevertheless has three singular values at least mu because D is 3 by 3. The exact shear formula from the partner theorem is

`sigma_min(L)=ell(||C D^{-1}||op)`,                               (4.17)

and `s3(PMQ)>=sigma_min(P)s3(M)sigma_min(Q)` proves (4.15) directly.

Finally apply the finite physical receiver (2.3) to the actual ORIGINAL-coordinate block I. Conditioning on all original coordinates outside I preserves independence inside I; outside cross terms become affine terms. This proves (4.8). No spectral-coordinate independence or convolution of a dependent remainder occurs. QED.

## 5. Useful simplified leakage form

Let P_Z be the Euclidean orthogonal projection onto the protected three-dimensional shield. If the added physical compression E satisfies only

`||E P_Z||op <= delta < mu0`,                                     (5.1)

then both eta and epsilon in (4.5) are at most delta. Hence

`gamma >= (mu0-delta)
          ell((rho0*mu0+delta)/(mu0-delta))^2`.                  (5.2)

There is still no bound on `P_W E P_W`.

Since

`ell(r)=2/(sqrt(r^2+4)+r) >= 1/(1+r)`,                            (5.3)

one also has the elementary lower bound

`gamma >= (mu0-epsilon)^3 /
          ((1+rho0)mu0+eta-epsilon)^2`.                           (5.4)

This gives a quick sufficient numerical gate without evaluating the square root in ell.

A particularly clean zero-cost statement follows from delta=0:

`E P_Z=0  =>  s3(H0+E)>=mu0 ell(rho0)^2`,                         (5.5)

even when the active added spectrum is arbitrarily large, indefinite and high rank inside W.

## 6. Literal added-eigenvalue interpretation

Let a global added symmetric matrix have spectral representation

`R=sum_r tau_r v_r v_r^T`,                                       (6.1)

with no restriction on the signs or magnitudes of tau_r. Restrict each v_r to the physical block I and decompose

`v_r|_I = w_r+z_r`, `w_r in W`, `z_r in Z`.                       (6.2)

Then the shield blocks of R satisfy the deterministic estimates

`||P_Z R[I,I] P_Z||op
 <= sum_r |tau_r| ||z_r||^2`,                                    (6.3)

and

`||P_W R[I,I] P_Z||op
 <= sum_r |tau_r| ||w_r|| ||z_r||`.                              (6.4)

Thus Theorem 4.1 gives an explicit stability theorem for adding both smaller and larger eigenvalues of either sign. An added eigenvector with z_r=0 costs **exactly zero regardless of |tau_r|**. More generally, a very large eigenvalue is allowed whenever its actual weighted leakage into the three-dimensional shield is correspondingly small. Signs may cancel in the actual operator norms, so (6.3)-(6.4) are conservative sufficient bounds, not necessary conditions.

All added spectrum supported outside I is also free: after conditioning on the outside ORIGINAL coordinates it enters only the outside scalar term and affine shifts already allowed by the physical receiver.

## 7. Non-coordinate-aligned concrete target-class family

The shield Z need not be spanned by independent coordinates. To make that explicit, let O be the 5 by 5 Householder orthogonal matrix

`O=I-2 uu^T`, `u=(1,1,1,1,1)^T/sqrt(5)`.                         (7.1)

Let W be the span of the first two columns of O and Z the span of the last three. Both are mixed across the five ORIGINAL coordinates.

In the W direct_sum Z basis take

`A0=0_(2x2)`,
`C0=[[1,0,0],[0,1,0]]`,
`D0=diag(3,-3,3)`.                                                (7.2)

Let G be **any** real symmetric 2 by 2 matrix, with unbounded norm and arbitrary signs. Let F,EZ be arbitrary subject only to

`||F||op<=1/4`, `||EZ||op<=1/4`.                                 (7.3)

Conjugate the resulting five-dimensional matrix by O back to the ORIGINAL physical coordinates. This conjugation is only how the deterministic matrix is defined; the input vector X is not rotated.

Here

`mu0=3`, `rho0=1/3`, `mu=11/4`, `rho_bar=5/11`.                   (7.4)

Therefore

`gamma`
`=(11/4) ell(5/11)^2`
`=(267-5 sqrt(509))/88`
`=1.752214298559264... >1`.                                      (7.5)

The final physical five-block has at least three eigenvalues of modulus greater than one for every G,F,EZ satisfying (7.3), so by threshold interlacing the ambient matrix is in the exact target spectral class. Equation (4.8) gives

`boxed:
 ||p_Q||infinity
 <= 2 sqrt(30 pi)/gamma
 =11.0809842959972... .`                                         (7.6)

The active two-dimensional spectral packet can move through zero, become arbitrarily large, change both signs independently and rotate internally. The estimate does not change.

The attached deterministic/random matrix checker tested 10,000 admissible F,EZ draws and active symmetric G scales between 10^-6 and 10^6. The smallest sampled ratio `s3/gamma` was about 1.57744 and there were no violations. This is only a sanity check; the proof is (4.9)-(4.17).

## 8. Required application of the newest three-volume theorem

The Schur-shield theorem is strongest when a bounded physical core has a three-dimensional complementary shield. The newest volume-stability theorem gives a complementary matrix-level route when a diffuse cross face is available.

Let A=A_base+R and let I,J be disjoint sets of ORIGINAL coordinates. Put

`M0=A_base[I,J]`, `E=R[I,J]`.                                     (8.1)

Assume

`s3(M0)>=a>0`,
`max_i (P_range(M0))_ii <=1/2`,
`||R[I,J]||op <= a/16`.                                          (8.2)

Apply the newest theorem (2.2) to the **actual** final cross block M=M0+R[I,J]. It gives

`boxed:
 ||p_(X^T A X)||infinity
 <= 24 sqrt(3) e/(5a)
 =22.5993707336750.../a <23/a.`                                  (8.3)

Moreover this branch has a continuous C0 density.

The point for additional eigenvalues is that every other face of R is unrestricted. In particular `R[I,I]`, `R[J,J]`, every outside block, and every outside coupling may contain eigenvalues of arbitrary magnitude and either sign. They are retained inside the theorem's arbitrary self functions/outside conditioning. Only the cross footprint in (8.2) is paid.

For the spectral expansion (6.1), a sufficient cross-footprint inequality is

`||R[I,J]||op
 <= sum_r |tau_r| ||(v_r)_I|| ||(v_r)_J|| <= a/16`.              (8.4)

Thus an arbitrarily large added eigenvalue is free in this branch whenever its eigenvector misses one side of the protected cut. This is a genuine equation-level application of the newest-Claude theorem, not a renamed copy of it.

## 9. Combined interpretation for full nonseparable tails

Sections 4 and 8 give two anisotropic matrix-level stability gates:

1. **Three-shield gate:** unlimited spectrum on the active W-W face; charge only W-Z and Z-Z leakage into a protected three-dimensional complement.
2. **Diffuse-cross gate:** unlimited spectrum on both self faces and outside the protected cut; charge only the actual I-J cross footprint.

Neither gate says a small matrix is a small random quadratic variable. Both keep all dependence induced by the quadratic form. They show that the absolute sizes of additional eigenvalues are often the wrong parameter: only the matrix faces through which they can destroy the existing smoothing certificate matter.

This is the concrete progress for the B12 assignment in this run.

## 10. What remains open

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** The bare global hypothesis `s3(A)>=1` has not been shown to force either of the two gates above, nor one of the previously paid grouped-bank, hub, ridge, pair, or scalar-Schur exits.

The remaining structural problem can now be phrased more sharply for this workstream: rule out, or control directly, matrices for which every candidate bounded physical block has large leakage into every potential three-dimensional shield **and** every useful original-coordinate cross cut fails the diffuse three-volume gate. This residue contains the high-leverage/low-cross-rank mixed-sign geometry and cannot be solved by simply discarding the extra spectrum.

Continuity is separately tracked. Section 8 proves continuity in its exact scope. The Schur-shield route uses only the current physical spectral receiver, so this report claims only essential boundedness for Sections 4-7 and for no larger class.

## 11. Computation and integrity notes

`CHECK.py` and `CHECK_RESULT.json` in this run folder record the exact constants and a finite matrix sanity check. The computation is not evidence for the universal conjecture.

The changed-file content was manually reviewed for the authorized mathematical scope and contains no credentials, account secrets, private unrelated data, signed URLs, or public-release material. No scheduler state, notifications, email delivery, permissions, task identities, cadence, paid model/API/Codex calls, remote workflows, or cross-account authentication were changed.

Repository access and writes do not establish native learned-memory ingestion. This run remains `WITHOUT_VERIFIED_BRAIN`.
