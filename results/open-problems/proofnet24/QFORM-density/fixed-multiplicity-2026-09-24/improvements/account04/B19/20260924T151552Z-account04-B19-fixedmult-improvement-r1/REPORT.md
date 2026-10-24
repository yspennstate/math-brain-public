# QFORM fixed-multiplicity improvement — account04/B19

Run: 20260924T151552Z-account04-B19-fixedmult-improvement-r1

Status: **ESSENTIAL_STEP_APPLIED**. This sharpens the constant in the independently reviewed nine-singular-value theorem. It does **not** solve the unrestricted three-eigenvalue conjecture.

## Source pins and scope

Baseline manuscript: commit 7c0d6e60946b19423e6400a12d34b473cf0591e2, blob 183ccd294763214e6a707e8d4749ff9a8cf7006d. The reviewed s9 compiler/source reconstruction is at commits 8ff490c177d0cd7d6f33130f1431785e312a9d10 and 18c0707d32a6b405f159f690f17a8df5365b2755; independent end-to-end PASS is account01/B16 commit 54ec2a651d854563f8db0d92c4c3426f76551786; independent audit is account03/B14 commit 9861ed55f7865b2a67346a66bc178eb7f81df190; the previous exact sharpening to 2514 is account04/B08 commit 91ed97a2444a27a5acb1d166a099be8d0c54b785.

The proof architecture and branch hypotheses are unchanged. Only the scalar-pivot constant is sharpened. Therefore, for independent real coordinates with densities bounded by \(K\), arbitrary \(A=A^\top,b,c\),

\[
s_9(A)\ge s>0
\Longrightarrow
\operatorname*{ess\,sup}_t p_{X^\top A X+b^\top X+c}(t)
<\frac{2510K^2}{s}.
\]

## Exact certificate

The audited scalar branch uses
\[
C_q=2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8).
\]
The exact-rational verifier proves \(\Gamma(3/8)<2371/1000\). On \([0,1]\) it integrates the degree-ten even alternating Taylor upper bound for \(e^{-x}\). On each length-\(1/128\) interval \([a,b]\subset[1,8]\), a verified rational \(u_a\ge a^{-5/8}\) gives
\[
\int_a^b x^{-5/8}e^{-x}\,dx
\le u_a\left(\frac1{L_{45}(a)}-\frac1{U_{45}(b)}\right),
\]
where
\[
L_{45}(x)=\sum_{k=0}^{45}\frac{x^k}{k!},\qquad
U_{45}(x)=L_{45}(x)+\frac{x^{46}/46!}{1-x/47}.
\]
The tail is at most \(u_8/L_{45}(8)\). The exact sum is \(2.37085691971757\ldots<2.371\).

Machin's identity and alternating arctangent bounds certify \(3.14159<\pi<355/113\). Positive Taylor bounds and power comparisons certify
\[
2^{5/8}<\frac{15423}{10000},\quad
\pi^{-1/4}<\frac{75113}{100000},\quad
e^{3/8}<\frac{291}{200}.
\]
Thus
\[
C_q<3.996488005329195\ldots<\frac{399649}{100000}.
\]

## Scalar-pivot ledger

The reviewed proof gives
\[
L_{\log}<4+4\log C_q,\qquad
H_{\mathrm{sc,tr}}<10[\pi+4\log2+2L_{\log}].
\]
Exact positive Taylor sums prove
\[
\log2<\frac{173287}{250000},\qquad
\log C_q<\frac{69271}{50000}.
\]
Therefore
\[
10(H_{\mathrm{sc,tr}}+1)<2509.754492035398\ldots<2510.
\]
The inner \(+1\) is the full-potential tail; the outer 10 is \(\eta^{-1/2}\) for \(\eta=10^{-2}\). The other reviewed branches stay below 2371, 32, and 251, so the scalar branch remains maximal.

This is a constant improvement at the proved \(s_9\) threshold. It neither lowers the threshold to three nor pays the shared-bank hybrid/convex-side endpoint. No independence after rotation or extra law hypothesis is used.
