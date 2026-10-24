# QFORM proof closure: conditional diffuse-range extraction after heavy-coordinate conditioning

**Run:** `20260922T141640Z-account04-B20-QFORM-r2`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## Target and sources

The target is the unrestricted statement for independent real coordinates with densities at most one and every real symmetric matrix having at least three eigenvalues of modulus at least one. No moments, compact support, connected support, log-concavity, or independence after rotation are assumed.

This report applies the completed full-spectrum diffuse-range theorem at
`math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, which gives a continuous density bounded by
[
C_0=rac{96e}{7sqrt2}<27
]
when the entire range projection has coordinate leverage at most (1/32), while allowing arbitrary extra small eigenvalues and arbitrary coordinate-separable phases.

The assigned partner `account01/B20` had no completed current-QFORM artifact in the source snapshot. No result is invented. The completed OTHER-account synthesis actually applied is account01/B19's hard saddle family and near-diagonal theorem, report `proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260922T121338Z-b19-qform-r11/REPORT.md`.

## Theorem: conditioned-whitened diffuse extraction

Let (A) be a real symmetric (n	imes n) matrix of rank (r). Write
[
A=ULambda U^T,qquad U^TU=I_r,
]
where (Lambda) is invertible and has at least three eigenvalues of modulus at least one. Let (H) be any set of original coordinates, (R=H^c), and write (u_i^T) for row (i) of (U). Define
[
S=U_R^TU_R=I_r-U_H^TU_H.
]
Assume (Ssucc0), put (delta=lambda_{min}(S)), and assume the exact residual leverage bound
[
max_{iin R}u_i^TS^{-1}u_ilerac1{32}.
]
Then for every independent input law with one-dimensional densities bounded by one,
[
Q=X^TAX
]
has a continuous density satisfying
[
oxed{|p_Q|_inftyle rac{C_0}{delta}<rac{27}{delta}.}
]

A convenient raw sufficient condition is
[
|U_H^TU_H|_{m op}le1-delta,qquad
max_{iin R}|u_i|_2^2lerac{delta}{32},
]
which implies the exact residual leverage hypothesis and the same conclusion.

### Proof

Condition on (X_H). Independence in the original coordinates is retained on (R). The conditional quadratic is
[
X_R^TA_{RR}X_R+sum_{iin R}b_i(X_H)X_i+c(X_H),
]
so the conditioning creates only a coordinate-separable linear phase and a constant.

Set
[
V=U_RS^{-1/2}.
]
Then (V^TV=I_r), and
[
A_{RR}=V,B,V^T,qquad B=S^{1/2}Lambda S^{1/2}.
]
Thus (V) is an orthonormal frame for the entire residual range. Its row leverage is exactly
[
|e_i^TV|_2^2=u_i^TS^{-1}u_ile1/32.
]

For singular values, the standard product inequality gives, for every (k),
[
s_k(B)ge s_{min}(S^{1/2})^2s_k(Lambda)=delta,s_k(Lambda).
]
Hence (B/delta) has at least three eigenvalues of modulus at least one. Apply the full-spectrum diffuse-range theorem to the conditional form divided by (delta). Its allowed separable phase includes the conditional linear term. The resulting conditional density is continuous and bounded by (C_0/delta), uniformly in (X_H).

Averaging the conditional densities gives a density for (Q) with the same bound. Continuity follows from dominated convergence because every conditional density is continuous and all are dominated by the same constant (C_0/delta).

For the raw criterion, (Ssucceqdelta I), so
[
u_i^TS^{-1}u_ile|u_i|_2^2/deltale1/32.
]
This proves the corollary.

## Actual integration with the hard saddle family

For account01/B19's exact family
[
A_m=Uegin{pmatrix}0&1&0\\1&0&0\\0&0&1end{pmatrix}U^T,
]
the unique physical pivot row has leverage one. With (H=arnothing), the diffuse hypothesis fails. With (H) equal to that pivot coordinate,
[
S=operatorname{diag}(0,1,1),qquaddelta=0.
]
Thus the new theorem diagnoses exactly why simple conditioning cannot close this family: conditioning exhausts one of the three spectral directions. This is not a weakness hidden by constants. The completed aggregate hyperbolic-square theorem instead controls that family by
[
|p_Q|_inftyle2^{11/4}<6.728.
]
Therefore the two mechanisms now form a clean proof split: condition-and-whiten whenever the residual spectral Gram has a positive floor and diffuse leverages; use product-preserving aggregation when heavy conditioning would make that floor vanish.

## What remains

The full conjecture is still open. The first missing exhaustive implication is now precise: given three large spectral directions, prove that either there exists a heavy set (H) satisfying the conditioned-whitened criterion with a universal (delta>0), or extract a disjoint-block aggregate normal form of the hyperbolic-square type (or another already controlled localized form). The hard family shows the second alternative is genuinely necessary.

The theorem proves continuity in its branch. The near-diagonal theorem only asserted an essentially bounded density, and the full target's continuity remains open.
