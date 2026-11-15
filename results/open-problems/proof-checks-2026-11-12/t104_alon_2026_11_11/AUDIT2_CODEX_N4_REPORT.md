# Referee report

**SOUND**

The dual proposition and the proof for every nonnegative weighted graph on four vertices are correct. I found no substantive gap. The sharp constant is 2/3, attained by the equal-weight three-edge star. The numerical check independently agrees with the proof; it is not used to establish the universal claim.

This report concerns N4_PROOF.md and the supplied text of Alon's paper. Detailed line-by-line findings and paper quotations are in LOG.md. Neither input was changed. No browsing, other agents, external code reuse, git operations or writes outside this folder were used.

## Verdict table

Line numbers refer to N4_PROOF.md.

| Statement | Verdict | Reason |
|---|---|---|
| Conjecture as stated, 5–8 | CORRECT | Same nonnegative weights, Specht Laplacian, whole-module minimum, dominance direction and constant as the paper. |
| Proposition 1, (b) implies (a), 20–22 | CORRECT | Sum with nonnegative weights, then bound the density-matrix expectation below by the least eigenvalue. |
| Proposition 1, (a) implies (b), 24–28 | CORRECT | Compact convex minimax applies and yields one density matrix valid at every simplex vertex. |
| Section 2(i), 35 | CORRECT | Sign Laplacian is 2W; every other block is bounded above by 2W times the identity. |
| Section 2(ii), 37–38 | CORRECT | CLR gives the assertion on connected support; positive semidefiniteness handles disconnected support. |
| Remaining dominance pair, 42–43 | CORRECT | The nontrivial partitions form the chain 31 > 22 > 211 > 1111. |
| Lemma 2: 211 identification and formula, 47–50 | CORRECT | Conjugate diagrams tensor with sign; the standard module is the sum-zero vertex space. |
| Lemma 2: 22 identification and formula, 50–53 | CORRECT | Quotient action on perfect matchings gives the standard S3 module and eigenvalues W ± D. |
| Theorem 3: equivalent inequalities, 55–58 | CORRECT | Direct substitution of Lemma 2 gives the claimed equivalence. |
| Support-function reduction to (*), 60–68 | CORRECT | The projection norm is correct and the chosen u bounds each fixed vector's weighted energy. |
| Coordinates, absolute values and ordering, 70–76 | CORRECT | All six differences are correct; taking matching maxima removes signs and coordinate permutations preserve feasibility. |
| Numbered inequality (1), 78 | CORRECT | pq+qr+rp <= p²+q²+r² = 1. |
| Numbered inequality (2), 79 | CORRECT | (p+q)² <= 2(p²+q²) <= 2. |
| Numbered inequality (3), 80–83 | CORRECT | The trigonometric maximum is 3; an independent quadratic-form calculation gives the same bound. |
| Case 1, 85 | CORRECT | Every lower bound is nonpositive, so u=0 works. |
| Case 2, 87–88 | CORRECT | Both lower coordinates dominate their bounds and the squared norm is (9/4)t_c² <= 1. |
| Case 3, 90–94 | CORRECT | Inequality (1) controls the first coordinate; (2) and (3) give the stated norm bound. |
| Star equality and optimality, 96 | CORRECT | Ordinary spectrum 0,1,1,4 gives block minima 2 and 3, with positive denominator. |
| Density-disc interpretation, 98–102 | CORRECT | Reflection expectations form the claimed disc; the scaling gives (*), and the single-edge computation is correct. |

There are minor wording qualifications, none affecting the theorem. The minimax proof should separate the vacuous n=1 case, since its weight simplex is empty. The informal “largest c” sentence should allow an infinite optimum when sigma=[n]. For complex density matrices the disc is the image of the Bloch ball; real density matrices themselves form the disc. Ratios require a positive denominator. “Piecewise linear” for the constructed state is understood on the normalised vector domain: the displayed formulas are piecewise affine in squared differences, and their constants can be replaced by multiples of sum_{i<j}(x_i-x_j)²=4.

## Paper comparison and theorem used

The supplied extraction loses Greek letters and relation glyphs. The following are quotations from the text as supplied, with its line numbers; missing mathematical symbols are not silently restored inside quotations:

