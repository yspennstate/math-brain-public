SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T20:00:16Z.
attacking: the high-leverage carrier survivor by balancing only the three genuinely large spectral directions and retaining every smaller spectral direction exactly inside the physical cross block.

# Early substantive checkpoint — top-three balance with an arbitrary spectral tail

The full QFORM conjecture remains open. This checkpoint records a new target-level sufficient branch; no small random quadratic error is deleted.

Let the eigenvalues of a real symmetric A be ordered by magnitude, |lambda_1| >= |lambda_2| >= |lambda_3| = a > 0, and let W be the n x 3 orthonormal frame of corresponding eigenvectors. Put

q_3 = max_i ||W_{i,*}||_2^2,

gamma = (1-sqrt(3 q_3))/2,

and write

A = W Lambda W^T + E,
Lambda = diag(lambda_1,lambda_2,lambda_3),
||E||_op = |lambda_4| =: b

(with b=0 if rank(A)<=3). Assume 3q_3<1 and b < gamma a.

A Rademacher physical-coordinate split I|J can be chosen so that

W_I^T W_I >= gamma I_3,
W_J^T W_J >= gamma I_3.

Indeed for physical rows w_i and iid signs eps_i,

F=(1/2) sum_i eps_i w_i w_i^T

satisfies

E ||F||_F^2 = (1/4) sum_i ||w_i||^4 <= (q_3/4) sum_i ||w_i||^2 = 3q_3/4.

Hence one sign choice has ||F||_op <= sqrt(3q_3)/2, giving the two Gram lower bounds.

On this literal original-coordinate cut,

B=A[I,J]=W_I Lambda W_J^T + E[I,J].

The first term has third singular value at least gamma a. Since ||E[I,J]||_op <= ||E||_op=b, Weyl gives

s_3(B) >= gamma a-b =: beta >0.

Now apply the completed physical third-volume theorem `QFORM-PHYSICAL-D3-NO-MARGINAL-GATE-v1` from account01/B20. It requires no volume-marginal hypothesis and retains arbitrary same-side curvature. Since

Z_3=e_3(BB^T) >= s_3(B)^6 >= beta^6,

it gives a continuous C_0 density and

||p_{X^T A X}||_infinity <= C_3/beta,
C_3=3*2^(4/3)*exp(1/3)=10.5501688311...,

and P{X^TAX in L} <= (C_3/beta)|L| for every interval L.

In particular, under the owner target a>=1, if q_3<=1/12 and |lambda_4|<=1/8, then gamma>=1/4 and beta>=1/8, hence

||p||_infinity <84.402.

This branch allows arbitrary rank and arbitrary signs in the spectral tail. The tail is not removed probabilistically; it is retained in B and enters only through the deterministic singular-value perturbation bound.

A stronger rank-one-tail version replaces b by b/2 because for E=b zz^T,
||E[I,J]||=b||z_I||||z_J||<=b/2.

Next: verify this on a genuinely overlapping family with full four-frame leverage equal to one, and apply the designated account02/B09 theorem to a separate concrete target inequality.