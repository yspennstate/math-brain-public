# Reported resolution of the polynomial-sample question

OpenAI, *Quantitative lower bounds for trace reconstruction*, September 24, 2026. [Manuscript header](https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/main.tex); [theorem and model](https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/sections/introduction.tex).

For ordinary independent complete deletion traces, unrestricted computation, fixed success s in (0,1], and 0<c<1/(4 log 2), the stated bound is

\[
T_{q,s}(n)\ge n^{c\log(q^3\log n)}
\]

eventually whenever n tends to infinity and q^3 log n tends to infinity. For each fixed deletion probability q in (0,1), this is superpolynomial. Thus the preprint reports a negative answer to polynomially many worst-case traces. It does not determine the exact order.

ArXiv identifier: none established. This is a repository preprint. The prior baseline arXiv:2607.04073 is a different paper. No later result changing the remaining order gap was found in the bounded search.

The new check here is the final testing transfer, conditional on the hard-family estimates; see AUDIT.md and PROOF.md. The full lower bound has not been independently certified here.
