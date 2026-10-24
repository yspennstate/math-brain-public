SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T10:57:38Z.
attacking: the invertible double-anchor Schur-Frobenius packet via aggregate physical five-volume and unconditional integrated Fourier control, with low-stable-rank residue kept explicit.

# account03/B02 r28 — aggregate five-volume receiver for the double-anchor Schur packet

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Owner control:** revision `2026-09-22.15`; QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport only  
**Full QFORM target:** OPEN  
**Target-wide universal unweighted Fourier L1 criterion:** OPEN / not refuted  
**Continuity:** proved on the new five-volume branch because the characteristic function is in L1; full-target continuity remains open.

## 1. Sources actually applied

1. Newest-Claude Fourier source, including the unrestricted fifth-volume theorem `D_5`:
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.
   It proves for any original-coordinate cross block `B`

   `||p_Q||inf <= 5 sqrt(2e) E5(B)^(-1/10)`,

   where `E5(B)=e5(B^T B)`, with no marginal condition. This is an L1 Fourier theorem and gives a continuous density.

2. The completed unconditional regularized-determinant estimate:
   `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`,
   `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`, equation (5.3):

   `|phi_Q(t)| <= det(I+4t^2 BB^T/(pi^2 e^2))^(-1/8)`

   for every physical cross block `B`, retaining arbitrary self blocks, affine terms, outside couplings and extra spectrum.

3. This slot's preceding double-anchor compiler, r27:
   `yspennstate/math-open-problems@ca2a43f342d9c5543457e2754c1c10db0d0300e3`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T102920Z-account03-B02-qform-r27/REPORT.md`.
   Its unresolved packet is, for a physical cross block

   `B=[[P,R],[C,M]]`,

   `G=||det(P)M-C adj(P)R||_F^2`,

   with either `G>Z3/24` on the live literal-minor endpoint, or the singular-pair two-star alternative.

4. Designated partner account04/B02:
   `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.
   On a nonsingular physical zero-diagonal `3x3` block `H0`,

   `integral |phi_Q(t)|^2 dt <= 6 pi 2^(2/3)|det H0|^(-1/3)`.

No law-uniform pointwise scalar quadratic-phase decay, post-rotation independence, arbitrary-joint coarea lemma, conditional density cap, or reciprocal selected minor is used.

## 2. Exact double-anchor to fifth-volume identity

Let `I,J` be disjoint sets of original independent coordinates and let `B=A[I,J]`. Reorder the chosen double anchor first and write

`B = [[P,R],[C,M]]`,

where `P` is `2x2`. Assume first that `P` is invertible. Set

`D=|det P|`,  `S=M-C P^(-1)R`.

For every far row triple `K` and far column triple `L`, the corresponding physical `5x5` minor contains all two anchor rows and columns. Schur's determinant formula gives exactly

`det B[{anchors} union K,{anchors} union L] = det(P) det S[K,L]`.    (2.1)

Squaring and summing over all `K,L` gives the anchored fifth-volume identity

`G5_anchor(B;P) = D^2 E3(S)`,                                    (2.2)

where

`E3(S)=e3(S^T S)=sum_{|K|=|L|=3} det S[K,L]^2`.

Since the total physical fifth volume includes these minors,

`boxed: E5(B) >= D^2 E3(S).`                                    (2.3)

This is the key new transport step. It pays the whole third compound of the true cross-Schur residual before choosing any single far minor.

The preceding r27 packet satisfies

`G = ||det(P)M-C adj(P)R||_F^2 = D^2 ||S||_F^2`.                 (2.4)

Thus the unresolved Frobenius packet and the fifth-volume currency are joined by a purely physical, exact compound identity.

## 3. Direct application of the newest unrestricted D5 theorem

Applying the completed newest-Claude theorem `D_5` to (2.3) gives immediately

`boxed:
 ||p_Q||inf <= 5 sqrt(2e) D^(-1/5) E3(S)^(-1/10).
}`                                                                  (3.1)

This application is within the exact source scope: `B` is an original-coordinate cross block, every same-bank quadratic term and every outside coupling is left arbitrary, and no marginal gate is imposed.

In particular, whenever `E3(S)>0`, the branch has a continuous density. The missing issue in r27 is therefore no longer merely “Frobenius Schur packet”: it is quantitatively the possibility that `E3(S)` is tiny relative to `||S||_F^6`.

