# T228: complete proof for the portfolio's concrete-model request

23 October 2026. Private research campaign; 30 requested GPT-6 agents, maximum reasoning requested, at most six subagents active concurrently.

**T228's concrete-model requirement is proved and independently internally audited.** The complete 13-page proof is `manuscript/T228_Proof.pdf`, with editable source `manuscript/T228_Proof.tex`. This supplies an explicit certificate for the original registry's average-contraction requirement, building on the previously verified T1–T3 dossier work. It does not establish a new discovery or an official increase in the solved-row count. The earlier T069 result is a carried-forward portfolio status, not a result re-audited by this campaign. This package does not change the central registry's status field or claim external peer review.

The registry asks for one specified nonlinear regression model, average contraction of its actual SGD maps, an invariant law, an asymptotically linear nonarithmetic multiplier, and an exact power tail with a strictly positive constant and index below two on a nonempty parameter range. The exact row and a thirteen-obligation audit are preserved in `sources/T228_REGISTRY.json` and `T228_OBLIGATION_MAP.json`.

## The completed model

Let

\[
\sigma(z)=z+10^{-3}\tanh z,\qquad
Y=\sigma(A\theta)+E,\qquad A,E\stackrel{\mathrm{ind}}\sim N(0,1),
\]

with fresh independent samples at every step. Train the scalar parameter with the squared loss and ordinary, unclipped, constant-step SGD:

\[
X_{n+1}=X_n-\eta A_{n+1}\sigma'(A_{n+1}X_n)
\bigl(\sigma(A_{n+1}X_n)-Y_{n+1}\bigr).
\]

For every fixed \(|\theta|\le1\) and \(0.99\le\eta\le1.01\), at batch size one:

- The actual random maps satisfy \(\mathbb E\operatorname{Lip}(\Psi)<0.99010707<1\).
- There is exactly one invariant probability law, even without imposing a first-moment assumption on a competing invariant law. Every deterministic start converges geometrically in Wasserstein distance of order one.
- There is a unique positive exponent \(\alpha\in(1,2)\) satisfying \(\mathbb E|1-\eta A^2|^\alpha=1\).
- For a finite strictly positive constant \(C_{\eta,\theta}\),

\[
\lim_{t\to\infty}t^\alpha\Pr_{\pi_{\eta,\theta}}(|X|>t)
=C_{\eta,\theta}\in(0,\infty).
\]

The same constant describes the tail of \(|X-\theta|\). Positive moments are finite exactly below \(\alpha\); in particular, stationary variance is infinite. The choice \(\theta=1,\eta=1\) is a genuine nonzero-signal example with a unique population-risk minimizer at one.

The proof supplies a uniform bounded remainder, verifies every scalar implicit-renewal hypothesis, and separately proves strict positivity by a joint-law tilt, uniformly tight overshoots, summable discounted errors, compact minorization, and a finite-horizon stationary last-exit argument. It never factors dependent within-step quantities or subtracts two infinite stationary moments.

## Additional results in the package

The main PDF is frozen at the audited batch-one theorem. Separate supplements preserve the additional results without changing that reviewed manuscript:

| Result | Proof | Independent review |
|---|---|---|
| Smooth, strictly decreasing batch-one tail index on \(0.99\le\eta\le1.01\) | `proofs/T228_INDEX_DEPENDENCE.md` | `reviews/A25.md` |
| Zero-teacher, batch-one moment phase diagram on \(0.99\le\eta\le1.01\), including linear critical growth and exact exponential supercritical growth | `proofs/T228_MOMENT_DYNAMICS.md` | `reviews/A25.md` |
| Batch-two interval \(1.1\le\eta\le1.2\), \(|\theta|\le1\), with contraction bound \(0.8680084\) | `proofs/T228_BATCH_TWO.md` | `reviews/A29.md` |
| Batch-one equal positive one-sided tail constants for \(|\theta|\le1\), \(0.99\le\eta\le1.01\), without symmetric stationary body when \(\theta\ne0\) | `proofs/T228_SIGNED_TAILS.md` | `reviews/A29.md` |
| Direct applicability of the original Mirek theorem, including its extra positivity condition | `reviews/A17.md` | `reviews/A28.md` |
| Certified tail-index brackets using interval arithmetic and analytic quadrature error | `checks/A13_tail_index_certificate.py` | `reviews/A24.md` |

For batch one the certified strict brackets are:

| Learning rate | Tail index |
|---:|---:|
| 0.99 | \(1.10928<\alpha<1.10929\) |
| 1.00 | \(1.09082<\alpha<1.09083\) |
| 1.01 | \(1.07272<\alpha<1.07273\) |

