# T104 lead: the 2/3 Specht-module conjecture (arXiv 2610.22151)

Row T104 of the probability list is Oliveira's conjecture on the mixing time of the interchange process.
G. Alon, arXiv 2610.22151 (15 Oct 2026), Theorem 1.8: Conjecture 1.5 below implies it.

Conjecture 1.5. For partitions sigma, tau of n with sigma != [n] and sigma dominating tau, and every weighted
graph G on [n], lambda_min(G, tau) >= (2/3) lambda_min(G, sigma), where
L(G, nu) = sum_{i<j} w_ij (I - rho_nu((i j))) on the Specht module of nu.

Known from the paper: true for quasi-complete graphs and whenever the Aldous order holds; a constant 1/n^3 in
general (Theorem 1.4); 2/3 is attained for unbounded n (Theorem 4.5); a positive constant exists exactly when sigma
dominates tau (Theorem 1.3). The author's numerical evidence: all unweighted graphs for n <= 7 and random weights.

What this folder adds: a minimisation of the ratio over the weights (alon_search.py; Young's orthogonal form,
L-BFGS from random flat, heavy-tailed, sparse, path-like and star-like starts), which is a harder test than
random weights.

Checks of the code: s_k^2 = I, braid and commutation relations, symmetry, and the star Laplacian spectrum of
Lemma 4.2, all to 2e-15 for n = 4, 5, 6; pairs with sigma = [n-1,1] give ratio 1 (Caputo, Liggett, Richthammer);
non-dominating pairs at n = 4 are driven to 0, as Theorem 1.3 says.

Results so far (dom_n4.tsv, dom_n5.tsv; smallest ratio found over all dominating pairs):
- n = 4: 0.666667 at tau = 211, sigma = 22, on the star K_{1,3} (15 starts a pair).
- n = 5: 0.750000 at tau = 2111, sigma = 221; next 0.798379 at tau = 311, sigma = 32 (20 starts a pair).
- n = 6 (dom_n6_local.tsv, 15 starts a pair, 43 pairs, run on the laptop): 0.666669 at tau = 2211, sigma = 222, on
  the disjoint union of K_{1,3} and one edge (both Laplacians are still invertible there, since 222 does not
  dominate 42); 0.666671 at tau = 21111, sigma = 222, on the star K_{1,5}; next 0.750002 at tau = 3111, sigma = 33
  on a star with a little weight elsewhere.
No ratio below 2/3.

The star values in closed form. By Lemma 4.2 the star K_{1,n-1} has lambda_min = n - 1 - nu_1 + m_1(nu) on the
Specht module of nu, where m_1 is the number of rows of length nu_1 (the largest content of a removable corner is
nu_1 - m_1). For tau = (a, 1^{n-a}) and sigma = (a^{n/a}), a >= 2 dividing n, the ratio is
(n - a) / ((n - a)(1 + 1/a)) = a/(a+1). So a = 2 gives exactly 2/3 for every even n, which is the family behind
the 0.6667 rows at n = 4 and 6, and a = 3 gives the 0.75 row at n = 6. On stars alone the smallest ratio over
dominating pairs is 2/3 (not proved here beyond this family; the search agrees through n = 6).


Running: n = 6, 7, 8 queued on Mac mini 1 at 01:40 on 11 Nov (jobs 20_agent_alon_n6/7/8, output
~/t104_alon/dom_n<N>.tsv there). n = 9 needs the pairs split across jobs (largest module has dimension 768).

Status: evidence only. A ratio below 2/3 would be a counterexample and would need an exact (rational) check
before any claim; ratios at or above 2/3 prove nothing.

## Additions, 11 Nov (second round)

- HOOKS_AND_TWO_ROWS.md: hooks are exterior powers (every pair of hooks has ratio >= k/j); conjugation
  lambda_min(G, nu') = 2W - lambda_max(G, nu); V_[n-2,2] as edge weightings of K_n with zero sum at every vertex;
  Conjecture F for the family ([2,1^(n-2)], [2,2,1^(n-4)]) with constant (n-2)/(n-1) (n = 4 is Theorem 3; search
  values 3/4 at n = 5, 4/5 at n = 6); the disjoint-union lemma and why 2/3 reappears at (2211, 222), (3211, 322),
  (4211, 422): these are the n = 4 pair (211, 22) on K_{1,3}, lifted through horizontal strips.
- n = 7 table (dom_n7.tsv, 87 pairs, Mac mini 1): minimum 0.666668 at (3211, 322); next 5/7 at (211111, 2221) on
  the star, 3/4 at (22111, 2221). Nothing below 2/3. n = 8 running there.
- A natural matching state for Conjecture F (auxiliary direction uniform) is exact at the star and at a single
  edge and fails between them, per edge and in the weighted form (canon_state.out, canon_primal.out). Whether a
  weighted auxiliary direction is enough for n >= 5: canon_cov.py, canon_cov.out.
- At n = 5 the pairs left after the trivial families and the hooks: (311, 32), (221, 32), (2111, 32), (221, 311),
  (2111, 221).

## Additions, 11 Nov (third round)

- dom_n8.tsv (Mac mini 1, 194 pairs): minimum 2/3 at (22211,2222), (2111111,2222), (4211,422), (221111,2222);
  the pair of Conjecture F gives 6/7. Nothing below 2/3 for n <= 8.
- HOOKS_AND_TWO_ROWS.md section 5 now lists four explicit choices of the covariance: a weight function of x_k
  (canon_omega.py, misses by 6e-4 at n = 5), the one-parameter family for three-valued x (canon_theta.py, always
  admissible), test vectors from the graph (canon_spectral.py, each simple one fails somewhere), and the
  gap-weighted state C = (lam Pi - L_G)/tau (canon_gap.py, canon_gap_target.py, gap_form_check.py), which is false
  at n = 4 and has no counterexample at n = 5, 6 in 170 local searches.
- Running: fillq job 21_agent_gap_search on Mac mini 1 (n = 5..8, 5500 local searches), outputs
  ~/t104_alon/gap_n5.out .. gap_n8.out.
- Open: prove Gval >= 0 for n >= 5 (section 5 (d)), or find its counterexample.

## 11 Nov, 03:40

- The fillq job was split into four one-core jobs (29_agent_gap_n5..8.job on Mac mini 1), outputs as above.
- Two-eigenvalue family (GAP_STATE_FORM.md, two_eig_family.py, substar_check.py): for N = g Q the gap-weighted
  inequality at the smallest admissible lam is Gval = 2 g^2 Psi(x) with
  Psi = (n-4)(2q - 1) - 2(n-3) p3^2 + (n-1)(n^2 - 6n + 6 + 2nq) m. Numerical minimum 0 for n = 4..8, at the star
  for n >= 5. Psi >= 0 is not proved; the averaged bounds lose for 2/3 < u < (n-1)/n.
- Independent readings by an agent (one reader; a second is still owed before anything is claimed):
  N4_PROOF.md, Proposition 1, Lemma 2 and Theorem 3 read line by line, the case analysis of Theorem 3 compiled in
  Lean 4 with Mathlib (standard axioms); the Caputo-Liggett-Richthammer reduction for [3,1] was not re-derived.
  Brain main 98b53434, 06_math_research/lean_checks_agent/t104_alon_n4/.
  HOOKS_AND_TWO_ROWS.md sections 1-3 and 7 (Lemma H, conjugation, the [n-2,2] model, Lemma U) checked with the
  reader's own code on 60 random graphs, n = 4..6 and all k, model n = 5..7, largest deviation 1.4e-14.
  Brain main 6abb227c, .../t104_alon_n4/hooks_referee/. Sections 4-5 were not refereed (conjectural). The reader's
  wording point on the norm identity in section 3 is applied.
- Reduction of Psi >= 0 on the two-eigenvalue family (GAP_STATE_FORM.md, last three sections; candidate):
  Psi = K((n-1)m - 1/n) + 2(n-3)D with D = q - 1/n - p3^2 >= 0, so Psi >= 0 once m >= 1/(n(n-1));
  m >= M = (1 - q + 2 S p3 - S^2)/(n(n-1)S^2 - 1) with S the coordinate of largest modulus; hence it is enough
  that Phi' = K N + 2n(n-3)(n(n-1)S^2 - 1) D >= 0, N = n(n-1)(1 - q + 2 S p3 - 2 S^2) + 1. Phi' is concave in
  (q, p3) for fixed S and n >= 5. The M bound and the concavity were checked by an agent (by hand and
  numerically; smallest Phi' found -2e-12, no negative Psi for n = 5..12; mesh answer 11 Nov 02:17Z).
  Phi' >= 0 is not proved. The relaxation to arbitrary measures is false (phi_boundary_scan.out, negative near
  S^2 = 0.41..0.44 at fractional multiplicities); vectors with integer multiplicities pass on a grid for
  n = 5..12 (phi_integer_scan.out), with zeros only at the edge and the star. A proof has to use integrality.

## 11 Nov, second audit of the n = 4 proof

A Codex referee (gpt-6.1-sol, high, Mac mini 1) read N4_PROOF.md cold and returned SOUND: every numbered statement CORRECT, its own
check on 32,000 random weighted graphs found no ratio below 2/3. With an agent's reading (and their Lean check of the case
analysis) the n = 4 case has two independent readings. The paper does not contain it. Files: AUDIT2_CODEX_N4_REPORT.md,
AUDIT2_CODEX_N4_LOG.md. Owed: the two wording points in the status line of N4_PROOF.md; a decision on a short note (n = 4 alone is
a small case of a three-week-old conjecture; it is better as one section of a note that also has the dual form, the hooks lemmas and
the two-eigenvalue reduction once those have a second reading).

