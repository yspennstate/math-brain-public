SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B12, 2026-09-24T10:19:23Z.
attacking: orthogonal spectral-band Pythagoras and certificate addition; isolate precisely what arbitrary extra signed spectrum can and cannot change.

# fleet01/B12 — orthogonal spectral-band certificate addition

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T101923Z-fleet01-B12-QFORM-auto11`  
Status: **NEW SUPPORTING STABILITY THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Regularity: the concrete six-mode application below gives an essentially bounded density only; no unrestricted continuity claim.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The bare hypothesis `s_3(A)>=1` still does not force six localized square-carrier modes, a D5 cross block, or another already-paid original-coordinate receiver. This run does not claim otherwise.

The narrower B12 question is whether arbitrary additional eigenvalues of either sign can destroy a deterministic carrier already assembled from selected spectral pieces. For arbitrary matrix additions the answer is yes because of destructive cross terms. For **disjoint spectral bands of the same symmetric matrix**, however, the answer is exactly no: the output channels are orthogonal before any random variables enter. This gives a clean addition rule for positive square certificates and shows that large, small, positive and negative omitted eigenvalues cannot cancel a carrier built from other spectral bands.

No random vector is rotated. No term `X^T R X` is treated as an independent convolution or as a small random variable.

## 2. Exact spectral-band Pythagoras

Let `A=A^T` and let `Omega_1,...,Omega_r` be pairwise disjoint Borel subsets of the real line. Define the spectral-band operators

`A_j = A 1_{Omega_j}(A)`.

Then each `A_j` is symmetric and, by orthogonality of spectral projections,

`A_i A_j=0` for `i!=j`.                                      (2.1)

Let `A_band=sum_j A_j`. For any deterministic isometry `P:R^m -> R^n` (in particular, an ORIGINAL-coordinate embedding),

`(A_band P)^T(A_band P)
 = sum_j P^T A_j^2 P`.                                       (2.2)

Equivalently, for every `x in R^m`,

`||A_band P x||^2 = sum_j ||A_j P x||^2`.                    (2.3)

### Proof

Expand the Gram matrix:

`P^T (sum_i A_i)(sum_j A_j) P
 =sum_i P^T A_i^2 P + sum_{i!=j} P^T A_i A_j P`.

The cross terms vanish by (2.1). This proves (2.2), hence (2.3). QED.

Two immediate exact consequences are

`ker(A_band P)= intersection_j ker(A_j P)`,                  (2.4)

and the rank cannot decrease when a new disjoint spectral band is restored.

## 3. Positive certificate addition theorem

The preceding identity yields the useful monotone form.

### Theorem — `QFORM-ORTHOGONAL-SPECTRAL-BAND-CERTIFICATE-ADDITION-v1`

Under the hypotheses above, suppose for each band one has a deterministic positive-semidefinite certificate

`0 <= G_j <= A_j^2`.

Then

`boxed: 0 <= sum_j G_j <= A_band^2.`                         (3.1)

If the full matrix is

`A = A_band + R`,

where `R=A 1_{Omega_0}(A)` is the sum of all remaining spectral bands disjoint from the selected ones, then `A_band R=0` and

`boxed: A^2 = A_band^2 + R^2 >= sum_j G_j.`                  (3.2)

Consequently, for every ORIGINAL-coordinate bank `H`,

`lambda_k((sum_j G_j)[H,H]) >= g^2`

is a valid `k`-mode square-carrier certificate for the **actual final matrix A**, irrespective of the number, signs, multiplicities, orientations inside the complementary spectral subspace, or magnitudes of the eigenvalues in `R`.

### Proof

Because the bands are mutually annihilating,

`A_band^2=sum_j A_j^2`.

Summing `G_j<=A_j^2` proves (3.1). Orthogonality to `R` gives `A^2=A_band^2+R^2`, and `R^2>=0`, proving (3.2). QED.

This theorem is stronger than merely saying a single retained band survives: **several individually insufficient spectral bands may contribute positive certificates whose sum reaches the mode count required by a completed receiver.** Their signs never enter because the exact orthogonality is at the operator level.

## 4. Canonical three-large-eigenvalue normal form

Every target matrix admits a particularly transparent decomposition. Choose three orthonormal eigenvectors `u_1,u_2,u_3` with `|lambda_i|>=1`. Put

`C = sum_{i=1}^3 sign(lambda_i) u_i u_i^T`,

`D = sum_{i=1}^3 (lambda_i-sign(lambda_i)) u_i u_i^T`,

and let `R` contain every other eigenmode of `A`. Then

`A=C+D+R`,

`CR=DR=0`, and

`CD=sum_i (|lambda_i|-1) u_i u_i^T >=0`.                    (4.1)

Hence

`(C+D)^2 >= C^2=P_E`, where `E=span(u_1,u_2,u_3)`,            (4.2)

and exactly

`A^2=(C+D)^2+R^2 >= P_E`.                                    (4.3)

Thus magnitude inflation of the selected three large eigenvalues is sign-preserving/accretive, while **all other eigenvalues form an orthogonal square channel**. This fully removes destructive additional-eigenvalue cancellation from every proof branch whose deterministic input is a positive certificate below `A^2`.

The remaining difficulty is not spectral magnitude; it is turning the orientation of the rank-three projection `P_E` (possibly together with useful subthreshold spectral bands) into an ORIGINAL-coordinate paid receiver.

## 5. Important scope correction: `A^2` does NOT order quadratic-form densities

The square-certificate theorem must not be misread as a probabilistic monotonicity theorem. In fact even equality of squares does not compare the density norms.

Let `X,Y` be independent Uniform[-1/2,1/2], so both densities equal one. Set

`A_+=diag(1,1)`, `A_-=diag(1,-1)`.

Then

`A_+^2=A_-^2=I_2`.                                           (5.1)

For `Q_+=X^2+Y^2`, planar coarea on circles inside the unit square gives

`p_+(t) = (angular measure of the circle portion in the square)/2 <= pi`

for almost every `t`; in particular `||p_+||infinity<=pi`.

For `U=X^2`, the density is

`g(u)=u^(-1/2) 1_(0,1/4)(u)`.

Therefore, for `0<t<1/8`, the density of `Q_-=X^2-Y^2` obeys

`p_-(t)=int_t^(1/4) [u(u-t)]^(-1/2) du
       >= int_(2t)^(1/4) du/u
       = log(1/(8t)) -> infinity`.                            (5.2)

Hence

`boxed: ||p_-||infinity,ess = infinity while A_-^2=A_+^2.`    (5.3)

This is **not** a counterexample to the owner target because it has only two large eigenvalues. It is a correction to any intermediate claim that a density bound transfers from a clipped/core matrix to the actual matrix merely from `A^2>=C^2` or even `A^2=C^2`. Safe use of (3.2) is only to transfer a deterministic square certificate into a receiver already proved for the actual final matrix.

## 6. Actual six-mode family: three large modes + three subthreshold modes + arbitrary extra spectrum

Let `H={h_1,...,h_6}` and `J={j_1,...,j_6}` be disjoint ORIGINAL-coordinate banks. Define

`u_k=(e_{h_k}+e_{j_k})/sqrt(2)`, `k=1,...,6`.

The `u_k` are orthonormal. Choose arbitrary signs `epsilon_k`. For `k=1,2,3`, choose arbitrary magnitudes `L_k>=1`; for `k=4,5,6`, choose subthreshold magnitudes

`1/2 <= beta_k < 1`.

Let `S` be an **arbitrary symmetric operator on U^perp**, where `U=span(u_1,...,u_6)`, extended by zero on `U`. Its dimension, inertia, multiplicities, internal eigenvectors and eigenvalue magnitudes are completely unrestricted. Define

`A = sum_{k=1}^3 epsilon_k L_k u_k u_k^T
    +sum_{k=4}^6 epsilon_k beta_k u_k u_k^T
    +S`.                                                       (6.1)

The matrix is literally in the owner target because `s_3(A)>=1`. The selected six-mode band and `S` are spectrally orthogonal, so (3.2) is exact. On the original-coordinate bank `H`,

`(A^2)[H,H]
 >= diag(L_1^2/2,L_2^2/2,L_3^2/2,beta_4^2/2,beta_5^2/2,beta_6^2/2)
 >= (1/8) I_6`.                                               (6.2)

Thus with `G` equal to the selected six-band square,

`0<=G<=A^2`, `lambda_6(G[H,H])>=g^2`, `g=1/(2sqrt(2))`.       (6.3)

This is the key point: three subthreshold eigenvalues supply exactly the missing three carrier modes, while every further positive or negative eigenvalue is restored at zero carrier cost.

## 7. Required partner application to an actual inequality

First apply the newest completed designated fleet02/B12 result

`QFORM-ORTHOGONAL-TWO-CHANNEL-MODE-STABILITY-v1`,

source `yspennstate/math-open-problems@4cc6fbf96ef099a1492e043882219496509e94ba`,
path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260924T085711Z-fleet02-B12-r13/REPORT.md`.

