# fleet01/B10 r13 — full fixed-multiplicity audit

SIGNED IN — account `fleet01`, slot `B10`, 2026-09-24T14:05:50Z. Objective acknowledged: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pins

- Baseline mathematical source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Manuscript path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.
- Git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- Source length: 790 lines, 47,883 bytes.
- Fresh `master` observed immediately before publication through `dd12ba4cca03c6e18c228fbff8b176398d1a95bf`.

I read `manuscript.tex` in full and also read the current root `README.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`, and `DELIVERY_STATUS.md`. The supplementary package gap seen in an earlier B10 run is now repaired: all four advertised reproducibility files are present on current `master`.

## Executive verdict

**Literal baseline seventeen-eigenvalue theorem: PASS in this independent B10 reconstruction.** I found no fatal mathematical gap or false statement in the theorem as written. No manuscript source range remains mathematically `UNCHECKED` in this run.

The statement checked is exactly: independent arbitrary real coordinate densities bounded by `K`; arbitrary real symmetric `A`; arbitrary affine `b,c`; if `s_17(A)>=s>0`, then `X^TAX+b^TX+c` has an essentially bounded density with norm at most `10000 K^2/s`. No continuity conclusion is inferred in the pivot branches, and no unrestricted three-eigenvalue claim is made.

This is an independent worker audit, not formal verification or journal peer review. Finite checker output is kept separate from proof status.

## Full source ledger

| Source lines | Status | B10 check |
|---|---|---|
| 1–83 | PASS | Definitions, theorem quantifiers, scaling target `K^2/s`, and proof architecture preserve arbitrary dimension, signature, remaining spectrum, affine terms, and rough product laws. |
| 84–168 | PASS | Fourier convention, Gaussian regularization, Plancherel/inversion factors, power-envelope integration, and half-Riesz normalization rederive correctly. |
| 169–217 | PASS | Singular-value perturbation works nonsymmetrically. Principal-pivot Schur spectral count is correct, including singular ambient `A`; strict diagonal dominance is used only as a rank contradiction. |
| 218–301 | PASS | Heat-flow geometric Brascamp–Lieb sign, large-time limit, rough-function approximation, product-projection bound, and scalar Fourier powers are valid. Deterministic rotations are not used to assert probabilistic independence. |
| 302–400 | PASS | Two-copy decoupling, graph-frame weights/Jacobian, regularizer `(2*pi*e)^2`, fourth-root determinant exponent `-1/8`, Cauchy–Binet expansion, order-five density and order-three half-Riesz uses all check. |
| 401–525 | PASS | Scalar square profile, definite pair, hyperbolic coarea and tails, quarter-power concentration, atom exclusion, and logarithmic potential are dependence-safe and compatible with rough laws. |
| 526–630 | PASS | Ordered disjoint minors, bordered determinant, singular-seed inequality, nonsymmetric interpolation support, global `rank R<=3r`, restricted `rank R[L,L]<=r`, zero diagonal of `E`, and seed-zero diagonal of `D` are correct. |
| 631–724 | PASS | `4k-3` spectral-to-volume conversion, random-cut factor `4^{-k}`, no-pivot consequences, singular kernels, pivot truncated half-potential, and nine-direction half-potential close with the stated hypotheses. |
| 725–790 | PASS | Main case split, Schur counts after scalar/pair pivots, constants, general `K,s` scaling, 33-direction corollary, and stated limitations are correct. |

### Schur-limit reconciliation

One current peer report labels the singular-ambient Schur paragraph near source line 205 as a repairable wording gap. I do **not** find a mathematical gap. Let

`m = N_A(t)-k`.

If `m<=0` there is nothing to prove. The invertible perturbation argument gives

`N_{S_epsilon}(t-|epsilon|)>=m`,

which is exactly

`s_m(S_epsilon)>=t-|epsilon|`

for the ordered absolute eigenvalues/singular values of the symmetric Schur complement. Since `S_epsilon -> S` in operator norm, singular values are continuous, so

`s_m(S)>=t`.

Therefore `N_S(t)>=m`. No continuity of the integer-valued counting function at a threshold is required. The manuscript's final sentence can be read through this closed singular-value inequality.

### Product-projection wording

After rows with `b_i=0` are dropped, the proof can simply keep those zero-leverage indices in the scalar inequality with zero left contribution. Then

`sum_i -b_i log b_i <= sum_i (1-b_i)=d`.

Equivalently the sum over retained rows is at most `d`. Thus the displayed `e^{d/2}` bound is valid; at most there is a harmless wording ambiguity, not a theorem gap.

## Exact arithmetic audit

The manuscript's no-pivot diagonal-dominance constants are comfortably positive:

