# A quantitative check of the finite-cell lemma

The lemma checked here is `found:lem-finite-cell` in OpenAI, *Strict convexity and differentiability of the planar exponential first-passage limit shape*, September 24, 2026, [primary source](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/strict/foundations.tex). The construction below is the paper's construction, with the projection argument and the boundary constant written out. This establishes the abstract lemma under its hypotheses. It does not establish that the FPP application supplies those hypotheses.

## Statement

Let `(eta_z)`, indexed by `z in Z²`, be independent random elements. Write `F_I = sigma(eta_z : z in I)` and `Q_a(z) = {u : |u-z|_infinity <= a}`. Fix an integer `H >= 2`. Let `V_(z,lambda)` be integrable real random variables, with an arbitrary label set containing a label 0. Assume that for every pair `a=(z,lambda)`, `b=(z',lambda')` with `|z-z'|_1 <= 1`, there is an `F_(Q_H(z))`-measurable variable `E_ab` such that

`||E_ab - (V_b - V_a)||_1 <= epsilon`.

Put

`R = 8H+20`, `m = (2H+1)²`, `q = (4H+1)²`,

`N = (2R+1)² 2^q`, `B = 4R+4H+11`,

`C_H = 2 + 2 N B 2^m`.

There are integrable `g_(z,lambda)`, measurable with respect to `F_(Q_(R+2H)(z))`, such that

`E g_(z,lambda) = E V_(z,lambda)`

and, for every pair covered by the hypothesis,

`||g_b - g_a - (V_b - V_a)||_1 <= C_H epsilon`.

The constant is independent of the number of labels, the distributions and internal sizes of the cells, and the spatial scale. For H=2 it can be written as `C_2 = 2 + 1737254 * 2^106`. The large constant is only a uniform bound.

## 1. Finite-product projections

For a finite set I let `P_I F = E[F | F_I]`, including `P_empty F = E F`. Independence implies

`P_I P_J F = P_(I intersection J) F`.

To justify this identity for general integrable F, first verify it for finite products of bounded functions of individual coordinates, where it follows by integrating coordinates outside I and J. Linear combinations give cylinder functions. Conditional expectations are L1 contractions, so approximation gives the identity for all integrable functions measurable with respect to the product sigma field. If F also uses extra randomness, first replace it by its conditional expectation on that product sigma field; both sides are unchanged. Thus no L2 assumption or infinite orthogonal expansion is needed.

For nonempty finite S define

`Pi_S F = sum_(I subset S) (-1)^(|S|-|I|) P_I F`.

Each summand is F_S-measurable, `E Pi_S F = 0`, and

`||Pi_S F||_1 <= 2^|S| ||F||_1`.

If F is F_J-measurable and S is not contained in J, choose `j in S minus J`. Independence gives `P_I F = P_(I intersection J) F`. Pair the term I not containing j with `I union {j}`. Their conditional expectations agree and their signs are opposite. Therefore `Pi_S F = 0`.

For F measurable on a finite set J,

`F = E F + sum_(empty != S subset J) Pi_S F`.

Indeed, on expanding the right side, the coefficient of `P_I F` is `sum_(I subset S subset J) (-1)^(|S|-|I|)`. It is zero unless I=J, when it is one. This also explains why every projection used below is a finite identity in L1.

## 2. The local gauge

Let script-S contain the nonempty finite S with `|S| <= m` and `diameter_infinity(S) <= 2H`. For such an S, let k(S) be its lexicographically least element and set

`U_S = Q_R(k(S))`, `z_S = k(S) + (R+4H+10)e_1`.

Define

`g_(z,lambda) = E V_(z,lambda) + sum_(S in script-S, z in U_S) Pi_S(V_(z,lambda) - V_(z_S,0))`.

This sum has at most N terms. In fact, `z in U_S` requires `k(S) in Q_R(z)`, giving `(2R+1)²` possibilities. For a fixed k(S), all of S is in `Q_(2H)(k(S))`, so at most `2^q` subsets are possible. The restrictions on size and on the least element only reduce this count.

Each term is integrable, has mean zero and depends only on eta in S. Also `S subset Q_(R+2H)(z)` whenever `z in U_S`. This proves both the required locality and the equality of means. The appearance of the distant reference V in a conditional expectation does not add distant realized inputs to its measurable support.

## 3. Boundary terms

