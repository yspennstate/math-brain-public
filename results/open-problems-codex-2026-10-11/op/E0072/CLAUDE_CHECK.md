# E0072: third check (claude-322bc92e, 12 Oct 2026 02:0x)

Verdict: PASS. Björklund's Problem 4 (Five remarks about random walks on groups, arXiv:1406.0763v2, p. 25) asks whether every symmetric measured group with an integrable bi-invariant (semi-)metric d has drift zero. The answer is no. The counterexample is the free group F_32 with mu uniform on its 64 letters and d(g,h) = L(g^-1 h), where L is the cancelation norm. Novelty is not verified.

What I checked, independently of the attempt and of the two audits:

1. The norm. L(w) is the least number of unpaired positions over noncrossing matchings of inverse letters. It is the cancelation norm of Brandenbursky, Gal, Kedra and Marcinkowski (arXiv:1310.2921, Proposition 2.A identifies it with the bi-invariant word norm). Invariance under inserting or deleting an adjacent inverse pair: all four cases of the deletion surgery are right, including the case with two external partners. A perfect noncrossing inverse matching forces the word to be trivial (a minimal matched interval is an adjacent inverse pair). Subadditivity holds by concatenation, inversion by reversal, and conjugation invariance by nesting u...u^-1 around the matching. So d is a genuine bi-invariant metric with first moment 1, and mu is symmetric, finitely supported and generating.
2. The bound. A fixed noncrossing positional matching with m pairs has all pairs inverse with probability 64^-m, since the pairs use disjoint independent letters. There are at most C(n,k) C_m <= C(n,k) 4^m such matchings with k unpaired positions. L <= n/4 forces m >= 3n/8, so P(L(X_n) <= n/4) <= 2^n 16^(-3n/8) = 2^(-n/2). The arithmetic is right, and the reduction from the raw word to X_n is exact because L is reduction invariant.
3. The drift. E L(X_n) is subadditive because the increments are independent and L obeys the triangle inequality. Fekete's lemma gives the limit, and it is at least 1/4. Borel-Cantelli gives liminf L(X_n)/n >= 1/4 almost surely. The F_32 choice matters only for the constant: the same bound works for F_r once (2/r)^(3/8) < 1/2, that is r >= 13.

The audits: o06 and o07 both PASS, each with an independent fetch of the source.

Not checked here: the finite DP checks in check.py and the Lean arithmetic file, beyond reading them. The literature search found no drift statement for this norm (BGKM has none), so the record is "answered here, novelty unverified". The scl test case Björklund suggests is not addressed.
