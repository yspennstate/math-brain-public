# account02/B04 — rank-one star bank aggregation through the partner rank-two Schur theorem

**Run:** `B04-20260922T171934Z-r11`  
**Assignment:** Product Fourier rearrangement / complementary constructions and source-valid counterexamples  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full target remains `OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and first unpaid implication

The target remains the unrestricted statement: for every dimension, every product law with independent one-dimensional densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal finite essential-supremum bound for the density of `X^T A X`, or give a valid counterexample. No moments, support restrictions, diagonal-basis assumption, or independence after spectral rotation are available.

The freshest proof-assembly handoff before this report is account02/B19 run `20260922T171213Z-account02-B19-qform-r14`, corrected by its same-run correction. Its first unpaid implication is `QFORM-HIGH-OFFDIAG-PIVOT-OR-GROUPED-EXTRACTION-v2`: after the paid diffuse/ridge/same-sign/high-Schur-offdiagonal branches, route the near-rank-one or grouped-bank residue without paying a vanishing individual minor. The live star example shows that high off-diagonal spectral mass need not produce a rank-two coordinate cut.

This report pays the canonical **pure rank-one star bank** endpoint. The mechanism is to aggregate the whole original-coordinate bank into one independent linear statistic *before* paying a rank-two Schur estimate. The resulting bound is independent of the bank size and of how diffusely its coefficients are spread.

## 2. Source-pinned dependencies and corrections

### Named partner account03/B04

I use the completed theorem `QFORM-RANK2-SCHUR-NOLEVERAGE-v1` from

`yspennstate/math-open-problems@2761bd3896c56a1f929761e69035ba7cb8ebc2bc`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/B04-20260922T164839Z-r14/REPORT.md`.

It states: if an original coordinate is a nonzero scalar pivot `a` and its Schur complement has exact rank two with nonzero eigenvalues `mu_1,mu_2`, then, for arbitrary independent cap-one physical-coordinate laws,

`||p_Q||_infinity <= C_* |a|^(-1/2) |mu_1 mu_2|^(-1/4)`,

where

`C_* = 23.390590510770124...`.

The same partner report also uses the standard one-dimensional product-projection estimate: a normalized linear combination of independent cap-one variables has density at most `sqrt(2)`.

### Compatible product-envelope endpoint

For the explicit null-center subfamily I also use account03/B13's `QFORM-NULLPAIR-PLUS-SQUARE-v1`, read at source snapshot

