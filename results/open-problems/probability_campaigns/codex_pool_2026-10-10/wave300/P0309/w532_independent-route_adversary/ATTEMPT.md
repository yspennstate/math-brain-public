# P0309 independent route, saved before paired proof

2026-10-10. Worker w532. Paired w531 proof has not been read. This is an independent observable route and a candidate obstruction; it does not solve P0309. Current openness remains UNKNOWN pending the exact intake record and later-status check.

Primary framework: Mathieu Lewin, *Coulomb and Riesz gases: The known and the unknown*, arXiv:2202.09240v2, Sections II.3, III.3 and VI.2. At positive temperature a crystalline point process means a periodic law with broken continuous translation symmetry. It does not mean that almost every particle configuration is an exact lattice. Short-range DLR, equation (45), is not automatically the renormalized long-range specification.

The route is to bound a local Fourier observable in the full Gibbs law, allowing vacancies and interstitials, and then pass that bound through the thermodynamic limit. No expansion of an unproved lattice ground state or product of dependent local events is used here.

## Local intensity criterion (independent derivation C1)

Let L be a full-rank lattice in R^d and Q a bounded fundamental parallelepiped centered at 0. Let G be a nonzero reciprocal vector, so G dot z is in 2*pi*Z for all z in L. Let P be an L-translation-invariant locally finite point process with q = E_P N(Q) finite and positive. Define

    m_G = E_P sum_{x in X intersect Q} exp(i G dot x),
    D_G = E_P sum_{x in X intersect Q} (G dot x)^2.

The elementary inequality cos(t) >= 1 - t^2/2, integrated against the intensity measure on Q, gives

    Re(m_G) >= q - D_G/2.

Consequently D_G < 2q implies m_G != 0. A process invariant under every translation has intensity rho*Lebesgue, hence m_G = rho integral_Q exp(i G dot x) dx = 0 for nonzero reciprocal G. Therefore this criterion certifies broken continuous translation symmetry of an already constructed L-periodic law. The proof needs no independence, no assignment of labels to lattice sites, and no one-particle-per-cell constraint. It is only a sufficient criterion; a uniformly translated crystal can have m_G = 0.

If D = E sum_{x in X intersect Q} |x|^2, then D_G <= |G|^2 D, giving the sufficient threshold D < 2q/|G|^2. A periodic cell convention and a fixed phase are part of the assumptions, not conclusions of the moment estimate.

## What an actual Gibbs proof would need

Construct finite-volume full Gibbs laws with boundary phase selected by L. Establish both positive limiting q and the strict bound D_G < 2q with a margin uniform in volume. If a periodic pinning field is introduced, the bound must also be uniform as that field goes to zero after volume goes to infinity. Verify tightness, local count uniform integrability, zero boundary mass for Q, L-periodicity of the limit, and the unpinned (possibly renormalized) DLR equation. These are proof obligations, not established premises.

The hardest open piece in this route is a volume-uniform localization bound for the *unrestricted*, unpinned Riesz Gibbs law. A harmonic Hessian bound around an assumed lattice does not establish it. The bound must include defects, competing structures and long-range interactions, and must not assume the ordered phase it is supposed to prove.

## Candidate finite-energy obstruction, to be refined

For the short-range repulsive grand-canonical DLR kernel at finite beta and finite chemical potential, a bounded region can be empty with strictly positive conditional probability. A proof that the full Gibbs law has probability one of exactly one particle in every prescribed cell contradicts this kernel. This does not rule out a periodic intensity or phase; it only rules out the excessively strong support claim. A sharper uniform vacancy bound and a sequential conditioning argument will be derived separately.

NEXT: Recover the intake's exact exponent/quantifier statement, derive the uniform DLR vacancy obstruction, then read and adversarially audit w531's decisive step.