The probability proof does not rely on numerical quadrature, simulation, or those brackets. The certificate relies on the documented Python Decimal arithmetic contract and is not proof-assistant formalization. A24 reproduced an invalid `PASS` from the historical script under optimized Python; the current executable rejects optimized execution before computation. The negative-test fixture is preserved as evidence of that repaired failure, not as a valid certificate.

## Scope and credit

The activation is **unbounded**, with a bounded smooth nonlinear perturbation of the identity. The registry's audited solver route explicitly allows this example. The result does not settle arbitrary neural-network losses, the illustrative architecture with a globally bounded activation, fixed-dataset sampling, every step/batch combination, or a universal minibatch monotonicity statement.

The contribution is an explicit verified application of existing general tail theorems, together with a concrete global-contraction regime and audited extensions. The prior dossier already marked all three repaired T228 targets verified. A concurrent campaign independently flagged that overlap; its source notice and the final counting clarification are preserved in `sources/CONCURRENT_T228_NOVELTY_CORRECTION.json` and `reviews/A30_followup_scope.md`. This campaign does not count the preexisting tail results again. It is not a claim that the underlying renewal or asymptotically linear-map theory was discovered here. Existing Math Brain T228 work is credited, including `w688`'s scalar argument, `claude_4af6ff1a`'s scalar leaky-ReLU work, and `claude_b1e26540`'s radial and forward-excursion positivity proofs. The main proof uses Jelenković–Olvera-Cravioto, arXiv:1006.3295v5, Theorem 3.1. A17/A28 verify the original Mirek route, and A23/A29 verify the ABB route.

All nineteen retrieved T228 source blob pins match. A historical second T3 review receipt was reported in the existing dossier but was not recovered; it is not presented as a verified receipt. Current acceptance rests on the newly recorded independent mathematical reviews. Some side-study source files underwent line-ending normalization during initial retrieval; exact remote bytes were subsequently recovered, their Git blobs verified, and the precise normalization documented in `SOURCE_PIN_RECOVERY.json`.

The initial baseline version-one hash appears in historical reports. The complete version-two baseline and its self-contained nonzero-teacher extension are the accepted sources; current proof validity does not depend on possession of that superseded draft's bytes. `CORRECTIONS.json` records historical and current versions honestly.

## Other research preserved

The campaign also produced and reviewed substantive partial work for other rows. These are not counted as additional solved rows:

- **T336:** an explicit raw-input transformer approximation for continuous PSD kernels on compact Euclidean domains, including infinite rank and an RBF specialization, uniformly over bounded context length and bounded context-label magnitude with positive observation noise. A separate prior-average ERM/generalization bridge permits genuinely unbounded Gaussian target labels and handles context tails by clipping. Kernel continuity and the stated architecture remain assumptions. The results do not establish optimizer convergence or the unrestricted bounded-kernel statement. See `../a02`, `../a05`, and reviews A19/A20.
- **T421:** a conditional diagonal-Adam classification assuming convergence of the second-moment coordinates, together with sharpness and epsilon-regime consequences. The general initialization and convergence obligations remain open. See `../a06` and review A21. The explicit specialization to beta1=0.9 is recorded before the threshold 38 is used.
- **Portfolio triage:** exact scope and unresolved obligations for T354, T357, T366, T248 and other candidates remain in `../a03/TRIAGE_REPORT.md`.

## Evidence and persistence

The agent roster distinguishes authors, alternative-route researchers, mathematical reviewers, literature auditors, and reproducibility auditors. Thirty agents do not mean thirty independent full-proof reviews. The requested configuration is recorded; underlying backend execution metadata beyond the tool configuration is not independently certified.

The complete package preserves proofs, source pins and recovered source bytes, every agent report, runnable checks and outputs, corrected historical versions, the manuscript, and manifests. `admin/CHECKPOINT_SAVE_RECEIPTS.json` records the initial successful saves and exact readbacks in both private repositories. The final repository commits and immutable verification receipts are recorded separately after upload. Repository persistence is distinct from native Brain graph ingestion; no native ingestion, external acceptance, public release, or messages to other people are claimed.

The root verification command for the assembled package is:

```bash
python campaign/checks/A26_verify_bundle.py --root . --manifest MANIFEST.json
```

The certificate can be independently rerun with ordinary, non-optimized Python:

```bash
python campaign/checks/A13_tail_index_certificate.py --output /tmp/t228-replayed-certificate.json
```

The current completion roster and final manifest govern package readiness; early checkpoint notices and author-candidate labels remain as dated historical evidence.