- `eta=1/100`, `sqrt(kappa)=1/80`.
- At worst `epsilon=(r+1)/80<=1/16` for `r<=4`.
- Diagonal lower bound: `1-1/16-1/100 = 371/400`.
- Off-diagonal per-entry bound used by the source: `<1/7+1/16=23/112`.
- Four-neighbor row sum: `<4*(23/112)=23/28`.
- Exact slack: `371/400-23/28 = 297/2800 >0`.

The current root checker independently records the same `297/2800` exact slack.

## Finite-check coverage: PASS as diagnostics, not proof

I read `verify.py` line by line and the recorded `checks.json` output. The current suite is internally scoped correctly and passed:

- 534 exact rational interpolation seeds;
- 18 exact volume-sampling comparisons;
- 9 strict sampling cases exhibiting the singular-seed inequality rather than equality;
- exact diagonal-dominance slack `297/2800`;
- 240 floating Schur-threshold diagnostics;
- 30 floating graph-weight diagnostics.

The suite checks the pinned source hash before running. It does **not** check the heat-flow proof, universal rough-law measure arguments, all hyperbolic/kernel integrals, all dimensions, or every possible matrix. Those portions are therefore `UNCHECKED BY THE FINITE CHECKER`, while they are `PASS` in the mathematical audit above. The historical counts in root `AUDIT.md` come from a different older suite; the current README/manifest explicitly say the new suite does not reproduce those counts.

## Adversarial exact small-matrix diagnostics

These are finite structural diagnostics only.

### 1. Simultaneous sharpness of the two interpolation rank bounds

For

```
A = [[ 2, 3,-1, 2],
     [ 3, 2, 1,-1],
     [-1, 1, 4,-1],
     [ 2,-1,-1,-2]],
```

choose the order-one seed `S={0}`, `T={1}`, so `B=[3]` and `L={2,3}`. The interpolation is

```
P = [[   2,  3,   -1,    2],
     [ 4/3,  2, -2/3,  4/3],
     [ 2/3,  1, -1/3,  2/3],
     [-2/3, -1,  1/3, -2/3]].
```

The manuscript completion gives

```
R = [[ 2, 3,   -1,    2],
     [ 3, 2,    1,   -1],
     [-1, 1, -1/3,  2/3],
     [ 2,-1,  1/3, -2/3]].
```

Exact rational elimination gives

`rank R = 3 = 3r`,

`rank R[L,L] = 1 = r`.

Thus the global and restricted rank constants can be simultaneously saturated already in a `4x4` symmetric example; a threshold reduction cannot come from a cosmetic replacement of `3r` or `r` by smaller universal rank bounds.

### 2. Singular deleted seed can have a nonsingular same-step extension

For

```
A0 = [[0,0,0,1],
      [0,0,1,0],
      [0,1,0,0],
      [1,0,0,0]],
```

the seed `S={0}`, `T={1}` is singular, but the extension with rows `{0,2}` and columns `{1,3}` is

```
[[0,1],
 [1,0]],
```

with determinant `-1`. This directly verifies why Lemma `lem:sampling` obtains an inequality after summation: singular seeds contribute no sampling mass but can have nonsingular extensions.

## Threshold status after reading current improvements

The baseline `17` theorem is no longer the strongest complete candidate in the repository. I independently inspected the current grouped product-Fourier reduction to multiplicity `9`: it uses the baseline order-three volume proposition plus a marginal-free third-crossing density receiver, and an order-two half-potential receiver after an outer scalar pivot. Multiple separate worker reconstructions now report PASS. I do not convert those reports into a self-awarded release certificate here.

Multiplicity `8` remains open. The strongest structural reduction I checked says that in the no-pivot `s_8>=1` chamber either the third disjoint volume is already large, or one obtains a quantitative overlap-one/two-sided collar packet. Existing rank arithmetic cannot close that terminal `r=2` chamber: under `s_8` it forces only two large diagonal residual coordinates, which is compatible with `rank R[L,L]<=2`. A genuinely new product-preserving collar receiver is still required.

## Final audit statuses

- Baseline seventeen-eigenvalue manuscript: **PASS** in this full B10 audit.
- Fatal mathematical gaps found: **NONE**.
- Manuscript source ranges mathematically UNCHECKED: **NONE**.
- Supplementary-file packaging gap from prior B10 run: **REPAIRED on current master**.
- Finite diagnostics: **PASS but non-universal by design**.
- Multiplicity nine: **current complete candidate, separately reviewed in the repository; owner/release synthesis is separate**.
- Multiplicity eight: **OPEN**.
- Unrestricted three-eigenvalue conjecture: **OPEN**.
- Global continuity: **OPEN outside the Fourier-integrable branches**.
