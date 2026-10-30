# B15 — the published balanced n=18 seed refutes universal extremality of the read-once Gamma

**Status:** `CANDIDATE_REFUTED` at the stated scope. Full uniform-cube FEI remains **OPEN / NOT PROVED**.

**Execution label:** `WITHOUT_VERIFIED_BRAIN`. Authenticated GitHub sources were read, but no authenticated mathematical/cognitive brain retrieval was delivered into the reasoning context.

## 1. Exact candidate version and prior missing implication

Current owner target: the all-gate inequality

\[
\Gamma(p_{\rm out})+H_t(G;p)\le \sum_i \operatorname{It}_i(G;p)\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}}
\tag{G}
\]

with the **read-once value-iteration potential** `cert_vi_h96k40_f4`, whose cap is
\(C_0=\Gamma(1/2)=6.4548\). Source candidate: `proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`, blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5` at scientific source commit `d866d0c009f65e37f58623b76de730c146a13e5e`.

The decisive missing implication was:

> the same read-once \(\Gamma\) satisfies (G) for every Boolean gate; equivalently, no gate asks for a margin \(c_G\) larger than the two-input AND constraint.

The gate code defines

\[
c_G(p)=\frac{-D_G(p)}{I(G;p)/4-p_{\rm out}(1-p_{\rm out})},
\]

and the constant is controlled by the **maximum**, not the minimum, of \(c_G\). Thus the live owner's phrase “minimum of \(c_G\)” has the inequality direction reversed relative to the source definition and `gates5.py`; the accompanying instruction “find a gate with \(c_G\) above the AND's” has the correct direction.

## 2. Named other-account result consumed

Consumed peer artifact:

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B15/20260921T130641Z-carry-congruence-n18-profile/REPORT.md`, blob `83f5f9a851b85a31f3ca03524f0ce589dc47d448`.

