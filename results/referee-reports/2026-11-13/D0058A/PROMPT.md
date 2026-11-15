Open problem D0058. Source: X. Chen, B. Derrida, Y. Hu, M. Lifshits, Z. Shi, "A max-type recursive model: some properties and
open questions" (2017; arXiv:1705.xxxxx, find it by authors and title), Conjecture 3, PDF p. 4: for the Derrida-Retaux recursion
X_{n+1} = (X_n^{(1)} + ... + X_n^{(m)} - 1)^+ on nonnegative integers, under the critical condition (4) of the source, E(X_n) is
asymptotic to (4m/(m-1)^3) n^{-2}, and more generally for every real r > 0, E(X_n^r) ~ c(r)/n^2 with
c(r) = (4/(m-1)) sum_{k >= 1} k^r m^{-k}. Read the source for the exact wording and EVERY hypothesis (the critical condition,
and any integrability assumption such as E[X_0^3 m^{X_0}] < infinity that the companion conjecture on P(X_n > 0) carries).

Important prior work of ours (do not redo, build on it and cite it as prior internal work only): for the companion statement
P(X_n > 0) ~ (4/(m-1)^2) n^{-2} (our D0056), the version with only the critical condition is false: Chen-Shi 2020 Theorem 1.1
gives one route, and a sparse critical law with atoms at 2^j gives limsup n^2 P(X_n > 0) = infinity; the published version with
the third tilted moment stays open. Chen-Hu-Shi arXiv:2306.12717 is relevant.

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only). State Conjecture 3 and the hypotheses exactly. Search:
   Chen-Dagard-Derrida-Hu-Lifshits-Shi ("The Derrida-Retaux conjecture on recursive models", Ann. Probab. 2021), Chen-Shi 2020,
   Chen-Hu-Shi 2023 (arXiv:2306.12717), Hu-Shi ("The free energy in the Derrida-Retaux recursive model"), Hu-Mallein-Pain,
   Collet-Eckmann-Glaser-Martin (1984), Derrida-Retaux 2014, Chen 2024-2026, and every 2017-2026 citer. Decide exactly what is
   proved about E(X_n^r) at criticality (orders n^{-2}, upper and lower bounds, exact constants, which r). If the conjecture is
   proved or refuted in print as stated, give the theorem and page and stop with RESOLVED_IN_LITERATURE.
2. Hypotheses: if the ledger wording (critical condition only) is weaker than the source's, say so and decide both versions.
   Under criticality alone, test whether the sparse 2^j construction (or Chen-Shi) also breaks the moment asymptotics.
3. Prove what you can, with complete proofs: the relation between E(X_n^r) and P(X_n > 0) at criticality (for example
   E(X_n^r) / P(X_n > 0) -> sum k^r m^{-k} (m-1)/m, i.e. the conditional law of X_n given X_n > 0 tends to geometric(1/m)),
   which would reduce Conjecture 3 to the P(X_n>0) conjecture; order-n^{-2} upper and lower bounds; or the exact constant in a
   special family (for instance the m = 2 exactly solvable laws in Chen et al.).
4. Compute (evidence only): exact iteration of the law (truncated support, FFT for the m-fold convolution) for several critical
   initial laws and m in {2, 3}, n up to 10^4 or more, tracking n^2 E(X_n^r) and the conditional law given X_n > 0.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
