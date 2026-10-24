# B20 r5 late source refresh — exact release status of the new nine/400 revision

During this invocation `scheduled_tasks/CURRENT_OBJECTIVE.md` advanced the release-gate source from the earlier nine-direction reconstructions to the new self-contained revision

- source commit `eeb752c8943536541b34b42b8bf48e924f4d3d2f`;
- blob `19fb119877426b640b2c0dae19ec2f78a399fe11`;
- SHA-256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`;
- `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`.

The exact new candidate is

` s_9(A)>=s  =>  ||p_{X^TAX+b^TX+c}||_infinity <= 400 K^2/s `

for arbitrary independent real coordinate laws with density cap `K`, arbitrary real symmetric `A`, arbitrary dimension/signature/remaining spectrum, and arbitrary affine terms.

## Release verdict for this exact revision

**PENDING / NOT YET INDEPENDENTLY VALIDATED.**

The package itself labels `AUDIT_NEW.md` as an authoring-agent self-audit. The complete B16/B19 reviews visible before this source pin predate commit `eeb752...` and therefore do not automatically certify this exact revision. B20 does not transfer those certificates to a later blob.

This invocation independently checked the following high-risk transitions in the new source:

1. theorem quantifiers and `K^2/s` scaling: PASS;
2. product-projection bound and zero-weight handling: PASS;
3. decoupling and regularized determinant derivation: PASS on the inspected chain;
4. grouped mollified-`L^2`/weighted-Holder mechanism and its product provenance: PASS on the inspected chain;
5. marginal-free order-three/order-two row-promotion interfaces: PASS on the inspected chain;
6. nonsymmetric interpolation support, global rank `<=3r`, restricted rank `<=r`, and the `4k-3` diagonal-dominance contradiction: PASS;
7. full pair half-potential scaling `D^{-1/4}` and normalized constants: PASS;
8. final branch arithmetic: PASS; the listed bounds are safely below 400;
9. overlap theorem Frobenius orthogonality and `s_8` corollary: PASS on the inspected chain;
10. regularity scope: PASS — the theorem claims essential boundedness globally, not global continuity.

However, this source appeared during the run after the initial mathematical reduction had already been developed. B20 has **not** performed a fresh line-by-line reconstruction of every one of all 955 source lines in this invocation. Therefore this note is not counted as a complete independent review of the exact `eeb752...` revision. The correct release state is unchanged until two complete post-pin reviews exist.

For the previously reviewed nine-direction theorem, multiplicity nine remains the lowest release-grade threshold. The stronger constant `400` is a candidate improvement awaiting its own two independent exact-source reviews; B20 does not downgrade the theorem itself merely because the improved constant is newly pinned.

## New below-nine mathematics from this same run

The companion `REPORT.md` at commit `74542593cca87e76d83b07f98e2c895f76b90796` proves `QFORM-S8-ROBUSTPAIR-ONEHIGH-CLOSURE-v1`: in the robust physical two-anchor `s_8` collar, every state with at most one leverage score above `2/3` has product-usable disjoint third-volume `W_dis>g/48` and hence a continuous density `<23.48`. Thus an unpaid robust-pair state must have exactly two high-leverage complement coordinates, and their literal `2x2` anchor cross minor satisfies `det(C_{ij})^2>g/3>=0.12164808862756733...`.

This does not prove multiplicity eight. The exact next interface remains `QFORM-S8-TWOHIGH-FOURCOORD-CORE-SCHUR-ENDPOINT-v1`.