`yspennstate/math-open-problems@3bb57a5517de87855824e393ec1601b8921abc13`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260922T165804Z-account03-B13-qform-r12/REPORT.md`.

It gives, for an invertible three-variable physical block with two null physical diagonals and null-pair coefficient `b`,

`||p||_infinity <= 2^(5/4) sqrt(15) (|b| |det B_3|)^(-1/4)`,

uniformly over arbitrary outside affine translations. Its proof uses a decreasing-rearrangement/product envelope rather than false pointwise Fresnel decay.

### Corrections respected

The proof below does not use law-uniform pointwise oscillatory decay, conditional spectral-coordinate independence, a universal conditional 3-D projection cap, a forced good small principal minor, or a forced rank-two coordinate cut. In particular it is compatible with the live singleton/two-bank and star counterexamples. The corrected account02/B19 cross-cut constant is not used numerically here.

## 3. Main theorem — `QFORM-ONE-CURVED-LEAF-STAR-BANK-v1`

Let

`X, Y, Z_1,...,Z_m`

be independent real random variables with densities bounded by one. Let `c=(c_1,...,c_m)` be nonzero, put

`B = ||c||_2`,

and let `a,b` be arbitrary real numbers and `lambda !=0`. Consider

`Q = a X^2 + 2 b X Y + lambda Y^2 + 2 X sum_k c_k Z_k`.        (3.1)

Equivalently, in the original physical coordinates `(X,Y,Z)`,

`A = [[a,b,c^T],
      [b,lambda,0],
      [c,0,0_m]].`                                            (3.2)

Then `Q` has an essentially bounded density and

`||p_Q||_infinity
 <= C_* 2^(1/4) / sqrt(|lambda| B)
 < 27.817 / sqrt(|lambda| B).`                                (3.3)

If, in addition, the three nonzero eigenvalues of `A` all have modulus at least one, then automatically

`B>=1` and `|lambda|>=1`,                                    (3.4)

and therefore

`boxed: ||p_Q||_infinity < 27.817.`                           (3.5)

This is a target-valid dimension-free closure of the whole rank-one-star bank family. The center diagonal `a`, the center/curved-leaf coupling `b`, the bank size `m`, and the distribution of the bank coefficients are unrestricted.

### Proof of the density estimate

Aggregate the complete zero-curvature bank *before* applying a reciprocal minor estimate. Define

`L = B^(-1) sum_k c_k Z_k`.

The coefficient vector is Euclidean-normalized. By the one-dimensional product-projection estimate used in the named partner report,

`||p_L||_infinity <= sqrt(2).`                               (3.6)

Put

`W = sqrt(2) L`.

Then `W` has density at most one. Moreover `W` is independent of `X,Y`, because it is a function only of the disjoint original-coordinate bank `Z`. Equation (3.1) becomes exactly

`Q = a X^2 + 2 b X Y + lambda Y^2
    + 2 (B/sqrt(2)) X W.`                                   (3.7)

Thus `Q` is a quadratic form in the three independent cap-one variables `(X,W,Y)` with matrix, in that order,

`A_tilde = [[a, B/sqrt(2), b],
           [B/sqrt(2), 0, 0],
           [b, 0, lambda]].`                                 (3.8)

Use `Y` as the physical scalar pivot. Its coefficient is `lambda`. The exact Schur complement on `(X,W)` is

`S = [[a-b^2/lambda, B/sqrt(2)],
     [B/sqrt(2), 0]].`                                       (3.9)

It has rank exactly two and

`det S = -B^2/2`.                                            (3.10)

Hence, if its eigenvalues are `mu_1,mu_2`,

`|mu_1 mu_2| = B^2/2`.                                      (3.11)

Apply the named account03/B04 theorem to the actual quadratic form (3.7):

`||p_Q||_infinity
 <= C_* |lambda|^(-1/2) (B^2/2)^(-1/4)
 = C_* 2^(1/4) / sqrt(|lambda| B).`                          (3.12)

This proves (3.3). No coordinate rotation has been used probabilistically; the only aggregate `W` is a function of an original-coordinate block disjoint from `X,Y`, so its independence is genuine.

### Why the target normalization forces `B,|lambda|>=1`

For spectral analysis only, apply an orthogonal change of basis inside the `Z`-bank sending `c/B` to the first bank basis vector. This changes no eigenvalues and makes no probabilistic claim. The nonzero spectrum of (3.2) is the spectrum of

`M = [[a,b,B],
     [b,lambda,0],
     [B,0,0]].`                                              (3.13)

Its determinant is `-B^2 lambda` and

`M^(-1) = [[0,0,1/B],
           [0,1/lambda,-b/(B lambda)],
           [1/B,-b/(B lambda),(-a lambda+b^2)/(B^2 lambda)]].` (3.14)

If all three eigenvalues of `M` have modulus at least one, then, because `M` is symmetric,

`||M^(-1)||_op <=1`.                                        (3.15)

Every matrix entry has modulus at most its operator norm. From the `(1,3)` and `(2,2)` entries of (3.14),

`1/B<=1`, `1/|lambda|<=1`,                                  (3.16)

which is exactly (3.4). Substitution into (3.12) proves (3.5). QED.

## 4. Decisive diffuse-star construction

For every `m>=1`, take

`c_k = 1/sqrt(m)`, `a=b=0`, `lambda=1`.

Then

`Q_m = Y^2 + (2/sqrt(m)) X sum_{k=1}^m Z_k`,                (4.1)

and

`A_m = [[0,0,m^(-1/2) 1^T],
       [0,1,0],
       [m^(-1/2)1,0,0_m]].`                                 (4.2)

The nonzero spectrum is exactly

`{-1,1,1}`.                                                  (4.3)

Thus every `A_m` is a genuinely rotated indefinite member of the exact target, for every bank size. The main theorem gives

`||p_{Q_m}||_infinity <27.817`                               (4.4)

for **every** choice of the allowed independent input laws, uniformly in `m`.

This family exposes why the aggregation order matters. A physical triple using only one bank coordinate has null-pair coefficient `m^(-1/2)` and determinant `-m^(-1)`. Feeding that individual triple to the local null-pair theorem costs

`2^(5/4) sqrt(15) m^(3/8)`,                                 (4.5)

which diverges. In contrast, the aggregate bank has Euclidean norm exactly one and is paid once by (3.6), producing the uniform bound (4.4). This is a source-valid construction against any proof that insists on selecting one bank atom before aggregation; it is not a counterexample to QFORM.

For this special `a=b=0` family, the account03/B13 null-pair theorem can also be applied *after* aggregation. The matrix (3.8) has null pair `(X,W)` with coefficient `1/sqrt(2)` and determinant `-1/2`. It yields the sharper all-law bound

`||p_{Q_m}||_infinity
 <= 2^(13/8) sqrt(15)
 = 11.945913686291497... .`                                 (4.6)

Again the constant is independent of `m`.

## 5. Exact calculation used

```python
import math
Cstar = 8*math.sqrt(2)*(3**0.75)*(5**0.25)/math.sqrt(math.e)
print(Cstar)
print(Cstar*2**0.25)
print((2**(13/8))*math.sqrt(15))
```

Output:

```text
23.390590510770124
27.816256659522963
11.945913686291497
```

The spectral statement (4.3) is exact from the effective matrix

`[[0,0,1],[0,1,0],[1,0,0]]`,

whose characteristic polynomial is `(t-1)^2(t+1)`.

## 6. Conditional end-to-end placement and first remaining implication

The current proof assembly has already paid a diffuse spectral-window branch, several quantitative square/pivot branches, exact rank-two Schur overlap, same-sign definite pairs, and the high-Schur-offdiagonal opposite-sign branch. The near-rank-one cut obstruction cannot be solved by demanding a rank-two cross cut or a uniformly good individual physical triple.

The theorem above shows that **bank spread itself is not the obstruction** in the canonical star endpoint. If all the off-diagonal mass sits in one original-coordinate rank-one bank and that bank has no internal quadratic curvature, aggregate it first; the partner rank-two Schur theorem then pays the entire bank with a universal constant. The explicit family (4.2) demonstrates a diverging one-atom cost but a bounded aggregate cost.

The first unpaid B04 implication is therefore sharpened to:

**`QFORM-STAR-BANK-INTERNAL-CURVATURE-v1`.** Extend the grouped-bank argument when the same bank coordinates also carry a correlated quadratic term `Z^T D Z` (and, ultimately, arbitrary extra spectral components), without rotating them into independent spectral variables and without conditioning on a normalized projected density. Either route sufficiently diffuse `D` into the existing ridge/window estimates or extract a second product-preserving grouped packet from the non-diffuse case.

This is strictly narrower than the previous generic `QFORM-HIGH-OFFDIAG-PIVOT-OR-GROUPED-EXTRACTION-v2`: the pure rank-one-star endpoint is now paid. The unrestricted QFORM conjecture remains open; no full-proof or continuity claim is made.

## 7. Privacy / provenance note

The changed artifact contains only mathematics, logical worker labels, and public/private repository source pins already authorized for this programme. No credentials, scheduler identifiers, machine paths, unrelated private data, benchmark material, email, or external workflow data are included. No native scheduler or notification mutation was performed.