# P0309: force balance does not imply a stable crystal

Author: w534. Date: 2026-10-10. Status: proved special cases by the author; independent review pending. P0309 remains unresolved. Current openness and novelty are UNKNOWN.

## Target and source

The exact intake asks to prove a crystalline Gibbs phase at sufficiently low positive temperature for the three-dimensional Coulomb or Riesz gas in the regimes predicted by Lewin's review. The intake is `brain_bundle_C006p02.json`, entry `op-p0309`, line 2217. The primary source is Mathieu Lewin, *Coulomb and Riesz gases: The known and the unknown*, arXiv:2202.09240v2 (2022), Section VI, printed pages 59–61 and 66–67 (zero-based PDF pages 58–60 and 65–66).

A precise working specialization is this: fix s>3 and intensity rho>0 for the classical continuum gas with interaction |x-y|^{-s}. Find a finite threshold b_s so that, whenever beta*rho^{s/3}>b_s, an infinite-volume Gibbs equilibrium law exists that is invariant under a full-rank lattice of translations and fails invariance under all translations. This is a formalization of the intake, not a quantified theorem quoted from the review. It does not demand that finite-temperature particles sit exactly on lattice sites. For s=1 the corresponding target uses a neutralizing background and a specified long-range Gibbs specification.

Lewin's Section VI treats a crystalline law as periodic at the level of a probability law; translated or rotated mixtures must be distinguished from a chosen symmetry-breaking component. The phase diagrams are numerical predictions. The short-range diagram has FCC at the lowest temperatures; the Coulomb diagram uses BCC. Thus neither lattice selection nor a universal transition temperature is available as a proved input. A bounded recent arXiv search did not establish a current resolution: current openness remains UNKNOWN.

## Prior attempts and scope

`brain_bundle_C006a05.json`, entry `at-p0309`, lines 2112–2116, evaluates the harmonic infrared integral int_0^1 r^{d-3}dr. It is finite in d=3, conditional on a stable lattice and its harmonic approximation. The record itself explicitly leaves lattice selection, defects, anharmonicity, and uniform volume control open. Exact-ID/title searches of the named H/I attempt directories yielded no additional matching attempt. The Lean annotated ranking only records the dated unsolved status. No percolation argument is relevant here. No claim of an exhaustive literature search is made.

Team O's cited board contains no P0309 assignment. The statement-only packet was prepared for w535 before this proof. This lane tests a separate prerequisite: a lattice can be force balanced while its phonon energy has a negative direction. This is not a counterexample to the earlier conditional infrared calculation, which never asserts that force balance suffices. It is a counterexample to the stronger auxiliary bridge: "a density-one, force-balanced periodic Riesz configuration necessarily has nonnegative displacement Hessian."

## Lemma A: exact alternating-plane instability, s>3

For real a set

    X_a = {(m+a*(n mod 2), l, n): m,l,n in Z}.

There are two particles per rectangular period cell of volume two. The density is one for every a. Define E_s(a) as mean Riesz energy per particle with unordered pairs counted once. For s>3 the relevant lattice sums converge absolutely. Then

    E_s(a) < E_s(0) if a is not an integer;
    E_s(a) = E_s(0) if and only if a is an integer;
    E_s''(0) < 0.

The assertion holds at any positive density after dilation, with energy multiplied by rho^{s/3}.

### Pair normalization

An even-plane particle sees an odd-plane particle with first-coordinate offset m+a; an odd-plane particle sees m-a. Replacing m by -m makes the two sums equal. Same-parity pairs are unchanged. Consequently

    Delta_s(a) := E_s(a)-E_s(0)
      = (1/2) sum_{n odd} sum_{m,l in Z}
        [((m+a)^2+l^2+n^2)^(-s/2) - (m^2+l^2+n^2)^(-s/2)].        (A1)

The factor 1/2 is the unordered-pair factor, not an additional averaging over the two particle types. There is no zero vector in the odd-n sum.

### Gaussian representation and strict sign

For t>0 write

    Theta(t,a) = sum_{m in Z} exp(-t*(m+a)^2),
    O(t) = sum_{n odd} exp(-t*n^2).

The gamma integral r^{-s}=Gamma(s/2)^{-1} int_0^infinity t^{s/2-1} exp(-t*r^2)dt and absolute convergence give

    Delta_s(a) = 1/(2*Gamma(s/2)) int_0^infinity
        t^{s/2-1} Theta(t,0) O(t) [Theta(t,a)-Theta(t,0)] dt.       (A2)

The Fourier coefficients of the periodic Gaussian Theta(t,a) are obtained by integrating exp(-t*x^2)*exp(-2*pi*i*k*x) over R. The elementary Gaussian integral gives sqrt(pi/t)*exp(-pi^2*k^2/t). Thus

    Theta(t,a)-Theta(t,0)
      = 2*sqrt(pi/t) sum_{k>=1} exp(-pi^2*k^2/t)*(cos(2*pi*k*a)-1). (A3)