11 Nov 08:42. Psi >= 0 for every n >= 5 has its two readers: an agent (no gap; Lean for steps 1 to 3) and a Codex referee (SOUND; corrections applied in GAP_STATE_FORM.md, marked [referee]; report AUDIT_CODEX_ALLN_REPORT.md). New section "What Psi >= 0 gives": Conjecture F holds on weighted graphs with two Laplacian eigenvalues (family of dimension n, both equality cases inside), checked directly for n = 5, 6, 7 (family_F_check.py). Conjecture F in general and Conjecture 1.5 are open; the row is not solved. Open side question: two negative values of Gval at n = 5 at a double top eigenvalue (gap_n5.out on Mac mini 1), being checked next to the crossing (gval_n5_check2.py).

11 Nov 09:16. an agent formalised the whole theorem for n >= 14 in Lean, normalisation included (T104Full.psi_nonneg, lean_checks_agent/t104_all_n_full, commit 952215e, standard axioms).

11 Nov 10:20. n = 5 side question answered numerically: the gap-weighted state inequality Gval >= 0 fails on graphs with a simple top eigenvalue close to a double one (Gval about 6.4 gap - 0.0024, negative for gap below about 3e-4; gval_n5_check2.out, section "n = 5: Gval < 0 next to a double top eigenvalue" of GAP_STATE_FORM.md). The single-eigenvector state cannot prove Conjecture F at n = 5 on all graphs; a state using the near-top eigenspace is needed. Conjecture F and the two-eigenvalue theorem are untouched. One implementation, not recomputed independently. A search of arXiv on the same day (dl_lit14.out in the top-200 vetting folder, 15 records) found no paper after arXiv 2610.22151 on its Conjecture 1.5.

## 11 Nov, 20:00: the note, and the operator form of the two-eigenvalue theorem

- T104_NOTE.md written: dual form, conjugation and hooks, n = 4, Conjecture F, the theorem for graphs with two
  Laplacian eigenvalues, Psi >= 0, remarks. NOT posted anywhere. Owed before any posting: the citation pass
  (C01-C16), with the title of arXiv 2610.22151, the page numbers of Bacher 1994 and Oliveira 2013, whether Alon's
  paper already has the hook statement or the n = 4 case, and the follow-up papers (arXiv 2609.10450, 2608.20613,
  2607.29018, 2511.03402, 2402.02427) checked for overlap; then a referee reading of the assembled note.
- New in the note, not in the earlier files: Theorem 5.3, the operator form
      lambda_max( sum_{i<j} x_i x_j rho_[n-2,2]((i j)) ) >= 1/2 - 2(n-1) max_{i<j} x_i x_j   (unit sum-zero x, n >= 5),
  equivalent to Conjecture F on the graphs w_ij = c - g x_i x_j, and Lemma 5.4, a direct derivation in the matrix
  model of the identity (R(x) - 1/2 + 2(n-1) m) Z = (2/(n-2)^2) Psi(x) for the uniform state on {1, x}^perp, with
  Z = (n^2 - 6n + 6 + 2nq)/(n-2)^2. This replaces the route through Gval and Reduction R in the proof of the theorem.
  Derived by hand (pair sums of x_i x_j, x_i x_j d^2, x_i x_j d^4; p_6 cancels) and checked by thmB_check.py
  (thmB_check.out): for n = 5, 6, 7, 8, 4 on 2002, 1502, 1002, 502, 502 vectors the ratio (R - rhs) Z / Psi is
  2/(n-2)^2 to 12 digits, and min(lambda_max(X) - rhs) is 0 to rounding, attained at the edge and star vectors.
  One author, one implementation; the lemma has not been read by a second reader.
- Not in the note: the n = 5 failure of the single-eigenvector state for general graphs (GAP_STATE_FORM.md, last
  section), which is numerical and from one implementation.

## 11 Nov, 00:00: referee report on the note, and the citation pass so far

- Codex referee (gpt-6.1-sol, high, Mac mini 1, a copy of the note with no history, no browsing): Theorem 5.2 SOUND,
  Theorem 5.3 SOUND. Items 1-7 CORRECT (matrix model, star and edge, two-eigenvalue parametrisation, Lemma 5.4 with
  exact rational residuals 0 at n = 4..7, deduction and equality cases, direct Young-form check at n = 5, 6 with least
  ratios 3/4 and 4/5, cone reduction). The finite certificate was reproduced independently for every n = 5..13 on both
  cones: no negative coefficient (one zero coefficient on R1, two on R2 in every case). Files
  AUDIT_CODEX_NOTE_REPORT.md, AUDIT_CODEX_NOTE_LOG.md. Its scripts and certificate files stayed on Mac mini 1 in
  ~/agent_run/NOTE (not copied here).
