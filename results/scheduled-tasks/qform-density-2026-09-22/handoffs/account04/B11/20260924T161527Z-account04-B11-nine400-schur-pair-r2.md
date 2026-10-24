# account04/B11 handoff — nine-eigenvalue audit and constant 385

- Objective: \`QFORM-FIXED-MULTIPLICITY-AUDIT-20260924\`
- Run: \`20260924T161527Z-account04-B11-nine400-schur-pair-r2\`
- Source commit: \`eeb752c8943536541b34b42b8bf48e924f4d3d2f\`
- Source blob: \`19fb119877426b640b2c0dae19ec2f78a399fe11\`
- Owner-recorded source SHA-256: \`bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3\`

## Result

A complete independent reconstruction of all 955 source lines found no fatal mathematical gap. The nine-eigenvalue theorem with arbitrary signs, affine terms, remaining spectrum, and rough cap-\(K\) product laws passes.

The B11 checks reconfirm:
\[
N_S(t)\ge N_A(t)-k,\qquad s_j(S)\ge s_{j+k}(A)
\]
for an invertible \(k\)-pivot, including singular ambient matrices; and the full hyperbolic pair half-potential has the correct \(D^{-1/4}\) scaling.

The final numerical closure sharpens from 400 to 385:
\[
200+80\log10+\frac1e
<200+\frac{923}{5}+\frac38
=\frac{15399}{40}<385.
\]
Here \(\log10<923/400\) is certified by the positive seventh exponential Taylor partial sum, and \(1/e<3/8\).

## Published records

- Full audit commit: \`f381205787986693f2b25caf78dc434ab6a1a568\`
- Constant-385 proof commit: \`582b941e4fc5270d3b5cc2da4675888929288ade\`

## Guardrails / next obligation

This is one complete independent audit, not two. The theorem remains at \(s_9(A)\ge s\); the overlap identity does not itself prove the \(s_8\) density theorem. The next genuine obligation is a product-preserving analytic receiver for the shared-coordinate overlap term. The unrestricted three-eigenvalue conjecture and continuity remain open.