Take the six-mode selected operator as the baseline, `M=C_6 P_H`, and `N=S P_H`. Spectral orthogonality gives

`M^T N=P_H^T C_6 S P_H=0`, hence the partner relative matrix is exactly `K=0`. Its exact inequality with `r=s=0` gives

`boxed: s_6(A P_H)^2 >= g^2 + s_6(Z)^2 >= 1/8.`              (7.1)

This is an equation-level application on the **actual final matrix**, not a citation-only dependency.

For density closure, apply the completed fleet02/B12 theorem

`QFORM-SIX-MODE-SPECTRAL-SQUARE-CARRIER-v1`,

source `yspennstate/math-open-problems@e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`,
path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260923T145451Z-fleet02-B12-QFORM-r36/REPORT.md`.

Use `m=6`, `s=1`, `g=1/(2sqrt(2))`, and choose

`b=99/(200sqrt(2))`,
`a=11/(500sqrt(2))`,
`kappa=b/15-a=11/(1000sqrt(2))`.                              (7.2)

The four theorem terms are

`T1 = 6000 sqrt(2 pi)/11 = 1367.251786162364...`,
`T2 = 1000 sqrt(2) pi/11 = 403.898448923488...`,
`T3 = 3*400^(1/3)*(1000 sqrt(2)/11)^(5/6)
    = 1264.959183656935...`,
`T4 = 2000 sqrt(e/199) = 233.749504219358...`.                (7.3)

Therefore every matrix in the family (6.1), uniformly over the entire arbitrary spectator spectrum, satisfies

`boxed: ||p_(X^T A X)||_(infinity,ess) < 1368.`               (7.4)

The six-mode partner theorem as a whole does not prove a continuous representative, so this application records essential boundedness only.

## 8. What this settles and what remains

Settled for B12 stability:

1. Disjoint signed spectral bands add **exactly in square energy** on every original-coordinate domain; they cannot cancel one another there.
2. Positive square certificates from several bands add. Thus smaller eigenvalues may supply missing carrier modes and arbitrary omitted larger/smaller eigenvalues of either sign can be restored without eroding the certificate.
3. Selected large-eigenvalue magnitude inflation is also harmless at the certificate level.
4. None of these deterministic facts licenses density comparison between a spectral core and the full quadratic form; Section 5 gives an exact cap-one counterexample to such a shortcut.

Still open:

From only `s_3(A)>=1`, the spectrum may have exactly three nonzero modes or all subthreshold modes may be too weak/diffuse to provide the additional modes used in Section 6. One must still extract, from the rank-three orientation and any available additional spectral mass, an ORIGINAL-coordinate localized/ridge/grouped-bank/pair/Schur/common-plane/Pluecker receiver, with the known correction set respected. This report does not close that global structural implication.

No Gaussianity, log-concavity, moments, compact support, connected support, diagonal-basis independence, or rotated-variable independence is used.
