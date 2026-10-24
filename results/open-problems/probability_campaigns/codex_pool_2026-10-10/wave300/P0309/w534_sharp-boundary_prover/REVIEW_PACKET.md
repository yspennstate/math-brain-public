# w534 -> w536: P0309 boundary result

The result is a counterexample to the auxiliary bridge "force balance implies a nonnegative displacement Hessian." It is not a resolution or refutation of P0309. Please audit the mathematics independently of the author's status labels and numerical checks.

Read `ATTEMPT.md`, Lemmas A–C, and final claim rows `S1.w534.C2`, `C3`, `C4` in `CLAIMS.jsonl`. C1 is the statement-only precursor superseded by C2. `STATEMENT_FOR_ADVERSARY.md` was sent to w535 before the complete proof was saved. The primary source is arXiv:2202.09240v2, Section VI, printed pages 59–61 and 66–67. `SOURCE_STATUS.json` separates the historical intake from the current UNKNOWN openness status.

Check the mean unordered-pair factor in A1/A2; the Gaussian Fourier coefficients and strict equality case in A3; the differentiation/convergence bounds for A4; the finite-support relative energy and dominated-convergence limit B2/B3; and the explicitly limited heat-regularization assertion in C4. The elementary harmonic integral from the prior attempt is only conditional; this packet does not contradict that properly qualified calculation.

The single hardest remaining P0309 gap is uniform nonlinear free-energy/order control for a stable BCC/FCC candidate, including defects and competing configurations, that produces a symmetry-breaking infinite-volume Gibbs law. No formal proof system was run. Trusted mathematical inputs are listed in ATTEMPT.md.

Numerical receipts will be saved in `verification.jsonl` and `VERIFICATION.json`; they check sign, normalization and the finite-support formula rather than replacing the proofs. Draft brain entries stay separate from submitted/reviewed/ingested/retrievable states. Do not integrate into the live store before review.

Please place your verdict in your own permitted worker folder, identifying each claim and every required correction, then point to it through the existing mesh. Any new result of yours needs the independent referee w539.
