# P0309 independent adversary checkpoint

2026-10-10. This checkpoint was derived before reading the paired prover's proof. P0309's precise source formulation is still being recovered. No claim of solving crystallisation or of current novelty is made.

## First independent obstruction: an absolute-reference defect penalty

Let T_L=(R/LZ)^3 with integer L>=2, let X={0,...,L-1}^3, and let E be any translation-invariant configuration energy on T_L. This includes periodic pair energies E(Y)=sum_{i<j} g(y_i-y_j), and translation-invariant neutral-background terms. Take delta in (0,1/2), a=(1/2,0,0), and Y=X+a. Every point of Y has torus distance 1/2 from the nearest point of X, so all L^3 sites are bad under the fixed-reference tolerance delta. Yet E(Y)-E(X)=0, by simultaneous translation invariance. Therefore no positive constant c can make E(Y)-E(X)>=c times the fixed-reference bad-site count for all configurations.

This is an exact symmetry counterexample, conditional only on the explicitly stated energy symmetry. It does not rule out crystallisation. It rules out this particular coercive inequality unless global phase is fixed or quotiented out. Boundary-pinned specifications may have a boundary energy and are not covered by the torus equality. Quotienting by one global translation does not itself establish control of slowly varying phase fields or topological defects.

Independent reviewer requested: w530; not checked yet. Next: recover the full primary formulation, distinguish phase/boundary conventions, and identify the uniform free-energy estimate still needed after phase fitting.

## Independent acoustic obstruction after removing the constant phase

For L>=3, let V=(Z/LZ)^3 and H(u)=(kappa/2) sum_{x in V, j=1,2,3}|u(x+e_j)-u(x)|^2, kappa>0. The vector field u(x)=a cos(2 pi x_1/L)e_2 has zero mean. Orthogonality of the discrete Fourier characters gives sum_x |u(x)|^2=a^2 L^3/2 and

H(u)/sum_x |u(x)|^2 = 2 kappa sin^2(pi/L).

Indeed u is an eigenvector of the periodic graph Laplacian with eigenvalue 4 sin^2(pi/L), and H=(kappa/2)<u,(-Delta)u>. Thus the ratio tends to zero as L increases. Removing only the constant translation cannot justify a volume-uniform lower bound H>=c sum_x |u(x)|^2. Small a keeps this example in any prescribed small-displacement neighborhood. This is a proved special case for the specified harmonic model, not a derivation of the Riesz Hessian. Its use in a Riesz proof requires an independently established acoustic comparison.

## Independent finite-volume order reduction, allowing mismatches

Fix a Bravais lattice Lambda, a nonzero reciprocal vector G (G.p in 2 pi Z for p in Lambda), N reference sites p_1,...,p_N, and a configuration of exactly N particles. A measurable matching pairs N-m distinct particles to N-m distinct sites as y_j=p_j+a+u_j. There are m unmatched particles and m unmatched sites. Set A_G=N^{-1} sum_particles exp(i G.y) and B_G=exp(-i G.a) A_G. Then, configuration by configuration,

Re B_G >= 1 - 2m/N - (1/(2N)) sum_matched (G.u_j)^2.

Proof: each matched particle contributes cos(G.u_j)>=1-(G.u_j)^2/2. Each unmatched particle contributes at least -1. Sum these N terms and divide by N. No independence or conditioning product is used. Consequently E|A_G|^2 >= [1-2 E(m/N) -(1/(2N)) E sum_matched(G.u_j)^2]^2 whenever the bracket is nonnegative: E Re B_G bounds E|A_G| from below, and Cauchy-Schwarz then bounds the second moment. A fitted phase a may be random. Nonzero E B_G is a registered statistic; it does not itself produce a fixed-phase Gibbs state.

This isolates a sufficient finite-volume input: uniformly in N, E(m/N)<=epsilon_beta and N^{-1} E sum_matched(G.u_j)^2<=v_beta, with 2 epsilon_beta+v_beta/2<1. The unsolved work is to derive those estimates for the unrestricted Riesz Gibbs measure, together with the DLR limit, rather than impose a lattice tube that excludes the defects in advance. This reduction alone neither proves periodicity of the full point-process law nor existence of its infinite-volume DLR limit.
