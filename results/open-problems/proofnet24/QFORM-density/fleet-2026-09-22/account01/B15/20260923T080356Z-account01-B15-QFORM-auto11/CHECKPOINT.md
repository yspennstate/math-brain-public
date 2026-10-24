# Early substantive checkpoint: zero-loss weak-limit closure of density height

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

Define, for a finite Borel measure nu on R,

H(nu)=inf{C>=0: nu(E)<=C |E| for every Borel E},

with H(nu)=+infinity if no such C exists. For absolutely continuous nu this is exactly ||dnu/dx||_infinity.

**Claim proved.** If nu_m => nu weakly, then

H(nu) <= liminf_m H(nu_m).

Proof: pass to a subsequence along which H(nu_m)->L<infinity. For every open interval J, Portmanteau gives nu(J)<=liminf nu_m(J)<=L |J|. Every open set is a countable disjoint union of open intervals, hence nu(O)<=L|O|. Outer regularity gives nu(E)<=L|E| for all Borel E. Therefore nu<=L dx.

Consequences already checked:

1. If product source laws mu_m converge to mu and quadratic polynomials q_m converge locally uniformly to q, then q_m#mu_m => q#mu. Any uniform density-height bound for the approximants passes to q#mu with exactly the same constant; no Fourier envelope, moment, continuity or uniform output convergence is needed.

2. For arbitrary cap-one marginals f_i, there exist C-infinity compactly supported cap-one probability densities f_{i,m} with ||f_{i,m}-f_i||_1->0. One construction truncates f_i on [-R,R], replaces the tail mass m_R by the constant density m_R on a disjoint unit interval, then convolves with a compact mollifier. Thus the full universal-height theorem may be proved on smooth compactly supported sources and passed to rough sources at zero loss.

3. Matrix genericization is likewise zero-loss at the HEIGHT level: after scaling A slightly upward to create s_3(A)>1 margin, approximate by symmetric rational matrices with simple spectrum and every nonempty principal minor nonzero. Since x^T A_m x -> x^T A x pointwise/local-uniformly and the source can be held fixed, the same weak-limit lemma removes the perturbation without moments. This is stronger than the previous common-Fourier-envelope closure when only the height bound, rather than uniform convergence of densities, is required.

4. Continuity is deliberately not claimed: uniform weak limits of continuous densities with a common L-infinity bound can have no continuous representative (e.g. Uniform[0,1] convolved with Gaussian noise of variance ->0). Continuity therefore needs a separate structural/Fourier argument.

Next step in this run: apply the completed account02/B15 one-sheet and volume-envelope results to concrete interval inequalities under this closure principle, and write the exact dense-core equivalence with proof.
