# B14 — affine host-edge geometry and an optimal eight-of-nine physical selector

**Classification:** `ESSENTIAL_STEP_APPLIED / AFFINE_GEOMETRY_LOCALIZED`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were used directly, but no authenticated installed/native brain retrieval or context entered the mathematics.

## 0. Live target, exact candidate version, and what changed

The current FEI chain uses the stable scalar-lift candidate
\[
C_*=6.5218512,
\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p),
\qquad a_*=0.2682048,
\]
and the universal missing implication is still the all-gate inequality for every composition-prime Boolean gate and every interior product bias.  Full FEI is not claimed here.

This run attacks a restriction-policy question on the **same nine-host shared-core geometry** that currently generates the strongest lower-bound/threat family.  The exact candidate version is:

> `SHARED-GRAFT-AFFINE-SELECTOR-v1`: can a non-coordinate affine query or an adaptive physical restriction expose the current shared-core hard family while preserving all host gadgets, so that the stable gate defect can be proved by a no-geometry-loss induction?

The answer has two parts.

1. **REFUTED (zero-loss affine version):** no nonconstant affine core query preserves all nine host edges.  A query supported on `k` pivot directions splits exactly `k` host edges.  In particular the coherent all-core parity splits all nine, while a physical coordinate splits exactly one.  Thus an affine change of coordinates cannot eliminate the geometry loss; physical coordinates are already optimal for this metric.
2. **PROVED (optimal adaptive replacement):** there is an adaptive physical decision tree that preserves **eight of the nine** grafts intact and sacrifices exactly one.  This is optimal.  The resulting defect/Poincare ledger differs from the unattainable all-nine-intact ledger by exactly one **mass-weighted one-coordinate restriction decrement** of the inserted gadget.

This gives a sharp replacement obligation rather than another broad selector search.

## 1. Named compatible peer result consumed and applied

The main other-account input is

`fleet02/B16/20260922T045841Z-source-bias-log-curvature/REPORT.md`,
report blob `06586519345fffaf8d2aa078b0659ada506f79eb`.

For the actual composition-prime `n=18` source gate it proves an exact biased zero-mode birth matrix.  Every one-coordinate diagonal is safe at singular order, but the coherent direction that biases **all nine core coordinates together** is dangerous:
\[
v^\top Bv=-\frac{67383}{32768},
\]
and hence the requested gate margin rises as
\[
c_F(\varepsilon)
=c_F(0)+\frac{67383}{2128}\varepsilon^2\log_2(1/\varepsilon^2)+O(\varepsilon^2).
\]
That peer leaves a finite remainder check for the stable candidate.

I apply that exact coherent direction to the **source host-edge geometry** from the shared-graft construction

`proofnet24/P03-fei/continuations/2026-09-21-three-hour-sprint/interactive/20260921T121509Z/SHARED_GRAFT_REPORT.md`,
report blob `11f0405c2869831a14eb6870636f182f52fff353`.
The nine exceptional core edges are
\[
\begin{array}{c|c|c}
j&P_j&\text{pivot direction }r_j\\\hline
0&(78,79)&0\\
1&(113,121)&3\\
2&(228,484)&8\\
3&(170,186)&4\\
4&(149,151)&1\\
5&(338,466)&7\\
6&(284,316)&5\\
7&(291,295)&2\\
8&(393,457)&6.
\end{array}
\]
Thus `(r_0,...,r_8)=(0,3,8,4,1,7,5,2,6)` is a permutation of all nine core directions.

I also use the exact fixed-candidate shared-core defect identity from
`fleet02/B16/20260922T031545Z-limit-prime-shared-core-threat-corridor/REPORT.md`,
report blob `7b8836311af20ce7c0342e3deaeb4869651d2cfe`:
\[
\Delta_*(T(h,b))
=\frac9{256}\Delta_*(h)
+\frac{133}{128}\bigl(C_*-T(b)\bigr).
\tag{1.1}
\]
Its rigorous scalar envelope is
\[
T(b)<M_+
:=6.52185121301287772365150440023918196647146413881.
\tag{1.2}
\]

## 2. Exact affine-query splitting theorem

Write the core cube as `F_2^9`.  An affine query has the form
\[
\ell_{a,c}(x)=a\cdot x+c,
\qquad 0\ne a\in\mathbb F_2^9.
\]
The two endpoints of `P_j` differ by `e_{r_j}`.  Therefore
\[
\ell_{a,c}(x+e_{r_j})-\ell_{a,c}(x)=a_{r_j}\pmod2.
\]
Hence:

### Theorem 2.1 — exact affine host-edge charge

The query `ell_{a,c}` splits `P_j` if and only if `a_{r_j}=1`.  Consequently
\[
\boxed{
N_{\rm split}(a)=|\operatorname{supp}(a)|.
}
\tag{2.1}
\]
Because the pivot directions are a permutation of the coordinate basis, every nonconstant affine query splits at least one host edge, and a non-coordinate query supported on `k>=2` directions splits at least two.

