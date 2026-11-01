# Thirty-agent DNN/probability research campaign — 23 October 2026

**Completed: 30 distinct GPT-6 workers with max reasoning, in waves under the six-worker concurrency limit. All 30 reports are preserved. The scoped T336 constructions, encoder grid, unconditional pretraining bound, and finite-mixture circuit passed independent agent review.**

The useful frontier work is now on **T336: quantitative GP posterior approximation and pretraining**. T228's smooth nonlinear stationary-tail theorem was already present in Brain. We preserve our replication, exact certificates, and the novelty correction rather than count it as a new solution.

## Read first

- [T336 synthesis and scope](research/T336_SYNTHESIS.md): conservative joint covariance, explicit RBF truncation/encoder, and Gaussian-NLL pretraining.
- [Claim register](CLAIMS.json): proved statements, limits, and review status.
- [Directions and rejected approaches](DIRECTIONS.md).
- [Provenance and overlap](PROVENANCE.md).
- [All 30 worker reports](agents/) and [reproducible checks](research/code/).

## What is established in the current notes

1. A data-space one-sided Chebyshev inverse gives a **conservative joint GP covariance** at every depth. Its residual is minimax among nonnegative residual polynomials of the same degree. The signed-dot-product operation has an exact implementation using two unnormalized ReLU-attention heads with stated masks and local linear mixing. The classical Chebyshev extremal theorem and scalar accelerated GP construction are prior work.
2. Explicit finite RBF features, followed by a quantitative raw-input ReLU encoder, give uniform forward-KL approximation on compact inputs and bounded context labels. The proof gives the feature count, encoder size, attention width and depth. This is an exact-real-arithmetic construction, not a softmax/layer-normalized architecture claim.
3. A finite-class ERM theorem controls **unconditional GP-prior averaged predictive KL**, with unbounded Gaussian context and query labels. An explicit encoder grid supplies a comparator, a sample bound, and a consistency sequence. See [the unconditional theorem](research/T336_UNCONDITIONAL_ERM.md) and [the grid construction](research/T336_ENCODER_GRID.md). This is statistical ERM, not a claim about SGD convergence.
4. Polynomial inverse and trace-log approximations give quantitative evidence-weight and predictive-mixture KL bounds for a finite hierarchical GP. [A30](agents/a30.md) constructs the restricted finite-feature circuit, including a padding-safe trace and a simplex-preserving ReLU readout; [A29](agents/a29.md) independently audits it. Its mixture pretraining theorem remains open.

The exact rational counterexample in A27 has a valid PSD joint Gram and noise variance 1/10: an ordinary depth-one data-space Chebyshev approximation produces variance **−17/30**, whereas the one-sided correction produces **21/110**. This does not contradict prior feature-space constructions whose variance already has a positive noise floor.

## What is not claimed

This package does not claim to have solved all of T336, discovered Chebyshev iteration, proved efficient SGD pretraining, or established external publication priority. Internal independent agent audits are not external peer review. The original unrestricted uniform-over-datasets statement requires additional assumptions; the constructive uniform theorem bounds inputs and context labels, while the statistical theorem concerns an average under a specified GP prior.

T069 was excluded as already solved. T228 was investigated before its newer full closure record was located; the package explicitly credits that prior proof. Basic scalar finite-rank T336 acceleration was also already reviewed in Brain, despite a stale dossier suggesting otherwise. See PROVENANCE.md for pinned sources.

## Reproduce

```bash
python research/code/a14_checks.py
python research/code/a20_certificate_audit.py
python research/code/a27_gp_checks.py
```

The first two scripts provide independently derived rational T228 contraction certificates. The third checks the GP recurrences, covariance inequalities, RBF truncation and KL bounds, including exact small examples. Floating-point experiments support algebraic checks; they are not replacements for the proofs.

This same package is published under `research_pushes/2026-10-23-codex30-frontier/` in Math Brain and `06_math_research/codex30_frontier_2026_10_23/` in Brain. The live coordinator receives a linked handoff. Repository persistence and a relay receipt do not by themselves establish native-store ingestion.