For Numaro's published balanced monotone 18-variable seed it records, after exact truth-table hash match

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`,

that

\[
I(G)=\frac{261}{128},
\]

and the certified entropy interval

\[
6.776605309005978082519790221891882314787235038
\le H(G)\le
6.776605309005978082519790221891882314787235039.
\tag{1}
\]

The current FEI handoff already notes that this seed yields the published lower bound
\(C_{\rm FEI}>6.521845710923046575\). This is external prior work, not a new lower-bound claim.

## 3. New exact inference: balanced gate margin = recursive-composition excess

### Proposition

Let \(G\) be any balanced Boolean gate, feed all its inputs independent unbiased fresh variables, and assume \(I(G)>1\). Let \(\Gamma\) be any symmetric potential with \(\Gamma(1/2)=C_0\). Then at the uniform bias vector

\[
\boxed{
c_G(1/2,\ldots,1/2)
=4\left(\frac{H(G)}{I(G)-1}-C_0\right).\ }
\tag{2}
\]

Moreover, if \(G\) is recursively self-composed on disjoint fresh blocks, then

\[
\boxed{
\lim_{m\to\infty}\frac{H(G^{\circ m})}{I(G^{\circ m})}
=\frac{H(G)}{I(G)-1},
}
\tag{3}
\]

so the uniform gate margin is exactly four times the asymptotic FEI-ratio excess of recursive self-composition over the cap \(C_0\).

### Proof

At uniform input bias, \(V_{1/2}=1\) and \(h(V_{1/2})=0\). Because the output is balanced, \(p_{\rm out}=1/2\), and because the gate itself is evaluated on fresh unbiased variables, its biased spectral entropy is its ordinary spectral entropy and

\[
\sum_i \operatorname{It}_i(G;1/2)=I(G).
\]

Therefore the defect in (G) is exactly

\[
D_G=C_0 I(G)-H(G)-C_0=C_0(I(G)-1)-H(G).
\tag{4}
\]

The Poincare margin denominator is

\[
I(G)/4-p_{\rm out}(1-p_{\rm out})=(I(G)-1)/4.
\tag{5}
\]

Substituting (4)-(5) into the definition of \(c_G\) gives (2).

For balanced disjoint self-composition, the standard composition identities reduce to

\[
I_{m+1}=I(G)I_m,\qquad H_{m+1}=I(G)H_m+H(G),
\]

starting from a fresh variable \((I_0,H_0)=(1,0)\). Hence

\[
I_m=I(G)^m,
\qquad
H_m=H(G)\sum_{j=0}^{m-1}I(G)^j,
\]

and division by \(I_m\), followed by \(m\to\infty\), yields (3). QED.

This proposition is independent of packet integrality and does not discard any negative information credit: it is an exact specialization of the common versioned gate/Shannon inequality itself.

## 4. Apply the proposition to the published n=18 seed

From (1) and \(I-1=133/128\),

\[
6.5218457109230465756581439729485784683666622922105\ldots
\le \frac{H}{I-1}
\le
6.5218457109230465756581439729485784683666622931729\ldots.
\]

Thus for the current read-once candidate \(C_0=6.4548\),

\[
\boxed{
0.2681828436921863026325758917943138734666491688421\ldots
\le c_G(1/2^{18})
\le
0.2681828436921863026325758917943138734666491726917\ldots
}
\tag{6}
\]

where `1/2^18` means the 18-component uniform bias vector, not the scalar \(2^{-18}\).

The current two-input AND candidate floor is approximately

\[
c_{\rm AND}=0.0043974201.
\]

Therefore this explicit 18-input balanced gate asks for a margin at least

\[
\frac{c_G}{c_{\rm AND}}>60.9864
\]

times the AND margin.

The uncorrected defect is

\[
D_G\le -0.069664684005978082519790221891882314787235038,
\]

and even after adding the full current AND margin \(c_{\rm AND}z(1-z)\), the gate defect remains approximately

\[
-0.068522385425314020019790221891882314787235038<0.
\]

Finally,

\[
C_0+\frac{c_G}{4}=\frac{H(G)}{I(G)-1},
\]

so the gate calculation recovers exactly the same asymptotic recursive-composition lower bound already supplied by the published seed. This equality is a consistency identity, not a new external lower-bound claim.

## 5. What is refuted, and what is not

**REFUTED:** the current read-once fixed-point potential \(\Gamma\) at cap 6.4548 is a universal all-gate potential. The statement that the two-input AND is extremal among **all** Boolean gates for this \(\Gamma\) is false. Owner job (2), “find a gate and bias vector with \(c_G\) above the AND's,” is therefore already fulfilled by a source-valid gate at arity 18 and uniform bias; an arity-5 search is not needed to falsify the universal claim.

**NOT REFUTED:** the gate reformulation of FEI. It asks for the existence of *some* symmetric nonnegative \(\Gamma\) with a finite cap. The failed object is this particular read-once \(\Gamma\), not the reformulation and not FEI.

**OPEN:** full FEI with a dimension-independent finite constant.

## 6. Replacement obligation / next attack

The common all-gate target must be restarted at the correct scale. Any universal potential must have

\[
\Gamma(1/2)\ge C_{\rm FEI}>6.521845710923046575
\]

or otherwise compensate the n=18 gate through a different shape while still satisfying its cap constraint. The next mathematically useful question is therefore not “is AND extremal for the read-once \(\Gamma\)?” but:

> construct or characterize a new symmetric \(\Gamma\) at cap \(C\ge6.521845710923046575\) that satisfies (G), or derive from (G) a necessary envelope operation whose fixed point can be tested on the n=18 gate and its recursive compositions.

`next_recipient`: `fleet03/B18` (Campaign-B lead), with the explicit instruction to supersede the read-once-Gamma universal candidate before integrating further B12/B15 Shannon work.

`applied_to_claim`: universal all-gate validity/extremality of the read-once fixed-point Gamma.

`remaining_implication`: existence of some finite-cap symmetric nonnegative Gamma satisfying (G) for every Boolean gate and every bias vector.

`full_problem_change`: one candidate is decisively eliminated; full FEI remains OPEN.
