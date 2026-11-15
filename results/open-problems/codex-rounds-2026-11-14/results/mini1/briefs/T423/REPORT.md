VERDICT: PARTIAL exact reduction to terminal-mass equality and a scalar occupation estimate

For any fixed pair of solutions driven by the same white noise and any
finite deterministic T, PROOF.md proves that equality of their terminal
total masses almost surely is equivalent to equality of the full fields
throughout [0,T]. Writing D for the mass difference and A for the spatial
integral of (sqrt(u)-sqrt(v))^2 gives

\[
\mathbb E D_T^2=\mathbb E\int_0^T A_s\,ds.
\]

The remaining condition is exactly

\[
\mathbb E\int_0^T
 \mathbf1_{\{|D_s|<\varepsilon\}}A_s\,ds=o(\varepsilon).
\]

The normalized occupation expression tends to E|D_T|, also the expected
symmetric local time at zero of D; its finite-width error is at most
epsilon/2. There is a quantitative consequence:

\[
\mathbb E\int_0^T\|u_s-v_s\|_1\,ds
 \leq2\sqrt{mT\,\mathbb E D_T^2}.
\]

In particular the unnormalized occupation integral equals
2*epsilon*E|D_T| with an error between -epsilon squared and zero.
It is always O(epsilon), while uniqueness requires o(epsilon).

The proof uses the known single-solution super-Brownian marginal law
only for continuous total mass and its first moment m. It then derives
the same-white-noise joint bracket directly. This is a reduction, with
no claim of novelty. It does not prove the required occupation estimate
or resolve pathwise uniqueness for nonzero initial mass.

Checks: the bracket identity is independently re-derived by expanding
the two-mass covariance; the local-time normalization is checked with
both a piecewise quadratic and a smooth convex approximation. The
spatial Cauchy--Schwarz constant is checked on proportional profiles.
The marginal second-moment coefficient is also checked by deriving the
Feller mass Laplace transform.
Zero mass, vanishing denominators, all-space cutoffs, endpoint times,
and the upgrade from almost-everywhere equality to indistinguishability
are treated explicitly.

What failed: equal masses do not algebraically control A. Disjoint
smooth profiles, and arbitrarily close equal-mass mixtures, demonstrate
the obstruction. These are tests of an inequality, not SPDE
counterexamples. Projecting the common white noise onto the two mass
processes gives scalar drivers with correlation C/sqrt(UV), which need
not be one. Applying scalar pathwise uniqueness with an assumed common
Brownian driver would therefore be invalid.

Literature search: approximately 2.3 minutes, within the ten-minute cap.
No verified resolution of this exact equation was found. Hao Wang's
[arXiv:1612.06055](https://arxiv.org/abs/1612.06055) was withdrawn because
of a gap in the main proof. The recent papers opened do not establish
the theorem asked for:

- Leonid Mytnik and Johanna Weinberger,
  [arXiv:2509.10984v3](https://arxiv.org/abs/2509.10984v3):
  weak existence and uniqueness with irregular drift.
- Jie Xiong and Wen Xu,
  [arXiv:2610.41400](https://arxiv.org/abs/2610.41400):
  catalytic systems with colored noise and inward-drift assumptions.
- Yi Han, [arXiv:2611.07310](https://arxiv.org/abs/2611.07310):
  weak uniqueness with uniformly nondegenerate diffusion.

The original distinctions are confirmed by Yu-Ting Chen,
[arXiv:1308.5141](https://arxiv.org/abs/1308.5141), and Jie Xiong,
[arXiv:1203.4873](https://arxiv.org/abs/1203.4873). The latter explicitly
explains why uniqueness for its distribution-function equation does not
transfer to the density equation. Search coverage is limited; absence
of a hit is not proof that no later result exists.

Commands and saved work: LOG.md records the search queries and local
commands. The proof is analytic; no simulation or numerical computation
supports its conclusions. Files were written with apply_patch and read
back with sed. Local commands were prefixed by OMP_NUM_THREADS=1 and
nice -n 15 after the initial negligible directory listing. The nice
wrapper warned because processes already inherit nice 20, confirmed by
Python's os.getpriority. No git, subagents, external writes, or heavy
computation were used.

Next worker: investigate the occupation estimate above using spatial
information specific to same-noise solution pairs. A useful estimate
must control cancellation between regions where u>v and u<v; arbitrary
profile inequalities cannot suffice. Check any proposed estimate against
the equal-mass examples in PROOF.md before attempting to close it.

Task: “push this problem forward by one checkable piece” — 14 November
2026, 22:14 Asia/Tbilisi session start.