Every summand is nonpositive. If a is not an integer, the k=1 term is strictly negative. Since Theta(t,0)>0 and O(t)>0, (A2) is strictly negative. If a is an integer, X_a=X_0 as unlabeled point sets and (A3) vanishes. This proves the sharp equality condition.

### Curvature and convergence

Differentiating (A3) twice at zero gives

    Theta_aa(t,0) = -8*pi^2*sqrt(pi/t)
                      sum_{k>=1} k^2*exp(-pi^2*k^2/t) < 0.

Therefore

    E_s''(0) = -4*pi^2*sqrt(pi)/Gamma(s/2) int_0^infinity
        t^{s/2-3/2} Theta(t,0) O(t)
        sum_{k>=1} k^2*exp(-pi^2*k^2/t) dt < 0.                  (A4)

Here is the justification for exchanging differentiation and integration. For 0<t<=1, Theta(t,0) and O(t) are O(t^{-1/2}); the absolute value of each a-derivative through order two of the difference in (A3) is O(t^{-1/2} exp(-pi^2/t)), uniformly in a. For t>=1 and |a|<=1/4, the primal Gaussian sum and its first two a-derivatives are bounded by C(1+t^2), while O(t)<=C exp(-t). These bounds are integrable with t^{s/2-1} for every fixed s>0. The quadratic expansion Delta_s(a)=(1/2)E_s''(0)*a^2+o(a^2) is consequently valid. No independence assumption is used.

## Lemma B: a compactly supported negative second variation, s>3

Let v_s(r)=|r|^{-s} and h_s(r)=partial_1^2 v_s(r), so

    h_s(r) = -s*|r|^{-s-2} + s*(s+2)*r_1^2*|r|^{-s-4}.          (B1)

The force at each point of Z^3 vanishes: the absolutely convergent gradient sum cancels under r -> -r. Thus this lattice is stationary for every finitely supported displacement.

Let Q_L={-L,...,L}^3 and p_x=1_{x in Q_L}*1_{x_3 odd}. Move x to x+a*p_x*e_1 and leave all other particles fixed. The relative unordered-pair energy H_L(a)-H_L(0) is absolutely defined: only finitely many particles move, and each far-field potential difference is bounded by C_s*|a|*|r|^{-s-1} for |a|<=1/4. Differentiation twice is justified by the summable Hessian bound |h_s(r)|<=C_s*|r|^{-s-2}. Its first derivative is zero by the force cancellation. Its second derivative is

    K_L = (1/2) sum_{r in Z^3\{0}} h_s(r)
                         sum_{x in Z^3}(p_{x+r}-p_x)^2.         (B2)

For each fixed r, divide the inner sum by |Q_L| and let L tend to infinity. The boundary fraction tends to zero. In the interior, the difference square is one when r_3 is odd and zero when r_3 is even. Also the inner sum divided by |Q_L| is at most two, since its support lies in Q_L union (Q_L-r). Dominated convergence with the summable |h_s| therefore gives

    lim_{L->infinity} K_L/|Q_L|
       = (1/2) sum_{r_3 odd} h_s(r) = E_s''(0) < 0.              (B3)

For all sufficiently large finite L, K_L<0. Taylor expansion then supplies arbitrarily small, finitely supported displacements with strictly lower relative energy. Hence simple cubic Z^3 is force balanced but is not a local Riesz ground state, even when the competitor must equal it outside a finite region. This closes the possible objection that Lemma A only changes infinitely many particles.

## Lemma C: the explicitly heat-regularized relative difference, s>0

For every fixed s>0 define D_s(a) to be the right side of (A2), irrespective of whether the separate raw energies exist. The small-t and large-t bounds above prove that this integral is finite for every a (reduce a modulo one) and that D_s(a)<0 precisely for nonintegral a. Its curvature at zero is (A4), strictly negative. For s>3, D_s=Delta_s by Lemma A. For 0<s<=3 this is a theorem about a specified relative heat regularization: any common background/self counterterms in the two heat representations cancel.

This is NOT an assertion that every proposed long-range DLR or thermodynamic normalization has already been identified with this relative energy. That identification is not needed for Lemmas A and B. In particular s=1 in Lemma C is not a Coulomb crystallization theorem.

## Attempt toward the original target and the hardest gap

A proof via a low-temperature expansion must first choose a genuinely stable reference phase, control its acoustic modes, and then compare it with all competing configurations. Simple cubic cannot serve as that reference: force balance does not provide the missing Hessian coercivity. Lemma B furnishes an exact finite-support counterexample to this bridge.

The single hardest remaining gap for P0309 is a uniform-in-volume nonlinear free-energy/order estimate for a stable BCC/FCC candidate that controls defects and competing phases and survives the thermodynamic limit as a non-translation-invariant Gibbs law. Neither the finite Gaussian infrared integral nor this instability lemma supplies that estimate. This packet stops at the proved obstruction; it does not claim P0309 solved.

Independent reviewer: w536. Adversary: w535. Independent review state: pending. Trusted mathematical inputs: the elementary Gaussian Fourier integral, the gamma integral, Taylor expansion, and dominated convergence. There is no formal-check receipt, no computer-assisted proof claim, and no admitted theorem placeholder.
