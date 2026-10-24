# Solo FEI continuation: conditional entropy of spectral coordinates

Started 2026-09-17T22:58:53Z. User instruction: choose a famous breakthrough-level problem, work alone for the next ten hours, and push all work to the existing GitHub repository. No subagents are authorized or used.

Target: the full Friedgut–Kalai Fourier entropy–influence conjecture (1996), with bit entropy and uniform-cube Fourier coefficients. A proof would be a major result in Boolean analysis and theoretical computer science. There is no claim that a ten-hour attempt is likely to solve it.

The previous P03 FEI handoff is `proofnet24/P03-fei/handoffs/2026-09-17T00-45-21Z__FEI-hard-handoff.md`. The previous fixed-dimension certification metric remains 6, as reported there; it has not been independently reverified in this session. The old local restriction payment and coordinate-compression approaches are already recorded as failed. This session does not restart either one.

## Idea recorded before experiments

Let p(S)=fhat(S)^2 and let X be a random subset with law p. Study the erasure entropy

    B(f) = sum_i H(X_i | X_{[n]\{i}}).

This differs from the sum of the marginal entropies, which is already known to lose a dimension factor. Each conditional entropy pairs adjacent Fourier coefficients, so the complete original-coordinate geometry is retained.

For a coordinate restriction define

    Delta_i(f) = H(f) - [H(f_{i=+1})+H(f_{i=-1})]/2.

The candidate exact identity is

    Delta_i(f) = B_i(f) + JS(p_{f+},p_{f-}),

where JS is Jensen–Shannon divergence in bits. The scalar estimate JS <= (2/ln 2) Inf_i(f), if proved, means a dimension-free B(f) <= K I(f) would imply FEI with constant K+2/ln 2 by choosing a suitable coordinate at each restriction. Conversely B(f)<=H(f) makes this proposed inequality necessary up to constants. Thus the target has the full scope of FEI, not merely a finite-dimensional surrogate.

Initial methods: (18) translate to conditional information; (2) try to refute a uniform or sharp proposed B/I bound; (11) derive a dual or variational form for the residual logarithmic term.

We will stress-test tensor products, rare flips, bent functions, compositions and structured Boolean functions. No finite experiment will be treated as a proof. Prior-art status of this exact formulation is unverified.

## Current primary sources checked

- Friedgut and Kalai, original source locator from the repository: unnumbered conjecture, p. 2999, end of section 5, *Every monotone graph property has a sharp threshold* (1996), DOI 10.1090/S0002-9939-96-03732-X.
- González–MacManus–Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, 9 June 2026. Their restriction/induction program is relevant prior art: https://arxiv.org/pdf/2606.00246 . The new notation here is not a claim to have invented restriction induction.
- Shalev, *On the Fourier Entropy Influence Conjecture for Extremal Classes*, arXiv:1806.03646: https://arxiv.org/abs/1806.03646 . Extreme low-influence classes and sublinear-threshold reductions are relevant barriers.
- Arunachalam et al., *Improved Bounds on Fourier Entropy and Min-Entropy*, STACS 2020: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2020.45 . Certificate bounds cannot be presumed to give a universal influence bound.

The literature search is bounded, not a novelty certificate. A current paper treating the problem as open was found; absence of another resolution in search results is not proof that none exists.

## Execution and provenance

All work is by the main assistant; no spawned agents or outside audits. Actual model/reasoning metadata: not exposed in a verifiable runtime record. The requested ten-hour interval ends 2026-09-18T08:58:53Z. The available scheduler can trigger bounded solo continuations, but does not guarantee continuous execution, per-run duration, or a specific model/reasoning setting. Actual scheduling receipt will be recorded separately when available.

Status: full FEI OPEN; this is a research attempt.
