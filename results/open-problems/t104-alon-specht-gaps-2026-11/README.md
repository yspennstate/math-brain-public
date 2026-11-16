# Spectral gaps on Specht modules (Alon's 2/3 conjecture): working record, 11-13 November 2026

For a weighted graph G on [n] and a partition nu of n, let lambda_min(G, nu) be the least eigenvalue of the
interchange Laplacian sum_{i<j} w_ij (I - rho_nu((i j))) on the Specht module V_nu. G. Alon (arXiv 2610.22151,
Conjecture 1.5) conjectures that lambda_min(G, tau) >= (2/3) lambda_min(G, sigma) whenever sigma != [n] dominates
tau, and shows (Theorem 1.8) that this implies Oliveira's conjecture on the mixing time of the interchange process.
The conjecture is open. This folder is the complete working record of one attempt on it: the note of partial
results, the numerical searches, the exact and interval checks, and the reports of the language-model referees who
audited each step. Home paths and internal names were replaced; nothing else was edited.

## What is already known, and what is new here

Already published, and used here with credit:
- the spectrum on the hook [n-k, 1^k] is the k-fold sums of the spectrum on [n-1, 1] (Bacher, J. Algebra 167
  (1994)); Alon and Kozma (Canad. Math. Bull. 56 (2013), Appendix A) identify Bacher's exterior powers with the hook
  Specht modules and deduce the chain [n-1,1] > [n-2,1^2] > ... > [1^n];
- the sign representation, lambda_1 on [1^n] equal to twice the total weight (Alon-Kozma, Corollary 2);
- the star values n-2 on [2,1^(n-2)] and n-1 on [2,2,1^(n-4)] (Alon-Kozma, Corollary 1), which show that the
  constant (n-2)/(n-1) proposed below cannot be raised;
- lambda_min(G, nu) >= lambda_1(G) for nu != [n] (Caputo, Liggett and Richthammer), and everything in Alon's paper:
  the conjecture for quasi-complete graphs, the constant 1/n^3 in general, and attainment of 2/3.

New in this record (`T104_NOTE.md`), none of which settles the conjecture:
- a dual form of any such comparison: every pure state of V_tau must be matched, transposition by transposition,
  by a mixed state of V_sigma (Proposition 2.1);
- the constant k/j between the hooks [n-j, 1^j] and [n-k, 1^k] (Proposition 3.1), read off Bacher's description;
- the conjecture for n = 4, where 2/3 is attained on the star (Theorem 4.2; the scalar inequality has a Lean proof,
  the representation-theoretic step is not formalised);
- for tau = [2,1^(n-2)], sigma = [2,2,1^(n-4)], the constant (n-2)/(n-1) on weighted graphs whose Laplacian has two
  distinct nonzero eigenvalues, the larger simple (Theorems 5.2-5.3, n >= 5), and a finite certificate for
  n = 5..13 that one referee reproduced.

A route that fails, recorded so it is not repeated: the state built from the top eigenvector satisfies the dual
inequality only after summing against the graph's weights, not transposition by transposition. At n = 5 with
x = (1,1,0,0,-2)/sqrt 6 the transposition (1 5) gives 1/2 against the required 13/24 (`state_check_n5.py`).

## Files

- `T104_NOTE.md`: the note, with proofs; `N4_PROOF.md`, `GAP_STATE_FORM.md`, `HOOKS_AND_TWO_ROWS.md`,
  `TRANSFER_IDEA.md`: the working drafts behind its sections.
- `alon_search.py` and `dom_n*.tsv`: minimisation of the ratio over the weights (Young's orthogonal form, L-BFGS from
  flat, heavy-tailed, sparse, path-like and star-like starts) over every dominating pair for n = 4 to 8. The smallest
  ratio found is 2/3 to six decimals at n = 4, 6, 7 and 8 (at n = 4 on the star K_{1,3}) and 3/4 at n = 5; no ratio
  below 2/3 was found.
- `t104_strat*_result.md`, `t104_strat_LOG.md` and the folders `strat2/` to `strat21/`: twenty proof strategies for
  the general case, each with its scripts, outputs and the reason it stopped (the workers' raw terminal transcripts
  are not included; their briefs, notes and results are).
- `cone_*.c`, `cone_recheck*.py`, `dense_*.out`, `chunk_n13.out`: the exact cone computations behind the n = 5..13
  certificate, and their independent rechecks.
- `canon_*.py`, `family_F_check.py`, `extremal_spectra.py`, `star_*`, `two_eig_family*`: checks of single lemmas;
  every `.py` has its output beside it as `.out` or `.json`.
- `AUDIT*_CODEX_*`, `CODEX_PSI_*`: briefs, logs and reports of the language-model referees, including the parts they
  could not confirm.

## Credit

The conjecture and the framework are Alon's. The hook computations rest on Bacher's work and on Alon and Kozma's
reading of it, and the comparison with the graph Laplacian on the theorem of Caputo, Liggett and Richthammer; the
mixing-time motivation is Oliveira's. Young's orthogonal form is used for every numerical computation. The
language-model workers (OpenAI Codex) refereed and extended individual steps; the coordinating agent chose the
questions, wrote the note and checked each claim. No result here has been refereed by a journal.
