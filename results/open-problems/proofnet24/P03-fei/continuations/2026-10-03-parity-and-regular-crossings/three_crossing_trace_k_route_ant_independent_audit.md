# Independent audit: trace-K route, exact obstructions, finite coverage and status

2 October 2026. Auditor: `/root/antivoter_audit`.

**PASS as a route checkpoint, with the actual retained-middle trace
inequality still UNPROVED.** I read the entire
`three_crossing_trace_k_route_checkpoint.md`, its actual obstruction
script and complete JSON, the original trace and component candidates,
and the full `exhaustive_small_weights_three_crossing.py`/JSON. I
independently checked both explicit same-score realizations, all endpoint
and influence factors, the asymptotic divergence, the TP2 minor, and
the exhaustive loop coverage. A new checker imports no author modules.
No counterexample to the actual-middle-crossing candidate was found.

## 1. Physical normalization and exact equivalent inequality

For a Boolean H, each undirected pivotal cube edge has two endpoints.
Thus \(K=E\Gamma_H=I(H)\) and
\(\nu_H(x)=\Gamma_H(x)/(2^nK)\) are exactly the influence and the
uniform-pivotal-edge/uniform-endpoint law. The density is not an
edge law with only one endpoint or a probability normalized by half K.

For consecutive regions (E_0,E_1,E_2,E_3\) with labels (+,-,+,-\),
let the physical fluxes be
\(x=e_{02},y=e_{13},o=e_{03}+e_{12},t=e_{01}+e_{23}\).
The middle halfspace crosses precisely those x,y,o edges. Its f-signed
endpoint sum is x-y, and f flips precisely on o,t. Therefore

\[
K=x+y+o,\quad I(f)=o+t,\quad
K\operatorname{Var}_{\nu_H}(f)=K-\frac{(x-y)^2}{K}.
\]

The inequality \(K\operatorname{Var}_{\nu_H}(f)\le2I(f)\)
is exactly equivalent, after expanding and multiplying by K, to

\[
4xy\le o^2+2t(x+y+o).
\]

The lower bound by (2\min(x,y)\) is correct: for (x\le y\), its
numerator remainder is (2x(y-x)+2yo+o^2\ge0\).
The component influence sums are (I(f)+2x\) and (I(f)+2y\).
Thus the still-missing trace bound would imply component constant three.
The exact five-weight witness ((2,2,2,2,3)\), cuts ((-2,0,2)\), has
physical fluxes

\[
(e_{01},e_{02},e_{03},e_{12},e_{13},e_{23})
=(1/2,3/4,3/8,0,3/4,1/2).
\]

It gives trace ratio (15/11\) but component ratio (23/11>2\).
The witness invalidates component constant two, not trace constant two.
I independently counted the direct cube edges and the signed pivotal
endpoints, rather than simply plugging its reported fluxes into a formula.

## 2. Dirichlet/Gram reduction

The normalization (L=\tfrac12\sum_i(\mathrm{Id}-\mathrm{flip}_i)\)
gives \(LH=H\Gamma_H\) for Boolean H and
\(E(uLv)=\sum_iE(D_i uD_i v)\). Positive halfspace derivatives are
zero-one slab indicators, with interval width (2w_i\) in the rest score.
For nested cuts a<b<c, the identities

\[
f=-H_a+H_b-H_c,\qquad H_bf=H_a-H_c-1
\]

hold on all four regions. Taking the Dirichlet products proves the
reported I(f) formula and
\(K E_{\nu_H}f=E(H_a,H_b)-E(H_b,H_c)\).
Three equal-length ordered derivative intervals cannot have pattern 101;
all the other listed patterns are possible. These correct facts do not
by themselves supply the four-flux inequality.

The abstract monotone-majority/dictator region example is properly
excluded from the common-additive-score setting. With N=2d+1 and L the
sum of the largest d positive majority weights, consecutive separation
would require the independent dictator weight to be both larger than L
and smaller than S-2L. But (S\le(2d+1)L/d\) implies (S-2L\le L\).
This contradiction checks even when unequal positive weights are allowed.
Thus monotonicity of a region index is strictly less than the required
score geometry, and this abstract obstruction is not an actual retained-
middle counterexample.

