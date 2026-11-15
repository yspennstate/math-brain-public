VERDICT: PARTIAL found a new edge-universality theorem relevant to T248; full statement not verified

The literature check found Guangchen Chen and Xing Lyu, *Tracy–Widom law for sample covariance matrices under quadratic form concentration*, [arXiv:2610.41416v2](https://arxiv.org/abs/2610.41416v2), revised 4 November 2026. Theorem 1.3 and Corollary 1.4 establish TW1 edge fluctuations for independent centered vectors with dependent coordinates under quadratic-form concentration and uniform covariance-edge regularity. This substantially advances the status supplied in the prompt. As instructed, the session stops at the literature stage.

[SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md) records the exact hypotheses, normalization, and conditional random-feature application. For fixed spherical-norm designs, centered Lipschitz activations give independent centered feature rows conditional on X, and bounded input operator norm gives the needed concentration. The remaining requirements concern the conditional covariance. The relevant sample count after transposing Y is m, not N; translating the theorem back multiplies eigenvalues by m/N.

Also opened: Renyuan Ma and Theodor Misiakiewicz, *The anisotropic local law for sample covariance matrices under quadratic-form concentration*, [arXiv:2609.09440v2](https://arxiv.org/abs/2609.09440v2). Its Proposition 2.8 and Example 2.11 explicitly support the concentration route for Lipschitz random features. Benigni–Péché arXiv:2201.04753v1 and Fan–Wang arXiv:2005.11879 were opened for context.

Checks against overclaiming: inspected the full theorem statements, rather than relying on abstracts; independently checked the Gram-matrix rescaling by singular values and by the identity YᵀY/N=(m/N)(YᵀY/m); checked the fixed-norm Gaussian marginals needed for exact conditional centering; distinguished dimension-uniform moment concentration from stochastic domination with a growing loss. The explicit exceptions and unresolved steps are listed in SOLVED_ELSEWHERE.md.

What was not proved: the full T248 assertion; deterministic edge centering for random designs at the TW scale; edge universality after arbitrary finite-rank outliers; the polynomial-activation extension; or aspect ratio one under the newly found theorem. The new papers were inspected for their statements and applicability, not independently re-proved or fully refereed.

Commands and search queries are in [LOG.md](LOG.md). No numerical experiment was run and no computation data file was produced. One tiny file-writing command used `OMP_NUM_THREADS=1 nice -n 15 python3`; the sandbox printed `nice: setpriority: Operation not permitted` but continued the file write. No further Python or numerical programs were launched. Subsequent document writes used the patch tool.

Next worker: first exploit the conditional theorem for spherical inputs and Lipschitz activations with the first three Hermite coefficients zero. Verify covariance regularity and control its finite-size edge, then address a nonzero second coefficient, critical/supercritical spikes, and conditional means for non-normalized designs. Do not label the complete original problem solved on the strength of the covariance theorem alone.

Task: “push this problem forward by one checkable piece” — 14 November 2026, first session clock reading 22:08:29 +04.
