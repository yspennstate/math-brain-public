VERDICT: PROVED invertibility and local critical-branch continuation of the disordered Fredholm formulas for all -1 < Delta < 1

This is an analytic lemma about the candidate formulas, not a proof of T133.
The earlier worker reported a theorem announcement and supplied no original
proof or computation. The new result, proved in [PROOF.md](PROOF.md), checks
one possible obstruction in the announcement's omitted interval
$1/2<\Delta<1$.

With $\gamma=\arccos\Delta$, the disordered integral operator satisfies

\[
\|K_B\|_{L^2\to L^2}\le |1-2\gamma/\pi|<1
\]

for every $B>0$. Its Fredholm determinant is positive, and the rank-one
determinant quotient is a linear resolvent integral. Thus these formulas
remain well defined throughout the omitted interval.

At every interior parameter of the proposed southwest boundary arc, its
envelope determinant is strictly positive. Consequently, for each
sufficiently small $B>0$ and fixed boundary parameter $\theta$, the two
critical equations determine a unique real pair $(x(B,\theta),y(B,\theta))$
that extends analytically to the envelope at $B=0$. An explicit quadratic
displacement is derived; its constants are checked by a second moment
argument and an exact free-fermion calculation. Where the stated curvature
quantity $C$ is nonzero, the critical point is a nondegenerate saddle.
This does not assert uniqueness of $(B,\theta)$ for a prescribed $(x,y)$.

The source definitions are from Alexey Bufetov,
[*Limit shape for domain-wall six-vertex model*, arXiv:2609.20576v1](https://arxiv.org/html/2609.20576v1).
The bounded literature check found no later version or complete proof.
The earlier report's description of the announcement survives direct
comparison with the abstract page, HTML and PDF. The new proof does not
assume its announced limit-shape theorems. No claim of literature priority
is made for these operator facts.

Reproduce the numerical audit with:

~~~sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_local.py
~~~

The script requires NumPy and mpmath. Detailed output is in
[verification.json](verification.json); commands and material outputs are
recorded in [LOG.md](LOG.md). All 19 numerical checks passed: five kernel
mass checks, three scalar-determinant versus resolvent comparisons, eight
local-branch checks, and three exact free-fermion checks. The latter agree
within $2.70\times10^{-10}$. Branch checks include unequal weights, both
kernel signs, and parameters near $\Delta=\pm1$. Final runtime was
0.61 seconds with peak RSS 33.8 MiB, one thread configured, and effective
nice 20.

What failed: the first numerical run emitted warnings from unused
meromorphic evaluations and BLAS-backed operations. The unused evaluations
were removed; explicit sums and a separate scalar determinant routine
replaced the flagged operations. The final run treats runtime warnings as
errors and passes. A Markdown delimiter error was also repaired and audited.
The shell cannot set nice 15 because its inherited priority is already 20.

What remains uncertain: no full proof behind the announcement was located;
the search cannot establish its absence. The local analytic branch has not
been proved to lie on the physical liquid side. Global critical-point
existence and uniqueness, the sign or possible vanishing of $C$, endpoint
control, and identification with the model's height limit remain unproved
here. The estimates are not uniform as $\Delta\to\pm1$. No antiferroelectric
extension was attempted.

Next worker: prove the sign of
$C(\theta)=x_0a''+y_0b''-e''$ on the southwest arc for
$0<\gamma<\pi/3$, then use the explicit quadratic displacement to determine
whether the local branch enters the proposed liquid region. This is a
smaller checkable target than global uniqueness or a probabilistic
limit-shape proof. Continue to distinguish analytic candidate formulas
from convergence of the six-vertex model.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, 01:33 Asia/Tbilisi.
