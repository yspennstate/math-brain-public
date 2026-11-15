# A transfer principle for C(tau, sigma) (working note, 11 Nov 2026)

Status: idea with two proved lemmas (short proofs below); no constant obtained from it yet. Not audited.

Goal behind it: a universal lower bound C(tau, sigma) >= c_0 > 0 for all sigma != [n] dominating tau would give
Oliveira's conjecture by the argument of Theorem 1.8 of arXiv 2610.22151 (row T104). The known bound is 1/n^3.

## Lemma A (pair energies split over isotypic components)

Let M be an orthogonal representation of S_n and E_ij(h) = <h, (I - (i j)) h> = (1/2)|h - (i j)h|^2 for h in M.
Let Pi_nu be the projection of M onto its nu-isotypic component. Then E_ij(h) = sum_nu E_ij(Pi_nu h) for every pair
ij, and every term is >= 0. In particular E_ij(Pi_sigma h) <= E_ij(h).

Proof. Pi_nu commutes with the action, so I - (i j) is block diagonal for the isotypic decomposition. QED

## Lemma B (pointwise contractions)

Let X be a finite S_n-set, M = R^X, and phi: R -> R 1-Lipschitz. Then E_ij(phi o f) <= E_ij(f) for every f in M and
every pair ij.

Proof. E_ij(f) = (1/2) sum_x (f(x) - f((i j)x))^2, and |phi(a) - phi(b)| <= |a - b|. QED

More generally, if h_1, ..., h_k are commuting symmetries of X (maps X -> X commuting with S_n; for X = S_n with
left action, right translations) and Phi: R^k -> R is L-Lipschitz for the Euclidean norm, then
g(x) = Phi(f(h_1 x), ..., f(h_k x)) has E_ij(g) <= L^2 k E_ij(f).

## Consequence

Let psi be a unit vector of V_tau and embed it in some R^X: pick an intertwiner J: V_tau -> R^X (for X = S_n,
J psi (s) = <psi, rho_tau(s) v> for a fixed v in V_tau; for X the set of tau-tabloids, the Specht embedding).
Put f = J psi, so E_ij(f)/|f|^2 = 1 - <psi, rho_tau((i j)) psi>. For a 1-Lipschitz phi let g = phi o f. If
Pi_sigma g != 0 it defines a state rho on V_sigma (the reduced state of Pi_sigma g / |Pi_sigma g| on the
V_sigma factor of the isotypic component), and by Lemmas A and B

    1 - tr(rho rho_sigma((i j))) = E_ij(Pi_sigma g)/|Pi_sigma g|^2 <= (|f|^2/|Pi_sigma g|^2) (1 - <psi, rho_tau((i j)) psi>).

With Proposition 1 of N4_PROOF.md:

    C(tau, sigma) >= inf over unit psi of  sup over (X, J, phi) of  |Pi_sigma(phi o J psi)|^2 / |J psi|^2.      (T)

The right side asks: how much of the mass of a contraction of f can be put in the sigma-component.

## What is known about (T) so far

- It cannot work alone for tau = [1^n]: f is +-1 valued on every X, phi o f = a + b f, no sigma-component. That pair
  is trivial for another reason (all pair energies of the sign state are maximal). So (T) has to be combined with the
  dual form: only pairs ij with small energy of psi need a good bound.
- Isotropy: if psi is fixed by a Young subgroup S_mu then so is every g built this way, so Pi_sigma g != 0 needs
  V_sigma to have S_mu-invariants, that is sigma dominates mu. Since tau dominates mu, dominance of sigma over tau is
  exactly what makes this possible for every mu. This is the mechanism of Theorem 1.3 of the paper.
- Upper limit: for tau = [2, 1^{n-2}], sigma = [2^{n/2}] and psi the star eigenvector the right side of (T) is at
  most 2/3 (Theorem 4.5 of the paper).

## Tensor powers (Lemma A alone)

Take M = V_tau^{tensor k} and h = psi^{tensor k} for a unit psi. Then E_ij(h) = 1 - t_ij^k with
t_ij = <psi, rho_tau((i j)) psi>, and 1 - t^k <= k (1 - t) on [-1, 1] for k >= 2. By Lemma A the state given by
P_sigma h (P_sigma the projection of V_tau^{tensor k} onto its sigma-component) has

    1 - tr(rho rho_sigma((i j))) <= k (1 - t_ij) / |P_sigma psi^{tensor k}|^2,

so C(tau, sigma) >= sup_k inf_psi |P_sigma psi^{tensor k}|^2 / k. The infimum is the minimum over the unit sphere
of V_tau of a nonnegative form of degree 2k.

## Where pure transferred states must fail

Any construction psi -> (a vector of the sigma-component built equivariantly from psi) vanishes at a psi whose line
is fixed by a subgroup H acting on it by a character chi such that the powers of chi do not occur in V_sigma
restricted to H. Example, n = 4, tau = 211, sigma = 22: V_211 is R^3 with S_4 acting as the rotation group of the
cube; psi = (1,1,1)/sqrt(3) is fixed by a 3-cycle, and a 3-cycle has no fixed vector in V_22. So
P_22 psi^{tensor k} = 0 for every k. This psi is the star eigenvector, the extremal point of Theorem 3 of
N4_PROOF.md, and the matching state there is the maximally mixed state I/2 on V_22 (u = 0 in the proof).

So the extremal examples of the conjecture sit at such twisted fixed points, and near them the matching state has to
be mixed. The maximally mixed state on V_sigma has 1 - tr(rho rho_sigma((i j))) = 1 - chi_sigma((1 2))/dim V_sigma
for every pair. A proof along these lines has to interpolate: transferred states where psi is far from the twisted
fixed points, mixed states near them. In the n = 4 proof this interpolation is the three cases.

## Next steps

1. Numerics at n = 4, 5 on X = S_n: for the pairs left open in N4_PROOF.md section 5, minimise over psi the best
   value of (T) over v and a small family of phi (|t|, max(t, 0), clipping at a level, t -> |t - a|). Does (T) reach
   2/3 at (211, 22)? What does it give at (2111, 221)?
2. If the values stay bounded below as n grows on the star family (tau = [a, 1^{n-a}], sigma = [a^{n/a}], exact value
   a/(a+1)), look for a proof of a universal constant on a family first (two-row sigma, hooks).
3. The k-argument version with right translations, to reach sigma-components that pointwise maps miss.
