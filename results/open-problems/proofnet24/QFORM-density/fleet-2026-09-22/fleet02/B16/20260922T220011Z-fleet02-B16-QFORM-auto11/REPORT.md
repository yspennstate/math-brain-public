SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-22T22:00:11Z.
attacking: grouped-bank projection-product interaction—compress collinear spectral-row banks before paying any reciprocal physical determinant, then test the resulting Pluecker aggregation.

# fleet02/B16 — finite spectral-line bank compression and physical-Pluecker averaging barrier

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Projection-product interaction  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Status:** `NEW SUPPORTING THEOREM + EXPLICIT AGGREGATION BARRIER / FULL QFORM OPEN`.

## 1. Full target and correction boundary

The full target remains open: for arbitrary independent real inputs with one-dimensional densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one dimension-independent essential density bound for `X^T A X`, or give a valid counterexample.

This report does not use independence after spectral rotation, an arbitrary-joint coarea bound, a positive moment of normalized conditional projection densities, a worst conditional-density supremum, law-uniform pointwise quadratic-phase decay, or deletion of additional spectral components. The construction keeps independence only when it comes from disjoint sets of ORIGINAL coordinates.

The exact question attacked here is the aggregation debt left by the designated partner fleet03/B16: a physical `3 x 3` determinant theorem is available, but diffuse Pluecker mass makes every individual physical triple tiny. I first prove that if many physical coordinates can be compressed into a bounded number of independent **row-direction banks**, then the partner theorem can be applied after compression with a dimension-free constant. I then show on a target-valid family that Cauchy--Binet volume sampling of the uncompressed physical-triple bounds loses a factor growing linearly with bank size even though bank compression gives a uniform bound.

## 2. Source-valid inputs actually applied

### 2.1 Scalar product-projection density bound

The completed rank-two fusion report

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`

records the Rogozin--Ball consequence used here: if independent `X_i` have densities at most one and `sum_i c_i^2=1`, then

`Y=sum_i c_i X_i`

has density

`||p_Y||_infinity <= sqrt(2)`.                                      (2.1)

This is a theorem about a single physical product projection; no independence between overlapping projections is inferred.

### 2.2 Designated partner fleet03/B16

The newest completed designated-partner theorem read for this run is

`yspennstate/math-open-problems@b94cc7446401c02727c42024274c002e2f4e0cab`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260922T202347Z-fleet03-B16-QFORM-r15/REPORT.md`.

Its `QFORM-PHYSICAL-TRIPLE-DETERMINANT-v1` states that for three independent cap-one variables, any invertible symmetric `3 x 3` quadratic matrix `B`, and arbitrary affine terms,

`||p||_infinity <= C_3 |det B|^(-1/3)`,                             (2.2)

where

`C_3=16 sqrt(30) 2^(1/4)=104.21688998922089... <105`.               (2.3)

The theorem also applies to a selected original-coordinate triple inside any ambient form after conditioning on all other **independent original coordinates**. This translation stability is what permits its use below after a legitimate product-bank compression.

## 3. Row-direction banks

Let the matrix have exact rank three:

`A=R Lambda R^T`, `R^T R=I_3`,                                      (3.1)

where `Lambda` is invertible symmetric and its three eigenvalues satisfy

`|lambda_j|>=1`.                                                     (3.2)

Write `r_i in R^3` for the `i`th row of `R`.

Assume the nonzero rows of `R` lie in the union of `K` one-dimensional subspaces of `R^3`. Equivalently, partition the relevant original coordinates into disjoint banks

`I_1,...,I_K`                                                        (3.3)

such that for every `i in I_k`,

`r_i=a_i v_k`,                                                       (3.4)

where `v_k` is a unit vector. Zero rows may be ignored.

Put

`s_k=(sum_(i in I_k) a_i^2)^(1/2),`
`u_k=s_k v_k`,
`c_i=a_i/s_k`,
`Y_k=sum_(i in I_k)c_i X_i`.                                        (3.5)

Empty banks are discarded, so `s_k>0`.

Because the banks are disjoint sets of original coordinates, the variables `Y_1,...,Y_K` are genuinely independent. By construction `sum_(i in I_k)c_i^2=1`, so (2.1) gives

