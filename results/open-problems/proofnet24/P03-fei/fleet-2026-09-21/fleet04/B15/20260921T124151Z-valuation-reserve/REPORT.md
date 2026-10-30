# B15 — tensor collision is exactly valuation-reserve transfer

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval/context or isolated model evaluator was used in this mathematics.  
**Route:** unequal-magnitude spectral packets / arithmetic remainder, continuing the spectral-lattice, centroid/carry, adjacent-boundary, mesh-infection, and remote-gap handoffs.  
**Novelty:** no publication-priority claim is made.

## 1. What moved

The preceding fleet04/B15 run left a bilateral arbitrary-selector crossing inequality as the next target. It proved such a bound only for an integral-selector catalyst with two packet magnitudes, and exhibited a family showing that a seed-only payment cannot be dimension-free when the catalyst exponent gap grows.

There is a simpler exact conservation law that removes the selector and integrality hypotheses entirely.

For every Boolean function `f`, use the inherited magnitude-packet notation

\[
R(f)=\sum_a p_a r_a,
\qquad
D(f)=\sum_a p_a\log_2(1/b_a),
\]

where `p_a` is the squared spectral mass of the packet of magnitude `a`, `r_a` is the minimum 2-adic valuation of its signed packet Walsh transform, and `b_a=a2^{r_a}` is its primitive physical mesh. The spectral-lattice continuation proved the exact identity

\[
\boxed{H(f)=2R(f)+2D(f).}
\tag{1}
\]

The centroid theorem also gives

\[
\boxed{R(f)\le 2\mathfrak I(f)\le 2I(f).}
\tag{2}
\]

## 2. Exact tensor conservation theorem

### Theorem A — valuation-reserve conservation

Let `f` and `g` be arbitrary Boolean functions on disjoint variable sets. Then

\[
\boxed{
D(f\otimes g)-D(f)-D(g)
=R(f)+R(g)-R(f\otimes g).
}
\tag{3}
\]

Equivalently,

\[
\boxed{
(R+D)(f\otimes g)=(R+D)(f)+(R+D)(g).
}
\tag{4}
\]

No plateaued, selector, lattice-valued, equal-mass, adjacent-gap, or automatic-integrality hypothesis is present.

### Proof

The squared Fourier distribution of a tensor product is the product of the two squared Fourier distributions. Hence Fourier entropy is additive:

\[
H(f\otimes g)=H(f)+H(g).
\tag{5}
\]

Apply the universal exact decomposition (1) to `f`, `g`, and `f\otimes g`, divide by two, and rearrange. This proves (3) and (4). QED.

The interpretation is exact: **every positive tensor-collision increase of the arithmetic remainder `D` is paid by an equal loss of valuation reserve `R`; every gain of `R` is an equal decrease of `D`.** The collision is a transfer between the two ledgers of the fixed additive quantity `H/2`, not creation of new joint arithmetic cost.

## 3. Universal bilateral collision payment

### Corollary B

For arbitrary Boolean `f,g`,

\[
\boxed{
D(f\otimes g)-D(f)-D(g)
\le R(f)+R(g)
\le 2I(f)+2I(g).
}
\tag{6}
\]

The first inequality is immediate from `R(f\otimes g)\ge0`; the second is (2).

More generally, for Boolean factors `f_1,\ldots,f_m` on disjoint variable sets,

\[
\boxed{
D\!\left(\bigotimes_{j=1}^m f_j\right)-\sum_jD(f_j)
=\sum_jR(f_j)-R\!\left(\bigotimes_{j=1}^m f_j\right)
\le 2\sum_j I(f_j).
}
\tag{7}
\]

Thus the bilateral crossing target from the remote-gap run has coefficient `2` in complete generality, without the integral-selector hypothesis.

## 4. Rigorous obstruction to the tensor-collision subroute

The conservation law also shows why controlling tensor mesh infection cannot by itself close unrestricted FEI.

Total influence is additive under independent tensor products:

\[
I(f\otimes g)=I(f)+I(g).
\tag{8}
\]

Together with entropy additivity,