Suppose z belongs to U_S but a nearest neighbor z' does not. Then z lies on the boundary of `Q_R(k(S))`. There is a nearest-neighbor path on that boundary from z to `k(S)+R e_1` of length at most 4R: the boundary has 8R edges, and the shorter of its two arcs has length at most 4R. Continue east for `4H+10` steps to z_S. The resulting path has length at most `4R+4H+10`.

Every starting vertex u along this path has `|u-k(S)|_infinity >= R`. Since `S subset Q_(2H)(k(S))` and `R>3H`, the sets `Q_H(u)` and S are disjoint. The local comparison variable on each step therefore has zero Pi_S projection. This follows from the cancellation established in Section 1; disjointness is more than is required.

First change label lambda to 0 at z if needed, using the allowed same-index comparison. Telescope the potential differences along the path to z_S, with that one extra comparison. The total number of comparisons is at most B. Projecting the sum of their errors gives

`||Pi_S(V_(z,lambda) - V_(z_S,0))||_1 <= B 2^m epsilon`.

The same estimate holds with the roles of z and z' reversed for a set entering the cutoff at z'. Notice that the bound depends on H only, not on lambda. This is the only use of an exterior detour around S.

## 4. Recovery of a neighboring increment

Fix a=(z,lambda), b=(z',lambda') under the hypothesis. Write `W=V_b-V_a`, `E=E_ab`, `delta=W-E`, so `||delta||_1 <= epsilon`. Let A_z be the sets S contributing to the gauge at z, and put

`K = A_z intersection A_z'`, `T = A_z symmetric-difference A_z'`.

Subtract the two gauge formulas. For S in K, the reference terms cancel and the summand is Pi_S W. For S in T, the summand is a signed boundary term of the preceding section. When z=z', T is empty.

Every nonempty S contained in `Q_H(z)` belongs to K: its size and diameter meet the definition of script-S, its least element lies within distance H of z, and within distance H+1 of z'. Both distances are less than R. Conversely, if S in K is not contained in `Q_H(z)`, then Pi_S E=0, since E is measurable on `Q_H(z)`. Hence the finite-product identity gives

`sum_(S in K) Pi_S E = E - E E`.

It follows that

`g_b - g_a - W = -(delta - E delta) + sum_(S in K) Pi_S delta + sum_(S in T) signed-boundary-term`.

The first term has L1 norm at most `2 epsilon`. Each term in the first sum has norm at most `2^m epsilon`. Each term in the second sum has norm at most `B 2^m epsilon`. Since B>=1 and

`|K| + |T| = |A_z union A_z'| <= 2N`,

the total norm is at most

`[2 + 2 N B 2^m] epsilon`.

This proves the claim, including same-index label changes. It also checks the sign of the centered error directly.

## 5. Translation covariance

Suppose the measure-preserving input shifts send the coordinate sigma field F_I to its translated field, the V differences transform covariantly, and their deterministic means have the corresponding covariance. Conditional expectation then commutes with those shifts. Lexicographic minima, cutoff squares and reference displacements commute with index translations. Every random term in g uses a difference of V, so a common random additive term in the translated V cancels. The displayed gauge therefore has the required covariance, as equality of random variables almost surely. As usual, countably many required shifts and labels allow a common exceptional null set; no simultaneous pointwise claim over an uncountable label set is needed for the pairwise L1 conclusion.

## 6. Checks and limits

The coefficient for H=2 follows in two forms. Direct substitution gives R=36, m=25, q=81, B=163 and `N=73² 2^81`. Multiplication gives `2 N B 2^m = 2*5329*163*2^106 = 1737254*2^106`.

The script `check_local_potential.py` independently finds the maximum boundary-to-reference distance by breadth-first search on the square boundary, and verifies the projection decomposition, zero means, support cancellation and L1 bounds by exact rational arithmetic on a biased four-cell Bernoulli product. These finite checks accompany the argument; they are not a proof for arbitrary product laws.

Several possible failure points do not invalidate this lemma. Individual V variables may be nonlocal and may contain a common random offset; only their differences enter the random gauge terms. Conditioning is on whole independent cells, so a cell can contain arbitrarily many microscopic variables. Same-index changes and arbitrary numbers of labels cost no extra factor. The bound is on each neighboring increment, not on the absolute discrepancy `||g-V||_1`, which is neither asserted nor proved.

The independent-cell hypothesis and the availability of every required neighboring and same-index comparison remain essential assumptions. This calculation does not verify the road-network comparisons, common-world gauge application, matched-cap link estimates, or closure of the improved road class. The abstract gauge construction therefore does not by itself prove strict convexity of an FPP limit shape.
