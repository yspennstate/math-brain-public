# Results

Source under review: ~/fei_solve_agent/NOTES.md,
read with `cat` as expressly permitted by BRIEF.md.

All five formal statements have independent proofs in preparation; no counterexample
has appeared. Proposition 4 is weaker than the following direct consequence of
`up(S) <= abs1(S)`:

    B <= A + 2 Gamma.

This removes the influence term in its second upper bound and improves the constants
in the joint A/Gamma equivalence.

Saved verification results:

- `census4.log`: all 65,536 four-variable functions passed; 578 Theorem 1 equality
  cases, 10 equality cases in Proposition 4's first inequality.
- `random.log`, `random_summary.csv`: 1,200,000 random draws passed, with 100,000 in
  each dimension/bias cell (dimensions 5 through 8; negative-output probabilities
  0.5, 0.2, 0.05).
- `structured.log`, `structured.csv`: all 91 structured instances and zero-dimensional constants passed.
- `composition_real.log`: all 65,536 outer functions tested by full truth-table
  composition with a balanced nontrivial inner function; every balanced
  four-variable inner function also tested. Real-valued recursion passed.
- `census_analysis.json`: independent integer-matrix rederivation of every census
  metric agrees to at most 1.12e-15 bits; full coefficient constraints and compressed
  frontiers are in the two `coefficient_*.json` files.

Theorem 1 equality is characterized exactly by the restricted-coefficient condition
in PROOFS.md. Its coefficient 2 is optimal: iterated composition of a balanced
degree-two function with B=0 gives (A-B)/I tending to 2.

Final results:

- `PROOFS.md` gives full proofs of all five statements, precise boundary conventions,
  equality cases, sharpness witnesses, the refined proposition, the census coefficient
  frontiers, and both FEI equivalences with constants.
- `REPORT.md` gives a verdict line for each statement and the limits of the conclusions.
- `final_audit.json` records PASS for 1,265,627 single-function instances,
  including 1,200,000 random draws with compressed expanded-spectrum composition
  checks, 143,942 independent full-truth-table composition pairs, and 262,306
  real-recursion coordinate checks.
- The independent integer-matrix census differs by at most 1.1102230246251565e-15
  bits; exact-normalization checks and the 80-digit coefficient audit also passed.
- Proposition 4's first summed coefficient is only 0.13657007572574492 in the
  four-variable census; its best universal value is not established here.
  The all-dimension theorem B <= A + 2 Gamma improves its second upper bound.

The informal Jensen remark has no specified inequality; the report flags that
ambiguity and supplies the valid Jensen bound instead. No formal statement was refuted.
