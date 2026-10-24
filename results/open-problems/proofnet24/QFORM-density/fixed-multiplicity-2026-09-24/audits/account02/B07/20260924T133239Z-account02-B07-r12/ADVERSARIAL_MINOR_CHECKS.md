# account02/B07 adversarial minor and rank checks

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`

Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`; SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

These are exact finite constructions used to test the ordered-minor, bordered-determinant, sampling-multiplicity and rank quantifiers in `lem:sampling`, `lem:completion`, `prop:volume` and `lem:cut`. They are diagnostics/counterexamples to stronger intermediate claims, not counterexamples to the 17-eigenvalue theorem.

## 1. `(r+1)^2` parent multiplicity is sharp

Fix `r in {1,2,3,4}`, put `m=r+1`, and let

`C_ij = 1/(i+j+1)`,  `0<=i,j<m`.

Let `tau=1/100` and form the symmetric `2m x 2m` bipartite matrix

`A_r = [[0, tau C],[tau C^T, 0]]`.

Take the fixed ordered child `(S',T')` consisting of all `m` left and all `m` right coordinates. Every parent obtained by deleting one row from `S'` and one column from `T'` has an invertible `r x r` seed: every such submatrix is a Cauchy minor, hence nonzero. Therefore the same ordered child has exactly

`m^2=(r+1)^2`

nonsingular parents. This proves that the manuscript's child-count constant cannot be lowered by a symmetry or orientation convention.

Exact child determinants after the `tau` scaling are:

- r=1: 4 parents, child determinant `1/120000`;
- r=2: 9 parents, child determinant `1/2160000000`;
- r=3: 16 parents, child determinant `1/604800000000000`;
- r=4: 25 parents, child determinant `1/2667168000000000000000`.

These examples are in the manuscript's no-pivot regime: all diagonal entries vanish and every principal 2x2 determinant has modulus at most `tau^2=1/10000<eta=1/100`.

For every parent, direct exact elimination gives

`det(child in appended order) = det(B) (a_lm-P_lm)`.

Sorting the enlarged row and column sets multiplies this by the product of two permutation signs. Across the deletion positions both signs occur; after squaring every case gives exactly

`det(sorted child)^2 = det(B)^2 (a_lm-P_lm)^2`.

Verdict on the manuscript's sign/multiplicity statement: **PASS**. Stronger claim `(r+1)^2` can be replaced by a smaller universal combinatorial factor: **FALSE** for this counting mechanism.

## 2. The good sampled seed is existential, not universal

Take

```
A0 = [[-6, 5, 3,-2],
      [ 5, 4, 1, 4],
      [ 3, 1, 4, 3],
      [-2, 4, 3,-2]]
A = A0/1000.
```

This is no-pivot: `max_i |a_ii|=3/500<1/100`, and the largest principal 2x2 determinant modulus is `49/1000000<1/100`.

At order r=1,

`V1=2/15625`,  `V2=247/250000000000`,

so the lemma's mean threshold is

`4 V2/V1 = 247/8000000 ~= 3.0875e-5`.

For the 1-indexed seed `S={1}, T={2}`,

`||F||_F^2 = 149/12500000 ~= 1.192e-5`,

which is below the threshold. But for the equally legitimate nonsingular seed `S={2}, T={3}`,

`||F||_F^2 = 97/200000 = 4.85e-4`,

more than fifteen times the threshold. Exact summation over all weighted nonsingular seeds gives the manuscript's expected-value upper bound (in this example equality holds).

Verdict on the manuscript's quantifier “there exist disjoint r-sets S,T”: **PASS**. Stronger claim that an arbitrary nonsingular seed satisfies the same bound: **FALSE**.

## 3. Global `3r` and restricted `r` rank bounds can be simultaneous equalities

Start with the 3x3 block

```
A0 = [[-2,-2,-2],
      [-2,-2,-1],
      [-2,-1,-2]]
```

with seed `S={1}`, `T={2}`, complement `L={3}`. For the unscaled block, the canonical interpolation/completion has `E=0`,

```
R = [[-2,-2,-2],
     [-2,-2,-1],
     [-2,-1,-1]],
```

with determinant `2`. Hence `rank R=3` and `rank R[L,L]=1`.

Scale the block by `1/250`. The ranks are unchanged, while all diagonal entries have modulus `0.008<eta` and every principal 2x2 determinant is far below `eta`; hence the example is no-pivot.

For each r=1,2,3,4 take the direct sum of r scaled copies, let S be the collection of the first seed coordinate in each copy, T the collection of the second, and L the collection of the third. The seed matrix is diagonal and invertible, `E=0`, and the canonical completion satisfies simultaneously

`rank R = 3r`,  `rank R[L,L] = r`.

Verdict on both rank bounds in `lem:completion`: **PASS and algebraically sharp for this construction**. Stronger universal replacement `rank R<=2r` from symmetry/no-pivot alone: **FALSE**.

## 4. Consequence for threshold bookkeeping

The order-five no-pivot density branch may encounter the small-ratio index r=4. With only sixteen unit-scale singular directions, the present global rank loss can force at most

`16-3*4 = 4`

large diagonal entries of D, exactly compatible with the restricted rank-four block. The strict-diagonal-dominance contradiction requires five. Because the examples above show that neither the `(r+1)^2` multiplicity nor the `3r/r` rank bookkeeping can simply be tightened by a counting convention, the current architecture does not certify a 16-eigenvalue theorem.

Likewise, switching to crossing order four without a new analytic theorem leaves the leverage-free determinant envelope at the endpoint `|t|^{-1}`, which is not absolutely integrable. Thus this run obtains no complete replacement proof below 17.

Next obligation: a valid threshold reduction needs a genuinely stronger analytic endpoint/cancellation receiver or a new structural decomposition preserving all arbitrary-law/affine/sign hypotheses; it cannot come from silently halving ordered-minor multiplicities, selecting an arbitrary seed, or replacing global `3r` by `2r`.
