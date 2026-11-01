# QFORM threshold-to-three verification — 2026-09-24

## Verified mathematical state

I rechecked the currently committed fixed-multiplicity package and the five-singular-value audit chain.

The strongest bounded-density theorem supported by the committed audit records is

[
s_5(A)ge s>0 quadLongrightarrowquad
|p_{X^TAX+b^TX+c}|_infty<2400,K^2/s,
]

for arbitrary real symmetric (A), arbitrary affine terms, and independent original-coordinate inputs with scalar densities bounded by (K).

The same package records a full negative-half-moment theorem under three large singular values. It does **not** establish bounded density from (s_4(A)) or (s_3(A)).

The two complete written audits of the five-value result both report PASS/no fatal gap. Their stated checks include the grouped product-Fourier receiver, five-direction extraction, maximal-pair completion, all pivot branches, the three-direction half-potential appendix, scaling, and the four-value obstruction.

## Why the present proof stops at five

The current density receiver needs an order-three crossing resource. The five-direction structural argument can force the needed anchored/ordinary third-minor mass. The committed four-value obstruction shows that four unit-modulus eigenvalues can coexist with no pivot and zero disjoint third-order crossing volume. Therefore simply repeating the five-value extraction at multiplicity four cannot work.

This obstruction is to the *current route*, not to the conjecture. The next proof must exploit a receiver not requiring disjoint third crossing volume, or use the three-direction half-potential theorem to control the remaining shared-bank/hub geometry before absoluteization.

## Route toward three

The most promising rigorous bridge exposed by the current results is:

1. retain the proved (s_3) full negative-half-moment bound as the base smoothing resource;
2. split the no-pivot (s_3) case into physical pair/star/hub geometries without rotating the product variables;
3. use a pre-absolute-value shared-bank receiver (rather than the refuted mixed norm (int |t|^{-1/2}|G_t|_2dt));
4. route disjoint-source square/hyperbolic configurations through the already proved (L^{3/2})-by-(L^3) convolution receiver;
5. isolate the genuinely overlapping one-hub/shared-bank configuration as the remaining endpoint.

A proof of the last shared-bank receiver with constants uniform in fragmentation would close the present gap to the desired three-singular-value density theorem. No such proof is currently verified in the repository.

## Lean / Claude verification

I searched the current QFORM tree and recent repository commit history for QFORM Lean artifacts. I found no QFORM-specific `.lean` source, `lakefile`, `lean-toolchain`, successful Lean build log, or commit establishing formal verification of this theorem.

The recent commits explicitly mentioning Lean are for FEI and other projects, not QFORM. In particular, the newest Lean-tagged commit found on 2026-09-24 is an FEI commit co-authored by Claude, not a QFORM formalization.

Therefore the QFORM Lean algorithm/formal proof is **not presently verifiable from committed evidence**. It must not be described as verified or working until its source and build output are committed.

## Packaging defect found

The five-value README and audit say that the complete 1,093-line manuscript is stored beside the audits as `main.tex`, but the current GitHub directory contains only the two audits and README. A direct fetch of that advertised `main.tex` returns 404.

This does not by itself refute the theorem, because the audit records exist and the earlier 17-value baseline source is committed, but it prevents an independent source-level re-audit of the claimed final five-value manuscript from the present repository snapshot. The five-value source should be committed before treating the package as self-contained.

## Status

- 17 values: committed complete baseline proof.
- 5 values: strongest currently audited bounded-density theorem; two written audits report PASS.
- 4 values: bounded-density theorem open; naive third-volume extension is obstructed.
- 3 values: full negative-half-moment theorem supported; bounded-density theorem open.
- QFORM Lean verification: no committed formalization/build evidence found.
- Full three-value conjecture: OPEN / NOT PROVED / NOT DISPROVED.

This report deliberately does not promote the (s_3) half-potential result to a density theorem and does not claim Lean verification without kernel/build evidence.
