# B17 — complete unbalanced dyadic-output quarter/half arity-5 face is nonbinding

**Run:** `fleet03-B17-20260922T100239Z-c35ac72e`  
**Role:** fleet03/B17, FEI adversarial constructions.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / FINITE_SLICE_EXCLUDED`. Full unrestricted FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and mathematical sources were consumed, but no authenticated native/cognitive brain retrieval or receiver-context result entered the mathematics.

## 0. Candidate version, old gap, and mechanism change


\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)\,
{\Gamma(p_i)+h_2(V_{p_i})\over V_{p_i}},
\qquad V_p=4p(1-p),
\tag{0.1}
\]

using the read-once value-iteration base candidate `cert_vi_h96k40_f4` at
\[
C_0=\Gamma_0(1/2)=6.4548.
\]
The comparable gate margin is
\[
c_G=-{D_G\over I(G;p)/4-p_{\rm out}(1-p_{\rm out})},
\tag{0.2}
\]
where \(D_G\) is right side minus left side in (0.1).  A positive larger value would threaten AND/decomposable extremality.

The previous B17 run deliberately killed a higher-even-moment repair hierarchy; repeating that route would violate the owner's convergence order.  This run therefore changes mechanism back to the owner's direct arity-5 falsification target.

## 1. Consumed cross-account result

I consume fleet04/B17's completed report

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B17/20260922T051537Z-quarter-half-arity5/REPORT.md`

(report blob `0da09626867e2eb621e8809332289a3692220115`).  It exactly enumerates the balanced slice
\[
(p_y,p_1,p_2,p_3,p_4)=(1/4,1/2,1/2,1/2,1/2),\qquad p_{\rm out}=1/2,
\]
proves that its worst positive-currency gate has strongly negative comparable margin, and names **unbalanced output on the same quarter/half input geometry** as the next exact adversarial target.

I apply that result rather than repeating it: the present calculation closes every remaining output bias on this face for which the read-once potential is source-exact from an AND-chain dyadic point.

## 2. Exact reduction for the unbalanced quarter/half face

Let \(y\) have bias \(1/4\) and let \(x_1,\ldots,x_4\) be unbiased.  Write the two four-bit restrictions of \(G\) as masks \(G_0,G_1\), with positive-row counts \(k_0,k_1\), and let \(a_T,b_T\) be their unnormalised integer Walsh sums.  Exactly as in the consumed peer slice, every full biased spectral mass is rational with denominator \(4096\):

\[
P(T)={\bigl(3a_T+b_T\bigr)^2\over4096},\qquad
P(T\cup\{y\})={3\bigl(b_T-a_T\bigr)^2\over4096}.
\tag{2.1}
\]

The output mass is
\[
p_{\rm out}={3k_0+k_1\over64}.
\tag{2.2}
\]
Define
\[
A={\operatorname{It}_y\over V_{1/4}}={4\over3}\operatorname{It}_y,
\qquad
B=\sum_{j=1}^4\operatorname{It}_{x_j}.
\tag{2.3}
\]
Since the four half-biased children contribute \(C_0\), while
\[
\Gamma_0(1/4)=C_0-2,
\]
the exact base defect at any source-exact dyadic output \(q=2^{-m}\) is
\[
\boxed{
D_G(q)=BC_0+A\bigl(C_0-2+h_2(3/4)\bigr)-\Gamma_0(q)-\widetilde H_G.
}
\tag{2.4}
\]
The dyadic value \(\Gamma_0(2^{-m})\) is not interpolated: it is the exact AND-chain slack
\[
\Gamma_0(2^{-m})=C_0 I(\mathrm{AND}_m)-H(\mathrm{AND}_m).
\tag{2.5}
\]
Thus every transcendental appearing here is a logarithm of an exact rational spectral mass; there is no arbitrary spectral law and no candidate interpolation error.

For \(q\in\{1/64,1/32,1/16,1/8,1/4\}\), the count constraint (2.2) leaves respectively
\[
\begin{array}{c|l}
q&(k_0,k_1)\\ \hline
1/64&(0,1)\\
1/32&(0,2)\\
1/16&(0,4),(1,1)\\
1/8&(0,8),(1,5),(2,2)\\
1/4&(0,16),(1,13),(2,10),(3,7),(4,4),(5,1).
\end{array}
\tag{2.6}
\]

## 3. Complete enumeration theorem

The four half-biased coordinates have the full cube automorphism group of size \(4!2^4=384\).  For each row of (2.6), `CHECK.py` canonicalises \(G_0\) under this simultaneous action and enumerates **every** \(G_1\) of the required weight.  This covers

\[
\boxed{10,857,979}
\]
raw Boolean gates by
\[
\boxed{155,935}
\]
orbit representatives.

At 80-decimal precision, using the exact integer spectral numerators before logarithms, the result is:

