# Complete non-normal orbit quotients of every order at least three

**Status: full source-matching proof candidate, internally checked; NOT campaign-closure-certified. Publication novelty UNVERIFIED. No independent audit votes are created by this package.**

## The result

For every integer m >= 3 there is an infinite connected locally finite simple transitive graph X and a freely acting non-normal subgroup B of Aut(X) such that the simple orbit quotient X_B is K_m. No normal subgroup N of ANY transitive subgroup Gamma' <= Aut(X) has X_N isomorphic to K_m.

This answers the literal finite-quotient-allowed formulation of Grimmett--Li Question 4.5. The ambient graph is infinite; the quotient is FINITE. It does not answer an additional infinite-quotient version or Question 4.6 on connective constants.

The construction is an existence argument using a published generating-set-preserving graphical regular representation theorem. It is not an explicitly listed final Cayley generating set. All parts of the reduction, the universal transitive-subgroup quantifier, and a non-optimal degree bound are proved in `solution.tex`.

## Credit and new contribution

P20 already supplied the K_3 candidate using S_3 * A_5:
`proofnet24/P20-closure-log-unimodality/successors/D0072/runs/2026-09-17/2026-09-17T16-18-23Z__run-report.md`
at `92b25a56025b3e0905274c554a4104d4acbc0685`.

This main-agent note credits that mechanism and extends it uniformly to every m >= 3, using F_m * F_m with F_3 = S_3 and F_m = A_m for m >= 4. It does not take ownership of D0072, alter P20's fixed E_NNQ=1, or count this self-check as an OTHER-track audit.

## Reproduce

From this directory, using Python 3.10+ and a LaTeX installation:

```sh
python3 artifacts/finite_core.py > finite_core.replayed.out
diff -u artifacts/finite_core.out finite_core.replayed.out
pdflatex -interaction=nonstopmode -halt-on-error solution.tex
pdflatex -interaction=nonstopmode -halt-on-error solution.tex
```

The standard-library-only checker was actually executed on 17 September 2026 and replayed byte-identically. It checks complete finite-group normal-subgroup lattices, non-normal stabilizers, right-coset partitions, quotient adjacency, and finite order obstructions for S_3, A_4 and A_5. It ends `ALL_EXACT_CHECKS_PASS`. The TeX compiled successfully twice to four pages.

The checker does NOT verify the infinite GRR theorem or simplicity of every A_m. The all-m statement uses the written proof and cited published results, not extrapolation from these three tests.

SHA-256:
- `solution.tex`: `7b212b3871cdf0b04e668c84ad5773452cbd39be3fdeb2128abe4a00340e249e`
- `artifacts/finite_core.py`: `50d893d09e86051cf66c288bd702f54ed651bfedf40dd03e4145143079c7368c`
- `artifacts/finite_core.out`: `77851f6f70a484459721af7f548543b135990805e697fc7c7713b3e12375ad4e`

## Primary sources and review limits

1. Grimmett and Li, *Self-avoiding walks and connective constants*, arXiv:1704.05884v2, Section 4.2, Question 4.5, printed pp. 16-17. https://arxiv.org/abs/1704.05884
2. Leemann and de la Salle, *Cayley graphs with few automorphisms: the case of infinite groups*, Annales Henri Lebesgue 5 (2022), 73-92. Theorem 1.1, Theorem 3.1, Proposition 3.2 and the proof of Theorem 1.1. https://doi.org/10.5802/ahl.118
3. Milne, *Group Theory*, v4.01 (2025), Chapter 4. https://www.jmilne.org/math/CourseNotes/GT.pdf

Primary source PDFs and the preservation of prescribed generators were checked directly. A bounded dated prior-art search found no explicit prior resolution, but that is not proof of novelty or worldwide open status. Related Schreier-graph literature remains to be examined more broadly. The GRR theorem and finite-group facts are known inputs.

P26 and one distinct research track, naturally P19 under its P20-directed audit duty, must independently check the exact source scope and entire proof before campaign closure. A proof candidate folder is not a declaration that those audits have occurred.
