# Theorem-closure and formalization-status audit

## Source pins

- Objective: \`QFORM-FIXED-MULTIPLICITY-AUDIT-20260924\`.
- Standalone source: \`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex\`.
- Source commit: \`eeb752c8943536541b34b42b8bf48e924f4d3d2f\`.
- Source blob: \`19fb119877426b640b2c0dae19ec2f78a399fe11\`.
- Constant-385 sharpening: commit \`582b941e4fc5270d3b5cc2da4675888929288ade\`.

## Verdict

**PASS** for theorem quantifiers, normalization, rescaling, interval/density equivalence, and dependency closure. The independently audited proof supports
\[
\boxed{\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
 <385\,\frac{K^2}{s}}
\qquad\text{whenever }s_9(A)\ge s>0.
\]
This audit does not lower the multiplicity below nine.

## Quantifier ledger

The theorem covers, without hidden restrictions:

- every finite dimension \(n\);
- arbitrary independent real coordinates with possibly different Lebesgue densities \(0\le f_i\le K\) almost everywhere;
- arbitrary real symmetric \(A\), all signatures, and arbitrary remaining spectrum;
- arbitrary deterministic \(b\in\mathbb R^n\) and \(c\in\mathbb R\);
- unbounded and fragmented supports, without moments, smoothness, log-concavity, identical distribution, or exact-rank assumptions.

Replacing each density by a Borel representative clipped on its null exceptional set does not change the coordinate law and legitimately permits pointwise cap statements inside Tonelli arguments.

## Exact normalization and rescaling

Set \(Y=KX\). Its coordinate densities are
\[
g_i(y)=K^{-1}f_i(y/K)\le1.
\]
Define
\[
\widetilde Q
 =Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c.
\]
Then \(s_9(A/s)\ge1\) and, identically,
\[
\widetilde Q=\frac{K^2}{s}Q,
\qquad
Q=\frac{s}{K^2}\widetilde Q.
\]
If the normalized density cap is \(C\), scalar pushforward gives
\[
p_Q(t)=\frac{K^2}{s}\,
p_{\widetilde Q}\!\left(\frac{K^2}{s}t\right),
\qquad
\|p_Q\|_\infty\le C\frac{K^2}{s}.
\]
There is no missing factor of \(K\), \(s\), or two. The affine terms scale compatibly and are allowed to be arbitrary in every normalized analytic input.

## Interval formulation

A density cap \(C\) immediately gives \(\mathbb P(Q\in J)\le C|J|\) for every interval. Conversely, interval domination extends first to open sets via their countable disjoint interval decomposition and then to all Borel sets by outer regularity. Hence the law is dominated by \(C\) times Lebesgue measure, and Radon--Nikodym yields an essentially bounded density. This avoids selecting point values of a rough density version.

## Dependency closure

Every specialized analytic and algebraic ingredient used by the theorem is reproved in \`paper.tex\`: Fourier inversion and Riesz estimates, geometric Brascamp--Lieb, projection bounds, decoupling, determinant estimates, grouped mollified-\(L^2\), row promotion, scalar/pair pivots, half-potentials, volume sampling, interpolation, and rank accounting. The cited classical works are antecedents, not hidden proof dependencies.

All probabilistic conditioning is on original coordinate sigma-fields. Deterministic rotations occur only inside integral or matrix estimates. No post-rotation independence is invoked.

## Formal-verification status

The pinned package exposes:

- \`verify_new.py\`, a Python/SymPy/NumPy checker;
- \`checks_new.json\`, its finite exact and floating diagnostic output;
- \`MANIFEST.json\`, which explicitly describes these as finite checks rather than proof.

The checker verifies 96 exact interpolation seeds, eight exact aggregate overlap cases, exact rational constant inequalities, and eight floating spectral diagnostics. Its own docstring says “not formal verification,” and the manifest likewise says finite tests do not replace the general proofs.

No Lean source, \`lakefile\`, compiled Lean artifact, theorem declaration, or Lean toolchain metadata is listed in the complete package manifest or README. Therefore the nine-eigenvalue theorem is **not Lean-verified by the pinned package**. A repository-wide code-search attempt for Lean imports was transiently rate-limited, so this report makes no claim that unrelated or work-in-progress Lean files exist nowhere else. What can be verified is that no Lean certificate is part of the theorem package presently under audit.

## Remaining obligations

1. Integrate the independently proved constant 385 into the standalone manuscript after the review gate.
2. A second genuinely independent end-to-end reconstruction is still needed for the owner's independent-validation criterion.
3. Lowering \(s_9\) to \(s_8\) still requires a product-preserving analytic receiver for the shared-coordinate overlap term.
4. The unrestricted three-eigenvalue conjecture and continuity remain open.
