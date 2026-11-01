from pathlib import Path
p=Path('SECOND_ATTEMPT.md')
p.write_text('''# C0100: second serious attempt (2026-10-12)

## Gap reread and two untried approaches

The first attempt's main point-source gap is isolated-maximal Hessian membership almost everywhere at intermediate limiting density. It also leaves the standard wired-square identity limit unidentified. The previous periodic-patch and two-scale arguments do not settle either gap.

**Approach A: the identity as an integer Dirichlet problem.** Prove the exact finite identity equals the Laplacian of the pointwise least integer function v with Delta v<=3 inside and v=0 outside. Then use the general integer-superharmonic continuum comparison mechanism (or its viscosity Dirichlet problem) at cutoff 3, without shifting to the all-ones recurrent class. This may establish a weak-* identity limit or a precise reduction to an existing Dirichlet convergence theorem without proving any patch geometry. The first attempt inspected the ellipse special case but did not pursue this general boundary-value route.

**Approach B: fixed-Hessian microstructure rigidity or counterexamples.** Seek two integer quadratic-plus-periodic locally recurrent functions with the SAME Hessian and different height histograms. The old recurrent checkerboard obstruction had only the same mean, not the same Hessian. A fixed-Hessian counterexample would refute a broad replacement for the isolated-maximal-Hessian hypothesis; conversely a rigidity theorem might identify frequencies on non-maximal Hessians and remove that gap. A concrete bounded search can enumerate periodic corrections and test forbidden subconfigurations, rather than simulating further point-source sizes.

I pursue A first because it addresses an actual requested family and exposes a precise distinction between the zero-class and all-ones-class boundary problems. B remains a secondary explicit construction search if A stalls.

## Brain query

Read-only math_recall.py on "sandpile isolated maximal Hessian Gamma positive density Pegden Smart pattern stability" returned the same older conditional patch argument, plus the LPS structure references. It did not provide a result establishing the gap. A second query targets "sandpile identity least integer Dirichlet recurrent representative Melchionna Pegden Smart". Brain suggestions are not treated as proofs.
''',encoding='utf8')
