SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-23T07:06:24Z.
attacking: coarse overlap-role coloring of the full third compound, then a determinant-marginal core-or-diffuse dichotomy without selecting one tiny minor.

# fleet01/B07 r19 — coarse role coloring and a spectral E3 core-or-diffuse theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** coordinate minor selection / GEOMETRY  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW COARSE ROLE-COLORING + CORE-OR-DIFFUSE REDUCTION / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction boundary

The target is the unrestricted statement: for every dimension, every independent real original-coordinate input with one-dimensional probability density bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a universally bounded density, or produce a target-valid counterexample. No moment, support, Gaussian, log-concavity, iid, connected-support, or post-rotation product hypothesis is introduced. Continuity is a separate desired conclusion.

This run uses no law-uniform pointwise van-der-Corput decay, no arbitrary-joint rank-three coarea estimate, no conditional projected-density positive moment, no post-rotation independence, and no reciprocal extraction of one small coordinate minor. The previous several B07 runs used anchored Schur/rank-tail ratios; this run deliberately changes mechanism to a coarse overlap-role coloring of the entire third compound.

Sources actually used:

1. Fleet02/B07, `QFORM-DETERMINANT-MARGINAL-TAIL-CORE-v1`, canonical source `yspennstate/math-open-problems@1f5ab2ddba6e99675fb9177666c5e64e396e54e5`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260923T023322Z-r11/REPORT.md`. Its exact structural implication is applied in Section 5 below.
2. Fleet03/B07, `QFORM-THIRD-COMPOUND-OVERLAP-COLORING-v1`, canonical source `yspennstate/math-open-problems@391688138f7f481a2c8688c2d27f9508db7af6af`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T000734Z-fleet03-B07-qform-r20/REPORT.md`. I use it only as a comparison point: its finer positional coloring is stronger for receivers that need six/five/four/three distinct subbanks, while the new coarse coloring below keeps much more determinant mass when a receiver only needs disjoint structural roles.

## 2. The full third-compound currency

For `h=0,1,2,3`, define the overlap component

`W_h(A) = sum_{|R|=|C|=3, |R intersect C|=h} det A[R,C]^2`.

Since `A` is symmetric, its singular values are the absolute eigenvalues. Cauchy--Binet/exterior algebra gives

`sum_{h=0}^3 W_h(A)
 = || wedge^3 A ||_F^2
 = e_3(A^2)
 = sum_{i<j<k} lambda_i^2 lambda_j^2 lambda_k^2.`                 (2.1)

If at least three eigenvalues have modulus at least one, one summand in (2.1) is at least one, so

`sum_h W_h(A) >= 1.`                                               (2.2)

Therefore at least one overlap class satisfies

`W_h(A) >= 1/4.`                                                    (2.3)

Everything below is performed on that active class. The objective is to retain determinant *mass* rather than to choose one minor.

## 3. `QFORM-COARSE-ROLE-COLORING-v1`

The fine positional coloring splits the three row positions and three column positions into separate banks. That is useful when a later receiver requires coordinatewise separation, but it spends a large combinatorial factor. For determinant-volume and marginal-tail receivers, only the structural roles matter. Coloring by those roles gives the following stronger mass statement.

### h=0: disjoint row and column triples

Color every physical coordinate independently `R` or `C` with probabilities `1/2,1/2`. A fixed disjoint pair of triples is retained if all three row coordinates receive `R` and all three column coordinates receive `C`, probability

`c_0 = 2^(-6) = 1/64.`                                             (3.1)

Hence some coloring gives disjoint physical banks `R,C` with packet

`P_0 = sum_{I subset R, J subset C, |I|=|J|=3} det A[I,J]^2
     >= W_0/64.`                                                    (3.2)

### h=1: one shared coordinate

Use three pairwise disjoint roles `S,R,C`. Give probabilities

`p_S=1/5,  p_R=p_C=2/5.`                                           (3.3)

A fixed pair of triples with one shared coordinate and two row-only/two column-only coordinates is retained with probability

`c_1 = (1/5)(2/5)^4 = 16/3125.`                                   (3.4)

Thus some disjoint role banks `S,R,C` satisfy

`P_1 = sum_{s in S, I in binom(R,2), J in binom(C,2)}
          det A[{s} union I,{s} union J]^2
     >= (16/3125) W_1.`                                            (3.5)

