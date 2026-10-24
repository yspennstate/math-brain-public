Independent C0056 route — checkpoint 2026-10-10

Parent claim: NOT PROVED. Current openness: UNKNOWN pending reconciliation of a September 23, 2026 public claim. No novelty claim for the elementary lemmas below. The independent route was recorded in ROUTE_PRECOMMIT.md before reading any peer proof.

The recovered intake record actually asks for two conclusions: absolutely continuous spectrum for the weak-disorder operator on Z^3, AND GOE local statistics for finite restrictions. These are distinct obligations. This attempt addresses a sufficient criterion for the spectral conclusion only; it gives no GOE limit.

Model slice: H = A + g V on l^2(Z^3), (A u)(x) = sum_{|y-x|=1} u(y), iid V(x) uniform on [-1,1], fixed g>0. H is bounded self-adjoint with norm at most 6+g. Reversing the hopping sign is a unitary conjugacy on the bipartite lattice. This uniform-law slice is more precise than the survey's general centered variance-one law; rescale the coupling by sqrt(3) for uniform variance-one potentials.

Fix a real continuous energy cutoff chi with compact support in an interior interval I, 0<=chi<=1. For a site x, let mu_x(B)=<delta_x,1_B(H)delta_x> and nu_x(dE)=chi(E)^2 mu_x(dE). Define P_eta(t)=eta/(pi*(t^2+eta^2)), p_eta=P_eta*nu_x, and S_eta=E ||p_eta||_2^2. All expectations use the original product law; no independence between resolvent entries or eigenvector weights is assumed.

L1. Exact smoothing and pair identities (proved deterministic statement, review pending).

For every finite positive Borel measure nu on R and eta>0,

  ||P_eta*nu||_2^2 = integral integral P_{2 eta}(s-t) nu(ds)nu(dt)
                     = (1/(2 pi)) integral exp(-2 eta |u|)|nu_hat(u)|^2 du.

Here nu_hat(u)=integral exp(-iuE)nu(dE). Proof: P_eta is real and symmetric. Tonelli expands the square and integrates over the energy variable. The convolution identity P_eta*P_eta=P_{2 eta} gives the first formula. Its Fourier transform is exp(-eta|u|); Plancherel gives the second. Both sides are finite since nu has finite mass and P_eta is in L^2. In particular these are products of the SAME measure, not independent draws of the random environment. At finite volume with distinct eigenvalues E_j and a_j=chi(E_j)^2<delta_x,P_j delta_x>, the first formula is exactly sum_{j,k} a_j a_k P_{2 eta}(E_j-E_k). Spectral projections P_j handle degeneracy without a basis choice. The diagonal is (1/(2 pi eta)) sum_j a_j^2; every off-diagonal term is nonnegative.

L2. Annealed L^2 criterion (proved conditional implication, review pending).

For a measurable random finite positive measure nu with uniformly bounded mass, sup_{0<eta<=1} E||P_eta*nu||_2^2 < infinity if and only if nu=f_omega dE almost surely and E||f_omega||_2^2 < infinity. In that case the supremum is exactly E||f_omega||_2^2. This is a stronger conclusion than mere absolute continuity.

Proof: in L1 the Fourier integrand increases as eta decreases. Monotone convergence in u and omega shows that the limit is (1/(2 pi)) E integral |nu_hat(u)|^2 du. Finiteness implies Fourier L^2 almost surely. Plancherel then represents the finite measure by an L^2 density: for a smooth compactly supported test function, Fourier inversion identifies the measure pairing with the inverse-Fourier L^2 function pairing, hence the measures agree. Conversely convolution is an L^2 contraction and P_eta is an approximate identity, so its L^2 norm tends to ||f_omega||_2. The same monotone formula gives equality of the expectations. Measurability can be taken from the limit in L^2 of the measurable smoothed measures. No almost-sure assertion at uncountably many couplings is made.

For the lattice, a bound at x=0 transfers to every x by stationarity. Intersect countably many site events. If it holds for a countable family of cutoffs positive on subintervals covering I, every mu_x has no singular mass in I. For any Lebesgue-null B subset I, <delta_x,1_B(H)delta_x>=0 for all x, so 1_B(H)delta_x=0 for every basis vector and 1_B(H)=0. Thus the restriction to I is purely absolutely continuous. Nonzero spectral weight is a separate obligation; the criterion by itself is also satisfied by zero measures.

L3. Pair concentration reduction (proved conditional implication, review pending).

