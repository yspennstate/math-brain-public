---
name: c0034_rank_one_prior_art_exact_certificates_2026_11_13
status: verified
evidence: REPORT.md; data/verification.json; data/induction_failure.json
---

C0034 literature correction: rank-one orthogonal union coupling is already Lyons 2003, Lemma 10.4, pp. 203–204; Proposition 10.3 handles the countable limit. Complementing to a three-color partition makes rank triples symmetric, so any one rank <=1 suffices; all |E|<=5 are known, and the first unsettled triple by this argument is (2,2,2) at n=6.

Arbitrary induction by rank-one addition fails even for a 4x4 Hadamard matrix: the saved exact example has correct stage marginals but wrong composed first-color law. This is not a C0034 counterexample.

This run produced 288 rational certificate files / 286 distinct instances, including all nonzero rank pairs for 18 rational orthogonal matrices at n=2,...,7, and all 15 / 105 exceptional column allocations for one matrix at n=6 / 7. A separate standard-library Fraction verifier evaluated principal kernel minors and verified all 14,772 marginal rows exactly. Thirty-two local real/complex dual searches found no counterexample. The full question was not solved; no full literature resolution was located in the bounded search.

This note is saved locally because the user required all writes inside this directory and the shared mesh database is read-only in the sandbox. It has not been installed into shared memory.
