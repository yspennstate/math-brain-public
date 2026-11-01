# Two-bank extension: arbitrary within-bank potentials

This extends [the diffuse two-light Fourier receiver](https://github.com/yspennstate/math-open-problems/blob/88488cf951d2c9552608f8d1dd8776f2bcf678d2/proofnet24/QFORM-density/interactive/20260923T205600Z-diffuse-two-light-local-potentials/REPORT.md) by replacing the row-leverage certificate with two independent planar-capped banks. It is a scoped all-target density theorem; an additional quadratic cross term between banks is outside the statement.

Let H be independent of two independent random vectors X_B,X_C. The scalar H has a probability density at most one. Each bank may internally have arbitrary dependence. Define L=L_B+L_C and V=V_B+V_C, where (L_j,V_j) is a linear projection of X_j whose joint probability density g_j is bounded by M_j, j=B,C. Let tau,lambda be nonzero real numbers, and let R_H(H),R_B(X_B),R_C(X_C) be arbitrary measurable real bank-local functions, finite almost surely. Put

Q=2tau H L+lambda V²+R_H(H)+R_B(X_B)+R_C(X_C).

Then Q has a bounded continuous density, with

||p_Q||_infinity <= 3 (M_B M_C)^(1/3) / (|tau| sqrt(|lambda|))^(2/3).    (1)

In particular, arbitrary original-coordinate affine terms and arbitrary **within-bank** quadratic tails are allowed, with no coefficient dependence, provided there is no additional cross-bank term.

Proof. For each Fourier parameter t, push the complex measure exp(itR_j(X_j))dP_{X_j} forward under (L_j,V_j). It has a density g_{j,t} satisfying |g_{j,t}|<=g_j, so ||g_{j,t}||_2<=sqrt(M_j). By independence of the two banks, the two-dimensional light characteristic function after the bank-local phases is the product of the Fourier transforms of g_{B,t} and g_{C,t}. Cauchy–Schwarz and two-dimensional Plancherel give

int_R² | E exp(i yL+i zV+itR_B+itR_C) | dy dz
 <= (2pi)² sqrt(M_BM_C).                                      (2)

This estimate is uniform in t and in the bank-local phases. Fresnel in lambda V² and the cap-one hub integral, exactly as in the linked report, yield

|phi_Q(t)| <= [pi^(3/2) sqrt(M_BM_C)/( |tau|sqrt(|lambda|))] |t|^(-3/2).  (3)

Together with |phi_Q(t)|<=1, integrate the minimum over t and use Fourier inversion to obtain (1).

## Balanced-ratio leakage corollary

Suppose in addition that P=P_B+P_C, with P_B=alpha L_B and P_C=−alpha L_C for an arbitrary real alpha. Then

LP=(L_B+L_C)(alpha L_B−alpha L_C)
   =alpha L_B²−alpha L_C².

Thus for every epsilon, the genuinely mixed-looking leakage 2epsilon LP is the sum of one potential on B and one on C. The theorem applies to

Q=2tau HL+lambda V²+2epsilon LP+R_H(H)+R_B(X_B)+R_C(X_C)

with **the same bound (1), uniform in alpha and epsilon**. All original-coordinate affine terms, hub self-square, and arbitrary further within-bank quadratic terms may be included in the R_j. If M_B,M_C<=2 and tau=lambda=1, the bound is 3·2^(2/3)<4.77.

This exact opposite-ratio relation is the separation gate. A global beta L² adds the cross-bank term 2beta L_B L_C and is outside this corollary unless its cross term is canceled by some other explicitly specified part of the form. The result does not cover arbitrary P rows or arbitrary cross-bank tails.

## Parameter-matched nonopposite ratios

More generally, suppose P_B=alpha_B L_B and P_C=alpha_C L_C, with no requirement that the two ratios be opposite. The exact expansion is

beta L²+2epsilon LP
= (beta+2epsilon alpha_B)L_B²
 + (beta+2epsilon alpha_C)L_C²
 + 2[beta+epsilon(alpha_B+alpha_C)]L_B L_C.

Thus if beta+epsilon(alpha_B+alpha_C)=0, the cross-bank term vanishes and the two remaining squares are bank-local. The theorem applies with the same bound (1), uniform in beta,epsilon,alpha_B,alpha_C subject to this exact cancellation condition. Under the condition the bank coefficients simplify to epsilon(alpha_B−alpha_C) and epsilon(alpha_C−alpha_B), respectively. The factor 2 in the cross coefficient is essential. This condition is sufficient for the bank-local-potential argument; no claim is made when it fails.

## Boundary

The theorem needs only two planar density caps, which can follow from product-source projection theorems when the two bank Gram matrices are robust. It does not assert that every s3(A)>=1 matrix admits this decomposition. A term such as beta(L_B+L_C)² introduces 2beta L_B L_C, and a term 2epsilon LP generally introduces further cross-bank couplings; those are not bank-local phases and are not controlled by (2). The general negative-target overlapping leakage and arbitrary-rank structural bridge remain open.
