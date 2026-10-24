# B13 — balanced-uniform gate slice already contains full FEI

**Status:** `CANDIDATE_REFUTED` for universal AND/decomposable extremality at the read-once-scale cap. Full uniform-cube FEI remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository sources were used, but no genuine authenticated brain retrieval was delivered into the reasoning context.

## 1. Live target and exact candidate

The current owner message asks all FEI workers to converge on the all-gate inequality

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le \sum_i \operatorname{It}_i(G;p)
       \frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\tag{G}
\]

for a symmetric nonnegative potential \(\Gamma\). The gate-reformulation source defines the requested margin

\[
c_G(p)=\frac{-D_G(p)}{I(G;p)/4-p_{\rm out}(1-p_{\rm out})}.
\]

Thus gates requiring a **larger** \(c_G\) are the obstruction; the current owner prose saying “minimum” has the direction reversed relative to the source definition, while its falsification instruction “find a gate ... with \(c_G\) above the AND's” has the correct direction.

The current read-once candidate has \(C_0=\Gamma(1/2)=6.4548\), and the proved read-once theorem is \(H\le6.4573 I\). Neither number can be the cap of a universal all-gate potential, as shown below.

## 2. Named other-account theorem consumed

Consumed peer artifact:

`proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260921T124438Z-support-deficit-balanced-equivalence/REPORT.md`, blob `040ed0078f4905b9b4a11e963f27a1e6dcc3ee8d`.

It proves, for every finite constant \(C\), the exact equivalence

\[
H(h)\le C I(h)\quad\text{for every Boolean }h
\]

if and only if

\[
H(f)\le C\bigl(I(f)-1\bigr)\quad\text{for every balanced Boolean }f.
\tag{B}
\]

The forward direction uses balanced recursive self-composition; the reverse direction uses the balanced suspension \(f(y,x)=y h(x)\). This is an all-dimensional theorem, not finite evidence.

For a source-exact quantitative obstruction I also consume the completed 162-input balanced shared-graft construction in

`proofnet24/P03-fei/continuations/2026-09-21-three-hour-sprint/interactive/20260921T121509Z/SHARED_GRAFT_REPORT.md`, blob `11f0405c2869831a14eb6870636f182f52fff353`,

which certifies

\[
I(F)=\frac{68013}{32768},
\]

and

\[
7.014850042680291613033104756310658624299893163
\le H(F)\le
7.014850042680291613033104756310658624299893164.
\tag{1}
\]

It follows there that

\[
\frac{H(F)}{I(F)-1}\ge
6.521850083658612443633672199029299526203969333669\ldots .
\tag{2}
\]

## 3. New applied inference: the balanced-uniform slice of (G) is FEI-complete

### Proposition

Fix \(C\ge0\) and any symmetric potential \(\Gamma\) with \(\Gamma(1/2)=C\). The following are equivalent:

1. FEI at constant \(C\): \(H(h)\le C I(h)\) for every uniform-cube Boolean function \(h\).
2. Inequality (G) holds **only at the uniform bias vector** \(p=(1/2,\ldots,1/2)\) for every **balanced** Boolean gate \(G\).

In particular, the shape of \(\Gamma\) away from \(1/2\) is irrelevant to this necessary slice.

### Proof

Let \(G\) be balanced and put every input bias equal to \(1/2\). Then \(V_{1/2}=1\), \(h(V_{1/2})=0\), \(p_{\rm out}=1/2\), the gate's biased spectral entropy is its ordinary spectral entropy \(H(G)\), and

\[
\sum_i \operatorname{It}_i(G;1/2)=I(G).
\]

Hence (G) becomes exactly

\[
C+H(G)\le C I(G),
\]

or equivalently

\[
H(G)\le C\bigl(I(G)-1\bigr).
\tag{3}
\]

By the consumed account02/B17 theorem, (3) for every balanced Boolean gate is equivalent, constant-for-constant, to full FEI. Conversely, full FEI implies (3), and therefore this uniform balanced slice of (G). QED.

This does not prove FEI. It proves that the current all-gate programme already contains the entire conjecture on its balanced-uniform slice, before any nonuniform bias or potential-shape issue is considered.

## 4. Decisive quantitative falsification of AND/decomposable extremality at the current cap

Apply the proposition to the certified 162-input balanced gate \(F\) from (1). Every universal all-gate potential must satisfy

\[
\boxed{\Gamma(1/2)\ge
6.521850083658612443633672199029299526203969333669\ldots .}
\tag{4}
\]

Therefore no change to the potential away from \(1/2\) can rescue a universal cap of 6.4548, 6.4559, or the proved read-once upper-bound scale 6.4573.

For the specific read-once candidate \(C_0=6.4548\), the balanced-gate identity gives

\[
c_F(1/2,\ldots,1/2)
=4\left(\frac{H(F)}{I(F)-1}-C_0\right),
\]

so the certified lower endpoint gives

\[
\boxed{c_F\ge
0.268200334634449774534688796117198104815877334678\ldots .}
\tag{5}
\]

Against the currently quoted two-input AND margin floor \(0.0043974201\), this is a factor greater than

\[
\boxed{60.9903826642}. 
\]

The corresponding gate defect at \(C_0=6.4548\) is at most

\[
-0.072118536332635363033104756310658624299893163<0.
\]

Even at cap 6.4573 the defect is at most

\[
-0.069429556230096300533104756310658624299893163<0.
\]

Thus the universal statement that the two-input AND/decomposable gates are extremal for the current read-once-scale potential is **REFUTED** by a genuine balanced Boolean gate. This strengthens the same-run B15 observation: it is not merely the particular read-once potential *shape* that fails. Any all-gate potential with a cap below (4) fails already on the balanced-uniform slice.

## 5. Status and replacement obligation

**REFUTED:** “the two-input AND is extremal among all Boolean gates at the read-once-scale cap,” and any proposed universal gate potential with \(\Gamma(1/2)<6.5218500836586124436\ldots\).

**PROVED:** for fixed cap \(C=\Gamma(1/2)\), the balanced-uniform slice of (G) is constant-for-constant equivalent to full FEI.

**OPEN:** existence of any finite \(C\) and symmetric nonnegative \(\Gamma\) satisfying (G) for every gate and every bias vector; equivalently, full FEI.

The gate programme must therefore be rebased at a cap at least as large as the certified balanced lower bound. Searching for a cleverer shape of \(\Gamma\) while keeping \(\Gamma(1/2)\) near 6.455 is mathematically impossible. Any successor candidate should first be tested on the balanced-uniform slice, where potential shape disappears entirely.

`consumed_peer_artifact`: account02/B17 `20260921T124438Z-support-deficit-balanced-equivalence`, blob `040ed0078f4905b9b4a11e963f27a1e6dcc3ee8d`.

`applied_to_claim`: universal AND/decomposable extremality and universal validity of an all-gate potential at the read-once-scale cap.

`remaining_implication`: prove a finite upper bound for \(H(f)/(I(f)-1)\) over every balanced Boolean gate (equivalently full FEI), then extend/encode it in a universal gate potential.

`next_recipient`: `account03/B18`, with the instruction that integration must supersede the read-once-scale universal candidate and retain the certified balanced lower bound.

No novelty or publication-priority claim is made. The peer equivalence and shared-graft construction are inherited results; the contribution here is their exact application to the live all-gate target and the resulting cap-independent obstruction.
