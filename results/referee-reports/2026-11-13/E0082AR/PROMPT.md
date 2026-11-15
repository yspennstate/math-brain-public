You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/ of another run):
open problem E0082, Open problem 2.3 of J. Pitman and W. Tang on waiting times for patterns in i.i.d. +-1 sequences (find the
arXiv paper by Pitman and Tang with "patterns", "random walks", "Brownian bridge", "first passage"; the claim cites Theorem 1.8(4)
on arXiv p. 6, Theorem 2.1 with the matching matrix, and a published chapter p. 65). The open problem asks (1) the exact
asymptotics of E T(BR_{alpha,n}) for alpha real (bridge patterns) and (2) the exact asymptotics of E T(FP_{alpha,n}) for alpha<0
(first-passage patterns). The claim (PARTIAL) asserts: (A) for every fixed real alpha, E T(BR_{alpha,n}) ~ n c_BR(alpha) with
c_BR given by an explicit convergent series of finite-dimensional integrals (its equation (10)), proved by convergence of the
weighted matching-matrix column sums, a lattice local limit theorem and uniform integrability; (B) for alpha<0,
c n log n <= E T(FP_{alpha,n}) <= C n log n (reconstructing an internal argument), so E T(FP)/n -> infinity and no finite limit on
scale n exists; (C) the task's premise misread the source for FP (the source bounds it between n and n^{5/4}).

Break it if it is wrong.
1. Get the Pitman-Tang paper into sources/ as plain text. State exactly the definitions of BR_{alpha,n}, FP_{alpha,n}, T, the
   matching matrix, Theorem 2.1, Theorem 1.8 and Open problem 2.3, and check that the claim's definitions match (in particular the
   meaning of alpha for bridges and for first passage, and whether T is the waiting time for the first occurrence of ANY pattern
   in the family).
2. Check (A) line by line: the formula for E T of a pattern family (Li / Gerber-Li / matching matrix: E T = 1/(sum of the entries
   of the solution vector) or the Conway leading-number form) and its exact use here; the scaling of overlap counts; the local
   limit theorem used; the uniform integrability or domination step (this is where such proofs fail: overlaps at short shifts
   and at shifts near n); and the final series (10) (does it converge, is it positive and finite). Evaluate c_BR(alpha) numerically
   from (10) yourself for a few alpha.
3. Check (B): both bounds, with all constants and the dependence on alpha<0; whether the lower bound really forces n log n
   (find the mechanism) and whether it contradicts the source's upper bound n^{5/4} (it should not).
4. Literature: is (A) or (B) already in print (Pitman-Tang published version, citers 2017-2026, Guibas-Odlyzko, Li 1980,
   Gerber-Li 1981, Chen-Zame, Nielsen, Banjevic, Zajkowski; "waiting time" "family of patterns" "Brownian bridge")?
5. Write your own independent code (do not reuse claim_files/code): exact E T for the bridge and first-passage families for n up
   to the feasible size (Aho-Corasick / prefix Markov chain, or the matching-matrix linear system with exact rationals), compare
   E T/n with your c_BR(alpha) and E T/(n log n) for FP.
6. Verdict on value: correct or not, novel or not, exactly what statement is proved, and whether part (1) of Open problem 2.3 can
   be called solved.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Source texts
may go in sources/ as plain text only; no PDFs kept, no page images or scans anywhere in this folder. Work only in this
directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
