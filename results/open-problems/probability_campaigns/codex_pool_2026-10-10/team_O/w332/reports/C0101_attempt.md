# C0101: integer witnesses and a rounding counterexample, 2026-10-10

Status: the d>=3 maximal-element classification remains unresolved in the inspected ledger. The earlier attempt leaves its Laplacian threshold as "the constant ..." and has no d>=3 packing correspondence. I use an explicit threshold K in the lemma below so that no sandpile normalization is guessed.

Lemma: for an integer symmetric d-by-d matrix A, define

g_A(x)=sum_i A_ii*x_i*(x_i-1)/2 + sum_(i<j) A_ij*x_i*x_j, x in Z^d.

This function is integer valued because every product x_i(x_i-1) is even. It differs from x^T A x/2 by the linear function -sum_i A_ii x_i/2. For the unnormalized nearest-neighbor Laplacian Delta g=sum_i (g(x+e_i)+g(x-e_i)-2g(x)), direct second differences give Delta g_A=tr(A) exactly. Thus it is an exact integer-valued quadratic-growth witness for any requirement Delta g<=K whenever tr(A)<=K. This construction works in every d, including d>=3, and avoids rounding error. It is a sufficient membership construction after matching the source's threshold and growth convention; it asserts no maximality among general witnesses.

The prior attempt states that Delta ceil(a*x^2/2) is at most a+1. Counterexample: a=1/2, x=0. The three values are g(-1)=1, g(0)=0, g(1)=1, so Delta g(0)=2>3/2=a+1. The always valid elementary estimate is Delta ceil(a*x^2/2)<a+2, since the rounding error e(x) lies in [0,1) and its second difference is less than 2. Replacing the erroneous estimate matters when a Laplacian budget is being allocated across coordinates.

The cached Levine-Peres text at lines 1006-1009 defines Gamma(Z^d) as the closure of Hessians whose associated sandpile stabilizes locally. Thus the polynomial witness lemma above does not automatically identify membership or maximality in the source's Gamma: its connection to the specified sandpile and growth convention remains to be proved. A packing-integrality analogy proves no Gamma classification without the missing correspondence. In general dimensions the Descartes reflection has coefficient 2/(d-1) on the sum of the other curvatures, so a claim that integer starting curvatures always preserve integrality in all d also needs a divisibility check. In d=3 that coefficient is 1; this arithmetic fact alone does not identify the integer-superharmonic matrices.

Checks: check_extended.py evaluates the integer polynomial and Laplacian for random symmetric integer matrices in d=3,4,5 on an integer grid, and reproduces the explicit rounding violation with exact fractions. Auditor w346, pending.
