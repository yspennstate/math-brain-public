# account04/B08 fixed-multiplicity handoff

Run: \`20260924T141600Z-account04-B08-fixedmult-improvement-r1\`

Owner objective: \`QFORM-FIXED-MULTIPLICITY-AUDIT-20260924\`.

## Result

Using the independently reviewed \(s_9\) proof compiler, I sharpened the density constant from \(2582\) to

\[
s_9(A)\ge s>0
\Longrightarrow
\operatorname*{ess\,sup}_t p_{X^\top AX+b^\top X+c}(t)
<
2514K^2/s.
\]

The improvement is an exact rational certificate for

\[
C_q=2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8)<4.01.
\]

It yields scalar-pivot constant \(<2513.886\); the no-pivot, definite, and indefinite branches remain \(<2371,<32,<251\).

## Source pin

- mathematics report commit: \`91ed97a2444a27a5acb1d166a099be8d0c54b785\`;
- exact checker commit: \`2d918eb65ca00be4d573e0a2f9635609cd879090\`;
- report path: \`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account04/B08/20260924T141600Z-account04-B08-fixedmult-improvement-r1/REPORT.md\`;
- checker path: same directory, \`verify.py\`.

The nine-eigenvalue structural proof has independent PASS reviews at commits \`54ec2a651d854563f8db0d92c4c3426f76551786\` and \`9861ed55f7865b2a67346a66bc178eb7f81df190\`.

## Boundary

This is a fixed-multiplicity \(s_9\) theorem. The unrestricted \(s_3\) conjecture remains open.
