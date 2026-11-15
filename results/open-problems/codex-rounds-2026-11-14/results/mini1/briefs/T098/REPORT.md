VERDICT: PARTIAL exact full-spectrum l-bits for Bernoulli-diluted transverse-field Ising chains

Proved a restricted interacting special case of T098. In

\[
 H=\sum_i h_iZ_i+\sum_i\xi_i g_iX_i+\sum_iJ_iZ_iZ_{i+1},
 \qquad \mathbb P(\xi_i=1)=p<1,
\]

the iid Bernoulli indicators create exact conserved spins at xi_i=0.
Controlled diagonalization of the intervening active blocks gives a complete
set of commuting l-bits, without any level-attraction assumption. The
construction covers the entire spectrum and allows arbitrary finite h, g, J.
For absolutely continuous iid h, independent of the other coefficients,
finite-volume simplicity holds almost surely, so every eigenvector carries
definite l-bit labels. Without that field assumption the result gives a
complete common eigenbasis, with the usual qualification for degenerate
energy eigenspaces.

For the common support envelope of either conjugation of any one-site
operator, uniformly in chain length,

\[
 \mathbb P(R_i>r)\le 2p^r-p^{2r},\qquad r\ge1.
\]

This is an equality for the envelope away from the physical boundaries. For
an operator A supported on X, the expected error of approximation by an
operator within distance r is at most 4|X| ||A|| p^r. The proof also constructs
the corresponding infinite-volume algebra automorphism. All steps and
quantifiers are in [PROOF.md](PROOF.md).

This elementary exact-barrier case does not prove a stable MBL phase for
generic nonzero transverse fields. No novelty claim is made. Setting even
one barrier's transverse field to epsilon breaks its old l-bit, with exact
commutator norm 2|epsilon|; the old diagonalizer leaves off-diagonal norm
|epsilon|. The required stability estimates remain open here.

Literature check: less than ten minutes, on 14 November 2026. No unconditional
solution of the stated problem was found. Imbrie's theorem still explicitly
assumes limited level attraction. [John Z. Imbrie, *On Many-Body Localization
for Quantum Spin Chains*, arXiv:1403.7837](https://arxiv.org/abs/1403.7837).
The recent mathematical survey discusses outstanding resonance and
high-probability issues. [Francois Huveneers, *Many-body localization: an
introduction for mathematicians*, arXiv:2609.39462, Section
4.5](https://arxiv.org/html/2609.39462v1).
The XXZ light-cone theorem concerns fixed intervals at the bottom of the
spectrum. [Alexander Elgart and Abel Klein, *Many-body localization for the
random XXZ spin chain in fixed energy intervals*,
arXiv:2602.01441](https://arxiv.org/html/2602.01441v3).
The October transport-capacity paper studies finite-size resonances
numerically and perturbatively; it does not supply the missing theorem.
[Jessica K. Jiang, Federica M. Surace, and Olexei I. Motrunich, *Charge
transport capacity as a probe of resonances in models of many-body
localization*, Phys. Rev. B 114, 194203 (2026), arXiv:2604.18710](https://journals.aps.org/prb/abstract/10.1103/l7n9-ql9y).
Only opened primary sources are cited. An unindexed result could have been
missed.

Reproduce the independent numerical audit with:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py > verification_stdout.txt 2> verification_stderr.txt
```

- 69 matrix cases, dimensions at most 128: all indicator patterns for
  L=1,...,5, five seven-site cases, and two degenerate cases. Independent
  Hamiltonian assemblies, full spectra, controlled gates, l-bits, joint
  labels, and both conjugation directions were checked.
- Largest normalized residual: 4.9960036108132044e-15.
- 855 exact rational probability checks, covering every site and r=1,...,L
  for L=1,...,9 and p=1/3,1/2,2/3; error exactly zero. Both bulk and boundary
  cases were included, using all 1022 indicator patterns across these lengths.
- The barrier perturbation with epsilon=1/32 gave commutator norm 1/16
  and old-diagonalizer residual 0.03125000000000196, agreeing with the
  independent exact Pauli calculation. An H=0 GHZ example checked the
  degeneracy qualification.
- Runtime 4.744 seconds; peak RSS 57,671,680 bytes; numerical thread limits
  set to one. The process inherited nice 20, verified through libc. macOS
  denied the redundant nice adjustment; the process remained below the
  requested priority.

Data: [verification.json](verification.json), [tail_checks.csv](tail_checks.csv),
[stdout](verification_stdout.txt), and [stderr](verification_stderr.txt).
The first BLAS matrix-multiplication run emitted floating-point warnings
despite small residuals. It was not accepted as the final audit; its data
are retained in verification_initial.json. The accepted run uses explicit
einsum contractions, fatal floating-point warnings, and finite-value checks,
and emitted no numerical warnings. These floating-point checks support the
analytic proof; they are not certified interval computations.

Next work: allow a small nonzero transverse term at the barriers. A concrete
first target is an anti-concentration estimate for the transition denominators
created by flipping one formerly frozen spin. In the unperturbed block basis
these denominators contain its independent longitudinal field linearly.
Determine whether geometric block-size tails compensate for the number of
conditional block-eigenstate pairs, before attempting further rotations.
Neither finite-volume simplicity nor continuity at fixed L supplies a bound
uniform in L.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 21:58 Asia/Tbilisi.
