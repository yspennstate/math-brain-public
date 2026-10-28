SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B08, 2026-09-23T09:14:14Z.
attacking: quantify the localized/diffuse hybrid on one original-coordinate matrix, compare volume and ridge certificates there, and build an exact grouped receiver for the huge-rank-one/fixed-E2 survivor.

# account04/B08 — anisotropic fixed-E2 direct-sum receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T091414Z-account04-B08-QFORM-r1`  
Status: `ESSENTIAL_STEP_APPLIED / PROVED_SCOPED_TARGET_THEOREM / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; repository publication is not native ingestion.

The unrestricted conjecture remains OPEN. The theorem below closes an exact original-coordinate model of the newest B08 “huge rank-one core plus fixed second-exterior currency” survivor. It does not absorb arbitrary same-bank leakage, arbitrary orthogonal twists, or arbitrary additional-spectrum interaction. Continuity is not asserted.


## 1. Sources used at equations

1. account01/B08 sharp floating transfer:
   `yspennstate/math-open-problems@584a2e98e85d49638590c24d2669e6589f2c625d`,
   theorem `QFORM-FLOATING-SHARP-CURVATURE-LADDER-v1`.
   Its clean diffuse router applies when a selected three-eigenvector frame has leverage `mu<=1/3`, giving actual child scale
   [
   c_0=0.158918622597891L,qquad b_0=0.0505102572168219L.
   ]
   The model below has selected-three leverage exactly one, so this diffuse exit is genuinely unavailable: it belongs to the localized/hybrid side, not to the diffuse branch.

2. account01/B08 same-matrix ridge/volume comparison:
   `yspennstate/math-open-problems@cce617dcecf1c8677c12fc9d8add83a221281386`,
   especially the scale-independent ridge obstruction and the warning that canonical volume marginals can be one.

3. account01/B08 robust recoloring:
   `yspennstate/math-open-problems@be091d613a838de2098ba9f266da080f7f4434af`,
   theorem `QFORM-RECOLOR-E3-OR-ORIGINAL-E2-v1`. Its surviving currency is
   [
   s_1(B)s_2(B)ge (1-delta)c^2,qquad E_2(B)ge(1-delta)^2c^4.
   ]
   The model below realizes the difficult anisotropic endpoint exactly:
   [
   s_1(H_R)s_2(H_R)=1,qquad E_2(H_R)=1,qquad s_1(H_R)/s_2(H_R)=R^2	oinfty .
   ]

4. The exact grouped rank-two receiver quoted and applied in account01/B08 r19 is the completed account02/B08 theorem
   `QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1`,
   canonical source `yspennstate/math-open-problems@c248abc9be918698c6d5a68108c615ba1c4790b3`.
   With a genuine outer square of coefficient (a) and incident rank-two volume (Delta), it gives
   [
   |p_Q|_inftyle C_{m grp}|a|^{-1/2}Delta^{-1/8},
   quad
   C_{m grp}=(2^{4/3}+1)sqrt3,2^{1/4}=7.250055108887958ldots .
   ]

## 2. One target-valid matrix carrying the extreme hybrid

For (Rge3), set
[
H_R=egin{pmatrix}R&0\0&R^{-1}end{pmatrix}
]
and, in the original coordinate order ((x_0,u_1,u_2,v_1,v_2)),
[
A_R=
egin{pmatrix}
1&0&0&0&0\
0&0&0&R&0\
0&0&0&0&R^{-1}\
0&R&0&0&0\
0&0&R^{-1}&0&0
end{pmatrix}.
]
For arbitrary independent real variables with probability densities at most one,
[
Q_R=X_0^2+2R,U_1V_1+2R^{-1}U_2V_2.
]

The spectrum is exactly
[
operatorname{spec}(A_R)={1,R,-R,R^{-1},-R^{-1}}.
]
Hence (A_R) is target-admissible for every (Rge1): the eigenvalues (1,R,-R) have modulus at least one. No law, support, or moment hypothesis is added.

The cross block has
[
s_1(H_R)=R,qquad s_2(H_R)=R^{-1},qquad
E_2(H_R)=det(H_R)^2=1.
]
Thus (R	oinfty) is precisely a huge rank-one core with a vanishing second singular value but fixed second-exterior mass.

## 3. All raw ridge and canonical volume certificates fail on this same matrix

### 3.1 Ridge failure at every regularization scale

For any ridge scale (ho>0),
[
K_ho=H_RH_R^T(ho^2I+H_RH_R^T)^{-1}
      =operatorname{diag}(k_1,k_2),
]
where
[
k_1=rac{R^2}{ho^2+R^2},qquad
k_2=rac{R^{-2}}{ho^2+R^{-2}},qquad 0<k_2le k_1.
]
The completed ridge criterion requires some (q) with
[
max_i(K_ho)_{ii}le q/2,qquad operatorname{tr}K_ho>2q.
]
The first inequality forces (qge2k_1), whereas
[
operatorname{tr}K_ho=k_1+k_2le2k_1le q<2q.
]
Contradiction. Therefore no one-scale ridge certificate works, for any (ho).

This is an actual application of the account01/B08 same-matrix comparison: the obstruction is not tied to the old test scale (1/16); it is scale-independent.

### 3.2 Rank-three volume failure

The block (H_R) has rank two, so (E_3(H_R)=0). Every rank-three volume theorem is unavailable.

### 3.3 Fractional rank-two volume-gate failure

There is exactly one nonzero (2	imes2) minor, with squared volume one. The canonical order-two volume distribution is therefore a point mass, and every physical row and column marginal equals one. The fractional (E_2) gate would require
[
	hetaalpha_ilerac12
]
for an admissible (	heta>2/3). Here (alpha_i=1), so it would require (	hetale1/2), impossible.

Consequently, on the very same original-coordinate matrix,
[
oxed{	ext{ridge fails at every scale,quad canonical }E_3	ext{ fails,quad canonical fractional }E_2	ext{ fails}.}
]

## 4. Nevertheless the full output density is uniformly bounded

Use the genuine original coordinate (X_0) as the outer square, so (a=1). Choose the physical row and column anchors (j=r=1) in (H_R). The double-incident rank-two bank is
[
Delta_{11}(H_R)
=sum_{k
e1, s
e1}
 det H_R[{1,k},{1,s}]^2
=det(H_R)^2
=1.
]
The completed grouped theorem therefore gives, for every (Rge3) and every allowed product input,
[
oxed{
|p_{Q_R}|_infty
le C_{m grp}
=(2^{4/3}+1)sqrt3,2^{1/4}
<7.251 .
}
]
This estimate is uniform as (R	oinfty), even though the anisotropy ratio is (R^2	oinfty), the second singular value tends to zero, and all three raw certificate families above remain unavailable.

The proof is entirely in original coordinates. The outer square and the two cross-bank channels use disjoint coordinate sets, exactly matching the grouped theorem's product provenance. No post-rotation independence is invoked.

## 5. What this pays and what remains

This proves `QFORM-ANISOTROPIC-RANK1-E2-DIRECTSUM-RECEIVER-v1`:

> The exact direct-sum huge-rank-one/fixed-(E_2) family (A_R) is target-admissible and has
> (|p_{X^TA_RX}|_infty<7.251) uniformly in (R), all cap-one coordinate laws, and all tails already present in the displayed matrix.

It also proves that “ridge OR canonical volume” cannot be the final exhaustive B08 dichotomy, even after optimizing the ridge scale: the correct receiver can be a grouped, anchored, anisotropic physical-coordinate estimate invisible to both canonical gates.

This does **not** pay the general account01/B08 survivor. The first unpaid implication is now more precise:

`QFORM-HUGE-RANK1-E2-LEAKAGE-STABLE-RECEIVER-v1`.

One must retain the above uniform grouped payment when the two arm banks carry arbitrary same-side quadratic terms and arbitrary additional cross/tail couplings. Those terms cannot simply be discarded because the input laws have no moments or bounded support. A valid extension must integrate them jointly with the exact anchor and the (E_2) channel, or route them to an independently paid curvature certificate.

Full QFORM remains OPEN. Continuity remains unproved for this grouped (L^3)-plus-square route.