`||p_(Y_k)||_infinity <= sqrt(2)`                                   (3.6)

for every bank. No projected-coordinate independence beyond this disjoint-source statement is used.

Let

`T=[u_1 ... u_K] in R^(3 x K)`.                                     (3.7)

Then the Parseval identity `R^T R=I_3` gives the exact grouped-frame relation

`T T^T=sum_k u_k u_k^T=I_3`.                                       (3.8)

Moreover

`R^T X=sum_k u_k Y_k=T Y`,                                          (3.9)

so the quadratic form is exactly

`Q=Y^T C Y`, `C=T^T Lambda T`.                                      (3.10)

Thus bank compression has not approximated or discarded any part of the rank-three form.

## 4. Main theorem: grouped determinant before inversion

### Theorem — `QFORM-FINITE-LINE-BANK-COMPRESSION-v1`

Under (3.1)--(3.4), define for each bank triple `S subset {1,...,K}`, `|S|=3`,

`w_S=det(T_S)^2`,                                                    (4.1)

where `T_S` is the `3 x 3` submatrix of columns indexed by `S`, and put

`w_*=max_(|S|=3) w_S`.                                               (4.2)

Then

`boxed: ||p_Q||_infinity <= 2 C_3 |det Lambda|^(-1/3) w_*^(-1/3).`  (4.3)

Since Cauchy--Binet and (3.8) give

`sum_(|S|=3) w_S=det(TT^T)=1`,                                      (4.4)

one has

`w_* >= 1/binom(K,3)`,                                              (4.5)

and hence the explicit finite-line-complexity bound

`boxed: ||p_Q||_infinity <= 2 C_3 binom(K,3)^(1/3)}`                (4.6)

with

`2 C_3=32 sqrt(30) 2^(1/4)=208.43377997844178... <209`.             (4.7)

In particular, if the spectral rows occupy exactly three line directions, the density is universally bounded by `<209`, independent of the number of physical coordinates in each line bank and independent of the input laws.

### Proof

Scale each grouped variable by

`Z_k=sqrt(2) Y_k`.                                                   (4.8)

By (3.6), the `Z_k` are independent and each has density at most one. Equation (3.10) becomes

`Q=Z^T (C/2) Z`.                                                     (4.9)

For a bank triple `S`, the corresponding principal block satisfies

`(C/2)_[S,S]=(1/2) T_S^T Lambda T_S`,                               (4.10)

so

`|det (C/2)_[S,S]|
 = (1/8) |det Lambda| det(T_S)^2
 = (1/8)|det Lambda| w_S`.                                          (4.11)

Choose `S_*` attaining `w_*`. Since (4.4) is one, `w_*>0`, so this principal block is invertible. Apply the designated partner theorem (2.2) to the three independent bank variables `Z_k`, `k in S_*`, conditioning on every other independent bank variable. All cross terms become affine terms in the selected triple, exactly within the partner theorem's scope. Therefore

`||p_Q||_infinity
 <= C_3 [(1/8)|det Lambda|w_*]^(-1/3)
 = 2 C_3 |det Lambda|^(-1/3) w_*^(-1/3)`,                           (4.12)

which is (4.3). Equations (4.4)--(4.6) follow from Cauchy--Binet. QED.

### Three-bank rigidity

When `K=3`, (3.8) says the square matrix `T` satisfies `TT^T=I_3`, hence `T` itself is orthogonal. Thus `w_*=1` exactly. This explains algebraically why arbitrarily diffuse physical coordinates inside three source banks cost nothing after the banks are compressed first.

## 5. Stress family: physical Pluecker averaging loses the bank size

For every integer `m>=1`, let

`A_m=(J_m/m) direct_sum (J_m/m) direct_sum (-J_m/m)`.                (5.1)

Its nonzero spectrum is exactly `{1,1,-1}`, so it is a valid exact-rank-three target matrix. Take arbitrary independent input coordinates with densities bounded by one.

There are three line banks, each consisting of `m` equal physical rows of coefficient `m^(-1/2)` along one spectral coordinate. The grouped theorem therefore gives

