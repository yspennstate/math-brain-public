SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-23T00:55:56Z.
attacking: operator-norm stability of the new two-large-directions plus collective-tail Fourier certificate, including the exact obstruction showing why raw collective tail energy cannot itself be stable under an arbitrary dense small-norm perturbation.

# Early substantive checkpoint

Target status at this checkpoint: OPEN.  This note records the first mathematical implication before the final report.

Let I,J be disjoint original-coordinate sets and M0=A0[I,J].  Fix an orthogonal projection P on the I-row space with max_i P_ii<=1/2 and put eps0=||(I-P)M0||op.  Let sigma_j=s_j(M0).  If the actual final cross block is M=M0+R with rho=||R||op, define the thresholded tail reserve

B_rho^2 = sum_{j>=3} (sigma_j-rho)_+^2.

Then Weyl gives, term by term,

s_2(M)>=s_2(M0)-rho,
T2(M):=sum_{j>=3}s_j(M)^2 >= B_rho^2,

while

||(I-P)M||op <= eps0+rho.

Therefore, if rho<s_2(M0), B_rho>0 and eps0+rho<=B_rho/15, the completed collective-tail marginal theorem at math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba applies to the ACTUAL final matrix.  Its q=4/3 estimate gives

||p_Q||inf <= (9 sqrt(3) e/2) [(s_2(M0)-rho)^4 B_rho^2]^(-1/6)
           = (9 sqrt(3) e/2) (s_2(M0)-rho)^(-2/3) B_rho^(-1/3).

The older completed D' theorem in the required Claude package e5f71d79eff325201dd0274053d20268ce65b837 already yields the same implication with the slightly larger coefficient 9 sqrt(3e), once its h=2/3 marginal gate is verified; thus this is an equation-level application of that completed result, not merely a citation.

For a full symmetric perturbation T with ||T||op<=delta plus arbitrary signed spectral additions L=sum_r tau_r v_r v_r^T, the protected cross-block perturbation satisfies

rho <= delta + sum_r |tau_r| ||(v_r)_I||_2 ||(v_r)_J||_2.

Hence added eigenvalues may be arbitrarily large provided their physical footprint on this cross certificate is small.  No assertion is made that X^T T X is a small random variable.

There is a sharp reason to use the thresholded reserve instead of raw baseline T2.  Let m=N+2 be a Hadamard order, U orthogonal with flat entries, d=N^(-1/2), and

M0=U diag(1,1,d,...,d) U^T.

Then baseline T2(M0)=N d^2=1 and the top-two projection has diagonal 2/m, while the dense perturbation

R=-U diag(0,0,d,...,d) U^T

has ||R||op=d->0 but annihilates the entire collective tail: M=M0+R has rank two and T2(M)=0.  Embedding as A=[[0,M],[M,0]] leaves four eigenvalues of modulus one, so even the FINAL matrix remains in the exact QFORM target class.  Thus raw collective-tail energy is not dimension-free stable under small operator norm alone; a thresholded reserve, a local-footprint packet, or another branch is genuinely necessary.
