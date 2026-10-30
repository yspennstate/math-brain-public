# MOC4 fleet04/B09 — exact no-go for the minimal zero-anchor permutation lift

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Worker/run:** fleet04/B09, `20260922T033823Z-b09-moc4-r33`  
**Assignment:** integrate the valid algebraic/geometric pieces and prove the exact remaining unitary-orbit step, including limit cases  
**Outcome:** `CANDIDATE_REFUTED`; the parent MOC4 target remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact live proof state consumed

The target is

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{r=0}^3(a_r+b_{\sigma(r)}):\sigma\in S_4\right\}
\]

for every complex normal `4 x 4` pair, including repeated spectra and singular sums.

This run read the newest complete campaign-lead report available at the start of the run, fleet03/B07 `20260922T013930Z-fleet03-B07-MOC4-r11`, candidate `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`. The lead proves that even a true zero-entry unitary need not admit a common `S_4` law reproducing all squared two-minors; its exact rational witness and the boundary identity

\[
|\det U[\{0,i\},\{0,j\}]|^2=|u_{i0}|^2|u_{0j}|^2
\tag{ZF}
\]

are retained.

The required named OTHER-account partner result is fleet01/B07 `20260922T030302Z-b07-moc4-r11`, candidate `MOC4-CARTAN-HESSIAN-PACKING-v1`. It combines the genuine one-entry Cartan path with the pair-Hessian trace and proves that, on the branch where all sixteen Cartan zero endpoints are support-safe, a gap-`gamma` global maximizer satisfies

\[
-\operatorname{Tr}H_{\rm pair}\ge36\gamma,
\qquad
2k+3(x-\bar c)\ge\frac92\gamma.
\tag{CHP}
\]

I also use the later fleet03/B20 integration `MOC4-PAIR-TWIRL-TWO-POINT-v1`, which consumes this worker's preceding `MOC4-FLAT-PAIR-TWIRL-LIFT-v1` and strengthens the same aggregate constraint to

\[
-\operatorname{Tr}H_{\rm pair}\ge48\gamma,
\qquad
2k+3(x-\bar c)\ge6\gamma.
\tag{PT}
\]

Thus the partner's Cartan theorem remains important for the exact zero/common-block dichotomy and entrywise curvature, while `(PT)` is the sharper currently known aggregate pair bound. Neither theorem closes a genuine violating Cartan zero endpoint. The campaign lead therefore leaves the zero-entry support problem as a real branch, with positive permutation lifts already known to be dangerous.

## 2. The weaker zero-anchor lift one might still hope for

Relabel a zero-entry true unitary so that `u_00=0`, and put

\[
P_{rc}=|u_{rc}|^2,
\qquad
x_i=P_{i0}\ (i=1,2,3),
\qquad
y_j=P_{0j}\ (j=1,2,3).
\]

Then `x` and `y` are probability vectors. By `(ZF)`, the nine squared minors through the distinguished row and column are

\[
Q_{ij}:=|\det U[\{0,i\},\{0,j\}]|^2=x_i y_j.
\tag{1}
\]

The campaign lead refuted a law reproducing *all* squared two-minor marginals. A materially weaker possible mechanism remained:

> **`MOC4-ZERO-ANCHOR-MARGINAL-LIFT-v1`.** There is a probability law `lambda` on `S_4` which reproduces all singleton marginals
> \[
> \Pr_\lambda[\sigma(r)=c]=P_{rc}
> \tag{2}
> \]
> and only the nine zero-anchored two-set marginals
> \[
> \Pr_\lambda[\sigma(\{0,i\})=\{0,j\}]=Q_{ij}=x_i y_j,
> \qquad i,j\in\{1,2,3\}.
> \tag{3}
> \]

This is strictly weaker than the already-refuted common all-two-minor lift: it discards every non-anchored middle-compound marginal. It would nevertheless synchronize the entire `k=1` exterior data with the rank-one `q^+` corner forced by the zero-face geometry, so it is a natural last positive-coupling shortcut to test before attempting a support-specific signed argument.

The result below refutes it exactly on the campaign lead's true rational orthogonal witness.

## 3. A pointwise valid inequality for every anchored permutation law

Because `(2)` gives `P_00=0`, every permutation in the support satisfies `sigma(0)!=0` and `sigma^{-1}(0)!=0`. Write

\[
i=\sigma^{-1}(0)\in\{1,2,3\},\qquad j=\sigma(0)\in\{1,2,3\}.
\]

Under `(2)`-`(3)`, the anchor pair has the forced product law

\[
\Pr[i=r,j=s]=x_r y_s.
\tag{4}
\]

Indeed the event `sigma({0,r})={0,s}` has two orientations, but the orientation `sigma(0)=0` has probability zero, leaving exactly `sigma(0)=s, sigma(r)=0`.

Define the signed singleton statistic

\[
\ell(\sigma)=
1_{\sigma(1)=3}+1_{\sigma(2)=1}+1_{\sigma(3)=2}
-1_{\sigma(1)=2}-1_{\sigma(2)=3}-1_{\sigma(3)=1}.
\tag{5}
\]

Define the nonnegative anchor cost `c(i,j)` by

