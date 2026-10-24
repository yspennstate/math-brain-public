# Independent obstruction, saved before reading paired prover

2026-10-10. Target: C0056, weak-disorder three-dimensional Anderson extended states. This is a counterexample to a proof implication, not to the Anderson conjecture. No w480 proof has been read.

Let X_x, x in Z^3, be iid uniform on [-1,1], and define the bounded diagonal operator D on l^2(Z^3) by D delta_x = X_x delta_x. Its site spectral measure is mu_x = delta_{X_x} for every realization. The standard basis is a complete eigenbasis; the operator is pure point.

For eta>0 and real E,

g_eta(E) = Im <delta_0,(D-E-i eta)^(-1) delta_0>
         = eta / ((X_0-E)^2+eta^2).

Consequently E[g_eta(E)] = (1/2) integral_{-1}^1 eta/((v-E)^2+eta^2) dv <= pi/2, uniformly in E and eta. Also integral_R g_eta(E) dE = pi for every realization. Neither a uniform first-moment bound nor a uniform integrated L^1 bound implies an absolutely continuous site spectral measure.

For X_0 in [-1/2,1/2] and 0<eta<1/2, the interval [X_0-eta,X_0+eta] lies in (-1,1). There g_eta >= 1/(2 eta). Thus integral_{-1}^1 g_eta(E)^p dE >= 2^(1-p) eta^(1-p). Since the event has probability 1/2, E integral_{-1}^1 g_eta^p >= 2^(-p) eta^(1-p), diverging for every p>1. This identifies precisely the stronger moment that the example defeats.

Boundary: D has no hopping, so this is not an Anderson counterexample at weak nonzero disorder with nearest-neighbor hopping. It rejects only an abstract conversion from annealed first-moment regularity to quenched absolute continuity.

Independent reviewer: w482, pending. Status: proved special case, independently unchecked. NEXT: recover the primary target assumptions and prove a sufficient p>1 resolvent criterion; then inspect the paired proof's corresponding inference.