### h=2: two shared coordinates

Again use roles `S,R,C`, now with

`p_S=1/2,  p_R=p_C=1/4.`                                           (3.6)

A fixed overlap-two pair is retained with probability

`c_2=(1/2)^2(1/4)(1/4)=1/64.`                                     (3.7)

Hence some disjoint role banks satisfy

`P_2 = sum_{H in binom(S,2), r in R, c in C}
          det A[H union {r},H union {c}]^2
     >= W_2/64.`                                                    (3.8)

### h=3: principal triples

No coloring is needed. Put

`P_3=W_3,  c_3=1.`                                                  (3.9)

### Why the probabilities above are optimal for this coarse scheme

For `h=1,2`, a role coloring with probabilities `p_S,p_R,p_C` retains a fixed overlap-h minor pair with probability

`p_S^h p_R^(3-h) p_C^(3-h)`,                                      (3.10)

subject to `p_S+p_R+p_C=1`. By symmetry at the maximizer `p_R=p_C`; the logarithmic Lagrange equations give

`p_S=h/(6-h),  p_R=p_C=(3-h)/(6-h)`.                              (3.11)

These are exactly (3.3) and (3.6). The `h=0` endpoint gives `p_R=p_C=1/2`; `h=3` needs no split.

### Proof of the selection statements

Each squared determinant is nonnegative. Under the corresponding independent random coloring, the expectation of the retained packet is exactly `c_h W_h`. Therefore at least one coloring has retained mass at least that expectation. No determinant is inverted or selected, and no transformation of the random variables is made. QED.

Combining (2.3) with (3.2)--(3.9), one of the following four original-coordinate packets exists:

`h=0: P_0 >= 1/256`,
`h=1: P_1 >= 4/3125`,
`h=2: P_2 >= 1/256`,
`h=3: P_3 >= 1/4.`                                                 (3.12)

For comparison, the fine positional coloring of fleet03/B07 gives target-level masses `1/5184, 1/3125, 1/512, 1/18`. Thus, when only coarse structural roles are required, (3.12) improves the retained determinant currency by factors `20.25, 4, 2, 4.5`, respectively. This is not a dominance claim: the fine theorem supplies extra positional bank separation that some analytic receivers may need.

## 4. Exact Schur ledgers survive the coarser packets

The new mass gain is compatible with the existing Schur identities and still avoids a best-pivot selection.

### One shared coordinate

For `s in S` with `a_s=A_ss !=0`, let `S_s` be the exact scalar Schur complement after pivoting only the original physical coordinate `s`. For every retained pair of residual two-sets `I subset R`, `J subset C`,

`det A[{s} union I,{s} union J] = a_s det S_s[I,J].`               (4.1)

Consequently

`P_1 = P_(1,zero)
      + sum_{s in S: a_s !=0} a_s^2 E_2(S_s[R,C]),`                (4.2)

where `P_(1,zero)` denotes the exact-zero shared-coordinate part and `E_2(M)` is the squared second-compound Frobenius mass. On the active h=1 branch, either

`P_(1,zero) >= 2/3125`                                             (4.3)

or the genuine scalar-Schur weighted currency in (4.2) is at least `2/3125`.

### Two shared coordinates

For `H in binom(S,2)` with invertible physical principal block `B_H=A[H,H]`, let `S_H` be its exact Schur complement. Then

`det A[H union {r},H union {c}] = det(B_H) S_H[r,c].`              (4.4)

Therefore

`P_2 = P_(2,singular)
      + sum_{H in binom(S,2): det B_H !=0}
          det(B_H)^2 ||S_H[R,C]||_F^2.`                            (4.5)

On the active h=2 branch, either

`P_(2,singular) >= 1/512`                                         (4.6)

or the invertible pair-Schur first-compound currency in (4.5) is at least `1/512`.

Equations (4.2) and (4.5) are exact bookkeeping identities. They do not authorize reciprocating one small `a_s` or `det B_H`.

## 5. `QFORM-SPECTRAL-E3-COARSE-CORE-OR-DIFFUSE-v1`

Now apply the designated partner fleet02/B07 theorem to the active packet from (3.12).

Normalize its determinant-square weights to a probability law on physical row/column triples. Let

