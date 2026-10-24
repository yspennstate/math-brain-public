SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T03:09:32Z.
attacking: projection-product overlap by conditioning genuinely overlapping original coordinates while preserving independent pure line and plane source banks.

# Early substantive checkpoint — conditional overlap transducer

Status: supporting exact-rank-three implication; full QFORM remains OPEN; continuity not claimed for the first certificate.

## Setup
Let A=RBR^T have exact rank three, R^TR=I_3, and every eigenvalue of the symmetric 3x3 matrix B have modulus at least one. Fix a spectral unit vector e and split ORIGINAL coordinates into disjoint sets I,J,K such that rows r_i of R obey r_i in span(e) for i in I, r_j in e^perp for j in J, while rows in K are arbitrary and may overlap both spectral pieces.

Choose e=e_1 and write r_i=(a_i,0,0) on I and r_j=(0,y_j) on J. Put

alpha=sum_{i in I} a_i^2,
G=sum_{j in J} y_j y_j^T,
m=min(alpha, lambda_min(G)).

Assume m>0. Define normalized original-product projections

S=alpha^{-1/2} sum_I a_i X_i,
Y=G^{-1/2} sum_J y_j X_j.

Then S and the whole pair Y are independent because I,J are disjoint original-coordinate banks. Their normalized coefficient systems have Gram 1 and I_2 respectively, so the product-projection bounds used in account02/B16 r23 give ||p_S||_infty<=sqrt(2) and ||p_Y||_infty<=2.

## Conditional use of the designated partner
Condition on X_K=x_K and let z_K=R_K^T x_K. With D=diag(sqrt(alpha),G^{1/2}) and xi=(S,Y),

Q | X_K=x_K = (D xi+z_K)^T B(D xi+z_K).

Because D is invertible, eta=D^{-1}z_K and C=DBD give

Q | X_K=x_K = (xi+eta)^T C(xi+eta).

The translation xi -> xi+eta preserves the independence of the scalar bank from the whole planar bank and preserves the one- and two-dimensional density caps: explicitly any scalar shift is obtained by deterministically translating the independent coordinates in I along their normalized coefficient vector, and any planar shift is obtained by deterministically translating the coordinates in J along the two orthonormal projection columns. Thus the translated conditional law is still exactly in the source-valid class of account02/B16 r23, not merely an arbitrary bounded joint projection.

Moreover

s_min(C)>=s_min(D)^2 s_min(B)>=m.

Hence C0=C/m is symmetric with all three eigenvalue moduli at least one. Apply account02/B16 r23, QFORM-DISJOINT-SPECTRAL-LINE-PLANE-44-v1, to (xi+eta)^T C0(xi+eta). It gives an essential density bound <44. Scaling the scalar output back by m gives, uniformly in x_K,

||p_{Q | X_K=x_K}||_infty < 44/m.

Averaging conditional densities yields the new implication

||p_Q||_infty < 44 / min(alpha,lambda_min(G)).

This pays arbitrary laws and arbitrary spectral overlap on K as long as a quantitative pure line bank and a quantitative pure planar bank survive. It uses no conditional projection-density cap and no post-rotation independence.

## Equation-level use of the newest volume theorem
Let D0=I union J and M=A[K,D0]. When G_K:=R_K^TR_K and G_D:=R_D0^TR_D0 are positive definite,

G_D=diag(alpha,G),
G_K=I_3-G_D=diag(1-alpha,I_2-G).

Factor R_K=U_K G_K^{1/2}, R_D0=U_D G_D^{1/2} with U_K,U_D having orthonormal columns. Then

M=U_K (G_K^{1/2} B G_D^{1/2}) U_D^T,

so, because rank(M)=3,

Z:=e_3(M^TM)=det(G_K) det(G_D) det(B)^2
 = alpha(1-alpha) det(G) det(I_2-G) det(B)^2.

For a rank-three M, its row volume marginal is exactly the leverage of its row range, hence for k in K

alpha_k^(vol)=r_k^T G_K^{-1} r_k.

Therefore, if max_{k in K} r_k^T G_K^{-1}r_k <=1/2, the q=1 case of the newest fractional-volume theorem at math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba gives a continuous density and

||p_Q||_infty <=3e Z^{-1/6}
 <=3e [alpha(1-alpha) det(G) det(I_2-G)]^{-1/6},

using |det B|>=1. This is a second, genuinely overlap-sensitive certificate on the same partition and retains all within-bank quadratic terms automatically.

## Remaining debt
Neither certificate is uniform if the pure line mass alpha or the least pure-plane Gram eigenvalue tends to zero; the volume certificate also requires a diffuse overlap bank. Thus the genuinely unpaid structural case is pure-bank depletion together with a high-leverage overlap bank. This is narrower than the previous statement that all overlapping leakage is unpaid, but it does not solve exact rank three or the full arbitrary-spectrum theorem.

Sources actually used:
- account02/B16 r23: yspennstate/math-open-problems@7044d3cf479cc067d97a317cf67b41121cc48aab, proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T023136Z-account02-B16-QFORM-r23/REPORT.md.
- newest fractional-volume theorem: yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba, proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md.
- source control at run start: yspennstate/math-research-brain@5b676f62db748a3615134619fc9978a22e796744, OWNER CONTROL revision 2026-09-22.15.
