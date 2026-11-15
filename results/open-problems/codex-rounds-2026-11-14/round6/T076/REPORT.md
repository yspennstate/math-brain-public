VERDICT: PARTIAL sharp square-function bound under restricted transfer between diffusion scales

The round-5 bounded-variation estimate and its two-logarithm example
hold. Their factorization, time integral, cosine normalization and lower
constant were independently rederived in [LOG.md](LOG.md). A literature
check under five minutes found no later solution to T076. The latest
inspected two-dimensional result remains Xujie Lai and Fan Yang,
*Localization Lengths for Two-Dimensional Random Band Matrices:
Exponential Lower Bounds*,
[arXiv:2609.24426v4](https://arxiv.org/abs/2609.24426v4).

New beyond round 5: [PROOF.md](PROOF.md) proves the proposed square-function
estimate with a restriction on spectral transfer in place of temporal
bounded variation. Let \(A=I-B\), \(G_u=(I-uB)^{-1}\), \(Q=I-P\), and
\(\Pi_j=\mathbf1_{(2^{-j},2^{1-j}]}(A)Q\). For measurable symmetric
contractions \(E(u)=QE(u)Q\), assume
\[
\Pi_iE(u)\Pi_j=0\quad\text{when }|i-j|>h.
\]
Then, without any temporal regularity,
\[
\int_0^t u^2E(u)A|B|G_u^2E(u)du
\preceq2(2h+1)t^2Q.
\]
For the same normalized errors and exact quadratic integral as round 5,
this gives
\[
|\mathcal J_t[D]_{xy}|
\leq\frac{2(2h+1)\delta^2t}{W^2}(G_tQ)_{00}.
\]
Fixed \(h\) therefore preserves the single return-kernel logarithm.
A version allowing nonzero distant couplings also holds: if
\(\|\Pi_iE(u)\Pi_j\|\leq c_{i-j}\) and
\(S=\sum_{m\in\mathbb Z}c_m<\infty\) uniformly in size and time,
replace \(2(2h+1)\) by \(2S^2\).

The dependence on the number of scales is sharp in order. Truncating the
earlier simultaneous swaps to square annuli gives continuous paths with
\(M=8^{R+2}\), \(t=1-M^{-4}\), and range \(h=6q+6\), for
every \(1\leq q\leq R\), such that
\[
\mathcal J_t[D]_{00}
\geq\frac{\delta^2\log8}{1440000W^2}qR.
\]
The square function also has a unit-vector quadratic form at least
\(q/20000\). Thus a size-independent bound cannot hold uniformly as
\(h\) grows, and the entry order \((h+1)\log M/W^2\) is attained in
this parameter range. For fixed \(q\), the examples' temporal variation
is \(2R\) while their spectral range stays fixed; the new criterion
controls cases where the earlier variation estimate grows with size.

What failed: using only blockwise triangle inequalities gives a needless
quadratic cost in \(h\). Applying contractivity before integrating reduces
it to the sharp linear order. The earlier pointwise envelope alone still
does not suffice. No implication from the full observable's positivity
and Ward identities to the new transfer criterion has been proved.

Validation was analytic. The proof includes two checks of the overlap
count, integral bound, Duhamel normalization, harmonic lower sum and final
constants; dyadic boundaries, negative modes, positive mass and the
extremes \(q=1,R\) were checked. Commands and opened sources are in
[LOG.md](LOG.md): `rg --files`, `ls -la`, `cat`, `sed`, `tail`, and the
web search tool. The priority probe
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
nice -n 15 /usr/bin/true` reported
`nice: setpriority: Operation not permitted`. No numerical job ran and
there is no computational script.

Limits: neither the normalized envelope nor the spectral transfer
assumption has been established for the random two-loop error. The
examples are not shown to preserve the full positivity and Ward
constraints or to arise from a resolvent. T076 remains open; there is no
new eigenvector or local-statistics theorem. No novelty is claimed for
the general dyadic operator argument.

Next worker: test the decaying-coupling condition on the actual normalized
error, after establishing an appropriate envelope. A concrete target is
\(\sup_u\|\Pi_iE(u)\Pi_j\|\leq C\rho^{|i-j|}\) with fixed
\(\rho<1\) and size-independent \(C\). First inspect its lowest-order
random expansion, rather than assuming that Ward row sums supply
spectral localization. If even this condition fails, seek a time-averaged
version of the row estimate (22) in PROOF.md; the pointwise sufficient
condition is not claimed necessary for a uniform square function.

All writes stayed in this folder. No git, external messages, registrations,
or subagents.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 10:32 Asia/Tbilisi.
