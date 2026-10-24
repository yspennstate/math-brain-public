# account02/B05 — general three-bank scalar core; arrowhead normal form not needed

**Run:** `20260922T202100Z-b05-qform-47d9c1a2`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`; live OWNER CONTROL revision `2026-09-22.15`  
**Classification:** `ESSENTIAL_STEP_APPLIED`; one stronger intermediate extraction requirement is `CANDIDATE_REFUTED`; full QFORM remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN` for native learned-memory purposes. Authenticated repository retrieval was used for source verification, but repository transport is not native learned-memory ingestion.

## 1. Target and first unpaid implication

The target is unchanged: for arbitrary independent real inputs with densities at most one and arbitrary real symmetric `A` with `s_3(A)>=1`, prove a universal essential density bound for `X^T A X`, or give a valid counterexample.

The preceding B05 theorem `QFORM-THREE-BANK-ARROWHEAD-SPECTRAL-CLOSURE-v1` proved a universal bound once three independent scalar banks had the special core

`[[0,x,0],[x,z,w],[0,w,y]]`.

Its first unpaid implication asked for an extraction of this special zero pattern, or a dependence-safe treatment of the forbidden `U^2` / `UZ` leakage. This run proves that the zero pattern is unnecessary at the scalar-bank level: **every density-normalized three-scalar core with a uniformly nonsingular 3x3 coefficient matrix has a universal bound, with arbitrary signs and affine terms.** The residual global debt is only the extraction of such independent aggregates while controlling within-bank residual quadratic dependence.

## 2. Sources actually used

1. account02/B05, run `20260922T122133Z-b05-qform-5c41e5bb`, canonical commit `e06922bfa31bbd225cdce6ee6aea563254e62563`, report `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T122133Z-b05-qform-5c41e5bb/REPORT.md`. The source theorem used below is `QFORM-SCALAR-SCHUR-COAREA-v1`:

`||p_Q||_infinity <= K |a det B|^(-1/4)`, `K=8*3^(3/4)`,

for an invertible original-coordinate 3x3 block with nonzero diagonal pivot `a`, arbitrary affine terms and arbitrary outside couplings.

2. Interactive full-matrix pair theorem, canonical commit `742ac943440e41925fe09db9a8c02a96cbd83dbc`, report `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`. For an invertible indefinite original-coordinate pair `B`, with `D=|det B|`, `kappa=sigma_min(B)`, and ambient `s_3(A)>=s`, it proves

`||p_Q||_infinity <= 3*400^(1/3) (D^2 kappa s)^(-1/6)`.

3. Named partner account03/B05, run `20260922T194010Z-account03-B05-QFORM-r16`, canonical commit `d6312e9c0de9a774079895ee3c7aad7043015e49`. Its theorem `QFORM-NEARZERO-MOVING-TRANSLATION-PAIR-REPAIR-v1` gives `<9.514` on the exact near-zero diagonal family, and its independent review is `PASS` for the stated scope of the arbitrary-rank pair theorem in item 2. I use the reviewed pair theorem in the small-diagonal branch below; the partner theorem is also applied as the sharper bound on its exact near-zero subfamily.

The live correction inbox consumed before publication includes the false arbitrary-joint coarea lemma, the false conditional projection positive-moment gate, the false post-rotation-independence shortcut, the curved-fiber supremum loss, and the pointwise Fresnel-decay failure. None is used below.

## 3. Main theorem: all three-scalar cores

### Theorem — `QFORM-THREE-BANK-GENERAL-CORE-v1`

Let `Y=(Y1,Y2,Y3)` have independent real coordinates, each with probability density bounded by one. Let `M` be a real symmetric `3x3` matrix with

`sigma_min(M) >= s > 0`.

For arbitrary `ell in R^3` and `c in R`, put

