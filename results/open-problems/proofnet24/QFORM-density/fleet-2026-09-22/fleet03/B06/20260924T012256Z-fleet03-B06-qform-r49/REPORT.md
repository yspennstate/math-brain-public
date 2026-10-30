SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-24T01:22:56Z.
attacking: the singular-T nonresonant shear-flat branch; pivot one physical outer hub, keep the full original-product two-frame, and turn the exact post-pivot rank-two coefficient determinant into aggregate cross-block curvature before any reciprocal minor.

# fleet03/B06 r49 — two-pivot aggregation for the singular shear coefficient

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control read at start: revision `2026-09-22.15`; programme revision `2026-09-22.5`  
Assignment: curved fiber integration / quantitative inequalities and rigorous computations  
Status: `NEW TARGET-LEVEL CONDITIONAL RECEIVER + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains OPEN. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation-independence assumption is added. Every pivot and conditioning step uses literal original coordinates.

## 1. Starting point

Use the r47/r48 physical two-hub shear-flat decomposition
\[
A=\begin{pmatrix}H&E\\E^T&C\end{pmatrix},
\qquad
H=\begin{pmatrix}a&c\\c&d\end{pmatrix},
\qquad
\delta=\det H\ne0,
\]
where the first two coordinates are literal independent input coordinates and the environment bank is also in the original coordinate basis. Write
\[
C-E^TH^{-1}E=D+E^TTE,
\]
with `D` diagonal and `E` a real `2 x m` matrix of row rank two. Thus
\[
C=D+E^TUE,\qquad U:=H^{-1}+T.
\]
The r48 unresolved singular endpoint is
\[
T=\lambda vv^T,\qquad \lambda\ne0,\qquad \|v\|_2=1.
\]
Put
\[
G=EE^T,\qquad W=\det G>0.
\]

For the columns `e_j` of `E`, define the normalized squared pair-area law
\[
\mu(\{j,k\})=\frac{\det(e_j,e_k)^2}{W}.
\]
Let `P,Q` be iid with law `mu` and
\[
\Omega=\Pr(P\cap Q=\varnothing).
\]

The purpose of this run is to avoid the bad move “choose a favorable physical minor, invert it, then average.” We first spend the whole pair-area law, and only then choose one of the two literal outer scalar pivots.

## 2. Exact one-pivot coefficient matrices

Let `q_1=(1,0)^T`, `q_2=(0,1)^T`. For each `s` with `h_ss:=H_ss !=0`, complete the square in the literal outer coordinate `X_s`. After conditioning on the other outer coordinate, the environment quadratic coefficient is
\[
D+E^TR_sE,\qquad
R_s:=U-h_{ss}^{-1}q_sq_s^T.
\]
The other outer coordinate contributes only an affine term in the environment after this conditioning, so the completed rank-two cross-block half-Riesz theorem may be applied once a rank-two environment cross block is obtained.

A direct `2 x 2` calculation gives the new exact identities
\[
\boxed{\det R_1=\frac{\lambda\,(Hv)_1^2}{a\,\delta}}
\quad(a\ne0),
\]
and
\[
\boxed{\det R_2=\frac{\lambda\,(Hv)_2^2}{d\,\delta}}
\quad(d\ne0).
\]
Indeed
\[
H^{-1}=\frac1\delta
\begin{pmatrix}d&-c\\-c&a\end{pmatrix},
\]
and the determinant of the sum of the rank-one Schur direction and `lambda vv^T` is the product of their coefficients times the squared exterior product.

Define the aggregate physical-pivot currency
\[
\boxed{
\Xi_H(v):=
\sum_{s:\,h_{ss}\ne0}|h_{ss}|\,|(Hv)_s|^2.
}
\]
Then
\[
\boxed{
\sum_{s:\,h_{ss}\ne0}
h_{ss}^2\,|\det R_s|
=
\frac{|\lambda|}{|\delta|}\,\Xi_H(v).
}
\tag{2.1}
\]
This is the first essential new identity. The outer pivot magnitude and the post-pivot rank-two determinant are aggregated in exactly the combination that appears in the scalar-pivot density theorem.

## 3. Spend the whole pair-area law before choosing the pivot

For a fair random physical bipartition `I | J` of the environment coordinates, the already-proved pair-area identity is
\[
\mathbb E\!\left[
\det(E_IE_I^T)\det(E_JE_J^T)
\right]
=
\frac{W^2}{16}\Omega.
\]
Hence if
\[
\Omega\ge\frac1{256},
\]
there is one deterministic physical cut `I | J` for which
\[
F:=\sqrt{\det(E_IE_I^T)\det(E_JE_J^T)}
\ge \frac{W}{64}.
\tag{3.1}
\]
Importantly, this same cut works for both candidate outer pivots `s`.

For pivot `s`, the environment cross block on this cut is
\[
N_s=E_I^TR_sE_J.
\]
Whenever `det R_s !=0`, Cauchy--Binet gives the exact rank-two singular-product identity
\[
\Delta_s:=\sigma_1(N_s)\sigma_2(N_s)
=
|\det R_s|\,F.
\tag{3.2}
\]
Combining (2.1), (3.1), and (3.2),
\[
\sum_s h_{ss}^2\Delta_s
=
F\frac{|\lambda|}{|\delta|}\Xi_H(v)
\ge
\frac{|\lambda|\,W\,\Xi_H(v)}{64|\delta|}.
\]
There are at most two admissible scalar pivots, so if `Xi_H(v)>0` some `s` satisfies
\[
\boxed{
h_{ss}^2\Delta_s
\ge
\frac{|\lambda|\,W\,\Xi_H(v)}{128|\delta|}.
}
\tag{3.3}
\]

This is the desired weighted replacement for selecting a curved-fiber maximum: the product structure is spent through the complete determinant-squared pair law before the reciprocal rank-two quantity is invoked.

## 4. Target-level conditional density theorem

The completed theorem `QFORM-RANK2-CROSS-SCALAR-PIVOT-v1` states that if a literal original-coordinate scalar pivot has coefficient `b !=0` and its exact Schur residual admits an original-coordinate cut with rank-two cross singular product `Delta`, then arbitrary same-side quadratic curvature and arbitrary affine terms are allowed and
\[
\|p_Q\|_\infty
\le
8\,|b|^{-1/2}\Delta^{-1/4}.
\tag{4.1}
\]

Apply (4.1) to the pivot supplied by (3.3). Since
\[
|h_{ss}|^{-1/2}\Delta_s^{-1/4}
=(h_{ss}^2\Delta_s)^{-1/4},
\]
we obtain the new theorem:

### Theorem — `QFORM-RANK1T-TWOPIVOT-AGGREGATE-v1`

Under the setup above, assume
\[
\Omega\ge\frac1{256},
\qquad
\Xi_H(v)>0.
\]
Then the complete ambient quadratic form, with the other outer hub, every diagonal same-bank term, all same-side environment curvature, all affine terms, and the full nonzero tail retained, has an absolutely continuous law satisfying
\[
\boxed{
\|p_Q\|_\infty
\le
8\left[
\frac{128|\delta|}
{|\lambda|\,\det(EE^T)\,\Xi_H(v)}
\right]^{1/4}.
}
\tag{4.2}
\]
Numerically the prefactor after extracting the `128` is
\[
8\cdot128^{1/4}
=
26.908685288118864\ldots .
\]

No continuity conclusion is claimed from (4.2), because the scalar-pivot/cross-half-Riesz receiver presently supplies absolute continuity and an essential bound.

### Uniform diagonal-nondegeneracy corollary

If both physical diagonal entries satisfy
\[
|a|,|d|\ge\tau>0,
\]
then
\[
\Xi_H(v)
\ge
\tau\|Hv\|_2^2
\ge
\tau\,\sigma_{\min}(H)^2,
\]
and therefore
\[
\boxed{
\|p_Q\|_\infty
\le
8\left[
\frac{128|\det H|}
{|\lambda|\,\det(EE^T)\,\tau\,\sigma_{\min}(H)^2}
\right]^{1/4}.
}
\tag{4.3}
\]
Thus the singular-`T` branch is paid whenever the two-frame is pair-diffuse and the literal outer pair is not itself approaching the zero-diagonal/tangency face.

## 5. Exact description of the remaining pivot obstruction

The only way `Xi_H(v)=0` can occur is highly structured.

* If both `a` and `d` are nonzero, then `Xi_H(v)=0` implies `Hv=0`, impossible because `H` is invertible.
* If exactly one diagonal is nonzero, say `a !=0,d=0`, then `Xi_H(v)=0` is exactly `(Hv)_1=a v_1+c v_2=0`. The only available nonzero scalar diagonal pivot is therefore tangent to the rank-one `T` direction.
* If `a=d=0`, then `H=[[0,c],[c,0]]` with `c!=0`, a literal pure hyperbolic physical pair.

Hence r49 reduces the singular-`T` difficulty to two explicit alternatives: low pair-law disjointness `Omega<1/256`, which by the completed pair-law theorem forces a literal environment leverage hub `>3/5`; or the zero-diagonal / one-zero-diagonal tangency face `Xi_H(v)=0`. Neither is silently set to zero or discarded.

## 6. Application of the designated fleet04/B06 result

The freshest completed designated-partner result found at the source refresh is

`yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B06/20260924T001014Z-fleet04-B06-QFORM-r3/REPORT.md`

with theorem `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`.

Suppose the same environment frame is diffuse in the literal coordinate sense
\[
\max_j e_j^TG^{-1}e_j\le\frac12.
\tag{6.1}
\]
Whiten `E`: `F=G^{-1/2}E`. Its two rows are orthonormal and every column has squared norm at most `1/2`. For the actual pivot `s` selected above, diagonalize the symmetric coefficient `M_s:=G^{1/2}R_sG^{1/2}` inside this two-dimensional coefficient plane. The resulting two row vectors `w,v` are orthonormal in the original product bank and still satisfy `w_j^2+v_j^2<=1/2`.

Thus the partner theorem applies to either nonzero eigenvalue `rho_s` of `M_s`. After the determinant-one output shear that removes the other tangential coordinate, and away from the actual fold by `r=1/64`, its concrete bound is
\[
\boxed{
\|g_{\rm off}\|_\infty
\le
\frac{256}{|\rho_s|}.
}
\tag{6.2}
\]
This is a continuous `C_0` two-output off-fold estimate and is uniform in all same-plane shared linear leakage. It is an actual application to the r49 post-pivot coefficient plane. I do **not** promote (6.2) to a density bound for the full scalar form, because the diagonal same-bank term `D` is outside the partner theorem's scope. The full scalar payment in the diffuse branch is instead (4.2).

Note also that (6.1) excludes the low-disjointness alternative: the completed pair-law theorem says `Omega<1/256` forces a leverage `>3/5`. Hence under (6.1), the pair-area hypothesis needed for (4.2) holds automatically.

## 7. Checks

A finite checker was run on 10,000 random invertible symmetric `2 x 2` matrices and random unit vectors. The maximum normalized discrepancies in the two determinant identities were below `4e-14`. This is only a sanity check; the proof above is exact algebra.

## 8. What remains

The full QFORM conjecture is still OPEN.

The next exact B06 debt is `QFORM-RANK1T-ZERODIAG-TANGENCY-OR-HEAVYHUB-v1`: retain the complete product bank, the rank-one `T` direction, the outer hyperbolic pair, diagonal same-bank curvature, and the nonzero tail. Close either the literal leverage-hub branch forced by `Omega<1/256`, or the explicit `Xi_H(v)=0` zero-diagonal/tangent face, using a dependence-safe hyperbolic pair receiver or the designated partner's curved-section mechanism without deleting the same-bank diagonal remainder.

Global continuity remains OPEN. Continuity is obtained only in the separately scoped partner two-output off-fold estimate, not in theorem (4.2).