- Item 8 WRONG, one sentence: the last paragraph of Section 5 said the state A A^*/tr(A A^*) is "matched" to x in the
  terms of Proposition 2.1. It is not: at n = 5, x = (1,1,0,0,-2)/sqrt 6, transposition (1 5),
  tr(D rho_[3,2]((1 5))) = -5/18 and the single-transposition inequality reads 1/2 >= 13/24. Recomputed here by
  state_check_n5.py (state_check_n5.out): tr(A A^*) = 2, the inequality fails by 1/24 at (1 5) and (2 5) and holds at
  the other eight transpositions; the sum against the weights m - x_i x_j is +0.8333. Neither theorem uses the
  sentence. It agrees with the earlier n = 5 finding that the single-eigenvector state does not prove Conjecture F
  for general graphs.
- Changes made to T104_NOTE.md: that paragraph now says the comparison holds only after summation against the
  weights, with the example; Lemma 5.4 states n >= 5; the proof for 5 <= n <= 13 says how the rays are enumerated
  (at most three nonzero gap coordinates); the horizontal-strip remark is restricted to a nonempty set; the numerical
  paragraph says "smallest ratios found".
- Independent checks by an agent (brain repo, 06_math_research/lean_checks_agent/): Theorem 3 of
  N4_PROOF.md (lambda_max(L_G) <= (4/3)W + (2/3)D) is a Lean proof (t104_n4, commit 5d3c8699; Lemma 2, the
  representation step, is not formalised); Lemma 5.4's two identities hold to 4e-15 at 640 random unit vectors,
  n = 5..8, with M_n built as an eigenspace of the transposition class sum (t104_lemma54, commit abdef0b).
- Citation pass, done so far from Alon's paper (lit/2610.22151.pdf): reference [1] now carries the title "Spectral
  comparison on Specht modules and mixing of the interchange process"; Conjecture 1.5, Theorem 1.8 and Theorem 4.5
  are quoted as they stand there; the introduction now names the cases Alon lists as proved (complete and
  quasi-complete graphs, the pairs of Alon-Kozma in the Aldous order, sigma = [n-1,1] by CLR); Alon-Kozma, Canad.
  Math. Bull. 56 (2013), 13-30, added as [5]. A word search of Alon's text finds no hook statement, no conjugation or
  exterior-power argument and no n = 4 theorem (lossy text file; Sections 3-4 not yet read line by line).
- Citation pass, still owed before any posting: read Alon-Kozma for hook pairs and the exterior-power description
  (Proposition 3.1 may overlap with it); confirm Bacher 1994 pages 460-472; whether Hermon-Salez (Ann. Appl. Probab.
  31 (2021)) should be cited for Oliveira's conjecture, which Alon cites as [7, Conjecture 1]; arXiv 2609.10450,
  2608.20613, 2607.29018, 2511.03402, 2402.02427 for overlap; then hooks C01-C16.
- Not extended: the uniqueness of the equality cases is proved for n >= 14 only.

## 12 Nov, 00:04: citation pass, Alon-Kozma read (lit/ak2013/1003.1710v2.pdf, ak.txt)