## 4. Stable-rank compiler

Put

`F^2=||S||_F^2`,  `r=sr(S)=F^2/||S||op^2`.

Let `lambda_j=s_j(S)^2`. Then `sum lambda_j=F^2` and `max lambda_j=F^2/r`. Newton's identity gives

`E3(S)=e3(lambda)
 =[(sum lambda)^3-3(sum lambda)(sum lambda^2)+2 sum lambda^3]/6`.  (4.1)

Since

`sum lambda^2 <= (max lambda)(sum lambda)=F^4/r`,

and `sum lambda^3>=0`, for every `r>3`,

`boxed:
 E3(S) >= (r-3)/(6r) F^6.
}`                                                                  (4.2)

Combining (2.4) and (4.2),

`boxed:
 E5(B) >= (r-3)/(6r) * G^3/D^4.
}`                                                                  (4.3)

Hence the newest-Claude D5 theorem already yields

`||p_Q||inf
 <=5 sqrt(2e) [6r/(r-3)]^(1/10) D^(2/5) G^(-3/10).`             (4.4)

For `r>=4`,

`boxed:
 ||p_Q||inf <16.019663 D^(2/5) G^(-3/10).
}`                                                                  (4.5)

This is a genuine receiver for the r27 invertible double-anchor packet whenever the cross-Schur residual has stable rank at least four.

## 5. Sharper integrated Fourier constant from the regularized determinant

The completed regularized-determinant theorem allows a better constant and is useful because it directly exposes the integrated Fourier estimate requested by B02. Put

`c=4/(pi^2 e^2)`.

For the same cross block `B`,

`|phi_Q(t)| <= det(I+c t^2 BB^T)^(-1/8)`.                         (5.1)

The determinant expansion has nonnegative elementary-symmetric coefficients, so

`det(I+c t^2 BB^T)
 =sum_{k>=0} c^k t^(2k) Ek(B)
 >=1+c^5 t^10 E5(B)`.                                           (5.2)

Therefore

`|phi_Q(t)| <= [1+c^5 E5(B)t^10]^(-1/8)`.                       (5.3)

This envelope is integrable. With `a=c^5 E5(B)`, the beta integral gives

`integral_R [1+a t^10]^(-1/8) dt
 =(1/5)a^(-1/10) B(1/10,1/40)`.                                 (5.4)

Since `a^(-1/10)=c^(-1/2)E5^(-1/10)=(pi e/2)E5^(-1/10)`, Fourier inversion yields the unconditional aggregate fifth-volume corollary

`boxed:
 ||p_Q||inf <= C5 E5(B)^(-1/10),
 C5=(e/20) B(1/10,1/40)=6.770121056043999...
}`                                                                  (5.5)

and `phi_Q in L1`; hence the density is continuous and vanishes at infinity. This sharpens the constant of the already-proved unrestricted D5 theorem; the substantive new use here is the double-anchor bridge (2.3)-(4.3).

Substituting (4.3) into (5.5), for `r>3`,

`boxed:
 ||p_Q||inf
 <= C5 [6r/(r-3)]^(1/10) D^(2/5) G^(-3/10).
}`                                                                  (5.6)

At `r>=4`,

`boxed:
 ||p_Q||inf
 <=9.302883 D^(2/5) G^(-3/10).
}`                                                                  (5.7)

On the exact live r27 endpoint `G>Z3/24`, this gives

`boxed:
 ||p_Q||inf <24.136869 D^(2/5) Z3^(-3/10)
}`                                                                  (5.8)

whenever `sr(S)>=4`. On the stronger account02/B02 anchor-heavy endpoint `G>Z3/6`, the same calculation gives

`||p_Q||inf <15.924395 D^(2/5) Z3^(-3/10)`.                       (5.9)

These are supporting branch bounds, not universal constants, because the remaining structural proof has not yet bounded the dimensionless combination involving `D,G,Z3` under the bare three-eigenvalue hypothesis.

## 6. Exact meaning of failure: the residue is low effective rank

The compiler is useful even when its gate fails. If `sr(S)<4`, then

`||S||op^2 > ||S||F^2/4 = G/(4D^2)`,

so

`D ||S||op > sqrt(G)/2`.                                         (6.1)