For arbitrary product bias on the nine core variables, let
\[
q_j=\Pr[X\in P_j]
\]
be the mass of host edge `P_j`.  The exact **mass charge** of `ell_a` is
\[
\boxed{
Q_{\rm split}(a)=\sum_{j:a_{r_j}=1}q_j.
}
\tag{2.2}
\]
Therefore
\[
\boxed{
\min_{a\ne0}Q_{\rm split}(a)=\min_j q_j,
}
\tag{2.3}
\]
and the minimum is attained by a physical single-coordinate query in the pivot basis.

This also charges a full affine recoding.  If `A in GL(9,2)` is used as a new affine coordinate system, each row of `A` is nonzero, so each new coordinate query splits at least one source host edge.  The total row-edge incidence is at least `9`, with equality for a permutation of the physical pivot basis.  Thus there is no hidden affine basis with zero or sub-physical geometry cost.

In particular the coherent all-core parity `a=(1,...,1)` suggested by the fleet02/B16 dangerous bias sector splits **all nine** host edges.  It is geometrically the worst possible single affine query, not a lossless way to follow that collective mode.

## 3. Optimal adaptive physical tree: eight intact grafts are achievable and best possible

The affine theorem immediately gives the upper bound.  The first nonconstant query in any physical/affine decision tree splits at least one of the nine host edges, and a split edge can never later reappear as an intact one-dimensional host leaf.  Therefore at most eight host edges can survive intact.

The adjacent checker performs an exact finite dynamic program on partial core assignments.  A state is a subcube specified by `(fixed_mask,fixed_values)`.  An edge survives a state only if both of its endpoints remain in the subcube.  A terminal earns one unit exactly when the state is one of the original host edges and its pivot coordinate was never queried.  The recurrence maximizes the sum over the two children of every allowed physical query.

