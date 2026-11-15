# Reported resolution of the polynomial-sample question

OpenAI, *Quantitative lower bounds for trace reconstruction*, September 24, 2026. The [manuscript header](snapshot/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/main.tex) gives the author and date. The [pinned introduction](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/sections/introduction.tex) states the model and theorems.

For binary words observed through independent complete deletion traces, with unrestricted randomized reconstruction, the claimed theorem is
\[
T_{q,s}(n)\ge n^{c\log(q^3\log n)}
\]
eventually along every sequence with \(n\to\infty\), \(q\in(0,1)\), and \(q^3\log n\to\infty\), for every fixed \(s\in(0,1]\) and \(0<c<1/(4\log2)\). Logarithms are natural. At every fixed deletion probability this is a superpolynomial lower bound, ruling out polynomially many worst-case traces if the theorem is valid. It does not determine the exact order.

ArXiv identifier: none established. This is a repository preprint; arXiv:2607.04073 is the separate baseline paper named in the task. No later result settling the exact-order gap was found in the bounded search.

The source is now pinned locally, including its complete OAI solution import closure. See [SNAPSHOT.md](SNAPSHOT.md). Hash and import checks do not certify the proof. No Lean execution or full mathematical verification is claimed. This follows the requested literature-stop branch; no new lower-bound construction was attempted.