Set C_nu(r)=integral integral 1_{|s-t|<=r}nu(ds)nu(dt). For eta>0,

  ||P_eta*nu||_2^2 = (4 eta/pi) integral_0^infinity r C_nu(r)/(r^2+4 eta^2)^2 dr.

Proof: P_{2 eta}(q)=integral_{|q|}^infinity (4 eta r/pi)/(r^2+4 eta^2)^2 dr, and Tonelli applies. Therefore if finite-volume local measures nu_L of mass at most one satisfy

  E C_{nu_L}(r) <= A r + B/N_L   for all r>0,

with A,B independent of L,r, then

  E||P_eta*nu_L||_2^2 <= A/2 + B/(2 pi eta N_L).

The constants use integral_0^infinity r^2/(r^2+a^2)^2 dr=pi/(4a), a=2 eta. This estimate controls ALL weighted eigenvalue pairs and includes the finite-volume atomic remainder. The desired unproved estimate is the displayed pair bound for the actual three-dimensional random operator, at fixed nonzero g.

L4. Correct order of volume and smoothing limits (proved deterministic transfer, review pending).

Use expanding Dirichlet cubes Lambda_L containing x. Extend their restrictions to the full space by deleting only the bonds across their boundary; the exterior remains an operator on the complement. These bounded operators converge strongly to H on finitely supported vectors and hence strongly on all vectors. Bounded continuous functional calculus gives weak convergence of the spectral measures at x, including the chi^2 weights. For each fixed eta and energy E, p_{eta,L}(E) converges to p_eta(E). The spectra lie in [-M,M], M=6+g. On a compact energy interval p_{eta,L}<=1/(pi eta), and for |E|>M+1 it is bounded by eta/(pi*(|E|-M)^2). These bounds give an integrable deterministic bound on the squared densities. Dominated convergence, also in omega, yields S_{eta,L}->S_eta at FIXED eta. Under L3, N_L->infinity now gives S_eta<=A/2 for every eta. Only then take eta down to zero in L2. Taking eta down to zero at fixed L always diverges when the cutoff measure is nonzero; coupled sequences alone need an additional comparison argument.

L5. Completely flat eigenvectors can converge to singular continuous local measures (proved counterexample, review pending).

This refutes the inference from flat eigenvectors or a vanishing diagonal term to absolute continuity. It is not an Anderson counterexample.

On Omega={0,1}^N with independent fair bits xi_i, define T=sum_{i>=1}2 xi_i/3^i and T_k=sum_{i=1}^k 2 xi_i/3^i. Let H and H_k be multiplication by T and T_k on L^2(Omega). Then ||H-H_k||<=3^{-k}. The Walsh characters, indexed by finite bit subsets, form an orthonormal basis and have pointwise modulus one. Each character's spectral measure for H is the standard Cantor measure mu. It has no atoms (a specified first m-bit cylinder has probability 2^{-m}) and is supported on the Cantor set, whose Lebesgue measure is zero (its mth cover has length (2/3)^m). Therefore these local measures are purely singular continuous.

On the N_k=2^k dimensional subspace of functions of the first k bits, H_k has the distinct eigenvalues T_k(xi), each with a normalized cylinder-indicator eigenvector. In the Walsh basis EVERY component of EVERY eigenvector has squared modulus 1/N_k. All inverse participation ratios are exactly 1/N_k. Every local spectral measure is mu_k=N_k^{-1} sum_xi delta_{T_k(xi)}, converging weakly to mu.

Put alpha=log(2)/log(3) and eta_k=N_k^{-1/2}. The diagonal in L1 is D_k=1/(2 pi sqrt(N_k))->0. Nevertheless for every eta in [3^{-k},1), choose m<=k with 3^{-m}<=eta<3^{1-m}. Two independent mu_k samples share their first m digits with probability 2^{-m}; their energy separation is at most 3^{-m}<=eta. Consequently

  ||P_eta*mu_k||_2^2 >= (2/(5 pi eta)) 2^{-m}
                       >= (1/(5 pi)) eta^{alpha-1}.

The second inequality uses 3^alpha=2. Since eta_k>=3^{-k}, S_k>=(1/(5 pi)) N_k^{(1-alpha)/2}->infinity. Thus the off-diagonal eigenvalue-pair contribution diverges while the diagonal vanishes and every finite eigenvector is completely flat. The multiplication operators have neither nearest-neighbor Z^3 geometry nor iid diagonal disorder; no target conclusion follows from this example.

