# account04/B19 fixed-multiplicity proof assembly

Run: \`20260924T132050Z-account04-B19-fixedmult-audit-r1\`

## Canonical source

- Manuscript blob: \`183ccd294763214e6a707e8d4749ff9a8cf7006d\`
- SHA-256: \`9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69\`
- Independent detailed audit and arithmetic certificate: commit \`6b11fd000e12a6c279d736781d3f886e43a487fd\`

## Verdict

The complete fixed-multiplicity theorem passes this independent end-to-end review. With no change to its hypotheses, the proof gives the stronger bound
\[
\boxed{\|p_{X^TAX+b^TX+c}\|_\infty<4340\,K^2/s}
\qquad\text{when }s_{17}(A)\ge s>0.
\]
The unrestricted three-eigenvalue conjecture is not proved.

## Noncircular proof graph

1. Original-coordinate decoupling plus geometric Brascamp--Lieb gives
   \[
   |\phi_Z(t)|\le
   \det\!\left(I+\frac{t^2M^TM}{\pi^2e^2}\right)^{-1/8}.
   \]
2. Cauchy--Binet converts the determinant to crossing volumes \(Z_k(M)\).
3. \(k=5\) yields bounded density; \(k=3\) yields the negative-half-moment receiver.
4. Disjoint-minor sampling and the two interpolation ranks \(3r\) globally and \(r\) outside the seed convert \(s_{17}\) into the required order-five crossing unless a physical pivot exists.
5. No pivot gives density below \(2400\).
6. A scalar pivot reduces to a nine-direction full half-potential. The refined pivot ledger gives truncated half-potential below \(433\), hence full half-potential below \(434\), and therefore density below \(4340\).
7. Definite and indefinite two-coordinate pivots give density below \(40\) and \(199\), respectively.
8. The rescaling \(Y=KX\) restores the factor \(K^2/s\).

Every probabilistic step remains in original coordinates. Conditional square and hyperbolic estimates are measure-domination formulas used through Tonelli, not post-rotation independence or worst conditional-density assertions.

## Exact constant ledger

The quarter-power coefficient satisfies
\[
2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8)<365/64,
\]
so \(L_0<11\). Keeping the exact far-region coefficient in the kernel bound gives
\[
J(d)\le8+2\sqrt2\log_+(1/|d|).
\]
Thus the scalar-pivot truncated half-potential is below \(410\). The indefinite-pair branch is the bottleneck:
\[
10(32+4\log16)+4/e
<54049/125
<433.
\]
The detailed report contains rational Taylor certificates for both logarithmic inequalities.

## Limitation witness

For \(M=\operatorname{diag}(\sigma_1,\ldots,\sigma_k)\), the determinant receiver factors exactly, and retaining its top coefficient gives the exponent \(k/4\). At \(k=4\) this is only \(|t|^{-1}\), so the present unweighted Fourier endpoint alone cannot lower the unconditional multiplicity threshold.
