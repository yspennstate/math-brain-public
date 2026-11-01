SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B10, 2026-09-23T14:53:37Z.
attacking: punctured true-near-coloop high-leverage collar; compile the weak-compression state into a scale-free aggregate of indefinite physical hub pairs and isolate the only remaining normalized-leverage failures.

# fleet01/B10 — bordered indefinite-pair mass in the punctured near-coloop collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T145337Z-fleet01-B10-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW_EXACT_STRUCTURAL_IDENTITY / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  

The full arbitrary exact-rank-three theorem and the owner-level three-large-eigenvalue conjecture remain **OPEN / NOT PROVED / NOT DISPROVED**. This report proves a new exact signed bordered-pair identity and uses it to show that the genuinely hard punctured near-coloop/near-null chamber carries order-one aggregate **indefinite physical pair determinant mass**, even when the partner spectral compression has determinant tending to zero and every individual local pair can be small. It then localizes failure of the completed diffuse-leaf Schur--Fresnel gate to at most three original longitudinal-heavy coordinates once the already-paid transverse-heavy branch is removed.

## 1. Exact-rank-three setup

Write

\[
A=UMU^T,\qquad U^TU=I_3,
\]

where `M` is real symmetric and every eigenvalue of `M` has absolute value at least one. Put

\[
D:=|\det M|\ge1.
\]

Choose an **original physical coordinate** `0` with spectral row

\[
u_0=\sqrt h\,r,\qquad \|r\|=1,
\]

and write the remaining rows as `u_i`, `i>0`. Thus

\[
G_L:=\sum_{i>0}u_i u_i^T=I-hrr^T.
\tag{1.1}
\]

Set

\[
a:=r^TMr,\qquad m:=Mr,\qquad s^2:=\|m\|^2=r^TM^2r.
\tag{1.2}
\]

Since every singular value of `M` is at least one,

\[
s^2\ge1.
\tag{1.3}
\]

Also, because the other two singular values are at least one,

\[
\|M\|_{op}\le D,
\qquad
|\operatorname{tr}M|\le3D.
\tag{1.4}
\]

The live true-collar reduction has `h>63/64` and a small normalized hub Rayleigh quotient. The newest designated partner fleet02/B10 supplies the nonzero-pivot payment used in Section 5 below.

## 2. New exact signed bordered-pair identity

For `i>0`, let

\[
\Delta_i:=\det A[\{0,i\}]
=A_{00}A_{ii}-A_{0i}^2.
\]

Because

\[
A_{00}=ha,
\qquad
A_{0i}=\sqrt h\,m^Tu_i,
\qquad
A_{ii}=u_i^TMu_i,
\]

we have

\[
\Delta_i
=h\left(a\,u_i^TMu_i-(m^Tu_i)^2\right).
\tag{2.1}
\]

Summing and using (1.1),

\[
\sum_{i>0}u_i^TMu_i
=\operatorname{tr}(MG_L)
=\operatorname{tr}M-ha,
\tag{2.2}
\]

while

\[
\sum_{i>0}(m^Tu_i)^2
=m^TG_Lm
=s^2-ha^2.
\tag{2.3}
\]

The `ha^2` terms cancel exactly. Therefore

\[
\boxed{
\sum_{i>0}\det A[\{0,i\}]
=h\left(a\operatorname{tr}M-s^2\right).
}
\tag{2.4}
\]

This is the main new identity of the run. It is an exact physical-coordinate statement and uses no probabilistic rotation.

### Transverse form of each summand

Write

\[
u_i=\alpha_i r+z_i,\qquad z_i\perp r,
\]

and put

\[
g:=P_{r^\perp}Mr,
\qquad
q_i:=z_i^TMz_i.
\]

Then `m^Tu_i=\alpha_i a+g^Tz_i` and a direct expansion in (2.1) cancels all longitudinal `\alpha_i` terms, giving

\[
\boxed{
\Delta_i=h\left(aq_i-(g^Tz_i)^2\right).
}
\tag{2.5}
\]

Thus the bordered physical-pair determinant is controlled entirely by the transverse row and the true hub cross field; longitudinal leakage does not appear in an individual determinant after the exact cancellation.

## 3. Scale-free indefinite-pair mass in the punctured ultra-collar

Assume now the partner-survivor inequality

\[
|a|D<2^{-12}.
\tag{3.1}
\]

From (1.3), (1.4), and (2.4),

\[
\sum_{i>0}\Delta_i
\le
h\left(3|a|D-1\right)
<
-h\left(1-\frac3{4096}\right).
\tag{3.2}
\]

In the true near-coloop collar `h>63/64`, define

\[
c_*:=\frac{63}{64}\frac{4093}{4096}
=\frac{257859}{262144}
=0.983654022216796875.
\tag{3.3}
\]

Then

\[
\boxed{
\sum_{i>0}\Delta_i<-c_*.
}
\tag{3.4}
\]

