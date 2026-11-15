# Reported negative answer to the polynomial-sample question

OpenAI, *Quantitative lower bounds for trace reconstruction*, September 24, 2026, repository preprint. The author and date are in the opened [manuscript header](https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/main.tex). ArXiv identifier: none located.

The opened [main theorem](https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/sections/introduction.tex) states that, for fixed s in (0,1] and 0<c<1/(4 log 2),

\[
T_{q,s}(n)\ge n^{c\log(q^3\log n)}
\]

eventually along every sequence with n tending to infinity and q^3 log n tending to infinity. Here q is the known deletion probability, all logarithms are natural, and T is the fixed-budget sample complexity for exact worst-case reconstruction from independent complete traces with unrestricted randomized computation.

For fixed q in (0,1), this rules out every polynomial sample bound. A matching order remains unsettled by this result. The independent algebraic check is in LOG.md; the additional formal-statement check is in AUDIT.md. These checks do not certify the full preprint proof.
