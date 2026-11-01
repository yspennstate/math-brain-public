# P0220 continuation: two untried approaches

2026-10-11. Completed continuation; final verdict SOLVED (historical priority unverified).

The previous gap is an audited, useful all-k joint law beyond the historical patience/Gamma representation. The previous attempt proved continuous non-Markov behavior but did not audit the general Schur/Fredholm formulas.

Two approaches not pursued in that attempt:

1. **Finite occupied-site duality and Eynard-Mehta.** Transpose partitions so first-row bounds become row-count bounds. Restrict the whole trajectory to d rows, with d equal to the final (effective) row cap. Earlier checkpoints with cap m<d force the lowest d-m nonintersecting walkers to occupy precisely 0,...,d-m-1. Instead of a gap Fredholm determinant on an infinite half-line, compute these finitely many mandatory occupations by a finite biorthogonal-ensemble correlation determinant. If correct, all joint survival probabilities become an ordinary finite block determinant with explicit factorial/Bessel entries.

2. **Direct drift-jump adjoint and gap-coordinate hierarchy.** Use X_1 independence from later gaps to remove one dimension of the correct stationary adjoint equation. Look for a closed Volterra hierarchy on the gap density, or an iterated resolvent with certified positive kernels. This avoids Schur-process convention issues but might not close because gap jumps couple neighbours and the first coordinate is integrated out.

Approach 1 is more promising: it targets the earlier changing-row-cap obstruction, uses only finitely many mandatory sites, and should admit exact coefficient checks against permutations. It has not been carried out in this folder. The brain query "Okounkov Reshetikhin Schur process multi time gap Fredholm kernel Plancherel" returned Borodin-Rains (2005), Eynard-Mehta theorem, and general determinantal-process cards. Those are leads only.

NEXT: derive the block determinant by elementary Cauchy-Binet and a generating function; verify the time-ordering and transpose matching independently.


## Candidate finite block determinant (saved before checks)

Sort distinct positive observation times 0<t_1<...<t_r=T, retaining at equal times the smallest particle index k_a. Replace k_a by its suffix minimum and put m_a=k_a-1; then m_a is nondecreasing. Set d=m_r. For each a<r require occupation of sites x=0,...,d-m_a-1 at t_a. Let J be this finite list of markers (t,x), and q=|J|. Let b_i=i, i=0,...,d-1, and p_u(y,x)=u^(y-x)/(y-x)! for y>=x, otherwise zero.

Define

    A_ij = sum_y p_T(y,b_i) p_1(y,b_j),
    F_i? = p_(t_?)(x_?,b_i),
    G_?j = sum_y p_(T-t_?)(y,x_?) p_1(y,b_j),
    Q_?? = 1_(t_?<t_?) p_(t_?-t_?)(x_?,x_?).

Candidate:

    P(X_(k_a)>t_a for all a)
       = exp(-T) det [[A, F], [-G, -Q]].

The matrix dimension is d+q. The sums in A,G are convergent one-dimensional factorial/Bessel series. No infinite spatial determinant and no inverse are required in this displayed formula. If d=0, the value is exp(-T); the determinant is empty.

Derivation to audit: transpose the Plancherel path; encode a d-row partition ? by the d distinct nonnegative integers ?_i+d-i. Skew-tableau weights are minors of the one-particle Poisson semigroup. The terminal row cap d is built into the finite particle number. Earlier cap m forces occupancy of 0,...,d-m-1. Multivariate occupation generating function should be det[A+F Z(I-Q Z)^(-1)G]. The all-marker coefficient is det(A) det(G A^(-1)F-Q), which equals the displayed block determinant. This needs proofs of source matching, nonnegativity, finite-cutoff Cauchy-Binet, coefficient extraction, and passage to infinite terminal positions.

For d=2 and only X_2>s, X_3>T, the formula predicts the stronger special case

    exp(-T) [I_0(2 sqrt(T)) I_0(2 sqrt(T-s))
               -sqrt((T-s)/T) I_1(2 sqrt(T)) I_1(2 sqrt(T-s))].

With X_1>s, X_2>t, X_3>u (s<=t<=u), replace T by u-s, first checkpoint by t-s, and the prefactor by exp(-u). This resums the earlier triple partition series to two Bessel products, if the candidate is correct.


Exact finite validation: finite_block_check.py compared all power-series coefficients through degree 7 with exhaustive uniform permutations and independent Poisson interval compositions. All 15 cases passed, including scalar caps, repeated times, nonmonotone caps, fractional times, a d=0 boundary, and a 14-by-14 matrix for five particles. Output saved in finite_block_checks.json. These checks support signs/time conventions; a full proof is still being completed.


## Completion

Approach 1 succeeded. FINITE_DETERMINANT.md contains the full proof of the finite block determinant for every stationary joint survival probability, plus a two-product Bessel formula for the triple survival function and a closed density. The key step is forced occupation of the lowest finite sites after transposition; it makes the changing-row-cap projections evaluable by a finite correlation determinant. This resolves the earlier mathematical gap without auditing a raw infinite Schur kernel. Approach 2 was recorded as an alternative and was not pursued after approach 1 succeeded.

Exact permutation coefficients, independent positive growth values, and the general Lean block-sign identity all pass. REFEREE.md records the complete self-review. No exact published theorem for this source was verified; classical determinant machinery is credited, and novelty/priority are unverified.