Let

\[
N_-:=\sum_{i:\Delta_i<0}|\Delta_i|
\]

be the total determinant mass of **indefinite** physical hub--leaf pairs. Since a real symmetric `2x2` matrix has negative determinant exactly when it is indefinite, writing the positive determinant mass as `N_+` gives

\[
N_+-N_- =\sum_i\Delta_i<-c_*.
\]

Hence

\[
\boxed{
N_->c_*>0.983654.
}
\tag{3.5}
\]

This conclusion is dimension-free and does not require one large local pair. In particular, the remaining weak-compression chamber cannot lose its hyperbolic curvature: it may fragment that curvature over arbitrarily many physical pairs, but the total indefinite pair determinant mass stays order one.

### Product-preserving local-or-two-bank split

The weights `w_i:=|\Delta_i|1_{\{\Delta_i<0\}}` are attached to original coordinates. From (3.5), either

\[
\max_i w_i\ge c_*/4,
\tag{3.6}
\]

or there is a partition of the negatively weighted leaf indices into two disjoint original-coordinate banks `J,K` such that

\[
\boxed{
\sum_{i\in J}w_i\ge c_*/4,
\qquad
\sum_{i\in K}w_i\ge c_*/4.
}
\tag{3.7}
\]

Indeed, in the absence of (3.6), greedily add weights to `J` until the first time its mass reaches `c_*/4`; its mass is then `<c_*/2`, leaving `>c_*/2` for `K`. The two banks preserve original-coordinate product provenance. Equation (3.7) is only a structural compiler; because the live `QFORM-NONZERO-MUTUAL-EDGE-TWO-SLOPE-INSUFFICIENT-v1` correction shows that two-slope currency alone can still collapse to a rank-two product singularity, a valid receiver must also spend the third rank-three resource below.

## 4. Exact bordered triple-volume identities

The following identities are source-compatible with the completed fixed-pair Pluecker calculations and are included here because they combine sharply with (3.5).

For every physical triple `I`,

\[
\det A[I]
=\det(U_I M U_I^T)
=\det M\,\det(U_I)^2.
\tag{4.1}
\]

Hence all nonzero principal `3x3` determinants have the same sign and

\[
\sum_{|I|=3}|\det A[I]|=D
\tag{4.2}
\]

by Cauchy--Binet.

Let `z_i=P_{r^\perp}u_i`. Projecting (1.1) to `r^\perp` gives

\[
\sum_{i>0}z_i z_i^T=I_{r^\perp}.
\tag{4.3}
\]

For triples containing the hub,

\[
\det(u_0,u_i,u_j)^2
=h\det(z_i,z_j)^2.
\]

A second Cauchy--Binet application in the transverse plane therefore gives

\[
\boxed{
\sum_{1\le i<j}|\det A[\{0,i,j\}]|=Dh.
}
\tag{4.4}
\]

Consequently the hub-free triple mass is exactly

\[
\boxed{
\sum_{1\le i<j<k}|\det A[\{i,j,k\}]|=D(1-h).
}
\tag{4.5}
\]

For one fixed leaf `i`, the two-dimensional Parseval identity

\[
\sum_{j>0}\det(z_i,z_j)^2=\|z_i\|^2
\]

gives

\[
\boxed{
\sum_{j>0,\,j\ne i}|\det A[\{0,i,j\}]|
=Dh\,\|z_i\|^2.
}
\tag{4.6}
\]

Thus as `h\uparrow1`, essentially all principal three-volume is **bordered by the same physical hub**, while the hub-free volume collapses. This is why a proof based only on hub-free triples necessarily deteriorates in the true near-coloop limit.

## 5. Actual application of the designated fleet02/B10 result

The newest completed designated-partner report consumed in this run is

