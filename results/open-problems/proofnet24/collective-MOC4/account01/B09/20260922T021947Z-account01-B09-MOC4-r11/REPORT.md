# MOC4 account01/B09 — an exact one-parameter rank-two bi-Rayleigh family satisfies the stationary-roof gate

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal 4-by-4 Marcus–de Oliveira target  
**Worker:** account01/B09  
**Candidate:** `MOC4-RANK2-STATIONARY-ROOF-FAMILY-v1`  
**Outcome:** `AUXILIARY_ONLY` — a continuous singular adversarial family is proved to satisfy the newest stationary-roof sufficient gate; full MOC4 remains OPEN.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Current end-to-end route and the exact missing implication

The source-exact target is

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\]

for every complex normal `4 x 4` pair, including singular sums and repeated spectra.

This run directly consumes the named OTHER-account result **account02/B07, `MOC4-PARITY-SLACK-v1` refutation, run `20260922T013439Z-b07-moc4-r11a`**. That report preserves the exact six-fiber support identity `(SR)` and sharpens the surviving route to `MOC4-SR-AT-BIRAYLEIGH-v2`: a hypothetical global support maximizer obeys all six row-pair and six column-pair top-Rayleigh conditions, and one must derive the actual six-fiber support bound from those coupled conditions rather than from the refuted unconditional parity-slack shortcut.

I also use account01/B08's exact 3-by-3 roof calculation, which isolates the narrower sufficient condition

\[
2\max\{M_K(L),M_K(U)\}\le
S(D,R,K):=\langle R,|K|\rangle-\langle D,K\rangle. \tag{SPR}
\]

A genuine pair-stationary counterexample to `(SPR)` would eliminate this remaining scalar-roof route while still not automatically refuting MOC4. The present run attacks precisely that possibility, using a materially different mechanism from B09's preceding isolated coefficient-lift and monomial-rigidity no-gos: an exact rational **one-parameter Schur-complement family**.

The compact conditional chain is therefore:

1. a strict support violation may be placed at a global support-maximizing true unitary after the team's generic reduction;
2. account02/B07's singular-safe pair-Rayleigh theorem gives twelve row/column top-Rayleigh conditions there;
3. the exact exterior-power/Hadamard reduction gives `(SR)`;
4. `(SPR)` would imply the required scalar roof inequality and hence `(SR)`;
5. so the immediate adversarial question is whether a true-unitary family can satisfy all twelve pair-top conditions while violating `(SPR)`.

This report gives a nontrivial negative answer for an explicit continuous singular family, not a universal proof of `(SPR)`.

## 2. Exact rank-two family

Fix the dense rational orthogonal matrix

\[
U=\begin{pmatrix}
-220/243&71/243&-62/243&14/81\\
-61/243&-220/243&-68/243&-16/81\\
68/243&62/243&-215/243&-22/81\\
-16/81&14/81&22/81&-25/27
\end{pmatrix},
\qquad b=(-4,-2,3,-1).
\]

For a real parameter `x`, set

\[
\begin{aligned}
a_1(x)&=(81x+266)/81,\\
a_2(x)&=\frac{4(184113x-208055)}{81(4131x-6755)},\\
a_3(x)&=\frac{43821x-83110}{27(729x+280)},\\
a_4(x)&=\frac{65043x+41476}{3(21141x+3088)}.
\end{aligned} \tag{1}
\]

Let

\[
X(x)=D_{a(x)}+UD_bU^T.
\]

The formulas in `(1)` are obtained by taking the leading `2 x 2` block as a pivot and imposing that the `2 x 2` Schur complement vanish identically. The verifier checks all sixteen `3 x 3` minors of `X(x)` vanish identically. Its leading `2 x 2` determinant is

\[
\frac{8(729x+280)(21141x+3088)}{59049(4131x-6755)}, \tag{2}
\]

which is positive on

\[
I=[177/100,89/50]. \tag{3}
\]

Hence

\[
\operatorname{rank}X(x)=2,\qquad \det X(x)=0,\qquad \operatorname{adj}X(x)=0 \tag{4}
\]

for every `x in I`. Exact Sturm/root counts also show the four `a_i(x)` are pairwise distinct and every `a_i(x)+b_j` is nonzero throughout `I`.

At `x=16/9`, this family contains B09's previous isolated rank-two witness. The new point is that the phenomenon is not isolated: it persists on an exact interval.

## 3. All twelve genuine pair-Rayleigh conditions are strict on the whole interval

Because `adj X(x)=0`, the directional derivative of `det X` vanishes for every matrix perturbation and hence for every true-unitary tangent direction. Account02/B07's `MOC4-BIRAYLEIGH-ORBIT-v1` says each row-pair or column-pair `U(2)` restriction is an exact `2 x 2` Hermitian Rayleigh quotient, valid even when the determinant is singular. At a stationary north pole, it is enough to compare the current value with the antipodal label-swap value.

For this family the current support in direction `eta=1` is `h(U)=0`. Every one of the twelve swap supports factors as a **negative constant times a square**, over the same positive denominator on `I`. For example,

\[
h(UP_{01})=
-\frac{32(256922199x^2+456394176x-894448615)^2}
{43046721(729x+280)(4131x-6755)(21141x+3088)}, \tag{5}
\]

and

\[
h(P_{01}U)=
-\frac{3165128(334611x^2-184761x-964610)^2}
{4782969(729x+280)(4131x-6755)(21141x+3088)}. \tag{6}
\]

The exact verifier checks that the quadratic square factors for **all six column swaps and all six row swaps have no zero in `I`**. Thus

\[
h(UP_{pq})<0=h(U),\qquad h(P_{ij}U)<0=h(U) \tag{7}
\]

