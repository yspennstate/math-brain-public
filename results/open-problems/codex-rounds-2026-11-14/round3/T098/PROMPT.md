# Open problem T098: Stability of many-body localization

Statement: For a one-dimensional spin chain with iid random fields, such as the Ising chain with transverse field H = Σ_i h_i σ_i^z + Σ_i γ_i σ_i^x + Σ_i J_i σ_i^z σ_{i+1}^z with weak transverse terms, at strong disorder every eigenstate is many-body localized in Imbrie's sense: there is a quasi-local unitary that turns H into a function of commuting integrals of motion (l-bits), where quasi-locality is probabilistic, holding away from rare resonant blocks whose probabilities decay with their size, with bounds uniform in the chain length.

Caveat: The quantifiers are part of the problem: the statement is for all eigenstates (infinite temperature), not only low energies. Exponential localization at every site, uniformly, is too strong a target, because resonant regions occur with positive density.

Source: D. M. Basko, I. L. Aleiner and B. L. Altshuler, Metal–insulator transition in a weakly interacting many-electron system with localized single-particle states, Ann. Physics 321 (2006); J. Z. Imbrie, On many-body localization for quantum spin chains, J. Stat. Phys. 163 (2016)

Where it stands (checked by us, Nov 2026): Imbrie (J. Stat. Phys. 163 (2016), arXiv:1403.7837) proved it for the random Ising chain with transverse field under an unproved assumption of limited level attraction. Avalanche arguments (De Roeck–Huveneers 2017) indicate instability in dimension two and higher, and numerics have raised doubts about the 1D transition (Šuntajs–Bonča–Prosen–Vidmar, arXiv:1905.06345, Phys. Rev. E 102 (2020)). Localization at low energies for the random XXZ chain is known (Elgart–Klein–Stolz, arXiv:1708.00474, Comm. Math. Phys. 361 (2018)), with logarithmic light cones at the bottom of the XXZ spectrum (Elgart–Klein, arXiv:2602.01441). Huveneers (arXiv:2609.39462) reviews the state of the question. An unconditional proof at positive energy density is open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T098 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Your job for this session: take the NEXT checkable step on this problem, building on that work.
1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was
   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and
   write in LOG.md whether it holds. If it does not hold, that finding is your result.
3. Then choose ONE piece that extends it: the next step its report names, a wider special case, a sharper constant,
   more cases computed, the missing lemma. Write the choice and why in LOG.md first, then do it. A proof goes in
   PROOF.md with every step written out; a computation is a script in this folder with the command and output in LOG.md.
4. Try to break your own result: re-derive every load-bearing number a second way; look for the case you miss.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> | VERDICT: EARLIER RESULT WRONG <what> . Then what is new beyond the earlier
   report, the commands, what failed, what you are unsure of, and what the next worker should do.

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.

----- earlier REPORT.md -----
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
