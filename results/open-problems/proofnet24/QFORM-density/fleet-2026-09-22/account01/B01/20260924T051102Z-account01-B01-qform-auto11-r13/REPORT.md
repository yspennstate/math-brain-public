SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-24T05:11:02Z.
attacking: tiny-currency aggregation in the finite-leak survivor; aggregate many weak physical star edges before inversion and close the full diagonal-plus-star Schur branch without scalar pointwise Fresnel decay.

# Star-dispersion half-Riesz aggregation and a scale-free diagonal-plus-star compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T051102Z-account01-B01-qform-auto11-r13`  
Role: account01/B01, Oscillatory replacement  
Status: **PROVED SUPPORTING THEOREMS / FULL QFORM OPEN / INDEPENDENT REVIEW PENDING**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and correction boundary

The full owner target remains open: for arbitrary independent real coordinates with densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal `L^infinity` bound for the density of `X^T A X`, or give a valid counterexample. Continuity of the full-target density is a separate open requirement.

This report keeps every variable used in conditioning/completion as an ORIGINAL independent coordinate. No Gaussianity, moment, support, log-concavity, connected-support, or post-rotation independence assumption is made.

The phase-aligned fragmented-support counterexample remains binding: no law-uniform pointwise estimate

`|E exp(i t X^2)| <= C |t|^{-alpha}`

with `alpha>0` is asserted. The argument below uses only joint averaged-frequency estimates in one physical hub variable, direct fractional-potential inversion, and exact Schur identities.

Source-pinned premises actually used:

1. **Designated partner, newest completed account02/B01 theorem available at the start of this run:** `QFORM-STAR-EDGE-TAIL-HALFRIESZ-v1`,
   `yspennstate/math-open-problems@c4b014741e90e63a6890920d3f1f8b17747f6797`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260924T040416Z-account02-B01-qform-auto11-r43/REPORT.md`.
   Its equation (2.9), applied to an arbitrary nonempty leaf group with slope vector `c_G`, gives

   `||G_{G,t}||_2^2 <= sqrt(2) pi / (|t| ||c_G||_2)`.

   The proof retains arbitrary diagonal quadratic phases and affine terms on the leaves.

2. **Orientation-free physical-pair half-Riesz theorem:**
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`:

   `H_{1/2}(Z^T Lambda Z + ell^T Z + c) <= 128 |det Lambda|^{-1/4}`

   for every invertible symmetric physical `2 x 2` matrix `Lambda`, arbitrary affine term, and two independent cap-one coordinates.

