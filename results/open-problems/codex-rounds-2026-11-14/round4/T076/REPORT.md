VERDICT: PARTIAL quadratic drift bound without an extra logarithm under a commuting low-mode envelope

The round-3 return-kernel asymptotic holds. An independent Fourier-cell
integral comparison and a covariance check recover its coefficient
5/(4*pi). A literature check under five minutes found no later solution
to T076; Xujie Lai and Fan Yang,
*Localization Lengths for Two-Dimensional Random Band Matrices: Exponential
Lower Bounds*, [arXiv:2609.24426v4](https://arxiv.org/abs/2609.24426v4),
remains the relevant inspected two-dimensional advance.

New beyond round 3: [PROOF.md](PROOF.md) treats the quadratic drift
\(W^2DBD\) with the exact two-coordinate Duhamel propagator from
Lai–Yang (2.33)–(2.39). Write \(G_u=(I-uB)^{-1}\), \(Q=I-P\),
\(a_k=1-b_k\). For real symmetric translation-invariant errors satisfying
\[
d_u(0)=0,\qquad
|d_u(k)|\leq\delta uW^{-2}a_k(1-ub_k)^{-2},
\]
the integrated term obeys
\[
-\delta^2tW^{-2}G_tQ\preceq\mathcal J_t[D]
\preceq\delta^2tW^{-2}G_tQ.
\]
Its entries are bounded by \(\delta^2tW^{-2}(G_tQ)_{00}\), retaining
the return kernel's single logarithm without another time logarithm.
The logarithmic order is sharp within this deterministic class.

The weaker envelope \(D(u)=\delta uW^{-2}G_uQ\) fails: its exact
quadratic integral is \(\delta^2t^3(3W^2)^{-1}BG_t^2Q\).
For \(0<1-t\leq M^{-4}\), its diagonal is
\[
\frac{\delta^2}{W^2}\left[c_*M^2+O(\log M)\right],\qquad
c_*=\frac{25}{48\pi^4}
\sum_{k\in\mathbb Z^2\setminus\{0\}}|k|^{-4}>0.
\]
Thus uniformly small centered error entries need not give a small
integrated quadratic drift. The coefficient is checked through a
real-space square-norm identity and Parseval, and the exact M=3 value
is independently verified as \(35\delta^2/(243W^2)\) at zero mass.

What failed and what remains uncertain: the weak family need not make
the approximate two-loop observable entrywise nonnegative. It is an
obstruction only under the explicitly stated envelope assumptions,
not a counterexample to the random-matrix dynamics. The sufficient
low-mode envelope has not been proved for a random resolvent error;
translation invariance also excludes its Fourier-mode couplings.
No new eigenvector, localization-length or local-statistics theorem is
claimed, and no novelty in deterministic Fourier analysis is asserted.

Commands and opened sources are in [LOG.md](LOG.md). Verification was
analytic; document inspection used `rg --files` and
`OMP_NUM_THREADS=1 nice -n 15 /bin/cat ...`. The sandbox emitted
`nice: setpriority: Operation not permitted`; no numerical experiment
was launched under unverified priority. All writes stayed here.
No git, external registration, external messages or subagents.

Next worker: examine the Fourier matrix elements of the actual centered
two-loop error. Seek a bound with the factor
\(a_k/(1-ub_k)\) before the diffusion time, or an averaged replacement
that controls noncommuting Fourier couplings. Establishing such a
bound, rather than improving the diagonal return estimate, is the
missing step needed to use this quadratic-drift lemma.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 04:39 Asia/Tbilisi.
