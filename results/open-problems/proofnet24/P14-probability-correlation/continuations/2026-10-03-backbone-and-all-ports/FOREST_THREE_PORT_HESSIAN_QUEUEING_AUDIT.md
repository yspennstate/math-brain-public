# Independent analytic audit of the three-port Hessian lemma

3 October 2026. I read `forest_three_port_hessian_lemma_k_proof.md` in full
and rederived its matrix and scalar bounds. Verdict: PASS, conditional only
on the explicitly credited and primary-source-checked ordinary coefficient-
one matroid log-concavity theorem. No stronger correlation result is assumed.

Adding the distinguished triangle gives exactly
`Z=F+A^T z+r(z12 z13+z12 z23+z13 z23)`: any two new edges can be added iff
all three ports were initially separate, and all three always make a cycle.
Thus the logarithmic Hessian at zero is
`rK/F-AA^T/F^2`, with `K=11^T-I`. Continuity from positive new-edge activities
is legitimate because F>0. Ordinary matroid log-concavity therefore gives
`C=AA^T-rF K` positive semidefinite.

For the strict quantitative bound, the homogeneous polynomial has degree N.
At the stated boundary point a, let `S=-Hess log g>=0`. Differentiated
Euler gives `Sa=grad log g` and `a^T S a=N`. A vector h supported only
on the three new coordinates satisfies `h^T S a=A^T x/F` and
`h^T S h=x^T Cx/F^2`. Semidefinite Cauchy-Schwarz yields
`x^T Cx>=(A^T x)^2/N`, exactly the claimed degree-sharpened matrix bound.
Neither singularity nor zero coordinates cause a division by zero, because
N>=3 and F>0. The asserted positive definiteness for r>0 follows: a kernel
vector has `A^T x=0`, then `Kx=0`, while K is invertible in dimension three.

Taking `x=(b1b2,b1b3,b2b3)` gives `A^T x=M` and
`x^T Kx=2B b1b2b3`; hence `M^2-2BJF>=M^2/N`. The elementary all-separated
partition contribution gives `BM>=9J` independently. Both are exactly the
gates used by the full arbitrary-backbone matching proof.

Required-present conditioning is correctly reduced to graphic deletion/
contraction after removing its positive common activity factor. Identified
ports produce r=0 and loops/parallel distinguished edges; the literal
triangle polynomial and the Hessian remain correct. Restoring the common
factor scales the matrix bounds quadratically. Fields change the permitted
activities only. The proof does not infer entrywise nonnegativity of C and
does not establish the general adjacent-edge Rayleigh conjecture.

The formal row `(1,0,0,0,1)` has `F=2,M=3,J=1,B=3` and violates the scalar
bound by -3. It is correctly labeled an unrealizable abstract boundary row,
not a counterexample to any weighted-forest theorem. The exact-check record
is supplementary; the verdict above follows from the analytic derivation.