`Q = Y^T M Y + ell^T Y + c`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity < 36/s`.                                      (3.1)

No sign condition, diagonal dominance, zero pattern, moment assumption, support assumption or post-rotation independence is used.

### Proof

Write `m_ij` for the entries of `M` and

`d=max_i |m_ii|`.

Because `sigma_min(M)>=s`, `M` is invertible and

`|det M| >= s^3`.                                                (3.2)

We split according to the original scalar coordinates `Y1,Y2,Y3`, so their independence is preserved.

#### Case 1: a scalar diagonal pivot is visible

Assume `d>=s/8`, and choose `i` with `|m_ii|=d`. Apply `QFORM-SCALAR-SCHUR-COAREA-v1` to this three-coordinate block. It gives

`||p_Q||_infinity <= K |m_ii det M|^(-1/4)`,
`K=8*3^(3/4)`.

By (3.2),

`|m_ii det M| >= (s/8)s^3 = s^4/8`,

hence

`||p_Q||_infinity <= K 8^(1/4)/s`
` = 8*216^(1/4)/s < 32/s`,                                     (3.3)

because `216<256`.

#### Case 2: all diagonal entries are small

Assume now

`|m_ii|<s/8` for all `i`.                                       (3.4)

Since `||M e_1||_2>=s`,

`m_12^2+m_13^2 >= s^2-m_11^2 > (63/64)s^2`.

Therefore for one `j in {2,3}`,

`|b|:=|m_1j| > sqrt(63/128) s`.                                (3.5)

Consider the original-coordinate principal pair

`B=[[a,b],[b,c]]`,

where `a=m_11`, `c=m_jj`. From (3.4)-(3.5),

`b^2>|ac|`,

so `B` is invertible and indefinite. Moreover, as a perturbation of `[[0,b],[b,0]]` by `diag(a,c)`,

`kappa:=sigma_min(B) >= |b|-max(|a|,|c|)`
` > (sqrt(63/128)-1/8)s`
` > (2/3-1/8)s = (13/24)s > s/2`.                              (3.6)

Also

`D:=|det B| = b^2-ac >= b^2-|ac|`
` > (63/128-1/64)s^2 = (61/128)s^2 > s^2/3`.                   (3.7)

Apply the reviewed full-matrix indefinite-pair theorem to this pair, with ambient third singular value at least `s`. Equations (3.6)-(3.7) give

`D^2 kappa s > (s^4/9)(s/2)s = s^6/18`.

Thus

`||p_Q||_infinity`
` <= 3*400^(1/3)(D^2 kappa s)^(-1/6)`
` < 3*400^(1/3)*18^(1/6)/s`
` < 36/s`.                                                       (3.8)

The last inequality is exact: after division by `3` and raising to the sixth power it is equivalent to

`400^2 * 18 < 12^6`,

namely `2,880,000 < 2,985,984`.

Cases 1 and 2 prove (3.1). QED.

## 4. Density-normalized bank corollary

Let `U,V,Z` be independent real scalar aggregates from three disjoint original-coordinate banks. Suppose certified density caps are

`||p_U||_infinity<=L1`, `||p_V||_infinity<=L2`, `||p_Z||_infinity<=L3`,

with finite positive `Li`. Let `D=diag(L1,L2,L3)` and let their quadratic core be `M`. Rescale

`Y=D(U,V,Z)^T`.

Each coordinate of `Y` has density cap at most one, and its quadratic matrix is

`M_tilde = D^(-1) M D^(-1)`.

Therefore, if

`sigma_min(M_tilde)>=s`,                                        (4.1)

then the aggregate quadratic-plus-affine law has

`||p||_infinity <36/s`.                                         (4.2)

An independent direct-sum quadratic remainder may be convolved in without increasing the density supremum.

This is the exact quantity that a global bank-extraction argument should now pay: the smallest singular value of the **density-normalized compressed core**, not a reciprocal physical coordinate minor and not the special arrowhead parameter `eta` alone.

## 5. The old exact-arrowhead extraction requirement is not exhaustive

The stronger intermediate claim that every target core can first be reduced, using only three disjoint scalar banks, to a zero-pattern core with `U^2=UZ=0` is false already in dimension three.

Take

`M0=[[2,1,1],[1,2,1],[1,1,2]]`.

Its eigenvalues are `4,1,1`, so it is an exact target matrix with `sigma_min(M0)=1`. With only three original coordinates, three nonempty disjoint banks must be the three singleton coordinates. Any bank aggregate is therefore a nonzero rescaling of one coordinate, possibly after permutation. The induced matrix is a diagonal congruence/permutation of `M0`, and hence every diagonal and every off-diagonal entry remains nonzero. In particular one cannot force either `U^2=0` or `UZ=0`.

Thus **exact arrowhead extraction by disjoint scalar banks is not a valid exhaustive reduction.** This is not a counterexample to QFORM: Theorem 3 gives `||p||_infinity<36` immediately for arbitrary independent cap-one inputs and arbitrary affine terms.

This refutation is useful because it removes a structurally impossible zero-pattern obligation rather than merely weakening its constant.

## 6. Named partner application

For the partner's exact family

`A_a=[[a,sqrt(1+a),0],[sqrt(1+a),0,0],[0,0,1]]`, `0<a<=1/3`,

the eigenvalues are `1+a,-1,1`, hence Theorem 3 alone gives `<36`. The named account03/B05 theorem applies more sharply and gives `<8*2^(1/4)<9.514`, uniformly as `a downarrow0`. This confirms, on the singular-pivot limit that defeated the older scalar-square absolute-half-Riesz order, that the small-diagonal branch must keep an indefinite pair intact. The general small-diagonal branch in Theorem 3 is exactly the reviewed arbitrary-rank version of that mechanism.

## 7. What is now paid and what remains unpaid

Paid here:

- the special `U^2=0` condition is unnecessary once three independent scalar aggregates are obtained;
- the special `UZ=0` condition is unnecessary;
- arbitrary signs and arbitrary affine terms on the three aggregates are allowed;
- the three-eigenvalue scale of the density-normalized compressed core directly yields a universal density bound;
- exact arrowhead extraction as an exhaustive three-bank reduction is source-validly refuted by `M0`.

First unpaid implication after this run:

`QFORM-DENSITY-NORMALIZED-TRIBANK-EXTRACTION-OR-RESIDUAL-LEAKAGE-v1`.

From arbitrary original-coordinate `A` with `s_3(A)>=1`, either:

1. produce three disjoint original-coordinate scalar aggregates with independent laws and certified caps `Li` such that the density-normalized compressed core `D^(-1) M D^(-1)` has `sigma_min>=c` for an absolute `c>0`, while all remaining quadratic terms are independent direct-sum or condition only into affine terms; or
2. send the matrix to an already-paid physical-pair, ridge/diffuse, grouped-star, or other dependence-safe branch; or
3. prove a coarea estimate that tolerates the remaining **within-bank quadratic residual dependence** jointly with the aggregate variables.

The missing factor is therefore no longer the internal 3x3 zero pattern. It is the preservation of an independent three-scalar aggregate interface in the presence of residual within-bank quadratic leakage.

## 8. Integrity / no hidden computation

No numerical simulation or finite search is used as mathematical evidence. All constants above follow from exact inequalities displayed in the proof. The only exploratory arithmetic performed during drafting was not used as a premise; the archived proof uses the exact `<36/s` comparison. No unrestricted curved-fiber supremum, arbitrary-joint coarea lemma, conditional density-cap claim, post-rotation independence, or law-uniform pointwise oscillatory decay is invoked.

Full QFORM remains OPEN.
