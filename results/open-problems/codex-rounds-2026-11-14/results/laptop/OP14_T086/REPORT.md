VERDICT: PROVED T086 in the cited preprint arXiv:2611.09495, Theorem 1.1; no new proof claimed

The complete result was located during the literature check, within ten minutes. See [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md) for the exact reference, theorem, links and scope. The paper is by Dmitriy Bilyk, Sebastian Neumayer and Tino Ullrich. Its Theorem 1.1 covers every dimension in the question, so the explicit stopping condition applies. No special-case computation or replacement proof was undertaken.

Checks against a false match:

- Checked the actual full text rather than relying on the search summary.
- Read the theorem independently in HTML and extracted PDF.
- Matched the Gaussian covariance, domain, absolute supremum event and both sides of the order estimate.
- Recomputed the two exponents from the separate entropy-to-small-deviation formula in Section 4: r = 1 gives 2, and beta = d - 1/2 gives 2d - 1. Substitution gives logarithmic powers 3, 5 and 7 for dimensions 2, 3 and 4 respectively.
- Checked that the stated theorem covers all fixed d >= 3 without an additional hypothesis on coefficients.

Commands and evidence: [LOG.md](LOG.md) records the web-search queries, opened sources and local commands. No numerical experiment was needed. A read-only math-store recall was also requested, with logging and Python bytecode disabled, to respect the prohibition on writing outside this folder.

What failed: the web tool could extract the PDF text, but both attempts to render a screenshot of PDF page 2 returned a cache-miss error. Thus visual PDF inspection was unavailable; the cross-check used extracted PDF text and HTML. The source date discrepancy is recorded in SOLVED_ELSEWHERE.md.

Uncertainty: this establishes that a directly matching complete theorem and proof have been posted. It does not constitute an independent audit of all arguments in the recent preprint, and it does not establish peer review or the validity of its advertised Lean certificate. The verdict attributes the proof to the cited paper.

Next worker: update T086's literature status with this reference. If independent proof certification is wanted, audit the probabilistic inequality in Theorem 2.1 and its use in Theorem 1.2 before relying on the new theorem; the final exponent substitution alone does not audit those steps.

Task: Open problem T086, small ball probabilities for the Brownian sheet in dimension three and higher.