## 3. Genuine two-crossing slab and its non-crossing trace threshold

The checkpoint's new construction is an actual common positive score,
not an abstract region map. For k coarse signs, odd N fine signs,
\(A=2N+1\), let

\[
Y=\sum_{j=1}^k2^{j-1}y_j,\quad T=\sum_{i=1}^Nx_i,
\quad S=AY+T,\quad p=2^{-k}.
\]

Y takes every indicated odd integer exactly once. Its unique value one
occurs at \(c^*=(-1,\ldots,-1,+1)\). Since (A>N\), the open slab
((0,2A)\) contains exactly that coarse fiber. Hence

\[
g=1-2\mathbf1_{\{y=c^*\}},\qquad I(g)=2kp.
\]

There are exactly two retained crossings, at 0 and 2A. Neither endpoint
is attained. The halfspace (H=\operatorname{sign}(S-A)\) has its
threshold inside the negative slab, where g DOES NOT cross. Within the
fiber it is majority; outside it equals the top coarse dictator:

\[
H=y_k-2\mathbf1_{\{y=c^*,\ T<0\}}.
\]

S-A cannot vanish: S is even whereas A is odd. This verifies the full
realization and explains exactly why this example is outside the actual-
middle retained-crossing candidate.

Monotonicity makes each halfspace influence its Chow coefficient. The
coarse coefficients sum to (1+(k-2)p\), and the fine coefficients sum
to (pM_N\), where

\[
M_N=E|T|=N\binom{N-1}{(N-1)/2}/2^{N-1}.
\]

At the fiber, the fine pivotal expectation is M_N. The coarse pivotal
count is k-1 when T<0 and one when T>0. Therefore

\[
K=1+(k-2)p+pM_N,\quad
M:=E[\Gamma_Hg]=1-2p-pM_N,
\]
\[
K-M=kp+2pM_N,\qquad K+M=2+(k-4)p.
\]

All signs and endpoint factors check. The independent script enumerates
every coarse bit pattern and every fine Hamming-weight orbit, weighted
by its exact binomial multiplicity. For each orbit it counts pivotal
coordinates by the actual score after each coarse/fine flip. This route
does not assume the formula for \(\Gamma_H\). It reconstructs all nine
reported truth-table triples K,M,I(g) exactly, including the 19-input
case, and reproduces every reported trace ratio.

## 4. Complete asymptotic divergence

Set (N=4^k+1\). For N=2d+1, the induction
\(\binom{2d}d/4^d\ge1/(2\sqrt d)\) is correct: its successive
ratio square exceeds (d/(d+1)\) by (1/[4(d+1)^2]\).
Consequently (M_N\ge\sqrt{N/2}\), while Cauchy–Schwarz gives
\(M_N\le\sqrt N\). Thus

\[
pM_N\ge1/\sqrt2,\quad pM_N<9/8,\quad
(k-2)p\le1/8\quad(k\ge2).
\]

This gives (K<9/4\), (K-M\ge\sqrt2>1\), and (K+M\ge3/2\).
The exact variance expression therefore satisfies

\[
K\operatorname{Var}_{\nu_H}(g)
=\frac{(K-M)(K+M)}K\ge2/3,
\qquad
\frac{K\operatorname{Var}_{\nu_H}(g)}{I(g)}
\ge\frac{2^k}{3k}\longrightarrow\infty.
\]

The elementary bounds prove the infinite statement; finite symbolic
binomial calculations are only corroboration. My independent script
also checks exact fractions for k=2..6. Hence a universal trace estimate
for arbitrary same-score slabs and arbitrary same-score halfspaces is
false. The retained-middle hypothesis is essential to distinguish the
unresolved candidate.

## 5. TP2 shortcut fails exactly

For weights (1,2), score order is -3,-1,1,3. At correlation one-half,
the stay/flip probabilities are 3/4 and 1/4. The stated ordered noise
matrix follows directly from Hamming distances. Its rows 0,1 and
columns 1,2 minor is exactly

