VERDICT: ACCEPT (no correction needed; two optional remarks)

Independent post-posting referee pass on "Global solutions of stochastic reaction-diffusion systems with triangular
structure and species-dependent transport noise", https://github.com/yspennstate/stochastic-reaction-diffusion-triangular-transport
(main.tex at 41818d1, 966 lines, read in full 14 Nov 2026 03:3x-04:0x laptop time; Zenodo 10.5281/zenodo.24203979).
Referee: an agent (Claude Opus 5.5), not the writer of the proofs (Codex GPT-6.1 wrote them; Codex referee run
I0071AR returned MINOR before posting). Lane: T-20261112-017 independent referee passes on posted papers.

What was checked, line by line, by hand:
- Lemma 3.1 (triangular weights): the weights t_i from the lower-triangular matrix, the backward solve with
  eta in [0, v/R_ii], the bound by lambda r^+, and S^{m-1}(1 + S) <= 2(1 + S^m). Correct.
- Lemma 3.2 (mixed Hessian form): the exponent difference -2 in the second derivative of the weighted power, the matrix
  C_beta = D[(1 - rho) I + rho 1 1^T] D, its eigenvalues 1 - rho (multiplicity l - 1) and 1 + (l - 1) rho, and the
  mixed small terms bounded by Cauchy-Schwarz. Correct.
- The Euler identity for the homogeneous energy and the lower bound on the diagonal part. Correct.
- Proposition 4.1 (coercivity of the diffusion form): diagonal >= (mu/2) D, off-diagonal <= rho K (l - 1) sum a^2, and
  the tuning rho K (l - 1) <= mu/4 gives Q >= (mu/4) D. Correct.
- Lemma 4.2 (face bound): Lambda L^2 N_m Phi; the cross term by Cauchy-Schwarz for the positive semidefinite form;
  Young with epsilon = mu/8. Correct.
- Lemma 6.1 (Ito expansion): (1/2) H[B, B] + H[B, g] + (1/2) H[g, g], the symmetrized transport diffusion, and the
  energy inequality with dissipation (mu/8) D. Correct.
- Proposition 6.2: the supermartingale Y, the tail and dissipation bounds, and the exhaustion by the stopping times
  Gamma_k. Correct.
- Proof of Theorem 2.1: the delta_0 bounds; kappa_0 = p_0(1 - delta_0/2) - 1 gives the identity h_0/(h_0 - 1);
  P(s < sigma < T) = 0 over countably many rational s, T, hence sigma = infinity a.s. Correct.
- Corollary 6.3 (dimension lifting) with margin min{mu, 2 min nu}. Correct.
- Remark 7.1: the counterexample gives Q = -2, so the structural hypothesis cannot be dropped. Correct.
- The remaining remarks of Section 7 (other local realizations; whole space and boundaries; superlinear zero-order noise): each states
  accurately what the proof uses and what stays open. The whole-space obstruction (a nonzero constant f(0) leaves
  unweighted L^q(R^d)) is correct and is correctly called a function-space obstruction, not a blow-up. The superlinear
  remark is right that the zero-order Hessian trace has degree m + h - 1 > m under local growth, so the triangular
  upper bound alone does not close the energy inequality.
- End matter and bibliography: the standard sections are present; citations are complete with DOIs and arXiv versions.

Not re-checked against the sources: page and proposition numbers in the Agresti-Veraar papers (AVlocal Proposition 7.1
p. 34, AVsurvey Assumption 8.4(3)) and the local well-posedness and blow-up criterion imported from AVlocal; the
statements as used are the standard ones.

Optional remarks (no change required):
1. Remark "Other local realizations" says the energy calculation applies to any compatible local realization with
   nonnegativity and the positive-time regularity; one sentence naming the blow-up criterion it needs (the one from
   AVlocal used in the proof of Theorem 2.1) would make the remark self-contained.
2. In the proof of Theorem 2.1 the countable union over rational (s, T) is the step that turns the per-interval bound
   into sigma = infinity a.s.; stating "s, T rational" explicitly at that point would spare the reader a re-check.