| output \(q\) | raw gates | orbit reps | smallest strictly positive \(D_G\) | largest \(c_G\) away from the zero-defect subcube cases |
|---:|---:|---:|---:|---:|
| \(1/64\) | 16 | 16 | none: every row is an AND-chain subcube | none |
| \(1/32\) | 120 | 120 | \(0.403425\) | \(-7.247494736842105\ldots\) |
| \(1/16\) | 2,076 | 1,836 | \(0.153425\) | \(-2.3104\) |
| \(1/8\) | 97,158 | 17,718 | \(0.05685\) | \(-0.72768\) |
| \(1/4\) | 10,758,609 | 136,245 | \(0.267125\) | \(-2.137\) |

Hence for every positive-currency gate in all five unbalanced dyadic slices,
\[
\boxed{D_G\ge0\quad\text{and therefore}\quad c_G\le0.}
\tag{3.1}
\]
Every zero-defect positive-currency orbit representative is a **coordinate subcube indicator**, i.e. a decomposable AND/OR/literal chain (possibly with free/dummy coordinates).  The sole zero-currency row at output \(1/4\) is the literal \(y\), also decomposable.  Thus no non-subcube Boolean gate on these slices even asks for a positive quadratic margin, let alone a margin exceeding the live two-input AND floor.

Output negation preserves \(H\), \(I\), the symmetric potential values and the margin, so the same theorem holds for the mirror outputs
\[
63/64,\ 31/32,\ 15/16,\ 7/8,\ 3/4.
\tag{3.2}
\]
Combining (3.1)-(3.2) with the consumed fleet04/B17 balanced theorem closes the entire **dyadic-output quarter/half face**
\[
p=(1/4,1/2,1/2,1/2,1/2),
\]
for output masses
\[
\{1/64,1/32,1/16,1/8,1/4,1/2,3/4,7/8,15/16,31/32,63/64\}.
\tag{3.3}
\]
The balanced row is peer mathematics and is not silently promoted to an independent recertification here.

## 4. Exact worst non-subcube quarter-output witness

The closest non-subcube row at \(p_{\rm out}=1/4\) occurs for branch masks
\[
G_0^+=\{0,1,2\},\qquad G_1^+=\{0,1,2,4,5,6,7\},
\]
represented by masks `7` and `247`.  Its spectral mass numerators over \(4096\) have histograms
\[
\text{no-}y:\quad64^{12},256^2,1024^2,
\qquad
y\text{-layer}:\quad192^4,0^{12}.
\]
Therefore
\[
\widetilde H_G={15\over4}-{3\over16}\log_2 3,
\qquad
A={1\over4},\qquad B={17\over16},
\tag{4.1}
\]
and the logarithms cancel in (2.4):
\[
D_G={5\over16}C_0-{7\over4}=0.267125.
\tag{4.2}
\]
Its Poincare currency is \(1/8\), so
\[
\boxed{c_G=14-{5\over2}C_0=-2.137.}
\tag{4.3}
\]
This exact witness confirms that the finite margin gap is not an artefact of comparing incomparable defects across arities.

## 5. What this changes and what it does not

**Old missing implication.** After the complete balanced one-quarter and two-quarter arity-5 slices, could an unbalanced output on the simplest asymmetric quarter/half input geometry produce the first positive genuine arity-5 margin?

**New proved/self-checked inference.** No source-exact dyadic output on that geometry does.  Every covered positive-currency gate has \(c_G\le0\), and equality occurs only on decomposable coordinate-subcube gates.

**Replacement obligation.** Another sweep of dyadic outputs on this geometry is now dead.  The nearest genuinely new falsification target is the non-dyadic output row \(p_{\rm out}=3/8\) (and its mirror \(5/8\)) using the committed source-exact value of the read-once candidate there, or a genuinely non-dyadic multi-input bias deformation.  If that also remains nonbinding, the useful proof direction is to explain analytically why the zero-defect locus on this face is exactly the decomposable subcube locus rather than continue enumerating adjacent dyadic rows.

**Next recipient.** `fleet04/B17` for continuation of the arity-5 adversary, with `fleet03/B18` for all-gate integration.  This report directly consumes the former's balanced quarter/half theorem.

**Implication to full FEI.** This is a finite-face exclusion that strengthens the observed decomposable/AND extremality pattern.  It does not construct a universal potential on all biases and all arities and therefore does **not** prove FEI.

## 6. Verification

`CHECK.py` is standard-library only.  It constructs the exact four-bit Walsh data, the complete 384-element automorphism group, all required branch masks, the exact rational spectral numerators (2.1), exact influences/currency, 80-decimal logarithmic evaluation, the full coverage counts, and the coordinate-subcube classification of every zero-defect positive-currency row.  It aborts if any nonzero defect is not strictly positive by more than `1e-40`.

Executed checker SHA-256:

`6f677712810d1a0866653bac4b7caac0b6c18303e2346b2f8f519c27c8c32b8f`

Captured PASS output SHA-256:

`1b4f187190a97f3f668739d3883424ce6757364393b8e830c9650c859c173404`

The enumeration and rational spectral construction are exact; the transcendental comparison is an 80-decimal self-check, not a formal proof assistant or independent interval package.  The smallest positive defect is `0.05685`, so the sign is separated from numerical zero by an enormous margin relative to the working precision.  No novelty or publication-priority claim is made.
