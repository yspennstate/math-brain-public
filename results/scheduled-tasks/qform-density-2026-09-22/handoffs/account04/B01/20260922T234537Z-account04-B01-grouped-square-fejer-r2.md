# account04/B01 handoff — disjoint grouped square innovations

Outcome: `SUPPORTING_TARGET-LEVEL_THEOREM / ESSENTIAL_STEP_APPLIED`; full QFORM remains `OPEN`; execution `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics: `yspennstate/math-open-problems@88003dc06af684cc4bc178a7dfe8e7cbebb0f987`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T234537Z-account04-B01-grouped-square-fejer-r2/REPORT.md`, report blob `536d54c0e463cc5a4729d849e4e59e9dcb76c11b`. The file was read back at that commit.

Fresh source boundary: owner revision `2026-09-22.15`; Claude source-directory newest commit `2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926`; assignment blob `0aabfb0233abb7f67e46808b03987c0300502329`; correction blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`; memory protocol blob `0d902d56688f4b5c575f5b921ddf9f6709e88312`.

## New theorem

Partition the original coordinates into (C,B_1,B_2,B_3). Let (L_j=a_j^TX_{B_j}), (sigma_j=|a_j|_2>0), and suppose
[
Q=R(X_C)+sum_{j=1}^3lambda_j(L_j+h_j(X_C))^2.
]
For any same-sign pair (j,k),
[
|p_Q|_inftyle
{2pioversigma_jsigma_ksqrt{|lambda_jlambda_k|}},
qquad p_Qin C_0(mathbb R).
]
Proof: the product-marginal bound gives (|p_{L_j}|_inftylesqrt2/sigma_j); the shifted-square envelope is (M_j/sqrt{|lambda_j|s}); the beta integral for two same-sign squares is (pi); the third independent square and the conditioned scalar remainder do not raise the cap.

The exact signed-Fejer consequence is
[
D_Toperatorname{law}(Q)(y)le
{2pioversigma_jsigma_ksqrt{|lambda_jlambda_k|}}
quadorall T>0, yinmathbb R.
]
No pointwise characteristic-function decay or absolute Fourier integrability is asserted.

## Designated account01/B01 result applied

The account01 completion-defect family at `bf06839b97a3af3f800751cd9bd8502bcf8011d0` has
[
Q_m=(u+v+w)^2+(u+z)^2+(v+	au)^2,qquad
operatorname{spec}_{
e0}(A_m)={4,2,1},
]
while every fixed physical coefficient vanishes as (m	oinfty). Conditioning on the (U,V) banks and applying the new theorem to the disjoint (W,Z,T) innovations gives, for every cap-one product input law,
[
|p_{Q_m}|_inftyle2pi,qquad p_{Q_m}in C_0,qquad
D_Toperatorname{law}(Q_m)(y)le2pi.
]
This removes the partner report's Gaussian-only restriction on the positive payment and confirms that aggregation must precede coordinate selection.

Remaining gap: a general no-pivot matrix need not provide disjoint grouped innovations; self-curvature and overlapping innovation maps remain unpaid. A structural disjointification theorem or an overlapping-source replacement is still needed.
