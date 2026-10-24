# account03/B12 — a 10-input genuine balanced gate refutes AND-extremality

**Outcome:** `CANDIDATE_REFUTED`. Full uniform-cube FEI remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. The live natural-language owner control superseded the older B12 spectral-code duty for this invocation and instructed the FEI fleet to converge on the all-gate margin claim: prove AND/decomposable extremality or produce a Boolean gate asking strictly more margin.

## 1. Exact candidate and peer result consumed

The current gate programme fixes a symmetric base potential with

\[
C_0=\Gamma(1/2)=6.4548
\]

and studies the correction \(\Gamma_c(z)=\Gamma(z)+c z(1-z)\). For a gate \(G\) at biases \(p\), if \(D_G\) denotes right side minus left side of the all-gate inequality, adding the quadratic correction changes the defect by

\[
c\,[I(G;p)/4-p_{out}(1-p_{out})].
\]

I consumed the completed other-account result

`proofnet24/P03-fei/fleet-2026-09-21/account01/B14/20260922T0044Z-balanced-gate-margin-refutation/REPORT.md`, blob `776ade5c2e2017844785b09ab7af50c7eaf54c03`.

Its exact balanced-uniform identity is: for every balanced Boolean gate with \(I>1\), evaluated at \(p_i=1/2\),

\[
\boxed{c_G=4\left(\frac{H(G)}{I(G)-1}-C_0\right).}
\tag{1}
\]

The peer applied (1) to the full 18-input Numaro seed. Here I apply the same identity to an explicit **10-input coordinate restriction** of that seed, reducing the obstruction from arity 18 to arity 10 and checking that the restricted gate is genuinely non-read-once.

The parent seed is reconstructed source-exactly from

`proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260921T181108Z-numaro-magnitude-flow-certificate/check_numaro_magnitude_flow_certificate.py`, blob `df90e544f471b9053aa864522d64302d0c8a3f9e`, whose parent truth-table SHA-256 is

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

## 2. The explicit 10-variable restriction

Use the parent coordinate order `0,...,17`. Fix

\[
(x_9,x_{10},x_{11},x_{12},x_{13},x_{14},x_{15},x_{16})
=(0,0,0,1,1,0,1,1),
\]

and leave coordinates

\[
0,1,2,3,4,5,6,7,8,17
\]

free, in that local order. The resulting 1024-entry truth table has SHA-256

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`.

The exact checker verifies:

* balance: 512 values of each sign;
* monotonicity in every one of the ten live coordinates;
* every coordinate is essential;
* exact influences

\[
\left(\frac{29}{128},\frac{29}{128},\frac{29}{128},\frac{29}{128},
\frac{29}{128},\frac{29}{128},\frac{49}{256},\frac{29}{128},
\frac{29}{128},\frac1{256}\right),
\]

so

\[
\boxed{I(G)=\frac{257}{128}.}
\tag{2}
\]

It also exhausts all 511 canonical nontrivial bipartitions of the ten variables. For no partition do the true cells form a Cartesian rectangle (an AND root), and for no partition do the false cells form a Cartesian rectangle (an OR root). Because the gate is monotone and every variable is essential, any read-once AND/OR/NOT representation could be De-Morganized to a monotone read-once AND/OR representation and would have such a root partition. Therefore this gate is **GENUINE**, not DEGENERATE or READONCE in the gate programme's classification.

## 3. Exact entropy enclosure and margin

The integer Walsh absolute-value histogram, with zero coefficients omitted, is

```text
4:337, 8:48, 12:108, 16:28, 24:32, 28:18, 32:34, 36:36,
40:24, 48:8, 56:8, 72:8, 80:16, 84:12, 96:8, 112:4,
196:1, 232:8.
```

Using a rational atanh-series enclosure for every logarithm, the checker proves

\[
6.509836127588151479
< H(G) <
6.509836127588151480.
\tag{3}
\]

Together with (2),

\[
\boxed{
\frac{H(G)}{I(G)-1}>6.459372281637855731.
}
\tag{4}
\]

Applying the consumed identity (1) gives the rigorous lower bound

\[
\boxed{c_G>0.018289126551422926.}
\tag{5}
\]

The current fine-candidate AND search reports `0.0043974201`; (5) is more than `4.1590582968` times that number. More importantly, the already proved read-once interval certificate at the same base cap \(C_0=6.4548\) verifies **all AND constraints with \(c=0.01\)**. At a balanced-uniform gate, (1) depends only on \(C_0\), not on the off-centre shape of the base potential. Since

\[
0.018289126551422926>0.01,
\]

this ten-input gate asks for strictly more quadratic margin than the globally certified AND family does. This is a rigorous refutation of AND/decomposable extremality for the read-once potential programme, not merely a comparison with a floating-point AND search.

Equivalently, the witness exceeds the \(c=0.01\) gate threshold by a certified entropy amount

\[
H(G)-(I(G)-1)(C_0+0.01/4)
>0.002088471338151479.
\]

(The executable output also records the larger excess `0.003500058852018666` over the finer search threshold `c=0.0043974201`.)

## 4. What is refuted, and what is not

**Old decisive implication:** the all-gate quadratic margin for the read-once base potential is maximized by a decomposable/two-input-AND constraint.

**Status:** **REFUTED**. The explicit genuine arity-10 balanced monotone gate above needs \(c>0.0182891\), while the complete AND family is certified at \(c=0.01\).

This does **not** refute FEI. The witness itself has moderate \(H/I\), and the conclusion concerns the attempted universal extension of the read-once potential. Full FEI remains **OPEN**.

**Replacement obligation:** any all-gate potential must depart from the read-once fixed-point candidate (or raise/reprice its balanced cap) enough to survive balanced gates. The account01/B14 identity shows that the balanced-uniform slice already encodes \(H/(I-1)\), so merely searching higher gate arity with the unchanged read-once potential is no longer a plausible proof route.

**Next recipient:** `account03/B18` (B lead), with `account01/B14` as the direct peer whose decisive identity was strengthened here. The next full-FEI implication is to choose a replacement universal Shannon/potential statement that survives this 10-input gate and the larger certified balanced seeds, and then prove a finite dimension-independent bound rather than an AND-extremality claim.

## 5. Reproducibility

`check_arity10_gate_refutation.py` reconstructs the parent from the inherited exact slices, checks both truth-table hashes, proves balance/monotonicity/essentiality, rejects every possible read-once root partition, recomputes the exact influences and Walsh histogram, and uses rational logarithm enclosures for (3)--(5). The exact committed code was executed in this invocation and returned `PASS`; `check_output.txt` records the output.

No novelty or publication-priority claim is made. The Numaro seed and the balanced-margin identity are inherited; this run's mathematical contribution is the explicit certified arity-10 genuine restriction and the strict comparison with the globally certified AND margin.