\[
(pq)q^2-(pq)p^2=-3/32<0.
\]

Thus score ordering does not make the cube noise transition TP2. This
blocks that particular one-dimensional semigroup shortcut, without
disproving any trace or FEI conjecture on its own.

## 6. Audit of the 47,693,379-case finite search

The actual exhaustive script enumerates sorted tuples from {1,...,8}
in dimensions one through eight and keeps gcd one. Sorting removes
coordinate permutations. Removing a common integer gcd loses no tuple
in the declared domain: its primitive rescaling still has entries at
most eight and represents the same ordered attained-score functions.
After grouping tied scores, all triples of distinct gaps are enumerated;
every one gives four nonempty retained components. Families with fewer
than four attained scores correctly have no relevant three-crossing
functions.

The six prefix-sum rectangle formulas are correct. For example
\(e_{12}\) uses rows [a,b) and columns [b,c), and \(e_{13}\) uses
rows [a,b) and columns [c,u). Each cube edge is counted once in its
positive-weight direction. The omitted common physical factor
\(2/2^n\) cancels in all reported ratios. The computed trace numerator
\((2x+o)(2y+o)\) is exactly \(K^2-(x-y)^2\).

All violations of constants two/three are tested by INTEGER comparisons.
There is no numerical threshold tolerance. At n<=8 the total number of
undirected edges is at most 1,024, so prefix sums and all products are
far below signed-int64 overflow. Floating division is used only to
select a maximum candidate, then its fraction is recorded exactly; it
does not affect the exhaustive violation counts. In this finite domain,
ratio denominators are at most 1,024² and ratios at most 1,024, so distinct
trace ratios are also separated by more than double-precision rounding.

I did NOT repeat all 47 million inequality evaluations. Instead the
independent script uses subset-sum BITSETS, without any edge prefix-sum
code, to rebuild every family's attained-score count and the number
\(\binom{u-1}3\) of gap triples. It agrees with each dimension's saved
counts and the totals 12,321 families and 47,693,379 triples.

It then independently counts edges directly for every relevant family
through dimension four (weights 1..8), plus five specified families in
dimensions five through eight. In all **57,822** triple-cut patterns,
the trace bound two and component bound three pass. It directly checks
the exact reported maximizing witnesses, obtaining trace 3/2 and
component 23/11. These checks support the finite report and its
normalization; they cannot prove an arbitrary-weight or unbounded-
dimension estimate.

The new checker and complete independent report are
`three_crossing_routes_ant_independent_check.py` and
`three_crossing_routes_ant_independent_checks.json`. The same script
separately checks the tiny-coordinate retained LOCAL obstruction; those
results must not be confused with a retained-middle TRACE violation.

## 7. Closed conclusions and unresolved claims

| Conclusion relevant to this route | Independent status |
|---|---|
| Original largest-weight local split bound fails for three crossings | Closed analytic obstruction; prior audit PASS |
| Requiring all crossings in both restrictions restores that bound | False; new full-retention obstruction and explicit bounds PASS |
| Component comparison constant two | False; exact common-score 23/11 witness PASS |
| Four-crossing general component comparison | Separately obstructed by the preserved prior construction |
| Generic same-score slab/halfspace trace bound | False; exact two-crossing construction and divergent ratio PASS |
| Scalar-score ordered noise is TP2 | False; exact two-bit negative minor PASS |
| Lacunary finite-crossing FEI | Closed derivation of a class already covered by prior decision-tree results |
| Actual-middle retained-three-crossing trace bound two | **Unproved**; finite evidence only |
| Arbitrary nearby/arbitrary-spacing three-crossing FEI via this route | **Unproved** |
| Unrestricted Boolean FEI | **Not solved by these checkpoints** |

The completed LTF/slab/parity-slab and related composition results in the
separate campaign files are not contradicted by any obstruction here.
The present audit neither expands their scope nor asserts novelty for
them. The new closed negative results concern specific proof criteria;
they do not show entropy exceeds every constant times total influence.
