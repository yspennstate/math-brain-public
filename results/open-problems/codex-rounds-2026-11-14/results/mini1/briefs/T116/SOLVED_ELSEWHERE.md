# T116: polynomial-sample question answered in a later preprint

OpenAI, *Quantitative lower bounds for trace reconstruction*, September 24, 2026, OpenAI Math Release preprint. The corporate author and date appear in the [manuscript source](https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/main.tex) and [release citation](https://github.com/openai/math/blob/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/README.md). [PDF](https://github.com/openai/math/blob/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf).

ArXiv identifier: none located. This is a repository preprint; arXiv:2607.04073 is the earlier paper by Arnav Burudgunte, Paul Valiant, Hongao Wang, not this lower bound.

The [main theorem](https://github.com/openai/math/blob/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/sections/introduction.tex) states the following. Let T_{q,s}(n) be the least fixed number of independent complete deletion traces needed to recover every deterministic binary word of length n with probability at least s, allowing unrestricted randomized computation. For every fixed s in (0,1] and 0<c<1/(4 log 2),

\[
T_{q,s}(n)\ge n^{c\log(q^3\log n)}
\]

eventually along every sequence with n tending to infinity and q^3 log n tending to infinity. Logarithms are natural. In particular, each fixed q in (0,1) requires n^{Omega(log log n)} samples. This rules out polynomial sample complexity, including at high success probability.

The [final proof section](https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/sections/transfer.tex) addresses genuine traces, padding to every sufficiently large length, and arbitrary fixed positive success probability. The [formalization scope note](https://github.com/openai/math/blob/main/lean/docs/122.md) reports matching Lean results; no Lean checks were run here.

A second advancement is OpenAI, *Uniform quasipolynomial-time trace reconstruction*, October 5, 2026. Its [manuscript](https://raw.githubusercontent.com/openai/math/main/preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/build/manuscript/main.tex), Theorem 1.1, gives a uniform decoder for known rational retention probability. At fixed retention probability, its trace count and bit complexity are exp(O_p((log n)^3(1+log log n)^6)), with success at least 2/3 on every input. No arXiv identifier was located for this preprint either.

These are reported preprint results, not proofs independently certified in this session. The polynomial-sample subquestion has a reported negative answer; a matching asymptotic order is not established by these bounds. The requested literature-stop branch applies.