for all six pairs of each type and every `x in I`.

Combining stationarity from `(4)` with the exact pair-Rayleigh theorem proves that the same dense nonmonomial `U` is a **strict top-Rayleigh point on all twelve genuine pair orbits for every parameter value in the interval**.

## 4. Exact stationary-roof calculation

For this fixed unitary, the 3-by-3 standard-representation matrices are constant:

\[
R=\frac1{59049}\begin{pmatrix}
47665&2692&8692\\
8692&45844&4513\\
2692&10513&45844
\end{pmatrix},
\]

\[
D=\frac1{59049}\begin{pmatrix}
46513&1540&-2860\\
2860&44044&95\\
-1540&-145&44044
\end{pmatrix}. \tag{8}
\]

The full 3-by-3 Birkhoff fiber has endpoints

\[
L=14384/19683,\qquad U_*=45844/59049. \tag{9}
\]

Reconstructing the structured support block `K(x)` from the exact spectral formulas, not inserting an arbitrary 3-by-3 matrix, the verifier proves the constant sign pattern

\[
\operatorname{sgn}K=
\begin{pmatrix}
-&+&-\\
-&+&-\\
+&+&+
\end{pmatrix} \tag{10}
\]

throughout `I`, with no zero entry there. It also root-certifies the exact minimum-absolute-entry choice on each negative-parity transversal. Therefore the endpoint parity penalties `M_L(x),M_U(x)` are fixed rational functions on `I`. Their difference factors as

\[
M_U-M_L=
-\frac{5384(334611x^2-184761x-964610)
(746976411x^2+2604036114x-1191480460)}
{129140163(729x+280)(4131x-6755)(21141x+3088)}, \tag{11}
\]

and exact root/sign certification gives `M_U>M_L` everywhere on `I`.

Consequently the exact `(SPR)` margin on the whole interval is

\[
\boxed{
G(x):=S(D,R,K)-2\max(M_L,M_U)
= -\frac{5P_4(x)}{10460353203(729x+280)(4131x-6755)(21141x+3088)}
} \tag{12}
\]

where

\[
\begin{aligned}
P_4(x)={}&417505228780624817193x^4
-7878953468924386283610x^3\\
&-8079182274144688129197x^2
+24854794555730927932854x\\
&-530351345114699817160.
\end{aligned}
\]

The denominator has no zero and is positive on `I`; `P_4` has no zero on `I`; evaluating at the rational midpoint gives

\[
G(71/40)=
\frac{330000120968261985271160143}
{1169947129251679184069784}>0. \tag{13}
\]

Hence `(SPR)` holds **strictly for every member of the one-parameter family**.

This matters because the family simultaneously exhibits the pathology that defeated the stronger monomial-rigidity route—dense nonmonomial true unitary, singular rank-two sum, and twelve strict pair-top conditions—yet it still cannot defeat the latest stationary-roof gate.

## 5. Not a target counterexample: exact hull containment on the whole interval

The determinant is identically zero. The verifier checks all 24 real permutation products remain pairwise distinct on `I`. Two fixed vertices keep opposite signs throughout:

\[
v_{(3,4,2,1)}(x)=
-\frac{10285(81x-1786)(81x+509)(11097x-260)(36531x-25915)}
{531441(729x+280)(4131x-6755)(21141x+3088)}>0,
\]

while

\[
v_{(4,2,1,3)}(x)=
-\frac{40(81x+185)(6723x+26209)(34911x+113350)(63828x+17317)}
{531441(729x+280)(4131x-6755)(21141x+3088)}<0. \tag{14}
\]

Thus `0=det X(x)` lies on the line segment joining those two target vertices for every `x in I`. The family is therefore source-valid and **provably inside the target hull**; it is not a counterexample to MOC4.

## 6. What this changes

The honest conclusion is `AUXILIARY_ONLY`, but it is a useful elimination rather than a census:

- The latest pair-stationary scalar-roof gate survives an exact continuous family of singular, dense, nonmonomial bi-Rayleigh maxima.
- The previous isolated rank-two witness was not concealing a nearby stationary-roof violation; the same mechanism persists over a rational interval with a large exact positive roof margin.
- The negative swap factorizations as squares indicate why this singular family is exceptionally stable under the twelve pair tests.
- Therefore the next adversarial effort should move **off the rank-two singular manifold** and search for a nonsingular true-unitary simultaneous pair-stationary point that violates `(SPR)`, or attack the full `X`-dependent `(SR)` directly. Producing more isolated rank-two singular points by the same mechanism is unlikely to pay the missing implication.

This does **not** prove `MOC4-STATIONARY-ROOF-v1`, `MOC4-SR-AT-BIRAYLEIGH-v2`, or MOC4. It proves only the exact family theorem stated above.

## 7. Verification and provenance

`verify_rank2_stationary_roof_family.py` reconstructs the unitary, spectra, rank-two condition, all twelve true-unitary swap supports, the exact `R,D,K` blocks, Birkhoff endpoints, parity minima, stationary-roof gap, all 24 permutation vertices, and the opposite-sign hull certificate using exact SymPy rational arithmetic and exact polynomial root counts. It exits 0 with `PASS MOC4-RANK2-STATIONARY-ROOF-FAMILY-v1`.

The target statement and source boundaries are those in the collective MOC4 `TARGETS.md` (Drury 2004 weakened n=4 result; Bebiano–da Providencia 2025 survey; Mulero-Martinez 2026 variational obstruction). No claim of worldwide novelty is made. No arbitrary bistochastic surrogate, floating tolerance, benchmark material, credentials, scheduler identifier, machine path, unrelated private data, email, Drive, public posting, paid model/API/Codex call, remote workflow, or permission bypass is used.
