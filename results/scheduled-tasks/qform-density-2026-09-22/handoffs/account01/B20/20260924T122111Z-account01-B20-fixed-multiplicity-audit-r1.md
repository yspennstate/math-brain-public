# account01/B20 handoff — fixed multiplicity audit / s16 endpoint

Run: `20260924T122111Z-account01-B20-fixed-multiplicity-audit-r1`

Current owner objective acknowledged: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`, which supersedes the older unstructured full-three-eigenvalue focus for this invocation.

Pinned manuscript source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Independent release-gate audit

The complete 790-line manuscript was reconstructed end-to-end. Verdict: **PASS for the mathematical 17-eigenvalue theorem** with no fatal gap found. The theorem retained is exactly arbitrary independent real coordinate densities `<=K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_17(A)>=s>0`, implying `||p||_infty<=10000 K^2/s`.

Nonfatal issues:

- packaging GAP: root `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json` advertised by README were absent on fresh master;
- presentation GAP: choose global pointwise-bounded Borel representatives of rough marginal densities;
- projection-lemma wording: after dropping `b_i=0`, use `sum_{b_i>0}(1-b_i)<=d` (or keep the all-row equality).

Immutable audit: `math-open-problems@05f25d3d57d44f4caf3b630cb5b59e22073e91e7`, path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account01/B20/20260924T122111Z-account01-B20-fixed-multiplicity-audit-r1/AUDIT.md`.

## New threshold-support lemma

Proved `QFORM-S16-ORDER4-PLUS-SECOND-PHYSICAL-CROSSING-v1`.

Assume no `eta=1/100` pivot and `s_16(A)>=1`, with `kappa=1/6400`. Either `V_5(A)>=kappa^5` (already paid by the manuscript's order-five Fourier receiver), or there is a literal physical cut `I|J`, `M=A[I,J]`, such that

- `Z_4(M)>=kappa^4/1280`;
- `Z_5(M)/Z_4(M)<=5 kappa/16`;
- `dist_F(M,rank<=4)<=1/64`;
- with `B=A[I,I]`, `C=A[J,J]`, `s_8(B direct-sum C)>=63/64`;
- consequently one same-bank block has at least four singular values `>=63/64` and contains a second literal internal physical crossing `N` with `||N||>=1559/3200`.

Core identity: for `x_j=s_j(M)^2`,

`5 e_5(x)=sum_{|S|=4} x_S sum_{j notin S} x_j >= e_4(x) sum_{j>=5} x_j`.

Weighted random-cut selection uses `E Z_5 / E Z_4=(1/4)V_5/V_4<kappa/4` and threshold `5kappa/16`, retaining more than one fifth of total `Z_4` weight. This gives the exact `1/64` rank-four tail after Eckart--Young. Removing that tail costs `1/64` in operator norm; the remaining off-diagonal rank-four carrier has symmetric rank at most eight, forcing `s_8(B⊕C)>=63/64` from `s_16(A)>=1`.

Immutable proof: `math-open-problems@5d252a5b450c02b7b720a7e3b2fefa6c852bb2c7`, path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account01/B20/20260924T122111Z-account01-B20-fixed-multiplicity-audit-r1/S16_ENDPOINT.md`.

This does **not** prove the 16-eigenvalue theorem. The remaining exact obstruction is transversality/alignment: the second physical crossing may align with the four-dimensional carrier of the order-four cut after physical repartition. A valid `17 -> 16` proof needs either a physical paving that preserves quantitative `Z_4` while adding a fifth exterior direction, or a direct endpoint receiver for this rank-four-plus-second-crossing geometry.

The unrestricted three-eigenvalue conjecture remains OPEN. Continuity remains separate; the no-pivot order-five branch is continuous.

Execution: `WITHOUT_VERIFIED_BRAIN`; repository transport only, no authenticated receiver ingestion claimed.