## October 2026 GitHub leads, inspected after the initial service search

Christopher D. Long, **A Sharp Capacity Criterion for Heterogeneous Four-State Potts Broadcasting on Trees**, 11 October 2026, https://github.com/long-mathematics/openai-math-extensions/tree/main/papers/01-heterogeneous-potts-capacity . The retrieved source and PDF study four states with heterogeneous edges and an L3 capacity criterion. They do not compare arbitrary numbers of Potts states. Their references point to the two sources below. Repository documentation explicitly distinguishes compilation and symbolic checks from independent peer review. No imported theorem here is treated as a solution of F0118.

OpenAI, **The Reconstruction Threshold for the Ferromagnetic Four-State Potts Model**, 5 October 2026, pinned commit **fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb**, https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026 . Theorem 1.1, PDF page 2, states (mathematical formatting transcribed):

> Theorem 1.1. For the channel (1.1), if dλ² ≤ 1, then lim_{n→∞} a_n(d,λ) = 0 in each of the following models:
> 1. the rooted d-ary tree, for every integer d ≥ 2;
> 2. the Poisson(d) Galton–Watson tree, for every real d > 0.
> In particular, the assertion includes dλ² = 1.

The objects are the uniform-root **four-state** ferromagnetic channel Pλ(j|i)=λ1{i=j}+(1-λ)/4. The probabilistic proof invokes a preserved higher-moment constraint and exact polynomial certificates. The PDF's statement, model and proof mechanism were inspected; the complete polynomial certificate computations were not independently re-run. This is a significant q=4 threshold lead, not the requested arbitrary-q monotonicity theorem. If its theorem is used as published, the q1=4 case follows immediately: reconstruction implies bλ²>1, and the all-q sufficient bound in ATTEMPT.md supplies reconstruction for q2. This implication is explicitly our argument and is not classified as SOLVED_IN_LITERATURE.

OpenAI, **A Capacity Criterion for Four-State Potts Reconstruction on Trees**, 5 October 2026, same pinned commit, https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026 . Theorem 1.1, PDF page 2, equates four-state reconstruction on bounded-degree deterministic trees with positive L3 capacity for squared channel resistances. Its imported posterior-law estimate is the companion threshold paper's Proposition 3.2. This criterion still concerns four states only.

The initial recursive OpenAI tree response was **truncated**. We therefore followed the exact two cited directories using GitHub's contents API at the pinned commit, then downloaded their PDFs and README files. Thus the two manuscripts were obtained despite the truncated global listing. All requests and payloads are recorded locally. These October leads were absent from the initial bounded arXiv results, so the GitHub search materially improved this status check.