- Lines 24–25: “Let G = ([n], wij) be a weighted graph with nonnegative weights. The Aldous conjecture, proved by Caputo, Liggett and Richthammer [2]”.
- Lines 30–37: “Here min(G,  ) means the minimum eigenvalue of the Laplacian matrix”, followed by “L(G,  ) =  ( wij(id - (ij)))” and the index “i<j”; the representation is identified as the irreducible representation or Specht module.
- Lines 273–275: “module, an R[Sn] module which realizes the corresponding irrep. It is equipped with an invariant inner product”.
- Lines 291–295: “The minimum eigenvalue is the minimum of this quotient:” followed by “min(G, ) = min RG,(f ).”
- Lines 64–65 identify the “standard dominance relation among partitions” through row-prefix sums.
- Lines 85–97 state “Conjecture 1.5”, the fraction 2/3, and its equivalent inequality for every weighted graph.
- Lines 113–115 explicitly include the case with standard partition [n-1,1] through the CLR theorem.

The reconstructed convention is sigma dominates tau when every row-prefix sum for sigma is at least the corresponding sum for tau. The more dominant partition is on the right-hand side of the comparison. The paper's standard-module statement and its star example independently fix this direction. The eigenvalue is the smallest eigenvalue including zero, not the smallest strictly positive eigenvalue. Complete quotations with the extraction damage are retained in LOG.md.

The precise CLR theorem used is equality of the spectral gaps of the interchange process and the single-particle random walk on a finite connected undirected weighted graph, with symmetric nonnegative rates and connected positive-rate support. Both generators use the same edge rates: a transposition occurs at rate w_ij, and the particle jumps from i to j at rate w_ij.

In the regular representation, the interchange Laplacian contains every nontrivial Specht block. Connected support leaves no kernel in those blocks, because its edge transpositions generate S_n. Its spectral gap is therefore the minimum of their least eigenvalues. The standard block already has minimum equal to the random-walk gap, so equality of the two gaps bounds every other block below by that value. For disconnected support the standard block's minimum is zero and the required inequality follows from positivity. Calling the disconnected zero a smallest positive eigenvalue would be incorrect; the note does not need to do that. I can confirm this theorem and its application from memory, and the supplied paper also states the needed block inequality explicitly. The original CLR article was not consulted.

## The two main proof checks

For Proposition 1, take the weight simplex Delta in R^{n choose 2} and the trace-one positive Hermitian matrices D on V_sigma. For n>=2 both are nonempty compact convex sets in finite-dimensional real spaces. The displayed f is continuous, linear in weights and affine in the density matrix. Equivalently replace its scalar constants by those constants times tr(rho) to obtain a bilinear extension. Thus

    min_{rho in D} max_{w in Delta} f(w,rho)
      = max_{w in Delta} min_{rho in D} f(w,rho).

For each w the inner minimum is nonpositive by (a) and the Rayleigh principle. Compactness attains the minimum on the left. Its minimizer is one rho for which every w has f<=0. Taking all simplex vertices gives all edge inequalities simultaneously. The proof does not choose a separate rho for each edge.

For Theorem 3, I checked each representation identification, each coordinate difference, and each norm calculation. Case 3 is the easiest place for a numerical constant error: the norm identity is exactly

    |u|² = (9/4)(t_b+t_c)² + (3/4)(t_c-t_b)².

Its hypotheses give 0<t_b+t_c<=1/3 and 0<=t_c-t_b<1, so the claimed upper bound holds. Independently, inequality (3) follows because (p+r)²+(p+q)² has matrix

    [2 1 1]
    [1 1 0]
    [1 0 1]

with eigenvalues 3,1,0. This verifies the tight upper bound 3 without the trigonometric argument.

The star equality is sufficient to prove optimality; the note does not claim an exhaustive equality classification. A single-edge graph also attains equality in the ordinary-Laplacian upper bound, but both compared minima vanish there, so it supplies no positive-denominator ratio.

## Independent numerical results