- Alon-Kozma (arXiv 1003.1710v2; Canad. Math. Bull. 56 (2013) 13-30) already contains three things the note used
  without attribution:
  (1) the hooks are ordered among themselves, [n] > [n-1,1] > [n-2,1^2] > ... > [1^n] (their (10), "basically a
      result of Bacher": the eigenvalues on [n-k,1^k] are the sums of k-tuples of the eigenvalues on [n-1,1]), and
      Appendix A proves that Bacher's wedge powers are the hook Specht modules. So Lemma 3.2 is Bacher's, and
      Proposition 3.1 is new only in the constant k/j.
  (2) Corollary 2: [n] > sigma > [1^n] for every sigma, by lambda_1(A; [1^n]) = 2 Wt(A): the tau = [1^n] case.
  (3) Corollary 1: [2,2,1^(n-4)] is not above [2,1^(n-2)], shown on the star: the star values n-2 and n-1 of Section 5
      and the fact that the constant of Conjecture F cannot exceed (n-2)/(n-1).
  Also [tau'] = [tau] tensor sgn (their (4)), the conjugation used in (3.1).
- T104_NOTE.md now says so: the statement of Proposition 3.1 in Section 1, Lemma 3.2 "(Bacher [2])" with the
  identification cited to [5, Appendix A], the tau = [1^n] case cited to [5, Corollary 2], and the star values cited
  to [5, Corollary 1] after Conjecture F.
- Bacher's reference confirmed from Alon-Kozma's list: J. Algebra 167:2 (1994), 460-472.
- What stays new in the note after this reading: the dual form (Prop. 2.1), the constant k/j for hooks, Theorem 4.2
  (n = 4 with constant 2/3), Conjecture F as a statement with the constant (n-2)/(n-1), Theorems 5.2/5.3, Lemma 5.4,
  Theorem 6.1. Not yet checked against the five follow-up arXiv papers or Hermon-Salez; Section 5's star paragraph
  should also carry the citation to [5, Corollary 1] where the values are computed.

## 12 Nov, 00:12: citation pass finished for the note as it stands (hooks C01-C13 gone through by hand)

- Follow-up papers, by abstract (lit/followups/ids.xml): arXiv 2609.10450 (Caputo, Quattropani, Sau), 2608.20613
  (Zhu), 2607.29018 (Lv, Zhou), 2511.03402 (Belotserkovskiy, Chen), 2402.02427 (Li, Xia, Zhou). All five are about
  which representation carries the spectral gap (other generating sets, wreath products, exchange models) or about
  the gap eigenspace. None compares lambda_min between two non-trivial Specht modules of a transposition Laplacian.
  Abstracts only: the papers themselves were not read.
- Forward citations of Alon's preprint (C05; Semantic Scholar, lit/refcheck/fwd.json): one, arXiv 2606.29829v2
  (Amir, Ghosh, noise sensitivity on S_n under the interchange process). No overlap by its abstract.
- Alon's paper re-extracted as UTF-8 (lit/alon_utf8.txt; the earlier .txt was lossy). Statements of Sections 3-4:
  Lemmas 3.4-3.6, proofs of Theorems 1.4 and 1.3, Definition 4.1, Lemma 4.2, Theorem 4.4 (quasi-complete graphs).
  No dual or semidefinite formulation, no hook or exterior-power statement, no n = 4 theorem, no two-eigenvalue
  family. Statements and a word search, not a line-by-line reading of the proofs.
- C06 (borrowed lemmas): Jucys-Murphy contents and Young's orthogonal form now cite Okounkov-Vershik [7]
  (Selecta Math. (N.S.) 2 (1996); title, journal, volume and year confirmed on Crossref, DOI 10.1007/bf02433451;
  pages 581-605 are from memory, Crossref carries none).
- C09 (software): the exact expansion for n <= 11 ran in SymPy (split_cert.py: sympy.polys.rings); the note now says
  so and cites Meurer et al. [6] (PeerJ Comput. Sci. 3 (2017) e103, confirmed on Crossref, DOI 10.7717/peerj-cs.103).
- C10 (our brain): math_recall finds our own card "T104 Alon 2/3 two-eigenvalue family" and the Oliveira and
  Caputo-Liggett-Richthammer cards; nothing of ours that the note should cite.
- C13: no sentence of the note is about its own writing (grep clean).
- Section 5 cites [5, Corollary 1] at the star values. Oliveira's conjecture stays cited to [4], with
  [1, Theorem 1.8] for the implication.
- C14-C16 apply only when the note is posted; it has not been, and T104 itself is not solved.
- Open before posting: confirm the Okounkov-Vershik pages from the journal; read the five follow-ups' introductions
  if the note is ever submitted anywhere.

## 12 Nov, 00:14: dated arXiv search (C11)

- Two arXiv queries, newest first ("interchange process" with Specht / irreducible representations / Aldous order;
  "interchange process" with eigenvalue; lit/refcheck/recent1.xml, recent2.xml). Since June 2026 they return only
  Alon's preprint (15 Oct 2026), Zhu 2608.20613 and Lv-Zhou 2607.29018. Nothing after Alon's preprint on comparing
  Specht modules. Two queries, not a full search: a paper that avoids the words "interchange process" is not seen.
- Durable memory filed: t104_note_what_is_ours_and_what_is_bacher_alon_kozma_2026_11_12.

## 12 Nov, 00:16: the referee's files are home; what the Lean theorem covers

- referee_scripts/: the Codex referee's working folder from Mac mini 1, unpacked (the repo ignores archives)
  (~/agent_run/NOTE); it travelled as one archive, 67 files, 402,637 bytes, sha256
  8119a4672cffd85cb012eb2ed95880cc872d6ee1de5586378047d9115729e285, equal on both machines. The compiled binary and
  the pid file are left out. Inside: referee.py, certificate_stream.cpp, the certificates, step*.json, its log and
  report). Scanned for credential-shaped strings before it was committed: none. The folder on Mac mini 1 may now be
  cleaned.
- Lean (an agent, brain repo commit 952215e, 06_math_research/lean_checks_agent/t104_all_n_full):
  T104Full.psi_nonneg states, for every n >= 14, every nonzero x with sum zero and every M' with x_i x_j <= M' for
  all i != j, that G(n, T, P, Q, M') >= 0, where G is literally the G_{M'} of the note (Section 6). With
  M' = max_{i<j} x_i x_j this is Theorem 6.1 (Psi >= 0) for n >= 14. Axioms: propext, Classical.choice, Quot.sound.
  Read from its README, its theorem line and its compiler output; I did not recompile it.
- So for the two-eigenvalue family: the scalar inequality is machine-checked for n >= 14, certified by exact
  arithmetic for n = 5..13 (ours, reproduced by the referee), and the representation step (Lemma 5.4) rests on the
  proof in the note, the referee's exact check at n = 4..7 and agent's numerics at n = 5..8. Lemma 5.4 is the
  piece with no formal proof.

## 12 Nov, 00:25: n = 5 near a double top eigenvalue, recomputed with an explicit model of V_[3,2]

- state_mix_n5.py / .out, state_mix_n5_id.py / .out; written up in GAP_STATE_FORM.md (last section).
- The closed formula for Gval and the explicit model agree (300 graphs, ratio 1 to 4e-13). The earlier finding
  stands: the state built from the single top eigenvector fails next to the two graphs with a double top eigenvalue.
- With x chosen in the plane of the top two eigenvectors the same construction gives slack at least 1.40 at both
  graphs and on 400 perturbations of each (true slack 3.2). The failure is the choice of x, not the graphs.
- Open: is the maximum over the plane nonnegative on every weighted graph on 5 vertices (min-max search, to be
  queued as a 1-core job). Nothing here changes the status of row T104: not solved.

## 12 Nov, 00:30: min-max search at n = 5 queued

- minmax_n5.py: F(G) = max over unit x in the plane of the top two eigenvectors of s(G, x); Nelder-Mead over the
  weights from ten families of starts (random, sparse, star, edge, two edges, the two graphs with a double top
  eigenvalue, triangle plus edge, path, complete). Smoke test, ten short starts on the laptop: smallest F 2.5e-9 at
  a single edge, no negative value; the two double-eigenvalue graphs give F = 1.39.
- Queued on Mac mini 1 as a one-core job (~/t104_alon, 300 starts, seed 21, output minmax_n5.out, stop file
  STOP_minmax_n5). Result not in yet.

## 12 Nov, 07:08: the n = 5 min-max search is in; stars with isolated vertices; H queued

- minmax_n5.out (300 starts): no negative value of F. End points: 95 at the edge and 53 at the uniform star (F = 0,
  the graphs of slack 0), 49 at K_{1,2} with two isolated vertices (F = 1/50), 22 at K_{1,3} with one (F = 1/69),
  the rest far above or not converged. GAP_STATE_FORM.md has the table.
- star_gval_exact.out: the top-eigenvector state on K_{1,k} with isolated vertices, exact, n = 5 to 40: positive for
  1 < k < n-1, smallest at k = n-2, about 1/n^2.
- At K_{1,2} and K_{1,3} (n = 5) the maximum of s(G, x) over all x equals the true slack; the best x is not in the
  top two-plane.
- beta_state_n5.out: the eigenvalue-weighted state D_beta removes the failure next to a double top eigenvalue for
  beta from 30 to 300; a fixed beta fails next to the uniform star by about exp(-1.6 beta) (seen at beta = 10).
- Queued on Mac mini 1: job 21_agent_minbeta_n5 (minbeta_n5.py 2000 31 4000; output ~/t104_alon/minbeta_n5.out;
  pid file minbeta_n5.pid; stop file STOP_minbeta_n5). About 6 s a start on the laptop.
- Running on the laptop when this was written: star_states_n.py 6 8 3 (star_states_n6_8.out, not pushed yet); the
  n = 6 lines agree with the exact values.
- Next: read minbeta_n5.out. If H >= 0 everywhere, look for the closed form of the pair terms of D_beta (each is
  a polynomial in the eigen-data, as Gval is) and for the first-order expansion at the uniform star and at the
  edge. Row T104: not solved.

## 12 Nov 14:28 - n = 5: s_30 and H have no negative end point in 2,000 minimisations
The Mac mini 1 run (minbeta_n5.py, 13,783 s) is in GAP_STATE_FORM.md, last section: s_10 fails next to the uniform
star (-1.6e-8, 448 end points), the top-eigenvector control fails next to a double top eigenvalue (-0.48, 249 end
points), s_30 and H have none below -1e-10. The smallest H/slack with slack above 1e-3 is 1/46, at K_{1,3} plus one
isolated vertex. Numerical; H >= 0 at n = 5 is not proved. Next: second order expansion of s_beta next to the uniform
star with beta of order log(1/distance); an independent second implementation of D_beta.

## 12 Nov 14:38 - a batched GPU version of the H search, n = 6 not yet controlled
t104_gpu_hsearch.py evaluates s_beta and H for any n in float64 with torch, batched, and minimises by a (1+1)
evolution strategy per graph. It agrees with a direct numpy evaluation to 4.9e-15 (n = 6) and 1.7e-14 (n = 5) on 200
graphs. One run on the laptop GPU at n = 6 (t104_gpu_n6_test.out; 4 rounds of 4,096 graphs, 400 steps): no value of H
below -1e-10, but the beta = 1e6 control was not negative either, so that run does not test anything: its starts did
not include graphs next to a double top eigenvalue. Starts built from two components with equal top eigenvalues
(kind 8) are added and not yet run. The laptop's GPU guard now refuses local CUDA torch runs, and MPS on the Mac minis
has no float64, so the next run of this script is on CPU, n = 5 first (the control must come out negative), then n = 6.

## 12 Nov 15:08 - the batched search is controlled at n = 6: s_10 fails next to the star, H does not
The batched code is right and its first runs were not. At the two n = 5 graphs where minbeta_n5 found the
top-eigenvector state failing, it gives that control at -0.40 and -0.29 (direct numpy evaluation agrees to all
printed digits; the log's -0.48 is at unrounded weights, and the gap of 8e-6 moves with the tenth digit), and H at
+1.41 there; at the near-star graph it gives s_10 = -1.58e-8 as the log does (t104_eval_bad.out). The beta = 1e6
failure is a needle: it needs the top gap tuned to about 1e-5, and away from that the value is flat near +1.4, so a
random-step search cannot find it, and it is not used as the control any more (--control BETA selects one).
s_10 next to the uniform star does have a basin, at n = 6 as at n = 5 (t104_star_scan_n6.out: smallest s_10 is
-4.6e-8 at leaf weights 1/5 + (d, 0, -d, 0, 0), d = 1.6e-4, with H = +5.0e-8 at the same graph). With a start family
that perturbs only the star's leaf weights (kind 11), the search at n = 6 on the laptop CPU (t104_cpu_n6_control10.out;
3 rounds of 1,024 graphs, 300 steps each) finds the beta = 10 control below -1e-10 at 254 of 3,072 end points, smallest
-4.71e-8, all next to the star, and H at none; the smallest end value of H is +1.4e-12. At n = 5 the same control
fires at 1 of 4,096 end points (-1.04e-8, before kind 11 existed), H at none.
Numerical, one implementation, a weak optimiser: it says H shows no failure where the search can see the failure
of a fixed beta, not that H >= 0 at n = 6. Next: a second implementation of D_beta by another reader; the second
order expansion of s_beta next to the star with beta of order log(1/distance), which is where H is smallest.

## 12 Nov 16:51 - next to the uniform star H >= s_inf, and s_inf = |delta|^2 + 4 eta + higher order
Where the top eigenvalue is simple, H = sup over beta of s_beta is at least the top-eigenvector state s_inf (the
other pairs carry exp(-beta gap/lam)), so the fixed-beta failure next to the star is no threat to H. Measured at
n = 5, 6, 7 (t104_star_local.py, .out): with leaf weights 1/(n-1) + delta and leaf-leaf weights of total eta,
s_inf = |delta|^2 + 4 eta + higher order, the same constants for each n, no negative value in any direction. If
proved, H > 0 on a punctured neighbourhood of the star. GAP_STATE_FORM.md, last section. Measured, not derived;
next is the perturbation computation. Row T104: not solved.

## 12 Nov 16:55 - the star expansion is fixed by symmetry and two constants, c = 1 and c1 = 4 (n = 5-12)
By the S_{n-1} symmetry of the star, s_inf = c1 eta + c |delta|^2 + O(eta |delta| + eta^2 + |delta|^3) (a proof: Schur
plus analyticity where the top eigenvalue is simple). Measured c = 1.000000, c1 = 4.000000 for n = 5 to 12
(t104_star_constants.py, .out), so H > 0 on a punctured neighbourhood of the star for those n. Constants measured,
not derived. Row T104: not solved.

## 12 Nov 17:16 - c = 1 and c1 = 4 proved for every n >= 5; the uniform star is an isolated equality case of H
Hand proof in GAP_STATE_FORM.md ("c = 1 and c1 = 4 for every n >= 5"): the branching [n-2,2] -> [n-3,2] + [n-2,1] (contents
n-3 and 0), the image of y -> Pi(u (x) y) in the [n-2,1] part, the transposition character, and dim V' = m(m-3)/2 give
c1 = 4 at first order and c = (n+1) - n = 1 at second order. Exact Kato expansion (t104_star_exact.py, .out) gives the
same rationals for n = 5, 6. So s_inf = 4 eta + |delta|^2 + higher order and H > 0 on a punctured neighbourhood of the
star for every n >= 5. Not independently audited. Row T104: not solved.

## 12 Nov 17:23 - the single-edge equality case is isolated too (first order); both equality cases of H are isolated
GAP_STATE_FORM.md ("The single-edge equality case is isolated too"): at one edge of weight 1 the top eigenvalue 2 is
simple and s_inf = (3/2) A + ((4n-10)/(n-3)) B + O(|w|^2), A the weight on edges touching the edge, B on the others.
Slopes from the S_2 x S_{n-2} symmetry: <K_23> = (n-5)/(n-3), <K_02> = 1/2; measured slopes n = 5..8 agree
(t104_edge_local.py, .out). With the star result, both equality cases are isolated for every n >= 5. What is left
for H >= 0 is global. Not independently audited. Row T104: not solved.

## 12 Nov 18:20 - uniform K_n is not a third equality case; a lambda_min(M) bound
The n = 5 control search stopped at uniform K_5 with H = -9e-16. That is the empty-quotient convention (every gap
is zero, the code returns -need, need = 0). GAP_STATE_FORM.md ("The uniformly weighted complete graph is not a third
equality case"): M(K_n) = (4/n) I by the content sum of [n-2,2], so H -> 4(n-2)/n near K_n; measured n = 5..8 at
eps 1e-3 (t104_kn_local.py, .out). Side bound H >= (n-2) lambda_min(M) - need settles about 12 per cent of sampled
graphs (t104_minM_bound.py, .out). Mini 2 searches (n = 5, 6 at distance 0.05-0.1 from the star and edge): no
negative H; the smallest values sit on the boundary of the excluded neighbourhoods. Row T104: not solved.

## 12 Nov 18:33 - the double-top stratum: sub-clique lemma
Where lambda_1 = lambda_2 the route H >= s_inf is unavailable. GAP_STATE_FORM.md ("H on the stratum where the top
eigenvalue is double"): the uniform K_k on k of the n vertices, 3 <= k < n, has H = 2(k-2)/(k-1) for every beta.
Only (Top, Zero) pairs have a gap; on Top (x) Zero each clique transposition acts on the Top factor alone, so M is
the scalar 2/(k-1) of the standard representation of S_k, and M commutes with the projection onto V_[n-2,2]
(t104_subclique.py/.out: n = 5..8; t104_subclique_eig.py/.out: eigenvector residual <= 7.5e-16). The triangle
(H = 1) is the smallest value seen on the stratum; that is measured only (t104_degen_top.py; mini 2 runs dg_n5/6/7
pending). t104_np_hsearch.py now also masks a neighbourhood of uniform K_n. Row T104: not solved.

## 12 Nov 18:58 - the double-top stratum: disjoint unions of cliques, and leaving the stratum
GAP_STATE_FORM.md ("Disjoint unions of cliques"): uniform cliques K_{a_1}, ..., K_{a_r}, edges of K_{a_i} weighted
proportionally to 1/a_i, have H = 2 - 2/D for every beta, D = sum (a_i - 1), when n - D >= 2 (proof; 23 unions,
n = 5..8, largest difference 4.9e-15, t104_degen_family.py/.out). The least value is 1, at the triangle and two
disjoint edges. C_5, C_7 and K_4 minus an edge measure above 1. Mac mini 2 double-top search n = 5 (dg_n5_s41,
1,667 rounds by 18:58): nothing below 1 on the stratum. Off the stratum H falls at unit rate in the gap: two edges
joined by a bridge of weight t give 1 - H = gap12 to 0.6 per cent for 1e-8 <= t <= 1e-3 (t104_2k2_bridge.py/.out,
beta to 1e10; the search grid stops at 1e6 and reads H low when gap12 < 1e-5). Far-region runs np_n5_a0.1,
np_n6_a0.05, np_n6_a0.1: no negative value so far. Open: H >= 1 on the stratum. Row T104: not solved.

## 12 Nov 19:20 - the beta -> infinity value on the double-top stratum
GAP_STATE_FORM.md ("The beta -> infinity value on the stratum"): on the stratum H >= s_inf, and
s_inf - 1 = (n-2)(R - lambda) + (1 - lambda), R the gap-weighted Rayleigh average of M over sym(Top (x) e_l).
Proved: lambda <= 1 on the stratum, with equality only at the balanced triangle and two equal disjoint edges; an
explicit edge formula for R - lambda (t104_R_identity.py, _n5.out, _n6.out, agreement 1e-14). Measured: H = s_inf
to 1.1e-5 at n = 5 (60 points), H - s_inf up to 0.09 at n = 6 (t104_sinf_stratum.py, _n5.out, _n6.out).
R >= lambda is false on the stratum (n = 5, seed 11, point 13: R - lambda = -0.0091, H = 1.12) and on 1,220 of
3,000 graphs off it (t104_R_vs_lambda.py, _n5.out); the statement to prove keeps the 1 - lambda term. Its ratio
(n-2)(lambda - R)/(1 - lambda) is at most 0.183 over 125 stratum points (limit 1). Mac mini 2 double-top search
n = 5 (t104_dg_n5_s41_snapshot.out): 4,036 rounds, no value below 1 on the stratum; least 0.999996, just off it.
Open: H >= 1 on the stratum. Row T104: not solved.

## 12 Nov 19:30 - the stratum target in closed form and in trace form
GAP_STATE_FORM.md ("A closed form of the stratum target"): with p = u * v and q_e = (b_e . u)(b_e . v),
|A|^2 = 1 - 2n/(n-2)|p|^2 and <A, M A> = lambda + mu - 2n/(n-2) p'Lp - 2 sum_e w_e q_e^2 (t104_R_closed.py,
_n5.out, _n6.out, agreement 1.1e-14). The target becomes 2 sum g sum w q^2 <= sum g P with P a sum of three
nonnegative terms; measured ratio at most 0.877 (C_5). Summed over pairs it has no basis left: a trace inequality
T(L, Pi_Top, lambda) >= 0 in five explicit sums (t104_trace_form.py, _n5.out, agreement 7.2e-15, s_inf to 4.1e-14).
Open: prove T >= 0 (start with D = 2). Row T104: not solved.

## 12 Nov 19:37 - the stratum target split by terms, and as a sum over edges
GAP_STATE_FORM.md ("Which terms carry the bound", "The eigenvalue term is a sum over edges"): writing the trace
target as X1 + X2 + X3 - Y, no two of the three positive terms suffice at n = 5 (t104_trace_terms.py, _n5.out,
_n6.out). Since tr L = 2, X1 = D sum_e w_e gamma_e with gamma_e = b_e' G b_e >= 0, and the target becomes
sum_e w_e gamma_e (2 tau_e - D) <= X2 + X3, tau_e = |Pi b_e|^2: only edges with more than D/2 of their squared
length in Top push against it (t104_edge_excess.py, _n5.out, agreement 2.1e-15, ratio at most 0.661 on 15 points).
Open: prove it (start with D = 2). Row T104: not solved.

## 12 Nov 19:45 - C_5 and the seed-11 point edge by edge
GAP_STATE_FORM.md ("C_5 as the test case for the edge-sum target"): at C_5 every edge has tau = 2 lambda > 1, left side
gamma (4 lambda - 2) = 0.2211 exactly, X2 = 4/15, ratio 0.6875 (t104_c5_terms.py, .out). The seed-11 point: heavy edges
lie almost in Top and cost little, ratio 0.503 (t104_seed11_edges.py, .out). Proved: gamma_e <= lambda (2 - tau_e); alone
it fails at C_5 (0.358 against 0.322), so the gap weights must be kept. Row T104: not solved.

## 12 Nov 19:53 - the target does not split by pairs or by low eigenvectors
GAP_STATE_FORM.md ("The target does not split by pairs, nor by low eigenvectors"): the trace form is the closed form
summed with gap weights. Pair by pair it is false (ratio 1.370, t104_per_pair.py, _n5.out); per low eigenvector with the
trace over Top it is false barely (1.020 at the seed-11 point, t104_per_l.py, _n5.out). A proof must use the gap-weighted
sum over low eigenvectors. Row T104: not solved.

## 12 Nov 20:03 - the sum over low eigenvectors, and a search for the worst point
GAP_STATE_FORM.md ("What the sum over low eigenvectors buys"): a Chebyshev step across low eigenvectors fails (F_l not
ordered like the gaps, t104_chebyshev.py, _n5.out, _n6.out); F_l < 0 at only 2 of 27 points. Penalised Nelder-Mead on the
margin ratio at n = 5 reaches 0.8733, below C_5's 0.8769 (t104_worst_ratio.py, _n5.out). Row T104: not solved.

## 12 Nov 20:27 - circulants, and C_5 a local maximum of the margin ratio
GAP_STATE_FORM.md ("Circulants", "C_5 is a local maximum of the margin ratio"): every circulant on odd n lies on the
stratum; the ratio sum g Q / sum g P at C_n is 0.8769 / 0.6538 / 0.5075 for n = 5, 7, 9 and no random circulant beats
C_n (t104_circulant_ratio.py, .out). 75 points pulled back onto the stratum within L1 distance 0.48 of C_5 all have a
smaller ratio, largest 0.876686 against 0.876857 (t104_c5_local.py, t104_c5_local_s7.out). Measured picture: C_5 is the
maximum at n = 5, at 0.877 of the limit 1. Open: a proof. Row T104: not solved.

## 12 Nov 20:41 - first-order conditions at C_5
GAP_STATE_FORM.md ("First-order conditions at C_5"): on the 7-dimensional stratum near C_5 the margin ratio falls at
slope -0.380 per unit of chord weight and as -2.047 s^2 along the 2-dimensional cycle face, the same in every direction
(t104_c5_first_order.py, .out). C_5 is a strict local maximum of the ratio (0.877 of the limit 1); constants measured.
Open: a proof of ratio <= 1 on the whole stratum. Row T104: not solved.

## 12 Nov 20:54 - C_7 is also a strict local maximum of the margin ratio
GAP_STATE_FORM.md ("The same at C_7"): chords lower the ratio at slope -0.658 (distance 2) and -0.129 (distance 3);
on the 4-dimensional cycle face it falls quadratically, curvature -9.4 to -11.0 on four directions (t104_cn_first_order.py,
t104_cn_first_order_n7.out). C_7 ratio 0.654 of the limit 1. Open: a proof of ratio <= 1. Row T104: not solved.

## 12 Nov 21:02 - the double-top searches at n = 6 and n = 7 are complete
GAP_STATE_FORM.md ("The double-top searches at n = 6 and n = 7"): Mac mini 2, one hour each: n = 6, 301,525 stratum points,
no negative, smallest H 1.000009 at the balanced triangle; n = 7, 179,303 points, no negative, smallest H 1.000014 at two
equal disjoint edges (t104_dg_n6_s42_snapshot.out, t104_dg_n7_s43_snapshot.out). Near-minimal rounds all carry two or three
heavy edges: no basin near 1 other than the equality cases. Open: a proof of H >= 1 on the stratum. Row T104: not solved.

## 12 Nov 21:18 - the stratum claim holds on odd circulants with n >= 21 (proved)
GAP_STATE_FORM.md ("Odd circulants with n >= 21"): with a unique top frequency both sides of the target are explicit
Fourier sums (checked against the direct computation to 2e-15, t104_circ_fourier.py, _out); Cauchy-Schwarz on the Q side and
three crude bounds on the P side reduce the claim to a linear inequality in lambda whose end values are explicit rational
functions, positive for n >= 21 (t104_circ_linear.py, t104_circ_ends.py, t104_circ_linear.out). n = 5..19, even n and tied top
frequencies remain; for fixed k both sides are quadratic in the weights. Row T104: not solved.

## 12 Nov 21:27 - odd circulants n = 5..17: face search finds the claim holds
GAP_STATE_FORM.md ("Odd circulants with n <= 17: an exact face search"): for each top frequency F = sum gP - sum gQ is a
quadratic on a polytope; enumerating all faces' KKT points gives min F = 0 only at K_n, every other KKT point >= 0.026
(t104_circ_qp.py, t104_circ_qp_5_13.out, t104_circ_qp_15_17.out). NUMERICAL (floating point). With push 126 only n = 19 is
missing among odd circulants with a unique top frequency (running). Row T104: not solved.

## 12 Nov 21:38 - proved: all circulants, every D >= 4, constant-diagonal projectors with n >= 8
GAP_STATE_FORM.md ("All weighted circulants, all D >= 4, and constant-diagonal projectors with n >= 8"): Codex worker STRAT
(t104_strat_RESULT.md) with an independent audit (t104_strat_audit.py/.out: sector vertices, every certificate entry from the pair
definitions to 6.5e-16, exact n = 7 bracket). D >= 4: Qtotal <= (4/D) X1. Pi_ii = D/n, n >= 8: Qtotal <= (8/n) X1. n = 5, 6, 7
circulants: nonnegative midpoint certificates. n = 19 face search agrees (t104_circ_qp_19.out). Open: D = 2, 3 with nonconstant
diag Pi. Row T104: not solved.

## 12 Nov 21:56 - uniform joins with a capped interior proved; the diagonal route is dead
GAP_STATE_FORM.md ("Uniform joins with a capped interior"): q >= 3 blocks of any sizes, weight t on every cross pair,
any interior graph with largest Laplacian eigenvalue below a t. T >= 0 for all of them: q = 3 by X1 + X2 >= 2 S5 one
eigenvalue of G_a at a time, endpoint margin (n-2-a)((n-1)a-n), plus X3 >= 0; q = 4 by X1 alone. Unequal blocks give a
nonconstant diag Pi. From Codex STRAT2, rederived and checked on 400 random joins (t104_join_audit.py, _audit.out).
Bounding tau by (sqrt Pi_ii + sqrt Pi_jj)^2 fails at n = 5 by 3.65 percent (t104_diag_route.py, _n5.out).
Open: D = 2, 3 with nonconstant diag Pi outside the join family. Row T104: not solved.

## 12 Nov 22:29 - a neighbourhood of K_n, and n = 5 with D = 3
GAP_STATE_FORM.md ("A neighbourhood of the complete graph, and n = 5 with D = 3"): T >= 0 on the whole stratum when
s = (n-1)lambda - 2 <= eps_n = (n-4)(3n-8)/[(n-1)(n-2)^2(n+4) - (n-4)^2], every D, any diag Pi; and at n = 5, D = 3 when
lambda <= 187/304. Proofs in t104_strat2_result.md (Codex STRAT2); audited by t104_strat2_audit.py (3000 graphs) and
t104_strat2_sym.py (exact algebra). Equitable partitions: X1 + X2 >= 2S5 on every instance of t104_equitable_test.py,
no proof. Row T104: not solved; open for D = 2, 3 outside joins and the K_n neighbourhood.

## 12 Nov 23:16 - n = 5 with D = 3 in full; equitable partitions
GAP_STATE_FORM.md ("n = 5 with D = 3 in full, and equitable partitions into three or four blocks"): T >= g/9 on the whole
n = 5, D = 3 stratum (moment bound m4 <= p + (3+5p) m3^2/4 plus the weight bound p <= (2+g)/(20g)); T > 0 for every
equitable partition into 3 or 4 blocks with the block contrasts on top; X1 + X2 >= 2S5 fails at block sizes 1,2,2
(exact example, margin -143/10000, T = 241/5000). Proofs t104_strat3_result.md (Codex STRAT3), audits strat3/exact_audit.py
and t104_strat3_audit.py (all identities exact, 371 random 1,a,b graphs). D = 2 worst ratio 2S5-side / rest, 60 starts each:
0.937 (n = 5), 0.835 (n = 6), 0.794 (n = 7), all below 1. Row T104: not solved; open for D = 2, 3 with a top space not
spanned by block contrasts.

## 13 Nov 00:17 - n = 5 with D = 2: disconnected graphs and three connected regions
GAP_STATE_FORM.md ("n = 5 with D = 2: disconnected graphs and three regions of the connected stratum"): T >= 0 for every
disconnected graph on the stratum (equality only at the balanced triangle plus two isolates and two edges of weight 1/2
plus an isolate); for connected graphs T >= 0 when a <= A0(b/a) (at least 4/11, 7/16 at equal gaps) and T >= 2a/2025 when
b/a <= 1/3000. Proofs t104_strat4_result.md (Codex STRAT4); its four exact certificates rerun here; black-box checks
t104_audit_isolated.py (40,000 graphs) and t104_audit_regions.py (9,000 frames). Worst quotient found 0.020276351509456
(triangle + pendant + isolate), numerical only. Row T104: not solved; open on the rest of connected n = 5, D = 2 and n >= 6.

## 13 Nov 01:15 - n = 5 with D = 2: five connected classes
GAP_STATE_FORM.md ("n = 5 with D = 2: more of the connected stratum"): T >= 0 for a <= 443/1000 (and a <= A1(r)), for
b/a <= 3/25 (quartic SOS certificate), on forty rational cells for 3/5 <= b/a <= 1, for equal gaps up to 0.5491, and for every
disconnected frame plus a uniform complete graph. Connected graphs approach the disconnected infimum 0.020276 (exact witnesses).
Proofs t104_strat5_result.md (Codex STRAT5); its six replay scripts rerun here; exact rechecks t104_strat5_psd_check.py and
t104_strat5_quartic_check.py; black-box t104_audit_strat5.py (12,000 frames, T > 0). Row T104: not solved; open on the rest of
connected n = 5, D = 2 and n >= 6.

## 13 Nov 02:34 - n = 5 with D = 2: radial reduction, ceiling 103/200
GAP_STATE_FORM.md ("the radial reduction and a larger connected region"): T(a, ar) is a(1 - a/a_end)L + (a/a_end)^2 T(a_end),
so each ray reduces to its far end; 176 rational cells give T >= 0 for a <= 103/200 on 3/25 <= r <= 1; equal gaps up to the
cubic root G ~ 0.551713; 47 boxes on the zero-weight face. Proof t104_strat6_result.md (Codex STRAT6), nine replays rerun here,
black-box audits t104_audit_strat6_result.py and t104_audit_strat6_final.py (no negative T). Row T104: not solved; open on the
residual connected region described there and n >= 6.
Disconnected N = 6, D = 2 (Codex STRAT7, t104_strat7_result.md): every class except 5+1 proved, 5+1 proved for internal
scale a <= 11/25; seven replays rerun here; black-box t104_audit_strat7_classes.py (least T -3e-16; equality cases T = 0).

## 13 Nov 03:42 - 5+1 at N = 6 to a <= 14/25; residual face boxes
GAP_STATE_FORM.md ("the 5+1 class and the residual face"): Codex STRAT9 (t104_strat9_result.md) proves T >= 0 for the 5+1 class at
N = 6 for every frame with a <= 14/25, at every scale when b/a <= 3/20, and up to the ratio-strip ceilings 66/125 to 76/125; for
every N >= 6, a <= 64/125. Codex STRAT8 (t104_strat8_result.md) adds 43 face boxes on the n = 5 residual and an exact partition of
the face chart (24,702 nonnegative, 10,208 excluded, 5,272 open leaves). Both exact replays rerun on Mac mini 2 (strat8/ and
strat9/replay_mini2.txt). Black-box audits t104_audit_strat9_51.py (least T 0.1397 on 5+1); t104_audit_strat6_final.py on the 176 final cells is still
running. STRAT4 rank-one certificate files added (rank_one_matrices.json and the two scripts that
write and recheck it). Row T104: not solved; open on the stated residual regions and n >= 6 connected.

## 13 Nov 06:16 - STRAT6 final-cell audit finished; N5 step written out
t104_audit_strat6_final.py on all 176 cells at their ceilings (528 points): least T 7.0285e-02 strong, 6.9545e-02 enhanced,
7.4922e-02 directional; 7.8453e-02 at the uniform ceiling a = 103/200 over 23 ratios. No negative T. In t104_strat4_result.md
the bound 2|df| <= 3/5 in (N5) now states its two inputs (d^2 <= A-1/5 by Bessel, f^2 <= C by Cauchy-Schwarz) and the same for
2|he|. Row T104: not solved.

## 13 Nov - region (11): sextic bound, ceilings 2849/5000 and 129/250, zero at the corner
GAP_STATE_FORM.md ("Region (11) of the 5+1 class at N = 6"): Codex STRAT10 (t104_strat10_result.md) proves the sextic moment bound
(sum u^3)^2 >= 3 sum u^4 - 3/2 for zero-sum unit u in R^5, raises the 5+1 ceilings to a <= 2849/5000 at N = 6 and
a <= 129/250 for every N >= 6, and finds an explicit family inside region (11) with T -> 0+ at the corner r = a = 1, so
(11) cannot be closed by cells alone. Final N = 6 partition: 24,708 positive, 10,226 excluded, 5,244 open leaves. Exact
replay rerun on Mac mini 2 (strat10/replay_mini2.txt); independent check of the sextic bound in t104_check_strat10_sextic.py.
Row T104: not solved; open on the corner neighbourhood of r = a = 1, the 5,244 open leaves, and n >= 6 connected.

## 13 Nov 09:46 - 5+1 at N = 6 closed: region (11) proved; every disconnected N = 6, D = 2 class done
t104_strat11_12_result.md: Codex STRAT11 (corner ball, T6 >= ||S-S0||/120 for 0 < ||S-S0|| <= 1/20800), STRAT12 (exact Bernstein
certificates with Farkas multipliers, 13,359 of 13,368 boxes) and STRAT13 (collars at the nine equality limits, two edges of weight 1/2
or a triangle of weights 1/3, T6 >= ||S-S_P||max/24 on balls of radius 1/15360 and 1/27864) close STRAT9 region (11): T6 > 0 there at
N = 6. Final partition 32,925 positive, 20,277 excluded, 17 collar leaves, no open leaf. strat13/replay_all.py passed all 18 stages
(1,093 s, Mac mini 1). Independent checks strat11_check, strat12_check (120 of 120 leaves) and strat13_check (425 of 425 collar
points on the final cover; chart stress 600 of 600 per type). With STRAT9 this proves the 5+1 class at N = 6, and with STRAT7 every
disconnected graph at N = 6, D = 2. Push 139 1d4a76e2. STRAT14 (Codex, Mac mini 1) now ports the same chain to the STRAT8 residual
of connected n = 5, D = 2 (5,272 open leaves). Row T104: not solved; open on connected n = 5, D = 2 (STRAT8 residual), the 5+1
residual for N >= 7, and n >= 6 connected.

## 13 Nov 10:33 - connected n = 5, D = 2 proved (STRAT14); every five-vertex D = 2 graph done
t104_strat14_result.md: Codex STRAT14 ports the STRAT11-13 chain to the STRAT8 residual. The n = 5 target is the all-N polynomial
of STRAT10 at N = 5 (C_N(-1) = 2 Cface), so certificates were recomputed against Cface. Collars at the two disconnected equality
types: two edges T5 >= ||h||_1/20 on ||h||_1 <= 1/520, triangle T5 >= ||h||_1/12 on ||h||_1 <= 1/600; nine exact zero witnesses
in STRAT8 open leaves 12437 12643 13871 14683 14814 17328 17952 18124 18548 (equality points, not counterexamples). The 5,272 open
leaves become 8,227 positivity, 3,729 exclusion and 14 collar leaves (depth <= 73, 0 open); global ledger 32,929 / 13,937 / 14 /
46,879 splits, volume 1152. replay_all.py 17 of 17 PASS (606 s, Mac mini 1). Independent checks strat14_check: target and all 25
constraints equal STRAT8's formulas exactly, 5,272 of 5,272 partitions exact, 140 of 140 sampled Bernstein leaves pass, 239 feasible
collar points all positive. Push 141 3dae1e7d. With STRAT4-8 this proves T >= 0 for every five-vertex graph with D = 2.
Row T104: not solved; open on the 5+1 class for N >= 7 and connected carriers with n >= 6.

## 13 Nov 12:1x - 5+1 class proved for every N >= 7 (STRAT15); five-vertex double carrier with isolates done for all N
strat15_check/t104_strat15_result.md: Codex STRAT15 writes C_N(q) = c0 + c1 q + c2 q^2 (q = N - 6) on the shared chart and certifies
c2, d1 = c1 + 2 c2 and C1 = c0 + c1 + c2 >= 0 on every leaf, so C_N >= 0 for every real q >= 1 and T_infinity >= 0. Region: 8,366
non-all-N leaves plus 1,004 exclusions that do not transfer under the all-N premises = 9,370 boxes; 9,357 at once, 13 refined into
18 leaves; ledger 9,289 positive + 86 exclusions, 17 collars kept; corner and nine equality limits by local_uniform.py (Bernstein in
v = 1/(N-2), T_N >= ||h||_1/12 on balls 1/4000 and 1/12900). replay_all.py 10 of 10 PASS (3452 s, Mac mini 1; first verify_new
attempt died on a spawn/import assertion, fixed by check_spawn.py). Independent checks strat15_check (same bank, certificates.json
60441b5e): 7,267/7,267 transfers, targets equal STRAT8/STRAT10 exactly, coverage and partition exact with 174/174 sampled
certificates, 176 collar points no negative. Tarball STRAT15_final.tgz sha256 554e13fe on Mac mini 1; sources pushed 146 583a5c5b.
Still open for disconnected D = 2 with components <= 5 (STRAT7 padding is isolates only): four-vertex double carrier with lower
components other than one edge; five-vertex double carrier with any lower component; split carriers 2+3, 2+4, 3+3 with lower
components; split carriers 2+5, 3+4, 3+5, 4+4, 4+5, 5+5.
Row T104: not solved; open on those disconnected combinations and on connected carriers with n >= 6.
