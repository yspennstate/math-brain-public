# Source comparison and novelty boundary

Checked during the 19 September 2026 continuation. The source facts below
are separated from the new derivations in MIXED_SPECTRUM.md. No exhaustive
priority search or independent novelty certificate is claimed.

## Existing owner research actually read

- `research_pushes/2026-09-18-sidorenko-fei-ising/SIDORENKO.md`, Git blob
  `dd296b0f524e6ce34e3e4b8e1371abd7f10b97d3`: exact rank-two polynomial,
  fixed-eigenvalue optimizer, sharp sixth-order remainder, and rank-three
  counterexamples to positivity-preserving truncation and spectral addition.
- `proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T18-50-49Z__report.md`,
  blob `ed1e908b6b6329892805b5812ad38cd61b0af368`, especially its Section 6:
  bipartite subcubic graphs with a zero cubic-moment tensor. The fair-sign
  extension here is not the same hypothesis: mixed base/sign moments are
  allowed and are accounted for by nonnegative base-edge factors.

The earlier constant-degree three-block theorem and its historical audits
are not newly produced by this continuation. No old audit is re-counted as
an audit of the results here.

## Primary literature inspected

1. Joonkyung Lee and Bjarne Schuelke, *Convex graphon parameters and graph
   norms*, arXiv:1910.08454v2 (16 January 2020).
   https://arxiv.org/abs/1910.08454
   Its abstract identifies the exact H as a notorious Sidorenko example and
   states that H is not weakly norming. This prevents claiming a general
   graph-norm argument merely from successful restricted calculations.

2. Laszlo Lovasz, *Subgraph Densities in Signed Graphons and the Local
   Simonovits--Sidorenko Conjecture*, Electronic Journal of Combinatorics
   18(1), #P127 (2011), DOI 10.37236/614; arXiv:1004.3026 (2010).
   https://www.combinatorics.org/ojs/index.php/eljc/article/view/v18i1p127
   https://arxiv.org/abs/1004.3026
   The official abstract proves signed graphon/cycle inequalities and a
   local Sidorenko theorem. The existence of an all-rank local neighborhood
   is therefore NOT claimed as new. Our note gives its own short induced-
   cycle/Schatten proof and records the H-specific theta cancellation and
   explicit error polynomial. No optimality of the local radius or a
   best-known improvement is claimed.

3. Daniel Kral', Taisa Martins, Peter Pal Pach and Marcin Wrochna,
   *The step Sidorenko property and non-norming edge-transitive graphs*,
   arXiv:1802.05007v4 (6 December 2019).
   https://arxiv.org/abs/1802.05007
   The official abstract distinguishes the stronger step property and says
   many bipartite graphs fail it. Consequently our proved module-replacement
   rule is not promoted to unrestricted conditional-averaging monotonicity.
   The exact obstruction in the owner archive remains a separate check.

4. Grigoriy Blekherman, Annie Raymond, Mohit Singh and Rekha R. Thomas,
   *Simple Graph Density Inequalities with No Sum of Squares Proofs*,
   arXiv:1812.08820v1; Combinatorica 40 (2020), 455--471,
   DOI 10.1007/s00493-019-4124-y.
   https://arxiv.org/pdf/1812.08820
   The original PDF was read, including its page 3 / Corollary 1.5 and the
   definitions of its graph-gluing algebra. It proves that H is a trivial
   square, H-e^15 is not a sum of squares in that algebra, and multiplication
   by 1+g with g a sum of squares does not repair this. This is an important
   restriction on a naive unrestricted finite-SOS completion. It does not
   forbid our restricted Bernstein certificates, smallness-dependent bounds,
   a constrained regular-kernel argument, or analytic/limit methods.

5. Pranav Garg, Annie Raymond and Amanda Redlich, *Non-Trivial Squares and
   Sidorenko's Conjecture*, Electronic Journal of Combinatorics 32(4),
   #P4.54 (28 November 2025), DOI 10.37236/11339.
   https://www.combinatorics.org/ojs/index.php/eljc/article/view/v32i4p54
   The official abstract discusses sum-of-squares limitations and small
   target graphs. This is relevant context, not a proof of our claims and
   not evidence that all possible spectral arguments are impossible.

6. Yuqi Zhao, *Tensor Amplification and Spectral Transfer for Sidorenko-Type
   Inequalities*, arXiv:2607.02260v1 (2 July 2026).
   https://arxiv.org/abs/2607.02260
   The official abstract gives equivalences within admissible classes. It
   does not turn one restricted class into all graphons by itself. This
   paper is not used as an unverified dependency of any theorem here.

## Search limitations

Searches covered the exact H, rank-two kernels, negative spectrum,
hierarchical/refinement constructions, local Sidorenko, and graph-algebra
sum-of-squares limitations. Several broad searches returned unrelated
material. Such responses are not evidence of novelty or absence of a
resolution. The reliable distinctions above rest on the directly inspected
primary sources and the explicit proofs in this package. A fresh specialist
comparison is still needed for the exact host-class closure principles and
numerical local constant. No third-party full text is republished here.
