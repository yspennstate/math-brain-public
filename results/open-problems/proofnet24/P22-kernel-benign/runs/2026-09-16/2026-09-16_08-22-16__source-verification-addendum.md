# ProofNet24 P22 — source-verification addendum for 2026-09-16 08:22:16 run

This immutable addendum strengthens, and does not alter, the mathematical report

`proofnet24/P22-kernel-benign/runs/2026-09-16/2026-09-16_08-22-16__run-report.md`

created at commit

`b9e261d6171135d59526731d36b324b57a08aab3`,

blob

`8dfbfe42df47a11ed7f3c13ded0958317ace01a3`.

The report conservatively recorded `PRIMARY_PAGE_NOT_LINE_INSPECTED` for the historical Gross/Nelson Gaussian hypercontractivity source because an authoritative scan had not yet been located at archive time. Immediately after exact-SHA report readback, a scan mirror of Leonard Gross's original 1975 paper was located and inspected.

## Source inspected

Leonard Gross, **Logarithmic Sobolev Inequalities**, *American Journal of Mathematics* 97(4) (1975), 1061–1083. The inspected scan reproduces the original journal pages and JSTOR footer.

Accessible scan mirror used for inspection:

`https://studylib.net/doc/27852139/gross-1975`

## Exact theorem statement checked

On original printed page 1073, Gross's Corollary 4.1, explicitly attributed there to Nelson [13, Theorem 3], states the Gaussian number-operator hypercontractive bound in the following parameterization: for `1<q,p<infinity`, if

\[
e^{-t}\le \left(\frac{q-1}{p-1}\right)^{1/2},
\]

then

\[
\|e^{-tN}\|_{L^q(v)\to L^p(v)}\le1,
\]

where `v` is Gaussian measure and `N` is the Gaussian number operator constructed in the preceding theorem. The surrounding proof identifies

\[
p(t,q)=1+(q-1)e^{2t}.
\]

Taking source-input exponent `q=2` and target exponent `p=r>=2` gives exactly

\[
e^{2t}\ge r-1
\quad\Longrightarrow\quad
\|e^{-tN}F\|_r\le\|F\|_2.
\]

For a homogeneous Gaussian chaos of degree `s`, `e^{-tN}H_s=e^{-st}H_s`, so

\[
\|H_s\|_r\le(r-1)^{s/2}\|H_s\|_2.
\]

The radial separation argument in the canonical report then gives the dimension-free spherical harmonic inequality

\[
\boxed{
\|Y_s\|_r\le(r-1)^{s/2}\|Y_s\|_2,
\qquad r\ge2.
}
\]

Thus the exact constant, exponent range, Gaussian-measure hypothesis, and dimension-free uniformity imported by the P22 growing-degree argument are now directly checked against the original Gross paper's displayed corollary. No mathematical claim in the canonical run report changes; this addendum removes only its conservative source-access qualification.

No email/Gmail action was used.