# C0048: brain-assisted bridge

Checkpoint 2026-10-10. The exact source statement is in STATEMENT_ONLY.md. The source's target is positive wired infinite-cluster probability at criticality, for the zero-field ferromagnetic nearest-neighbor Potts model, integer q>=3 and d>=3. Current openness is UNKNOWN; there is no novelty claim.

The prior C0048-A001 attempt tried improving chessboard contour-entropy constants. Its own result is unsolved and lacks an independent check. No exact C0048 record was found by targeted search in the H/I attempt directories; the Lean intake contains an annotated ranking row, not a formal proof receipt. Team O's board has no C0048 row. This attempt uses a disjoint local-witness bridge.

## L1

For a finite graph, p in (0,1), q>=1 and boundary partition xi, put a=p/[p+q(1-p)]. Let K_e mean that the endpoints of e are connected without using e, with xi applied. Then

phi^xi(omega_e=1) = a + (p-a) phi^xi(K_e).

Proof: the conditional random-cluster weight ratio between the open and closed states of e is p/(1-p) if its endpoints are already connected, and p/[q(1-p)] otherwise. Converting the ratio to a probability and averaging proves the identity.

For two boundary conditions at the same p and q, the corresponding edge-density difference equals (p-a) times the difference in K_e probabilities. At q>1, p-a=p(1-p)(q-1)/[p+q(1-p)]>0.

Status: elementary finite-graph result with a complete proof, awaiting independent review; no novelty claim. The identity does not create a positive critical difference. The provisional hardest gap is a volume-uniform positive lower bound on the free/wired K_e difference at p_c for every integer q>=3 and d>=3.

## L2: a local witness forces an edge-density difference

Let mu_0 and mu_1 be measures on {0,1}^E admitting a coordinatewise monotone coupling X<=Y. For every finite F subset E and every event A depending only on F,

|mu_1(A)-mu_0(A)| <= sum_{e in F} [mu_1(omega_e)-mu_0(omega_e)].

Proof: in the coupling, 1_A(X) can differ from 1_A(Y) only if some coordinate in F differs. Hence its absolute expected difference is at most the union bound sum_{e in F} P(X_e!=Y_e). Monotonicity makes each term E[Y_e]-E[X_e]. This proof uses no independence. In fact the same argument bounds total variation distance of the restrictions to F.

