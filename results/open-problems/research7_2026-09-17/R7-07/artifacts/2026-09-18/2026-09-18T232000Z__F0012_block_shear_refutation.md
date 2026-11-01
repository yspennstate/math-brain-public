Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0012 — an explicit `2^{n^2/2+O(n)}` family with integral spectrum

Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.5. For the iid Rademacher matrix `M_n`, the source conjectures

`P(Spec(M_n) subset Z[i]) = 2^{-(1+o(1)) n^2}`.

This note gives a source-level counterexample family. It is stronger than needed: every constructed matrix has **ordinary integer** spectrum.

## B2 — attack the source assertion from the opposite direction

The prior campaign attempt `F0012-A001` found only `2^{O(n)}` explicit examples (rank-one sign matrices). The key question is whether one can make a whole `Theta(n^2)`-dimensional sign family whose spectrum is forced arithmetically.

Take `n=2m` and write a sign matrix in four `m x m` blocks

`M = [[A,B],[C,D]]`,

where all entries of `A,B,C,D` are in `{+1,-1}`. Let

`S = [[I,0],[I,I]]`,  `S^{-1} = [[I,0],[-I,I]]`.

A direct multiplication gives the exact identity

`S^{-1} M S = [[A+B, B], [C+D-A-B, D-B]].`      (1)

Impose the three conditions

1. `C+D=A+B` entrywise;
2. `A+B` is upper triangular;
3. `D-B` is lower triangular.

Then (1) becomes block upper triangular,

`S^{-1} M S = [[A+B,B],[0,D-B]],`

whose two diagonal blocks are triangular integer matrices. Hence every eigenvalue of `M` is an integer. In fact the eigenvalues are precisely the diagonal entries of `A+B` and `D-B`, and therefore lie in `{-2,0,2}`.

### Exact independent count

The constraints separate over the `m^2` scalar positions. Write one scalar quadruple as `(a,b,c,d) in {+1,-1}^4`.

- If `i>j`, upper-triangularity requires `a+b=0`, and the equality condition then gives `c+d=0`. Thus `b=-a` and `d=-c`: exactly **4** choices.
- If `i<j`, lower-triangularity requires `d-b=0`; together with `c+d=a+b` this gives `d=b` and `c=a`: exactly **4** choices.
- If `i=j`, only `c+d=a+b` is required. The common sum is `-2,0,2`, giving `1+4+1=6` choices.

There are `m(m-1)` off-diagonal positions and `m` diagonal positions. Therefore the number of distinct matrices in the family is exactly

`N_m = 4^{m(m-1)} 6^m`.

The choices determine the four blocks entrywise, so there is no quotient or overcount.

Since every `2m x 2m` sign matrix has probability `2^{-4m^2}` under the iid Rademacher law,

`P(E_{2m}) >= 4^{m(m-1)} 6^m 2^{-4m^2}`

`             = 2^{-2m^2 + m(log_2 6 - 2)}`

`             = 2^{-n^2/2 + (n/2) log_2(3/2)}.`            (2)

Consequently, for the frozen metric

`u_GI = liminf_n [-log_2 P(E_n)]/n^2`,

we have the strict source-opposing bound

`u_GI <= 1/2`.

The source conjecture would force `[-log_2 P(E_n)]/n^2 -> 1`. Equation (2) along every even `n` is incompatible with that conclusion. Therefore **Conjecture 9.5, literally as stated for iid nonsymmetric Rademacher matrices, is refuted by this explicit family.**

No asymptotic estimate, simulation, or unproved lemma enters the argument.

## B1 — change category: fixed-flag hypercube sections

The construction above is naturally a fixed-invariant-flag construction rather than a random-matrix estimate.

Let `U_n` be the vector space of upper-triangular real `n x n` matrices. For any fixed invertible `P`,

`L_P = {P T P^{-1}: T in U_n}`

is a linear subspace of `R^{n^2}` of dimension `n(n+1)/2`.

### Hypercube-section lemma

If `L` is any `d`-dimensional linear subspace of `R^N`, then

`|L cap {+1,-1}^N| <= 2^d`.

Proof. The coordinate functionals restricted to `L` span `L^*`; choose `d` of them forming a basis. Projection to those `d` coordinates is injective on `L`. A sign vector has one of only `2^d` projected sign patterns. QED.

Thus any **single fixed basis** in which sign matrices are required to be triangular contains at most

`2^{n(n+1)/2} = 2^{n^2/2+O(n)}`

sign matrices.

Our block-shear family is itself contained in one such fixed flag after reversing the coordinate order in the lower `m`-block: `A+B` is upper triangular, `D-B` is lower triangular, and the off-diagonal block is arbitrary. Its cardinality

`4^{m(m-1)}6^m = 2^{n^2/2+O(n)}`

therefore **saturates the leading `n^2/2` entropy exponent possible for any single fixed triangularizing basis**.

This diagnoses the source failure sharply: the obstruction is not a tiny low-rank or repeated-row family. A fixed rational/integer flag already supports a half-dimensional hypercube section of sign matrices with integer spectrum.

## B21 — import the invariant-flag / Borel viewpoint

Every complex matrix whose characteristic polynomial splits is triangularizable. For Gaussian-integral spectrum, the generalized eigenspaces can be chosen over `Q(i)`, so the event is naturally a union of `Q(i)`-rational invariant-flag strata. Each fixed flag has ambient linear dimension `n(n+1)/2` (a conjugate Borel subalgebra).

The explicit shear flag above realizes the maximal possible leading hypercube-section entropy for one flag. This suggests the correct post-refutation problem is no longer Vu's exponent `1`; it is to control the **effective number and overlap entropy of rational invariant flags** that can be realized by sign matrices with Gaussian-integral spectrum. A `2^{o(n^2)}` effective flag count would be compatible with a corrected exponent `1/2`; proving such a bound is a new problem and is **not** claimed here.

This Borel/flag translation also explains why the older spectrum-counting route missed the obstruction: a single spectrum may have a half-dimensional family of sign representatives inside a fixed invariant-flag stratum, so bounding only the number of possible Gaussian-integral spectra cannot prove the source exponent.

## Exact local certificate

The companion checker exhausts all 16 scalar sign quadruples under the shear transform

`[[a,b],[c,d]] -> [[a+b,b],[c+d-a-b,d-b]]`

and certifies the local counts `6/4/4`, then verifies the exact family-count/probability formula for several `m`. It was executed in this run and returned `EXACT_LOCAL_COUNT_AND_EXPONENT_PASS`.

Checker path:
`research7_2026-09-17/R7-07/artifacts/2026-09-18/2026-09-18T232000Z__F0012_block_shear_exact_check.py`

Output path:
`research7_2026-09-17/R7-07/artifacts/2026-09-18/2026-09-18T232000Z__F0012_block_shear_exact_check.out`

## What is and is not closed

Mathematically, the literal source conjecture is refuted by (2). Under the owner's closure protocol this is **REFUTED-CANDIDATE / NOT YET CERTIFIED CLOSED** until there is a dated independent P26 audit, a distinct OTHER-track audit, and the self-contained paper package has been independently checked. No self-review is counted as either audit. Novelty is UNVERIFIED; bounded searches found no prior source-matching refutation, but search failure is not a novelty certificate.