3. **Previous account01/B01 any-sign two-pivot receiver and square peel:**
   `yspennstate/math-open-problems@5a750c5b1188ea297a92c01b9692de5d87ab7f4c`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260924T041020Z-account01-B01-qform-auto11-r12/REPORT.md`.
   If `s_3(A)>=s>0` and an ORIGINAL physical pair has first LDL pivot `a!=0` and second pivot `d!=0`, then

   `||p_Q||_infinity <= C_2 |a|^{-1/2}|d|^{-2/5}s^{-1/10}`,

   with `C_2=27.2653244653667...`. The dependence-safe square peel is

   `||p_{a(X_0+h)^2+R}||_infinity <= |a|^{-1/2} H_{1/2}(R)`.

All source claims are used only in these stated scopes.

## 2. First essential implication: aggregate a whole star before paying reciprocals

Let `H,Y_1,...,Y_m` be independent ORIGINAL coordinates with probability densities bounded by one. Consider

`R = d H^2 + sum_i (d_i Y_i^2 + 2 c_i H Y_i)
     + ell_H H + sum_i ell_i Y_i + q_0`,                         (2.1)

where all real coefficients are arbitrary. Put

`C^2 = sum_i c_i^2`,
`c_* = max_i |c_i|`,
`E_star = C^4 - c_*^4`.                                        (2.2)

The quantity `E_star` is positive exactly when at least two star edges are nonzero. It measures dispersion of the squared edge mass away from a single physical leaf.

### Theorem 2.1 — `QFORM-STAR-DISPERSION-HALFRIESZ-v1`

If `E_star>0`, then

`boxed:
 H_{1/2}(R):=sup_s E|R-s|^{-1/2}
 <= 8 E_star^{-1/8}.`                                          (2.3)

This keeps arbitrary hub curvature `d`, arbitrary diagonal leaf curvature `d_i`, and all affine terms.

### Proof

Choose a partition of the leaves into two nonempty sets `P,Q`. Set

`C_P=(sum_{i in P} c_i^2)^{1/2}`,
`C_Q=(sum_{i in Q} c_i^2)^{1/2}`.                              (2.4)

For `t!=0`, condition only through the literal hub value `H=h`. Ignoring the hub-only unimodular factor, the conditional characteristic function is a product

`F_t(h) G_t(h)`,                                                (2.5)

where `F_t` uses leaves in `P` and `G_t` uses leaves in `Q`. Since the density of `H` is bounded by one,

`|phi_R(t)| <= int |F_t(h)G_t(h)| dh
             <= ||F_t||_2 ||G_t||_2`.                          (2.6)

Apply the completed account02/B01 grouped-leaf `L^2` estimate separately to the two groups. It gives

`||F_t||_2^2 <= sqrt(2) pi/(|t| C_P)`,
`||G_t||_2^2 <= sqrt(2) pi/(|t| C_Q)`.                          (2.7)

Therefore

`boxed:
 |phi_R(t)|
 <= min{1, sqrt(2) pi (C_P C_Q)^{-1/2}|t|^{-1}}.`              (2.8)

This is the averaged-frequency replacement: the critical `1/|t|` is generated jointly by two independent physical leaf groups. It is not a pointwise Fresnel estimate for any scalar quadratic phase.

Use the already proved fractional-potential Fourier interface

`H_{1/2}(R)
 <= (2pi)^{-1/2} int_R |t|^{-1/2}|phi_R(t)| dt`.               (2.9)

For `K>0`,

`int_R |t|^{-1/2} min(1,K/|t|) dt = 8 sqrt(K)`.                (2.10)

With `K=sqrt(2) pi (C_P C_Q)^{-1/2}`, equations (2.8)-(2.10) give

`H_{1/2}(R)
 <= 2^(11/4) (C_P C_Q)^{-1/4}.`                                (2.11)

It remains to choose the partition without paying one tiny edge. Let

`w_i=c_i^2`, `W=sum_i w_i=C^2`, `m=max_i w_i=c_*^2`.           (2.12)

Order the weights arbitrarily and take partial sums until first crossing `W/2`. One of the two adjacent partial sums lies within `m/2` of `W/2`. Thus there is a subset `P` with

`|sum_{i in P}w_i-W/2| <= m/2`.                                (2.13)

Writing `x=sum_{i in P}w_i`,

`x(W-x)
 >= W^2/4-m^2/4
 = (C^4-c_*^4)/4
 = E_star/4`.                                                   (2.14)

Since

`C_P C_Q = sqrt(x(W-x)) >= (1/2)E_star^{1/2}`,                 (2.15)

substitution into (2.11) yields

`H_{1/2}(R)
 <= 2^(11/4) 2^(1/4) E_star^{-1/8}
 = 8 E_star^{-1/8}`.                                           (2.16)

This proves (2.3). QED.

### Interpretation

The estimate spends the aggregate quantity `C^4-c_*^4` before taking a reciprocal. Hence a large number of individually tiny physical edges can be useful even when no single edge-tail product is target scale. The exact failure `E_star=0` localizes the entire star to one physical edge.

## 3. Scale-free closure of every diagonal-plus-star residual after a nonzero outer pivot

Now let the full quadratic matrix satisfy

`s_3(A) >= 1`.                                                  (3.1)

Assume an ORIGINAL coordinate has nonzero physical pivot `a=A_00`. Complete that literal coordinate exactly:

`Q = a(X_0+h(Z))^2 + R(Z)`,                                    (3.2)

and let the residual Schur matrix be a diagonal-plus-one-star matrix

`S = [[d,c^T],[c,D]]`,
`D=diag(d_1,...,d_m)`.                                         (3.3)

No size assumption is imposed on `a`, the star coefficients, or the residual diagonal coefficients.

### Theorem 3.1 — `QFORM-OUTER-PIVOT-DIAGONALSTAR-SCALEFREE-v1`

Every form satisfying (3.1)-(3.3) has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= C_star |a|^{-1/2},
 C_star = 128(16/3)^(1/4)
        = 194.5179355268077... .`                               (3.4)