`||p_(X^T A_m X)||_infinity <209`                                   (5.2)

uniformly in `m` and in all cap-one source laws.

In fact the special diagonal bank-level signature gives the much sharper elementary bound `2 pi`: each normalized bank sum has density at most `sqrt(2)`, and the two positive bank squares have convolution density at most `2 pi`; convolution with the independent negative bank square cannot increase the supremum. The weaker `<209` estimate is recorded because it comes from the designated partner theorem and survives arbitrary rotation of the three bank directions in spectral space.

Now inspect the uncompressed physical triples. A principal physical triple is invertible exactly when it takes one coordinate from each bank. There are `m^3` such triples and every one has

`|det A_m[S,S]|=m^(-3)`.                                            (5.3)

The partner local physical-triple theorem applied before grouping therefore gives the same cost on each nonzero triple,

`C_3 |det A_m[S,S]|^(-1/3)=C_3 m`.                                 (5.4)

The exact Pluecker weights are

`w_S=m^(-3)`                                                        (5.5)

on those `m^3` triples and zero elsewhere, so Cauchy--Binet volume sampling has total mass one. But its weighted average of the local reciprocal-determinant bounds is

`sum_S w_S C_3 w_S^(-1/3)
 = C_3 sum_S w_S^(2/3)
 = C_3 m`.                                                          (5.6)

Thus the most natural linear Cauchy--Binet averaging of the local determinant theorem diverges linearly in `m`, even though the actual output density is at most `2 pi` and the grouped partner application is bounded by `<209`.

Indeed, under the volume-sampling law all nonzero sampled triples have the identical local cost `C_3 m`; hence **every positive moment** of that sampled local cost also grows like `m`. The failure is therefore not repaired by replacing the mean by any positive `L^p` average of the same reciprocal local bounds.

This is an obstruction only to that aggregation mechanism, not to QFORM.

## 6. What this proves about projection-product interaction

The theorem supplies a fully source-valid bridge from bounded-density product projections to a curved quadratic pushforward:

1. first compress disjoint original-coordinate banks by normalized linear projections;
2. spend the Rogozin--Ball bound once per bank, obtaining independent bank variables with cap `sqrt(2)`;
3. only then use the rank-three quadratic determinant geometry;
4. select/pay a determinant at the **bank level**, where Cauchy--Binet mass is no longer diluted by within-bank multiplicity.

The stress family proves that reversing steps 1 and 4 can lose an arbitrarily large factor.

The theorem also makes the unresolved structural quantity explicit. For an exact-rank-three spectral frame, a bounded number of row directions, or more generally a bank decomposition with `w_*` bounded below, is enough. The bare three-large-eigenvalue hypothesis does **not** supply such a finite row-direction decomposition. Generic diffuse frames may have many non-collinear row directions, and normalizing arbitrary spectral fibers is forbidden by the live corrections.

For matrices with additional spectral components, another genuine debt remains: compressing only the chosen three-dimensional large eigenspace does not make the complementary quadratic form a function of the bank variables, nor independent of them. Deleting it, conditioning on overlapping spectral projections, or taking a normalized conditional-density supremum would revive refuted mechanisms.

## 7. First unpaid full-target implication

A target-level continuation must replace exact line banks by a source-valid **approximate/grouped bank transducer** which either

- produces finitely many disjoint original-coordinate bank variables while controlling the full residual quadratic interaction, or
- routes the non-line-bank residual into an already proved ridge/full-matrix-pair branch,

without normalizing thin spectral fibers and without first paying reciprocal physical minors.

The exact adaptive quantity suggested by this run is `w_*` after legitimate product-bank compression, not the maximum physical Pluecker atom before compression.

## 8. Status

`QFORM-FINITE-LINE-BANK-COMPRESSION-v1`: **PROVED**, conditional only on the pinned scalar projection theorem and the pinned completed fleet03/B16 physical-triple determinant theorem.  
`QFORM-PHYSICAL-PLUECKER-VOLUME-AVERAGING-v1`: **REFUTED AS A UNIVERSAL AGGREGATION MECHANISM** by (5.1)--(5.6).  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Continuity: **NOT established by this run**.
