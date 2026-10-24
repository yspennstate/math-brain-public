# account04/B20 handoff — fixed-multiplicity audit

Run: \`20260924T132150Z-account04-B20-fixedmult-audit-r1\`

The later owner directive \`QFORM-FIXED-MULTIPLICITY-AUDIT-20260924\` superseded the historical three-eigenvalue task. I independently audited the pinned 790-line manuscript at blob \`183ccd294763214e6a707e8d4749ff9a8cf7006d\`, SHA-256 \`9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69\`.

Verdict: PASS for the fixed-multiplicity theorem. No post-rotation independence, arbitrary-joint coarea, or unproved conditional-density cap is used. The current reproducibility files are present and pin the same source.

New certified improvement:
\[
s_{17}(A)\ge s
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty<4340\,K^2/s.
\]
The bottleneck is the indefinite-pair truncated half-potential \(<433\); the nine-direction full half-potential is \(<434\), so the scalar-pivot branch is \(<4340\). Detailed rational certificates and the determinant-method barrier witness are in math-open-problems commit \`6b11fd000e12a6c279d736781d3f886e43a487fd\`. The clean proof assembly is commit \`d2cfe6dfcc06e070f9b40a8e099a9354d80cfc52\`.

The unrestricted three-eigenvalue conjecture remains open. Do not infer it from the fixed-multiplicity theorem.