No continuity assertion is made for arbitrary merely measurable input densities.

### Proof

Write the full matrix in block form before completion,

`A=[[a,r^T],[r,C_0]]`,
`S=C_0-r r^T/a`.                                                (3.5)

There is the exact rank-one decomposition

`A = (1/a) [a;r][a;r]^T + diag(0,S)`.                           (3.6)

The first term has rank one. The singular-value rank perturbation inequality therefore gives

`s_3(A) <= s_2(S)`.                                             (3.7)

Hence

`s_2(S)>=1`.                                                    (3.8)

We use the fixed threshold `tau=1/4`.

### Case A: a residual literal diagonal is not tiny

Suppose

`max(|d|,max_i|d_i|) >= 1/4`.                                  (3.9)

Choose a residual original coordinate `k` with `|S_kk|>=1/4`. The ORIGINAL physical pair `{0,k}` in the full matrix has first LDL pivot `a`, and its second LDL pivot is exactly `S_kk`, because

`det A[{0,k}] = a S_kk`.                                       (3.10)

Apply the preceding any-sign two-pivot receiver with `s=1`:

`||p_Q||_infinity
 <= C_2 |a|^{-1/2}|S_kk|^{-2/5}
 <= C_2 4^(2/5)|a|^{-1/2}`                                    (3.11)

and

`C_2 4^(2/5)=47.4716871435532... < C_star`.                    (3.12)

### Case B: all residual diagonals are tiny

Assume instead

`|d|<1/4`, `|d_i|<1/4` for all `i`.                             (3.13)

Let

`B=[[0,c^T],[c,0]]`,
`E=diag(d,d_1,...,d_m)`,
`S=B+E`.                                                        (3.14)

The only nonzero singular values of the pure star `B` are

`s_1(B)=s_2(B)=C:=||c||_2`.                                    (3.15)

Since `||E||<1/4`, Weyl's singular-value inequality and (3.8) imply

`C >= s_2(S)-||E|| > 3/4`.                                     (3.16)

Put `c_*=max_i|c_i|` and `E_star=C^4-c_*^4`.

#### Case B1: diffuse enough star currency

If

`E_star >= 65/256`,                                             (3.17)

Theorem 2.1 gives

`H_{1/2}(R)
 <= 8(65/256)^(-1/8)
 = 9.49523708588021...`.                                       (3.18)

The outer square peel yields

`||p_Q||_infinity
 <= 9.49523708588021... |a|^{-1/2}`.                           (3.19)

#### Case B2: exterior star currency is concentrated

Suppose

`E_star < 65/256`.                                              (3.20)

From (3.16),

`C^4 > (3/4)^4 = 81/256`,                                      (3.21)

so

`c_*^4 = C^4-E_star > 16/256=1/16`,
`c_*^2>1/4`.                                                    (3.22)

Choose a leaf `j` with `|c_j|=c_*`. Condition every other residual coordinate. The remaining two-coordinate quadratic matrix is

`Lambda=[[d,c_j],[c_j,d_j]]`.                                  (3.23)

By (3.13) and (3.22),

`|det Lambda|
 = |d d_j-c_j^2|
 >= c_j^2-|d d_j|
 > 1/4-1/16
 = 3/16`.                                                       (3.24)

The orientation-free physical-pair half-Riesz theorem therefore gives, uniformly in all conditioned values,

