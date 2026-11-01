# An independent pinning route: proved reference lemmas, not a Riesz proof

Author: w531, 2026-10-10. Independent review requested from w533; none recorded yet. These are elementary mathematical proofs in a labelled harmonic reference model and a conditional point-process criterion. No formal checker has been run. The single transfer gap is at the end.

## L1. Uniform nonzero-mode covariance in three dimensions

Fix beta>0, kappa>0, h>0, and integer N>=2. On the discrete torus T_N=(Z/NZ)^3 let u_x in R^3 have density proportional to exp(-beta H_N,h(u)), where

H_N,h(u) = (kappa/2) sum_{x,j=1}^3 |u_{x+e_j}-u_x|^2 + (h/2) sum_x |u_x|^2.

Each positively oriented edge occurs as written, including the two directed occurrences of a bond when N=2. Define omega(k)=4 sum_j sin^2(k_j/2). Discrete Fourier diagonalization gives

Cov(u_x) = beta^{-1} g_N(h) I_3,
g_N(h) = N^{-3} sum_{k in (2pi/N)T_N} (kappa omega(k)+h)^{-1}.

For every N>=2 and h>0,

g_N(h) <= 1/(h N^3) + 13/(16 kappa).

Proof. Choose integer representatives n_j with |n_j|<=N/2. For the nonzero frequencies, sin(pi |n_j|/N)>=2|n_j|/N, so omega(2pi n/N)>=16|n|^2/N^2. In the shell max_j|n_j|=m there are at most (2m+1)^3-(2m-1)^3=24m^2+2 representatives. Its contribution to the nonzero-mode sum is at most (24+2/m^2)/(16 kappa N). There are floor(N/2) shells, each numerator is at most 26, and floor(N/2)<=N/2. The total is at most 13/(16 kappa). The omitted frequency k=0 contributes exactly 1/(h N^3). This proves the inequality. The centered, zero-spatial-average Gaussian at h=0 is also defined; it has the same bound with the zero term omitted.

For fixed h>0 the integrand is continuous and periodic, hence

lim_{N->infinity} g_N(h) = g(h) = integral_{[-pi,pi]^3} (kappa omega(k)+h)^{-1} dk/(2pi)^3.

On this cube omega(k)>=4|k|^2/pi^2. Consequently 1/omega is integrable near zero in dimension three. Monotone convergence yields

lim_{h down to 0} g(h) = G_3/kappa < infinity,
G_3 = integral_{[-pi,pi]^3} omega(k)^{-1} dk/(2pi)^3 <= 13/16.

The last bound follows by first taking N to infinity in the discrete inequality at fixed h and then h to zero. This order of limits is essential: at fixed N the zero mode diverges as h down to zero. Setting h=0 in the unrestricted finite torus does not define a probability density. A zero-average constraint is a distinct finite-volume measure, not permission to discard a mode of the unrestricted gas.

## L2. Bragg order without independent displacements

Let A be an invertible real 3 by 3 matrix, Lambda=A Z^3, and K a nonzero reciprocal vector (A^T K in 2pi Z^3). At reference positions A x+t define

M_N(K)=N^{-3} sum_{x in {0,...,N-1}^3} exp(-i K dot (A x+t+u_x)).

For the Gaussian in L1,

E M_N(K) = exp(-i K dot t) exp(-|K|^2 g_N(h)/(2 beta)),
E |M_N(K)|^2 >= exp(-|K|^2 g_N(h)/beta).

Proof. The reciprocal condition removes exp(-iK dot Ax). Each single marginal K dot u_x is centered Gaussian with variance |K|^2 g_N(h)/beta. Its characteristic function is exp(-variance/2). Linearity of expectation proves the first identity and E|Z|^2>=|EZ|^2 proves the second. The u_x are correlated; no product of per-site conditional bounds is used.

In the order N->infinity followed by h down to zero, the mean amplitude is

m(K)=exp(-|K|^2 G_3/(2 beta kappa))>0.

There exists a stationary centered Gaussian field indexed by Z^3 with covariance

C(r) I_3 = [1/(beta kappa)] integral_{[-pi,pi]^3} exp(i k dot r) omega(k)^{-1} dk/(2pi)^3 I_3.