For free/wired FK limits on Z^d with q>=1 and 0<p<1, stochastic domination supplies such a coupling (Strassen's monotone-coupling theorem). If both measures are invariant under translations and lattice rotations, their marginal difference rho is the same on every edge. A positive difference delta for a fixed cylinder event A supported on M edges gives rho>=delta/M. Conversely, equality of all edge marginals forces equality on all finite cylinders and therefore equality of the two measures. This converse uses the coupling and does not infer a measure from its individual marginals without an order assumption.

## L3: conditional quantitative pressure bridge

Assume integer q>=2, d>=2, 0<p<1, beta=-log(1-p). Let mu_f,mu_w be translation- and rotation-invariant Potts Gibbs states obtained from free and monochromatic boundaries, with their corresponding FK marginals phi_f,phi_w. Assume a fixed event A on M>=1 edges has phi_w(A)-phi_f(A)=delta>0. Then, for the pressure per vertex

P(beta)=lim_{n->infinity} |Lambda_n|^{-1} log Z_{Lambda_n}(beta),

P'_+(beta)-P'_-(beta) >= d*delta/(p*M)>0.

Proof: the Edwards-Sokal joint law satisfies E_phi[omega_e]=p*mu(sigma_x=sigma_y), including fixed monochromatic boundary conditions; take local limits. Thus the two spin energy densities per vertex differ by d*rho/p, where rho is the common edge-marginal gap. L2 gives rho>=delta/M.

To justify the pressure step without assuming convergence of a spatial average of finite-box derivatives, let mu be either infinite-volume Gibbs state. In a box with exterior spin configuration eta, write H_Lambda^eta for the sum of equal-spin indicators over edges touching the box, with exterior spins fixed. For every t with beta+t>=0, Jensen's inequality gives

log Z_Lambda^eta(beta+t)-log Z_Lambda^eta(beta) >= t*E_{mu_Lambda,beta^eta}[H_Lambda^eta].

Average over eta drawn from mu. By the DLR property the averaged right side equals t*E_mu[H_Lambda]. Exterior-boundary changes affect log Z by at most a constant times the number of crossing edges; after division by volume that vanishes uniformly in eta. Translation/rotation invariance makes the normalized mean energy converge to e(mu)=d*mu(sigma_0=sigma_e1). Taking the thermodynamic limit yields P(beta+t)-P(beta)>=t*e(mu). Consequently P'_-(beta)<=e(mu)<=P'_+(beta). Applying this separately to mu_w and mu_f proves the claimed derivative gap.

Scope: this is a conditional bridge, at any beta. It does not prove that delta>0 at p_c and does not replace the source's critical-magnetization target by pressure non-differentiability. No claim here establishes the critical free-state infinite-cluster behavior.

## L4: exact refutation of finite-volume positivity as a transition certificate

Let P_L be the path with L>=2 edges, fixed q>1, 0<p<1, and a=p/[p+q(1-p)]. Compare free boundaries with the partition identifying the two endpoints. Every edge has free marginal a, and the wired marginal exceeds it by

Delta_L = (q-1)(1-a)a^L / [1+(q-1)a^L] > 0.

Proof: under the free law every edge is independent Bernoulli(a), since on a tree k(omega)=|V|-|omega|. Identifying the two endpoints reduces the cluster count by one except when every edge is open. Therefore the wired law has density [1+(q-1)1{all L edges open}]/[1+(q-1)a^L] relative to the free law. Computing an edge expectation gives the formula. Since 0<a<1, Delta_L tends to zero. The marginal on any fixed r edges converges to the same Bernoulli(a) product law; the density correction on the all-open r-pattern is bounded by a constant times a^(L-r). The two infinite-volume limits coincide and have no infinite cluster at any p<1. Thus positive wired/free gaps in every finite volume do not imply a finite-temperature first-order transition.

Scope: this refutes that general inference, not the Potts conjecture in d>=3. It also explains why L2 needs a fixed support and a positive gap in the infinite-volume limit. Exact enumeration agrees for 72 path/parameter/edge cases. For q=3,p=1/2, the measured marginal gap decreases from 1/12 at L=2 to 1/12297829382473034412 (8.1315e-20) at L=32.

## L5: exact three-state mean-field barrier and the published error allowance

Use normalized coupling J=2d*beta for the nearest-neighbor model and the probability-vector mean-field functional F_J(x)=sum_i x_i log x_i -(J/2)sum_i x_i^2. At q=3, J_0=4 log 2. On the surface max_i x_i=1/2, the minimum of F_{J_0} is attained at permutations of (1/2,1/4,1/4), and its excess above F_{J_0}(1/3,1/3,1/3) is

B = log 3 -(19/12)log 2 >0.

Proof: fix x_1=1/2 and write x_2=s,x_3=1/2-s. The second derivative of this restricted functional is 1/s+1/(1/2-s)-2J_0 >=8-8 log 2>0. Symmetry puts its unique minimum at s=1/4. Direct substitution gives B. Positivity is exact: 12B=log(3^12/2^19), and 531441>524288. A state satisfying F_{J_0}(x)<=inf F_{J_0}+epsilon with epsilon<B therefore cannot lie on max_i x_i=1/2, since inf F_{J_0}<=F_{J_0}(uniform). This one-coupling exclusion alone does not prove a transition or identify the actual critical coupling.

Compare full hypotheses of Biskup-Chayes: their Theorem 1.1 assumes a translation- and rotation-invariant infinite-volume Gibbs state. Their Main Theorem's infrared estimate applies to extreme thermodynamic magnetizations, d>=3, reflection-positive normalized nearest-neighbor interactions, and has allowance E=J*n*kappa*I_d/2. For the tetrahedral Potts representation, n=q-1 and kappa=(q-1)/q; at q=3, E=(2J/3)I_d. Theorem 2.1 concludes jumps only for sufficiently large d depending on fixed q; even there it does not identify the jump with the onset of magnetization (the theorem's following discussion explicitly preserves that possibility). None of these statements supplies the fixed critical witness required by L2/L3.

In their notation I_d is the integral of t(k)^2/(1-t(k)), t(k)=d^{-1}sum_j cos(k_j). Shifting every k_j by pi changes t to -t, so I_d=int t^2/(1-t^2)>=int t^2=1/(2d). The isolated singular points are integrable for d>=3; the inequality also follows by nonnegative monotone convergence of the even-power expansion. Hence at d=3,J=J_0 the published allowance E is at least J_0/9=0.3080654, whereas B=0.0011292528. The strict comparison also has the exact integer witness 2^73>3^36, since J_0/9>B is equivalent to (73/36)log 2>log 3. The allowance is at least 272.80465 times that barrier. This is a floor on the theorem's error allowance, not a positive lower bound on actual covariance, and not a refutation of all mean-field techniques. It proves that this particular error bound cannot certify this separator at q=d=3. No high-dimensional asymptotic is substituted at d=3.

## Single hardest remaining gap

Construct, for each fixed integer q>=3 and d>=3, a fixed finite cylinder event A and a delta(q,d)>0 such that its free/wired probability difference stays at least delta along increasing boxes at p=p_c, and prove the required implication to the source's critical wired percolation target. None of L1-L3 constructs that witness. In particular, a positive finite-box difference that vanishes with box size, or an event whose support grows with the box, does not close this gap. Critical wired percolation remains unproved here.

NEXT: Obtain a volume-uniform critical lower bound for a fixed event without importing large-q, large-d or spread-out assumptions; the referee should check L3's pressure normalization and the L4/L5 obstructions first.
