# B14 — balanced-uniform gate margin identity and an 18-input refutation of AND extremality

**Outcome:** `CANDIDATE_REFUTED`. Full uniform-cube Friedgut–Kalai Fourier entropy-influence remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository sources were read directly; no native brain retrieval/runtime was used.

## 1. Live candidate and named peer result consumed

The live owner target asks whether, for the read-once potential with `C0 = Gamma(1/2) = 6.4548`, the gate margin

\[
c_G(p)=\frac{-D_G(p)}{I(G;p)/4-p_{out}(1-p_{out})}
\]

is universally maximized by a decomposable/two-input-AND constraint. The owner's falsification criterion is a genuine Boolean gate and bias vector with `c_G` above the AND margin.

I consumed the exact named other-account theorem

`proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260921T124438Z-support-deficit-balanced-equivalence/REPORT.md`, blob `040ed0078f4905b9b4a11e963f27a1e6dcc3ee8d`.

It proves, constant-for-constant, that

\[
C_{FEI}=\sup_{f\ balanced,\ I(f)>1}\frac{H(f)}{I(f)-1}.
\tag{1}
\]

I also consumed the source-exact balanced monotone 18-input Numaro seed as reconstructed in

`proofnet24/P03-fei/continuations/2026-09-21-three-hour-sprint/interactive/20260921T121509Z/SHARED_GRAFT_REPORT.md`, blob `11f0405c2869831a14eb6870636f182f52fff353`.

For that seed `g`, the report records

\[
I(g)=261/128
\]

and

\[
6.521845710923046575658143972948578468366662292
\le \frac{H(g)}{I(g)-1}
\le
6.521845710923046575658143972948578468366662293.
\tag{2}
\]

This 18-input seed is enough; the newer 162-input shared-graft improvement is not needed for the refutation below.

## 2. Exact balanced-uniform margin identity

Let `G` be any balanced Boolean gate and evaluate the all-gate inequality at uniform biases `p_i=1/2`.
Then `p_out=1/2`, `V_{p_i}=1`, `h(V_{p_i})=0`, and the biased quantities become the ordinary spectral entropy and total influence. Hence

\[
D_G=C_0 I(G)-C_0-H(G)=C_0(I(G)-1)-H(G).
\]

The Poincare denominator becomes

\[
I(G)/4-p_{out}(1-p_{out})=\frac{I(G)-1}{4}.
\]

Therefore, for every balanced `G` with `I(G)>1`,

\[
\boxed{
 c_G(1/2,\ldots,1/2)
 =4\left(\frac{H(G)}{I(G)-1}-C_0\right).
}
\tag{3}
\]

Combining (3) with the peer equivalence (1) yields the extended-real identity

\[
\boxed{
\sup_{G\ balanced} c_G(1/2,\ldots,1/2)
=4(C_{FEI}-C_0).
}
\tag{4}
\]

Thus the proposed global gate-margin extremality question already contains the full FEI constant on the balanced-uniform slice. It is not enough to inspect small arity or special named gates.

## 3. A genuine 18-input counterexample to AND extremality

Apply (3) to the 18-input balanced monotone seed `g` from (2). Using the certified lower endpoint,

\[
\boxed{
 c_g(1/2,\ldots,1/2)
\ge
0.268182843692186302632575891794313873466649168.
}
\tag{5}
\]

The owner's current quoted AND margin floor is

\[
c_{AND}=0.0043974201.
\]

Therefore

\[
\boxed{
\frac{c_g}{c_{AND}}>60.9864051178.
}
\tag{6}
\]

At `C0=6.4548` the corresponding gate defect is already strictly negative:

\[
D_g=C_0(I(g)-1)-H(g)
\le -0.0696646840059780825197902218918823147872350377812.
\tag{7}
\]

So the live statement "the two-input AND/decomposable gate is extremal for the current read-once potential" is decisively false. A search beginning at arity five is unnecessary for falsification: an explicit balanced monotone gate of arity 18 already exceeds the AND margin by more than a factor 60.

The stronger 162-input shared-graft witness gives an even larger certified margin, as independently recorded by account03/B13 in `20260922T003238Z-balanced-uniform-gate-slice`, but (5) is the smaller-arity obstruction.

## 4. Consequence for the current gate programme

If one tried to prove `c_G <= c_AND` for all gates with the present `C0`, then (4) would force

\[
C_{FEI}\le C_0+c_{AND}/4
=6.455899355025,
\]

contradicting the certified 18-input lower bound (2), already before the 162-input improvement.

Accordingly, the read-once fixed-point potential cannot be the universal all-gate potential at its present cap, and no proof of decomposable extremality for that candidate can exist.

This is an elimination result, **not** evidence that FEI itself is close to solved. The successor universal task is to prove finiteness of the balanced quantity in (1), or equivalently to construct a different all-gate potential whose cap is at least the current certified balanced lower bound.

## 5. Exact old/new missing implication

**Old missing implication:** prove that every Boolean gate has margin no larger than the decomposable/two-input-AND margin for the read-once potential.

**New result:** that implication is false. Equations (3)–(7) give a source-admissible 18-input balanced monotone counterexample.

**Replacement obligation:** obtain a dimension-independent upper bound on
\[
\sup_{f\ balanced}\frac{H(f)}{I(f)-1},
\]
which by the consumed theorem is exactly the full FEI constant. Any successor gate potential must first survive this balanced-uniform slice.

No novelty or publication-priority claim is made. The balanced equivalence and the 18-input seed are inherited; the new applied contribution is the exact margin identity (4) and the smaller-arity direct refutation of the live AND-extremality target.