Indeed the Fourier kernel is integrable and nonnegative, so the finite covariance matrices are positive semidefinite and define consistent Gaussian marginals. C(r)->0 as |r|->infinity by the Riemann-Lebesgue lemma. For this field,

E exp[-iK dot (u_x-u_y)] = exp[-|K|^2(C(0)-C(x-y))].

Thus E|M_N|^2 converges to m(K)^2. To justify averaging, for each epsilon choose a finite set of differences outside which the displayed pair expectation differs from m(K)^2 by at most epsilon. The fraction of pairs with a difference in that finite set is at most its size/N^3; the contribution outside it is at most epsilon. This also proves M_N converges in L2 to exp(-iK dot t)m(K).

This constructs a reference point process nu_t=sum_{x in Z^3} delta_{Ax+t+u_x}. Its expected count in a half-open fundamental cell F is one: stationarity of the single-label marginal and the tiling by F-Ax give sum_x P(Ax+t+u_x in F)=1 by Tonelli. A compact set is covered by finitely many such cells, so nu_t is locally finite almost surely. Distinct labels collide with probability zero because u_x-u_y has a nondegenerate Gaussian density for x!=y; countably many pairs still have probability zero.

Let v=|det A| and lambda_t=E nu_t. Lattice stationarity makes lambda_t Lambda-periodic. Periodization and the reciprocal identity give its normalized Fourier coefficient

lambda_hat_t(K) := v^{-1} integral_F exp(-iK dot y) lambda_t(dy)
                 = v^{-1} exp(-iK dot t) exp(-|K|^2 G_3/(2 beta kappa)).

It is nonzero, so the reference point process is not invariant under all translations. Uniformly averaging t over F makes a fully translation-invariant mixture with a vanishing nonzero first Fourier coefficient, while |M_N|^2 retains the same positive limit. A vanishing first moment in an averaged state therefore cannot refute crystalline order in its phase components.

The reference field is built on fixed lattice labels. It has NOT been shown to satisfy any Riesz gas DLR specification. Positive order at every beta in this reference model is not a claim about a Riesz phase diagram.

## L3. A defect-tolerant criterion for a periodic point process

Let (J_x,u_x)_{x in Z^3} be jointly stationary under integer shifts, with J_x in {0,1}, u_x in R^3, and E[J_0 |u_0|^2]<infinity. They need not be independent. Let eta be a Lambda-periodic-in-law random counting measure with E eta(F)<infinity; it need not be independent of the matched particles. Put

nu=sum_x J_x delta_{Ax+t+u_x} + eta,
q_m=1-E J_0, q_b=E eta(F), delta=E[J_0 |u_0|^2].

Then nu is locally finite almost surely, its expected counting measure lambda is Lambda-periodic, and

Re[exp(iK dot t) v lambda_hat(K)] >= 1-q_m-q_b-(|K|^2/2) delta.

Proof. The same tiling/Tonelli argument as L2 gives one-cell matched mass E J_0 and the exact matched Fourier coefficient E[J_0 exp(-iK dot(t+u_0))]. Local finiteness follows from finite expected mass in every translated cell. The extra measure's Fourier contribution has absolute value at most q_b. Apply cos z>=1-z^2/2 to the matched term and (K dot u)^2<=|K|^2 |u|^2. This proves the bound without any dependence hypothesis beyond shift stationarity.

If q_m+q_b+|K|^2 delta/2<1, then lambda_hat(K)!=0 and nu's law is not invariant under every translation. If, in addition, nu is actually a Gibbs law for a specified translation-covariant Riesz gas specification, its translations with distinct exp(-iK dot a) are distinct Gibbs laws for the same specification. This conditional conclusion is symmetry breaking and nonuniqueness. It does not establish the stronger classification of all extreme phases, BCC/FCC selection, or an explicit transition temperature.

## Single hardest remaining gap

For the FULL nonlinear, unlabelled, unpinned Riesz gas, construct a lattice-periodic Gibbs limit together with a stationary matched-particle/defect decomposition satisfying q_m+q_b+|K|^2 delta/2<1, uniformly as volume tends to infinity and pinning is removed. The harmonic covariance does not supply this decomposition, control defect fugacity, prove a global Riesz Hessian lower bound, or justify the renormalized long-range DLR limit. None of those missing obligations is assumed to have been proved. L1-L3 are complete special-case/conditional lemmas, not a solution of P0309.