\[
\begin{array}{c|ccc}
 c(i,j)&j=1&j=2&j=3\\ \hline
 i=1&0&2&1\\
 i=2&1&0&2\\
 i=3&2&1&0
\end{array}.
\tag{6}
\]

### Lemma — exact 18-state inequality

For every permutation with `sigma(0)!=0`, one has

\[
\boxed{\ell(\sigma)+c(\sigma^{-1}(0),\sigma(0))\ge0.}
\tag{7}
\]

#### Proof

Fix the anchor pair `(i,j)`. The remaining two nonzero rows must map bijectively to the remaining two nonzero columns, so there are exactly two completions. Directly in the six off-diagonal anchor cases, the minimum of `ell` over those two completions is respectively

\[
-1,-2,-2,-1,-1,-2,
\]

in the order `(2,1),(3,1),(1,2),(3,2),(1,3),(2,3)`, while for `(1,1),(2,2),(3,3)` the minimum is zero. These are exactly `-c(i,j)`. Thus `(7)` holds pointwise. The verifier independently enumerates all 18 relevant permutations; the only values of the left side are `0` and `3`. QED.

Taking expectation under any proposed lift and using `(2)` and `(4)`, every such lift must satisfy

\[
\boxed{
\begin{aligned}
& P_{13}+P_{21}+P_{32}-P_{12}-P_{23}-P_{31}\\
&\quad +y_1x_2+2y_1x_3+2y_2x_1+y_2x_3+y_3x_1+2y_3x_2\ge0.
\end{aligned}}
\tag{8}
\]

This is a necessary inequality for the *weaker* anchored lift, not an MOC4 inequality.

## 4. Exact true-unitary violation

Use the campaign lead's rational orthogonal matrix

\[
U=\begin{pmatrix}
0&3/5&16/25&-12/25\\
-69/325&-192/325&48/65&16/65\\
48/65&16/65&69/325&192/325\\
16/25&-12/25&0&-3/5
\end{pmatrix}.
\tag{9}
\]

Exact rational arithmetic gives `UU^T=I`. Its anchor distributions are

\[
y=(9/25,256/625,144/625),
\tag{10}
\]

\[
x=(4761/105625,2304/4225,256/625),
\tag{11}
\]

and each sums exactly to one.

For this `P=|U|^2`, the signed singleton part in `(8)` is

\[
P_{13}+P_{21}+P_{32}-P_{12}-P_{23}-P_{31}
=-\frac{848}{845}.
\tag{12}
\]

The anchor-cost expectation is

\[
y_1x_2+2y_1x_3+2y_2x_1+y_2x_3+y_3x_1+2y_3x_2
=\frac{194512}{203125}.
\tag{13}
\]

Therefore the necessary left side of `(8)` is exactly

\[
\boxed{-\frac{121344}{2640625}<0.}
\tag{14}
\]

This contradicts `(8)`. Hence no probability law on `S_4` can simultaneously reproduce even the singleton marginals `P` and the nine rank-one zero-anchor two-set marginals `(1)` for this genuine zero-entry orthogonal matrix.

## 5. Consequence for the shared proof architecture

This is a stronger *route elimination* than the lead's earlier all-two-minor no-go in the following precise sense: the proposed law here is required to match strictly less exterior data, yet it still does not exist. Thus the zero-face obstruction is already visible before one asks for the full second compound.

Accordingly, a successful zero-entry proof cannot proceed by first coupling the distinguished zero row/column to a classical permutation with the forced product anchor law `x_i y_j` while simultaneously preserving the exact singleton matrix `P`. In particular, the exact rank-one identity `(ZF)` does not by itself provide a classical hidden matching compatible with the first exterior power.

This does **not** refute MOC4. It does not even refute the exact zero-face support inequality. The correct surviving mechanisms remain support-specific:

1. the fleet04/B08 `MOC4-ZERO-FACE-GAP-v1` identity retains the essential `X`-dependent fiber gaps rather than seeking a universal positive lift;
2. the fleet01/B07 Cartan theorem gives the exact zero/common-block escape alternative and curvature payments;
3. the fleet03/B20 pair-twirl theorem closes every genuinely flat pair orbit and gives the sharper universal pair-gap/Hessian collar;
4. any remaining zero-entry violation produced by a Cartan escape must therefore be handled directly at the structured support level, not by the minimal anchor coupling refuted here.

The first essential unpaid target-level implication is still the source-exact support statement for a genuine Cartan zero-entry violator (or, on the no-zero-escape branch, the strict compact interior inequality). This run narrows the admissible mechanism by eliminating the last obvious positive coupling that uses only the forced zero-anchor factorization and the first compound.

## 6. Verification and non-claims

`verify_zero_anchor_lift.py` uses only Python standard-library `fractions.Fraction` and `itertools.permutations`. It checks exact orthogonality, the two anchor probability sums, all 18 pointwise inequalities `(7)`, and the exact rational violation `(14)`.

No numerical tolerance, arbitrary bistochastic surrogate, benchmark material, credentials, machine-local data, email/Drive material, public posting, paid model/API/Codex call, remote workflow, or permission change is used.

**Status:** `MOC4-ZERO-ANCHOR-MARGINAL-LIFT-v1 = REFUTED`; full MOC4 remains **OPEN**.
