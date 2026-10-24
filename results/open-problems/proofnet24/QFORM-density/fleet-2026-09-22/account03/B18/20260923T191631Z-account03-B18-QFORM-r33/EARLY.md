# account03/B18 r33 — early substantive calculation

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T19:16:31Z.

Targeted implication: a four-original-coordinate rank-three principal core with one physical zero diagonal.

Let B be real symmetric 4x4, rank(B)=3, B_00=0. Let its three nonzero eigenvalues have magnitudes at least s>0. Let z be a unit kernel vector and put h=1-z_0^2. Let C=B[{1,2,3},{1,2,3}].

New deterministic observation to prove fully in REPORT.md:

    sigma_min(C) >= s z_0^2 = s(1-h).

Sketch by Cauchy interlacing plus the rank-three adjugate identity det C=(mu_1 mu_2 mu_3)z_0^2. In each possible signature, the two compression eigenvalues already trapped away from zero and bounded above by the corresponding parent magnitudes let the determinant identity pay the remaining one; in the mixed-sign cases the same argument is applied to each of the two potentially small compression eigenvalues.

Consequences if the observation holds:

1. Conditioning on X_0 and every outside original coordinate leaves three independent cap-one coordinates with fixed quadratic matrix C and arbitrary affine term. The completed account03/B18 cap-one three-variable theorem gives

    ||p||_infty < 148/[s(1-h)].

2. The newly completed account01/B18 four-coordinate cofactor theorem gives independently

    ||p||_infty <= 576^(1/3) s^(-1) h^(-1/3)

for h>0.

At the simple split h_0=18^(-3)=1/5832:

    h<h_0 => 148/(1-h) < 149,
    h>=h_0 => 576^(1/3) h^(-1/3) <= 18*576^(1/3) < 150.

So the planned theorem is a uniform <150/s essential-density bound for every such original-coordinate four-core, with arbitrary affine terms and arbitrary ambient completion handled by conditioning. This would remove the h->0 divergence in the account01 cofactor receiver by switching to the complementary leaf compression rather than perturbing the zero pivot.

The unrestricted QFORM problem remains open because the global hypothesis s_3(A)>=1 does not force the existence of such a qualifying four-coordinate rank-three zero-diagonal principal core.