L6. A verified eigenvalue-counting theorem plus an unproved conditional eigenvector-moment estimate would suffice (proved conditional reduction, review pending).

Established input, checked in the primary source: Combes-Germinet-Klein, Generalized eigenvalue-counting estimates for the Anderson model, arXiv:0804.3202v3, equations (1.4), (2.7) and Remark 2.2(i). For a deterministic self-adjoint finite-volume hopping matrix plus independent diagonal potentials with densities bounded by R, and any bounded interval Q, n_Q=Tr 1_Q(H_L) satisfies E[n_Q(n_Q-1)] <= (R |Q| N_L)^2. This result needs no localization hypothesis and permits Dirichlet restrictions. For our coupling g, R=1/(2g). The source's earlier equation (1.3) has a pi factor; this argument uses the sharper (1.4), not a misquotation of (1.3).

Additional UNPROVED assumptions: almost surely simple eigenvalues, ordered as E_1,...,E_N; local weights a_j=chi(E_j)^2|phi_j(x)|^2; E sum_j a_j^2 <= D/N; and, conditional on the full ordered eigenvalue vector, E[a_j a_k | E_1,...,E_N] <= K/N^2 for every j!=k. K,D are independent of volume. For a cutoff supported in an interval of length W>0 these assumptions imply L3 with A=max(18 K R^2 W,1/W), B=D.

Proof: for 0<r<=W, partition the support interval into at most W/r+1<=2W/r bins of length at most r. Enlarge each bin by r on both sides to an interval Q of length at most 3r. Any ordered distinct pair at distance at most r, with its first energy in that bin, is counted in n_Q(n_Q-1). Condition on the FULL energy vector, so this pair event is measurable; the assumed conditional mark bound then gives K/N^2 times the expected unweighted pair count. Applying the established count estimate to all bins bounds the off-diagonal contribution by 18 K R^2 W r. The diagonal is at most D/N in expectation. For r>W, mass at most one gives C_nu(r)<=1<=r/W. No conditional products are multiplied and no eigenvector/eigenvalue independence is asserted.

The conditional mark bound is the missing structural hypothesis, not a consequence of Minami's estimate or inverse participation ratios. It permits order-one conditional moments even when the maximum coordinate grows logarithmically, and avoids an implausible volume-uniform maximum-weight assumption. Simplicity for finite-volume continuous site laws is compatible with the count estimate (cover a compact spectral interval with small intervals and let their length go to zero), but supplies no mark bound.

L7. Free-model calibration in three dimensions (proved special case g=0, review pending).

For A on l^2(Z^3), Fourier transformation identifies the local density as f_3=f_1*f_1*f_1, where f_1(s)=1/(pi sqrt(4-s^2)) on (-2,2), and zero elsewhere. f_1 is the pushforward of uniform circle measure under 2 cos(theta) and is in L^{3/2}. Twice applying Young's convolution inequality (L^{3/2}*L^{3/2}->L^3, then L^3*L^{3/2}->L^infinity) gives ||f_3||_infinity <= ||f_1||_{3/2}^3. Since f_3 has mass one, ||f_3||_2^2 <= ||f_1||_{3/2}^3 = B(1/2,1/4)^2/(2 pi^3). Thus all cutoff measures with 0<=chi<=1 satisfy L2 at g=0 with this explicit constant. This proves only the zero-disorder calibration. No perturbation estimate uniform down to zero smoothing at fixed g>0 is supplied.

L8. A bounded averaged density does not imply quenched absolute continuity (proved counterexample, review pending).

Let X be uniform on [0,1] and let nu_X=delta_X. Then E nu_X is Lebesgue measure on [0,1], with bounded density one, while EVERY nu_X is pure point. L1 gives E||P_eta*nu_X||_2^2=1/(2 pi eta). This shows exactly why first-moment spectral averaging alone cannot replace L2. It is an abstract one-dimensional random operator example, not a counterexample to the lattice target.

Single hardest gap.

Prove a uniform marked two-eigenvalue concentration estimate E C_{nu_L}(r)<=A(g,chi) r+B(g,chi)/|Lambda_L| for the true weak-disorder Z^3 operator at fixed g>0, with constants independent of L and r. L6 reduces this sufficient estimate to a precise conditional eigenvector-moment hypothesis, which is NOT proved. L1-L4 would convert the estimate into pure absolute continuity on the cutoff window. It is stronger than the existence-of-ac-component target. Nonzero spectrum in a window and the GOE statistics obligation are additional obligations. The September 2026 preprint's claim is not used as a theorem in this route.
