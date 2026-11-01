# C0056 independent route, recorded before paired proof

2026-10-10, w484. This file was created before reading w483's proposed proof. Exact intake hypotheses and primary sources are still being recovered; this is an approach plan, not a proof attempt against an unspecified model.

Plan: use scalar spectral measures and the Poisson transform of diagonal resolvents. Identify a sufficient uniform-integrability condition that upgrades regularized disorder averages to almost-sure absolute continuity. Test whether first-moment estimates can establish that condition using an explicit random atomic spectral measure. This avoids assuming that a smooth integrated density of states has the spectral type of an individual realization.

Hardest expected gap: prove an estimate, uniform as the imaginary part tends to zero at fixed positive disorder, that excludes concentration of local spectral mass. No weak-disorder perturbation expansion or finite-time diffusion estimate will be promoted to that bound without proof.

The exact intake row (problems.jsonl:56) requests both absolutely continuous spectrum at small positive disorder on Z^3 and GOE finite-volume local statistics. It leaves the single-site law, energy interval, boundary condition and unfolding unspecified. The recorded attempt (attempts.jsonl:45) tried tree transfer and finite kinetic-time results. The present route uses scalar spectral-measure compactness and single-site conditioning instead. For the primary variance-one uniform law use V=sqrt(3)U, U uniform[-1,1], hence the coupling in the formulas below is sqrt(3) times that primary coupling. Reversing unit hopping is a bipartite unitary conjugacy; a convention adding 6 times the identity requires the corresponding energy shift. The primary Anderson definition and spectral-type discussion in Stolz, arXiv:1104.2317, Sections 2 and 9.2, have been read. The directly cited Bourgade Section 2.1 source is being checked separately.

## Independent derivation (saved before paired proof)

Fix the resolvent convention G(z)=(H-z)^(-1), z=E+i eta, eta>0, so its diagonal imaginary part is nonnegative. Write u_eta(E)=Im G_00(E+i eta)/pi = (P_eta * mu_0)(E), where P_eta(t)=eta/[pi(t^2+eta^2)].

**L01: a first-moment bound cannot determine sample spectral type.** On l^2(Z^3), take D_omega delta_x=U_x delta_x with independent U_x uniform on [-1,1]. Every sample has a complete eigenbasis delta_x, so every local spectral measure is a point mass. Nevertheless,

    E u_eta(E) = (1/(2 pi)) integral_{-1}^1 eta/[(v-E)^2+eta^2] dv <= 1/2

for every real E and eta>0. At E=0 it equals atan(1/eta)/pi and tends to 1/2. The averaged local spectral measure has density (1/2)1_{[-1,1]}. Also the exact Ward identity holds:

    sum_x |G_0x(E+i eta)|^2 = Im G_00(E+i eta)/eta.

At E=0, E|G_00|^2=atan(1/eta)/eta diverges, and for every realization

    integral_R u_eta(E)^2 dE = 1/(2 pi eta).

Thus iid randomness, stationarity, a smooth averaged measure, a bounded first moment and Ward's identity together still allow pure point spectrum. This is a counterexample to that implication, not to the weak-disorder Anderson conjecture: D has zero hopping. Scaling D by any fixed lambda>0 gives first-moment bound 1/(2 lambda), still with pure point samples. No independence across energies or resolvent rows is used.

**L02: a sufficient compactness premise.** Let mu_omega be a measurable random probability measure, I a bounded open interval, 1<p<infinity and eta_n decreasing to zero. If

    sup_n E integral_I (P_eta_n * mu_omega)^p dE <= C < infinity,

then mu_omega restricted to I has an L^p(I) density almost surely. Proof: A(omega)=liminf_n integral_I u_n^p is finite a.s. by Fatou. For such an omega choose n_k with those integrals tending to A. Reflexivity gives a further subsequence converging weakly in L^p(I) to f. For each phi in C_c(I), extend phi by zero and use the uniform approximate-identity convergence P_eta*phi -> phi on R. Therefore integral phi f dE = integral phi dmu_omega. Positivity and uniqueness of finite measures identify mu_omega|I=f dE. Weak lower semicontinuity gives ||f||_p^p<=A. This is pathwise compactness, not an exchange of disorder average and a singular boundary limit. The atomic L01 example disproves the p=1 variant.

For a stationary countable-site self-adjoint operator, a bound of this form for mu_0 transfers in law to every mu_x. Intersect the resulting countably many full-probability events. On that common event all basis spectral measures are absolutely continuous on I. For any Lebesgue-null B subset I, the spectral projection satisfies ||1_B(H)delta_x||^2=mu_x(B)=0 for every x; hence 1_B(H)=0. This establishes pure absolute continuity on I *if the premise is proved*. Separately, nonzero spectral mass in I must be established; otherwise the conclusion can be vacuous. The criterion is sufficient, not necessary for absolute continuity. It says nothing about GOE statistics.

**L03: expose the required cavity estimate without a tree recursion.** Specialize the target to bounded iid potentials with density rho, ||rho||_infinity=M, and H=A+lambda V on Z^3, where A is nearest-neighbor adjacency and lambda>0. Delete the origin. Let h be the coupling vector to its six neighbors, and let

    Sigma(z)=<h,(H^(0)-z)^(-1)h>, a=E+Re Sigma(z), b=eta+Im Sigma(z)>0.

The Schur complement, an exact identity on the full lattice, gives

    G_00(z) = 1/(lambda V_0-a-i b).

Sigma is measurable with respect to potentials other than V_0. Conditional integration in V_0, using only that independence, yields

    E[u_eta(E)^2 | (V_x)_{x != 0}]
        <= (M/(lambda pi^2)) integral_R b^2/[(v-a)^2+b^2]^2 dv
        = M/(2 pi lambda b).

Consequently a uniform bound sup_n E integral_I b(E,eta_n)^(-1)dE < infinity is a sufficient remaining premise for L02 with p=2 at fixed lambda. The automatic inequality b>=eta yields only O(eta^(-1)), which fails this requirement.

For the representative law V_0 uniform[-1,1], if |a|+b<=lambda, the integral contains [a-b,a+b], on which b^2/[(v-a)^2+b^2]^2>=1/(4b^2). Hence

    E[u_eta(E)^2 | cavity] >= 1/(4 lambda pi^2 b) on {|a|+b<=lambda}.

This necessary lower bound on resonant cavities accompanies the sufficient upper bound. The unresolved task is therefore quantitative control of small b on resonant environments, uniform as eta->0 for fixed positive lambda, not just an equation for the average self-energy. The scalar Schur complement remains valid even though the six-neighbor cavity variables are correlated. We have made no closure or product assumption about them.

All three derivations are independent and unreviewed. No parent-problem solution or novelty claim is made. The primary target's GOE branch remains a separate unresolved problem.

NEXT: Obtain w485's independent checks of L01-L03, then audit w483's actual core step against these precise premises.