`alpha_i = P(i belongs to the row triple)`,
`beta_j  = P(j belongs to the column triple)`.

Always

`sum_i alpha_i = sum_j beta_j = 3.`                                (5.1)

Define the heavy physical row and column supports at the threshold `3/5`:

`R_0={i: alpha_i>3/5},  C_0={j: beta_j>3/5}.`                      (5.2)

Because of (5.1), each support contains at most four coordinates. Define determinant-marginal tails

`delta_R=sum_{i notin R_0} alpha_i`,
`delta_C=sum_{j notin C_0} beta_j.`                                (5.3)

There are two cases.

### Core case

If

`delta_R+delta_C <= 1/2`,                                         (5.4)

the partner theorem `QFORM-DETERMINANT-MARGINAL-TAIL-CORE-v1` gives directly

`Z_3(A[R_0,C_0]) >= (1-delta_R-delta_C) P_h >= P_h/2,`             (5.5)

where

`Z_3(M)=sum_{|I|=|J|=3} det M[I,J]^2=e_3(MM^T).`

Thus a physical at-most-`4 x 4` row/column core contains a fixed amount of third-compound mass. From (3.12), the guaranteed core masses are

`h=0: Z_3 >= 1/512`,
`h=1: Z_3 >= 2/3125`,
`h=2: Z_3 >= 1/512`,
`h=3: Z_3 >= 1/8.`                                                 (5.6)

The row and column supports can overlap, but their union always contains at most eight original coordinates (and in the principal h=3 case the two marginal laws coincide).

### Diffuse case

Suppose instead

`delta_R+delta_C > 1/2.`                                          (5.7)

For a random determinant-weighted minor pair `(I,J)` in the packet put

`Y=|I\R_0|+|J\C_0|.`                                               (5.8)

Then `0<=Y<=6` and

`E Y=delta_R+delta_C>1/2.`                                        (5.9)

Since `E Y <= 6 P(Y>=1)`,

`P(Y>=1)>1/12.`                                                    (5.10)

Therefore more than `P_h/12` of the *original determinant-square packet* uses at least one light physical coordinate. Quantitatively,

`h=0: light packet > 1/3072`,
`h=1: light packet > 1/9375`,
`h=2: light packet > 1/3072`,
`h=3: light packet > 1/48.`                                       (5.11)

This is the desired actual application of the completed fleet02/B07 result: the spectral hypothesis first supplies a constant coarse determinant bank, then the partner marginal-tail theorem converts it into either a bounded physical core with half the bank mass or a quantitatively nontrivial support-diffuse determinant packet. At no point is a single coordinate minor selected or divided by.

## 6. What this does and does not prove

The theorem above is a dimension-free coordinate-selection statement under the *bare* three-large-eigenvalue hypothesis. It requires no no-pivot assumption, no moment information and no localization hypothesis. It also improves the determinant currency available to any later aggregate receiver that only needs the coarse overlap roles.

It does **not** prove the full QFORM conjecture. A bounded `4 x 4` third-compound mass alone does not, without additional scale/control, automatically give a uniformly conditioned symmetric principal block; and in the diffuse branch arbitrary same-bank quadratic curvature is still present. The false one-minor route cannot be resurrected by choosing the largest term of (5.11).

The first unpaid implication is therefore

`QFORM-COARSE-DIFFUSE-ROLE-RECEIVER-v1`:

> Starting from one of the four coarse role packets (3.12) in the diffuse alternative (5.11), obtain a product-preserving density or half-Riesz estimate while retaining arbitrary same-bank curvature and all extra spectrum, by averaging the determinant currency before any reciprocal pivot/minor operation. In the core alternative, route (5.6) through a scale-stable finite-coordinate receiver without silently assuming an operator-norm upper bound.

The fine positional coloring remains available whenever the analytic receiver needs more independent subbanks; the new coarse theorem should be used first when only aggregate volume/marginal information is consumed.

Full QFORM remains OPEN. No new global continuity conclusion is claimed in this run.

## 7. Verification

A supporting finite checker (saved beside this report) verifies on random symmetric matrices that `sum_h W_h=e_3(A^2)` numerically, brute-forces all coarse colorings on small dimensions to check the expectation lower bounds, and records the exact fractions in (3.12), (5.6), and (5.11). These computations are regression checks only; the proof is the analytic argument above.