Thus failure of the stable-rank-four L1 exit forces the cross-Schur Frobenius packet to concentrate into at most a few singular directions. This is precisely the regime for the grouped-hub / low-rank leaf mechanisms rather than another volume-averaging attempt. No claim is made that stable rank below four means exact rank below four.

The singular-pair branch `det P=0` remains separate. R27 gives an inverse-free two-star product there; equation (2.1) cannot be used because `P^-1` does not exist. This run does not silently regularize the singular pair.

## 7. Designated account04/B02 theorem applied at an actual inequality

Assume additionally that the full form contains a nonsingular physical zero-diagonal triple `H0` in the scope of the completed designated partner theorem. Write

`L2sq = integral |phi_Q(t)|^2 dt
 <=6 pi 2^(2/3)|det H0|^(-1/3)`.                                (7.1)

From (5.3), dropping the `1` at high frequency gives

`|phi_Q(t)| <= K |t|^(-5/4)`,
`K=(c^5 E5(B))^(-1/8)=(pi e/2)^(5/4) E5(B)^(-1/8)`.             (7.2)

For any `T>0`, Cauchy-Schwarz on `[-T,T]` and (7.2) outside give

`integral |phi_Q|
 <= sqrt(2T L2sq)+8K T^(-1/4)`.                                 (7.3)

Optimizing `T` exactly yields

`integral |phi_Q| <=6 sqrt(2) L2sq^(1/6) K^(2/3)`.              (7.4)

After Fourier inversion and simplification,

`boxed:
 ||p_Q||inf
 <= C04 |det H0|^(-1/18) E5(B)^(-1/12),
 C04=3*6^(1/6)*e^(5/6)*2^(-2/9)
     =7.976817268854006...
}`                                                                  (7.5)

This is an actual new inequality using the designated partner result, not merely a citation.

Combining with (4.3),

`||p_Q||inf
 <= C04 [6r/(r-3)]^(1/12)
    |det H0|^(-1/18) D^(1/3) G^(-1/4).`                         (7.6)

At `r>=4`,

`boxed:
 ||p_Q||inf
 <=10.395545 |det H0|^(-1/18) D^(1/3) G^(-1/4).
}`                                                                  (7.7)

On the r27 `G>Z3/24` endpoint this is `<23.009123 |det H0|^(-1/18)D^(1/3)Z3^(-1/4)`. The density is continuous on this overlap because the fifth-volume branch itself already proves `phi_Q in L1`.

## 8. Deterministic checks

`CHECK.py` and captured `CHECKS.txt` in this run directory perform two regression checks; they are not substitutes for the symbolic proof.

* 500 random physical block matrices verify the exact anchored identity `G5_anchor=D^2 E3(S)` with maximum relative numerical error `5.97e-15`.
* 1,183 generated spectra with stable rank `>3` verify (4.2); minimum observed slack was positive (`0.0654`), with the smallest ratio `E3/lower_bound` about `1.1515`.
* Constants independently recomputed: `C5=6.7701210560`, stable-rank-four direct constant `9.3028829900`, partner hybrid constant `7.9768172689`, stable-rank-four partner constant `10.3955446218`.

## 9. What changed and what remains

Before this run, r27 reduced a transport failure to the double-anchor packet

`G=||det(P)M-C adj(P)R||F^2`

or a singular two-star packet, but there was no integrated-Fourier receiver for a general nonlocal Frobenius Schur residual.

This run proves that for `det P!=0` the whole third compound of the cross-Schur residual embeds exactly into a physical fifth-volume of the original cross block. Therefore every such packet with `sr(S)>3` has an explicit L1 Fourier estimate; in particular `sr(S)>=4` is paid quantitatively. The remaining invertible-pair obstruction is now the low-effective-rank cross-Schur regime, not arbitrary Frobenius geometry. The `det P=0` two-star packet and the two one-sided anchor/strip hybrids also remain.

Next mechanism: `QFORM-DOUBLEANCHOR-LOWRANK-GROUPEDHUB-v1` — use the failure inequality (6.1) to extract a grouped cross direction and combine it with the completed grouped-hub Pluecker smoothing theorem while retaining arbitrary opposite-bank curvature. If the opposite curvature cannot be put in the theorem's diagonal-plus-low-rank form, record that exact incompatibility rather than deleting it.

The full universal QFORM conjecture remains OPEN. No target-valid counterexample to a universal target-wide unweighted `integral |phi_Q|` bound is produced here.