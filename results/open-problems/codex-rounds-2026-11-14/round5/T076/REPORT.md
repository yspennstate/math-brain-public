VERDICT: PARTIAL sharp two-logarithm bound for noncommuting quadratic errors and a bounded-variation criterion

The round-4 commuting quadratic-drift bound holds. Its exact time factor
and its M=3 check were independently rederived. A literature search under
five minutes found no later solution to T076. The latest inspected
two-dimensional paper remains Xujie Lai and Fan Yang,
*Localization Lengths for Two-Dimensional Random Band Matrices:
Exponential Lower Bounds*,
[arXiv:2609.24426v4](https://arxiv.org/abs/2609.24426v4).
Its improvement over the original brief was already recorded in round 1.

New beyond round 4: [PROOF.md](PROOF.md) removes translation invariance
from the deterministic analysis of the same quadratic term. Write
\(A=I-B\), \(G_u=(I-uB)^{-1}\), \(Q=I-P\), and parametrize the
pointwise envelope by real symmetric contractions \(E(u)=QE(u)Q\):
\[
D(u)=\delta uW^{-2}A^{1/2}G_uE(u)G_uA^{1/2}.
\]
This is equivalent, on \(Q\), to the previous strong Loewner envelope
\(-\delta uW^{-2}AG_u^2Q\preceq D(u)\preceq\delta uW^{-2}AG_u^2Q\).

For the exact two-coordinate Duhamel integral \(\mathcal J_t[D]\),
if \(E\) has operator-norm total variation \(V\) on \([0,t]\), then
\[
-\delta^2tW^{-2}(1+2V)G_tQ
\preceq\mathcal J_t[D]
\preceq\delta^2tW^{-2}(1+2V)G_tQ.
\]
Thus bounded variation independent of the torus size preserves the
single return-kernel logarithm. A time-independent contraction needs
no commutation assumption. Integration by parts and a separate
telescoping argument give the same factor \(1+2V\).

The pointwise envelope alone has a sharp worst-case diagonal order
\(\delta^2(\log M)^2/W^2\). The proof gives a general upper bound
and an explicit continuous family attaining it: for
\(M=8^{R+2}\), \(t=1-M^{-4}\),
\[
\mathcal J_t[D]_{00}
\geq\frac{\delta^2\log8}{720000W^2}R(R+1).
\]
The construction swaps successive squares of low cosine modes with
modes at the currently active diffusion scale. Its total variation is
\(2R\). With \(W=\lceil R^{3/4}\rceil\), all error entries tend
uniformly to zero, but this quadratic diagonal tends to infinity.
This obstruction satisfies the stronger envelope from round 4;
that round's obstruction used a weaker one.

What failed: extending the single-logarithm estimate using only the
noncommuting pointwise Loewner envelope. A preliminary single-output-mode
example broke only an operator comparison, so it was replaced by the
simultaneous-mode construction above. No numerical experiment ran:
the sandbox refuses to set the requested nice priority. Verification
was analytic, including independent matrix factorizations, a direct
two-by-two swap check, and two harmonic-sum lower bounds. Commands,
constants, opened sources and failed steps are in [LOG.md](LOG.md).

Limits: these are conditional deterministic statements. The constructed
errors are not shown to arise from random resolvents or to preserve the
full observable's entrywise positivity and Ward identities. The normalized
random error may have infinite total variation. No new eigenvector,
localization-length, or local-statistics theorem is proved; T076 remains
open. No claim of novelty in the underlying operator inequalities is made.

Next worker: test whether the actual two-loop positivity and Ward
constraints exclude the simultaneous mode transfers in the example.
A concrete sufficient target, after establishing a suitable normalized
envelope, is the square-function estimate
\[
\int_0^t u^2E(u)A|B|G_u^2E(u)\,du\preceq Ct^2Q
\]
with size-independent \(C\). It would replace the bounded-variation
assumption and recover a single logarithm for this quadratic term.
The general envelope proved here gives only \(C(1+\log M)Q\).

All writes stayed in this folder. No git, external messages, registrations,
numerical jobs or subagents.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 08:02 Asia/Tbilisi.