All numerical results below were produced by this command, run in this folder:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
nice -n 10 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 \
independent_check.py > numerical_output.txt
```

The sandbox refused the niceness adjustment with “setpriority: Operation not permitted”; Python nevertheless executed successfully. The check used one numerical thread, 0.604 seconds and 78.6 MiB peak resident memory. The script also imposes a 240-second wall alarm and a CPU limit below five minutes.

The code generates standard Young tableaux and Young's orthogonal adjacent-transposition matrices from contents. It forms every (ij) by a word in adjacent transpositions. It checks the Coxeter relations and the full irreducible character table on the five conjugacy classes. Dimensions are 1,3,2,3,1. Maximum Coxeter residual was 1.11e-16. No numerical code from elsewhere in the workspace was read or reused.

Seed: **261022151**. Tested **32,000 random graphs**, 4,000 from each of eight families: bounded dense weights, exponential weights, a Dirichlet distribution concentrated near sparse boundaries, two sparse distributions, log-uniform weights, graphs with one to three very large weights, and perturbed stars. Amplified weights reach approximately 1e8 times the baseline. Added all 64 unweighted supports and eight named graphs, for **32,072 total**. The named graphs include the star, path, triangle-plus-pendant and single edge.

For every graph, the code computes the minimum in all five partitions, including [4]. Each row below uses the same command above. Edge weights are ordered **(12,13,14,23,24,34)**. Minima were recomputed from 70-digit Young matrices using mpmath.

| sigma | tau | Smallest ratio | Weights where attained | lambda_sigma | lambda_tau |
|---|---|---:|---|---:|---:|
| 31 | 22 | 1 | (0,1,1,1,1,0), a four-cycle | 2 | 2 |
| 31 | 211 | 2 | (1,1,1,0,0,0), a star | 1 | 2 |
| 31 | 1111 | 3 | (1,1,1,1,1,1), K4 | 4 | 12 |
| 22 | 211 | 0.66666666666666666666666666666666666666666666666666666666666666667 | (1,1,1,0,0,0), a star | 3 | 2 |
| 22 | 1111 | 2 | (1,1,1,0,0,0), a star | 3 | 6 |
| 211 | 1111 | 1.5 | (1,1,1,1,1,1), K4 | 8 | 12 |
| 31 | 31 | 1 | (1,1,1,0,0,0) | 1 | 1 |
| 22 | 22 | 1 | (1,1,0,0,0,0) | 1 | 1 |
| 211 | 211 | 1 | (1,1,0,0,0,0) | 1 | 1 |
| 1111 | 1111 | 1 | (1,0,0,0,0,0) | 2 | 2 |

Reflexive pairs are included to cover non-strict dominance conventions. For numerical ties within 1e-12 the code keeps the first representative. This avoids replacing exact symmetric examples with last-bit noise. All reported minima have high-precision confirmation.

Weights are normalised to W=1 before double-precision diagonalisation. The maximum absolute disagreement with Lemma 2 on this scale was **2.74e-15**. Exact zero denominators are identified using the kernel for each of the 64 unweighted supports and excluded from ratios; their inequalities follow from positive semidefiniteness. The number of zero denominators was 4,439 for sigma=31, 2,730 for sigma=22, 2,355 for sigma=211 and 688 for sigma=1111. Positive denominators below 1e-9 and apparent violations trigger high-precision recomputation.

**No ratio below 2/3 - 1e-9 occurred.** No counterexample weights exist to save from this run. All sampled weights, including every sparse and extreme graph, are saved in sampled_graphs.npz. Machine-readable minima, graph identifiers, eigenvalues, resource measurements and library versions are in numerical_results.json; numerical_output.txt records the command output.

## What the paper already contains

I searched the full supplied text. It does not state a proof for every weighted graph at n=4. Its introduction, lines 106–118, lists complete graphs, quasi-complete graphs, existing Aldous-order cases and numerical tests on small unweighted graphs (up to seven vertices). Numerical tests do not prove the weighted assertion.

Theorem 1.4 gives only 1/n³, hence 1/64 at n=4. Theorem 4.4 gives 2/3 for quasi-complete graphs. A general four-vertex graph need not be quasi-complete under any relabelling: a connected quasi-complete graph has a universal vertex, whereas the four-vertex path does not. CLR does not cover the remaining pair 22,211 with constant 1, as the star ratio itself shows. The note's full assertion is therefore not an immediate specialisation of those stated comparison theorems.

The equality example is already present: Theorem 4.5, lines 740–765, with m=2 gives precisely tau=211, sigma=22 and the unweighted three-edge star, ratio 2/3. The partition [2^m] there means m parts equal to 2; the paper explains that convention in its footnote. The new part of this note is the universal weighted-four-vertex bound, not this sharpness example. This is a comparison with the supplied paper, not a claim of novelty relative to other literature.

## Limits of the review

The supplied extraction prevents literal verification of every lost Greek letter and relation glyph. The surrounding definitions, proofs and examples consistently fix the intended conjecture and its direction. No original PDF or external source was fetched, as instructed.

The note's historical numerical runs in Section 4 were not reproduced from their original code, and its separate n=5 numerical claims in Section 5 were not checked. Neither is needed for Proposition 1 or the n=4 proof. The independent run above replaces the historical numerical evidence for this review.

Overall verdict: **SOUND**.

Task: “You are refereeing a short mathematical note” — 2026-11-11, 07:25 +04 (Asia/Tbilisi).