\[
\frac{H(f\otimes g)}{I(f\otimes g)}
=
\frac{I(f)}{I(f)+I(g)}\frac{H(f)}{I(f)}
+
\frac{I(g)}{I(f)+I(g)}\frac{H(g)}{I(g)}
\tag{9}
\]

when both influences are positive, with the degenerate cases interpreted in the evident way. Therefore the tensor-product FEI ratio is a weighted average of the factor ratios and cannot exceed their maximum.

Consequently, even spectacular positive `D` mesh infection under tensoring cannot create a worse FEI ratio: it must be exactly offset by loss of `R`. A universal proof strategy that spends its main effort paying positive tensor-collision `D` while discarding the simultaneous negative `R` movement is structurally lossy.

This is **not** an obstruction to FEI. It is an obstruction to treating tensor-collision growth of `D` as the remaining universal difficulty in isolation.

## 5. Exact checks

A standard-library checker recomputes integer Walsh transforms, packet valuations, reserves, and influences.

For the previously exhibited positive-collision example

- `f`: 3-bit positive mask `0x37`;
- `g`: 4-bit positive mask `0x5f75`;

it obtains

\[
R(f)=0,\qquad R(g)=\frac38,\qquad R(f\otimes g)=\frac{21}{128},
\]

and hence from (3)

\[
\Delta D=\frac38-\frac{21}{128}=\frac{27}{128},
\]

exactly matching the earlier direct collision computation.

A second example has nonzero reserve in both factors:

- `f`: 4-bit positive mask `0x6094`;
- `g`: 4-bit positive mask `0x0ee7`;

with

\[
R(f)=\frac38,\qquad R(g)=1,\qquad R(f\otimes g)=\frac{271}{256},
\]

so

\[
\Delta D=\frac{81}{256}.
\]

The checker also scans all `65,536` ordered 3-bit by 3-bit Boolean pairs and finds no positive `D` defect there. This finite scan is only a sanity check and is not used in the proof.

Checker SHA-256:

`c7635eaf4460a9abcb1ae8076870762c2bb2fa7b9b3dc31ece55c50f210cea0c`

Verification-output SHA-256:

`762b83eae1156a9c959dbccfdf4e0c15403d5601f0b95c1c549b6c0c60e0962e`

## 6. Relation to the current literature

A bounded primary-source check on 21 September 2026 found no unrestricted FEI proof. O'Donnell--Tan's composition theorem is directly consistent with the tensor perspective: independent/compositional constructions preserve FEI control under appropriate hypotheses rather than manufacture an ever-worse ratio. González--MacManus--Pereyra instead emphasize a restriction/stopping-tree entropy decrement as a possible route to the full conjecture. Potapov's 18 September 2026 result proves the conjecture for plateaued functions with sharp class constant four, not for arbitrary unequal-magnitude spectra. Xiao Han gives a general bound with an additional influence-profile entropy term. None of these sources is used to claim novelty for Theorem A.

## 7. Precise next obligation

The tensor-collision crossing problem is now algebraically closed at the level needed for a bilateral influence payment, but full FEI remains OPEN.

The next arithmetic target should be a **non-product operation**, especially restriction. Since `R+D=H/2`, for a coordinate restriction one has the exact joint decrement

\[
(R+D)(f)-\frac12\bigl[(R+D)(f^{+})+(R+D)(f^{-})\bigr]
=\frac12\Delta_i H.
\tag{10}
\]

The universal problem is therefore not to control `D` alone, but to select a coordinate whose **joint valuation/free-energy decrement**, with all cross-packet credits retained, is paid by that coordinate's influence. This is the restriction analogue of the conservation law and interfaces directly with the stopping-tree programme.

A decisive next B15 step is to derive a packet-exact decomposition of the left side of (10) that retains the packet KL, local-geometry, and coordinate-incompatibility credits instead of dropping them. If that decomposition yields no dimension-free selected-coordinate payment, the target should be refuted by an explicit Boolean family rather than hidden behind a loose `D` estimate.

### Scope summary

**PROVED here:** exact tensor valuation-reserve conservation (3); universal bilateral tensor-collision bound (6); multi-factor form (7); tensor FEI-ratio weighted-average obstruction (9).

**NOT proved:** a universal bound `D(f)\le C I(f)`; a restriction-level payment; unrestricted FEI.
