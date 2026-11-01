# B18 — recursive shared-core graft raises the balanced FEI floor

**Classification:** `CANDIDATE_REFUTED` for the current `PRIME-GATE-LIFT` candidate at the previous certified balanced cap.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository sources were used directly; no authenticated cognitive-brain retrieval/context was used.

## 1. Exact candidate bound and peer results consumed

The campaign's current all-gate reformulation asks for a symmetric nonnegative potential `Gamma` such that, for every Boolean gate `G` and every product bias vector,

\[
\Gamma(p_{out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u).
\tag{1.1}
\]

The named other-account result applied here is fleet02/B17,

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260922T004442Z-gate-composition-cocycle/REPORT.md`, commit
`d1277d4acccafbd93b9703359626e740a5a8347a`.

It proves the exact gate-composition cocycle. In particular, after adding a scalar quadratic correction `a p(1-p)` to a reference potential, both the corrected gate slack and its Poincare currency compose with the same nonnegative weights. Hence a violating gate has a composition-prime violating factor. That report proposed the explicit successor

> `PRIME-GATE-LIFT`: with the previous strongest certified balanced lower bound
> \[
> L_*=6.521850083658612443633672199029299526203969334\ldots,
> \]
> lift the old read-once potential by the minimal quadratic amount needed to reach `L_*`, and prove the corrected gate inequality on every composition-prime gate and every product bias.

This run directly attacks that exact candidate rather than auditing it.

I also apply the existing shared-core construction in

`proofnet24/P03-fei/continuations/2026-09-21-three-hour-sprint/interactive/20260921T121509Z/SHARED_GRAFT_REPORT.md`, commit
`ba37f4275024ddfff125dec2eb1f75fd871cd6c7`.

It starts from the source-validated balanced monotone 18-bit Numaro gate `g`, whose truth-table SHA-256 is

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`,

and constructs a balanced monotone 162-input gate `F_1` by placing one fresh copy of `g` on each of nine disjoint host edges while identifying one small-influence gadget coordinate with the corresponding host pivot. Its exact structural formulas, not a 162-bit brute-force enumeration, are the input to the new construction below.

The already-proved addressing/tribes/sparse-defect reductions were also respected: disjoint recursive composition cannot increase the normalized gate margin by the cocycle, common-data addressing collapses to a three-input MUX, and one/two-point sparse defects reduce to smaller cores. Therefore the mechanism below deliberately uses **shared-coordinate interference**, the one mechanism not erased by those reductions.

## 2. The old shared-core gate and a new exact singleton coefficient

Let

\[
I_1=I(F_1)=\frac{68013}{32768}.
\tag{2.1}
\]

The source certificate gives

\[
R_1:=\frac{H(F_1)}{I(F_1)-1}
\in
[6.521850083658612443633672199029299526203969334,\,
 6.521850083658612443633672199029299526203969335].
\tag{2.2}
\]

For the shared-core construction write `a(x)` for the fixed nine-bit core, `Q_j` for the signed host-edge indicator, and let `b=1/256` be the distinguished singleton coefficient of the original 18-bit gadget. The empty-fresh-coordinate Fourier coefficient is

\[
\widehat F_1(S)=\widehat a(S)+b\sum_{j=0}^8\widehat Q_j(S).
\tag{2.3}
\]

Taking `S={0}` (any of the nine symmetric core coordinates works after relabeling in this source representation), the exact integer Walsh numerators give

\[
\frac{\widehat a(\{0\})}{1}
=\frac{114}{512},
\qquad
\frac{\sum_j\widehat Q_j(\{0\})}{512}
=\frac{2}{512}.
\]

Hence the corresponding singleton Fourier coefficient of `F_1` is exactly

\[
\boxed{
 c_1=\frac{114}{512}+\frac1{256}\frac2{512}
 =\frac{14593}{65536}.
}
\tag{2.4}
\]

This number is much larger than the original gadget's distinguished coefficient `1/256`. It is the lever used below.

## 3. Balanced self-composition preserves the excess ratio and multiplies the chosen singleton coefficient

For a balanced Boolean gate `f`, let `f^{\circ d}` denote depth-`d` disjoint self-composition: every input of the outer copy is replaced by a fresh copy of `f`, recursively.

The standard balanced composition identities are

\[
I(f^{\circ d})=I(f)^d,
\qquad
H(f^{\circ d})=H(f)\frac{I(f)^d-1}{I(f)-1}.
\tag{3.1}
\]

Therefore

\[
\frac{H(f^{\circ d})}{I(f^{\circ d})-1}
=\frac{H(f)}{I(f)-1}.
\tag{3.2}
\]

If a specified leaf follows a specified singleton coordinate through each composition level, its Fourier singleton coefficient is the product of the corresponding singleton coefficients. Thus for

\[
A:=F_1^{\circ4}
\]

we have exactly

\[
I_A=I_1^4
=\frac{21397731153333612561}{1152921504606846976},
\tag{3.3}
\]

\[
H_A=H(F_1)\frac{I_A-1}{I_1-1},
\tag{3.4}
\]

and the chosen leaf coefficient is

\[
\boxed{
 b_A=c_1^4
 =\frac{45350108441011201}{18446744073709551616}.
}
\tag{3.5}
\]

The gate `A` remains balanced and monotone.

## 4. Apply the shared-core transform a second time

The old shared-core proof in fact works for **any** balanced monotone gadget `h` with a selected distinguished singleton coefficient `b`. Let

\[
\phi(t)=-t\log_2 t,
\qquad
\alpha=\frac9{256},
\]

and define

\[
H_{core}(b)
=\sum_{S\subseteq[9]}
\phi\!\left(\left[\widehat a(S)+b\sum_j\widehat Q_j(S)\right]^2\right).
\tag{4.1}
\]

The resulting nine-host graft `T(h,b)` satisfies exactly

\[
H(T(h,b))
=H_{core}(b)
+\alpha\,[H(h)-\phi(b^2)+16(1-b^2)],
\tag{4.2}
\]

\[
I(T(h,b))
=\frac{261}{128}+\alpha\,[I(h)-1].
\tag{4.3}
\]

These formulas follow coefficient-by-coefficient from the disjoint Fourier supports of the host indicators and do not assume that the shared pivot is independent of the gadget.

Now set

\[
F_2:=T(A,b_A).
\]

The same free-edge argument used for `F_1` proves `F_2` is an actual balanced monotone Boolean function: off the nine hosts it equals the fixed core; on host `j` it equals a fresh copy of `A`, with the selected leaf identified with that host's pivot coordinate.

From (3.3) and (4.3),

\[
\boxed{
I(F_2)
=\frac{784028312243315011737}{295147905179352825856}.
}
\tag{4.4}
\]

The entropy is evaluated from (4.2) with exact rational logarithm enclosures.

## 5. Certified strict improvement

The committed checker reconstructs the published 18-bit source, verifies the complete source truth-table SHA-256, performs the integer Walsh transforms on the nine-bit core and the source gate, and evaluates every logarithm using an exact `Fraction` atanh-series enclosure with a rigorous remainder after dyadic range reduction. The enormous composed gate is **not** enumerated; equations (3.1)--(4.3) are used exactly.

It returns

\[
R_1=\frac{H(F_1)}{I(F_1)-1}
=6.521850083658612443633672199029299526203969334\ldots,
\tag{5.1}
\]

and

\[
\boxed{
R_2:=\frac{H(F_2)}{I(F_2)-1}
>6.521850763518463531668608228451477683404661344.
}
\tag{5.2}
\]

Most importantly, the sign comparison is exact-rational:

\[
\boxed{
R_{2,\mathrm{lower}}-R_{1,\mathrm{upper}}
>
0.00000067985985108803493602942217815720069200998516.
}
\tag{5.3}
\]

The checker also asserts the coarser rational bound

\[
R_{2,\mathrm{lower}}-R_{1,\mathrm{upper}}>6.7\times10^{-7}.
\]

Thus this is a rigorously larger balanced excess ratio, not a floating-point tie or finite-search observation.

Because `F_2` is balanced, standard balanced self-composition of `F_2` yields finite Boolean functions whose ordinary `H/I` ratios approach `R_2`. Consequently

\[
\boxed{
C_{FEI}
\ge
6.521850763518463531668608228451477683404661344\ldots
}
\tag{5.4}
\]

with the displayed value understood as the certified lower endpoint from this construction. This improves the preceding `6.5218500836586...` floor.

## 6. Direct refutation of the current PRIME-GATE-LIFT candidate

The fleet02/B17 successor candidate fixed the center cap at the previous certified balanced value `L_*` and proposed proving the corresponding lifted gate inequality on every composition-prime gate.

At uniform input bias, a balanced gate reduces (1.1) exactly to

\[
H(G)\le \Gamma(1/2)[I(G)-1].
\tag{6.1}
\]

For `G=F_2`, (5.2) contradicts (6.1) whenever

\[
\Gamma(1/2)\le L_*
=6.521850083658612443633672199029299526203969334\ldots.
\]

Therefore the exact current candidate is false. Moreover, fleet02/B17's cocycle theorem applies: if `F_2` is functionally decomposable, at least one composition-prime factor must itself violate the corrected candidate. Hence the failure cannot be repaired by restricting the same cap to prime gates.

For the old `C_0=6.4548` reference potential, any purely quadratic scalar lift must now satisfy at least

\[
\boxed{
a\ge4(R_2-C_0)
>0.268203054073854126674432913805910733618645376.
}
\tag{6.2}
\]

If instead one anchors at the rigorously certified read-once cap `6.4573`, the corresponding floor is

\[
\boxed{
\lambda\ge4(R_2-6.4573)
>0.258203054073854126674432913805910733618645376.
}
\tag{6.3}
\]

These are lower bounds on this scalar-lift strategy, not upper bounds for FEI.

## 7. A useful exact iteration identity

The construction suggests an iterative lower-bound transformation. Put

\[
K(b)=H_{core}(b)+\alpha[-\phi(b^2)+16(1-b^2)],
\qquad \alpha=\frac9{256},
\qquad B=\frac{257}{256}.
\]

If a balanced gadget has excess ratio `R=H/(I-1)`, influence `I`, and chosen singleton coefficient `c`, first take its fourth self-composition and then apply the nine-host shared-core transform. The new ratio `R'` obeys exactly

\[
\boxed{
R'-R
=\frac{K(c^4)-\frac{133}{128}R}
       {\alpha I^4+B}.
}
\tag{7.1}
\]

The chosen core singleton for the next round is

\[
\boxed{c'=\frac{57}{256}+\frac{c^4}{256}.}
\tag{7.2}
\]

Equation (7.1) is algebraic and shows that the **sign** of the next improvement is independent of the current influence; only `R` and the chosen singleton coefficient matter. This may be useful for turning the one-step improvement into an analytically controlled limiting family. I do **not** claim here that every later step has been rigorously certified or that the limiting value is optimal.

## 8. Old and new missing implications

**Old missing implication:** prove `PRIME-GATE-LIFT` at the previous cap `L_*`, i.e. prove the corrected gate inequality for every composition-prime gate and every product bias after the minimal lift forced by the previous 162-bit lower-bound construction.

**Result:** `CANDIDATE_REFUTED`. The new source-valid balanced Boolean construction has excess ratio strictly larger than `L_*`; by the gate cocycle, a composition-prime violating factor exists if the displayed gate itself decomposes.

**New first missing implication:** one must either

1. raise/recompute the universal potential envelope so that its center is at least the new certified lower endpoint in (5.4), then prove its all-prime/all-bias gate inequality; or
2. construct a different finite-cap universal potential/induction whose compensating terms survive the shared-coordinate graft and the known half-band/crossing obstructions.

The recursive identity (7.1) should be analyzed before fixing another candidate at the newest finite construction, because another shared-core round may force a further increase.

This is a lower-bound/candidate-elimination result, **not** a proof that a finite universal FEI constant exists. Full FEI remains OPEN.

## 9. Reproduction and privacy boundary

The exact checker is `CHECKER.py`; `CHECK_OUTPUT.txt` records the successful run. It verifies the external source hash, exact influences, exact singleton coefficient, exact self-composition identities, the second shared-graft influence, and the strict entropy-ratio gain with rational interval arithmetic. Finite computation is used only to certify explicit rational/logarithmic quantities in a construction whose Booleanity and Fourier formulas are proved symbolically above.

Scoped privacy/secret review: the committed artifacts contain mathematical source data, hashes, formulas and sanitized provenance only. They contain no credentials, scheduler identifiers, machine paths, unrelated private transcripts, paid-compute instructions, permission changes, email/Drive actions, or public-posting instructions.
