# Reported resolution of the polynomial-sample question

OpenAI, *Quantitative lower bounds for trace reconstruction*, September 24, 2026, OpenAI Math Release preprint. Author, title and date were checked in the [manuscript header](https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/main.tex) and [release citation](https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/README.md). ArXiv identifier: none verified; the release citation provides none.

The [main theorem](https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/sections/introduction.tex) states that for fixed success s in (0,1] and 0<c<1/(4 log 2),

\[
T_{q,s}(n)\ge n^{c\log(q^3\log n)}
\]

eventually whenever n tends to infinity and q^3 log n tends to infinity. Here q is deletion probability and logarithms are natural. The model observes independent complete traces of deterministic binary words, and permits unrestricted randomized computation.

Consequently each fixed q in (0,1) requires n^{Omega(log log n)} traces. This answers the polynomial-sample subquestion negatively if the reported theorem is valid. The exact asymptotic order remains undetermined by this bound. LOG.md independently checks the implication. AUDIT.md locates the actual comparison configuration and solution source; no formal checker or full proof audit was performed.

The required literature-stop branch applies to this reported resolution. There is no new mathematical theorem in this folder.
