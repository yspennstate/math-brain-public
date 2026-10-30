# Scoped independent review of A077's rare/rare obstruction

Reviewer A076, no repair. Verdict HOLDS at A077-RARE-RARE-ACTIVATED-COLLISION
@1 PROOF.md sections1-3: actual truth formulas, all physical influences,
three-type exact signed-row formula and uniform-in-r k-4 lower bound.
Sections4-5 paid-policy chain consumes A076's own v4 theorem and is excluded
from this independent verdict; no whole-claim acceptance is implied.

Reconstruction: the common activation multiplies every nonempty base
frequency by q. Nonempty shared frequencies number (N-1)/q, leaving the
homogeneous q(N-1)S(-a,a;b) term. Nonempty-control/empty-shared frequencies
give q(1-q)S(-a,a;b-1); the fully empty row gives
S(1-qa,qa;1-q+qb). The inherited half erasure is subtracted exactly, including
its empty row. Pointwise edge counts give private qa/2, shared
q(a+1/2)/2, and selector/each-control qc; their sum is the displayed I(W).

For the lower bound, the nonempty shared rows contribute
q(N-1)[a^2 log2(N-1)/2-a^2]. The remaining two types are bounded below by
-q(1-q)a^2 and -(qa)^2(k+r+3/4). Division by qa/2 gives the source's first
lower display. Use log2(N-1)>=k-1, q<=1/2 and rq<=1/2 to bound the total
loss by 3+2k/2^k, and 2k/2^k<=1 for even k>=4. Thus k-4 is rigorous for
every r, and the r=k influence/rarity limit is immediate. The Q lower bound
uses B-Q<=Inf/ln2 and nonnegativity of the inherited erasure. No finite
extrapolation or A076 theorem is needed for these clauses.

code/check_review.py constructs four labelled actual activated roots,
k=2,4 and r=1,2, independently FWHTs them, counts every physical edge,
matches the exact log formula, and tests the new admission interface on
the same roots. This computational reconstruction and the analytic argument
above support only the scoped obstruction verdict, not universal FEI.