`H_{1/2}(R)
 <= 128(3/16)^(-1/4)
 = 128(16/3)^(1/4)
 = C_star`.                                                     (3.25)

The outer square peel proves (3.4). QED.

### What this closes

After one nonzero original scalar completion, **every residual diagonal-plus-one-star geometry is paid with a universal constant independent of the number of leaves and of all star/diagonal coefficients**. The only remaining dependence is the unavoidable explicit outer-pivot factor `|a|^{-1/2}`.

The theorem removes the partner's qualitative `almost single edge` obstruction inside this star normal form: either many edges aggregate through `E_star`, a residual diagonal is usable through a second original pivot, or concentration forces a uniformly invertible physical hub-leaf pair.

## 4. Actual application of the completed designated partner theorem

The completed account02/B01 theorem in source item 1 applies to the full-target family

`Q_* = X_0^2 + 2H(U+V/2)`.                                    (4.1)

Its coefficient matrix has spectrum

`{-sqrt(5)/2, 0, 1, sqrt(5)/2}`,                               (4.2)

so exactly three eigenvalues have modulus at least one. In the partner theorem,

`a=1`, `beta=1`, `C_tail=1/2`.                                 (4.3)

Therefore the actual inequality is

`boxed:
 ||p_{Q_*}||_infinity
 <= 2^(21/8)(1/2)^(-1/4)
 = 2^(23/8)
 = 7.33603234563737... .`                                      (4.4)

This run uses the same completed partner result more essentially in (2.7): its grouped-leaf `L^2` estimate is applied twice, once to each side of the balanced partition, producing the new aggregate theorem (2.3).

For comparison, Theorem 2.1 itself applies to (4.1) with slopes `(1,1/2)`. Here

`C^2=5/4`, `c_*^2=1`,
`E_star=(5/4)^2-1=9/16`,                                       (4.5)

and hence

`H_{1/2}(2H(U+V/2))
 <= 8(9/16)^(-1/8)
 = 8.59655945458834...`.                                       (4.6)

The designated partner's heavy-edge/tail orientation is sharper on this two-edge example, while the new theorem is permutation-free and aggregates arbitrarily many weak edges.

## 5. Why this does not contradict the phase-aligned counterexample

The false scalar statement tries to control a single transform

`E exp(i t X^2)`

pointwise for every cap-one law. Nothing in Sections 2-3 does that. Equation (2.8) is obtained only after integrating the physical hub variable and applying two independent bank `L^2` budgets. The subsequent `|t|^{-1/2}`-weighted time integral is a fractional-potential identity. Thus phase-aligned fragmented supports remain valid counterexamples to the rejected scalar mechanism.

## 6. Remaining implication

The full conjecture is **OPEN**. The full continuity claim is **OPEN**.

This run removes the diagonal-plus-star residual as a qualitative obstruction once one original scalar pivot is nonzero. The first unpaid quantitative implication is now:

`QFORM-FINITELEAK-OUTER-PIVOT-AGGREGATION-v2`:

> Under `s_3(A)>=1`, in the remaining finite-leak structural decomposition, avoid paying `|a|^{-1/2}` when every available literal outer scalar pivot is tiny or zero. Force a target-scale pair/grouped/cross-volume currency, or aggregate the many tiny physical pivots/edges before inversion. Retain non-star residual curvature and every nonzero collar; do not delete a small random quadratic tail.

The new star theorem can be inserted as a terminal receiver whenever a Schur branch is diagonal-plus-one-star. It does not prove that an arbitrary full target matrix reaches such a branch with `|a|` bounded below.

## 7. Status

- `QFORM-STAR-DISPERSION-HALFRIESZ-v1`: proved here, pending independent review.
- `QFORM-OUTER-PIVOT-DIAGONALSTAR-SCALEFREE-v1`: proved here, pending independent review.
- Full QFORM theorem: OPEN.
- Full-target continuity: OPEN.
- Phase-aligned scalar pointwise-decay counterexample: preserved.
- Native brain receiver use: not verified; execution remains `WITHOUT_VERIFIED_BRAIN`.
