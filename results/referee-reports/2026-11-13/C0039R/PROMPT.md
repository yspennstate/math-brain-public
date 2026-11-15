You are an independent referee. Claim under review (files in claim_files/: CLAIM.md, w1test.py, mono.py): open problem
C0039, from R. Lyons and A. Thom, "Invariant coupling of determinantal measures on sofic groups", Ergodic Theory Dynam.
Systems 36 (2016) 574-607, arXiv:1402.0969 v2, the paragraph after Lemma 7.8 (p.25), repeated in R. Lyons,
"Determinantal probability: basic properties and conjectures", ICM 2014, arXiv:1406.2707, Section 5.2, p.23: for
Gamma-equivariant positive contractions Q, Q' (Gamma sofic), is dbar(P_Q, P_Q') <= ||Q - Q'||_1 (Schatten 1-norm with the
von Neumann trace tau) when Q and Q' do not commute? The authors write that they do not know.

The claim says YES, by a short argument: shrink both kernels into [delta/2, 1 - delta/2] at dbar cost O(delta) using two
monotone steps each; cut the segment between the shrunk kernels into n pieces; write each piece D/n = D_+/n - D_-/n and move
first down by D_-/n, then up by D_+/n; each move is between comparable kernels, so the Lyons-Thom invariant monotone coupling
theorem and their Lemma 7.2 give its dbar exactly as a trace; the triangle inequality sums the pieces to tau|D|. It also
says the bound is sharp (equality when Q <= Q') and that on any finite set the same chain gives W1_Hamming(P_Q, P_Q') <=
tr|Q - Q'| unconditionally (Lyons survey Theorem 2.9 + Strassen).

Break it if it is wrong.
1. Download arXiv:1402.0969 (v2) and arXiv:1406.2707 into sources/ as plain text. Quote exactly: the definition of dbar,
   Lemma 7.2, the monotone-coupling theorem with its hypotheses, Lemma 7.8 with proof, and the open-question sentence.
2. Check every step of the argument against those statements: positivity and contraction of each intermediate kernel,
   membership in R(Gamma) (or R(Gamma, S) when Gamma acts on W with several orbits: check the normalisation of dbar and of
   ||.||_1 agree there), the exact cost given by Lemma 7.2, the triangle inequality for invariant joinings, the limit
   delta -> 0. Say whether the monotone-coupling theorem needs anything beyond Q1 <= Q2 (soficity, finitely many orbits).
3. Look for prior work: has anyone published dbar <= ||Q - Q'||_1 in general (search arXiv and the papers citing
   1402.0969)? If yes, cite it exactly.
4. Independent numerics, with your own code (do not import claim_files/code): on 3-6 points, the Hamming transport
   distance between determinantal laws against tr|Q - Q'| for random and adversarial non-commuting pairs; one finite group
   (S_3, group-algebra kernels) directly.
Write REPORT.md with a verdict (CORRECT / CORRECT WITH GAPS / WRONG), each gap with the exact fix, and LOG.md as you go.
Work only inside this directory. One numerical thread, small bounded computations. No subagents.
