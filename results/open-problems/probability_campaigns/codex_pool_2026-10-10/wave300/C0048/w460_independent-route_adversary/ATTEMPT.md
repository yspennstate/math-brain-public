# C0048 independent route: a finite witness to a latent-heat gap

Recorded 2026-10-10 before reading any proposed proof from w459.

Scope recovered from the primary lecture conjecture: nearest-neighbor ferromagnetic Potts model on Z^d, integer q >= 3 and d >= 3, with a discontinuous transition at its critical inverse temperature. Current 2026 openness remains UNKNOWN until the dated local record and present primary literature checks are complete. The large-q and large-d theorems do not settle the remaining pairs.

Independent method: stochastic coupling and a finite event witness, followed by a convex-pressure argument. This is a conditional reduction, not a solution.

Let E be a countable edge set and let mu <=st nu on {0,1}^E. For a finite F subset E and an increasing cylinder event A measurable on F, an ordered coupling (X,Y), X <= Y, gives

    0 <= nu(A)-mu(A)
       = P(X not in A, Y in A)
       <= sum_{e in F} P(X_e=0,Y_e=1)
       = sum_{e in F} (nu(omega_e)-mu(omega_e)).                 (L1)

No independence of edge discrepancies is used: the middle step is a union bound. Thus identical one-edge marginals of two stochastically ordered measures imply equality of every finite marginal and hence equality of the measures. Distinct ordered, translation-invariant and lattice-symmetric measures on Z^d must have a positive nearest-neighbor edge-density gap.

For the free/wired random-cluster application, obtain the infinite ordered coupling by taking finite-volume monotone couplings, extending both configurations by closed edges outside the finite box, and extracting a weak subsequential limit on the compact countable binary product. The marginals converge by the primary source's Proposition 1.8. The coordinatewise order relation is closed, so the limiting coupling remains ordered. The generic stochastic-order formulation also follows from the usual ordered-coupling theorem on this standard Borel product; the argument above supplies the coupling directly for the application.

For random-cluster free and wired states at a fixed p in (0,1), assume

    theta_w = nu(0 connects to infinity) >= eta > 0,
    theta_f = mu(0 connects to infinity) = 0.                    (H)

For B_R=[-R,R]^d intersect Z^d, A_R={0 connects to the inner vertex boundary of B_R using edges in B_R}, the events decrease to {0 connects to infinity}. Choose R with mu(A_R) <= eta/2. The event has

    m_R = d*(2R)*(2R+1)^(d-1)

support edges. Symmetry and (L1) yield

    Delta_e = nu(omega_e)-mu(omega_e) >= eta/(2*m_R) > 0.       (L2)

For the Hamiltonian H=-sum_{<x,y>} 1_{sigma_x=sigma_y}, inverse temperature beta and p=1-exp(-beta), Edwards-Sokal gives phi(omega_e=1)=p*P(sigma_x=sigma_y). Corresponding spin states therefore differ in energy score per site by at least

    Delta_s >= d*eta/(2*p*m_R).                                (L3)

Remaining justification: connect these two infinite-volume spin states to pressure subgradients with a complete finite-volume convexity/boundary argument. Remaining OPEN TARGET: prove (H), or another finite increasing event separation at p_c(q,d), for the missing q,d pairs. The finite-witness lemma by itself cannot supply this premise. Referee w461 must independently check the new quantitative deduction.

Adversarial test queued: boundary partition functions can differ by O(|boundary|) and have the same limiting pressure while their derivatives or Gibbs limits differ. A proof that differentiates a vanishing pressure difference needs an additional argument; equal limiting pressures alone do not force or exclude latent heat.

## Complete pressure reduction (still awaiting independent review)

Let F(beta)=lim_N |B_N|^-1 log Z_N^free(beta), with the equality-indicator Hamiltonian used above and counting measure on the q spin values. Use the monochromatic partition function Z_N^wired obtained by fixing all spins on the inner vertex boundary to color 1; fixed boundary vertices are not summed. If b_N is the number of boundary vertices, recoloring the boundary of any configuration to color 1 changes at most 2*d*b_N edge scores. There are q^b_N possible original boundary colorings. Consequently, for beta >= 0,

    Z_N^wired <= Z_N^free <= q^b_N exp(2*d*beta*b_N) Z_N^wired.

Since b_N/|B_N| tends to zero, both pressures have the same limit, uniformly on compact beta intervals. Existence of the free pressure follows by tiling large boxes with fixed smaller boxes: deleting interbox ferromagnetic bonds changes log Z by at most beta times their number, which is o(volume) as the small-box size then tends to infinity.

For an edge farther than R from the boundary, random-cluster domain monotonicity sandwiches its finite free marginal between the free R-box marginal and the infinite free marginal; the finite wired marginal is between the infinite wired marginal and the wired R-box marginal. First N -> infinity, then R -> infinity. The fraction of edges within R of the boundary vanishes. Therefore

    (F_N^free)'(beta) -> a_f = d*phi^free_p(omega_e)/p,
    (F_N^wired)'(beta) -> a_w = d*phi^wired_p(omega_e)/p.

The identity is the conditional edge-opening probability p given equal endpoint spins in Edwards-Sokal; it is not the formula for full endpoint connectivity. For each fixed boundary condition, finite spin pressure is convex. Its tangent inequality, passed to the limit at beta and any t >= 0, gives

    F(t) >= F(beta)+(t-beta)*a_f,
    F(t) >= F(beta)+(t-beta)*a_w.

Thus a_f and a_w are subgradients of F at beta. For beta > 0, the one-sided derivatives satisfy

    F'_+(beta)-F'_-(beta) >= a_w-a_f
                              >= d*eta/(2*p*m_R) > 0          (L4)

under (H). More generally, a finite increasing event gap delta on m edges gives the lower bound d*delta/(p*m). This argument does not differentiate an o(1) pressure error.

The source's simplex convention has a.b=(q*1_{a=b}-1)/(q-1); if beta_s is its inverse temperature, beta=q*beta_s/(q-1) in this report. Hence p=1-exp(-q*beta_s/(q-1)), and source-pressure slope differences gain a factor q/(q-1). An additive affine pressure shift contributes no jump.

## Exact obstruction to differentiating the boundary error

For n >= 1, set f_n(t)=n^-1 log(exp(2*n*t)+2) and g_n(t)=n^-1 log(2*exp(2*n*t)+1). Both are analytic convex finite-state pressures. The ratio of their partition functions lies between 1/2 and 2, so sup_t |f_n-g_n| <= log(2)/n. Both limits equal 2*max(t,0). Nevertheless,

    f_n'(0)=2/3, g_n'(0)=4/3 for every n.

This refutes the abstract implication 'a subextensive boundary free-energy difference implies equal limiting energy densities'. The example is a two-phase finite-state model, not an asserted nearest-neighbor Potts counterexample. It also makes clear why finite-volume analyticity does not prove differentiability of the thermodynamic limit.

## Single hardest open step

At p_c(q,d), establish a positive wired percolation probability for the missing low-q, low-d pairs, together with a free-state separation sufficient for the pressure route. Conjecture 2 itself asks for positive critical spontaneous magnetization. The pressure criterion (H) is an explicitly stronger sufficient premise unless its free-state part is independently established. No estimate of eta or R is supplied here, and no theorem for q=3,d=3 is claimed.

NEXT: Run the bounded exact normalization checks; then read the paired core-proof lane and return an audit of its critical separation step.