`yspennstate/math-open-problems@f81263344356dd37ef7f6323f863ba48b49f1a34`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260923T132259Z-fleet02-B10-QFORM-5d7c/REPORT.md`.

It proves for the same physical hub that, with

\[
v=\frac{Mr}{\|Mr\|},
\qquad
C_m=M|_{v^\perp},
\]

one has the exact compression determinant

\[
\boxed{
\det C_m=\frac{a\det M}{s^2}.
}
\tag{5.1}
\]

It also supplies the reviewed nonzero-pivot density payment

\[
\|p_Q\|_\infty
\le128[h^2|a|D]^{-1/4}.
\tag{5.2}
\]

Therefore, in the true collar `h>63/64`,

\[
|a|D\ge2^{-12}
\quad\Longrightarrow\quad
\boxed{\|p_Q\|_\infty<1033.}
\tag{5.3}
\]

This is the required application of a completed designated-partner result to an actual inequality. The only punctured near-null branch needing the new structural compiler is therefore (3.1).

On that complementary branch, (5.1) and `s^2\ge1` imply

\[
|\det C_m|<2^{-12},
\tag{5.4}
\]

whereas (3.5) gives simultaneously

\[
N_->0.983654.
\tag{5.5}
\]

So the partner's **weak spectral compression** and the physical bordered-pair geometry are reciprocal in a strong aggregate sense: compression determinant can vanish, but order-one indefinite physical pair mass survives.

## 6. High normalized leaf leverage reduces to at most three longitudinal exceptions

The completed fleet03/B10 `QFORM-NEARNULL-WITT-COMPRESSION-v1` branch pays every leaf whose transverse leverage is at least `1/4` by an essential density bound `<609`. Thus in the still-unpaid true collar we may assume

\[
\tau_i:=\|z_i\|^2<\frac14
\qquad(i>0).
\tag{6.1}
\]

Put

\[
\delta:=1-h.
\]

Because `G_L=\delta rr^T+P_{r^\perp}`, the normalized leaf leverage used by the completed punctured-hub Schur--Fresnel theorem is

\[
\ell_i
:=u_i^TG_L^{-1}u_i
=\frac{\alpha_i^2}{\delta}+\tau_i.
\tag{6.2}
\]

If `\ell_i>1/2`, then (6.1) forces

\[
\frac{\alpha_i^2}{\delta}>rac14.
\tag{6.3}
\]

But

\[
\sum_{i>0}\alpha_i^2
=r^TG_Lr
=\delta.
\tag{6.4}
\]

Therefore there are at most three strict violations of the diffuse gate:

\[
\boxed{
\#\{i>0:\ell_i>1/2\}\le3.
}
\tag{6.5}
\]

This is an original-coordinate localization statement. No spectral random variable is rotated or declared independent.

The previous fleet01/B10 theorem `QFORM-PUNCTURED-HUB-SCHUR-FRESNEL-v1` says that if there are **no** such violations then `Q` has a continuous density and

\[
\|p_Q\|_\infty\le12[D(1-h)]^{-1/3}.
\tag{6.6}
\]

Hence

\[
D(1-h)\ge2^{-9}
\quad\Longrightarrow\quad
\boxed{\|p_Q\|_\infty\le96}
\tag{6.7}
\]

on the fully diffuse punctured branch.

Combining all current payments, the hard nonzero true-near-coloop state can now be restricted to

\[
0<|a|D<2^{-12},
\qquad
h>63/64,
\tag{6.8}
\]

all transverse row leverages `<1/4`, together with one of only two mechanisms:

1. **diffuse ultra-volume:** every `\ell_i\le1/2` but `D(1-h)<2^{-9}`; or
2. **finite longitudinal core:** between one and three original rows violate `\ell_i\le1/2`.

Both mechanisms simultaneously retain the order-one indefinite bordered-pair mass (3.5) and the exact bordered three-volume (4.4).

## 7. Why this does not yet close the collar

It is not valid to infer one uniformly good local scalar/pair/triple from the aggregate masses above. The designated partner's fragmented family and the live local-minor corrections show that all individual local determinants can be small while the aggregate remains order one. It is also not valid to use only the two-bank split (3.7): a live source-valid correction exhibits an aligned rank-two product singularity with two strong slopes and a nonzero mutual edge. A correct receiver must spend the **third rank-three resource** before that collapse.

The correct next obligation is therefore

`QFORM-BORDERED-INDEFINITE-MASS-THIRD-RESOURCE-RECEIVER-v1`:

> In the punctured true-near-coloop state (6.8), use the order-one aggregate mass of negative hub--leaf `2x2` determinants together with the bordered principal-triple mass `Dh` and the original product provenance to obtain a dimension-free density bound. The receiver must remain valid under fragmentation and, in the high-normalized-leverage subbranch, must tolerate at most three longitudinal-heavy literal original coordinates. It may not replace the leaf banks by dependent spectral coordinates or delete the small nonzero hub square.

This is a strictly narrower target than the previous generic high-leverage collar: weak compression is now accompanied by a quantified order-one physical hyperbolic packet, transverse-heavy leaves are already paid, and any remaining failure of the diffuse Schur--Fresnel gate is finite-dimensional on the original-coordinate side.

## 8. Continuity and status

- Partner branch (5.3): essential boundedness is used; no new continuity upgrade is asserted here.
- Diffuse branch (6.6): the cited Schur--Fresnel theorem gives a continuous `C_0` density.
- New bordered-mass compiler (Sections 2--6): structural only; it proves no density continuity by itself.
- Full exact-rank-three theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full owner QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.

## 9. Verification note

The proof of (2.4), (4.4), and (4.6) is exact algebra. As a regression check only, 1000 random Parseval `n x 3` frames and random symmetric `M` with all eigenvalue magnitudes at least one gave maximum floating-point errors

- signed pair-sum identity (2.4): `1.07e-14`;
- total hub-triple identity (4.4): `5.68e-14`;
- fixed-leaf triple packet (4.6): `2.84e-14`.

The regression is not part of the proof.