It proves
\[
\boxed{\max_{\mathcal T}\#\{\text{intact host-edge terminals}\}=8.}
\tag{3.1}
\]
More strongly, **every** physical coordinate can be chosen as the first query and there is a continuation preserving all eight other host edges.  For example, querying `x_0` first sacrifices only `P_0`, and an exact adaptive continuation preserves `P_1,...,P_8` intact.

Thus (3.1) is not merely a counting obstruction; it is a tight realizable policy.

For nonuniform core product measure, choose the first physical query to be the pivot of an edge `j_*` minimizing `q_j`.  The same decision tree preserves every other edge.  Hence the optimal geometry-only loss is exactly
\[
\boxed{q_{j_*}=\min_jq_j.}
\tag{3.2}
\]
No affine query can improve this by (2.3).

## 4. Exact defect ledger: all geometry loss becomes one mass-weighted cofactor decrement

Consider the shared-core graft `T(h)` in which each host edge carries a copy of a Boolean gadget `h`, with its distinguished input identified with that edge's pivot coordinate.  Fix a symmetric gate potential `Gamma` and let `D_Gamma` be its gate defect.

For one host edge `j`, let `s_j` be the product bias of its pivot, and write `h_{j,0},h_{j,1}` for the two cofactors obtained by fixing the distinguished input.  Define the one-coordinate defect decrement
\[
\delta_{\Gamma,j}(h)
:=D_\Gamma(h)
-\bigl[(1-s_j)D_\Gamma(h_{j,0})+s_jD_\Gamma(h_{j,1})\bigr].
\tag{4.1}
\]

The unattainable ideal in which all nine host edges survive intact would have terminal continuation
\[
\mathcal C_{\rm ideal}=\sum_j q_jD_\Gamma(h_j).
\]
The optimal physical tree that sacrifices only `j_*` has
\[
\mathcal C_{\rm phys}
=\sum_{j\ne j_*}q_jD_\Gamma(h_j)
+q_{j_*}\bigl[(1-s_{j_*})D_\Gamma(h_{j_*,0})
+s_{j_*}D_\Gamma(h_{j_*,1})\bigr].
\]
Therefore
\[
\boxed{
\mathcal C_{\rm ideal}-\mathcal C_{\rm phys}
=q_{j_*}\,\delta_{\Gamma,j_*}(h).
}
\tag{4.2}
\]
This is the exact mass-weighted geometry charge.  No affine coordinate change is hidden and no descendant slack is discarded.

At the uniform source geometry, every `q_j=1/256`, every pivot has `s_j=1/2`, and a tree sacrificing one edge gives
\[
\boxed{
\mathcal C_{\rm phys}
=\frac8{256}D_\Gamma(h)
+\frac{D_\Gamma(h_0)+D_\Gamma(h_1)}{512}.
}
\tag{4.3}
\]
The remaining `494/512=247/256` of the core mass ends at constant leaves.

The same identity holds for the Poincare currency `W`.  If
\[
\omega_j
:=W(h)-[(1-s_j)W(h_{j,0})+s_jW(h_{j,1})],
\]
then the exact one-coordinate restriction identity gives
\[
\omega_j=s_j(1-s_j)\bigl(d_j-(r_1-r_0)^2\bigr)\ge0.
\tag{4.4}
\]
For a balanced monotone gadget at uniform bias whose distinguished singleton coefficient/influence is `b`,
\[
\boxed{\omega=\frac{b(1-b)}4.}
\tag{4.5}
\]
For the original source auxiliary coordinate `b=1/256`,
\[
\omega=\frac{255}{262144},
\qquad
\frac{\omega}{256}=\frac{255}{67108864}.
\tag{4.6}
\]
Under the stable quadratic lift, the **positive lift contribution** to the unavoidable one-edge split is therefore exactly
\[
a_*\frac{255}{67108864}
=0.000001019123554229736328125.
\tag{4.7}
\]
This does not by itself prove the full split defect is positive: the signed base-potential restriction decrement remains live and must not be dropped.

## 5. Apply the ledger to the current shared-core threat corridor

At uniform bias, the fixed-core stable-candidate identity (1.1) has an immediate restriction interpretation.  The ideal all-nine-intact continuation is exactly
\[
\frac9{256}\Delta_*(h).
\]
Hence its ideal local block term is
\[
L_*(b)=\frac{133}{128}(C_*-T(b)).
\]
Replacing the impossible ideal by the optimal realizable eight-of-nine tree gives the exact physical block decrement
\[
\boxed{
D^{\rm block}_{\rm phys}
=\frac{133}{128}(C_*-T(b))
+\frac1{256}\delta_*(h),
}
\tag{5.1}
\]
where `delta_*` is the distinguished-input restriction decrement (4.1) computed with the **same** stable potential at root and cofactors.

This sharply replaces the vague instruction “find a better restriction.”  If `T(b)>C_*`, the exact selector/potential payment required by this optimal physical policy is
\[
\boxed{
\delta_*(h)
\ge 256\frac{133}{128}\,[T(b)-C_*]
=266\,[T(b)-C_*].
}
\tag{5.2}
\]
The fleet02/B16 global source envelope (1.2) implies that the single uniform sufficient bound
\[
\boxed{
\delta_*(h)
\ge
0.00000346142547449130017046362240308140946092346
}
\tag{5.3}
\]
would pay the **entire currently certified fixed-core threat corridor** by this realizable tree.

Equation (5.3) is an obligation, not a proved inequality.  In particular, one must also keep the two cofactor continuations source-valid; a positive quadratic contribution alone is insufficient because the base restriction decrement is signed.

## 6. Exact status and replacement obligation

### PROVED

1. Every nonconstant affine core query splits at least one source host edge; a support-`k` affine query splits exactly `k`.
2. Physical single-coordinate queries minimize the exact split mass among all affine queries.
3. An adaptive physical tree can preserve eight host edges intact and sacrifice exactly one; eight is optimal.
4. The full affine/physical geometry loss is exactly one mass-weighted distinguished-coordinate defect decrement, equation (4.2).
5. For the stable shared-core corridor, the optimal physical block condition is exactly (5.2), with the global sufficient numerical threshold (5.3).

### REFUTED

The exact strategy “use a clever non-coordinate affine query to follow the coherent dangerous direction while preserving all shared grafts” is impossible on the actual source geometry.  The coherent all-core parity splits all nine host edges, and no nonzero affine query has zero split cost.

### OPEN

The inequality (5.2) for every source-valid near-tight threat gadget is not proved.  Nor is `D_{Gamma_*}(G;p)>=0` proved for every composition-prime gate and every product bias.  Full FEI remains OPEN.

The next mathematically sharp attack is therefore **not another affine recoding**.  It is to prove (or falsify) the single distinguished-coordinate restriction bound (5.2) on the tiny `(absolute defect, singleton)` corridor already localized by fleet02/B16, while retaining both cofactor defects.  A source-valid gadget in that corridor violating (5.2) would refute this restriction compiler; proving it together with cofactor safety would close the current shared-core restriction gap.

`consumed_peer_artifact`: `fleet02/B16/20260922T045841Z-source-bias-log-curvature/REPORT.md`.  
`applied_to_claim`: non-coordinate/adaptive restriction policy for the exact nine-host shared-core hard geometry.  
`remaining_implication`: prove/falsify (5.2) with signed cofactor continuation on the localized stable-candidate threat corridor; universal all-prime/all-bias gate inequality remains open.  
`next_recipient`: `fleet02/B16` (current biased-prime/threat-corridor lane).

## 7. Verification

`CHECKER.py` verifies exactly that the nine listed pairs are disjoint Hamming edges with pivot directions forming a permutation; enumerates all `511` nonzero affine query vectors and obtains the exact split-count histogram
\[
(9,36,84,126,126,84,36,9,1)
\]
for split counts `1,...,9`; runs the exact dynamic program proving the maximum number of intact edge terminals is `8` and that every physical first query admits an eight-edge continuation; and checks the rational Poincare arithmetic and the decimal threshold in (5.3).

The finite checker certifies only this nine-bit source geometry and the displayed arithmetic; the universal defect identities are proved algebraically above.  No novelty/publication-priority claim is made.
