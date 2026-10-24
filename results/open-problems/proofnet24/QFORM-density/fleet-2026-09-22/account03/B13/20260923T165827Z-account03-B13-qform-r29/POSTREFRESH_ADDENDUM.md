# account03/B13 r29 post-refresh proof clarification

Status: proof clarification preserving `QFORM-BIHUB-VOLUME-CASCADE-CLOSURE-v1`; full QFORM and global continuity remain OPEN.

Fresh control remained QFORM-only at OWNER CONTROL revision `2026-09-22.15`. No correction invalidating the source-pinned projected-crossing receiver was found in the fresh correction/search pass. The receiver itself remains a complete written supporting argument pending independent review, so the r29 theorem remains conditional on that source exactly as stated in `REPORT.md`.

## Necessary physical-conditioning clarification

In Stages 1 and 2 of `REPORT.md`, the grouped projected-crossing theorem is applied **after conditioning every original coordinate outside `L union R`**. This is essential for the row-marginal gate and is the intended proof.

After that conditioning, all outside interactions become deterministic affine terms. They are permitted by the receiver and do not change the cap-one product law of the still-random original coordinates in `L union R`.

### Stage 1

Use hub `H={i}`, light row bank `I=L\{i}`, and light column bank `J=R`. The hub-to-`J` row is exactly `m=B[i,R]`. The projected crossing matrix in the receiver is therefore **exactly** the matrix with rows

`c_a=P_(m^perp) n_a`, `a in L\{i}`,

not a larger matrix. Thus its two-volume currency is exactly `Z2=e2(CC^T)`, and the row marginals required by the receiver are exactly the `gamma_a` defined in the report. Hence `gamma_a<=1/2` for all `a` is precisely the theorem's gate.

### Stage 2

After the same conditioning, use hubs `H={i,h}`, light row bank `I=L\{i,h}`, and `J=R`. The hub-to-`J` matrix is exactly `M2=[m;n_h]`, and the projected crossing rows are exactly

`d_a=P_(span{m,n_h}^perp)n_a`, `a in L\{i,h}`.

Thus the receiver's one-volume currency is exactly `Z1=sum_a||d_a||^2`, and its row marginals are exactly `delta_a=||d_a||^2/Z1`. Therefore `delta_a<=1/2` is exactly the required gate.

### Stage 3

One may either keep the same conditioning and use the three hubs `{i,h,h2}` against the surviving light coordinates, or use all remaining original coordinates without conditioning. In either case the full hub cross block contains the restriction `M3` on columns `R`, so its three-singular-value product is at least that of `M3` by Loewner monotonicity of the 3x3 Gram matrices. The exact rank-three crossing receiver therefore applies with the same lower bound.

This conditioning repair removes a possible ambiguity in the original wording “contains `C` as a row submatrix”: merely enlarging a projected crossing matrix would preserve `e2` but would not preserve the row-marginal `<=1/2` gate. The actual proof uses the exact conditioned matrix, so no such monotonicity assertion is needed.

All conditioning is on disjoint ORIGINAL coordinates. No independence after spectral rotation is asserted.
