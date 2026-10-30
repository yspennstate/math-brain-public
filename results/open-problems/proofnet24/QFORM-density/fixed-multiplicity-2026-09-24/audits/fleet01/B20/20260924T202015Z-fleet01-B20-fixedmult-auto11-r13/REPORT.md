# fleet01/B20 fixed-multiplicity audit

Run: 20260924T202015Z-fleet01-B20-fixedmult-auto11-r13

## Exact source ledger

Baseline manuscript blob 183ccd294763214e6a707e8d4749ff9a8cf7006d:
- lines 1-471: PASS
- lines 472-475: GAP_REPAIRABLE_LOCAL
- lines 476-790: PASS after the local repair
- FALSE: none found
- UNCHECKED here: fresh execution of finite checker, PDF rebuild, formal verification, exhaustive novelty search.

The local repair is in the negative hyperbolic tail: choose the maximizing original coordinate for the negative exponential vector independently from the coordinate chosen for the positive tail. The two vectors have equal Euclidean norm, so the cutoff and constants are unchanged.

Current nine-value source commit eeb752c8943536541b34b42b8bf48e924f4d3d2f, blob 19fb119877426b640b2c0dae19ec2f78a399fe11:
- lines 1-597: PASS
- lines 598-600: GAP_REPAIRABLE_LOCAL, same repair
- lines 601-955: PASS after repair
- FALSE: none found.

## Threshold accounting

A complete multiplicity-eight replacement proof is present at blob 8f792f8f80d70fd1eda26dfdabd855b9a6235e29. Two separate complete reviews are present at blobs f7ac28a10e99a7dac1b343ee5b86c0a25cdc1951 and ab46124605dc2795c2fd65bbc62a0b97e9894b9b. These support the safe theorem
[
s_8(A)ge s>0implies |p_Q|_{infty,mathrm{ess}}<2400K^2/s.
]
This is mathematical review evidence, not formal verification, journal review, or an owner release flag.

The five-value directory has two PASS audit summaries but its advertised 1,093-line main.tex is absent from the current Git tree. Therefore the five-value density theorem is source-level UNCHECKED/PACKAGING-GAP in this run, not false. Multiplicity four and three density remain OPEN.

## New supporting theorem: two-hub real-space receiver

Let U=(U1,U2) and Y be disjoint original-coordinate blocks with all scalar densities bounded by K. Let C be a real 2 by m row-rank-two matrix, q in R^2, and F(Y) arbitrary measurable. If
[
Q=2U^TCY+q^TU+F(Y),qquad g=det(CC^T)>0,
]
then
[
oxed{|p_Q|_inftyle esqrtpi,K^2g^{-1/4}.}
]

Proof: condition on Y=y. The cap-K product-projection theorem gives conditional density at most (sqrt e K/|2Cy+q|_2). The random vector (2CY+q) has an R^2 density bounded by (M=eK^2/(4sqrt g)). For every probability density h on R^2 with h<=M, radial rearrangement gives
[
int h(v)|v|^{-1}dvle2sqrt{pi M}.
]
Combining yields the displayed bound. No moments, bounded support, iid assumption, smoothness, log-concavity, or rotated independence are used.

For two independent zero-hub star blocks
[
A_r=egin{pmatrix}0&a_r^T\a_r&B_rend{pmatrix},
]
with arbitrary symmetric leaf blocks B_r and arbitrary affine terms, an L2 convolution argument gives the sharper
[
|p_Q|_inftyle {4sqrt e,K^2oversqrt{|a_1|_2|a_2|_2}}.
]
Thus the exact four-eigenvalue two-star obstruction is paid even with arbitrary same-leaf quadratic curvature and affine terms. The unresolved s4 endpoint requires genuinely nonzero hub-principal curvature and/or coupling between the star banks. No s4 theorem is claimed.

Status: supporting theorem proved; s4, s3 bounded density, and unrestricted three-eigenvalue conjecture remain OPEN.
